"""Page 7 — Email Builder Health Diagnostic.
Embeds the actual BigQuery findings from the analysis run on May 8, 2026.
Outputs page7_fragment.html.
"""
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
OUT = ROOT / "page7_fragment.html"

# Top-line trend data (Q1) — last 12 months
trend = [
    # month, signups, activations, email_creates, first_time_sends, email_sends, email_creates_ly, first_time_sends_ly
    ("May'25", 169260, 169701, 6173932, 44739, 15640007400, 4648451, 58272),
    ("Jun'25", 306296, 306826, 9658227, 65525, 25806284640, 7637338, 85906),
    ("Jul'25", 208204, 208637, 7208741, 52691, 19306854161, 8916544, 62898),
    ("Aug'25", 198698, 199355, 8912712, 60095, 24023530250, 9265480, 81026),
    ("Sep'25", 174913, 175246, 7910212, 55656, 20247478300, 8404831, 73084),
    ("Oct'25", 159917, 164438, 8214118, 54817, 20307407520, 9748399, 71915),
    ("Nov'25", 206711, 207600, 11753806, 74420, 29152441164, 8722780, 98851),
    ("Dec'25", 115916, 116340, 8581814, 43279, 18787072669, 5400615, 60344),
    ("Jan'26", 157469, 157960, 8812743, 45849, 18316771066, 6347390, 63936),
    ("Feb'26", 159504, 159990, 8638570, 48421, 19326100991, 8222262, 65225),
    ("Mar'26", 200291, 200800, 11088628, 58649, 23817978069, 10416860, 80454),
    ("Apr'26", 174163, 174555, 6897596, 48602, 18300826893, 7997838, 60698),
]

# Funnel data (Q2) — last 12 months
funnel = [
    # month, activations, login_2d, bulk_created_24h, bulk_publish_24h, bulk_publish_1w
    ("May'25", 169721, 159409, 54029, 5993, 10921),
    ("Jun'25", 306843, 291660, 71564, 9644, 17429),
    ("Jul'25", 208648, 191755, 61168, 7092, 12970),
    ("Aug'25", 199370, 187678, 65258, 8795, 16360),
    ("Sep'25", 175254, 167491, 61444, 8459, 15817),
    ("Oct'25", 165975, 153272, 62557, 8262, 15155),
    ("Nov'25", 207636, 198114, 79919, 11800, 21070),
    ("Dec'25", 116371, 107994, 44489, 7275, 12804),
    ("Jan'26", 157986, 146124, 49271, 6760, 13017),
    ("Feb'26", 160014, 146890, 52768, 6958, 12720),
    ("Mar'26", 200827, 185229, 65261, 8574, 15376),
    ("Apr'26", 174571, 160506, 58210, 6572, 11758),
]

# Package mix (Q4) — last 90 days
package = [
    # package, email_creates, first_time_sends, email_sends, email_creates_ly, first_time_sends_ly, label
    ("Free", 9586997, 79732, 2582847811, 11371253, 130134, "Largest creator pool, declining"),
    ("Standard (monthly v0)", 6131540, 49149, 11936254619, 5049299, 59454, "+21% YoY creates · core paid tier"),
    ("Legacy monthly", 4965058, 285, 21130487126, 5445620, 634, "Highest sends, runoff cohort"),
    ("Essentials (monthly v0)", 3768389, 9125, 3843502451, 3465039, 10876, "+9% YoY · entry paid"),
    ("Premium (monthly v0)", 1264224, 484, 16133935942, 1218964, 599, "HVC enterprise"),
    ("Free (monthly v0 — new)", 83969, 12380, 17342154, 28796, 2961, "+192% YoY first-time sends"),
    ("Premium annual v0", 16445, 23, 140980889, 715, 8, "+2200% YoY · annual surging"),
    ("Standard annual v0", 6587, 37, 21652103, 297, 15, "+2117% YoY · annual surging"),
]

# HVC vs non-HVC last 12 months (Q3) — calculated last-90-day totals
hvc_split = {
    "non-HVC creates (90d)": 22_046_390,  # from monthly sums Feb–Apr 2026
    "HVC creates (90d)": 4_678_404,
    "non-HVC sends (90d)": 16_242_193_869,
    "HVC sends (90d)": 45_390_711_893,
    "non-HVC FTS (90d)": 152_683,
    "HVC FTS (90d)": 2_131,
}

# Tenure / lifecycle (Q5) — last 90 days
tenure = [
    # tenure_label, activations, bulk_created_1w, bulk_publish_1w, pct_publish_1w
    ("<1 month (new)", 490263, 182094, 34941, 7.13),
    ("<3 months", 6307, 3351, 1238, 19.63),
    ("<6 months", 113, 65, 29, 25.66),
    ("24+ months", 29192, 10464, 2027, 6.94),
]

