"""Render the FULL Page 5 v2 fragment combining:
  - Slack VOC tables (bugs / barriers / missing)
  - Strategic HVC research session findings table (Eric/Jacob/Nina)
  - Combined-signal section (where both data sources reinforce)
  - REVISED 3-phase plan with combined signal

Replaces voc_page5_fragment.html.
"""
import html
import json
from pathlib import Path

from research_sessions import FINDINGS, combined_score, PRIORITY_WEIGHT, FRUSTRATION_WEIGHT

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
THEMES = ROOT / "voc_themes.json"
OUT = ROOT / "voc_page5_fragment.html"

data = json.load(open(THEMES))
themes = data["themes"]
themes_by_name = {t["theme"]: t for t in themes}


def fmt_mrr(v):
    return f"${v:,.0f}"


def trunc(s, n=240):
    s = (s or "").replace("\n", " ").strip()
    if len(s) > n:
        s = s[: n - 1].rstrip() + "…"
    return html.escape(s)


# ------------- Slack VOC tables (same as v1, for context above) -------------

def render_quote_block(q):
    plan = html.escape(q.get("plan") or "—")
    mrr = fmt_mrr(q.get("mrr") or 0)
    ts = q.get("ts_human") or "—"
    perm = q.get("permalink")
    fs = q.get("fullstory")
    quote = trunc(q.get("quote") or "")
    perm_html = f' · <a href="{html.escape(perm)}" target="_blank" rel="noopener">Slack</a>' if perm else ""
    fs_html = f' · <a href="{html.escape(fs)}" target="_blank" rel="noopener">Fullstory</a>' if fs else ""
    return (
        f'<div class="voc-quote">'
        f'<div class="voc-meta-line"><span class="voc-mrr">{mrr}/mo</span> '
        f'· <span class="voc-plan">{plan}</span> · <span class="voc-date">{ts}</span>'
        f'{perm_html}{fs_html}</div>'
        f'<div class="voc-text">"{quote}"</div>'
        f'</div>'
    )


def render_theme_row(t):
    cat_class = {"bug": "cat-bug", "barrier": "cat-barrier", "missing": "cat-missing"}[t["category"]]
    quotes_html = "".join(render_quote_block(q) for q in t["top_quotes"][:2])
    return (
        f'<tr class="{cat_class}">'
        f'<td class="voc-th"><strong>{html.escape(t["theme"])}</strong>'
        f'<div class="voc-sub">{html.escape(t["category_label"])}</div></td>'
        f'<td class="voc-mrr-cell"><div class="voc-mrr-big">{fmt_mrr(t["hvc_mrr_exposure"])}</div>'
        f'<div class="voc-users">{t["n_unique_users"]} HVC users · {t["n_mentions"]} mentions</div></td>'
        f'<td class="voc-quotes">{quotes_html}</td>'
        f'</tr>'
    )


bugs = sorted([t for t in themes if t["category"] == "bug"],
              key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))
barriers = sorted([t for t in themes if t["category"] == "barrier"],
                  key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))
missing = sorted([t for t in themes if t["category"] == "missing"],
                 key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))

bug_rows = "\n".join(render_theme_row(t) for t in bugs)
barrier_rows = "\n".join(render_theme_row(t) for t in barriers)
missing_rows = "\n".join(render_theme_row(t) for t in missing)

# ------------- Research session findings table -------------

