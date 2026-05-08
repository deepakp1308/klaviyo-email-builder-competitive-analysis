"""Inject Page 5 fragment into index.html as a new <section class='page' id='page5'>.

Idempotent: removes any existing page5 section before re-inserting.
"""
import re
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
INDEX = ROOT / "index.html"
FRAGMENT = ROOT / "voc_page5_fragment.html"

html = INDEX.read_text()
fragment = FRAGMENT.read_text()

# Build the page5 section
page5_section = f'''
  <!-- ============ PAGE 5 — VOC-DRIVEN HVC PRIORITIZATION ============ -->
  <section class="page" id="page5">
    <div class="page-head">
      <div>
        <div class="eyebrow">Competitive Intelligence · Executive Brief · Page 5 of 5</div>
        <h1>HVC VOC + research-session prioritization — combined-signal plan</h1>
        <div class="subtitle">Two reinforcing data sources for the Mailchimp email builder: <strong>(1)</strong> 18-month HVC Slack VOC across <code>#hvc_feedback</code>, <code>#mc-hvc-escalations</code>, <code>#mc-feedback-summary</code> (themed, MRR-weighted), and <strong>(2)</strong> 33 hand-extracted findings from PM research sessions with strategic HVC accounts (Eric · Jacob · Nina). Combined-signal scored, then sequenced into a 3-phase plan to close the most HVC MRR risk and deepest research conviction first.</div>
      </div>
      <div class="meta">
        <div><strong>Sources:</strong> 3 Slack channels + 3 research sessions</div>
        <div style="margin-top:6px;"><strong>HVC threshold:</strong> &gt;$299/mo MRR · strategic accounts</div>
      </div>
    </div>

    {fragment}

    <div class="source">
      <strong>Sources (Page 5):</strong>
      <em>Slack:</em> <code>#hvc_feedback</code> (C051Y4H98VB) · <code>#mc-hvc-escalations</code> (C095FJ3SQF4) · <code>#mc-feedback-summary</code> (C06EVEZ4ZTQ).
      <em>Research sessions:</em> 33 PM-extracted findings — Eric (Session 1, 15 findings) · Jacob (Session 2, 15 findings) · Nina (Session 3, 3 delights).
      Per-quote source-of-record: Slack permalink + Fullstory session replay (where Qualtrics captured one).
      <br/><br/>
      <em>Combined-signal score (per item):</em> <code>(priority_weight + 2 × frustration_weight) × 100 + Slack_MRR/100 + category_boost (Bug+50, Parity+30, Delight−1000)</code>, divided by sizing_weight (Quick Win=1, Medium Lift=2, Big Lift=4). Items confirmed by both Slack VOC and research sessions get a natural double boost. Phase boundaries are scored quantiles of the unified backlog. Strategic-HVC research findings are weighted heavily because they come from PM-led 1:1 sessions with high-spend accounts — even a single research finding represents deeper conviction than a Slack ping.
    </div>
  </section>
'''

# Remove existing page5 if present (idempotent), preserving the surrounding newlines
html = re.sub(
    r'\n\s*<!--\s*=+\s*PAGE 5\s*[\s\S]*?</section>\s*\n',
    '\n',
    html,
    flags=re.MULTILINE,
)

# Insert before the final closing </div> of .page-wrap (which is followed by <script>)
# Anchor on the script tag for reliability
INSERT_MARKER = "</div>\n\n<script>"
if INSERT_MARKER not in html:
    # Fall back to other potential markers
    print("ERROR: insert marker not found")
    print("Last 200 chars before </script>:")
    idx = html.rfind("<script>")
    print(html[max(0, idx-200):idx])
    raise SystemExit(1)
new_html = html.replace(INSERT_MARKER, f"{page5_section}\n</div>\n\n<script>", 1)

INDEX.write_text(new_html)
print(f"Injected Page 5 into {INDEX}")
print(f"Index size: {len(new_html):,} chars")
