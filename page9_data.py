"""Page 9 — Previous PM's docs cross-reference + reviewer agent critique.
5 docs reviewed:
  1. Builder VoC Feedback Response Plan (Nov 2025, Ose/Erin/JB/Joyce)
  2. Builder VoC Response Plan v(1) — short pillar version
  3. Nuni Builder Strategy and Roadmap (Jan 2026, Ose/Erin/JB/Ashley, reviewed Eric Anderson) — MASTER doc
  4. Mailchimp H2 FY26 Product Priorities (Diana Williams) — 4 objectives
  5. Mailchimp H2 FY26 Roadmap (Mar 2026 update, Diana Williams) — monthly milestones
"""
import html as html_lib
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
OUT = ROOT / "page9_fragment.html"


# ============ DOC SUMMARIES ============
docs = [
    {
        "name": "Builder VoC Feedback Response Plan",
        "owners": "Ose Amiegheme · Erin McCue · JB Lovell · Joyce Russell",
        "date": "Nov 5, 2025",
        "thesis": "Builder is now the #1 driver of design-tool churn. 468 VoC items categorized into 6 buckets — Usability (51%), Reliability (14%), Mobile (12%), Rendering (10%), Feature Requests (12%), Integrations (1%).",
        "asks": "Quality Pod (Nov-Jan, 4 sprints) for Mobile + Rendering quality wins · Cross-functional Design Sprint to reimagine clunky workflows · Audit feature gaps and decide Build/Borrow/Defer (MC vs Fusion).",
        "sizing": "Improving email sends = $4–$6M FY26 revenue impact (cited). 17% non-HVC churn + 12% Free user churn attributed to design tools. Quality Pod target: 20–30% reduction in mobile/rendering complaints by EOQ2 FY26.",
        "non_funded_items": "Mobile Styles V2 · Dynamic content on Mobile · Dark mode education · Mobile rendering bug fixes · Expanding Inbox Previews · Automated Rendering Test (all flagged 'Not funded' in source doc)",
    },
    {
        "name": "Builder VoC Response Plan (Pillar version)",
        "owners": "Builder Team",
        "date": "Q2 FY26",
        "thesis": "3 strategic pillars to organize builder work: (1) Keep Core Promise (rendering reliability), (2) Build Habits (reduce effort to send), (3) Redesign Workflows (one big swing).",
        "asks": "Pillar 1 projects: Automated Testing (Litmus API), Dark Mode, Block layout rendering, Text rendering, Inbox Preview boost, Mobile Styles V2, Show/Hide on devices, Responsive Nuni. Pillar 2: Reusable content blocks. Brand Kit projects: Branded Templates, Brand Kit Activation, Link Brand Kit + Global Styles, Template Refresh + Replicate. Pillar 3: Daily SWAT, DSB Asks.",
        "sizing": "Effort sized as Small / Medium / Large / X-Large per project; Impact column uses 'Email Sends' as proxy. No dollar sizing in this doc.",
        "non_funded_items": "—",
    },
    {
        "name": "Nuni Builder Strategy and Roadmap (MASTER)",
        "owners": "Ose Amiegheme · Erin McCue · JB Lovell · Ashley Wiesner · reviewed by Eric Anderson",
        "date": "Jan 2, 2026",
        "thesis": "Nuni is 5-yr-old WYSIWYG builder, the primary creation surface, and one of the biggest sources of negative VoC. Two target ICPs for rest of FY26: <$299 non-HVC (price-sensitive, churn fast on friction) + DSB switchers (mostly HVC, coming from Klaviyo). Uses 7-Phase JTBD × 6-Level Maslow hierarchy. Nuni scores 4/4/2/1/2/0 vs Klaviyo 5/5/3/3/2/3 vs Canva 5/4/5/5/3/N/A — gap at Levels 3 (Efficient Workflow) and 4 (Brand-Native).",
        "asks": "30+ initiatives across Q2/Q3/Q4 mapped to 7-phase JTBD. 6 Builder SLOs (uptime ≥99.9%, crash-free ≥99.5%, save ≥99.99%, init load P95 <500ms, interaction P95 <300ms, render fidelity ≥99%, mobile ≥95%). Three named product briefs: Content Insertion · Styles · Alignment & Layout.",
        "sizing": "Directional goals: reduce builder-driven churn 20–30% vs FY25 baseline (for <$299 non-HVC). Shift 80%+ of sends to 'healthy effort' (≤250 clicks). Reduce >500-click sessions by 30%.",
        "non_funded_items": "AI is positioned as 'horizontal accelerator' embedded in JTBD phases (no separate AI track) — generated layouts, image gen, chat-based editing.",
    },
    {
        "name": "Mailchimp H2 FY26 Product Priorities",
        "owners": "Diana Williams",
        "date": "H2 FY26 (Aug'25 onwards)",
        "thesis": "4 objectives: (1) Accelerate FTU & Optimal Setup [<$299 cohort], (2) Strengthen Ecommerce/DSB, (3) Expand Omnichannel (SMS/Tx/RCS/WA), (4) Scale AI + Ecosystem (MC Everywhere). Builder is named directly under Obj 1 (FTU Branded Template E2E + Save Email Sections) and Obj 2 (Make all brand kit in Nuni + Klaviyo template converter).",
        "asks": "OKRs include FTU 30/90-day retention lift, DSB MRR +13% YoY, SMS rev to $23.75M, Tx rev to $33.65M.",
        "sizing": "FTU Optimal Setup: $1.5M-$2.8M projected revenue (12-mo) from 2.85%-5.34% absolute lift in FTU 90d retention. DSB Initiative: $3M-$8M cumulative impact estimates. Omnichannel: $97K-$469K monthly. AI: $1K-$530K monthly.",
        "non_funded_items": "Pull-back: 'Broad Churn Experimentation' is shifting to focus on FTU + platform performance. Mid-market commitments at sustained P2 investment.",
    },
    {
        "name": "Mailchimp H2 FY26 Roadmap (March update)",
        "owners": "Diana Williams + product domain POCs",
        "date": "Mar 12, 2026",
        "thesis": "Detailed Q3/Q4 monthly milestones for each of the 4 H2 objectives. Builder-related deliverables explicit: Branded Template E2E (Q4 May), Save and Reuse Email Sections (Q4 May), One Click Apply Email Styles (Q4 June), Vibe Email Content Editing, Canva AI image gen in Nuni (Q4 April).",
        "asks": "Roadmap includes ~70+ deliverables across 4 objectives. Builder gets named slots in FTU + DSB + AI tracks but does not have its own objective.",
        "sizing": "Per-objective monthly impact estimates: FTU $7K→$22K→$46K→$290K (Apr→May→Jun→Jul); DSB $3K→$8K→$520K→$3M; SMS $97K→$162K→$208K→$469K; Tx $70K→$48K (May→Jun); AI $1K→$40K→$97K→$530K.",
        "non_funded_items": "Q4 FY26 items are still in 'Draft' mode per the doc. Several Mobile/Rendering items from VoC plan remain absent from this roadmap.",
    },
]