def render_research_row(f):
    cat_class = {
        "UI Improvement": "rs-cat-ui",
        "Bug": "rs-cat-bug",
        "Feature Parity": "rs-cat-parity",
        "Delight": "rs-cat-delight",
    }[f["category"]]
    pri_class = {"HIGH": "rs-pri-hi", "MEDIUM": "rs-pri-mid", "LOW": "rs-pri-lo", "NA": "rs-pri-na"}[f["priority"]]
    fr_class = {"High": "rs-fr-hi", "Medium": "rs-fr-mid", "Low": "rs-fr-lo", "Delight": "rs-fr-delight"}[f["frustration"]]
    excl = "YES" if f["exclusive"] else "no"
    excl_class = "rs-excl-yes" if f["exclusive"] else "rs-excl-no"
    slack_link = ""
    if "slack_theme" in f:
        # Look up MRR and add badge
        t = themes_by_name.get(f["slack_theme"])
        if t:
            slack_link = f' <span class="rs-link-slack" title="Reinforced by Slack VOC: ${t["hvc_mrr_exposure"]:,.0f}/mo across {t["n_unique_users"]} HVC users">↔ Slack ${t["hvc_mrr_exposure"]:,.0f}/mo</span>'
    return (
        f'<tr>'
        f'<td><code class="rs-id">{html.escape(f["id"])}</code></td>'
        f'<td><span class="rs-src">{html.escape(f["source"])}</span></td>'
        f'<td><span class="rs-cat {cat_class}">{html.escape(f["category"])}</span></td>'
        f'<td>{html.escape(f["detail"])}</td>'
        f'<td class="rs-summary">{html.escape(f["summary"])}{slack_link}</td>'
        f'<td><span class="rs-fr {fr_class}">{html.escape(f["frustration"])}</span></td>'
        f'<td><span class="rs-excl {excl_class}">{excl}</span></td>'
        f'<td class="rs-num">{f["score"]}</td>'
        f'<td>{html.escape(f["sizing"])}</td>'
        f'<td><span class="rs-pri {pri_class}">{html.escape(f["priority"])}</span></td>'
        f'</tr>'
    )


# Sort: HIGH priority first, then by score desc
findings_sorted = sorted(
    FINDINGS,
    key=lambda f: (-PRIORITY_WEIGHT.get(f["priority"], 0), -f["score"]),
)
research_rows = "\n".join(render_research_row(f) for f in findings_sorted)

# Counts for the research KPI strip
n_total = len(FINDINGS)
n_high = sum(1 for f in FINDINGS if f["priority"] == "HIGH")
n_med = sum(1 for f in FINDINGS if f["priority"] == "MEDIUM")
n_low = sum(1 for f in FINDINGS if f["priority"] == "LOW")
n_delight = sum(1 for f in FINDINGS if f["category"] == "Delight")
n_quickwin = sum(1 for f in FINDINGS if f["sizing"] == "Quick Win")
n_mapped = sum(1 for f in FINDINGS if "slack_theme" in f)


# ------------- Combined-signal items (reinforced by both sources) -------------

def find_slack_theme(name):
    return themes_by_name.get(name)


reinforced = []
for f in FINDINGS:
    if "slack_theme" in f:
        t = find_slack_theme(f["slack_theme"])
        if t:
            reinforced.append((f, t))

# Group by Slack theme so we don't double-list (S1.11 and S2.89 both → universal content)
from collections import defaultdict
themed_reinforced = defaultdict(lambda: {"theme": None, "findings": []})
for f, t in reinforced:
    themed_reinforced[t["theme"]]["theme"] = t
    themed_reinforced[t["theme"]]["findings"].append(f)


def render_reinforced(item):
    t = item["theme"]
    fs = item["findings"]
    finding_chips = "".join(
        f'<span class="rs-id-chip" title="{html.escape(f["summary"])}">{f["id"]} ({f["source"]})</span> '
        for f in fs
    )
    return (
        f'<div class="reinforced-card">'
        f'<div class="rc-head"><div class="rc-title">{html.escape(t["theme"])}</div>'
        f'<div class="rc-mrr">{fmt_mrr(t["hvc_mrr_exposure"])}<small>/mo</small></div></div>'
        f'<div class="rc-meta">'
        f'<span class="rc-pill rc-pill-slack">Slack: {t["n_unique_users"]} HVC users · {fmt_mrr(t["hvc_mrr_exposure"])}/mo</span> '
        f'<span class="rc-pill rc-pill-research">Research: {len(fs)} session finding{"s" if len(fs)>1 else ""}</span>'
        f'</div>'
        f'<div class="rc-findings">{finding_chips}</div>'
        f'</div>'
    )


reinforced_html = "".join(render_reinforced(item) for item in
                          sorted(themed_reinforced.values(),
                                 key=lambda x: (-x["theme"]["hvc_mrr_exposure"], -len(x["findings"]))))


# ------------- REVISED 3-phase plan with combined signal -------------

def slack_mrr_for(f):
    t = find_slack_theme(f.get("slack_theme", ""))
    return t["hvc_mrr_exposure"] if t else 0