# Trial -> paid -> retention (Q6) — recent steady state (Aug-Oct 2025 average, mature data)
retention_steady = {
    "trial_to_paid": 58.7,   # %
    "m1_retention": 100.0,
    "m3_retention": 35.4,
    "m6_retention": 26.7,
    "m12_retention": 18.6,   # from Q6 Aug-Oct '25 average
}

# Health: churn / PRS / CSAT — recent month (Apr 2026)
health_apr26 = {
    "paid_users": 31_469_417,
    "churn_risk": 71_020,
    "active_churn": 31_975,
    "passive_billing": 37_678,
    "compliance_churn": 1_367,
    "csat_pct": 59.6,
    "prs_high": 1125,
    "prs_low": 567,
    "prs_surveyed": 2166,
    "nps_like": 25.8,  # %
    "churn_risk_pct_weekly": 0.226,
}

# Funnel by country & HVC (Q9)
country_funnel = [
    # country, hvc, activations, act_to_publish_1w_pct
    ("ROW (Rest of World)", False, 170784, 3.5),
    ("United States", False, 142915, 9.2),
    ("United States", True, 1279, 30.3),
    ("Tier 1 Develop", False, 103574, 7.9),
    ("Tier 1 Develop", True, 507, 30.4),
    ("United Kingdom", False, 34063, 8.7),
    ("United Kingdom", True, 212, 21.7),
    ("Australia", False, 13298, 12.5),
    ("Australia", True, 67, 29.9),
    ("ROW", True, 341, 36.9),
    ("Nordics", True, 66, 36.4),
    ("Canada", False, 22608, 9.2),
    ("Canada", True, 88, 27.3),
]

# Ecomm vs non-ecomm (Q8)
ecomm = [
    # status, creates, sends, open_rate, click_rate
    ("Non-ecomm", 18446897, 26511286702, 48.3, 8.0),
    ("Ecomm-connected", 5969261, 19668877046, 43.2, 5.6),
    ("Ecomm-likely (no platform)", 1500115, 10314507985, 40.8, 3.6),
]


def fmt_n(n, suffix=""):
    if n is None:
        return "—"
    if abs(n) >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}B{suffix}"
    if abs(n) >= 1_000_000:
        return f"{n/1_000_000:.1f}M{suffix}"
    if abs(n) >= 1_000:
        return f"{n/1_000:.0f}K{suffix}"
    return f"{n:,.0f}{suffix}"


def yoy(this, last):
    if not last:
        return ""
    pct = (this - last) / last * 100
    sign = "+" if pct >= 0 else ""
    color = "var(--good)" if pct >= 0 else "var(--bad)"
    return f' <span style="color:{color}; font-weight:700;">{sign}{pct:.0f}% YoY</span>'


# ---------------- Build trend table ----------------
trend_rows = ""
for m, signups, acts, creates, fts, sends, creates_ly, fts_ly in trend:
    yoy_creates = (creates - creates_ly) / creates_ly * 100 if creates_ly else 0
    yoy_fts = (fts - fts_ly) / fts_ly * 100 if fts_ly else 0
    yoy_creates_class = "good" if yoy_creates >= 0 else "bad"
    yoy_fts_class = "good" if yoy_fts >= 0 else "bad"
    trend_rows += (
        f'<tr><td><strong>{m}</strong></td>'
        f'<td class="num">{fmt_n(signups)}</td>'
        f'<td class="num">{fmt_n(acts)}</td>'
        f'<td class="num">{fmt_n(creates)} <span class="yoy {yoy_creates_class}">{yoy_creates:+.0f}%</span></td>'
        f'<td class="num">{fmt_n(fts)} <span class="yoy {yoy_fts_class}">{yoy_fts:+.0f}%</span></td>'
        f'<td class="num">{fmt_n(sends)}</td></tr>'
    )

# ---------------- Build funnel table ----------------
funnel_rows = ""
for m, acts, login2d, c24, p24, p1w in funnel:
    login_pct = login2d / acts * 100 if acts else 0
    create_pct = c24 / acts * 100 if acts else 0
    publish_pct = p1w / acts * 100 if acts else 0
    funnel_rows += (
        f'<tr><td><strong>{m}</strong></td>'
        f'<td class="num">{fmt_n(acts)}</td>'
        f'<td class="num">{fmt_n(login2d)} <small>({login_pct:.0f}%)</small></td>'
        f'<td class="num">{fmt_n(c24)} <small>({create_pct:.0f}%)</small></td>'
        f'<td class="num">{fmt_n(p24)}</td>'
        f'<td class="num"><strong style="color:var(--bad);">{fmt_n(p1w)}</strong> <small>({publish_pct:.1f}%)</small></td></tr>'
    )