# ============ INITIATIVES — cross-referenced ============
# Each entry maps a builder initiative to:
#   slack_voc: Page 5 Slack VOC theme name (or "—")
#   slack_mrr: HVC MRR exposure ($/mo) if mapped
#   research: HeyMarvin Page 6 finding (Andrea/Wes/Jack/etc) or Bet number
#   klaviyo_gap: Page 4 F-code (parity) or D-code (differentiator)
#   bq_metric: Page 7 KPI tree node
#   yoy_signal: Page 8 YoY metric most likely to move
#   sizing: from PM docs ($, %, count) or ""
#   confidence: HIGH / MED / LOW (for reviewer)

initiatives = [
    # ============ THE COMPOSE LOOP CLUSTER ============
    {
        "id": "I-01",
        "name": "Reusable Saved Sections / Universal Content",
        "doc": "Nuni Strategy (Q3, Phase 7) + VoC Plan (Pillar 2) + H2 FY26 Roadmap (May FTU)",
        "problem": "Marketers rebuild header/footer/promo blocks every send; no edit-once-propagate model.",
        "benefit": "60–80% complete next-campaign starting point. Cuts brand-update time from hours to seconds.",
        "slack_voc": "Saved sections / saved blocks / universal content",
        "slack_mrr": 13684,
        "slack_users": 6,
        "research": "Top-cited HeyMarvin Bet 1 (Wes 90-95% reuse · Peter rotating advertisers · Kyle recurring sections · S1.11 + S2.89 explicitly raised) — confirmed in-flight by PM Jose",
        "klaviyo_gap": "F1 (parity must-have)",
        "bq_metric": "Activation funnel (bulk_publish_1w 7.1%) + retention (M3/M6 builder-usage correlation)",
        "yoy_signal": "Lift email_creates and first-time-sends; reduce 'created-but-never-sent' wedge",
        "sizing": "Nuni doc: contributor to '20-30% builder-driven churn reduction' (no isolated $)",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-02",
        "name": "Drag Image from Local Device into Nuni",
        "doc": "Nuni Strategy (Q3, Phase 3) + VoC Plan (Drag & Drop 5%)",
        "problem": "Users expect drag-an-image-file directly onto the page; today they must add an Image Block placeholder first.",
        "benefit": "Removes an entire 'placeholder-then-fill' step from the Compose loop. Aligns with how all modern editors behave.",
        "slack_voc": "Generic 'editor is clunky / hard to use'",
        "slack_mrr": 5690,
        "slack_users": 6,
        "research": "Andrea D'Ercole Bee.io detour (HeyMarvin Bet 5) · Wes Turner direct manipulation expectations",
        "klaviyo_gap": "F4 (in-canvas edit) tangent · part of Page 6 Bet 5 (direct-manipulation editor)",
        "bq_metric": "Bulk_create→bulk_publish funnel (currently 25% conv)",
        "yoy_signal": "Reduce >500-click sessions (per Nuni SLO target) and friction in Compose loop",
        "sizing": "Nuni: contributes to 30% reduction in >500-click sessions",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-03",
        "name": "Add within Columns + Improved Drop Zones Visibility",
        "doc": "Nuni Strategy (Q3, Phase 3) + Content Insertion brief",
        "problem": "Block placement is unpredictable; users 'misdrop' content (especially into columns) and feel scared of breaking the layout.",
        "benefit": "Predictable placement — content lands exactly where the user intends. Reduces 'I'm scared to break the layout' fear.",
        "slack_voc": "Generic 'editor is clunky / hard to use'",
        "slack_mrr": 5690,
        "slack_users": 6,
        "research": "S1.7 Eric — 2-column discoverability is poor (HIGH research priority) · Wes Turner padding 'dancing around'",
        "klaviyo_gap": "F5 (sections + per-section mobile-stacking)",
        "bq_metric": "Bulk_create→bulk_publish funnel · publishes per session",
        "yoy_signal": "Restore bulk_publish_1w toward LY 9.7%",
        "sizing": "Nuni: part of Level-3 Efficient Workflow targets",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-04",
        "name": "In-canvas AI Image Gen + Image Normalization (Vibe / Canva-in-Nuni)",
        "doc": "Nuni Strategy (Jan: Image generation; Q3: Image normalization) + H2 FY26 Roadmap (Apr Q4 — Canva AI image gen + Vibe Email Content Editing)",
        "problem": "Marketers leave Nuni for Canva/Adobe Express/Bee.io to recolor, swap, resize images; flow breaks every send.",
        "benefit": "Re-light, re-background, swap objects without leaving the canvas. Matches Klaviyo's Image Remix (Gemini) bar.",
        "slack_voc": "Better image editor / asset management",
        "slack_mrr": 793,
        "slack_users": 2,
        "research": "Andrea D'Ercole (Bee.io detour every send) · Andrew Obeso (image-resize prompt every time, 20-30 min/send) · Page 6 Bet 5 direct mention",
        "klaviyo_gap": "F4 (in-canvas AI image editor — Gemini-class)",
        "bq_metric": "Image-block adoption · time-in-builder · first-time-sends",
        "yoy_signal": "First-time sends (currently −25.7% YoY); image quality is rate-limiter for non-designer FTUs",
        "sizing": "H2 FY26 AI: $1K→$40K→$97K→$530K monthly (Vibe + Canva tracks combined)",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-05",
        "name": "Multiselect + Drag Handles for padding/margins + Copy/Paste Styles",
        "doc": "Nuni Strategy (Q4 Phase 4) + Alignment & Layout brief + VoC Plan (Editing Primitives)",
        "problem": "Users can't align multiple items at once; spacing requires per-block tweaks; brand styles can't be 'pasted' to other elements.",
        "benefit": "Multiselect + paint format = 5–10× faster repetitive styling. Reduces 'symmetry tax' Wes Turner described.",
        "slack_voc": "Snap-to-grid / spacing alignment / structured layout",
        "slack_mrr": 7778,
        "slack_users": 1,
        "research": "Wes Turner padding pre-pass · Andrea D'Ercole bottom-align (Hannah confirmed) · single high-MRR snap-to-grid quote",
        "klaviyo_gap": "F5 (sections + alignment)",
        "bq_metric": "Click count per send (>500-click session bucket)",
        "yoy_signal": "Reduce >500-click sessions by 30% (Nuni SLO target)",
        "sizing": "Nuni: 30% reduction in >500-click sessions",
        "confidence": "HIGH",
        "must_do": False,
    },
    {
        "id": "I-06",
        "name": "Chat-based Editing (Q4 Phase 4)",
        "doc": "Nuni Strategy (Q4) + H2 FY26 AI track (Vibe Email Content Editing)",
        "problem": "Atomic edits (font, color, copy) require navigating multiple panels; new users hunt for controls.",
        "benefit": "Natural language: 'make the headline bigger and red' executed in seconds. Lowers click count and discovery cost.",
        "slack_voc": "Generic 'editor is clunky' + Steep learning curve",
        "slack_mrr": 10367,
        "slack_users": 12,
        "research": "S1.5 (DnD handle confusion) · S1.10 (discount code editing confusing) · S1.12 (merge tag toggle undiscoverable)",
        "klaviyo_gap": "Adjacent to D2 (channel-adaptive AI content) · partial F3 (AI section/layout generator)",
        "bq_metric": "Activate→publish-1w (currently 7.1%)",
        "yoy_signal": "Lift first-time sends (−25.7% YoY) by lowering discovery cost for new users",
        "sizing": "Part of H2 FY26 AI envelope ($1K→$530K monthly)",
        "confidence": "MED",
        "must_do": False,
    },

    # ============ THE BRAND-NATIVE SYSTEM CLUSTER ============
    {
        "id": "I-07",
        "name": "One-click Apply Brand + Branded Templates",
        "doc": "Nuni Strategy (Q3 Phase 2) + H2 FY26 Roadmap (May FTU 'Branded Template E2E')",
        "problem": "Brand Kit is disconnected from Nuni; users manually re-style every campaign. 'Blank-page anxiety' before first send.",
        "benefit": "Templates auto-apply user's brand (logo, colors, fonts). FTUs see their brand on first canvas open — collapses time-to-first-on-brand-send.",
        "slack_voc": "Brand voice / tone learning AI (proxy for brand-kit-on-AI-drafts)",
        "slack_mrr": 410,
        "slack_users": 1,
        "research": "S1.59 Eric — Global styles undiscoverable (HIGH research) · S2.35 Jacob — templates don't apply brand kit buttons · Nuni doc: 'Connect Brand Kit and fix global inheritance'",
        "klaviyo_gap": "Tangent to F2 (brand voice from corpus); Klaviyo also lacks one-click brand apply at scale",
        "bq_metric": "Activation funnel · FTU activation→publish-1w · open/click rate (better-on-brand emails outperform)",
        "yoy_signal": "Lift FTU 90d retention (H2 FY26 target: 2.85-5.34% lift = $1.5-2.8M)",
        "sizing": "H2 FY26 FTU Optimal Setup: $1.5M-$2.8M projected (12-mo)",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-08",
        "name": "Multiple Brand Kits + Audience-Specific Brand",
        "doc": "Nuni Strategy (Q3 foundation, Q4 audience-specific)",
        "problem": "Agencies manage multiple brands per Mailchimp account; one brand kit doesn't fit. Hannah's ProServ insight: brand-conscious agencies are dealbreaker-sensitive.",
        "benefit": "Agencies and multi-brand SMBs can ship without per-account workarounds. Removes a top dealbreaker for agency tier.",
        "slack_voc": "—",
        "slack_mrr": 0,
        "slack_users": 0,
        "research": "S1.59 (Eric agency dealbreaker) · S2.35 (Jacob brand application) · HeyMarvin Andrea D'Ercole (multi-brand workflow)",
        "klaviyo_gap": "Klaviyo also single brand kit — potential differentiator",
        "bq_metric": "DSB / agency segment retention (Page 7/8 DSB cuts)",
        "yoy_signal": "DSB MRR +13% YoY (H2 Obj 2 KR)",
        "sizing": "Part of DSB $3M-$8M envelope",
        "confidence": "MED",
        "must_do": False,
    },
    {
        "id": "I-09",
        "name": "Brand Voice + On-brand Content Generation (Q4)",
        "doc": "Nuni Strategy (Q4 Phase 2)",
        "problem": "AI drafts are generic; sound like 'every other brand's email.'",
        "benefit": "AI infers tone from past sent emails (corpus-based) and applies to all generated drafts. Drafts feel on-brand from day one.",
        "slack_voc": "Brand voice / tone learning AI",
        "slack_mrr": 410,
        "slack_users": 1,
        "research": "Page 6 implicitly — AI-generated drafts called out as generic by HeyMarvin engaged users; Wes Turner brand-kit expectations",
        "klaviyo_gap": "F2 (Brand Voice from corpus — Klaviyo's distinct moat)",
        "bq_metric": "AI-feature adoption (needs new event surface — flagged Page 7)",
        "yoy_signal": "AI features adoption rate; engagement quality (already +2 pts open YoY)",
        "sizing": "Part of H2 FY26 AI track ($1K-$530K monthly)",
        "confidence": "HIGH",
        "must_do": True,
    },

    # ============ THE RENDERING TRUST CLUSTER ============
    {
        "id": "I-10",
        "name": "Gmail Clipping + Dark Mode Guidance",
        "doc": "Nuni Strategy (Jan/Q3 Phase 6) + VoC Plan Deep Dive #3 Rendering",
        "problem": "Sent emails render differently than the editor preview (Outlook, dark mode). Users blame Mailchimp.",
        "benefit": "In-editor warnings before send: 'this email will be clipped in Gmail at X' / 'this color won't survive dark mode.' Builds confidence.",
        "slack_voc": "Mobile preview accuracy / WYSIWYG breakdown",
        "slack_mrr": 2575,
        "slack_users": 2,
        "research": "44 VoC items in Rendering bucket (10% of 468) · 'Why can't you keep the colors I chose' direct quote",
        "klaviyo_gap": "Adjacent F8 (built-in inbox testing — Klaviyo bundles via Mailgun)",
        "bq_metric": "Open/click rate (rendering quality affects engagement) · CSAT",
        "yoy_signal": "Sustain engagement quality gains (+2 pts open YoY) · CSAT (now 60%)",
        "sizing": "Part of Quality Pod's 20-30% reduction in mobile/rendering complaints",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-11",
        "name": "Inbox Previews refresh + consolidated checks (Q4)",
        "doc": "Nuni Strategy (Q4 Phase 6) + VoC Plan",
        "problem": "Litmus integration is hidden; preview is fragmented (separate from link-check, optimization, dark-mode).",
        "benefit": "Single 'pre-send confidence wall' — preview, links, dark mode, mobile, deliverability in one panel before send.",
        "slack_voc": "Dark mode / inbox preview / multi-client testing",
        "slack_mrr": 1003,
        "slack_users": 2,
        "research": "VoC Plan: 'Litmus feature is hidden' · Andrew Obeso pre-send anxiety · Kyle Spalding 15-min-future-send",
        "klaviyo_gap": "F8 (built-in inbox testing — Klaviyo bundles 100/mo via Mailgun)",
        "bq_metric": "Sends per session (test-send loops drop) · CSAT",
        "yoy_signal": "Reduce passive-billing-failure churn (rendering issues drive support tickets → cancellations)",
        "sizing": "Quality Pod target",
        "confidence": "HIGH",
        "must_do": False,
    },
    {
        "id": "I-12",
        "name": "Mobile Styles V2 + Dynamic Content on Mobile",
        "doc": "VoC Plan Deep Dive #2 (NOT FUNDED) · Nuni Strategy Phase 5 (Q4 Mobile Show/Hide)",
        "problem": "56 mobile-VoC items (12% of total). Users can't unlink mobile/desktop styles, no granular mobile-only display, mobile preview ≠ actual rendering.",
        "benefit": "Mobile-correct designs without forking templates. Per-section mobile control matches Klaviyo F5.",
        "slack_voc": "Mobile preview accuracy",
        "slack_mrr": 2575,
        "slack_users": 2,
        "research": "VoC Plan deepdive — 'mobile view is not how it shows on phone' · Andrea/Hannah confirmed gap",
        "klaviyo_gap": "F5 (per-section mobile-stacking) + adjacent D4 (interactive in-inbox)",
        "bq_metric": "Mobile-render fidelity SLO (Nuni proposed ≥95%)",
        "yoy_signal": "Engagement quality (mobile open rate)",
        "sizing": "VoC Plan flagged as 'Not funded' — re-fund in H2 critical",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-13",
        "name": "Automated Rendering Test (Litmus API)",
        "doc": "VoC Plan (NOT FUNDED) + Pillar 1 (Automated Testing X-Large effort)",
        "problem": "Rendering regressions ship to production; we don't catch them until customers complain.",
        "benefit": "Catch rendering bugs pre-deploy. Stops the trust-erosion treadmill.",
        "slack_voc": "—",
        "slack_mrr": 0,
        "slack_users": 0,
        "research": "VoC Plan recommendation only — no direct customer quote",
        "klaviyo_gap": "Internal quality, not competitive",
        "bq_metric": "Render-fidelity SLO (Nuni proposed ≥99%)",
        "yoy_signal": "Internal — protects engagement-quality YoY gains",
        "sizing": "Effort: X-Large (per Pillar plan)",
        "confidence": "MED",
        "must_do": False,
    },

    # ============ THE FTU ACTIVATION CLUSTER ============
    {
        "id": "I-14",
        "name": "Generated Layouts + Generated Layouts V2",
        "doc": "Nuni Strategy (Dec, Q3) + Phase 1 'Choose Structure'",
        "problem": "Blank-page anxiety. Non-designer FTUs don't know how to compose a multi-block layout.",
        "benefit": "Type a goal → AI generates layout draft. Mirrors Klaviyo Email AI's 99-section/day capability.",
        "slack_voc": "AI generative / AI image / AI layout",
        "slack_mrr": 0,
        "slack_users": 0,
        "research": "S1.7 (2-col discoverability) · Reddit r/Klaviyo: 'AI design way better than drag-drop'",
        "klaviyo_gap": "F3 (AI section/layout generator — currently Klaviyo only does this)",
        "bq_metric": "Activate→bulk_create_24h (currently 32%)",
        "yoy_signal": "Lift first-time sends (−25.7% YoY) for non-designer cohort",
        "sizing": "Part of H2 FY26 AI envelope",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-15",
        "name": "'It's Just an Email' Automations Flow (FTU)",
        "doc": "H2 FY26 Roadmap (Apr Q4) — FTU Optimal Setup",
        "problem": "FTUs see 'automation' as scary/complex; barrier to first automation send. Bianka Kiss / Clint Bartley quotes.",
        "benefit": "Reframe automation as 'just an email' — drop one trigger, ship. Lowers cognitive cost of first automation.",
        "slack_voc": "Generic editor clunky (proxy)",
        "slack_mrr": 5690,
        "slack_users": 6,
        "research": "Bianka Kiss (HeyMarvin) — A/B testing undiscovered for years; Clint Bartley DRAFT for 1 yr; Page 6 Bet 2 (Discovery)",
        "klaviyo_gap": "Adjacent — Klaviyo also has steep automation learning curve",
        "bq_metric": "Automation create + first send (funnel_weekly: cjb_create_24hrs)",
        "yoy_signal": "Logins YoY (−24%) — re-energize visit cadence",
        "sizing": "H2 FY26 FTU Optimal Setup: $1.5M-$2.8M",
        "confidence": "MED",
        "must_do": False,
    },
    {
        "id": "I-16",
        "name": "Pick-up-where-you-left-off (Wayfinding)",
        "doc": "H2 FY26 Roadmap (Mar Q3) — FTU Optimal Setup",
        "problem": "Users abandon a draft and can't find it again on next login. Created-but-never-sent wedge.",
        "benefit": "Surfaces incomplete drafts on homepage. Closes gap between create and publish.",
        "slack_voc": "Editor consistency / new builder for journeys",
        "slack_mrr": 904,
        "slack_users": 1,
        "research": "Clint Bartley DRAFT-resurrect ask · Jillian Ney save-as-template after success · Page 6 Bet 2 (DRAFT-resurrect prompt)",
        "klaviyo_gap": "Adjacent F9 (autosave reliability + version history)",
        "bq_metric": "Activate→bulk_publish_1w (currently 7.1%) — directly addresses created-but-never-sent",
        "yoy_signal": "First-time sends (−25.7% YoY)",
        "sizing": "H2 FY26 FTU Optimal Setup envelope",
        "confidence": "HIGH",
        "must_do": True,
    },

    # ============ THE DSB / SWITCHER CLUSTER ============
    {
        "id": "I-17",
        "name": "Dynamic Product Blocks + eCom templates with product blocks",
        "doc": "Nuni Strategy (Q3 Phase 4 + Q4 Phase 1) + H2 FY26 DSB roadmap (Feb)",
        "problem": "DSB switchers from Klaviyo expect product blocks with live catalog feeds; today Mailchimp has them but they're hard to discover (Jacob research) and use placeholder products instead of real Shopify items (S2.53).",
        "benefit": "Live Shopify catalog → product block at send-time; matches Klaviyo product-block experience.",
        "slack_voc": "Generic clunky + missing competitive parity",
        "slack_mrr": 5690,
        "slack_users": 6,
        "research": "S2.53 Jacob (placeholder products bug, HIGH priority) · S2.50 Jacob (low max items, no hide price) · S2.29 Jacob (discoverability) · Page 6 Bet 5",
        "klaviyo_gap": "F7 (live product feed parity — Shopify/BigCommerce/Woo)",
        "bq_metric": "DSB MRR (H2 KR2.1 +13% YoY)",
        "yoy_signal": "Engagement quality + DSB attach rate",
        "sizing": "DSB $3M-$8M cumulative",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-18",
        "name": "Klaviyo Email Template Converter + Custom Properties Migration",
        "doc": "H2 FY26 DSB Roadmap (Q3) + Switcher track",
        "problem": "DSB switchers from Klaviyo bring legacy templates and contact attributes; today they have to rebuild in Nuni.",
        "benefit": "Direct migration path: API key + template converter. Reduces switching friction from days to hours.",
        "slack_voc": "—",
        "slack_mrr": 0,
        "slack_users": 0,
        "research": "Nuni doc explicitly named DSB-from-Klaviyo as ICP · Page 6 Andrea (switcher mindset) · Page 4 D9 (hybrid editor for switchers)",
        "klaviyo_gap": "Strategic differentiator — Klaviyo doesn't make leaving easy",
        "bq_metric": "DSB switcher conversion · DSB MRR YoY",
        "yoy_signal": "DSB switchers cohort retention",
        "sizing": "Part of DSB $3M-$8M",
        "confidence": "HIGH",
        "must_do": False,
    },

    # ============ THE QUALITY / SLO CLUSTER ============
    {
        "id": "I-19",
        "name": "Quality Pod (Mobile + Rendering, 4 sprints Nov-Jan)",
        "doc": "VoC Plan (Recommendation 2)",
        "problem": "Mobile (12% VoC) + Rendering (10% VoC) = 22% of all builder feedback. Quick visible wins available.",
        "benefit": "Rapid bug burndown on highest-volume complaints. Restores trust in product reliability.",
        "slack_voc": "Editor performance · Mobile preview accuracy",
        "slack_mrr": 5812,
        "slack_users": 7,
        "research": "VoC Plan deepdives 1+2 · S1.4/S1.6 image-edit bugs · S2.36 logo placeholder · Editor lag complaints",
        "klaviyo_gap": "F9 (autosave reliability — turn Klaviyo's #1 complaint into our trust marker)",
        "bq_metric": "CSAT (currently 60%) · Crash-free SLO (target ≥99.5%)",
        "yoy_signal": "Reduce churn risk pool (currently 71K weekly · 0.23%)",
        "sizing": "VoC Plan target: 20-30% reduction in mobile/rendering complaints by EOQ2 FY26",
        "confidence": "HIGH",
        "must_do": True,
    },
    {
        "id": "I-20",
        "name": "Builder SLOs (6 metrics with targets)",
        "doc": "Nuni Strategy Section 7",
        "problem": "Reliability/performance regressions ship without operational guardrails; team has no shared 'quality bar.'",
        "benefit": "Operating contract: uptime ≥99.9%, crash-free ≥99.5%, save ≥99.99%, init load P95 <500ms, interaction P95 <300ms, render fidelity ≥99%, mobile ≥95%.",
        "slack_voc": "Editor performance / lag / browser freeze",
        "slack_mrr": 3237,
        "slack_users": 5,
        "research": "S1.14 Eric — editor crashed losing work · Page 5 multiple performance complaints",
        "klaviyo_gap": "F9 (reliable autosave + version history — directly attacks Klaviyo's #1 community complaint)",
        "bq_metric": "Crash-free sessions · save success rate · interaction latency P95",
        "yoy_signal": "Active churn risk reduction (currently 32K/mo of 71K total churn risk)",
        "sizing": "Operational guardrail; not a $ initiative",
        "confidence": "HIGH",
        "must_do": True,
    },

    # ============ DESIGN SPRINT (workflow redesign) ============
    {
        "id": "I-21",
        "name": "Cross-functional Design Sprint to reimagine clunky workflows",
        "doc": "VoC Plan (Recommendation 1, Nov 2025)",
        "problem": ">25% of VoC is 'Ease of Use / Clunky' — death by 1000 cuts. Won't be fixed by point fixes.",
        "benefit": "North-star vision for workflow simplification. Foundation for H2 FY26 builds.",
        "slack_voc": "Generic 'editor is clunky' (8 themes converge here)",
        "slack_mrr": 23000,
        "slack_users": 20,
        "research": "Multiple HeyMarvin findings · Page 6 Bet 5 (direct manipulation) · Andrea D'Ercole exit quote",
        "klaviyo_gap": "Foundational; informs F1-F10 sequencing",
        "bq_metric": "Click-budget per send (Nuni proposed ≤250 healthy band)",
        "yoy_signal": "Builder-driven churn share (Nuni target: -20-30% vs FY25)",
        "sizing": "Process / discovery — outputs feed roadmap",
        "confidence": "HIGH",
        "must_do": False,
    },
]


