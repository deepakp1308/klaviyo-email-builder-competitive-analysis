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
        <h1>HVC VOC prioritization — bugs, barriers &amp; missing features by MRR exposure</h1>
        <div class="subtitle">18-month synthesis of high-value-customer Slack feedback (<code>#hvc_feedback</code>, <code>#mc-hvc-escalations</code>, <code>#mc-feedback-summary</code>) for the Mailchimp email builder. Themed, MRR-weighted, and sequenced into a 3-phase plan to close the most HVC MRR risk first.</div>
      </div>
      <div class="meta">
        <div><strong>Slack channels:</strong> 3 specified · 2 with HVC-tagged data</div>
        <div style="margin-top:6px;"><strong>HVC threshold:</strong> &gt;$299/mo</div>
      </div>
    </div>

    {fragment}

    <div class="source">
      <strong>Sources (Page 5):</strong>
      Slack channels — <code>#hvc_feedback</code> (C051Y4H98VB) · <code>#mc-hvc-escalations</code> (C095FJ3SQF4) · <code>#mc-feedback-summary</code> (C06EVEZ4ZTQ, broader/non-HVC reference channel).
      Source-of-record per quote: Slack permalink + Fullstory session replay (where Qualtrics captured one).
      <br/><br/>
      <em>Methodology:</em> Cached Slack pull (May 2025 → April 2026 from <code>#hvc_feedback</code> + <code>#mc-hvc-escalations</code>) parsed for email-builder-relevant feedback (regex-filtered against editor / builder / template / block / drag-and-drop / image / merge-tag concepts; non-HVC sentiment-only pings excluded). 150 surviving HVC messages classified across {{}} themes via builder-specific regex rules iteratively tuned by re-inspecting unclassified samples. <strong>HVC MRR exposure per theme = sum across unique HVC users (one user counted once per theme, max-MRR taken)</strong> to avoid double-counting repeated complaints from the same account. Quote selection prefers messages whose feedback explicitly matches the theme pattern, then most recent. Phasing optimizes for MRR closed × user breadth × engineering cost, and aligns with the Page 4 strategic plan (Phase 1 = parity moves that also neutralize Klaviyo).
    </div>
  </section>
'''

# Remove existing page5 if present (idempotent)
html = re.sub(
    r'<!--\s*=+\s*PAGE 5\s*[\s\S]*?</section>\s*',
    '',
    html,
    flags=re.MULTILINE,
)

# Insert before the final closing </div> of .page-wrap (which is followed by <script>)
INSERT_MARKER = "</section>\n\n</div>"
if INSERT_MARKER not in html:
    print("ERROR: insert marker not found")
    raise SystemExit(1)
new_html = html.replace(INSERT_MARKER, f"</section>\n{page5_section}\n</div>", 1)

INDEX.write_text(new_html)
print(f"Injected Page 5 into {INDEX}")
print(f"Index size: {len(new_html):,} chars")