# Score every research finding
scored_findings = []
for f in FINDINGS:
    if f["category"] == "Delight":
        continue  # delights aren't actionable here
    score = combined_score(f, slack_mrr_for(f))
    scored_findings.append((score, f))

# Score every Slack-only theme (one not yet covered by research)
covered_slack_themes = {f.get("slack_theme") for f in FINDINGS if "slack_theme" in f}
slack_only = []
for t in themes:
    if t["theme"] in covered_slack_themes:
        continue
    # Synthesize a virtual "finding" from the Slack theme for combined ranking
    pseudo_priority = "HIGH" if t["hvc_mrr_exposure"] >= 5000 or t["n_unique_users"] >= 6 else (
        "MEDIUM" if t["hvc_mrr_exposure"] >= 1500 or t["n_unique_users"] >= 3 else "LOW"
    )
    pseudo_frust = "High" if t["category"] == "bug" and t["hvc_mrr_exposure"] >= 2000 else (
        "Medium" if t["hvc_mrr_exposure"] >= 800 else "Low"
    )
    pseudo = {
        "id": f"VOC-{t['theme'][:20]}",
        "source": "Slack VOC",
        "category": {"bug": "Bug", "barrier": "UI Improvement", "missing": "Feature Parity"}[t["category"]],
        "detail": "—",
        "summary": t["theme"],
        "frustration": pseudo_frust,
        "exclusive": False,
        "score": min(5, 1 + t["n_unique_users"] // 2),
        "sizing": "Medium Lift",
        "priority": pseudo_priority,
        "slack_theme": t["theme"],
    }
    score = combined_score(pseudo, t["hvc_mrr_exposure"])
    slack_only.append((score, pseudo))

all_scored = scored_findings + slack_only
all_scored.sort(key=lambda x: -x[0])

# Phase boundaries — by combined score quantiles
n = len(all_scored)
phase_cuts = [n // 3, 2 * n // 3]


def render_combined_row(score, f):
    cat_chip = {
        "Bug": "ph-bug", "UI Improvement": "ph-barrier",
        "Feature Parity": "ph-missing", "Slack VOC": "ph-barrier",
    }.get(f["category"], "ph-barrier")
    cat_label = {"UI Improvement": "Barrier", "Feature Parity": "Missing", "Bug": "Bug"}.get(f["category"], f["category"])
    src = f["source"]
    if src == "Slack VOC":
        src_html = '<span class="src-tag src-slack">Slack VOC</span>'
    else:
        src_html = f'<span class="src-tag src-research">{html.escape(src)} · {html.escape(f["id"])}</span>'
    mrr = slack_mrr_for(f)
    mrr_html = f"{fmt_mrr(mrr)}/mo" if mrr else "—"
    fr = f["frustration"]
    return (
        f'<tr><td><span class="ph-cat {cat_chip}">{cat_label}</span></td>'
        f'<td>{html.escape(f["summary"][:130]) + ("…" if len(f["summary"]) > 130 else "")}</td>'
        f'<td>{src_html}</td>'
        f'<td class="num">{mrr_html}</td>'
        f'<td>{html.escape(fr)}</td>'
        f'<td>{html.escape(f["sizing"])}</td>'
        f'<td class="num">{score:.0f}</td></tr>'
    )


def phase_table(items):
    rows = "".join(render_combined_row(s, f) for s, f in items)
    total_mrr = sum(slack_mrr_for(f) for _, f in items)
    return rows, total_mrr


p1_items = all_scored[:phase_cuts[0]]
p2_items = all_scored[phase_cuts[0]:phase_cuts[1]]
p3_items = all_scored[phase_cuts[1]:]

p1_rows, p1_mrr = phase_table(p1_items)
p2_rows, p2_mrr = phase_table(p2_items)
p3_rows, p3_mrr = phase_table(p3_items)


# ------------- Build the final fragment -------------

total_themed_mrr = sum(t["hvc_mrr_exposure"] for t in themes)

fragment = f"""
    <div class="voc-kpi-row" style="margin-bottom:14px;">
      <div class="kpi"><div class="v">150 + 33</div><div class="l">HVC Slack messages + strategic-HVC research findings (Eric · Jacob · Nina)</div></div>
      <div class="kpi"><div class="v">28 + {n_total}</div><div class="l">Slack themes + research items · {n_high} HIGH · {n_med} MEDIUM · {n_low} LOW · {n_delight} DELIGHT</div></div>
      <div class="kpi"><div class="v">{fmt_mrr(total_themed_mrr)}/mo</div><div class="l">Aggregate Slack-attributed HVC MRR exposure · plus {n_mapped} research items reinforce specific themes</div></div>
      <div class="kpi"><div class="v">{n_quickwin} quick wins</div><div class="l">Research items sized as Quick Wins · {n_high - sum(1 for f in FINDINGS if f["priority"]=="HIGH" and f["sizing"]=="Quick Win")} HIGH-priority items still > Quick Win</div></div>
    </div>

    <div class="card tinted" style="margin-bottom:14px;">
      <p style="margin:0 0 4px;"><strong>Methodology — two reinforcing data sources.</strong>
      <strong>(1) Slack VOC:</strong> 150 HVC messages across <code>#hvc_feedback</code> + <code>#mc-hvc-escalations</code> (May 2025 → April 2026), thematized with HVC MRR exposure aggregated per theme.
      <strong>(2) Strategic HVC research sessions:</strong> 33 hand-extracted findings across 3 PM-led research sessions with strategic Mailchimp HVC accounts (Eric session 1, Jacob session 2, Nina session 3). Each finding tagged with frustration, engineering sizing, exclusivity, and pre-assigned priority.
      <strong>Combined-signal score</strong> = priority_weight + 2×frustration_weight (×100) + Slack_MRR/100 + category_boost (Bug+50, Parity+30, Delight−1000), divided by sizing_weight (Quick Win=1, Medium Lift=2, Big Lift=4). Items appearing in <em>both</em> sources get a natural double boost via the MRR term. <code>#mc-feedback-summary</code> remains broader/non-HVC reference.</p>
    </div>

    <h2><span class="num">23</span>Critical bugs (Slack VOC) — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (Slack + Fullstory links)</th></tr></thead>
      <tbody>
{bug_rows}
      </tbody>
    </table>

    <h2 style="margin-top:18px;"><span class="num">24</span>Key barriers (Slack VOC) — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (Slack + Fullstory links)</th></tr></thead>
      <tbody>
{barrier_rows}
      </tbody>
    </table>

    <h2 style="margin-top:18px;"><span class="num">25</span>Missing features (Slack VOC) — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (Slack + Fullstory links)</th></tr></thead>
      <tbody>
{missing_rows}
      </tbody>
    </table>

    <h2 style="margin-top:20px;"><span class="num">26</span>Strategic HVC research session findings (Eric · Jacob · Nina)</h2>
    <p style="margin-bottom:8px;">{n_total} hand-extracted findings from PM research sessions with strategic Mailchimp HVC accounts. Sorted by Priority then Score. The <span class="rs-link-slack" style="position:relative; top:1px;">↔ Slack</span> badge appears where the same issue is also present in Slack VOC and shows the MRR exposure.</p>
    <div class="rs-table-wrap">
    <table class="rs-table">
      <thead>
        <tr>
          <th>#</th><th>Source</th><th>Category</th><th>Surface</th><th>Detail</th>
          <th>Summary <span style="font-weight:400; color:#999;">(↔ Slack reinforcement where applicable)</span></th>
          <th>Frust.</th><th>Excl.</th><th>Score</th><th>Sizing</th><th>Priority</th>
        </tr>
      </thead>
      <tbody>
{research_rows}
      </tbody>
    </table>
    </div>

    <h2 style="margin-top:20px;"><span class="num">27</span>Reinforced items — where both Slack VOC <em>and</em> research sessions agree</h2>
    <p style="margin-bottom:8px;">These themes show up in <strong>both</strong> the high-volume Slack signal <em>and</em> the deep PM research conversations. Highest credibility — multi-source confirmation. Phase 1 priority candidates.</p>
    <div class="reinforced-grid">
{reinforced_html}
    </div>

    <h2 style="margin-top:20px;"><span class="num">28</span>REVISED 3-phase plan — combined-signal prioritization</h2>
    <p style="margin-bottom:8px;">Each row scored on combined signal. Phase boundaries are scored quantiles of the unified backlog (research findings + Slack-only themes). The <strong>$/mo column shows Slack-attributed HVC MRR exposure</strong>; research-only items show "—" (research-confirmed strategic-HVC pain that hasn't yet surfaced via Qualtrics PRS).</p>

    <div class="grid cols-1" style="margin-bottom:14px;">
      <div class="phase">
        <div class="label">Phase 1 · 0–3 months · Stop the bleed + reinforced items</div>
        <h3>Top {len(p1_items)} items by combined signal · Slack MRR addressed: {fmt_mrr(p1_mrr)}/mo</h3>
        <table class="voc-phase-table">
          <thead><tr><th>Cat</th><th>Item</th><th>Source</th><th class="num">Slack $/mo</th><th>Frust.</th><th>Sizing</th><th class="num">Score</th></tr></thead>
          <tbody>{p1_rows}</tbody>
        </table>
      </div>
    </div>

    <div class="grid cols-1" style="margin-bottom:14px;">
      <div class="phase p2">
        <div class="label">Phase 2 · 3–9 months · Capability parity + reliability</div>
        <h3>Next {len(p2_items)} items · Slack MRR addressed: {fmt_mrr(p2_mrr)}/mo</h3>
        <table class="voc-phase-table">
          <thead><tr><th>Cat</th><th>Item</th><th>Source</th><th class="num">Slack $/mo</th><th>Frust.</th><th>Sizing</th><th class="num">Score</th></tr></thead>
          <tbody>{p2_rows}</tbody>
        </table>
      </div>
    </div>

    <div class="grid cols-1">
      <div class="phase p3">
        <div class="label">Phase 3 · 9–18 months · Depth + delight + tail</div>
        <h3>Remaining {len(p3_items)} items · Slack MRR addressed: {fmt_mrr(p3_mrr)}/mo</h3>
        <table class="voc-phase-table">
          <thead><tr><th>Cat</th><th>Item</th><th>Source</th><th class="num">Slack $/mo</th><th>Frust.</th><th>Sizing</th><th class="num">Score</th></tr></thead>
          <tbody>{p3_rows}</tbody>
        </table>
      </div>
    </div>

    <h2 style="margin-top:18px;"><span class="num">29</span>Strategic delights to defend (Nina session)</h2>
    <div class="grid cols-3">
      <div class="card col-loved">
        <p style="margin:0;"><strong>Auto-generated alt text (S3.8).</strong> Strategic agency calls this a "surprise delight" — saves meaningful effort on image-heavy D2C emails. Keep investing; market it harder; consider expanding to image descriptions inside Image Remix-style edits.</p>
      </div>
      <div class="card col-loved">
        <p style="margin:0;"><strong>Product recommendation blocks (S3.19).</strong> "Easier to implement than competitors." This is a defensible Mailchimp moat against Klaviyo's product blocks — preserve the simplicity, expand depth (more catalogs, more dynamic data properties).</p>
      </div>
      <div class="card col-loved">
        <p style="margin:0;"><strong>Core builder met Klaviyo power-user expectations (S3.20).</strong> Nina's quote: "intuitive and standard." Validates that table-stakes is achieved on the core canvas — now ship the differentiated bets in Page 4 to leapfrog.</p>
      </div>
    </div>
"""

OUT.write_text(fragment.strip())
print(f"Wrote Page 5 v2 fragment to {OUT} ({len(fragment):,} chars)")
print(f"Phase 1: {len(p1_items)} items · ${p1_mrr:,.0f}/mo Slack MRR")
print(f"Phase 2: {len(p2_items)} items · ${p2_mrr:,.0f}/mo Slack MRR")
print(f"Phase 3: {len(p3_items)} items · ${p3_mrr:,.0f}/mo Slack MRR")
print(f"\nReinforced themes (both Slack + research): {len(themed_reinforced)}")
for name, item in themed_reinforced.items():
    print(f"  - {name} (${item['theme']['hvc_mrr_exposure']:,.0f}/mo + {len(item['findings'])} research finding(s))")
print(f"\nTop 10 Phase 1 items by combined score:")
for s, f in p1_items[:10]:
    src = f["source"] if f["source"] != "Slack VOC" else "Slack"
    print(f"  {s:6.0f} | [{src:8}] {f['summary'][:70]}")