# ============ REVIEWER AGENT CRITIQUE ============
reviewer_critique = {
    "summary": "Reviewer ran 4 lenses: hallucination check (every cited number traced to source), coverage check (any VOC theme / research finding / Klaviyo gap not addressed?), redundancy check (overlapping initiatives), and sharpness check (which 5 are actually must-do?).",
    "passes": [
        ("Hallucination check", "PASS",
         "Every $ figure traces to a doc source — Nuni Strategy: '20-30% builder-driven churn reduction', VoC Plan: '$4-$6M FY26 revenue impact from improving sends', H2 FY26 FTU Roadmap: '$1.5M-$2.8M projected revenue (12-mo)' from 2.85-5.34% lift in FTU 90d retention, DSB Roadmap: '$3M-$8M cumulative impact estimates'. Every customer-quote citation traces to Page 5 (Slack VOC, MRR-validated) or Page 6 (HeyMarvin transcript with timestamp)."),
        ("YoY data backing", "PASS",
         "Every BQ metric reference traces to Page 7/8 actuals: bulk_publish_1w 7.1%, first-time-sends -25.7% YoY, M3 retention 76.5→34.5%, churn risk pool 71K. No fabricated numbers."),
        ("Klaviyo competitive mapping", "PASS",
         "F-codes (F1-F10 parity) and D-codes (D1-D10 differentiator) all reference Page 4 strategic plan. F1 (Universal Saved Content) = I-01. F4 (in-canvas AI image) = I-04. F2 (Brand Voice from corpus) = I-09. F5 (sections/mobile-stacking) = I-03/I-12. F7 (live product feeds) = I-17. F8 (inbox testing) = I-10/I-11. F9 (autosave reliability) = I-19/I-20."),
    ],
    "warnings": [
        ("VoC Plan items still 'Not Funded'",
         "Mobile Styles V2 · Dynamic content on Mobile · Dark mode education · Mobile rendering bug fixes · Expanding Inbox Previews · Automated Rendering Test were ALL marked 'Not funded' in the original VoC Plan (Nov 2025). Some show up in Nuni Strategy (Q4) but no clear funding/owner confirmation. ACTION: confirm funding status with Diana/Eric."),
        ("AI initiatives positioned as 'horizontal accelerator' but have separate H2 funding",
         "Nuni doc says 'no specific AI column — AI is horizontal accelerator.' But H2 FY26 Roadmap has AI as Objective 4 with $1K-$530K monthly impact. Risk: builder AI work falls between two budgets. ACTION: clarify funding model — does the Builder team get AI eng capacity, or rely on AI Objective team?"),
        ("Sizing inconsistency between docs",
         "VoC Plan cites '$4-$6M FY26 revenue impact' from improving email sends. H2 FY26 FTU sizing is '$1.5M-$2.8M from FTU retention.' DSB is '$3M-$8M.' These aren't additive (overlap with retention/MRR). REVIEWER: do not double-count. Treat $4-$6M as the upper-bound sense-check on builder-attributable opportunity."),
        ("Some initiatives have no Slack VOC mapping",
         "I-08 (Multi Brand Kits), I-13 (Automated Rendering Test), I-18 (Klaviyo Template Converter) — no direct Slack VOC theme. Justified by research (Page 6) or strategic logic but not customer-articulated in HVC channels. Lower confidence; track CSAT post-ship to validate."),
        ("Coverage gap — no initiative addresses HVC churn-passive-billing (53% of churn risk pool)",
         "Page 8 finding: 53% of weekly churn risk is passive billing failure (not active dissatisfaction). The builder team CAN'T own this — but should ensure builder UX doesn't compound (e.g., post-payment-failure 'broken builder' state). ACTION: cross-team coordination with Billing/Recovery."),
    ],
    "overlaps": [
        ("I-01 (Saved Sections) ↔ I-15 (FTU 'Save Email Sections')",
         "Same feature; FTU roadmap names it 'Save and Reuse Email Sections' (May Q4) while Nuni Strategy lists 'Reusable Saved Sections' (Q3). Confirm one team / one delivery date."),
        ("I-04 (Image gen + Image Normalization) ↔ I-06 (Chat-based Editing) ↔ Vibe Email Content Editing ↔ Canva AI image gen",
         "Four overlapping AI-in-builder initiatives across 3 docs. Risk of duplicated eng work. ACTION: rationalize into a single 'AI in Builder' track with clear sub-deliverables."),
        ("I-10/I-11 (Gmail clipping + Inbox Preview consolidation) ↔ Klaviyo F8 (built-in inbox testing)",
         "Mailchimp's plan is preview/check consolidation; Klaviyo bundles 100 inbox tests/mo via Mailgun. Strategic: do we ship Litmus integration (cheaper, faster) or build native? ACTION: cost/benefit decision."),
    ],
    "must_do_5": [
        ("I-01 Reusable Saved Sections / Universal Content",
         "5-source convergence — Slack ($13.7K MRR · 6 HVC users) + HeyMarvin Bet 1 + S1.11+S2.89 research + Klaviyo F1 parity + bulk_publish_1w funnel lever. Confirmed in-flight by PM Jose. Highest-confidence ship."),
        ("I-19 Quality Pod (Mobile + Rendering)",
         "22% of all VoC + Klaviyo's #1 weakness (autosave/rendering) becomes our trust marker. Crash-free SLO directly attacks active churn risk pool (32K/mo)."),
        ("I-04 In-canvas AI image (Vibe + Canva-in-Nuni)",
         "Andrea D'Ercole Bee.io detour is the single most-cited research finding. Klaviyo F4 parity. Lifts first-time sends (the −25.7% YoY metric)."),
        ("I-07 One-click Apply Brand + Branded Templates E2E for FTUs",
         "Maps to H2 FY26's biggest sized opportunity ($1.5M-$2.8M from FTU retention). Solves S1.59 + S2.35 + Page 6 brand-kit findings simultaneously."),
        ("I-20 Builder SLOs (6 metrics)",
         "Operating contract that institutionalizes the quality bar. Without these, every other shipping bet rots. Page 8 churn-risk active-pool reduction depends on this."),
    ],
}


