"""Render Page 5 (VOC-Driven Prioritization) HTML fragment from voc_themes.json.

Outputs:
  voc_page5_fragment.html — the HTML to be embedded into index.html
"""
import html
import json
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
INP = ROOT / "voc_themes.json"
OUT = ROOT / "voc_page5_fragment.html"


def fmt_mrr(v):
    return f"${v:,.0f}"


def trunc_quote(q, n=240):
    q = q.replace("\n", " ").strip()
    if len(q) > n:
        q = q[: n - 1].rstrip() + "…"
    return html.escape(q)


def render_quote_block(q):
    plan = html.escape(q.get("plan") or "—")
    mrr = fmt_mrr(q.get("mrr") or 0)
    ts = q.get("ts_human") or "—"
    perm = q.get("permalink")
    fs = q.get("fullstory")
    quote = trunc_quote(q.get("quote") or "")
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


def render_theme_row(t, rank=None):
    cat_class = {"bug": "cat-bug", "barrier": "cat-barrier", "missing": "cat-missing"}[t["category"]]
    quotes_html = "".join(render_quote_block(q) for q in t["top_quotes"][:2])
    rank_html = f'<span class="voc-rank">{rank}</span>' if rank else ""
    return (
        f'<tr class="{cat_class}">'
        f'<td class="voc-th">{rank_html}<strong>{html.escape(t["theme"])}</strong>'
        f'<div class="voc-sub">{html.escape(t["category_label"])}</div></td>'
        f'<td class="voc-mrr-cell"><div class="voc-mrr-big">{fmt_mrr(t["hvc_mrr_exposure"])}</div>'
        f'<div class="voc-users">{t["n_unique_users"]} HVC users · {t["n_mentions"]} mentions</div></td>'
        f'<td class="voc-quotes">{quotes_html}</td>'
        f'</tr>'
    )