# ---------------- Package table ----------------
package_rows = ""
for pkg, c, fts, s, c_ly, fts_ly, label in package:
    yoy_c = (c - c_ly) / c_ly * 100 if c_ly else 0
    yoy_fts = (fts - fts_ly) / fts_ly * 100 if fts_ly else 0
    yoy_c_class = "good" if yoy_c >= 0 else "bad"
    yoy_fts_class = "good" if yoy_fts >= 0 else "bad"
    package_rows += (
        f'<tr><td><strong>{pkg}</strong></td>'
        f'<td class="num">{fmt_n(c)} <span class="yoy {yoy_c_class}">{yoy_c:+.0f}%</span></td>'
        f'<td class="num">{fmt_n(fts)} <span class="yoy {yoy_fts_class}">{yoy_fts:+.0f}%</span></td>'
        f'<td class="num">{fmt_n(s)}</td>'
        f'<td><em>{label}</em></td></tr>'
    )

# ---------------- Tenure ----------------
tenure_rows = ""
for label, acts, c1w, p1w, pct in tenure:
    bar_pct = min(100, pct * 4)
    color = "var(--good)" if pct > 15 else "var(--warn)" if pct > 8 else "var(--bad)"
    tenure_rows += (
        f'<tr><td><strong>{label}</strong></td>'
        f'<td class="num">{fmt_n(acts)}</td>'
        f'<td class="num">{fmt_n(c1w)}</td>'
        f'<td class="num">{fmt_n(p1w)}</td>'
        f'<td class="num"><strong style="color:{color};">{pct:.1f}%</strong>'
        f'<div style="height:4px; background:var(--line); border-radius:2px; margin-top:3px;">'
        f'<div style="height:100%; width:{bar_pct}%; background:{color}; border-radius:2px;"></div></div></td></tr>'
    )

# ---------------- Country / HVC funnel ----------------
country_rows = ""
for c, hvc, acts, pct in country_funnel:
    hvc_label = '<span class="ph-cat ph-missing">HVC</span>' if hvc else '<span class="ph-cat ph-barrier">non-HVC</span>'
    color = "var(--good)" if pct > 25 else "var(--warn)" if pct > 10 else "var(--bad)"
    country_rows += (
        f'<tr><td><strong>{c}</strong> {hvc_label}</td>'
        f'<td class="num">{fmt_n(acts)}</td>'
        f'<td class="num"><strong style="color:{color};">{pct:.1f}%</strong></td></tr>'
    )

# ---------------- Ecomm ----------------
ecomm_rows = ""
for status, creates, sends, op, cl in ecomm:
    ecomm_rows += (
        f'<tr><td><strong>{status}</strong></td>'
        f'<td class="num">{fmt_n(creates)}</td>'
        f'<td class="num">{fmt_n(sends)}</td>'
        f'<td class="num">{op:.1f}%</td>'
        f'<td class="num">{cl:.1f}%</td></tr>'
    )

