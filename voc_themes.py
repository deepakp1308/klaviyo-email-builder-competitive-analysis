"""Classify VOC records into themes (Bug / Barrier / Missing Feature) and aggregate MRR.

Output:
  voc_themes.json — structured data ready for HTML rendering
  voc_themes_report.md — human-readable summary for sanity check
"""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
INP = ROOT / "voc_emailbuilder.json"
OUT_JSON = ROOT / "voc_themes.json"
OUT_MD = ROOT / "voc_themes_report.md"

# Theme rules: ordered (first match wins). Each rule = (category, theme, regex)
# Categories: bug | barrier | missing
# Coverage tuned by inspecting unclassified records iteratively.
RULES = [
    # ---------- BUGS (something is broken / unexpected behavior) ----------
    ("bug", "Block reordering / lost layout",
        r"(rearrang|reorder|moves|jumps|order.*chang|wrong order|flip|switch.*order|"
        r"layout (?:got|is) (?:lost|messed|broken)|"
        r"shuffl(?:e|ed|es))"),
    ("bug", "Autosave / lost work",
        r"\b("
        r"lost\s+(?:my|all|the)\s+(?:work|edits?|changes?|content|email|template|design)|"
        r"didn'?t\s+save|did\s+not\s+save|"
        r"autosave|auto-?save|"
        r"save\s+button|"
        r"work\s+disappeared|edits?\s+disappeared|"
        r"editor\s+(?:crashed|froze|frozen|hung|hangs)"
        r")\b"),
    ("bug", "Editor performance / lag / browser freeze",
        r"\b("
        r"(?:editor|builder|page|template|site|content\s+studio)\s+is\s+(?:so\s+)?(?:slow|laggy|unresponsive)|"
        r"slow\s+(?:editor|builder|to\s+load)|"
        r"very\s+laggy|laggy\s+(?:editor|builder|template)|"
        r"unresponsive\s+(?:when|while|after)|"
        r"browser\s+(?:freez|crash|hang)|freezes?\s+(?:my\s+)?browser|"
        r"upload\s+image\s+is\s+slow|"
        r"can'?t\s+use\s+the\s+editor|loading\s+forever"
        r")\b"),
    ("bug", "Image upload / cropping / resize",
        r"(image (?:won'?t|cannot|can'?t|doesn'?t) (?:upload|load|insert|crop|resize|appear|show|display)|"
        r"upload(?:ed)? .*(?:fail|error|broken)|"
        r"crop(?:ping)? (?:bug|broken|issue|problem|doesn'?t)|"
        r"resize\s+(?:bug|broken|issue|doesn'?t)|"
        r"file\s+manager|content\s+studio.*(?:bug|broken|error|issue))"),
    ("bug", "Text formatting / fonts / spacing",
        r"(font\s+(?:color|size|change|family|won'?t|doesn'?t|reverts)|"
        r"text\s+(?:color|formatting|won'?t|doesn'?t|reverts)|"
        r"spacing\s+(?:issue|bug|broken|problem|wrong)|"
        r"line\s+spacing|line-?height|"
        r"alignment\s+(?:issue|wrong|broken)|"
        r"bold|italic|underline.*(?:bug|broken|won'?t))"),
    ("bug", "Mobile preview / responsiveness",
        r"(mobile\s+(?:preview|view|render|display|version)\s*(?:bug|broken|wrong|doesn'?t)|"
        r"responsive\s+(?:bug|broken|issue|problem)|"
        r"renders?\s+differently|render(?:ing)?\s+(?:bug|broken|wrong)|"
        r"looks\s+(?:bad|wrong|broken)\s+on\s+mobile)"),
    ("bug", "Block/section misc bugs",
        r"(block (?:disappear|missing|won'?t|broken|stuck)|"
        r"section\s+(?:disappear|missing|broken|stuck)|"
        r"button\s+(?:doesn'?t|won'?t|missing|broken)|"
        r"divider\s+(?:bug|broken|won'?t)|"
        r"can'?t\s+delete\s+block|can'?t\s+edit\s+block|"
        r"duplicat(?:e|ing).*block.*(?:bug|broken|doesn'?t))"),
    ("bug", "Hyperlink / button URL / link won't remove",
        r"(hyperlink|link\s+(?:button|broken|won'?t|doesn'?t)|"
        r"insert\s+link|button\s+(?:link|url)|"
        r"remove\s+the\s+link|link\s+keeps\s+(?:popping|appearing)|"
        r"link.*(?:doesn'?t\s+work|broken|missing|keeps\s+popping))"),
    ("bug", "Preview / test send mismatch",
        r"(preview\s+(?:doesn'?t|wrong|different|mismatch)|"
        r"test\s+(?:email|send)\s+(?:looks|appears|renders).*(?:different|wrong|doesn'?t)|"
        r"what\s+you\s+see\s+isn'?t)"),
    ("bug", "Code / HTML editor",
        r"(html\s+(?:code|block|editor)\s+(?:bug|broken|won'?t|doesn'?t)|"
        r"code\s+view\s+(?:bug|broken|missing)|"
        r"source\s+code|raw\s+html)"),

    # ---------- BARRIERS (friction, confusion, complexity, doable but painful) ----------
    ("barrier", "Steep learning curve / confusing UX",
        r"(confusing|confused|hard\s+to\s+(?:figure|use|understand)|"
        r"not\s+intuitive|unintuitive|"
        r"learning\s+curve|takes\s+(?:weeks|months)\s+to\s+learn|"
        r"difficult\s+to\s+(?:use|navigate|find)|"
        r"can'?t\s+find|where\s+(?:is|did))"),
    ("barrier", "UI churn / new builder dislike / 'bring back the old'",
        r"(everything\s+(?:keeps|always)\s+changing|"
        r"changed\s+(?:again|the\s+UI|the\s+interface)|"
        r"redesign(?:ed)?|why\s+did\s+you\s+change|"
        r"used\s+to\s+(?:be|work|have)|bring\s+back|"
        r"old\s+(?:editor|builder|version|designer)|"
        r"old\s+one\s+(?:was|is)\s+better|"
        r"don'?t\s+like\s+the\s+new|"
        r"hate\s+the\s+(?:new|update)|"
        r"new\s+(?:builder|designer|editor).*(?:clunky|bad|worse|hate|don'?t\s+like|incredibly\s+different)|"
        r"(?:brown|grey)\s+(?:designer|editor))"),
    ("barrier", "Switching between views / tabs / modes",
        r"(switch(?:ing)?\s+between|toggling\s+between|"
        r"jumping\s+between|going\s+back\s+and\s+forth|"
        r"too\s+many\s+(?:clicks|steps|tabs)|"
        r"can'?t\s+see\s+both|side\s+by\s+side)"),
    ("barrier", "Time wasted iterating / preview-edit loop",
        r"(test\s+preview.*edit.*(?:try\s+again|over|again)|"
        r"keep\s+(?:editing|trying|iterating)|"
        r"trial\s+and\s+error|"
        r"so\s+many\s+(?:steps|clicks)|"
        r"too\s+much\s+time)"),
    ("barrier", "Brand consistency / brand kit setup",
        r"(brand\s+(?:kit|style|consistency|guidelines)\s+(?:hard|confusing|missing|limited)|"
        r"can'?t\s+(?:save|set)\s+brand|"
        r"applying\s+brand\s+style|"
        r"colors?\s+keep\s+resetting)"),
    ("barrier", "Saved templates / content discovery",
        r"(can'?t\s+find\s+(?:my|saved|the)\s+(?:template|content|block)|"
        r"saved\s+template.*(?:lost|missing|hard\s+to\s+find)|"
        r"organize\s+(?:templates|saved|blocks)|"
        r"folders?\s+for\s+(?:templates|saved))"),

    # ---------- MISSING FEATURES (would-be-nice / explicit asks) ----------
    ("missing", "Universal saved content / global blocks",
        r"(universal\s+content|global\s+block|edit\s+once.*(?:everywhere|all|update\s+all)|"
        r"shared\s+(?:block|content|footer|header)|"
        r"update.*all.*emails?\s+at\s+once)"),
    ("missing", "AI generative / AI image / AI layout",
        r"(generate.*email|AI\s+generate|AI\s+(?:built|create|design|layout)|"
        r"AI\s+image|image\s+AI|AI\s+remix|generative\s+ai|"
        r"better\s+ai|need\s+ai|wish\s+ai|missing\s+ai|"
        r"ai\s+(?:layout|design|template))"),
    ("missing", "Brand voice / tone learning AI",
        r"(brand\s+voice|tone\s+of\s+voice|learn\s+(?:my|our)\s+(?:brand|voice|style)|"
        r"AI.*(?:brand|tone|voice))"),
    ("missing", "Dark mode / inbox preview / multi-client testing",
        r"(dark\s+mode|inbox\s+preview|inbox\s+test|email\s+on\s+acid|litmus|"
        r"render\s+across\s+(?:clients|inbox)|"
        r"how\s+it\s+looks\s+in\s+(?:gmail|outlook|apple))"),
    ("missing", "Conditional / dynamic content per segment",
        r"(conditional\s+(?:content|block)|dynamic\s+content|"
        r"show.*hide\s+(?:block|content)|"
        r"different\s+content.*(?:segment|audience|customer)|"
        r"personalize.*per\s+(?:user|customer|segment))"),
    ("missing", "Interactive / AMP / shop-in-email",
        r"(interactive\s+email|amp\s+for\s+email|amp4email|"
        r"shop\s+(?:in|inside|directly)\s+(?:email|inbox)|"
        r"poll|survey\s+in\s+email|RSVP)"),
    ("missing", "Better mobile editor / mobile-first",
        r"(mobile\s+editor|edit\s+on\s+mobile|mobile\s+app\s+editor|"
        r"mobile-?first|mobile\s+specific|edit.*from.*phone)"),
    ("missing", "Code/HTML/dev-friendly editor",
        r"(react\s+email|html\s+import|custom\s+code|"
        r"dev-?friendly|developer\s+(?:tools|access)|"
        r"liquid\s+template|jinja|django\s+tag)"),
    ("missing", "Better text/font/typography control",
        r"(more\s+font|custom\s+font|google\s+font|adobe\s+font|"
        r"line\s+height|letter\s+spacing|kerning|"
        r"better\s+(?:text|font|typography))"),
    ("missing", "Better image editor / asset management",
        r"(image\s+editor|edit\s+image\s+in[- ]place|"
        r"asset\s+library|asset\s+management|"
        r"bulk\s+image|tag\s+image)"),
    ("missing", "Drag-drop / layout flexibility (sections, columns)",
        r"(more\s+(?:layout|column|section)|"
        r"4\s+column|multi-?column|flexible\s+layout|"
        r"section.*column.*flexibilit)"),
    ("missing", "Multilingual / localization in editor",
        r"(multilingual|multiple\s+language|translation\s+in\s+email|"
        r"localiz(?:e|ation)|i18n)"),

    # ---------- ADDITIONAL RULES (added after iterating unclassified set) ----------
    ("missing", "Saved sections / saved blocks / universal content",
        r"(saved\s+section|saved\s+block|"
        r"reusable\s+(?:section|block|footer|header|element|drag)|"
        r"recreate\s+(?:our|my|the)\s+footer|"
        r"footer\s+from\s+scratch|"
        r"footer\s+library|saved\s+footer|"
        r"content\s+block\s+(?:feature|that\s+can\s+be\s+inserted|in\s+multiple\s+emails)|"
        r"updates?\s+across\s+all|update.*all\s+(?:active\s+)?emails?|"
        r"update\s+list\s+templates?|update\s+(?:from\s+email|footer).*all|"
        r"snippet|content\s+library|library\s+system)"),
    ("missing", "Snap-to-grid / spacing alignment / structured layout",
        r"(snap[\s-]?to[\s-]?(?:place|grid)|"
        r"line\s+up\s+spacing|consistent\s+spacing|structured\s+(?:email\s+)?design|"
        r"alignment\s+guide|grid\s+system|guidelines\s+for\s+spacing)"),
    ("bug", "Preview from template list / template gallery navigation",
        r"(preview.*from\s+(?:the\s+)?template\s+list|"
        r"preview\s+templates?|template\s+gallery|template\s+list|"
        r"have\s+to\s+(?:edit|open)\s+(?:the\s+)?template\s+(?:to|before)\s+preview)"),
    ("missing", "Advanced merge tag / content variables / conditional / loops",
        r"(merge\s+tag.*(?:json|object|conditional|advance|loop|item)|"
        r"json\s+(?:object|with).*(?:merge\s+tag|template)|"
        r"json\s+(?:in\s+)?merge\s+tag|"
        r"content\s+variables?|"
        r"conditional\s+merge|advanced\s+template\s+language|"
        r"liquid|jinja|loop\s+in\s+template)"),
    ("barrier", "Editor feels dated / less powerful than competitors",
        r"(klaviyo|hubspot|active\s*campaign|constant\s*contact|brevo|"
        r"compared\s+to|other\s+(?:platform|tool|provider)|"
        r"behind\s+(?:the\s+)?competition|outdated|dated\s+ui|legacy\s+feel)"),
    ("bug", "Template export / import / migration",
        r"(import\s+(?:my|the)\s+template|"
        r"export\s+template|migrate\s+template|"
        r"copy\s+template\s+(?:from|to)|"
        r"template\s+(?:lost|missing|disappeared))"),
    ("barrier", "Plan-gating / paywall on basic editor features",
        r"(only\s+(?:available|on)\s+(?:premium|standard|paid|higher\s+plan)|"
        r"locked\s+behind|paywall|"
        r"upgrade\s+(?:required|to\s+access|just\s+to)|"
        r"essential.*plan.*can'?t)"),
    ("missing", "Editor undo / redo / version history",
        r"(undo|redo|version\s+history|version(?:ing)?\s+system|versioning\s+sistem|"
        r"revision\s+history|"
        r"revert\s+to|previous\s+version|change\s+log)"),
    ("missing", "Better drag-drop / block reorder UX",
        r"(drag\s+block\s+(?:hard|difficult)|"
        r"can'?t\s+drag|hard\s+to\s+(?:drag|drop|move)\s+block|"
        r"better\s+drag(?:\s|-)?and(?:\s|-)?drop)"),
    ("bug", "Saved/draft campaign opens to wrong state",
        r"(open(?:s)?\s+(?:to\s+)?(?:wrong|empty|blank)\s+(?:state|template)|"
        r"draft\s+(?:lost|missing|disappeared)|"
        r"campaign\s+(?:lost|missing|reverted))"),
    ("missing", "Custom CSS / direct HTML editor / view full code",
        r"(custom\s+(?:css|html|code|styling)|"
        r"view\s+(?:the\s+)?(?:full|whole)\s+html|"
        r"direct\s+html\s+editor|html\s+editor\s+tool|"
        r"add\s+css|inline\s+css|stylesheet)"),
    ("missing", "AI subject line / preheader / copy assist",
        r"(subject\s+line\s+(?:generator|ai|suggestion)|"
        r"preheader|"
        r"ai.*write.*subject|"
        r"intuit\s+assist.*subject)"),
    ("barrier", "Mobile preview accuracy / what-you-see-is-not-what-you-get",
        r"(mobile.*(?:doesn'?t\s+match|differs\s+from)|"
        r"preview.*not\s+(?:accurate|matching|reliable)|"
        r"campañas?\s+lucen\s+diferente|"
        r"different\s+in\s+(?:every\s+)?email\s+client|"
        r"showing\s+up\s+differently|"
        r"editor\s+vs.*(?:inbox|bandeja)|"
        r"wysiwyg\s+(?:broken|inaccurate))"),
    ("missing", "More block types (text+button combo, social, other)",
        r"(more\s+blocks?|"
        r"new\s+block\s+types?|"
        r"text\s*\+\s*button|combined\s+block|"
        r"telegram|whatsapp\s+block|tiktok\s+block|"
        r"animation\s+(?:in\s+)?(?:template|email|block)|"
        r"animated\s+block)"),
    ("missing", "Better A/B testing / multivariate in builder",
        r"(a/?b\s+test|multivariate|split\s+test|"
        r"better\s+a/?b|test\s+facilities)"),
    ("missing", "Better post-send / editor navigation / find what was sent",
        r"(post-?send|after.*email\s+is\s+sent|"
        r"see\s+the\s+final\s+email|navigate\s+to\s+sent|"
        r"main\s+post-?activities|navigation.*improve)"),
    ("missing", "Editor consistency / new builder for journeys / one editor",
        r"(customer\s+journey.*(?:legacy|old|grey|new)\s+(?:builder|editor)|"
        r"different\s+editor\s+for\s+(?:journey|automation|flow)|"
        r"two\s+different\s+(?:editor|builder)|"
        r"unified\s+editor|one\s+editor\s+for|consistent\s+editor)"),
    ("bug", "Image editor bugs / black lines / asset rendering",
        r"(black\s+lines?|"
        r"image\s+(?:editor|tool).*(?:bug|broken|black|lines|wrong)|"
        r"editor\s+foto.*(?:nere|black|broken)|"
        r"thumbnail\s+(?:wrong|broken|missing))"),
    ("missing", "Footer customization / unsubscribe legal control",
        r"(footer\s+(?:customization|legal|unsubscribe|libraries)|"
        r"forced\s+to\s+use.*(?:footer|unsubscribe|legal)|"
        r"mentions?\s+légales|own\s+(?:STOP|unsubscribe)\s+(?:link|sms))"),
    ("barrier", "Generic 'editor is clunky / hard to use / unusable'",
        r"(clunky|"
        r"hard\s+to\s+use|"
        r"not\s+user[ -]?friendly|user-unfriendly|"
        r"too\s+many\s+inconsistencies|too\s+many\s+glitch|"
        r"pathetic|terrible\s+(?:tool|editor|builder)|"
        r"awful\s+(?:tool|editor|builder)|"
        r"unusable)"),
]