def main():
    data = json.load(open(INP))
    themes = data["themes"]

    # Per-category sorting
    bugs = sorted([t for t in themes if t["category"] == "bug"],
                  key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))
    barriers = sorted([t for t in themes if t["category"] == "barrier"],
                      key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))
    missing = sorted([t for t in themes if t["category"] == "missing"],
                     key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))

    # Phasing: combined ranking
    all_ranked = sorted(themes,
                        key=lambda t: (-t["hvc_mrr_exposure"] - t["n_unique_users"] * 500,
                                       -t["hvc_mrr_exposure"]))

    # Phase split: P1 = top items (~$50K+ MRR closed), P2 = middle ($25-50K closed), P3 = tail
    def phase_block(themes_in_phase, label, color_class):
        rows = ""
        cum = 0
        for t in themes_in_phase:
            cum += t["hvc_mrr_exposure"]
            cat_chip = {"bug": "ph-bug", "barrier": "ph-barrier", "missing": "ph-missing"}[t["category"]]
            rows += (
                f'<tr><td><span class="ph-cat {cat_chip}">{html.escape(t["category_label"])}</span></td>'
                f'<td>{html.escape(t["theme"])}</td>'
                f'<td class="num">{fmt_mrr(t["hvc_mrr_exposure"])}</td>'
                f'<td class="num">{t["n_unique_users"]}</td></tr>'
            )
        return rows, cum

    # Manual partition based on MRR + user breadth + strategic alignment with Page 4 plan
    # Phase 1 = highest-MRR + broadest user reach + universal pain or quick wins
    p1_themes_keys = {
        "Saved sections / saved blocks / universal content",
        "UI churn / new builder dislike / 'bring back the old'",
        "Generic 'editor is clunky / hard to use / unusable'",
        "Steep learning curve / confusing UX",
        "Text formatting / fonts / spacing",
        "Hyperlink / button URL / link won't remove",
        "Preview from template list / template gallery navigation",
    }
    # Phase 2 = capability parity, performance, mid-MRR feature additions
    p2_themes_keys = {
        "Snap-to-grid / spacing alignment / structured layout",
        "Advanced merge tag / content variables / conditional / loops",
        "Editor performance / lag / browser freeze",
        "Mobile preview accuracy / what-you-see-is-not-what-you-get",
        "Editor undo / redo / version history",
        "Editor feels dated / less powerful than competitors",
        "Better A/B testing / multivariate in builder",
        "Editor consistency / new builder for journeys / one editor",
        "Better post-send / editor navigation / find what was sent",
        "Image upload / cropping / resize",
    }
    # P3 = everything else

    p1 = [t for t in themes if t["theme"] in p1_themes_keys]
    p2 = [t for t in themes if t["theme"] in p2_themes_keys]
    p3 = [t for t in themes if t["theme"] not in p1_themes_keys and t["theme"] not in p2_themes_keys]
    # sort each
    for lst in (p1, p2, p3):
        lst.sort(key=lambda t: (-t["hvc_mrr_exposure"], -t["n_unique_users"]))

    p1_rows, p1_total = phase_block(p1, "Phase 1", "p1")
    p2_rows, p2_total = phase_block(p2, "Phase 2", "p2")
    p3_rows, p3_total = phase_block(p3, "Phase 3", "p3")

    total_themed_mrr = sum(t["hvc_mrr_exposure"] for t in themes)
    total_themed_users = sum(t["n_unique_users"] for t in themes)
    n_themes = len(themes)

    # Render
    bug_rows = "\n".join(render_theme_row(t) for t in bugs)
    barrier_rows = "\n".join(render_theme_row(t) for t in barriers)
    missing_rows = "\n".join(render_theme_row(t) for t in missing)

    fragment = f"""
    <div class="voc-kpi-row" style="margin-bottom:14px;">
      <div class="kpi"><div class="v">{data['total_records_in_window']}</div><div class="l">HVC builder feedback messages classified · 18-mo window (cached subset: May 2025 → Apr 2026)</div></div>
      <div class="kpi"><div class="v">{n_themes}</div><div class="l">Distinct themes — {len(bugs)} bugs · {len(barriers)} barriers · {len(missing)} missing features</div></div>
      <div class="kpi"><div class="v">{fmt_mrr(total_themed_mrr)}/mo</div><div class="l">Aggregate HVC MRR exposure across all themes · ≈ ${total_themed_mrr*12/1000:.0f}K ARR at risk</div></div>
      <div class="kpi"><div class="v">{total_themed_users}</div><div class="l">Unique HVC user-issue pairs (one user may appear in multiple themes)</div></div>
    </div>

    <div class="card tinted" style="margin-bottom:14px;">
      <p style="margin:0 0 4px;"><strong>Methodology.</strong> Pulled the last ~12 months of cached messages from <code>#hvc_feedback</code> (C051Y4H98VB) and <code>#mc-hvc-escalations</code> (C095FJ3SQF4). Filtered to messages mentioning email-builder concepts (editor, builder, template, blocks, drag-and-drop, image editor, etc.) and excluded sentiment-only / tracking pings ("Received*", "Top!", "Badge*"). Each surviving message was theme-classified by regex rules across <em>Bug · Barrier · Missing Feature</em>. <strong>HVC MRR exposure per theme = sum of MRR across unique users mentioning that theme</strong> (one user counted once per theme, max-MRR taken). Quotes link back to the original Slack thread + Fullstory session replay where available. Date window: <strong>2025-05-05 → 2026-04-22</strong>. <em>#mc-feedback-summary</em> (C06EVEZ4ZTQ) is broader/non-HVC and surfaces additional volume but doesn't change the HVC-MRR prioritization below.</p>
    </div>

    <h2><span class="num">23</span>Critical bugs — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (with Slack + Fullstory links)</th></tr></thead>
      <tbody>
{bug_rows}
      </tbody>
    </table>

    <h2 style="margin-top:18px;"><span class="num">24</span>Key barriers — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (with Slack + Fullstory links)</th></tr></thead>
      <tbody>
{barrier_rows}
      </tbody>
    </table>

    <h2 style="margin-top:18px;"><span class="num">25</span>Missing features — by HVC MRR exposure</h2>
    <table class="voc-table">
      <thead><tr><th>Theme</th><th>HVC MRR exposure</th><th>Top customer quotes (with Slack + Fullstory links)</th></tr></thead>
      <tbody>
{missing_rows}
      </tbody>
    </table>

    <h2 style="margin-top:20px;"><span class="num">26</span>3-phase MRR-weighted plan — close the most HVC risk first</h2>
    <p style="margin-bottom:8px;">Phasing optimizes for <strong>MRR closed × user breadth × engineering cost</strong>, and aligns with the Page 4 strategic plan (Phase 1 = parity + Klaviyo neutralization). The number in each phase header is the cumulative HVC MRR exposure addressed.</p>

    <div class="grid cols-3" style="margin-bottom:8px;">
      <div class="phase">
        <div class="label">Phase 1 · 0–3 months</div>
        <h3>Stop the bleed · win-the-hour fixes</h3>
        <div class="goal"><strong>HVC MRR closed:</strong> {fmt_mrr(p1_total)}/mo (≈ ${p1_total*12/1000:.0f}K ARR) · <strong>Mostly bugs + 1 universal feature</strong></div>
        <table class="voc-phase-table">
          <thead><tr><th>Type</th><th>Theme</th><th>$/mo</th><th>Users</th></tr></thead>
          <tbody>{p1_rows}</tbody>
        </table>
        <div class="goal" style="border-top:1px dashed var(--line); border-bottom:0; padding-top:8px; padding-bottom:0; margin-top:8px;"><strong>Plays:</strong> autosave + version-history hardening · ship Universal Saved Content (matches Page 4 F1) · "bring back the old" preference toggle · Ctrl+K hyperlink fix · template-list inline preview · UX polish sweep on top clunkiness reports.</div>
      </div>

      <div class="phase p2">
        <div class="label">Phase 2 · 3–9 months</div>
        <h3>Capability parity + reliability</h3>
        <div class="goal"><strong>HVC MRR closed:</strong> {fmt_mrr(p2_total)}/mo (≈ ${p2_total*12/1000:.0f}K ARR) · <strong>Performance + missing capabilities</strong></div>
        <table class="voc-phase-table">
          <thead><tr><th>Type</th><th>Theme</th><th>$/mo</th><th>Users</th></tr></thead>
          <tbody>{p2_rows}</tbody>
        </table>
        <div class="goal" style="border-top:1px dashed var(--line); border-bottom:0; padding-top:8px; padding-bottom:0; margin-top:8px;"><strong>Plays:</strong> editor performance budget (browser-freeze gone) · snap-to-grid + alignment guides · advanced merge tags / content variables · undo+versioning · in-builder A/B test winner reuse · mobile-preview accuracy parity · unify Customer-Journey editor with email builder.</div>
      </div>

      <div class="phase p3">
        <div class="label">Phase 3 · 9–18 months</div>
        <h3>Depth + delight + differentiation</h3>
        <div class="goal"><strong>HVC MRR closed:</strong> {fmt_mrr(p3_total)}/mo (≈ ${p3_total*12/1000:.0f}K ARR) · <strong>Tail asks + pro-grade depth</strong></div>
        <table class="voc-phase-table">
          <thead><tr><th>Type</th><th>Theme</th><th>$/mo</th><th>Users</th></tr></thead>
          <tbody>{p3_rows}</tbody>
        </table>
        <div class="goal" style="border-top:1px dashed var(--line); border-bottom:0; padding-top:8px; padding-bottom:0; margin-top:8px;"><strong>Plays:</strong> direct HTML editor + custom CSS · dark-mode preview · conditional content per segment · in-canvas image editor (Gemini-class) · brand-voice from corpus · footer customization · more block types (text+button, Telegram, etc.) · post-send navigation polish.</div>
      </div>
    </div>

    <p style="font-size:11.5px; color:var(--muted); margin-top:6px;">
      <strong>Cumulative MRR closed across all 3 phases:</strong> {fmt_mrr(p1_total + p2_total + p3_total)}/mo
      (≈ ${(p1_total+p2_total+p3_total)*12/1000:.0f}K ARR exposure addressed).
      Remaining unclassified ${data['total_hvc_mrr_in_window'] - total_themed_mrr:,.0f}/mo
      sits in long-tail one-off requests with no thematic cluster.
    </p>
"""

    OUT.write_text(fragment.strip())
    print(f"Wrote {OUT}")
    print(f"Phase 1 MRR: {fmt_mrr(p1_total)}")
    print(f"Phase 2 MRR: {fmt_mrr(p2_total)}")
    print(f"Phase 3 MRR: {fmt_mrr(p3_total)}")
    print(f"Total themed: {fmt_mrr(p1_total + p2_total + p3_total)}")
    print(f"Total in dataset: {fmt_mrr(data['total_hvc_mrr_in_window'])}")


if __name__ == "__main__":
    main()