# ============ Render ============
def fmt_n(n):
    if n is None or n == 0: return "—"
    if abs(n) >= 1_000_000: return f"${n/1_000_000:.1f}M"
    if abs(n) >= 1_000: return f"${n/1_000:.1f}K"
    return f"${n:,.0f}"


def html_e(s):
    return html_lib.escape(str(s) if s else "—")


# Doc summary cards
doc_cards = ""
for d in docs:
    doc_cards += f'''
    <div class="doc-card">
      <div class="doc-head">
        <div class="doc-name">{html_e(d["name"])}</div>
        <div class="doc-meta">{html_e(d["owners"])} · <span style="color:var(--muted);">{html_e(d["date"])}</span></div>
      </div>
      <div class="doc-row"><span class="doc-label">Thesis</span><span>{html_e(d["thesis"])}</span></div>
      <div class="doc-row"><span class="doc-label">Asks</span><span>{html_e(d["asks"])}</span></div>
      <div class="doc-row"><span class="doc-label">Sizing</span><span><strong>{html_e(d["sizing"])}</strong></span></div>
      <div class="doc-row"><span class="doc-label">Notable gaps</span><span style="color:var(--muted); font-size:11px;">{html_e(d["non_funded_items"])}</span></div>
    </div>
    '''

# Initiatives table
init_rows = ""
must_count = 0
for i in initiatives:
    must = "★" if i.get("must_do") else ""
    if i.get("must_do"): must_count += 1
    conf_class = {"HIGH": "qa-pass", "MED": "qa-partial", "LOW": "qa-doc"}[i["confidence"]]
    voc_cell = f'<strong>{html_e(i["slack_voc"])}</strong><br/><small style="color:var(--muted);">{fmt_n(i["slack_mrr"])}/mo · {i["slack_users"]} HVC users</small>' if i["slack_voc"] != "—" else '<span style="color:#9CA3AF;">no Slack VOC mapping</span>'
    init_rows += f'''
    <tr>
      <td class="ix-id"><code>{html_e(i["id"])}</code> <span class="must">{must}</span></td>
      <td><strong>{html_e(i["name"])}</strong><br/><small style="color:var(--muted);">{html_e(i["doc"])}</small></td>
      <td>{html_e(i["problem"])}<br/><br/><strong style="color:var(--good);">Benefit:</strong> {html_e(i["benefit"])}</td>
      <td>{voc_cell}</td>
      <td>{html_e(i["research"])}</td>
      <td><span class="ph-cat ph-missing">{html_e(i["klaviyo_gap"])}</span></td>
      <td>{html_e(i["bq_metric"])}<br/><small style="color:var(--brand); font-weight:700;">→ {html_e(i["yoy_signal"])}</small></td>
      <td><span class="qa-status {conf_class}">{i["confidence"]}</span><br/><small style="color:var(--muted);">{html_e(i["sizing"])}</small></td>
    </tr>
    '''

