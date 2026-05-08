"""Strategic HVC research session findings — Eric, Jacob, Nina.
Hand-extracted from PM research opportunity database screenshots.
Combined with Slack VOC themes to drive a unified prioritization.
"""

# Each finding: id, source, category, detail, summary, frustration, exclusive, score, sizing, priority
# frustration: Low / Medium / High / Delight
# exclusive: True (concern unique to this customer) / False (universal)
# score: 1-5
# sizing: Quick Win / Medium Lift / Big Lift / NA
# priority: HIGH / MEDIUM / LOW / NA

FINDINGS = [
    # --- ERIC (Session 1) ---
    {"id":"S1.1", "source":"Eric", "category":"UI Improvement", "detail":"Templates",
     "summary":"Template library navigation is frustrating — going back after previewing a template doesn't return to the same place, and page keeps reloading.",
     "frustration":"High", "exclusive":False, "score":5, "sizing":"Medium Lift", "priority":"HIGH",
     "slack_theme":"Preview from template list / template gallery navigation"},

    {"id":"S1.2", "source":"Eric", "category":"UI Improvement", "detail":"Templates",
     "summary":"Template preview doesn't show how brand kit assets would look in-situ. Logo auto-replacement only happens after loading, not during browse.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S1.3", "source":"Eric", "category":"UI Improvement", "detail":"Images",
     "summary":"Stock image library quality is unimpressive — user assumed results were AI-generated rather than curated stock photography.",
     "frustration":"Low", "exclusive":False, "score":3, "sizing":"Quick Win", "priority":"LOW"},

    {"id":"S1.4", "source":"Eric", "category":"Bug", "detail":"Images",
     "summary":"Image block fill toggle is one-way — switching from Original to Fill can't be reversed back to Original.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Quick Win", "priority":"MEDIUM"},

    {"id":"S1.5", "source":"Eric", "category":"UI Improvement", "detail":"Drag & Drop",
     "summary":"Drag and drop requires grabbing a specific handle instead of the element directly. Non-intuitive and frustrating.",
     "frustration":"High", "exclusive":False, "score":5, "sizing":"Quick Win", "priority":"HIGH",
     "slack_theme":"Generic 'editor is clunky / hard to use / unusable'"},

    {"id":"S1.6", "source":"Eric", "category":"UI Improvement", "detail":"Crop",
     "summary":"Crop function is not inline — user expected to crop directly on the canvas with original/cropped comparison side by side.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Quick Win", "priority":"LOW"},

    {"id":"S1.7", "source":"Eric", "category":"UI Improvement", "detail":"General",
     "summary":"2-column layout discoverability is poor — user needed help to find that images were nested inside a Columns block to control desktop vs mobile rendering.",
     "frustration":"High", "exclusive":False, "score":5, "sizing":"Medium Lift", "priority":"HIGH",
     "slack_theme":"Steep learning curve / confusing UX"},

    {"id":"S1.8", "source":"Eric", "category":"Feature Parity", "detail":"Cart Abandonment",
     "summary":"Cart block in abandoned cart automation email is not editable. For brand-conscious agencies, un-editable blocks are a dealbreaker.",
     "frustration":"High", "exclusive":True, "score":4, "sizing":"Medium Lift", "priority":"HIGH"},

    {"id":"S1.9", "source":"Eric", "category":"UI Improvement", "detail":"General",
     "summary":"Anchor functionality is too complex and poorly explained — experienced user abandoned it immediately.",
     "frustration":"Medium", "exclusive":True, "score":3, "sizing":"Medium Lift", "priority":"LOW"},

    {"id":"S1.10", "source":"Eric", "category":"UI Improvement", "detail":"Discount code block",
     "summary":"Discount code editing is confusing — user couldn't figure out how to display the code prominently in the email.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S1.11", "source":"Eric", "category":"Feature Parity", "detail":"Reusable Blocks",
     "summary":"No universal/global block functionality. Can't update a block once (e.g., footer year) and have it propagate across all emails/campaigns.",
     "frustration":"High", "exclusive":False, "score":5, "sizing":"Medium Lift", "priority":"HIGH",
     "slack_theme":"Saved sections / saved blocks / universal content"},

    {"id":"S1.12", "source":"Eric", "category":"UI Improvement", "detail":"Merge Tags",
     "summary":"Merge tag / dynamic data toggle is undiscoverable. User couldn't figure out how to enable personalization variables.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S1.13", "source":"Eric", "category":"UI Improvement", "detail":"General",
     "summary":"Order items block is not editable and provides no visual cue distinguishing it from editable blocks. User wasted significant time troubleshooting.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Quick Win", "priority":"MEDIUM"},

    {"id":"S1.14", "source":"Eric", "category":"Bug", "detail":"General",
     "summary":"Email editor crashed with a generic error message and refreshed, losing user's work.",
     "frustration":"High", "exclusive":False, "score":5, "sizing":"Quick Win", "priority":"HIGH",
     "slack_theme":"Editor performance / lag / browser freeze"},

    {"id":"S1.59", "source":"Eric", "category":"Feature Parity", "detail":"Brand & Global Styles",
     "summary":"Global styles panel is undiscoverable. For brand-conscious agencies, every email element must be editable for font and hex color. Non-editable blocks are dealbreakers.",
     "frustration":"High", "exclusive":True, "score":4, "sizing":"Big Lift", "priority":"MEDIUM"},

    # --- JACOB (Session 2) ---
    {"id":"S2.29", "source":"Jacob", "category":"UI Improvement", "detail":"General",
     "summary":"Product recommendation blocks are hard to discover in the email builder content panel.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"HIGH"},

    {"id":"S2.30", "source":"Jacob", "category":"Bug", "detail":"General",
     "summary":"Layout option selector (horizontal/vertical) renders in a way that looks like a loading state, confusing users into waiting.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Quick Win", "priority":"MEDIUM"},

    {"id":"S2.31", "source":"Jacob", "category":"Feature Parity", "detail":"Social Media Icons",
     "summary":"Social icon block only offers preset color themes. No custom hex color option for brand-specific icon styling.",
     "frustration":"Low", "exclusive":True, "score":2, "sizing":"Medium Lift", "priority":"LOW"},

    {"id":"S2.32", "source":"Jacob", "category":"UI Improvement", "detail":"Social Media Icons",
     "summary":"Social icon block doesn't warn when too many icons are added to fit on one line, causing layout overflow.",
     "frustration":"Low", "exclusive":True, "score":2, "sizing":"Medium Lift", "priority":"LOW"},

    {"id":"S2.33", "source":"Jacob", "category":"UI Improvement", "detail":"General",
     "summary":"Email preview loads very slowly, especially when discount code or dynamic content is involved.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Big Lift", "priority":"MEDIUM",
     "slack_theme":"Editor performance / lag / browser freeze"},

    {"id":"S2.34", "source":"Jacob", "category":"UI Improvement", "detail":"Integrations",
     "summary":"Clicking into app integrations from within the email builder navigates away entirely, losing the user's context.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S2.35", "source":"Jacob", "category":"Bug", "detail":"Brand Application",
     "summary":"Email templates don't apply saved brand kit button styles. Template uses generic button colors instead of user's defined brand buttons.",
     "frustration":"Medium", "exclusive":False, "score":5, "sizing":"Medium Lift", "priority":"HIGH"},

    {"id":"S2.36", "source":"Jacob", "category":"Bug", "detail":"Email within automation",
     "summary":"Logo is correctly applied in email builder but shows as placeholder in automation flow preview cards.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S2.37", "source":"Jacob", "category":"UI Improvement", "detail":"Link Checker",
     "summary":"Link checker is slow and doesn't indicate which specific links have been verified vs. pending.",
     "frustration":"Low", "exclusive":False, "score":3, "sizing":"Medium Lift", "priority":"LOW"},

    {"id":"S2.38", "source":"Jacob", "category":"Feature Parity", "detail":"Test Send",
     "summary":"No ability to save and name test email recipient lists. Agencies need reusable, named seed lists shared across team members.",
     "frustration":"Low", "exclusive":True, "score":2, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S2.39", "source":"Jacob", "category":"UI Improvement", "detail":"Email within automation",
     "summary":"Email preview thumbnails in automation flow view are static/non-interactive — can't scroll or click into them.",
     "frustration":"Medium", "exclusive":False, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S2.50", "source":"Jacob", "category":"Feature Parity", "detail":"Product Blocks",
     "summary":"Product rec block has a low max item count and no option to hide/show price — limiting customization for e-commerce emails.",
     "frustration":"Medium", "exclusive":True, "score":4, "sizing":"Medium Lift", "priority":"MEDIUM"},

    {"id":"S2.53", "source":"Jacob", "category":"Bug", "detail":"Product Blocks",
     "summary":"Product rec preview shows placeholder products instead of actual Shopify store products despite active integration.",
     "frustration":"Low", "exclusive":False, "score":3, "sizing":"Quick Win", "priority":"HIGH"},

    {"id":"S2.54", "source":"Jacob", "category":"UI Improvement", "detail":"General",
     "summary":"Trigger/action select dropdowns are too small and require extra clicks — should open pre-expanded.",
     "frustration":"Low", "exclusive":False, "score":3, "sizing":"Medium Lift", "priority":"LOW"},

    {"id":"S2.89", "source":"Jacob", "category":"Feature Parity", "detail":"Reusable Blocks",
     "summary":"Still no reusable/universal content blocks. Can't update a footer once and have it propagate across all emails. Repeated from Session 2 (re-raised by Jacob).",
     "frustration":"Medium", "exclusive":False, "score":5, "sizing":"Medium Lift", "priority":"HIGH",
     "slack_theme":"Saved sections / saved blocks / universal content"},

    # --- NINA (Session 3 — Delights) ---
    {"id":"S3.8", "source":"Nina", "category":"Delight", "detail":"Accessibility",
     "summary":"Auto-generated alt text was a surprise delight. Agency spends significant time on alt text for image-heavy D2C emails — this feature saves meaningful effort.",
     "frustration":"Delight", "exclusive":False, "score":3, "sizing":"NA", "priority":"NA"},

    {"id":"S3.19", "source":"Nina", "category":"Delight", "detail":"Product Blocks",
     "summary":"Product recommendation blocks and dynamic product feeds were easier to implement than in competing platforms. Drag-and-drop with pre-built data properties was a positive surprise.",
     "frustration":"Delight", "exclusive":False, "score":3, "sizing":"NA", "priority":"NA"},

    {"id":"S3.20", "source":"Nina", "category":"Delight", "detail":"General",
     "summary":"Email builder praised as intuitive and standard. Core email creation experience met expectations of a Klaviyo power user.",
     "frustration":"Delight", "exclusive":False, "score":3, "sizing":"NA", "priority":"NA"},
]


# Combined-priority scoring
# Inputs: research priority + frustration + Slack MRR (if matched) + sizing
PRIORITY_WEIGHT = {"HIGH": 10, "MEDIUM": 5, "LOW": 2, "NA": 0}
FRUSTRATION_WEIGHT = {"High": 3, "Medium": 2, "Low": 1, "Delight": 0}
SIZING_WEIGHT = {"Quick Win": 1, "Medium Lift": 2, "Big Lift": 4, "NA": 1}


def combined_score(finding, slack_mrr=0):
    """Higher = more urgent. Bugs and parity gaps get a small boost."""
    p = PRIORITY_WEIGHT.get(finding["priority"], 0)
    f = FRUSTRATION_WEIGHT.get(finding["frustration"], 0)
    s = SIZING_WEIGHT.get(finding["sizing"], 1)
    base = (p + f * 2) * 100  # heavy on priority + frustration
    mrr_bonus = slack_mrr / 100  # $1k MRR = 10 points
    cat_boost = {"Bug": 50, "Feature Parity": 30, "UI Improvement": 0, "Delight": -1000}.get(finding["category"], 0)
    return (base + mrr_bonus + cat_boost) / s


if __name__ == "__main__":
    # Quick sanity check
    from collections import Counter
    c = Counter(f["priority"] for f in FINDINGS)
    cat = Counter(f["category"] for f in FINDINGS)
    src = Counter(f["source"] for f in FINDINGS)
    siz = Counter(f["sizing"] for f in FINDINGS)
    print(f"Total findings: {len(FINDINGS)}")
    print(f"By priority:  {dict(c)}")
    print(f"By category:  {dict(cat)}")
    print(f"By source:    {dict(src)}")
    print(f"By sizing:    {dict(siz)}")
    matched = [f for f in FINDINGS if "slack_theme" in f]
    print(f"Mapped to Slack themes: {len(matched)} of {len(FINDINGS)}")
    for f in matched:
        print(f"  {f['id']} → {f['slack_theme']}")