CATEGORY_LABEL = {
    "bug": "Bug",
    "barrier": "Barrier",
    "missing": "Missing Feature",
}


def classify(text: str):
    """Return list of (category, theme) matches. Empty if none."""
    if not text:
        return []
    out = []
    for cat, theme, pattern in [(c, t, re.compile(p, re.IGNORECASE)) for c, t, p in RULES]:
        if pattern.search(text):
            out.append((cat, theme))
    return out


def main():
    records = json.load(open(INP))
    # Bucket: (category, theme) -> list of records
    bucket = defaultdict(list)
    unclassified = []

    for r in records:
        text = (r.get("feedback") or "") + "\n" + (r.get("reason") or "")
        matches = classify(text)
        if not matches:
            unclassified.append(r)
            continue
        # Avoid double-counting the same record's MRR across themes:
        # take the first (highest priority) match per category only
        seen_cats = set()
        for cat, theme in matches:
            if cat in seen_cats:
                continue
            seen_cats.add(cat)
            bucket[(cat, theme)].append(r)

    # Aggregate per theme
    themes = []
    for (cat, theme), recs in bucket.items():
        # Dedup by user_id (one user can submit multiple times — count their MRR once)
        by_user = {}
        for r in recs:
            uid = r.get("user_id") or f"anon-{r['ts']}"
            # keep highest MRR per user (or first if tied)
            if uid not in by_user or (r.get("mrr") or 0) > (by_user[uid].get("mrr") or 0):
                by_user[uid] = r
        unique_recs = list(by_user.values())
        unique_mrr = sum(r.get("mrr") or 0 for r in unique_recs)
        n_unique = len(unique_recs)
        # Pick top quotes — prefer ones whose own feedback matches the theme pattern,
        # then by most recent. This avoids attributing a quote that only loosely relates.
        theme_pattern = next((p for c, t, p in RULES if c == cat and t == theme), None)
        if theme_pattern:
            theme_re = re.compile(theme_pattern, re.IGNORECASE)
            unique_recs.sort(key=lambda r: (
                0 if theme_re.search((r.get("feedback") or "")) else 1,
                -r["ts"],
            ))
        else:
            unique_recs.sort(key=lambda r: r["ts"], reverse=True)
        top_quotes = []
        for r in unique_recs[:5]:
            fb = (r.get("feedback") or "").strip()
            # truncate to 240 chars
            if len(fb) > 280:
                fb = fb[:277] + "..."
            top_quotes.append({
                "quote": fb,
                "mrr": r.get("mrr"),
                "plan": r.get("plan"),
                "prs": r.get("prs"),
                "ts_human": r.get("ts_human"),
                "channel": r.get("channel"),
                "permalink": r.get("permalink"),
                "fullstory": r.get("fullstory"),
            })
        themes.append({
            "category": cat,
            "category_label": CATEGORY_LABEL[cat],
            "theme": theme,
            "n_mentions": len(recs),
            "n_unique_users": n_unique,
            "hvc_mrr_exposure": round(unique_mrr, 0),
            "top_quotes": top_quotes,
        })

    # Sort by HVC MRR exposure descending
    themes.sort(key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))

    # Totals
    total_records = len(records)
    total_mrr_all = sum(r.get("mrr") or 0 for r in records)
    classified_records = total_records - len(unclassified)

    summary = {
        "total_records_in_window": total_records,
        "classified_records": classified_records,
        "unclassified_records": len(unclassified),
        "total_hvc_mrr_in_window": round(total_mrr_all, 0),
        "themes": themes,
    }

    with OUT_JSON.open("w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Markdown report for sanity check
    lines = [f"# VOC Theme Analysis — Mailchimp Email Builder",
             f"Window: 18 months | Records: {total_records} | Classified: {classified_records} | HVC MRR exposure (all): ${total_mrr_all:,.0f}/mo\n"]
    for cat in ["bug", "barrier", "missing"]:
        lines.append(f"\n## {CATEGORY_LABEL[cat]}s\n")
        cat_themes = [t for t in themes if t["category"] == cat]
        cat_themes.sort(key=lambda t: -t["hvc_mrr_exposure"])
        for t in cat_themes:
            lines.append(f"### {t['theme']}")
            lines.append(f"- HVC MRR exposure: **${t['hvc_mrr_exposure']:,.0f}/mo** | unique users: {t['n_unique_users']} | mentions: {t['n_mentions']}")
            for q in t["top_quotes"][:3]:
                quote = q["quote"][:200].replace("\n", " ")
                lines.append(f"  - [{q['ts_human']}] ${q['mrr']:.0f} {q['plan'] or ''}: \"{quote}\"")
            lines.append("")

    OUT_MD.write_text("\n".join(lines))

    # CLI summary
    print(f"Themes: {len(themes)} | Bugs: {sum(1 for t in themes if t['category']=='bug')} | "
          f"Barriers: {sum(1 for t in themes if t['category']=='barrier')} | "
          f"Missing: {sum(1 for t in themes if t['category']=='missing')}")
    print(f"Unclassified: {len(unclassified)} of {total_records}")
    print(f"\nTop 10 themes by HVC MRR exposure:")
    for t in themes[:10]:
        print(f"  [{t['category_label'][:7]:7}] {t['theme']:55} "
              f"${t['hvc_mrr_exposure']:>8,.0f}/mo  ({t['n_unique_users']} users)")


if __name__ == "__main__":
    main()