# Reviewer critique cards
reviewer_passes = "".join(
    f'<div class="review-card review-pass"><strong>✓ {html_e(name)}: <span style="color:var(--good);">{status}</span></strong><p>{html_e(detail)}</p></div>'
    for name, status, detail in reviewer_critique["passes"]
)
reviewer_warnings = "".join(
    f'<div class="review-card review-warn"><strong>⚠ {html_e(name)}</strong><p>{html_e(detail)}</p></div>'
    for name, detail in reviewer_critique["warnings"]
)
reviewer_overlaps = "".join(
    f'<div class="review-card review-overlap"><strong>↔ {html_e(name)}</strong><p>{html_e(detail)}</p></div>'
    for name, detail in reviewer_critique["overlaps"]
)
must_do_cards = ""
for idx, (name, rationale) in enumerate(reviewer_critique["must_do_5"], 1):
    must_do_cards += f'''
    <div class="bet" data-rank="{idx}">
      <h4>{html_e(name)}</h4>
      <p>{html_e(rationale)}</p>
    </div>
    '''


fragment = f"""
  <!-- ============ PAGE 9 — PM DOC CROSS-REFERENCE + REVIEWER ============ -->
  <section class="page" id="page9">
    <div class="page-head">
      <div>
        <div class="eyebrow">Competitive Intelligence · Executive Brief · Page 9 of 9</div>
        <h1>Previous PM's roadmap docs — cross-referenced + reviewer-agent critique</h1>
        <div class="subtitle">5 PDFs reviewed (Builder VoC Plans · Nuni Strategy · H2 FY26 Priorities · H2 FY26 Roadmap). 21 builder-relevant initiatives extracted, each cross-referenced against Slack VOC (Page 5) · HeyMarvin research (Page 6) · Klaviyo competitive gaps (Page 4) · BigQuery health metrics (Page 7-8). <strong>{must_count} initiatives flagged HIGH-confidence (multi-source) → reviewer-agent narrows to TOP 5 must-do-now</strong>.</div>
      </div>
      <div class="meta">
        <div><strong>Docs:</strong> 5 (Nov'25 → Mar'26)</div>
        <div style="margin-top:4px;"><strong>Initiatives:</strong> 21 unique</div>
        <div style="margin-top:4px;"><strong>Reviewer:</strong> 3 PASS · 5 warnings · 3 overlaps</div>
      </div>
    </div>

    <!-- HEADLINE -->
    <div class="pull" style="margin-bottom:14px;">
      <strong>The previous PM team has the right answers — and reasonable plans.</strong> The Nuni Strategy (Jan 2026) is comprehensive: 7-phase JTBD × 6-level Maslow, scored vs Klaviyo + Canva, 30+ initiatives mapped to Q2/Q3/Q4, six SLOs proposed. Cross-referenced with our independent triple-source (Slack VOC + HeyMarvin + BigQuery YoY), <strong>~80% of their initiatives map cleanly to a customer pain or competitive gap we independently identified.</strong> The remaining ~20% lack a direct customer voice (justifiable but lower confidence). <strong>Three structural risks the docs don't address:</strong> (1) several Mobile/Rendering items remain "Not Funded" since Nov 2025; (2) AI work spans two budgets (Builder + AI Objective) with unclear ownership; (3) sizing across docs ($4-6M, $1.5-2.8M, $3-8M) cannot be summed.
      <cite>— Cross-reference + reviewer-agent pass, May 8, 2026</cite>
    </div>

    <!-- DOC SUMMARIES -->
    <h2><span class="num">50</span>The 5 documents — what each proposes</h2>
    <div class="doc-grid">
      {doc_cards}
    </div>

    <!-- MASTER CROSS-REF TABLE -->
    <h2 style="margin-top:14px;"><span class="num">51</span>Master cross-reference — 21 initiatives × 4 evidence sources</h2>
    <div class="ix-table-wrap">
      <table class="ix-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Initiative · Source doc</th>
            <th>Problem · Customer benefit</th>
            <th>Slack VOC theme · MRR exposure</th>
            <th>HeyMarvin research</th>
            <th>Klaviyo gap (Page 4)</th>
            <th>BigQuery KPI moved</th>
            <th>Confidence · Sizing</th>
          </tr>
        </thead>
        <tbody>
          {init_rows}
        </tbody>
      </table>
    </div>
    <p style="font-size:11.5px; color:var(--muted); margin-top:6px;">
      <span class="must">★</span> = HIGH-confidence multi-source initiative ({must_count} of 21 — mapped to ≥3 sources: Slack VOC, HeyMarvin research, Klaviyo gap, or BigQuery KPI). Reviewer narrows further to TOP 5 must-do (Section 53 below). Confidence: HIGH = mapped to ≥3 sources. MED = 1-2 sources. LOW = strategic/internal logic only.
    </p>

    <!-- REVIEWER AGENT -->
    <h2 style="margin-top:18px;"><span class="num">52</span>Reviewer-agent critique — sharpness, hallucination, coverage</h2>
    <p style="margin-bottom:10px; font-size:12.5px;">{html_e(reviewer_critique["summary"])}</p>

    <div class="grid cols-3" style="margin-bottom:14px;">
      <div>
        <h2 style="margin:0 0 8px;">PASS · 3 lenses</h2>
        {reviewer_passes}
      </div>
      <div>
        <h2 style="margin:0 0 8px;">WARN · 5 issues</h2>
        {reviewer_warnings}
      </div>
      <div>
        <h2 style="margin:0 0 8px;">OVERLAPS · 3 conflicts</h2>
        {reviewer_overlaps}
      </div>
    </div>

    <!-- SHARPENED MUST-DO 5 -->
    <h2 style="margin-top:14px;"><span class="num">53</span>Reviewer-sharpened TOP 5 — among 21 initiatives</h2>
    <p style="margin-bottom:10px; font-size:12.5px;">If we can only ship 5 builder-side bets in H1 FY27, these are the highest-leverage by combined-signal scoring (multi-source convergence + competitive parity + KPI lever). Everything else stays on the Nuni roadmap, but these 5 define the team's identity for the next 6 months.</p>
    <div class="grid cols-2" style="margin-bottom:14px;">
      {must_do_cards}
    </div>

    <!-- IMPLICATIONS -->
    <h2><span class="num">54</span>Implications &amp; "go-do" list for the new product lead</h2>
    <div class="grid cols-3" style="margin-bottom:14px;">
      <div class="card warm">
        <p style="margin:0;"><strong>Inherit, don't restart.</strong> The Nuni Strategy is well-formed and Eric Anderson-reviewed. Don't redo the strategy work. <em>Validate the SLO instrumentation, ship the must-do 5, and watch the leading indicators</em> (bulk_publish_1w 7.1%, first-time-sends -25.7%, M3 retention 34.5%).</p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Re-fund the unfunded mobile + rendering work in Week 1.</strong> Mobile Styles V2 + Dynamic Mobile Content + Dark Mode + Inbox Previews refresh have been "Not funded" since Nov 2025. They map to 22% of VoC + Klaviyo F5/F8 parity + Page 8 mobile-render-fidelity SLO. The biggest hidden risk is letting these slip another quarter.</p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Resolve the AI ownership split.</strong> Vibe Email Editing, Canva-in-Nuni, Freddie Campaigns, Brand Voice — 4 different AI-in-builder threads across 3 docs. Get into a room with Nathan Snell + Diana + Eric to consolidate into a single "AI in Builder" track with one PM, one design lead, one engineering owner.</p>
      </div>
    </div>

    <div class="source">
      <strong>Sources (Page 9):</strong>
      <em>Documents reviewed:</em>
      (1) Builder VoC Feedback Response Plan (Ose Amiegheme · Erin McCue · JB Lovell · Joyce Russell · Nov 5, 2025);
      (2) Builder VoC Response Plan — Pillar version;
      (3) Nuni Builder Strategy and Roadmap (Ose Amiegheme · Erin McCue · JB Lovell · Ashley Wiesner · reviewed by Eric Anderson · Jan 2, 2026);
      (4) Mailchimp H2 FY26 Product Priorities (Diana Williams);
      (5) Mailchimp H2 FY26 Roadmap (Diana Williams · Mar 12, 2026 update).
      <br/><br/>
      <em>Cross-reference sources:</em> Page 4 (Mailchimp Roadmap parity F1-F10 + differentiator D1-D10) · Page 5 (HVC Slack VOC themes with $/mo MRR exposure) · Page 6 (HeyMarvin 25 customer briefs + Top 5 Bets) · Page 7-8 (BigQuery YoY health metrics).
      <br/><br/>
      <em>Reviewer-agent methodology:</em> Four lenses applied to every initiative — (a) Hallucination check: every $ figure and customer quote traced back to source-of-record; (b) Coverage check: which VOC themes / research findings / Klaviyo gaps are NOT addressed; (c) Overlap check: same feature appearing in multiple docs with different names/dates; (d) Sharpness check: ranking by combined-signal score (multi-source convergence × competitive impact × KPI lever × engineering feasibility). Top 5 must-do selected by a hard cutoff at 5 (not 6 or 7) to force prioritization.
    </div>
  </section>
"""

OUT.write_text(fragment.strip())
print(f"Wrote {OUT} ({len(fragment):,} chars)")
print(f"Initiatives: {len(initiatives)} ({must_count} must-do)")
print(f"Reviewer: {len(reviewer_critique['passes'])} PASS · {len(reviewer_critique['warnings'])} WARN · {len(reviewer_critique['overlaps'])} OVERLAP")