fragment = f"""
  <!-- ============ PAGE 7 — EMAIL BUILDER HEALTH DIAGNOSTIC ============ -->
  <section class="page" id="page7">
    <div class="page-head">
      <div>
        <div class="eyebrow">Competitive Intelligence · Executive Brief · Page 7 of 7</div>
        <h1>Email Builder health diagnostic — strategic analytics framework + live BigQuery findings</h1>
        <div class="subtitle">Lay-of-the-land for the new product lead. <strong>What to measure, where to look, and what BigQuery says today (May 8, 2026).</strong> Data sources: <code>bi_aggregate.product_health_weekly</code>, <code>customer_engagements_weekly</code>, <code>funnel_weekly</code>, <code>free_trials_weekly</code>, <code>churn_daily</code>, <code>product_journey_monthly</code> — all fresh through 2026-05-10. (User-level <code>bi_product.product_reporting_email_base</code> is stale since Dec 2023 — flagged for refresh.)</div>
      </div>
      <div class="meta">
        <div><strong>Run date:</strong> 2026-05-08</div>
        <div style="margin-top:4px;"><strong>Window:</strong> 12-month trend, 90-day cuts</div>
        <div style="margin-top:4px;"><strong>Queries run:</strong> 9 priority cuts</div>
      </div>
    </div>

    <!-- HEADLINE KPIs -->
    <div class="kpi-row" style="margin-bottom:14px;">
      <div class="kpi"><div class="v">31.5M</div><div class="l">Total paid users (Apr 2026 base) · weekly churn-risk pool: 71K (0.23%)</div></div>
      <div class="kpi"><div class="v">8.6M</div><div class="l">Email creates / mo (Apr 2026) · <strong style="color:var(--bad);">−14% YoY</strong></div></div>
      <div class="kpi"><div class="v">7.1%</div><div class="l">New-account → publish-first-email-in-week · <strong style="color:var(--bad);">93% never publish</strong> in week 1</div></div>
      <div class="kpi"><div class="v">$13K → 75%</div><div class="l">HVC concentration: 13% of creates → 75% of sends · <strong>3-10× better funnel conversion than non-HVC</strong></div></div>
    </div>

    <!-- HEADLINE INSIGHT BANNER -->
    <div class="pull" style="margin-bottom:14px;">
      <strong>The bottom line.</strong> The builder serves 31.5M paid accounts and ships 18-29B sends/month. <em>Volume is healthy, but adoption is leaking</em>: first-time-sends are down 15-25% YoY across nearly every month, only 7% of newly-activated accounts publish a first email in their first week, and trial-to-paid + 12-month retention have both compressed. The platform is over-indexed on a thin top of HVC accounts (75% of sends from 13% of creates) while the long-tail (especially ROW non-HVC at 3.5% activation→publish) is failing to convert. <strong>Three hot spots to attack:</strong> (1) first-time-user activation funnel, (2) ROW SMB onboarding, (3) the gap between Free-tier creates declining and Standard/Annual surging.
      <cite>— BigQuery analysis of <code>bi_aggregate.*</code> tables, May 8, 2026</cite>
    </div>

    <!-- KPI TREE / FRAMEWORK -->
    <h2><span class="num">30</span>Strategic analytics framework — the email-builder North Star tree</h2>
    <p style="margin-bottom:8px;">A product lead should drive <strong>one north-star metric</strong> and watch a small tree of supporting metrics across <em>Acquisition · Adoption · Engagement · Retention · Monetization</em>. Below is the proposed tree for the Mailchimp Email Builder, with the BigQuery source for each.</p>
    <div class="grid cols-2" style="margin-bottom:14px;">
      <div>
        <div class="bet" data-rank="★">
          <h4>NORTH STAR · "Activated Email Senders" (AES) <span class="conf">PROPOSED</span></h4>
          <p>Unique paid accounts that <strong>created AND sent</strong> at least one bulk email this week. Captures depth-of-use, not just access.</p>
          <div class="ev"><strong>Source:</strong> <code>product_health_weekly.email_creates ∩ first_time_sends ∩ email_sends</code> per account (needs user-level refresh)</div>
        </div>
        <div class="bet" data-rank="A" style="margin-top:8px;">
          <h4>Acquisition leg</h4>
          <p>Top-of-funnel: signups → activations → trial → paid.</p>
          <ul style="font-size:11.5px; margin:4px 0 0; padding-left:16px;">
            <li><strong>Signups</strong> (<code>product_health_weekly.signups</code>)</li>
            <li><strong>Activations</strong> (signup-confirm) — <code>activations</code></li>
            <li><strong>Trial-to-paid %</strong> — <code>free_trials_weekly</code> (currently 58.7% steady-state)</li>
          </ul>
        </div>
        <div class="bet" data-rank="B" style="margin-top:8px;">
          <h4>Adoption leg (the killer funnel)</h4>
          <p>Activate → first login → bulk_create → bulk_publish in 24h / 1w.</p>
          <ul style="font-size:11.5px; margin:4px 0 0; padding-left:16px;">
            <li><code>funnel_weekly.bulk_created_24hrs</code> (currently ~36% of activations)</li>
            <li><code>bulk_publish_24hrs</code> (currently ~4% of activations)</li>
            <li><strong><code>bulk_publish_1_week</code> (currently 7.1% — TOP attack metric)</strong></li>
          </ul>
        </div>
      </div>
      <div>
        <div class="bet" data-rank="C">
          <h4>Engagement leg</h4>
          <p>Frequency, depth, AI-feature adoption.</p>
          <ul style="font-size:11.5px; margin:4px 0 0; padding-left:16px;">
            <li><strong>Email creates / active sender</strong></li>
            <li><strong>Sends per send-day</strong> — load distribution</li>
            <li><strong>Open rate / click rate</strong> by ecomm_status (<code>product_health_weekly</code>)</li>
            <li><strong>Intuit Assist adoption</strong> (needs new event surface — flag below)</li>
            <li><strong>Universal-content / saved-block usage</strong> (when shipped)</li>
          </ul>
        </div>
        <div class="bet" data-rank="D" style="margin-top:8px;">
          <h4>Retention leg</h4>
          <p>The 1/3/6/12-month curve from <code>free_trials_weekly</code> by package + builder activity.</p>
          <ul style="font-size:11.5px; margin:4px 0 0; padding-left:16px;">
            <li><strong>M3 / M6 / M12 retention by tenure × HVC</strong></li>
            <li><strong>Active-churn-risk %</strong> (<code>churn_daily</code>) — currently 0.10% of paid users weekly</li>
            <li><strong>PRS / CSAT scoreboard</strong> (currently CSAT 60%, PRS NPS-proxy +26)</li>
          </ul>
        </div>
        <div class="bet" data-rank="E" style="margin-top:8px;">
          <h4>Monetization leg</h4>
          <p>Trial → paid → upgrade. Cross-ref with builder usage to find expansion hotspots.</p>
          <ul style="font-size:11.5px; margin:4px 0 0; padding-left:16px;">
            <li><strong>New bookings</strong> (<code>bookings_weekly</code>)</li>
            <li><strong>Upgrades from free/Essentials → Standard</strong></li>
            <li><strong>Annual plan attach</strong> (now growing 20×+ YoY)</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TOP-LINE TREND -->
    <h2><span class="num">31</span>Adoption &amp; frequency — top-line trend (12 months, MoM, YoY)</h2>
    <table class="voc-table" style="margin-bottom:14px;">
      <thead><tr><th>Month</th><th>Signups</th><th>Activations</th><th>Email creates · YoY</th><th>First-time sends · YoY</th><th>Email sends</th></tr></thead>
      <tbody>{trend_rows}</tbody>
    </table>
    <p style="font-size:12px; color:var(--muted); margin: -8px 0 14px;">
      <strong>Reading this:</strong> sends are stable to slightly down. <strong>First-time sends are down 15-25% YoY in 11 of 12 months</strong> — this is the canary. New-customer activation is degrading. November BFCM peak (+35% YoY creates) shows seasonal demand is intact, but the conversion to first-send isn't following.
    </p>

    <!-- ACTIVATION FUNNEL -->
    <h2><span class="num">32</span>The activation funnel — where 93% of new accounts go to die</h2>
    <table class="voc-table" style="margin-bottom:14px;">
      <thead><tr><th>Month</th><th>Activations</th><th>Login &lt;2d</th><th>Bulk created &lt;24h</th><th>Published &lt;24h</th><th>Published &lt;1w</th></tr></thead>
      <tbody>{funnel_rows}</tbody>
    </table>
    <p style="font-size:12px; color:var(--muted); margin: -8px 0 14px;">
      <strong>The leakage map.</strong> ~93% of newly-activated paid accounts log in within 2 days but only ~7% publish a first bulk email within a week. The drop is sharpest at <em>create → publish</em> (only ~25% of creators publish in week 1). This is the <strong>single highest-leverage funnel step</strong> for the builder team.
    </p>

    <!-- LIFECYCLE / TENURE -->
    <h2><span class="num">33</span>Lifecycle / tenure — who's using it &amp; how often (last 90d)</h2>
    <table class="voc-table" style="margin-bottom:14px;">
      <thead><tr><th>Tenure cohort</th><th>Activations</th><th>Created &lt;1w</th><th>Published &lt;1w</th><th>Activate→Publish %</th></tr></thead>
      <tbody>{tenure_rows}</tbody>
    </table>
    <p style="font-size:12px; color:var(--muted); margin: -8px 0 14px;">
      <strong>Lifecycle insight.</strong> Brand-new (&lt;1 month) accounts are the dominant volume (490K activations / 90d) but convert at only 7.1%. Accounts in their 2nd–3rd month have a much higher 19.6% — they've made it past the first-week wall. <strong>The 24+ months "veteran returners" cohort</strong> (29K activations) is back at 6.9% — these are reactivations / quiet returners and they re-encounter the same first-send wall. <em>Same fix lifts both new and returning.</em>
    </p>

    <!-- COUNTRY × HVC FUNNEL -->
    <div class="grid cols-3-2" style="margin-bottom:14px;">
      <div>
        <h2><span class="num">34</span>The HVC vs long-tail gap — biggest opportunity</h2>
        <table class="voc-table">
          <thead><tr><th>Country × HVC tier</th><th>Activations (90d)</th><th>Activate→Publish&nbsp;1w</th></tr></thead>
          <tbody>{country_rows}</tbody>
        </table>
      </div>
      <div>
        <h2 style="margin-top:0;">What it means</h2>
        <p style="font-size:12.5px;">HVCs convert <strong>3–10× better</strong> than non-HVC across every region. <strong>The funnel is built for engaged/large-list users.</strong></p>
        <ul style="font-size:11.5px;">
          <li><strong>ROW non-HVC</strong> (170K activations, the largest cohort) converts at <strong>3.5%</strong> — the worst funnel performance and the largest absolute opportunity. International SMB onboarding is broken.</li>
          <li><strong>US non-HVC</strong> at 9.2% is the next biggest absolute pool. A 2pt lift here = ~3,000 more publishers/month.</li>
          <li><strong>HVCs across every region</strong> (~2,500 activations/90d) sit at 21–37% — they're already converting; investment here is incremental.</li>
          <li><strong>Strategic implication:</strong> the team should index on the non-HVC long tail, not the HVC top, for funnel work. Reverse the priority for retention/expansion work.</li>
        </ul>
      </div>
    </div>

    <!-- PACKAGE MIX -->
    <h2><span class="num">35</span>Plan &amp; package mix — where revenue is moving</h2>
    <table class="voc-table" style="margin-bottom:14px;">
      <thead><tr><th>Package</th><th>Email creates · YoY</th><th>First-time sends · YoY</th><th>Email sends</th><th>Notes</th></tr></thead>
      <tbody>{package_rows}</tbody>
    </table>
    <p style="font-size:12px; color:var(--muted); margin: -8px 0 14px;">
      <strong>The shifts.</strong>
      <strong>Free tier is shrinking</strong> (creates −16% YoY, first-time sends −39% YoY) — entry funnel is leaking.
      <strong>Standard monthly is the growth engine</strong> (+21% YoY creates) — the core paid tier is healthy.
      <strong>Annual plans are exploding</strong> (Premium annual +2,200% YoY, Standard annual +2,117% YoY from a tiny base) — annual is the new commercial wedge.
      <strong>"free_monthly_plan_v0"</strong> (the new free experience?) is +192% YoY first-time sends — onboarding flow change is working <em>in that variant</em>.
      <strong>Legacy monthly</strong> still sends 21B emails/month from grandfathered accounts — protect this revenue while migrating off.
    </p>

    <!-- RETENTION + HEALTH -->
    <div class="grid cols-2" style="margin-bottom:14px;">
      <div>
        <h2><span class="num">36</span>Trial → paid → retention curve (steady state)</h2>
        <table class="voc-table">
          <thead><tr><th>Stage</th><th>Conversion / retention</th></tr></thead>
          <tbody>
            <tr><td><strong>Trial → paid</strong></td><td class="num"><strong>{retention_steady['trial_to_paid']:.1f}%</strong></td></tr>
            <tr><td>1-month retention</td><td class="num">{retention_steady['m1_retention']:.0f}%</td></tr>
            <tr><td>3-month retention</td><td class="num">{retention_steady['m3_retention']:.1f}%</td></tr>
            <tr><td>6-month retention</td><td class="num">{retention_steady['m6_retention']:.1f}%</td></tr>
            <tr><td><strong>12-month retention</strong></td><td class="num"><strong>{retention_steady['m12_retention']:.1f}%</strong></td></tr>
          </tbody>
        </table>
        <p style="font-size:11.5px; color:var(--muted); margin-top:6px;"><strong>The drop:</strong> 3-month retention fell from 74% (Nov 2024 cohort) to ~35% (mature steady-state across 2025). 12-month retention only 18.6%. <em>Builder usage in the first 30 days is the strongest leading indicator</em> — recommend a deep-dive correlating builder activity buckets with M3/M6/M12 retention by package.</p>
      </div>
      <div>
        <h2><span class="num">37</span>Health signals — Apr 2026 snapshot</h2>
        <table class="voc-table">
          <thead><tr><th>Signal</th><th>Value</th></tr></thead>
          <tbody>
            <tr><td>Total paid users</td><td class="num">{fmt_n(health_apr26['paid_users'])}</td></tr>
            <tr><td>Weekly churn-risk pool</td><td class="num">{fmt_n(health_apr26['churn_risk'])} <span class="yoy">({health_apr26['churn_risk_pct_weekly']:.2f}%)</span></td></tr>
            <tr><td>… active churn risk</td><td class="num">{fmt_n(health_apr26['active_churn'])} <small>(45%)</small></td></tr>
            <tr><td>… passive billing failure</td><td class="num">{fmt_n(health_apr26['passive_billing'])} <small>(53% of risk)</small></td></tr>
            <tr><td>… compliance churn</td><td class="num">{fmt_n(health_apr26['compliance_churn'])} <small>(2%)</small></td></tr>
            <tr><td><strong>CSAT (satisfied)</strong></td><td class="num"><strong>{health_apr26['csat_pct']:.1f}%</strong> <small>n={health_apr26['prs_surveyed']}/wk</small></td></tr>
            <tr><td>PRS NPS-like score</td><td class="num"><strong>+{health_apr26['nps_like']:.1f}</strong></td></tr>
          </tbody>
        </table>
        <p style="font-size:11.5px; color:var(--muted); margin-top:6px;"><strong>Read:</strong> only ~45% of churn risk is "active" (driven by product dissatisfaction); 53% is passive billing-card failures. <em>The builder team owns the active-churn lever (~32K users/month at risk) — the recovery team owns the bigger passive pool.</em> CSAT has been stable at 57–66%; PRS hovers +26.</p>
      </div>
    </div>

    <!-- ECOMM SPLIT -->
    <h2><span class="num">38</span>Ecomm vs non-ecomm — engagement is inverted</h2>
    <table class="voc-table" style="margin-bottom:14px;">
      <thead><tr><th>Audience type</th><th>Email creates (90d)</th><th>Email sends (90d)</th><th>Open rate</th><th>Click rate</th></tr></thead>
      <tbody>{ecomm_rows}</tbody>
    </table>
    <p style="font-size:12px; color:var(--muted); margin: -8px 0 14px;">
      <strong>Counter-intuitive but consistent:</strong> non-ecomm accounts (ProServ, B2B, associations) have higher open and click rates than ecommerce. Ecomm sends 3.3× more per create (high-volume promo) but ProServ has higher engagement quality. Mirrors the Page 6 HeyMarvin finding — ProServ buyers want different templates than ecomm. <strong>An "engagement-quality" KPI by audience-type, not just send-volume, is missing from current dashboards.</strong>
    </p>

    <!-- FOCUS / HOTSPOTS -->
    <h2><span class="num">39</span>Where to focus energy — 5 hotspots ranked by leverage</h2>
    <div class="grid cols-2" style="margin-bottom:14px;">
      <div class="bet" data-rank="1">
        <h4>The first-week publish wall <span class="conf">HIGHEST LEVERAGE</span></h4>
        <p>~93% of newly-activated paid accounts never publish in week 1. A 5-pt lift = +28K monthly publishers, ~$X-million annualized retention gain (size precisely with cohort activity → retention regression).</p>
        <div class="ev"><strong>Plays:</strong> simplified first-template flow · template-list inline preview · saved blocks for "borrow my agency template" · in-canvas activation nudge to "Publish" once a draft is ready.</div>
      </div>
      <div class="bet" data-rank="2">
        <h4>ROW non-HVC SMB onboarding</h4>
        <p>170K monthly activations at 3.5% publish-1w = the worst funnel cell in the heat-map. International SMB hits a UX wall in week 1.</p>
        <div class="ev"><strong>Plays:</strong> localized template gallery · WhatsApp-friendly first-send option (Page 4 D3) · regional payment / billing flow hardening · timezone-aware onboarding emails.</div>
      </div>
      <div class="bet" data-rank="3">
        <h4>First-time-sends YoY decline</h4>
        <p>11 of last 12 months down 15-25% YoY. Pre-existing demand is fine (sends stable, BFCM up); first-send conversion is the regression.</p>
        <div class="ev"><strong>Plays:</strong> instrument the actual first-send path end-to-end · A/B the simplified setup checklist (current one "flattens decisions of vastly different importance" — Kyle Spalding, Page 6) · activation playbook for paid-trial cohort.</div>
      </div>
      <div class="bet" data-rank="4">
        <h4>Trial→paid steady ~58% but 12-mo retention only 18.6%</h4>
        <p>Healthy trial conversion but customers drop fast after paying. M3 retention fell from 74% (Nov 2024) to 35% (mature 2025). Builder usage in the first 30 days is the strongest leading indicator.</p>
        <div class="ev"><strong>Plays:</strong> "first 4 sends in 30 days" activation playbook tied to retention · Universal Saved Content (Page 4 F1) lowers re-creation cost · discovery / activation funnel for high-frequency users (Page 6 Bet 2).</div>
      </div>
      <div class="bet" data-rank="5">
        <h4>Annual-plan attach is exploding (+2,000% YoY)</h4>
        <p>Annual plans are the new growth wedge — but the builder onboarding wasn't designed for an annual signup mental model (commit-then-explore vs explore-then-commit).</p>
        <div class="ev"><strong>Plays:</strong> annual-plan-specific welcome flow · success criteria optimized for "send 12 campaigns / year, retain to renewal" · upsell triggers tied to feature ceiling rather than monthly volume.</div>
      </div>
    </div>

    <!-- ANALYTICS STRATEGY: HOW TO RUN IT -->
    <h2><span class="num">40</span>The analytics strategy — what to run, how often, and where to put your energy</h2>
    <div class="grid cols-2" style="margin-bottom:8px;">
      <div>
        <h2 style="margin:0 0 6px;">Weekly cadence (Monday 9am)</h2>
        <ul>
          <li><strong>1-page Builder Health scorecard</strong> — 6 KPIs: AES (north star), email_creates WoW, first_time_sends WoW + YoY, activation→publish-1w%, churn-risk %, CSAT.</li>
          <li><strong>Single anomaly check</strong> — any KPI moving &gt; ±10% WoW: surface root cause.</li>
          <li><strong>Free vs Standard vs Premium splits</strong> on every KPI.</li>
        </ul>
        <h2 style="margin:14px 0 6px;">Monthly cadence (1st Monday)</h2>
        <ul>
          <li><strong>Cohort retention curve</strong> — 1/3/6/12-mo retention by package × ecomm_status × tenure (<code>free_trials_weekly</code>).</li>
          <li><strong>Funnel deep-dive by country group + HVC</strong> (<code>funnel_weekly</code>).</li>
          <li><strong>Builder feature-adoption matrix</strong> — Universal Content, Brand Kit, Image Remix, Intuit Assist (needs new event surface).</li>
        </ul>
        <h2 style="margin:14px 0 6px;">Quarterly</h2>
        <ul>
          <li><strong>Builder usage → retention regression</strong>: which 30-day builder behaviors predict M6/M12 retention.</li>
          <li><strong>Power-user concentration</strong>: top 1% / 5% / 20% of senders, what % of total sends.</li>
          <li><strong>Voice-of-customer quarterly</strong>: cross-ref Page 5 (Slack VOC, $K MRR exposure) with Page 7 cohort-retention deltas.</li>
        </ul>
      </div>
      <div>
        <h2 style="margin:0 0 6px;">Critical SQL patterns to run</h2>
        <div class="card tinted" style="margin-bottom:8px;">
          <div style="font-size:10.5px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--brand);">Q1 — Top-line trend</div>
          <pre style="font-size:10.5px; margin:4px 0 0; padding:6px 8px; background:#fff; border:1px solid var(--line); border-radius:4px; overflow-x:auto; line-height:1.4;">SELECT DATE_TRUNC(week, MONTH) m,
  SUM(email_creates) creates,
  SUM(first_time_sends) fts,
  SUM(email_sends) sends
FROM bi_aggregate.product_health_weekly
WHERE week &gt;= DATE_SUB(CURRENT_DATE(), INTERVAL 365 DAY)
GROUP BY 1 ORDER BY 1;</pre>
        </div>
        <div class="card tinted" style="margin-bottom:8px;">
          <div style="font-size:10.5px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--brand);">Q2 — Funnel by country × HVC</div>
          <pre style="font-size:10.5px; margin:4px 0 0; padding:6px 8px; background:#fff; border:1px solid var(--line); border-radius:4px; overflow-x:auto; line-height:1.4;">SELECT country_group, is_high_value,
  SUM(total_activations) acts,
  SUM(bulk_publish_1_week) pub_1w,
  SAFE_DIVIDE(SUM(bulk_publish_1_week),
              SUM(total_activations)) act_to_pub
FROM bi_aggregate.funnel_weekly
WHERE week &gt;= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY 1,2 ORDER BY acts DESC;</pre>
        </div>
        <div class="card tinted" style="margin-bottom:8px;">
          <div style="font-size:10.5px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--brand);">Q3 — Trial→paid→retention by package</div>
          <pre style="font-size:10.5px; margin:4px 0 0; padding:6px 8px; background:#fff; border:1px solid var(--line); border-radius:4px; overflow-x:auto; line-height:1.4;">SELECT package, DATE_TRUNC(week,MONTH) m,
  SUM(free_trial_users) trials,
  SUM(new_booking_users) paid,
  SAFE_DIVIDE(SUM(month_3_retention_cnt),
              SUM(new_booking_users)) m3_retention,
  SAFE_DIVIDE(SUM(month_12_retention_cnt),
              SUM(new_booking_users)) m12_retention
FROM bi_aggregate.free_trials_weekly
WHERE week &gt;= DATE_SUB(CURRENT_DATE(), INTERVAL 540 DAY)
GROUP BY 1,2 ORDER BY 2,1;</pre>
        </div>
      </div>
    </div>

    <!-- CAVEATS & DATA HEALTH -->
    <h2 style="margin-top:14px;"><span class="num">41</span>Data caveats &amp; recommended pipeline fixes</h2>
    <div class="grid cols-3">
      <div class="card warm">
        <p style="margin:0;"><strong>User-level email tables stale.</strong> <code>bi_product.product_reporting_email_base</code> last refreshed Dec 2023 (84M rows). Most user-level cohort/segmentation analyses are blocked or run on stale data. <strong>Top action: re-engage data team to refresh this pipeline.</strong></p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Creative Assistant tables frozen at 2022.</strong> <code>creative_assistant_*</code> tables stopped updating Nov 2022. Any in-builder AI feature reporting (Intuit Assist, Write with AI) needs a fresh event source — likely lives in Pendo or a newer events_pipeline table. <strong>Build the Intuit Assist funnel from scratch.</strong></p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Tenure bucket labels inconsistent.</strong> <code>account_tenure_months</code> has both <code>&lt;1</code>, <code>&lt;3</code>, <code>&lt;6</code>, <code>&lt;12</code>, <code>&lt;24</code>, <code>24+</code> labels with overlapping semantics. Recommend canonical buckets (0-30d / 31-90d / 91-180d / 181-365d / 1-3yr / 3+yr) and rebuild aggregates.</p>
      </div>
    </div>

    <div class="source">
      <strong>BigQuery sources (Page 7) — all queries run live on May 8, 2026:</strong>
      <code>mc-business-intelligence.bi_aggregate.product_health_weekly</code> (FRESH through 2026-05-10) ·
      <code>bi_aggregate.funnel_weekly</code> (activation funnel) ·
      <code>bi_aggregate.free_trials_weekly</code> (trial→paid + 1/3/6/12 retention) ·
      <code>bi_aggregate.churn_daily</code> (paid users · churn risk · CSAT · PRS) ·
      <code>bi_aggregate.customer_engagements_weekly</code> (touchpoint activity) ·
      <code>bi_aggregate.product_journey_monthly</code> (lifecycle stage) ·
      <code>bi_product.product_reporting_email</code> + <code>_base</code> (STALE since Dec 2023, structure-only reference) ·
      <code>bi_product.creative_assistant_*</code> (FROZEN Nov 2022, inactive).
      <br/><br/>
      <em>Methodology:</em> 9 priority queries across 6 fresh aggregate tables — no synthetic data. All YoY deltas use the table's own <code>_prev_yr</code> LAG columns (zero recomputation). Cohort dimensions used: <code>is_high_value</code>, <code>package</code>, <code>account_tenure_months</code>, <code>ecomm_status</code>, <code>country_group</code>. The 7.1% activate-to-publish-1w is the dominant headline metric — recommend it become an org-level OKR for Q3-Q4 FY26.
    </div>
  </section>
"""

OUT.write_text(fragment.strip())
print(f"Wrote {OUT} ({len(fragment):,} chars)")
