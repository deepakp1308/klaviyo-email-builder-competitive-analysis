Source URL: https://deepakp1308.github.io/klaviyo-email-builder-competitive-analysis/#page10
Title: Klaviyo Email Builder — Competitive Analysis (Executive 2-Pager)

 Competitive Brief — Klaviyo Email Builder

1 · Overview 2 · Strategy 3 · Voice of Customer 4 · Mailchimp Roadmap 5 · HVC VOC Prioritization 6 · Customer Research (HeyMarvin) 7 · Builder Health Diagnostic 8 · YoY · QA · F·B·I·R 9 · PM Doc Review + Reviewer 10 · Mailchimp Builder Brief 11 · Mailchimp VOC Print / PDF 

Competitive Intelligence · Executive Brief · Page 1 of 11

# Klaviyo's Email Builder

The WYSIWYG canvas inside Campaigns where ecommerce marketers compose, design, brand, and personalize one-off email campaigns — drag-and-drop blocks, sections, brand kit, and a stack of in-editor AI tools.

**Scope:** Email Builder only  
(excludes Flows, SMS, segmentation, deliverability, customer hub)

**Last updated:** May 2026

160+

Pre-built email templates in library, filterable by use case, layout, season, Shopify

\~13

Native drag-and-drop block types (text, image, button, product, table, HTML, split, header bar, divider, spacer, drop shadow, social, video)

99 / day

Email AI section generations per account (33 prompts × 3 drafts) — paid plans only

100 / mo

Inbox renderings per user via built-in Mailgun-powered inbox testing (paid)

## 01What the product feature is

The **Klaviyo Email Editor** (officially: "drag-and-drop email template editor", marketed as "Create engaging emails, faster") is the canvas marketers open inside a Campaign to design a one-off broadcast email. The current generation replaced the deprecated _Classic Editor_ in May 2023 and is now the default for all new templates.

It is positioned as a **no-code, AI-assisted, brand-aware** builder — purpose-built for ecommerce. The product surface is bounded: a left-rail block library, a center canvas with sections & columns, a right-rail style/properties panel, and a top bar for preview, test send, AI assist, and version controls.

Drag-and-drop canvas Sections + columns Universal saved content Brand kit auto-apply In-editor AI Inbox & mobile preview HTML block + Django tags 

## 02Why it matters strategically

**The editor is Klaviyo's daily-touchpoint surface.** Marketers may visit segmentation or deliverability monthly, but they touch the editor every time they ship a campaign. This is where retention is earned and competitive switching costs accumulate.

Klaviyo has invested heavily here in 2024–2026: the editor rewrite, the Email AI generative layer, Brand Voice extraction, Image Remix (Gemini-powered), and Universal Content. They're racing to close the gap to Mailchimp's polished editor while extending an AI-native moat.

## 03Block library inside the canvas

Marketers compose emails by dragging these atomic units from the left sidebar onto the canvas. Each block has its own style/properties panel; structural blocks (Section, Split) contain content blocks.

T

Text

Content

▭

Image

Content

▢

Button

Content

⊞

Table

Content

🛍

Product

Catalog

▶

Video

Content

⫻

Split

Layout

▬

Header Bar

Layout

━

Divider

Layout

↕

Spacer

Layout

◐

Drop Shadow

Style

@

Social

Content

</>

HTML

Power user

Six block types (button, divider, HTML, image, spacer, text) can additionally be saved as **Universal Content** — edit once, propagates to every email/template that uses it.

## 04Core editor capabilities

* **Sections & columns:** group blocks, save as units, control mobile stacking direction (left→right, right→left, or off).
* **Universal Content:** reusable blocks/sections that propagate updates globally — header, footer, promo banners.
* **Background images per section** with fallback colors and Original / Fit / Fill / Tile sizing.
* **Brand kit:** logos, colors, fonts, buttons, social links, brand voice — applied automatically to library templates and new flow emails.
* **Personalization engine:** Django-style template tags (`{{ first_name|title|default:'there' }}`), filters (`floatformat`, `multiply`), custom object support, dynamic show/hide blocks per segment.
* **Productivity:** undo/redo (⌘+Z), autosave, faster preview, in-canvas text editing.
* **HTML block + Django Tag Builder** for power users (replacing source-code mode in text blocks).
* **Preview & test:** desktop ↔ mobile toggle, dark-mode preview, send test email, shareable preview links (6-day expiry), inbox testing across desktop/web/mobile/dark via Mailgun (capped 100/user/mo, paid).

## 05AI built into the editor

### Email AI Paid only

Type a plain-text prompt ("3-column section with image + headline + button"). AI generates 3 fully-styled draft sections inheriting the template's Styles tab. Toggle through drafts, regenerate, or edit description.

Generates layouts, copy, image placeholders, buttons, columns. Limit: 33 prompts × 3 drafts = 99 sections/day. Image URLs, product feeds, alt text still configured manually.

### Brand Voice Guidelines Paid

Klaviyo analyzes your **past emails** to extract tone, vocabulary, sentence patterns. Generates writing rules that the AI auto-applies to every future Email AI draft. Manually editable.

Distinctive: most competitors require user-typed style guides; Klaviyo infers from corpus.

### Subject Line AI Free tier

Natural language prompt → multiple subject line suggestions. Regenerate freely. Available to anyone (also surfaced as a public free tool on klaviyo.com).

Lowest-friction AI surface — used as an acquisition hook before paywall.

### Image Remix (Gemini) Paid

In-canvas AI image editor powered by Google Gemini. Change backgrounds, recolor objects, add/remove people, change facial expressions, all via text prompt. 1–3 min per image; original preserved.

Eliminates the Canva/Photoshop round-trip — rare among email tools.

### Marketing Agent Free tier

Pulls brand assets (images, copy, colors) from your website on connect, then proposes campaign concepts and pre-fills the editor with on-brand drafts.

Onboarding accelerant — gets a free user to first sent email faster.

### Personalized Campaigns AI Paid

For A/B/n campaigns, the AI auto-routes each subscriber to the variant most likely to convert _them_ (not the population average). Builder shows which variant won per segment.

Differs from classic A/B: continuous personalization, not single-winner.

 Sources (Page 1): klaviyo.com/products/email-marketing/templates · klaviyo.com/product/whats-new/email-editor · klaviyo.com/product/whats-new/email-ai · klaviyo.com/solutions/ai/remix · klaviyo.com/tools/email-subject-line-generator · help.klaviyo.com (editor guide, brand voice, sections & columns, inbox testing, personalization tags) · klaviyo.com/whats-new (Spring 2026)

Competitive Intelligence · Executive Brief · Page 2 of 11

# Differentiation, JTBD, Pricing & Gaps

Where Klaviyo's email builder wins, who reaches for it and why, what it costs to unlock the AI layer, and what they still don't do well.

**Reading time:** \~4 min

**Confidence:** High (vendor docs + reviews)

## 06What truly differentiates the builder (vs Mailchimp, Omnisend, Attentive)

vs. Mailchimp

### Ecommerce-native blocks

Product blocks are first-class with live catalog feeds; the template library has a dedicated Shopify category. Mailchimp's product block exists but feels bolted-on relative to its content-marketing roots.

vs. all rivals

### Brand voice _inferred_, not typed

Klaviyo derives writing rules from your past sent emails. Competitors (Mailchimp Intuit Assist, Omnisend AI, Attentive AI) require the marketer to write their own style guide.

vs. Mailchimp / Omnisend

### In-editor AI image edit (Gemini)

Image Remix lets you re-light, re-background, swap objects without leaving the canvas. Most rivals push you to Canva, Adobe Express, or external editors.

vs. Mailchimp

### Universal Content with global propagation

Edit a saved block once → updates every email it appears in. Mailchimp's "content blocks" are templated copy-paste; not truly globally bound.

vs. Attentive

### Built-in inbox rendering

Mailgun-powered inbox tests across mobile, desktop, web, and dark mode are bundled (100/user/mo). Attentive and most ESPs require Litmus or Email on Acid subscriptions.

vs. Mailchimp

### Section-level mobile stacking control

Marketers control whether columns stack, in which order (L→R, R→L), or stay horizontal on mobile, per-section. Mailchimp offers global only.

## 07Who's using it & jobs to be done

**Primary persona:** 1–3 person ecommerce marketing team at a $5M–$200M GMV DTC brand on Shopify. Often a solo email marketer or a brand designer who also ships campaigns.

**Reference customers using the builder:** Tatcha Twinings Marine Layer LifeStraw Alessi 

Solo email marketer · DTC apparel

"Build me a Friday promo email that's on-brand in under 30 minutes — without opening Figma or pinging the designer."

Solved by: Email AI + Brand Kit + library template + Image Remix.

Brand designer · Beauty

"Lock down our header, footer, and disclaimer block once so junior marketers can't break the brand."

Solved by: Universal Saved Content + Brand Kit defaults.

Lifecycle marketer · Home goods

"Show repeat customers a different hero block than first-time subscribers from one template."

Solved by: Dynamic show/hide blocks + segment conditions on blocks.

Email developer · Mid-market

"Drop in a custom HTML countdown timer and live product feed without forking a template."

Solved by: HTML block + Django Tag Builder + Product block.

Marketing manager · Holiday season

"Verify this BFCM email renders in Gmail dark mode, Outlook, and on iPhone before I send to 200K."

Solved by: Dark-mode preview + inbox testing (Mailgun) + mobile toggle.

## 08Pricing — what plan unlocks what

Builder itself is in **every plan** (including Free). The differentiation Klaviyo monetizes is the **AI layer**, **inbox testing**, and the underlying contact volume.

#### Free Builder ✓

$0 · up to 250 profiles

* Drag-and-drop editor
* Basic templates (subset of 160+)
* Subject Line AI
* Marketing Agent
* No Email AI generation
* No Image Remix
* No inbox testing

#### Starter Builder + AI ✓

\~$20/mo · up to 500 profiles

* Full template library (160+)
* Email AI (99 sections/day)
* Brand Voice Guidelines
* Image Remix (Gemini)
* Inbox testing (100/mo)
* Universal Content

#### Growth All editor AI

\~$60/mo · up to 2,500 profiles

* Everything in Starter
* Personalized Campaigns AI (A/B/n auto-routing)
* Higher AI generation ceilings
* Custom HTML support tier

#### Pro All editor AI

\~$150/mo · up to 10,000 profiles

* Everything in Growth
* Dedicated success / onboarding
* Same builder feature set as Growth

 Note: Klaviyo uses **contact-based pricing**; the builder doesn't gate by feature beyond AI. SMS is a separate credit pool. Annual billing saves 10–20%.

## 09What customers love · what they call out

## Loved (strengths)

\+ Builder wins

* **Drag-and-drop is genuinely fast** once learned; auto-save and ⌘+Z reduce fear of breaking work.
* **Universal saved content** is the most-praised power-user feature — global header/footer updates without hunting.
* **Image Remix wow-factor:** reviewers consistently flag this as best-in-class — replaces an entire Canva workflow.
* **Brand voice extraction from past emails** lands more on-brand drafts than any prompt-based competitor.
* **Inbox testing built-in** is a real cost saver vs Litmus ($99+/mo external).
* **Deep Shopify hooks** in product blocks & templates — live catalog feeds, dynamic pricing.

## Called out (gaps)

– Builder gaps

* **Steep learning curve** — solopreneurs hit a wall vs Mailchimp's friendlier first-run.
* **UI churns frequently** — "every month something moves" (Gartner Peer Insights). Erodes muscle memory for power users.
* **Source-code view being removed** from text/table/split blocks — friction for HTML-first marketers; forces migration to dedicated HTML block.
* **Brand voice "writing rules" editor reportedly buggy** (Badsender, May 2025).
* **Email AI doesn't auto-configure** product feeds, image URLs, or button destinations — generated sections need cleanup.
* **Daily AI cap (99 sections)** can bite agencies running multiple brands.
* **Cost escalates** with contact growth — builder is "free" but the platform isn't, once you're past 2,500 profiles.

## 10So what — implications for our roadmap

**Match the table stakes.** Sections + columns, universal saved content, mobile-stacking control, dark-mode preview, and inbox testing are now expected. Anything less reads as dated to a Klaviyo evaluator.

**The AI bar moved.** Generate-from-prompt and brand-voice-from-corpus are the new floor. In-canvas image editing (Gemini-tier) is the new ceiling. A "subject line generator" alone no longer impresses.

**Attack vectors:** (1) friendlier first-run / lower learning curve, (2) UI stability promise, (3) better HTML/dev workflow, (4) higher / unlimited AI ceilings, (5) flat-rate pricing tiers that don't punish growth.

 Sources (Page 2): klaviyo.com/blog/pricing-update · klaviyo.com/customers/case-studies (Tatcha, Twinings, Marine Layer, LifeStraw, Alessi) · help.klaviyo.com (brand styles, universal content, dark-mode preview) · community.klaviyo.com (sections & columns, classic vs new editor) · academy.klaviyo.com (Email AI quick guide) · G2 / Gartner Peer Insights / Badsender / Sender.net / Mailsoftly reviews · Polaris Growth + Uplers blogs · attentive.com/blog (comparative context) · zigpoll Klaviyo vs Mailchimp vs Attentive 2026  
  
_Methodology:_ synthesized from Klaviyo's product pages, what's-new posts, help center articles, developer reference, customer case studies, third-party reviews, and competitive comparison content. Scope deliberately limited to the **Email Builder / template editor** surface — not Flows, SMS, segmentation, deliverability, Customer Hub, or Helpdesk.

Competitive Intelligence · Executive Brief · Page 3 of 11

# Voice of Customer — what people actually say

Sentiment synthesis from Reddit (r/Klaviyo, r/ecommerce, r/ShopifyAppDev, r/graphic\_design), Klaviyo Community forum, G2, Capterra, Trustpilot, agency blogs, and YouTube tutorial commentary — strictly about the **email builder/editor**. **Refreshed May 8, 2026.**

**Sources scanned:** 35+ threads, 7 review sites

**Window:** 2024 → May 2026 (refresh)

★ MAY 2026 REFRESH — WHAT'S NEW SINCE LAST PULL

**5 material developments** since this page was first compiled, all from primary sources (Klaviyo Community, klaviyo.com newsroom, ecom-tools.de):

* **Composer launched March 24, 2026** — full-campaign generation from plain-language prompts (audience, message, timing, channels). Klaviyo positioning itself as "autonomous B2C CRM" — bigger AI narrative than the prior K:AI Marketing Agent (Sep 2025). Implies a category move from _marketing automation_ to _autonomous decision-making_.
* **Senior PM (Devin) launched a community feedback campaign June 2026** — 12-day open feedback window in Klaviyo Community for the email editor, then publishing the prioritized roadmap publicly. Confirmed in-progress: multi-image upload · Preview & Test button placement · copy block styles (format painter) · image & universal content folders · text formatting improvements. _Direct response to the bug-noise complaints documented below — meaningful signal that they're listening._
* **Image editing feature DEPRECATED from new editor** (community thread "Why is the 'edit image' feature gone?"). Major user pushback — they relied on it for resizing + rounded corners. Klaviyo says it was deprioritized; users feel _downgraded_. Net new on the "hated" list.
* **"Tone of Voice" added to AI Customer Agent** — 4 preset tones (Neutral · Professional · Friendly · Playful). _Different from the prior Brand Voice from corpus._ Limited to marketing calls (not service interactions) to avoid "tonal dissonance." Mixed reception — useful guardrail but reads as preset-driven vs. inferred-from-data.
* **Klaviyo confirmed text-editor migration is rolling out in 2 stages** — automatic migration of existing templates after the new templates default. Triggering a wave of "the new text editors get in the way" complaints (Klaviyo Community campaigns-and-flows-30 thread #12042). Klaviyo support has acknowledged "delete & rename functionality for saved content is coming soon."

**Net sentiment shift:** the underlying complaint pattern hasn't changed (slowness, autosave, UI churn) — but Klaviyo is _visibly responding_ via Composer (top-of-stack AI move) and the Devin-led PM feedback initiative (bottom-of-stack execution). Watch June-July 2026 for whether the in-progress fixes actually land and whether users de-escalate the Community forum negative sentiment.

 The editor is **capability-rich and bug-noisy**. Customers love the _power_ (Universal Content, Image Remix, brand kit, dynamic product blocks) but are vocally frustrated by _execution_ — slowness, autosave failures, popup obstructions, and a constantly-shifting UI. The AI is praised when it solves a workflow (Remix, Brand Voice from corpus) and dismissed when it just rewrites prompts (subject lines). **May 2026 update:** Klaviyo is now responding visibly via Composer (autonomous-CRM AI move) and a public PM-led community feedback campaign — but the in-progress fixes haven't yet shipped to broad availability.— Synthesis across G2, Capterra, Trustpilot, Reddit r/Klaviyo, Klaviyo Community, agency blogs · refreshed May 8, 2026 

## 11Sentiment by channel

G2

4.6 / 5

1,319 reviews · editor capabilities praised

Capterra

4.6 / 5

525 reviews · ease vs power balance

Sender.net editorial

3.8 / 5

Editor good, learning curve called out

Trustpilot

1.8 / 5

350+ reviews · billing dominates · editor ≠ main complaint

Reddit r/Klaviyo

Mixed

AI design split · "Beautiful Designs by AI" thread upvoted

Klaviyo Community forum

Negative

Editor bug threads dominate · self-selected complaints

Agency blogs

Positive

Hickman, InboxArmy, Polaris, Uplers · pros endorse it

YouTube tutorials

Positive

Kovac, official Klaviyo · creators sell content on it

**Read the gap, not just the score.** G2/Capterra reviewers are typically vetted business buyers, Trustpilot skews consumer/billing, Reddit skews practitioners venting. The editor itself isn't loved or hated uniformly — it's praised for capability and roasted for execution.

## What people love (strengths)

\+ 6 themes

### Universal Saved Content Top praise

"Edit once, propagate everywhere" lands as the most-loved power-user feature. Frequently called out as the #1 reason brand designers keep using Klaviyo.

> "Big news! Universal Content is now available!" — community announcement thread, hundreds of upvotes, broadly positive replies.

**Sources:** Klaviyo Community announcement thread · G2 reviews · Polaris Growth blog

### Image Remix (Gemini) Wow factor

Praised as the most genuinely novel addition. Marketers say it removes a Canva/Photoshop round-trip — change backgrounds, recolor, swap models without leaving the editor.

> "Takes marketers from idea to execution in minutes rather than days" — Klaviyo blog, echoed in agency reviews and r/Klaviyo positive threads.

**Sources:** Klaviyo blog · Klaviyo Community Remix thread · Reddit r/Klaviyo "Beautiful Designs by AI"

### Dynamic product blocks & Shopify hooks Ecom-native

Live catalog feeds with dynamic pricing — most-cited reason brands picked Klaviyo over Mailchimp for the editor experience.

> "Dynamic product blocks with e-commerce integrations like Shopify, WooCommerce, BigCommerce" called out as standout — Badsender, May 2025.

**Sources:** Badsender deep review · G2 vs MailerLite/Mailjet pages · Hickman Design agency roundup

### Brand kit + Brand Voice from corpus AI that delivers

Marketers like that Brand Voice infers tone from past sent emails — they don't have to write a style guide. Drafts feel more on-brand than rivals'.

> "Klaviyo analyzes your past emails… generates writing rules that the AI applies to future drafts" — help center; reviewers note this is the AI feature most worth turning on.

**Sources:** Klaviyo help center · Mailflow Authority AI review · agency blogs

### Sections, columns, custom fonts, mobile stacking Modernized

The new editor's structural primitives (vs the old Classic) are universally welcomed — finally side-by-side blocks, controllable mobile stacking direction, custom fonts without code.

> "Sections and columns for more flexible layouts… controllable mobile stacking" — community guide post praised in replies.

**Sources:** Klaviyo Community new vs classic thread · Polaris Growth · Uplers

### AI-generated layouts (when they help non-designers) Niche love

For marketers without design chops, Email AI is a real unlock: "way better than drag-and-drop" if you struggle with layout. Heavier-skilled designers find generated drafts generic.

> "AI-generated email designs are way better than drag and drop… solves a huge problem." — r/Klaviyo, "Beautiful Designs by AI" thread.

**Sources:** Reddit r/Klaviyo · counterpoint: Mailflow Authority calls subject-line AI generic

### ★ Composer (March 2026) — full-campaign generation NEW · Mar 2026

Klaviyo's March 24, 2026 release: type a plain-language prompt, the agent decides audience targeting, message, timing, channels, and optimization. Built on K:AI Marketing Agent (Sep 2025). Reframes Klaviyo from "email tool" to "autonomous B2C CRM" in marketing.

> "Klaviyo is no longer a mere email service — it has completed its transformation into an autonomous B2C CRM, with K:AI agents functioning as the fundamental operating system rather than optional add-ons." — ecom-tools.de 2026 analysis.

**Sources:** klaviyo.com/newsroom/composer (Mar 24 2026) · ecom-tools.de Klaviyo 2026 analysis · klaviyo.com/blog/klaviyo-ai-for-autonomous-marketing-and-customer-service

### ★ PM-led community feedback campaign NEW · Jun 2026

Senior PM Devin opened a 12-day community feedback window on the Klaviyo Community forum and committed to publishing a public roadmap. **In progress:** multi-image upload · Preview & Test button placement · copy block styles (format painter) · image & universal content folders · text formatting fixes. _Direct response to the bug-noise complaints — meaningful signal that they're listening._

> "Klaviyo support has confirmed: text block fixes including link styling and custom fonts have already been addressed. Functionality to delete and rename saved content is coming soon. The product team is prioritizing fixes for the new editor." — Klaviyo Community announcements, June 2026.

**Sources:** community.klaviyo.com/product-updates-announcements-51 · Devin "Share your feedback with me" thread (June 2026)

## What people hate (gaps)

– 8 themes

### Editor performance is brutal #1 complaint

"Outrageously slow" — 5-10 second waits during autosave, scrolling lags, performance degrades the longer the editor is open. Multiple long threads.

> "Why does Klaviyo's new editor work so slow?" — community thread title; hundreds of co-signers complaining about typing latency in text blocks.

**Sources:** Klaviyo Community "Content Editor Slow in New Version?" · "Why does Klaviyo's new editor work so slow" · "New Editor: Feature requests"

### Autosave is unreliable Lost-work fear

Autosave sometimes stops, the manual save button doesn't always work, edits get lost. Forces marketers to copy work to a doc as backup.

> "Is the New Editor Auto-Save feature broken?" — recurring community thread; users describe re-entering the editor as the workaround.

**Sources:** Klaviyo Community autosave thread · "New Template Editor — Am I the only one seeing a lot of bugs?"

### \~10 named bugs in one user's count Trust-eroding

Section padding switch resets, undo unreliable, blocks disappear on refresh, mobile preview inaccurate, duplicate button missing, dynamic coupon false positives.

> "The bugs/glitches… starting to irritate me to the point where I'll just stop using Klaviyo editors and fully switch to plain text editor… or some other builder." — power user, \~100 emails across 3 projects.

**Sources:** Klaviyo Community "New Klaviyo Template Builder?" thread · Side Million blog "Klaviyo, you really frustrate me"

### Inline-styling popups obstruct text UX downgrade

New inline popups cover the text being edited, replacing the older flyout drawer. Forces users to compose in Word and paste in.

> "The new text editors get in the way… a downgrade to the editing experience." — community campaigns & flows thread.

**Sources:** Klaviyo Community "The new text editors get in the way" · Side Million

### Saved-blocks management is poor Power-user pain

Can't rename, can't reorder, no folders, can't easily edit/delete from list. Old-editor blocks were silently auto-migrated with no organization.

> "Saved blocks from old editor now showing in new editor, BUT…" — community thread; reply piles describe the migration as opaque.

**Sources:** Klaviyo Community saved-blocks migration thread · "New Editor: Feature requests" thread

### HTML ↔ drag-and-drop interop is broken Dev workflow

Exported HTML loses drag-drop on re-import. Source-code view is being removed from text/table/split blocks. Forces HTML-first marketers into the dedicated HTML block or off the platform.

> "Klaviyo made emails harder than they should be." — r/ShopifyAppDev thread title.

**Sources:** r/ShopifyAppDev · Klaviyo Community "Adding drag/drop into HTML template" · "Lack of drag-and-drop functionality from HTML template"

### AI subject lines & generic content AI shallow

Subject Line AI produces "Don't Miss Our Spring Collection" / "New Arrivals You'll Love" — useful for brainstorming, useless verbatim. Reviewers say the AI lacks brand voice on the surface tools (even though Brand Voice itself works on body copy).

> "Sounds like every other brand's email… use them for inspiration, then refine with Claude or ChatGPT." — Mailflow Authority Klaviyo AI review.

**Sources:** Mailflow Authority AI review · Klaviyo Community "AI Subject Line Analysis" · Reddit AI threads

### Brand Voice "Writing Rules" buggy Polish gap

The very feature Klaviyo markets as the AI moat (Brand Voice from corpus) is reported to "bug every other time" in the configuration UI.

> "The 'writing rules' option in the style configuration bugs every other time." — Badsender May 2025 deep technical review.

**Sources:** Badsender · sender.net editorial · G2 reviews

### Steep learning curve · UI churns monthly Switch trigger

Newcomers compare unfavorably to Mailchimp's first-run; veterans complain the UI "moves something every month" eroding muscle memory.

> "At least once a month there's an update that makes you say wait, where did _that_ functionality go?" — Gartner Peer Insights review.

**Sources:** Gartner Peer Insights · Sender.net · Reddit r/ecommerce switching threads

### ★ Image editing feature DEPRECATED from new editor NEW · 2026

The full image-editing toolset (resize, rounded corners, effects beyond cropping) was removed from the new editor. Klaviyo says it was deprioritized; users describe it as a downgrade and rely on it for routine work.

> "Why is the 'edit image' feature gone from the template editor?" — Klaviyo Community thread title (community.klaviyo.com/marketing-30/9032). Users report relying on it for resizing and adding effects like rounded corners.

**Sources:** Klaviyo Community marketing-30 thread #9032 · "Why is the edit image feature gone" — significant negative reaction in replies

### ★ Billing change still hurting brand sentiment Persistent · 2025-2026

February 2025 billing model change (charging for all active profiles incl. unengaged) continues to dominate Trustpilot reviews into 2026\. Bills jumping 5-10× overnight is the dominant complaint.

> "$39 → $200 overnight" / "$625 → $2,765 in a single billing cycle" — recurring quotes across Trustpilot reviews. Trust-breaking event called out by SaaS Scored, Sender.net, EmailCloud reviews.

**Sources:** Trustpilot 1.8/5 · CheckThat.ai aggregator · SaaS Scored 7.5/10 · EmailCloud 2026 review · NOT directly editor — but bleeds into editor sentiment via brand-trust erosion

### ★ "Tone of Voice" presets — guardrail or downgrade? NEW · 2026 · Mixed

New AI Customer Agent feature: 4 preset tones (Neutral · Professional · Friendly · Playful). Limited to marketing calls (not service interactions) to avoid "tonal dissonance." _Different from Brand Voice from corpus_ — preset-driven vs inferred-from-data.

> "Tone settings apply only to marketing-oriented calls, not service-oriented interactions, to avoid 'tonal dissonance' in sensitive customer situations." — klaviyo.com/blog/ai-voices-for-brand-tone-customization. Reception is mixed: useful guardrail, but reads as preset-driven vs the corpus-inferred Brand Voice marketers prefer.

**Sources:** klaviyo.com/blog/ai-voices-for-brand-tone-customization · Mailflow Authority AI feature review

## 12AI sentiment, by feature

Loved

### Image Remix (Gemini)

Real workflow win. Reviewers and Reddit users repeatedly call out as best-in-class. Removes Canva/Photoshop dependency.

Loved (when it works)

### Brand Voice from corpus

Inferred-not-typed style guide is the AI moat marketers want. But the configuration UI itself is reportedly buggy.

Mixed

### Email AI (section generation)

"Way better than drag-and-drop" for non-designers (r/Klaviyo). Skilled designers find drafts generic and the manual cleanup (image URLs, product feeds, button URLs) annoying.

Mixed

### K:AI Marketing Agent

Promising — pulls assets from your site, builds first drafts. Community feedback notes it requires significant manual tweaking and can be slower than doing it yourself.

Dismissed

### Subject Line AI

"Generic," "sounds like every other brand," fine for brainstorming, useless verbatim. Most reviewers refine in Claude/ChatGPT instead.

Loved (orthogonal to editor)

### Predictive analytics + Smart Send Time

Often called Klaviyo's _strongest_ AI work — but lives outside the editor. Frequently mentioned as the reason marketers tolerate the editor's bugs.

## 13Why some are switching _away_ (editor as a factor)

* **"Klaviyo made emails harder than they should be"** — r/ShopifyAppDev. The HTML/drag-drop interop and learning curve push some Shopify devs to Shopify Email or Omnisend.
* **"Switching from Klaviyo to Shopify Emails"** — r/Klaviyo own subreddit thread; cited reasons mix billing + editor friction for smaller stores.
* **Pricing escalation past 2,500 profiles** — editor doesn't gate, but the bill does. Mid-market shops downgrade or move to MailerLite / Sender.
* **Power users threaten to "fully switch to plain text editor"** after enough bugs — quoted in community thread, \~100 emails across 3 projects.

## 14Why people stay despite the gripes

* **Switching cost on Universal Content + Brand Kit** is real — once 50+ flows reference saved blocks, leaving means rebuilding.
* **Shopify integration depth** — product blocks with live catalog feeds aren't trivially replaced.
* **Brand Voice corpus learning** means the AI gets better the longer you stay (a real moat).
* **Inbox testing built-in** saves Litmus subscription cost (\~$99+/mo).
* **Predictive analytics + Smart Send Time** are genuinely missed when leaving.

## 15So what — implications for our positioning

**Klaviyo's softest tissue is execution, not capability.** Their feature list is hard to match; their reliability and UI consistency are not. A "boringly stable, never-loses-your-work" editor with autosave you can prove is a credible wedge.

**HTML / dev workflow is an underserved seam.** r/ShopifyAppDev rage about HTML-drag-drop interop and Klaviyo removing source-code from text blocks is a clear gap to attack.

**AI: pick the workflow wins, skip the gimmicks.** Image-edit-in-canvas (Remix-tier) and brand-voice-from-corpus are the AI surfaces customers actually praise. Subject-line generators are no longer credible AI proof points.

**Sources (Page 3):** Reddit — r/Klaviyo ("Beautiful Designs by AI" 2025, "Switching from Klaviyo to Shopify Emails" 2025, "Get Your Flows Flowing"), r/ecommerce ("Go-to ecommerce email marketing software"), r/ShopifyAppDev ("Klaviyo made emails harder than they should be"), r/graphic\_design (Klaviyo email design pricing thread). Klaviyo Community forum — "Why does Klaviyo's new editor work so slow?", "New Editor: Feature requests", "New Template Editor — Am I the only one seeing a lot of bugs?", "Is the New Editor Auto-Save feature broken?", "The new text editors get in the way", "Saved blocks from old editor now showing in new editor, BUT…", "Klaviyo's new feature, Remix", "Big news: Universal Content is now available!", "AI Subject Line Analysis", "Klaviyo AI" thread, "New Klaviyo Template Builder?". Reviews — G2 (4.6/5, 1,319 reviews; comparison pages vs Mailjet, MailerLite), Capterra (4.6/5, 525 reviews), Trustpilot (1.8/5, 350+), Sender.net editorial (3.8/5), CheckThat.ai cross-platform aggregator, SaaS Scored, Mailsoftly, Toksta Reddit-sentiment aggregator. Blogs — Badsender (May 2025 deep technical review), Polaris Growth, Uplers, Hickman Design "Inbox Architects", InboxArmy comparison guide, FirstPier agency guide, Labyrinth Digital best practices, Side Million "Klaviyo, you really frustrate me", Mailflow Authority "Klaviyo AI Features Review". YouTube — Klaviyo official "Customize Klaviyo Email Templates" tutorial, Elliot Kovac "The Only Klaviyo Email Design Tutorial You'll Ever Need".  
  
_Methodology:_ \~30 threads + 6 review platforms scanned for editor-specific commentary. Quotes lightly edited for length, not for sentiment. Channel skew explicitly called out (Trustpilot is billing-heavy, Klaviyo Community self-selects toward complainers, agency blogs are commercially aligned). Scope strictly limited to the email builder/editor — Flows, SMS, segmentation, deliverability, billing, and customer support sentiment excluded except where editor-adjacent.

Competitive Intelligence · Executive Brief · Page 4 of 11

# Mailchimp Email Builder — parity, leapfrog, and 3-phase roadmap

Emerging-threats landscape, the foundational gaps Mailchimp must close to be a credible front-runner against Klaviyo, the differentiated bets to steal from Klaviyo + the AI-native challengers, and a phased plan to win the omnichannel campaign builder.

**POV:** Mailchimp PM strategy

**Horizon:** 18 months · 3 phases

 The omnichannel campaign builder market is fragmenting fast. **Klaviyo** owns DTC editor mind-share. **Bird** ($1.1B raised, $3.8B valuation) is commoditizing channel infra and racing up to AI orchestration. **YC's W22-W25 batches** (Resend, Loops, Zaymo, Eden, Mailmodo, Apten) are unbundling Mailchimp from below with AI-native, interactive, and agentic angles. Mailchimp's defensible position is _SMB scale + Intuit data + omnichannel breadth_ — but the editor itself is a parity gap today. We must **achieve editor parity in Phase 1, leapfrog with single-canvas omnichannel + WhatsApp in Phase 2, and own agentic 1-to-1 in Phase 3**.— Strategy synthesis, May 2026 

## 16Emerging threats landscape — who's coming for the omnichannel builder

Tier 1 · Scaled, well-funded (acute threats — already ARR-significant)

Bird (was MessageBird) Acquired/rebrand · 2024

"Omnichannel Platform-as-a-Service" — SMS, email, WhatsApp, voice, push, AI agents. Slashed SMS pricing 90% in 2024 to commoditize Twilio and move up to AI orchestration.

**$1.1B raised**$3.8B valuation · $500M–$1B ARR · 15,000+ customers · 170+ countries

ACUTE

Attentive Late-stage · pre-IPO

SMS-first DTC marketing, expanded into email. Drove \~$2B brand revenue Cyber Week 2025\. Direct overlap with Mailchimp's DTC segment.

**$500M+ ARR (2024)**8,000+ businesses · DTC dominant

ACUTE

Braze Public · NASDAQ

Enterprise CDP + cross-channel engagement. Acquired OfferFit for AI decisioning. Mostly upmarket from Mailchimp but compresses ceiling.

**\~$693M ARR**2,296 customers · 247 at $500K+ · FY25 26% growth

HIGH

Customer.io Growth-stage

Workflow-first cross-channel platform popular with growth-stage SaaS. Direct mid-market overlap with Mailchimp Standard/Premium.

**$100M ARR (Sep 2025)**9,000+ brands · 111% NDR

ACUTE

Bloomreach Growth-stage

"Loomi AI" agentic platform for ecommerce. Fast-growing, agentic-first narrative.

**$260M+ ARR (2025)**FCF-positive · record net new ARR

HIGH

Postscript Series C · 2022

SMS-first for Shopify brands. Conversational replies, native two-way SMS in editor.

**$65M Series C**8,000+ Shopify brands · 25× avg ROI claimed

HIGH

Tier 2 · AI-native disruptors (high disruption signal, lower scale today)

Resend YC W23 · a16z-backed

Developer-first email infra moving up to marketing. Open-source React Email (300K weekly downloads, 14K stars). Customers: Warner Bros, Decathlon, Raycast.

**$18M Series A (Dec 2024)**200K+ developers · a16z-led

DEV-LED

Loops YC W22

"Email platform built for SaaS" — product, marketing, transactional in one canvas. Craft Ventures backed.

**\~$13M raised total**$3.2M seed Sep 2023 · DC-based

MED

Knock Notification infra

G2-leader notification infrastructure. Multi-channel preference center, deduplication. Could move into builder space.

**State-of-Notification report 2025**Category leader (vs Novu, Courier, SuprSend)

MED

Singulate Pre-seed · 2024

"Singulation" — generates unique 1-to-1 content per recipient via LLMs. Beta showed 5–10× CTR vs blasts. Founded by Hopin alumni.

**$2.3M pre-seed**Bowery Capital + Seedcamp · angels: Hopin, Indeed, SaaStock

EARLY

Tier 3 · YC W22–W25 batch (newest builder-layer entrants)

Zaymo YC W24

Interactive email builder — shop, browse, buy _inside_ the email. AMP-for-Email native. Claims +27% revenue vs traditional emails.

**YC backing**Shopify-focused · interactive in-inbox

HIGH

Mailmodo / Mailmodo AI YC

Interactive widgets in email (polls, quizzes, calculators, spin-the-wheel) + prompt-first AI campaign creation. "Prompt-first email marketing for the AI era."

**YC backing**AMP-for-Email native · AI campaign builder

HIGH

Eden YC

AI-personalized campaigns based on _why_ customers hesitate (CRM + analytics + support tickets fused). 1-to-1 hesitation-driven content.

**YC backing**Behavioral 1:1 personalization

MED

Apten YC

Omnichannel AI agents across SMS, voice, email, webchat with unified memory. Agentic next-best-action across channels. Hundreds of thousands of leads/month.

**YC backing**Agentic orchestration · enterprise consumer services

HIGH

Tier 4 · WhatsApp-first commerce (huge in international ecom — under-attacked by US-centric ESPs)

AiSensy India · CTWA Partner of the Year 2024

WhatsApp marketing & engagement: broadcasting, chatbots, click-to-WhatsApp ads, payments. Meta CTWA Partner of the Year. Dream Green Capital backed.

**50,000+ businesses**₹1,000+ cr brand revenue · 80–100M msgs/mo

ACUTE (intl)

Wati Global · 4.6 G2

WhatsApp Business API + team inbox + AI lead qualification. 16,000+ customers worldwide.

**16,000+ customers**Global SMB WhatsApp commerce

HIGH

Charles · Zoko · Interakt · LimeChat WhatsApp-DTC stack

Conversational commerce on WhatsApp + IG + Messenger. Catalog product cards, abandoned-cart, subscription, two-way chat.

**Various seed/A-stage**Shopify-WhatsApp fusion · DACH/India focus

HIGH

**Reading the landscape:** the threat isn't one company — it's a converging pincer. Bird is racing UP from infra. Klaviyo is racing OUT from DTC email. Attentive is expanding from SMS. AiSensy/Wati are owning WhatsApp internationally. Zaymo/Mailmodo are reinventing the inbox itself. Apten/Singulate are betting the builder becomes an agent. Mailchimp is structurally exposed in the editor while these multiply.

## 17Foundational gaps Mailchimp must close (parity to be a credible Klaviyo front-runner)

These are **table-stakes Mailchimp does not credibly have today in the email builder**. Without these, evaluators compare us against Klaviyo and we lose on capability before we get to talk about omnichannel breadth.

F1

Universal Saved Content

Save a header / footer / promo block once, edit it once, propagate to every campaign and template that uses it.

Match: **Klaviyo's #1-praised feature** · also Bloomreach

F2

Brand Voice from corpus (AI)

Auto-extract tone, vocabulary, and writing patterns from past sent emails. Apply automatically to all AI drafts. Editable.

Match: **Klaviyo Brand Voice** · differentiator vs Mailchimp's prompt-typed style

F3

AI section/layout generator (not just copy)

Generate full multi-column, multi-block _layouts_ from a prompt — not only inline copy edits. 3 drafts per prompt.

Match: **Klaviyo Email AI** (99 sections/day) · Intuit Assist today only does copy

F4

In-canvas AI image editor

Change backgrounds, recolor, swap objects/people, restyle product photos via text prompt — without leaving the editor.

Match: **Klaviyo Image Remix** (Gemini) · Mailchimp has Creative Assistant but no in-canvas Gemini-tier edit

F5

Sections + per-section mobile-stacking control

Group blocks into sections; control mobile stacking direction (L→R, R→L, off) per section, not just globally.

Match: **Klaviyo new editor** · current Mailchimp builder is global-only

F6

Dynamic show/hide blocks per segment

Conditionally show different hero/CTA blocks to different segments from a _single template_ — no template fork required.

Match: **Klaviyo dynamic blocks** · Mailchimp limited equivalent

F7

Live product feed blocks (Shopify/BigCommerce/Woo parity)

Drop a product block, point at a live catalog feed; pricing, inventory, images sync at send-time. Match Klaviyo's Shopify depth.

Match: **Klaviyo Product blocks** · Mailchimp depends on integrations

F8

Built-in inbox testing

Render the email across desktop / mobile / web / dark-mode inboxes inside the builder. Eliminate the Litmus subscription dependency.

Match: **Klaviyo + Mailgun** bundled · Mailchimp would need Litmus parity

F9

Reliable autosave + version history

Visible save state, diff between versions, "restore to" any prior point. Specifically attack Klaviyo's #1 community complaint.

Steal: **weakness in Klaviyo** ("Is autosave broken?" community thread) · turn into our strength

F10

HTML block + safe template-tag builder

Dedicated HTML block with React Email / Liquid / Django-style tag autocomplete for power users. Don't break dev workflow.

Match: **Klaviyo HTML block + Django Tag Builder** · Steal: **r/ShopifyAppDev rage** at HTML/drag-drop interop

## 18Differentiated bets to steal from Klaviyo + emerging threats (leapfrog moves)

These are the **positioning wedges** — what makes Mailchimp not just "as good as Klaviyo" but "better and differently shaped" — by stealing the best ideas across the threat landscape and binding them to our omnichannel + Intuit-data advantages.

D1

True omnichannel composition canvas

One editor → email + SMS + WhatsApp + push + in-app. Compose channel-specific variants in tabs of a single campaign, not 4 separate tools.

Steal: **Bird** (omnichannel-as-a-service) · attacks Klaviyo's separate-canvas weakness

D2

Channel-adaptive AI content reuse

Write the email; AI auto-generates the SMS short-form, the WhatsApp template-compliant variant, the push headline. Marketer reviews/edits.

Steal: **Apten unified memory** \+ **Bird AI** · 5× reduces multi-channel composition time

D3

Native WhatsApp template builder in editor

First-class WhatsApp Business template builder: Marketing / Utility / Authentication types, button limits, header types, CTWA campaigns — all inside the same builder.

Steal: **AiSensy + Wati + Charles** · open up emerging-market ecom moat Klaviyo doesn't have

D4

Interactive in-inbox blocks (AMP for Email)

Native AMP blocks: shop-the-product, RSVP, NPS, poll, quiz, spin-the-wheel — render inside Gmail/Yahoo. Click-out becomes click-in.

Steal: **Zaymo + Mailmodo** · +27% revenue claim baked into product

D5

1-to-1 generative personalization ("singulation")

Past static merge-tags; AI generates a unique hero block + headline + product story per recipient using Intuit's customer data graph.

Steal: **Singulate + Eden** · 5–10× CTR claim · Intuit-data is the unfair advantage

D6

Agentic next-best-action orchestration

In the campaign canvas, opt in to "let agent decide" — channel + send time + variant + frequency-cap, per recipient, optimizing on the goal you set.

Steal: **Apten + Bloomreach Loomi + Braze OfferFit** · become the agent-OS for SMB campaigns

D7

Cross-channel preference + dedup center

Subscriber-level preference center across email/SMS/WhatsApp/push. Smart dedup so a single event doesn't fire 3 channels. Builder shows live channel reach pre-send.

Steal: **Knock** · turn compliance pain into trust feature

D8

Inline conversational reply handling

When SMS/WhatsApp recipient replies, conversation surfaces in the same builder. Marketer (or AI agent) replies without context-switching.

Steal: **Postscript + Charles + Apten** · close the broadcast→conversation loop

D9

Hybrid code/no-code editor (React Email layer)

Designers ship React Email components; marketers drag-edit them; engineers extend in code. Both populations served, no platform fragmentation.

Steal: **Resend + Loops** · attack Klaviyo's source-code-removal rage on r/ShopifyAppDev

D10

Click-to-WhatsApp ad → builder → flow loop

Build the WhatsApp landing-message inside the builder; AI generates the matching Meta ad creative; first-message reply auto-enrolls into a flow.

Steal: **AiSensy CTWA** · close the paid-acquisition → owned-channel loop

## 19For each feature — core problem solved & customer functional benefit

| ID                                 | Feature                                     | Core problem it solves                                                                                                                                | Customer functional benefit                                                                                                     |
| ---------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Foundational (parity with Klaviyo) |                                             |                                                                                                                                                       |                                                                                                                                 |
| F1                                 | **Universal Saved Content**                 | Marketers manually update the same header / footer / promo block across dozens of templates → drift, errors, brand inconsistency.                     | Edit once, propagate everywhere. Cuts brand-update time from hours to seconds; eliminates "wrong promo on Tuesday's send."      |
| F2                                 | **Brand Voice from corpus (AI)**            | AI drafts read generic; "sounds like every other brand's email"; marketers throw away most AI suggestions.                                            | AI writes in _your_ voice from day one; usable drafts ship 3–5× more often without rewrite.                                     |
| F3                                 | **AI section / layout generator**           | Blank-canvas paralysis; non-designers can't compose a coherent multi-block layout from scratch.                                                       | "3-column section with hero + headline + button" → 3 styled drafts in seconds. Solo marketers ship without designer dependency. |
| F4                                 | **In-canvas AI image editor**               | Marketer leaves builder for Canva / Photoshop to recolor a photo, swap a background, or refit a product shot. Slow, breaks flow.                      | Re-light, re-background, swap objects in 1–3 minutes inside the builder. Replaces a Canva subscription.                         |
| F5                                 | **Per-section mobile-stacking control**     | Multi-column emails stack the wrong way on mobile; marketers fork desktop and mobile templates.                                                       | Per-section control (L→R, R→L, off). One template, two devices, no fork.                                                        |
| F6                                 | **Dynamic show/hide blocks per segment**    | "Repeat customers should see X; new subs should see Y" → marketer forks the template, doubling maintenance.                                           | One template, conditional blocks. Personalization without template explosion.                                                   |
| F7                                 | **Live product feed blocks**                | Static product images go stale; out-of-stock items get sent; pricing drifts from store.                                                               | Send-time fresh: pricing, stock, image always reflect the live store. Lifts revenue and reduces refund/complaint rate.          |
| F8                                 | **Built-in inbox testing**                  | Marketer pays $99+/mo for Litmus / Email on Acid _just_ to verify rendering before send.                                                              | Bundled rendering across Gmail / Outlook / Apple Mail / dark mode / mobile. Saves $1.2K+/year per seat.                         |
| F9                                 | **Reliable autosave + version history**     | Editor loses unsaved work (Klaviyo's #1 community complaint); marketer ships in fear or copies to a doc.                                              | Visible save state, diff between versions, restore-to-any-point. Removes lost-work anxiety; trust marker vs Klaviyo.            |
| F10                                | **HTML block + safe tag builder**           | HTML-first marketers and dev teams pushed off the platform when source-code editing is removed (Klaviyo case).                                        | Power users ship custom HTML / tags without breaking templates. Keeps dev / agency seats on the platform.                       |
| Differentiated (steal & leapfrog)  |                                             |                                                                                                                                                       |                                                                                                                                 |
| D1                                 | **Omnichannel composition canvas**          | To run a campaign across email + SMS + WhatsApp + push, marketers use 2–4 disconnected tools and re-author content.                                   | One canvas, channel tabs, shared content + audience. Compress launch time from 2 weeks to 2 days.                               |
| D2                                 | **Channel-adaptive AI content reuse**       | Re-authoring email body for SMS / WhatsApp / push is tedious and inconsistent.                                                                        | Write once; AI generates compliant SMS, WhatsApp template, push headline. Marketer edits, doesn't author from scratch.          |
| D3                                 | **Native WhatsApp template builder**        | WhatsApp Business templates (Marketing / Utility / Auth) require Meta-approved structure; marketers cobble together via 3rd parties (AiSensy / Wati). | Build, submit, and send WhatsApp templates inside Mailchimp. Open international ecom that's invisible to Klaviyo.               |
| D4                                 | **Interactive in-inbox blocks (AMP)**       | "Click-out to website to RSVP / shop / vote" loses 60–80% of intent at the click.                                                                     | RSVP, poll, shop, NPS render inside Gmail/Yahoo. +27% revenue uplift claim (Zaymo) realized in product.                         |
| D5                                 | **1-to-1 generative personalization**       | Merge-tags personalize the name; the rest of the email is identical to 100K other recipients.                                                         | AI writes a unique hero + product story + CTA per recipient using Intuit's customer-data graph. 5–10× CTR (Singulate beta).     |
| D6                                 | **Agentic orchestration**                   | Marketer manually picks channel, send time, variant, frequency cap — and gets it wrong per individual.                                                | Opt-in agent decides per recipient, optimizes on goal. Marketer sets guardrails, not micro-decisions.                           |
| D7                                 | **Cross-channel preference + dedup center** | Same event fires email + SMS + push → recipient gets spammed → unsubscribes from _all_ channels.                                                      | Smart dedup respects preferences across channels. Pre-send live-reach indicator. Reduces churn-by-fatigue.                      |
| D8                                 | **Inline conversational reply handling**    | SMS / WhatsApp replies land in a separate inbox tool; broadcast → conversation loop is broken.                                                        | Replies surface in same builder; AI agent or marketer responds inline. Closes the loop on conversational commerce.              |
| D9                                 | **Hybrid code/no-code editor**              | Designers want to ship React Email components; marketers want drag-edit; engineers want code extension. Today they fork tools.                        | One platform serves all three populations. Enterprise + agency seats stick instead of leaving for Resend/Loops.                 |
| D10                                | **CTWA → builder → flow loop**              | Paid WhatsApp ads drive a first message → goes to a separate inbox; no auto-enrollment in lifecycle.                                                  | Meta ad creative + landing message + first-reply flow built in one place. Closes paid-acquisition → owned-channel loop.         |

## 203-phase sequencing — two swim lanes per phase

**North star:** by end of _Phase 1_, Mailchimp is a credible front-runner against Klaviyo's email builder. By end of _Phase 2_, Mailchimp owns the omnichannel + WhatsApp + interactive narrative. By end of _Phase 3_, Mailchimp is the agentic 1-to-1 customer engagement OS for SMB.

Phase 1 · Months 0–6

### Neutralize Klaviyo's editor moat

**Outcome:** Win the head-to-head Klaviyo "feature parity" demo. Stop losing deals on capability gaps. Position the omnichannel wedge.

Foundational (parity)

* `F1` Universal Saved Content
* `F3` AI section/layout generator (extend Intuit Assist beyond copy)
* `F4` In-canvas AI image editor (Gemini or Imagen)
* `F8` Built-in inbox testing
* `F9` Reliable autosave + version history (turn Klaviyo's weakness into our trust marker)

Differentiated (early wedge)

* `F2` Brand Voice from corpus — match + brand-it-better than Klaviyo
* `D1` Omnichannel canvas v1 (email + SMS + push tabs)
* `D2` Channel-adaptive AI content reuse — email → SMS first cut

**Demo line:** "Everything Klaviyo's editor does — plus a single canvas where one campaign reaches email, SMS, and push, with AI adapting your copy to each channel."

Phase 2 · Months 7–12

### Own omnichannel + WhatsApp + interactive

**Outcome:** No competitor matches the breadth (incl. WhatsApp) or the in-inbox interactivity. Open international ecom that's invisible to Klaviyo.

Foundational (round out parity)

* `F5` Per-section mobile-stacking control
* `F6` Dynamic show/hide blocks per segment
* `F7` Live product feed blocks (Shopify / BigCommerce / Woo parity)
* `F10` HTML block + safe template-tag builder

Differentiated (leapfrog)

* `D3` Native WhatsApp template builder (Marketing / Utility / Auth) inside builder
* `D4` Interactive in-inbox blocks (AMP) — start with poll, RSVP, NPS, then shop-the-product
* `D7` Cross-channel preference + dedup center with live pre-send reach
* `D8` Inline conversational reply handling (SMS + WhatsApp)

**Demo line:** "The only platform where you compose, send, AND have a conversation across email + SMS + WhatsApp + push from one canvas — with shop, RSVP, and quizzes living inside the inbox."

Phase 3 · Months 13–18+

### Become the agentic 1-to-1 engagement OS

**Outcome:** Mailchimp is no longer compared feature-by-feature; it's compared as a category — agent vs. tools. Klaviyo, Bird, and Attentive become point solutions in our story.

Foundational (durable polish)

* Editor reliability hardening — measurable autosave / preview accuracy SLOs
* Mobile preview accuracy parity with real-device tests
* Performance budget — hard ceiling on canvas latency at 100+ blocks
* Accessibility & compliance polish (WCAG 2.2, GDPR-aware AI, SOC 2 trail)

Differentiated (category move)

* `D5` 1-to-1 generative personalization (Singulate-style) on Intuit data graph
* `D6` Agentic orchestration — channel + time + variant + cap, per recipient
* `D9` Hybrid code/no-code editor (React Email layer for designers/devs)
* `D10` Click-to-WhatsApp ad → builder → flow loop with Meta-side creative gen

**Demo line:** "Set the goal. The agent picks the channel, the time, the variant, and writes a unique message per recipient using your Intuit customer graph. You set guardrails, not micro-decisions."

## 21How we measure winning each phase

Phase 1 success

* Win-rate vs Klaviyo in head-to-head SMB & mid-market evals: **+15 pts**
* Feature-parity-loss reasons in CRM: **cut by 60%**
* "Editor lost my work" support tickets: **< 1/10K sends**
* Active omnichannel campaign sends (email+SMS+push): **2× lift**

Phase 2 success

* WhatsApp campaigns sent through Mailchimp: **1M+/month**
* International new-logo ARR (esp. EMEA, India, LATAM): **+30%**
* AMP-block adoption among ecom accounts: **30%+**
* Cross-channel reply-handled rate: **80%+ within builder**

Phase 3 success

* Agent-mode adoption among ecom Standard+: **40%**
* 1-to-1 personalized sends as % of total: **25%+**
* Lift on agent-mode vs manual: **2× campaign revenue per send**
* Analyst & press category reframe: **"agentic engagement OS"**

## 22Risks & guardrails

**UI churn risk.** Klaviyo gets called out for monthly UI changes — don't replicate. Ship a stable shell; iterate behind feature flags. Keep Classic Builder users protected.

**AI quality bar.** Subject Line AI burned Klaviyo's AI credibility (generic output). Don't ship F3/F2/D5 until they beat hand-written drafts in blind tests with real merchants.

**Channel-cost discipline.** Bird commoditized SMS to attack Twilio. WhatsApp template costs scale fast. Build cost-aware sending UX (live cost preview pre-send) — turn it into a differentiator.

**Sources (Page 4):** Y Combinator companies directory (Bird, Apten, Outbound, Zaymo, Mailmodo, Eden, Loops, Resend), Bird/MessageBird (TechCrunch rebrand Feb 2024 + $200M Series C 2020 at $3B → $3.8B today, 15K+ customers, 170+ countries, $500M–$1B ARR per FundBat), Attentive (Wikipedia — $500M+ ARR 2024, 8K+ businesses, \~$2B Cyber Week 2025), Braze (FY25 investor release — $693M ARR, 2,296 customers, 247 at $500K+, OfferFit acquisition), Customer.io (vendor materials — $100M ARR Sep 2025, 9K+ brands, 111% NDR), Bloomreach (press release — $260M+ ARR, Loomi AI), Postscript ($65M Series C 2022, 8K+ Shopify brands), Sendlane ($20M Series A, $7M+ ARR — Christine Hall TechCrunch), Resend (resend.com/blog/series-a — $18M a16z Dec 2024, 200K developers, Warner Bros / Decathlon / Raycast), Loops (loops.so — YC W22, $13M total, $3.2M seed Craft Ventures Sep 2023), Knock (state-of-notification report 2025), Singulate (singulate.com — $2.3M pre-seed Bowery + Seedcamp), Backstroke / Mutiny / Dreamlit (vendor pages), AiSensy (CB Insights, Pitchonnet, Zee News, CXOToday — 50K+ businesses, ₹1,000+cr brand revenue, 80–100M msgs/mo, Meta CTWA Partner of the Year 2024, Dream Green Capital), Wati (16K+ customers, 4.6 G2), Charles / Zoko / Interakt / LimeChat (vendor pages), Mailchimp current state (mailchimp.com/help/compare-mailchimps-email-builders — 250 templates new builder, mailchimp.com/newsroom/introducing-intuit-assist, Feb 2026 release — Site Tracking Pixel, 26% more ecom triggers, SMS Europe expansion, Yotpo/Judge.me integrations), Mailchimp vs Klaviyo gap analysis (Datawhistl capability map, get-creative.co, sendpulse).  
  
_Methodology:_ threat tiers built on (a) funding raised, (b) ARR / customer count, (c) editor-builder relevance, (d) likely overlap with Mailchimp's SMB+mid-market book. Foundational features = those Klaviyo and 2+ other competitors have but Mailchimp's email builder credibly lacks today. Differentiated features = best ideas across the threat landscape that bind well to Mailchimp's omnichannel + Intuit-data advantage. Phasing prioritized for Phase-1 head-to-head Klaviyo demos, then breadth (Phase 2), then category move (Phase 3).

Competitive Intelligence · Executive Brief · Page 5 of 11

# HVC VOC + research-session prioritization — combined-signal plan

Two reinforcing data sources for the Mailchimp email builder: **(1)** 18-month HVC Slack VOC across `#hvc_feedback`, `#mc-hvc-escalations`, `#mc-feedback-summary` (themed, MRR-weighted), and **(2)** 33 hand-extracted findings from PM research sessions with strategic HVC accounts (Eric · Jacob · Nina). Combined-signal scored, then sequenced into a 3-phase plan to close the most HVC MRR risk and deepest research conviction first.

**Sources:** 3 Slack channels + 3 research sessions

**HVC threshold:** \>$299/mo MRR · strategic accounts

150 + 33

HVC Slack messages + strategic-HVC research findings (Eric · Jacob · Nina)

28 + 33

Slack themes + research items · 10 HIGH · 13 MEDIUM · 7 LOW · 3 DELIGHT

$73,465/mo

Aggregate Slack-attributed HVC MRR exposure · plus 7 research items reinforce specific themes

8 quick wins

Research items sized as Quick Wins · 7 HIGH-priority items still > Quick Win

**Methodology — two reinforcing data sources.** **(1) Slack VOC:** 150 HVC messages across `#hvc_feedback` \+ `#mc-hvc-escalations` (May 2025 → April 2026), thematized with HVC MRR exposure aggregated per theme.**(2) Strategic HVC research sessions:** 33 hand-extracted findings across 3 PM-led research sessions with strategic Mailchimp HVC accounts (Eric session 1, Jacob session 2, Nina session 3). Each finding tagged with frustration, engineering sizing, exclusivity, and pre-assigned priority.**Combined-signal score** \= priority\_weight + 2×frustration\_weight (×100) + Slack\_MRR/100 + category\_boost (Bug+50, Parity+30, Delight−1000), divided by sizing\_weight (Quick Win=1, Medium Lift=2, Big Lift=4). Items appearing in _both_ sources get a natural double boost via the MRR term. `#mc-feedback-summary` remains broader/non-HVC reference.

## 23Critical bugs (Slack VOC) — by HVC MRR exposure

| Theme                                                           | HVC MRR exposure               | Top customer quotes (Slack + Fullstory links)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preview from template list / template gallery navigation**Bug | $3,6001 HVC users · 1 mentions | $3,600/mo · Premium · 2025-09-15 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1757976270527039) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/af43bce4-713a-41b4-9922-de5902d2e2bf%3A8fdde2b2-5dd0-4f7c-94f8-638c7b2bd638?integration%5Fsrc=qualtrics)"All I needed to do today was to preview some of the templates. I use to ba bale to do that from the template list. Now I need to go to edit the template before I can get to preview it. It's only one more step, but it's really annoying!!"                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Text formatting / fonts / spacing**Bug                        | $3,0195 HVC users · 5 mentions | $727/mo · — · 2026-04-22 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1776896347423629) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/4c70259c-abbe-4b9b-80b7-b3c14c0c2737%3A8904f945-e7a4-4771-9894-d5e4eb0f0336?integration%5Fsrc=qualtrics)"Your first line custoner support is often terrible and then it takes too long to get to someone who knows what they are doing. Your support person on chat, name given was Ziggy (today at 5pm eastern), could not resolve a simple issue re fo…"$680/mo · Standard · 2026-02-20 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1771549880508059) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/fb6f10da-e4a7-4356-90dc-fa41068ef3f9%3Ac201ddb3-959c-4e2a-afc2-bea98d436fbc?integration%5Fsrc=qualtrics)"I often get frustrated with line spacing issues and type fonts that don't clear or change the way I want them to."                                  |
| **Hyperlink / button URL / link won't remove**Bug               | $2,7492 HVC users · 3 mentions | $949/mo · — · 2026-02-13 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770996973378069) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/1f95b57b-08fa-445d-b57b-37dfb759ddd3%3Ad14ef723-3604-4408-b3d9-36a033951b32?integration%5Fsrc=qualtrics)"I absolutely HATE that in the new builder Ctrl+K to insert links doesn't work on Firefox or Chrome. It's maddening! And I hate how the styling rules are so rigid now--I understand that it's probably trying to streamline the process, but wh…"$1,800/mo · Premium · 2025-06-09 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1749448185872999) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/69149c4f-0d12-44bc-a05e-00b5ddd30cf6%3A4acef924-2033-43bf-92fc-b5ec1aea2415?integration%5Fsrc=qualtrics)"Teh email design tool is so bad. It is not at all user friendly. I have tried 50 times to remove the link but it keeps popping up. Pathetic tool." |
| **Editor performance / lag / browser freeze**Bug                | $2,3273 HVC users · 3 mentions | $820/mo · — · 2026-02-10 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770757367177539) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/155f4e16-85da-4fdf-ab9e-05a4e945d596%3A3a354e02-efa4-49c0-a7aa-853fb17fc065?integration%5Fsrc=qualtrics)"Can't use the editor without my browser freezing. Useless."$802/mo · — · 2025-10-14 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1760441594183879)"Our template is very laggy and the site is unresponsive when adding new modules."                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Image editor bugs / black lines / asset rendering**Bug        | $6551 HVC users · 1 mentions   | $655/mo · — · 2025-05-05 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1746445778553929) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/243b9923-5216-4818-9855-2866ade21b8f%3A929a3e1d-06b2-4d94-a0de-1d518b80c346?integration%5Fsrc=qualtrics)"Mi piacerebbe che ci fossero più blocks tra cui scegliere, ad esempio testo + pulsante insieme o altro. Nel block social non c'è Telegram. A volte quando si lavora con l'editor foto si creano delle righe nere in alto o di lato sulla foto."                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Image upload / cropping / resize**Bug                         | $6211 HVC users · 1 mentions   | $621/mo · Standard · 2025-08-19 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1755606624125399) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/a78fd118-04fe-4f3e-9dd9-598372334ce9%3A4e446383-b49e-47ee-95ef-2bc8684da64f?integration%5Fsrc=qualtrics)"Content studio not loading images. Email builder breaking and not working properly. Had to keep quitting out and re-loading in order to swap images. Which I then couldn't see because content studio kept breaking. Absolutely shocking. And w…"                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Block reordering / lost layout**Bug                           | $3401 HVC users · 1 mentions   | $340/mo · — · 2025-09-15 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1757949961102769) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/2a00bd64-512e-4717-aa37-00b0ca82b4b1%3A66d6d56b-021c-4dd9-9d0c-54691e7801d7?integration%5Fsrc=qualtrics)"When making a long bulleted list, when I click in to make edits, the cursor jumps to a different place. There's no way to check for dynamic content prior to sending. It's hard to find aspects I use regularly - like email sign up forms or m…"                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## 24Key barriers (Slack VOC) — by HVC MRR exposure

| Theme                                                                 | HVC MRR exposure               | Top customer quotes (Slack + Fullstory links)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Generic 'editor is clunky / hard to use / unusable'**Barrier        | $5,6906 HVC users · 6 mentions | $918/mo · Premium · 2026-01-20 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1768927852031469) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/4a0b89ec-a10b-41d6-94f1-d0acb6216f69%3A8f6432cd-7315-4ff0-9e57-88040014ccd5?integration%5Fsrc=qualtrics)"The emails editor feels very clunky"$300/mo · — · 2026-01-11 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1768118402667719)"the newsletter editor is clunky. The prices are insane. If I could find another newsletter with the same segmentation functionality I would leave."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **UI churn / new builder dislike / 'bring back the old'**Barrier      | $5,2348 HVC users · 8 mentions | $949/mo · — · 2026-02-13 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770996973378069) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/1f95b57b-08fa-445d-b57b-37dfb759ddd3%3Ad14ef723-3604-4408-b3d9-36a033951b32?integration%5Fsrc=qualtrics)"I absolutely HATE that in the new builder Ctrl+K to insert links doesn't work on Firefox or Chrome. It's maddening! And I hate how the styling rules are so rigid now--I understand that it's probably trying to streamline the process, but wh…"$1,325/mo · Premium · 2026-02-02 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770066920468879) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/bc73070f-3709-48a9-9cc1-334738b5a681%3A213acac4-a3aa-44b2-9d23-ac6e29b0878a?integration%5Fsrc=qualtrics)"Can you please bring back the creative assistant feature? I used to use it a lot."                                                                                                                                                                   |
| **Steep learning curve / confusing UX**Barrier                        | $4,6776 HVC users · 6 mentions | $410/mo · Standard · 2025-12-08 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1765231520773259) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/a27d8f89-708b-41aa-88a0-3a1e719a4f77%3A0b937cfe-2b93-4bba-96ff-e2c8054e42d9?integration%5Fsrc=qualtrics)"My single biggest pain point is the templates editor. Each of the options poses challenges. We use largely custom-coded templates because they display most reliably across inboxes, but building an email with a custom template is buggy (edi…"$978/mo · Premium · 2025-10-29 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1761753787106789) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/ad362463-9f7a-4c6c-81c0-a54e702f83f4%3A0d39af7f-9f30-4c2a-899a-5fd17123a55f?integration%5Fsrc=qualtrics)"The UX flow for template use is extremely confusing and unintuitive"                                                                                                                                                                            |
| **Mobile preview accuracy / what-you-see-is-not-what-you-get**Barrier | $2,5752 HVC users · 2 mentions | $1,553/mo · — · 2025-12-09 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1765297849456199) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/055cd2e6-c9bd-46d5-848b-594a071c9e0d%3Ac81af71c-a3d5-4058-b7d8-70e46d9d6748?integration%5Fsrc=qualtrics)"the formatting bugs are making it so that we can't format in the proper alignment, with the correct link colors, with as many images as we'd like, and they are showing up differently in every email client server. I spent 5 hours on the pho…"$1,022/mo · Premium · 2025-11-24 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1764028168366679) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/589c8201-e3aa-47c7-a27d-d5453626ecaf%3A9c024469-5bf2-450a-aeb3-9cbe07b21f02?integration%5Fsrc=qualtrics)"Al momento de crear las campaña estas lucen diferente en el editor VS cómo lucen una vez en mi bandeja. En 2 ocasiones me han dejado sin respuesta los agentes que me contactan por correo cuando respondo en español. He tenido curiosidad de…"   |
| **Editor feels dated / less powerful than competitors**Barrier        | $1,3143 HVC users · 3 mentions | $439/mo · Premium · 2026-01-08 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1767888113021129) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/080bbbf6-6587-44a6-b3db-5ad84ec94ecd%3A1f86d8b4-531f-443e-a023-b1fece6ac1ef?integration%5Fsrc=qualtrics)"Overall it's very glitchy and I often have formatting issues show up when they are not visible on the editor and previews. It happens pretty frequently and I never had issues like that with Constant Contact. I would not use or recommend Ma…"$535/mo · Premium · 2025-12-18 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1766081046423769) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/88c01d08-1a16-48e5-8326-235e27599e59%3A8d8f253f-9347-4ac7-b330-4439a67a1ef8?integration%5Fsrc=qualtrics)"Former email developer for Intuit & web developer here. UX is great, very approachable. Email builder is really well done. I appreciate being able to set styles email-wide. Thank you for adding easy subject line a/b testing. 1\. Would lik…" |
| **Switching between views / tabs / modes**Barrier                     | $6622 HVC users · 2 mentions   | $331/mo · — · 2026-02-12 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770860533282159)"I would like if it was easier to use the results of an A/B test to replicate the winner into a new email without it still being an A/B test. Being able to easily switch between regular campaigns and tests would be nice."$331/mo · — · 2025-07-17 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1752769610640919) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/5f320762-4d1e-4cf2-afc4-7804587b7af3%3A79ed7c26-d1ad-45f6-aea4-1523bca01b51?integration%5Fsrc=qualtrics)"I want more options to have more than just 2 columns and I want a way to make blocked text show up as the same size in my emails when they are side by side. One is often a tiny bit taller. You have a template that has a 3 column style but…"                                                                                                                                                                                                           |

## 25Missing features (Slack VOC) — by HVC MRR exposure

| Theme                                                                           | HVC MRR exposure                | Top customer quotes (Slack + Fullstory links)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Saved sections / saved blocks / universal content**Missing Feature            | $13,6846 HVC users · 6 mentions | $1,150/mo · Premium · 2026-04-14 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1776210444038839)"I wish I could update list templates for from email, footer, etc., from within the creation interface. Right now I have to hunt it down. It's not easy to find this. Other than that, I need to spend more time exploring features to fully ans…"$1,010/mo · Standard · 2026-01-13 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1768330348142639)"I think a reusable drag and drop elements library would be helpful. Designed modules that would retain orientation and links — but then be editable after drop."                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Snap-to-grid / spacing alignment / structured layout**Missing Feature         | $7,7781 HVC users · 1 mentions  | $7,778/mo · — · 2025-05-20 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1747748989129779) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/a1e4ecc0-d8f4-43ce-8c1c-8a729c3a64a6%3Ae56eb376-82f3-4d27-a45c-26a1b6ab5997?integration%5Fsrc=qualtrics)"Allow for more structured email design, It is hard to line up spacing between elements. It would be nice if there was a snap to place feature or something to keep consistent spacing."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Advanced merge tag / content variables / conditional / loops**Missing Feature | $6,2252 HVC users · 2 mentions  | $5,200/mo · — · 2025-10-15 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1760551590742139) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/621648d8-6a09-4264-b7a0-de4b4e0f0360%3A4fad40e5-b979-407c-9893-07995fc88266?integration%5Fsrc=qualtrics)"- Allow for JSON objects in Merge Tags in order to use them in Templates Ex: Merge Tag: PRODUCT\_1, {item: "My Item", price: "$2.99" } and to use as \*\|PRODUCT\_1.item|\*"$1,025/mo · Premium · 2025-08-27 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1756311326941819) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/7d831e72-73a9-4eaa-9c30-50e28200c0d8%3A36a27aee-ae8c-4230-92ca-199f077d49a4?integration%5Fsrc=qualtrics)"Better scheduling tools. Let the user define multiple delivery dates and times + updated the Subject, while Mailchimp handles the message replication in the background. Add Content Variables (similar to merge tags, but for email content. E…"                                                                 |
| **Editor undo / redo / version history**Missing Feature                         | $2,1972 HVC users · 2 mentions  | $492/mo · — · 2026-03-20 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1773998492331739) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/fdcec621-48f2-4883-9848-96f468c7c374%3Acb28383d-ff1e-4e01-97e2-7bc3f1b255a8?integration%5Fsrc=qualtrics)"Every time I copy and past text into an email campaign template, it breaks the whole template and can't be undone"$1,705/mo · Premium · 2025-08-08 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1754643979706339)"Add template versioning sistem."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Custom CSS / direct HTML editor / view full code**Missing Feature             | $1,8021 HVC users · 1 mentions  | $1,802/mo · — · 2025-08-12 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1755001272661699) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/c203fc3c-8c38-4eb5-89f3-f4f46c3dfa9e%3A7e0fad21-a622-4340-94e5-73a3b3a145ea?integration%5Fsrc=qualtrics)"I would love to be able to view the full HTML code with the click of a button, along with a direct HTML editor tool. Not just a single block of code, but the entire email as a whole."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Better A/B testing / multivariate in builder**Missing Feature                 | $1,5392 HVC users · 2 mentions  | $1,208/mo · — · 2026-02-23 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1771832979531389) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/104f4658-dc34-4387-ab97-cc0b2bec9404%3A514ae373-9729-49a3-a80d-4032ef823a8f?integration%5Fsrc=qualtrics)"A better editor to set up mail flows and a better A/B test facilitys"$331/mo · — · 2026-02-12 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1770860533282159)"I would like if it was easier to use the results of an A/B test to replicate the winner into a new email without it still being an A/B test. Being able to easily switch between regular campaigns and tests would be nice."                                                                                                                                                                                                                                                                                                                                                                              |
| **Better post-send / editor navigation / find what was sent**Missing Feature    | $1,2021 HVC users · 1 mentions  | $1,202/mo · Premium · 2026-03-26 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1774559092743299) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/260baa7d-c7a4-464d-b486-b58c9608bc31%3A0959207d-7e80-4fc1-a3c5-ebff6ba6639b?integration%5Fsrc=qualtrics)"The navigation in general needs a lot of improvement. After an email is sent, the main post-activities (see the final email design, get its primary details like subject, etc.) need to be easy to achieve for both single and multivariant ema…"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Dark mode / inbox preview / multi-client testing**Missing Feature             | $1,0032 HVC users · 3 mentions  | $468/mo · — · 2026-02-15 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1771173388936109) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/c6256206-a4d2-4dc6-bf20-e2c911dab58e%3Abe003ce8-5f0e-4ec3-a1a2-34a363ffd08c?integration%5Fsrc=qualtrics)"Make it easier to develop an email for all the different screen experiences (light/dark mode in particular, but also mobile and desktop, while improved, has some room to grow. We'd also like to place background images in the new builder, b…"$535/mo · Premium · 2025-12-18 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1766081046423769) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/88c01d08-1a16-48e5-8326-235e27599e59%3A8d8f253f-9347-4ac7-b330-4439a67a1ef8?integration%5Fsrc=qualtrics)"Former email developer for Intuit & web developer here. UX is great, very approachable. Email builder is really well done. I appreciate being able to set styles email-wide. Thank you for adding easy subject line a/b testing. 1\. Would lik…" |
| **Editor consistency / new builder for journeys / one editor**Missing Feature   | $9041 HVC users · 1 mentions    | $904/mo · Premium · 2026-03-06 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1772789988305819) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/d6bf4796-743c-4566-93b8-65360baf1455%3Ac7bc96fb-bad6-4f32-a967-3ee3fa35cbe2?integration%5Fsrc=qualtrics)"I'm actually quite disappointed that your customer journeys are still edited in your legacy builder. Kind of takes away the point..."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Footer customization / unsubscribe legal control**Missing Feature             | $8151 HVC users · 1 mentions    | $815/mo · Premium · 2026-01-07 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1767809246872159) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/454d3877-0e35-469d-9634-c71c3532d75e%3A1724e075-527e-4e69-9c7e-8f1da12701de?integration%5Fsrc=qualtrics)"Très insatisfait par le fait de nous forcer à utiliser vos mentions légales (footer email - unsubscribe) et pour les SMS (lien dans le SMS) alors qu'on a notre propre STOP SMS... Très insatisfait également de ne pas pouvoir réaliser un seg…"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Better image editor / asset management**Missing Feature                       | $7932 HVC users · 2 mentions    | $410/mo · — · 2025-11-25 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1764031513867889) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/455c6357-0536-4438-b311-9786f922c81b%3Aa698d276-43b6-47ad-afb4-fe46c5086174?integration%5Fsrc=qualtrics)"bring back the paint tool in the image editor"$383/mo · Standard · 2025-09-02 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1756850865860559) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/704924e4-2dca-4588-aed9-99fe9f042792%3Adfd554f7-e9bc-4a2c-a456-76a8297c277a?integration%5Fsrc=qualtrics)"The Image editor is not very flexible to work with, I often need to edit images outside of Mailchimp and then re-upload them."                                                                                                                                                                                                                                                                                                                     |
| **Better text/font/typography control**Missing Feature                          | $6551 HVC users · 1 mentions    | $655/mo · — · 2025-09-30 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1759270061399919)"It'd be amazing if you got a template for mailing that allows us to link any Google Font into our messages!"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **More block types (text+button combo, social, other)**Missing Feature          | $6551 HVC users · 1 mentions    | $655/mo · — · 2025-05-05 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1746445778553929) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/243b9923-5216-4818-9855-2866ade21b8f%3A929a3e1d-06b2-4d94-a0de-1d518b80c346?integration%5Fsrc=qualtrics)"Mi piacerebbe che ci fossero più blocks tra cui scegliere, ad esempio testo + pulsante insieme o altro. Nel block social non c'è Telegram. A volte quando si lavora con l'editor foto si creano delle righe nere in alto o di lato sulla foto."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Brand voice / tone learning AI**Missing Feature                               | $4101 HVC users · 1 mentions    | $410/mo · Standard · 2025-05-06 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1746551428691709) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/251a0923-cc52-4ce7-a75b-d0e78c62ffd8%3Ac0ebf738-6e0a-4aaa-882d-d8172d70f275?integration%5Fsrc=qualtrics)"Please stop the AI tool notifications - it disrupts our user experience. We have also had difficulties with our brand guide being easily accessible during email creation."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Conditional / dynamic content per segment**Missing Feature                    | $3401 HVC users · 1 mentions    | $340/mo · — · 2025-09-15 · [Slack](https://intuit.enterprise.slack.com/archives/C051Y4H98VB/p1757949961102769) · [Fullstory](https://app.fullstory.com/ui/ZHBMT/client-session/2a00bd64-512e-4717-aa37-00b0ca82b4b1%3A66d6d56b-021c-4dd9-9d0c-54691e7801d7?integration%5Fsrc=qualtrics)"When making a long bulleted list, when I click in to make edits, the cursor jumps to a different place. There's no way to check for dynamic content prior to sending. It's hard to find aspects I use regularly - like email sign up forms or m…"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## 26Strategic HVC research session findings (Eric · Jacob · Nina)

33 hand-extracted findings from PM research sessions with strategic Mailchimp HVC accounts. Sorted by Priority then Score. The ↔ Slack badge appears where the same issue is also present in Slack VOC and shows the MRR exposure.

| #     | Source | Category       | Surface                 | Detail                                                                                                                                                                              | Summary (↔ Slack reinforcement where applicable) | Frust. | Excl. | Score       | Sizing | Priority |
| ----- | ------ | -------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------ | ----- | ----------- | ------ | -------- |
| S1.1  | Eric   | UI Improvement | Templates               | Template library navigation is frustrating — going back after previewing a template doesn't return to the same place, and page keeps reloading. ↔ Slack $3,600/mo                   | High                                             | no     | 5     | Medium Lift | HIGH   |          |
| S1.5  | Eric   | UI Improvement | Drag & Drop             | Drag and drop requires grabbing a specific handle instead of the element directly. Non-intuitive and frustrating. ↔ Slack $5,690/mo                                                 | High                                             | no     | 5     | Quick Win   | HIGH   |          |
| S1.7  | Eric   | UI Improvement | General                 | 2-column layout discoverability is poor — user needed help to find that images were nested inside a Columns block to control desktop vs mobile rendering. ↔ Slack $4,677/mo         | High                                             | no     | 5     | Medium Lift | HIGH   |          |
| S1.11 | Eric   | Feature Parity | Reusable Blocks         | No universal/global block functionality. Can't update a block once (e.g., footer year) and have it propagate across all emails/campaigns. ↔ Slack $13,684/mo                        | High                                             | no     | 5     | Medium Lift | HIGH   |          |
| S1.14 | Eric   | Bug            | General                 | Email editor crashed with a generic error message and refreshed, losing user's work. ↔ Slack $2,327/mo                                                                              | High                                             | no     | 5     | Quick Win   | HIGH   |          |
| S2.35 | Jacob  | Bug            | Brand Application       | Email templates don't apply saved brand kit button styles. Template uses generic button colors instead of user's defined brand buttons.                                             | Medium                                           | no     | 5     | Medium Lift | HIGH   |          |
| S2.89 | Jacob  | Feature Parity | Reusable Blocks         | Still no reusable/universal content blocks. Can't update a footer once and have it propagate across all emails. Repeated from Session 2 (re-raised by Jacob). ↔ Slack $13,684/mo    | Medium                                           | no     | 5     | Medium Lift | HIGH   |          |
| S1.8  | Eric   | Feature Parity | Cart Abandonment        | Cart block in abandoned cart automation email is not editable. For brand-conscious agencies, un-editable blocks are a dealbreaker.                                                  | High                                             | YES    | 4     | Medium Lift | HIGH   |          |
| S2.29 | Jacob  | UI Improvement | General                 | Product recommendation blocks are hard to discover in the email builder content panel.                                                                                              | Medium                                           | no     | 4     | Medium Lift | HIGH   |          |
| S2.53 | Jacob  | Bug            | Product Blocks          | Product rec preview shows placeholder products instead of actual Shopify store products despite active integration.                                                                 | Low                                              | no     | 3     | Quick Win   | HIGH   |          |
| S1.2  | Eric   | UI Improvement | Templates               | Template preview doesn't show how brand kit assets would look in-situ. Logo auto-replacement only happens after loading, not during browse.                                         | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S1.4  | Eric   | Bug            | Images                  | Image block fill toggle is one-way — switching from Original to Fill can't be reversed back to Original.                                                                            | Medium                                           | no     | 4     | Quick Win   | MEDIUM |          |
| S1.10 | Eric   | UI Improvement | Discount code block     | Discount code editing is confusing — user couldn't figure out how to display the code prominently in the email.                                                                     | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S1.12 | Eric   | UI Improvement | Merge Tags              | Merge tag / dynamic data toggle is undiscoverable. User couldn't figure out how to enable personalization variables.                                                                | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S1.13 | Eric   | UI Improvement | General                 | Order items block is not editable and provides no visual cue distinguishing it from editable blocks. User wasted significant time troubleshooting.                                  | Medium                                           | no     | 4     | Quick Win   | MEDIUM |          |
| S1.59 | Eric   | Feature Parity | Brand & Global Styles   | Global styles panel is undiscoverable. For brand-conscious agencies, every email element must be editable for font and hex color. Non-editable blocks are dealbreakers.             | High                                             | YES    | 4     | Big Lift    | MEDIUM |          |
| S2.30 | Jacob  | Bug            | General                 | Layout option selector (horizontal/vertical) renders in a way that looks like a loading state, confusing users into waiting.                                                        | Medium                                           | no     | 4     | Quick Win   | MEDIUM |          |
| S2.33 | Jacob  | UI Improvement | General                 | Email preview loads very slowly, especially when discount code or dynamic content is involved. ↔ Slack $2,327/mo                                                                    | Medium                                           | no     | 4     | Big Lift    | MEDIUM |          |
| S2.34 | Jacob  | UI Improvement | Integrations            | Clicking into app integrations from within the email builder navigates away entirely, losing the user's context.                                                                    | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S2.36 | Jacob  | Bug            | Email within automation | Logo is correctly applied in email builder but shows as placeholder in automation flow preview cards.                                                                               | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S2.39 | Jacob  | UI Improvement | Email within automation | Email preview thumbnails in automation flow view are static/non-interactive — can't scroll or click into them.                                                                      | Medium                                           | no     | 4     | Medium Lift | MEDIUM |          |
| S2.50 | Jacob  | Feature Parity | Product Blocks          | Product rec block has a low max item count and no option to hide/show price — limiting customization for e-commerce emails.                                                         | Medium                                           | YES    | 4     | Medium Lift | MEDIUM |          |
| S2.38 | Jacob  | Feature Parity | Test Send               | No ability to save and name test email recipient lists. Agencies need reusable, named seed lists shared across team members.                                                        | Low                                              | YES    | 2     | Medium Lift | MEDIUM |          |
| S1.6  | Eric   | UI Improvement | Crop                    | Crop function is not inline — user expected to crop directly on the canvas with original/cropped comparison side by side.                                                           | Medium                                           | no     | 4     | Quick Win   | LOW    |          |
| S1.3  | Eric   | UI Improvement | Images                  | Stock image library quality is unimpressive — user assumed results were AI-generated rather than curated stock photography.                                                         | Low                                              | no     | 3     | Quick Win   | LOW    |          |
| S1.9  | Eric   | UI Improvement | General                 | Anchor functionality is too complex and poorly explained — experienced user abandoned it immediately.                                                                               | Medium                                           | YES    | 3     | Medium Lift | LOW    |          |
| S2.37 | Jacob  | UI Improvement | Link Checker            | Link checker is slow and doesn't indicate which specific links have been verified vs. pending.                                                                                      | Low                                              | no     | 3     | Medium Lift | LOW    |          |
| S2.54 | Jacob  | UI Improvement | General                 | Trigger/action select dropdowns are too small and require extra clicks — should open pre-expanded.                                                                                  | Low                                              | no     | 3     | Medium Lift | LOW    |          |
| S2.31 | Jacob  | Feature Parity | Social Media Icons      | Social icon block only offers preset color themes. No custom hex color option for brand-specific icon styling.                                                                      | Low                                              | YES    | 2     | Medium Lift | LOW    |          |
| S2.32 | Jacob  | UI Improvement | Social Media Icons      | Social icon block doesn't warn when too many icons are added to fit on one line, causing layout overflow.                                                                           | Low                                              | YES    | 2     | Medium Lift | LOW    |          |
| S3.8  | Nina   | Delight        | Accessibility           | Auto-generated alt text was a surprise delight. Agency spends significant time on alt text for image-heavy D2C emails — this feature saves meaningful effort.                       | Delight                                          | no     | 3     | NA          | NA     |          |
| S3.19 | Nina   | Delight        | Product Blocks          | Product recommendation blocks and dynamic product feeds were easier to implement than in competing platforms. Drag-and-drop with pre-built data properties was a positive surprise. | Delight                                          | no     | 3     | NA          | NA     |          |
| S3.20 | Nina   | Delight        | General                 | Email builder praised as intuitive and standard. Core email creation experience met expectations of a Klaviyo power user.                                                           | Delight                                          | no     | 3     | NA          | NA     |          |

## 27Reinforced items — where both Slack VOC _and_ research sessions agree

These themes show up in **both** the high-volume Slack signal _and_ the deep PM research conversations. Highest credibility — multi-source confirmation. Phase 1 priority candidates.

Saved sections / saved blocks / universal content

$13,684/mo

Slack: 6 HVC users · $13,684/mo Research: 2 session findings

S1.11 (Eric) S2.89 (Jacob) 

Generic 'editor is clunky / hard to use / unusable'

$5,690/mo

Slack: 6 HVC users · $5,690/mo Research: 1 session finding

S1.5 (Eric) 

Steep learning curve / confusing UX

$4,677/mo

Slack: 6 HVC users · $4,677/mo Research: 1 session finding

S1.7 (Eric) 

Preview from template list / template gallery navigation

$3,600/mo

Slack: 1 HVC users · $3,600/mo Research: 1 session finding

S1.1 (Eric) 

Editor performance / lag / browser freeze

$2,327/mo

Slack: 3 HVC users · $2,327/mo Research: 2 session findings

S1.14 (Eric) S2.33 (Jacob) 

## 28REVISED 3-phase plan — combined-signal prioritization

Each row scored on combined signal. Phase boundaries are scored quantiles of the unified backlog (research findings + Slack-only themes). The **$/mo column shows Slack-attributed HVC MRR exposure**; research-only items show "—" (research-confirmed strategic-HVC pain that hasn't yet surfaced via Qualtrics PRS).

Phase 1 · 0–3 months · Stop the bleed + reinforced items

### Top 17 items by combined signal · Slack MRR addressed: $62,899/mo

| Cat     | Item                                                                                                                                | Source        | Slack $/mo | Frust. | Sizing      | Score |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- | ------ | ----------- | ----- |
| Bug     | Email editor crashed with a generic error message and refreshed, losing user's work.                                                | Eric · S1.14  | $2,327/mo  | High   | Quick Win   | 1673  |
| Barrier | Drag and drop requires grabbing a specific handle instead of the element directly. Non-intuitive and frustrating.                   | Eric · S1.5   | $5,690/mo  | High   | Quick Win   | 1657  |
| Bug     | Product rec preview shows placeholder products instead of actual Shopify store products despite active integration.                 | Jacob · S2.53 | —          | Low    | Quick Win   | 1250  |
| Bug     | Image block fill toggle is one-way — switching from Original to Fill can't be reversed back to Original.                            | Eric · S1.4   | —          | Medium | Quick Win   | 950   |
| Bug     | Layout option selector (horizontal/vertical) renders in a way that looks like a loading state, confusing users into waiting.        | Jacob · S2.30 | —          | Medium | Quick Win   | 950   |
| Barrier | Order items block is not editable and provides no visual cue distinguishing it from editable blocks. User wasted significant time … | Eric · S1.13  | —          | Medium | Quick Win   | 900   |
| Missing | No universal/global block functionality. Can't update a block once (e.g., footer year) and have it propagate across all emails/cam… | Eric · S1.11  | $13,684/mo | High   | Medium Lift | 883   |
| Barrier | 2-column layout discoverability is poor — user needed help to find that images were nested inside a Columns block to control deskt… | Eric · S1.7   | $4,677/mo  | High   | Medium Lift | 823   |
| Barrier | Template library navigation is frustrating — going back after previewing a template doesn't return to the same place, and page kee… | Eric · S1.1   | $3,600/mo  | High   | Medium Lift | 818   |
| Missing | Cart block in abandoned cart automation email is not editable. For brand-conscious agencies, un-editable blocks are a dealbreaker.  | Eric · S1.8   | —          | High   | Medium Lift | 815   |
| Missing | Still no reusable/universal content blocks. Can't update a footer once and have it propagate across all emails. Repeated from Sess… | Jacob · S2.89 | $13,684/mo | Medium | Medium Lift | 783   |
| Missing | Snap-to-grid / spacing alignment / structured layout                                                                                | Slack VOC     | $7,778/mo  | Medium | Medium Lift | 754   |
| Missing | Advanced merge tag / content variables / conditional / loops                                                                        | Slack VOC     | $6,225/mo  | Medium | Medium Lift | 746   |
| Barrier | UI churn / new builder dislike / 'bring back the old'                                                                               | Slack VOC     | $5,234/mo  | Medium | Medium Lift | 726   |
| Bug     | Email templates don't apply saved brand kit button styles. Template uses generic button colors instead of user's defined brand but… | Jacob · S2.35 | —          | Medium | Medium Lift | 725   |
| Barrier | Product recommendation blocks are hard to discover in the email builder content panel.                                              | Jacob · S2.29 | —          | Medium | Medium Lift | 700   |
| Barrier | Crop function is not inline — user expected to crop directly on the canvas with original/cropped comparison side by side.           | Eric · S1.6   | —          | Medium | Quick Win   | 600   |

Phase 2 · 3–9 months · Capability parity + reliability

### Next 18 items · Slack MRR addressed: $17,400/mo

| Cat     | Item                                                                                                                                | Source        | Slack $/mo | Frust. | Sizing      | Score |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- | ------ | ----------- | ----- |
| Bug     | Text formatting / fonts / spacing                                                                                                   | Slack VOC     | $3,019/mo  | High   | Medium Lift | 590   |
| Bug     | Hyperlink / button URL / link won't remove                                                                                          | Slack VOC     | $2,749/mo  | High   | Medium Lift | 589   |
| Missing | Editor undo / redo / version history                                                                                                | Slack VOC     | $2,197/mo  | Medium | Medium Lift | 476   |
| Bug     | Logo is correctly applied in email builder but shows as placeholder in automation flow preview cards.                               | Jacob · S2.36 | —          | Medium | Medium Lift | 475   |
| Missing | Custom CSS / direct HTML editor / view full code                                                                                    | Slack VOC     | $1,802/mo  | Medium | Medium Lift | 474   |
| Missing | Better A/B testing / multivariate in builder                                                                                        | Slack VOC     | $1,539/mo  | Medium | Medium Lift | 473   |
| Missing | Product rec block has a low max item count and no option to hide/show price — limiting customization for e-commerce emails.         | Jacob · S2.50 | —          | Medium | Medium Lift | 465   |
| Barrier | Mobile preview accuracy / what-you-see-is-not-what-you-get                                                                          | Slack VOC     | $2,575/mo  | Medium | Medium Lift | 463   |
| Barrier | Editor feels dated / less powerful than competitors                                                                                 | Slack VOC     | $1,314/mo  | Medium | Medium Lift | 457   |
| Barrier | Template preview doesn't show how brand kit assets would look in-situ. Logo auto-replacement only happens after loading, not durin… | Eric · S1.2   | —          | Medium | Medium Lift | 450   |
| Barrier | Discount code editing is confusing — user couldn't figure out how to display the code prominently in the email.                     | Eric · S1.10  | —          | Medium | Medium Lift | 450   |
| Barrier | Merge tag / dynamic data toggle is undiscoverable. User couldn't figure out how to enable personalization variables.                | Eric · S1.12  | —          | Medium | Medium Lift | 450   |
| Barrier | Clicking into app integrations from within the email builder navigates away entirely, losing the user's context.                    | Jacob · S2.34 | —          | Medium | Medium Lift | 450   |
| Barrier | Email preview thumbnails in automation flow view are static/non-interactive — can't scroll or click into them.                      | Jacob · S2.39 | —          | Medium | Medium Lift | 450   |
| Barrier | Stock image library quality is unimpressive — user assumed results were AI-generated rather than curated stock photography.         | Eric · S1.3   | —          | Low    | Quick Win   | 400   |
| Missing | No ability to save and name test email recipient lists. Agencies need reusable, named seed lists shared across team members.        | Jacob · S2.38 | —          | Low    | Medium Lift | 365   |
| Missing | Better post-send / editor navigation / find what was sent                                                                           | Slack VOC     | $1,202/mo  | Medium | Medium Lift | 321   |
| Missing | Dark mode / inbox preview / multi-client testing                                                                                    | Slack VOC     | $1,003/mo  | Medium | Medium Lift | 320   |

Phase 3 · 9–18 months · Depth + delight + tail

### Remaining 18 items · Slack MRR addressed: $9,177/mo

| Cat     | Item                                                                                                                                | Source        | Slack $/mo | Frust. | Sizing      | Score |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------- | ------ | ----------- | ----- |
| Missing | Editor consistency / new builder for journeys / one editor                                                                          | Slack VOC     | $904/mo    | Medium | Medium Lift | 320   |
| Missing | Footer customization / unsubscribe legal control                                                                                    | Slack VOC     | $815/mo    | Medium | Medium Lift | 319   |
| Barrier | Anchor functionality is too complex and poorly explained — experienced user abandoned it immediately.                               | Eric · S1.9   | —          | Medium | Medium Lift | 300   |
| Missing | Global styles panel is undiscoverable. For brand-conscious agencies, every email element must be editable for font and hex color. … | Eric · S1.59  | —          | High   | Big Lift    | 282   |
| Barrier | Email preview loads very slowly, especially when discount code or dynamic content is involved.                                      | Jacob · S2.33 | $2,327/mo  | Medium | Big Lift    | 231   |
| Bug     | Image editor bugs / black lines / asset rendering                                                                                   | Slack VOC     | $655/mo    | Low    | Medium Lift | 228   |
| Bug     | Image upload / cropping / resize                                                                                                    | Slack VOC     | $621/mo    | Low    | Medium Lift | 228   |
| Bug     | Block reordering / lost layout                                                                                                      | Slack VOC     | $340/mo    | Low    | Medium Lift | 227   |
| Missing | Better image editor / asset management                                                                                              | Slack VOC     | $793/mo    | Low    | Medium Lift | 219   |
| Missing | Better text/font/typography control                                                                                                 | Slack VOC     | $655/mo    | Low    | Medium Lift | 218   |
| Missing | More block types (text+button combo, social, other)                                                                                 | Slack VOC     | $655/mo    | Low    | Medium Lift | 218   |
| Missing | Brand voice / tone learning AI                                                                                                      | Slack VOC     | $410/mo    | Low    | Medium Lift | 217   |
| Missing | Conditional / dynamic content per segment                                                                                           | Slack VOC     | $340/mo    | Low    | Medium Lift | 217   |
| Missing | Social icon block only offers preset color themes. No custom hex color option for brand-specific icon styling.                      | Jacob · S2.31 | —          | Low    | Medium Lift | 215   |
| Barrier | Switching between views / tabs / modes                                                                                              | Slack VOC     | $662/mo    | Low    | Medium Lift | 203   |
| Barrier | Social icon block doesn't warn when too many icons are added to fit on one line, causing layout overflow.                           | Jacob · S2.32 | —          | Low    | Medium Lift | 200   |
| Barrier | Link checker is slow and doesn't indicate which specific links have been verified vs. pending.                                      | Jacob · S2.37 | —          | Low    | Medium Lift | 200   |
| Barrier | Trigger/action select dropdowns are too small and require extra clicks — should open pre-expanded.                                  | Jacob · S2.54 | —          | Low    | Medium Lift | 200   |

## 29Strategic delights to defend (Nina session)

**Auto-generated alt text (S3.8).** Strategic agency calls this a "surprise delight" — saves meaningful effort on image-heavy D2C emails. Keep investing; market it harder; consider expanding to image descriptions inside Image Remix-style edits.

**Product recommendation blocks (S3.19).** "Easier to implement than competitors." This is a defensible Mailchimp moat against Klaviyo's product blocks — preserve the simplicity, expand depth (more catalogs, more dynamic data properties).

**Core builder met Klaviyo power-user expectations (S3.20).** Nina's quote: "intuitive and standard." Validates that table-stakes is achieved on the core canvas — now ship the differentiated bets in Page 4 to leapfrog.

**Sources (Page 5):** _Slack:_ `#hvc_feedback` (C051Y4H98VB) · `#mc-hvc-escalations` (C095FJ3SQF4) · `#mc-feedback-summary` (C06EVEZ4ZTQ)._Research sessions:_ 33 PM-extracted findings — Eric (Session 1, 15 findings) · Jacob (Session 2, 15 findings) · Nina (Session 3, 3 delights). Per-quote source-of-record: Slack permalink + Fullstory session replay (where Qualtrics captured one).  
  
_Combined-signal score (per item):_ `(priority_weight + 2 × frustration_weight) × 100 + Slack_MRR/100 + category_boost (Bug+50, Parity+30, Delight−1000)`, divided by sizing\_weight (Quick Win=1, Medium Lift=2, Big Lift=4). Items confirmed by both Slack VOC and research sessions get a natural double boost. Phase boundaries are scored quantiles of the unified backlog. Strategic-HVC research findings are weighted heavily because they come from PM-led 1:1 sessions with high-spend accounts — even a single research finding represents deeper conviction than a Slack ping.

Competitive Intelligence · Executive Brief · Page 6 of 11

# Direct customer research — HeyMarvin synthesis (50 sessions, 25 briefs)

Cross-customer view of how customers _actually_ create, design, and ship email campaigns in Mailchimp. Synthesized from 50 transcribed HeyMarvin UX research videos (\~25 hours of audio) across 25 individual customer briefs (17 very-high-signal, 10 high, 15 medium). Every claim links to a customer + transcript timestamp. Source repo: mailchimp-campaign-builder-research.

**Audio source:** 50 HeyMarvin UX videos

**Transcription:** Whisper small.en (local)

**Cohort:** DSB · ProServ · Internal

50

UX research transcripts (\~25 hr audio) — 17 very-high · 10 high · 15 medium · 7 low · 1 none

25

Customer briefs synthesized · all-substantive cohort with quote-level traceback

0

Customers named Klaviyo / ActiveCampaign / HubSpot organically — comparators were Bee.io · Adobe Express · Canva · Constant Contact · Outlook · Levitate

5+

Independent customers with power features unused for **years** — discovery is the single largest growth lever

## 30Headline finding — the bifurcated builder

The Mailchimp campaign builder is the **most-used surface in the dataset** — and the experience is bifurcated. For the **happy-path simple-newsletter cohort** (Kim Vavrick, Courtney Fong, Andrew Obeso, Nicholas H), the editor works fine: replicate-and-edit + drag-drop + send, same-day shipping. **For everyone else, friction concentrates in four predictable places:** layout flexibility, multi-author collaboration, asset/library management, and **discoverability of features that already exist**. Multiple very-high-signal customers describe being on the legacy builder for years without knowing the new builder shipped (Jack Hally, Jeffrey Davis), or paying for third-party design tools because the editor doesn't deliver Photoshop-style direct manipulation (Andrea D'Ercole's Bee.io detour for every send).

 "The point is if you were coming up with paying MailChimp, so we are pretty kind of stick with you and I'm adding on one software. The problem is not that — the problem is you need to make our life easier. No more complicated."**Andrea D'Ercole · DSB UK · \[00:35:18\]** — single most-quotable customer line in the dataset 

## 31Who's using the builder & the 5 workflow shapes

| Segment                                            | US                                                                                                               | UK                                                                                                  | Internal                                               |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **DSB**e-commerce, retail, services                | Andrew Obeso · Bob Gray · Clint Bartley · Courtney Fong · Jeffrey Davis · Kim Vavrick · Shauna Todd · Wes Turner | Andrea D'Ercole                                                                                     | —                                                      |
| **ProServ**legal, financial, advisory, association | Chris Rich · Jack Hally · Lauren Goglick · Nick Hamer · Shannon Riso                                             | Bianka Kiss · Gilles Gauthier · Ian Stuart · Jillian Ney · Matt Cresswell · Nicholas H · Peter Bell | —                                                      |
| **Internal Intuit**                                | —                                                                                                                | —                                                                                                   | Kyle Spalding (employee, dogfooding) · UXR Watch Party |

**5 distinct workflow shapes** in the dataset (drives feature priority by cohort):

#### 1Fast Monday-morning sender

Replicate last week, swap content, ship in 30–90 min. Editor friction = minutes per send → hours per year.

Andrew Obeso · Andrea D'Ercole · Kim Vavrick · Clint Bartley

#### 2All-week ad-libber

Living-document newsletter, edited continuously, multi-author review. **Save-conflicts dominate.**

Jack Hally — 76 Capital, 10–20 logins/day

#### 3Brand-first methodical builder

Top-down build from layout/padding before copy. Brand kit in active use. Builds patterns that should be reused but aren't (saved-blocks gap).

Wes Turner · Bob Gray

#### 4Third-party-tool-in-the-loop

Designs outside Mailchimp because the builder can't match. **Most strategically expensive cohort to ignore.**

Andrea D'Ercole (Bee.io) · Wes Turner (Adobe Express) · Jack Hally (Canva)

#### 5Non-adopter / barely uses the builder

Newsletter only, monthly/quarterly. Discovery gap on advanced features dominates.

Shannon · Matt Cresswell · Gilles Gauthier

## 32Top of funnel — template gallery & first-template setup

| Pattern                                                                    | Customer evidence                                                            | Voice (quote + timestamp)                                                                                                                                                                                                   |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **B2B / ProServ-specific templates missing**                               | Chris Rich · Bianka · Matt Cresswell · Jack Hally · Jillian Ney · Wes Turner | _"Many, given that you are not an e-commerce business, are really not tailored towards your organization, it feels like there's probably a missed opportunity."_ — Hannah Graffeo conceding live to Chris Rich \[00:28:15\] |
| **Templates feel "over-designed" for B2B / association use cases**         | Jillian Ney · Shannon (Levitate envy) · Bianka · Matt                        | _"I personally think they've been over-designed… they feel more like e-commerce emails than what they do, providing some information."_ — Jillian Ney \[00:06:09\]                                                          |
| **Polished templates feel "intimidating"** — show someone else's content   | Jillian Ney · Wes Turner                                                     | _"Love the look of these, but they actually feel quite intimidating because they're already designed with somebody else's content."_ — Jillian Ney \[00:28:55\]                                                             |
| **First-template build is non-intuitive** even when ongoing edits are easy | Nicholas H                                                                   | _"That first process of building, I found slightly tricky and not intuitive… if I tried to start from zero again, I think I would encounter the same challenges."_ — Nicholas H \[00:06:01\]                                |
| **Vibe-based template browsing** — customers ignore category labels        | Wes Turner                                                                   | _"Honestly I don't even look at the categories here on the left."_ — Wes Turner \[00:07:06\]                                                                                                                                |
| **Industry-specific templates are a competitor differentiator**            | Shannon (Levitate envy)                                                      | _"Depending on what field you're in, they have templates already. Like, oh, you are an accountant. Here's, you know, ideas."_ — Shannon \[00:26:36\]                                                                        |

**Implication:** the gallery does too much for some users and too little for others. ProServ buyers want skeletons + industry-appropriate aesthetics; e-commerce buyers want the opposite. Wes's instinct to browse by _layout only_ is the cleanest signal that the IA is mismatched with at least one major cohort.

## 33Builder canvas — 4 friction clusters

## 4a. Layout flexibility — biggest single complaint

* **Drag-and-drop is restrictive vs Photoshop / Bee.io.** Andrea demoed live. Andrea D'Ercole \[00:11:41\] Full Bee.io detour exists because Mailchimp can't match.
* **Side-by-side text-and-image alignment** unreliable when columns are unequal heights. Hannah confirmed gap. Andrea + Hannah \[00:10:46\]
* **Two-column layouts are 3 steps**, not 1\. _"Why was that three steps instead of one step?"_ Kyle Spalding \[00:22:25\] — Andrea hit the same.
* **Image resize is proportional only.** _"I can't really reduce on one side. I can't really move the image."_ Andrea \[00:13:30\]
* **Padding inconsistency across templates.** Wes builds top-down by layout/padding _first_ because templates have _"everything very small and centered, or the images are dancing around each other."_ Wes Turner \[00:09:48\]

## 4b. Image / asset library — "hunting in the attic"

* **Duplicate uploads** because the library is hard to search. _"Now I'm duplicating the image."_ Andrew Obeso \[00:12:38\]
* **Image-resize prompt every time.** Andrew uploads 15–20 images per send. _"That's about a minute… so an additional 20–30 minutes just to resize everything."_ Andrew \[00:25:31\]
* **Content asset management is unmemorable.** _"Hunting around in the attic for stuff."_ Peter Bell \[00:14:16\]
* **Major discovery gap on My Products / WooCommerce auto-pull.** Jeffrey didn't find this for 3.5 years. Devin demoed live: _"Damn, they're already in here."_ Jeffrey Davis \[00:21:13\]

## 4c. Multi-author collaboration breaks

* **Save conflicts** when multiple editors are in the canvas simultaneously. **3 independent customers report this:**
* Jack Hally \[00:11:54\] 76 Capital, 4 reviewers: _"I feel like we have a disconnect in what saves… neither of our work is there or one of our work there the other one isn't."_
* Kyle Spalding _"We just write it all right in the canvas"_ — same problem, same workaround (email-thread review).
* Bianka Kiss half her team is "scared" of the builder; teammates email Bianka or Katarina rather than self-serve.
* **No real-time co-edit, no change history, no draft-staging** — three independent feature asks for the same shape.

## 4d. Brand-fit pre-pass adds tax to every send

* **Pill CTAs need re-shaping every time** — Wes flips them to rectangles for brand fit on every send. Wes Turner \[00:14:10\]
* **Hyperlink color** — Nicholas couldn't figure out how to change link color from default blue to brand orange. Nicholas H \[00:13:11\]
* **Background color of text block** — Nicholas couldn't figure out the picker. Nicholas H \[00:14:18\]

## 34A/B testing & pre-flight checks

**The A/B test architecture forces the decision before content creation.** Wes had to _delete a finished email_, save it as a template, then re-enter via the multivariate-test path to test a content section against another. PM Jose confirmed it's a known limitation but not yet on the roadmap.

 "A/B testing it looks like is only available for like the subject line once you've created the content. Is that correct?… If I had a choice I would create the content first… and then afterward pick something from that email to A/B test."**Wes Turner · DSB US · \[00:25:15\] + \[00:27:04\]** 

**Adjacent friction (send confidence):**

* **Test-send-to-self workflow is universal** — Kim, Kyle, Jack all do this. Saved-blocks-style "send-and-thread" automation for boards/teams = high leverage.
* **Send button is "scary."** Kyle (Mailchimp employee) **schedules sends 15 min in the future to avoid hitting Send live.** _"I think it's so stressful."_ Kyle \[00:27:55\]
* **Send button is active before send-time is set.** _"It really bothers me that this send button is active when there isn't a send time. Like this isn't done."_ Kyle \[00:26:30\]

## 35Subject line, send time, from name & schedule

* **Subject line is "embarrassing if wrong"** (date errors). _"If I put December 11th on the 19th send, that's really embarrassing."_ Kyle \[00:30:11\] — high decision frequency.
* **From name "never changes"** — low decision frequency.
* **Audience "never changes"** for replicate-and-edit cohorts — low frequency.

 "The decision levels here don't feel the same. I'm never going to change \[audience or from-name\] either. So why do I go through this every time?"**Kyle Spalding · Internal · \[00:30:01\]** — campaign-setup checklist _flattens decisions of vastly different importance_ 

**Send-time discipline is real and arbitrary across cohorts:**

* Kim Vavrick — Tuesdays 9am Time Warp
* Jeffrey Davis — Tuesdays 9am Time Warp + auto-resend Wed to non-openers
* Kyle's running club — Tuesdays 2–4pm
* Jack Hally — Sundays 11am
* Andrew Obeso — distributors Mondays 8am

**No customer reported using Mailchimp's send-time-optimization feature** — either it doesn't exist by name or isn't discoverable.

## 36Reporting & post-send analysis

| Pattern                                                      | Evidence                                              | Notes                                                                                                                                                            |
| ------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No vertical / cohort benchmarks**                          | Bianka · Matt Cresswell · Shauna Todd · Jeffrey Davis | _"What actual benchmarking looks like — for, within some kind of, even if it's just like what SMBs do in a professional services industry."_ Matt \[00:30:39\]   |
| **Attribution methodology change unannounced**               | Jeffrey Davis                                         | Sept attribution-model update caused his Mailchimp-attributed-sales share to **jump 5–10% → 35–85%**. Devin confirmed internal change. **Customer-trust event.** |
| **No product-level reporting**                               | Jeffrey Davis (planning to build his own DB)          | Wants _"show me everyone who bought a bolt clamp."_                                                                                                              |
| **Multi-channel automation reporting fragments**             | Bianka                                                | Wants email + SMS + every touch point summarized in one view                                                                                                     |
| **Reporting features "set it and forget it" for happy-path** | Kim Vavrick · Courtney Fong                           | Glance at opens, that's it.                                                                                                                                      |

## 37Cross-cutting — discovery is the single largest growth lever

5+ independent customers report power features sitting **unused for years** because they didn't find them:

| Customer                     | Feature undiscovered                | How long                                               |
| ---------------------------- | ----------------------------------- | ------------------------------------------------------ |
| **Bianka Kiss** · ProServ UK | A/B testing                         | "A number of years"                                    |
| **Jack Hally** · ProServ US  | New email builder                   | **4–6 years** (inherited a replicated legacy template) |
| **Jeffrey Davis** · DSB US   | My Products / WooCommerce auto-pull | 3.5 years                                              |
| **Clint Bartley** · DSB US   | Welcome automation in DRAFT         | 1 year                                                 |
| **Wes Turner** · DSB US      | Saved blocks (still coming)         | Hadn't shipped at time of call                         |
| **Nicholas H** · ProServ UK  | Tag/segment usage                   | Multi-year (uses two-audience workaround)              |

**This is the strongest cross-cutting theme in the dataset.** Mailchimp's in-product feature discovery does not reach high-frequency users. Existing nudges (Peter Bell — _"It keeps popping up the automation side"_ Peter \[00:09:24\]) don't convert sophisticated users.

## 38Functional & emotional patterns — 3 cohorts

#### 1 · Polite / silent-churn risk (MOST COMMON)

→ Don't churn loud. Stop renewing one day.

Calm, self-blaming, not actively frustrated, but quietly under-utilizing. Repeated language: _"10–20% of capability"_, _"I should be doing more"_, _"I just haven't gotten deep enough."_

**Customers:** Andrea D'Ercole · Shannon · Peter Bell · Bianka · Clint · Matt · Jack Hally

#### 2 · Engaged / methodical builder

→ Closeable cohort. Articulate exact needs.

Curious, problem-solving, capable of articulating exactly what they need.

**Customers:** Wes Turner · Bob Gray · Chris Rich · Jeffrey Davis

#### 3 · Mature satisfied customer

→ Expand-revenue cohort. Wants more depth.

Warm tone, requesting more depth.

**Customers:** Kim Vavrick · Jeffrey Davis · Courtney Fong

**Anti-pattern:** Andrew Obeso's signal-saturation rejection of automations is unique. Sales-driven B2B already saturates customer relationships — doesn't want more touchpoints.

## 39Top 5 recommended bets — ranked by evidence × impact × feasibility

#### Saved blocks / section reuse CONFIRMED IN-FLIGHT

Confirmed by PM Jose during Wes Turner's session. Multiple customers asked for the same shape independently. **Ship and announce loudly to high-frequency users.**

**Evidence:** Wes (90–95% of his emails share three components) · Peter Bell (rotating advertiser blocks) · Kyle Spalding (recurring newsletter sections) · directly maps to F1 on Page 4 + Slack VOC's #1 missing feature ($13.7K/mo MRR · 6 HVC users)

#### Discovery / activation funnel for high-frequency users

Single largest growth lever. Mailchimp comes to the customer, not the other way around.

* In-product feature changelog surfacing new builders / A/B / My Products to high-frequency users (Bianka, Jack, Jeffrey)
* Weekly drip from Mailchimp itself (Clint's direct ask \[00:29:18\])
* DRAFT-resurrect prompt for stalled automations (Clint's year-old DRAFT)
* Save-as-template prompt after a successful send (Jillian's self-correction)
* Proactive chatbot suggestions for unbuilt automations (Bianka)

#### B2B / ProServ-specific template gallery

7+ ProServ customers explicitly want non-e-commerce templates. **Hannah Graffeo agreed live with Chris Rich.** Add a "Professional Services" / "B2B Services" / "Industry Association" template category with _skeleton-style_ structures (not finished mockups), brand-kit-aware defaults, info-heavy / image-light layouts.

**Evidence:** Chris Rich · Bianka · Matt Cresswell · Jack Hally · Jillian Ney · Wes Turner · Hannah's live concession \[00:28:15\]

#### Multi-author collaborative editing in the canvas

3 independent customers report save-conflicts and absent draft-staging. **Real-time co-edit + change history + per-block presence indicators.** Direct competition with Google Docs, Notion, Figma where this is table-stakes. Will land hardest with multi-reviewer ProServ + rotating-board nonprofit cohorts.

**Evidence:** Jack Hally (76 Capital, 4 reviewers) · Kyle Spalding (Mailchimp internal) · Bianka Kiss (half team scared)

#### Direct-manipulation editor improvements

Andrea D'Ercole's Bee.io detour is the strongest single piece of evidence for the editor's biggest gap: **direct image manipulation** (free resize, asymmetric resize, free placement, drag-anywhere). Competitive ground vs Bee.io, Adobe Express, Canva.

* Free / asymmetric image resize (Andrea)
* Bottom-align of side-by-side text boxes (Andrea, Hannah confirmed gap)
* Two-column layouts in 1 click, not 3 (Kyle, Andrea)
* Single-screen edit experience without "done" view back-and-forth (Andrea)
* A/B test sections post-creation (Wes)
* Brand-kit-aware template defaults — square/round corners, pill/box CTAs (Wes)

**Strategic alignment.** This direct-customer research _independently confirms_ the prioritization on Pages 4–5 from a different evidence base (1:1 PM-led research, no MRR weighting). The convergence is striking:**Bet 1 (Saved blocks)** ↔ **F1 + Slack $13.7K/mo** ↔ **S1.11 + S2.89 research findings.** **Bet 2 (Discovery)** ↔ **Page 4 attack vector "friendlier first-run + UI stability."** **Bet 3 (B2B templates)** ↔ new Page 4 differentiator candidate **not previously surfaced**.**Bet 4 (Multi-author collab)** ↔ new D11 to add to Page 4 (Google Docs / Figma table stakes).**Bet 5 (Direct manipulation)** ↔ **F4 (in-canvas AI image edit) + D9 hybrid editor.** Three data sources (Slack VOC + research session opportunity-DB + HeyMarvin 1:1s) now agree on the same Phase 1 backbone — high confidence to ship.

## 40Caveats & methodology integrity

* **Cohort bias:** 22 of 50 transcripts are Hannah Graffeo's 1:1s. Customers self-selected to the research panel — skews toward higher-engagement users; quieter customers underrepresented.
* **Whisper transcription artifacts:** Bianka K (1) was truncated to \~25-char segments and supplemented by her clean second meeting. Other transcripts have minor spelling artifacts (e.g. "Bee free" vs "Bee.io").
* **No customer named Klaviyo, ActiveCampaign, or HubSpot organically.** Comparators reached for: **Bee.io · Adobe Express · Canva · Constant Contact · Outlook · Microsoft Dynamics · Levitate · Text in Church · Shopify.** Notable absence in light of Page 1 / Page 2 competitive framing.

* **Internal Intuit voices** (Kyle Spalding · UXR Watch Party) provide candid product critique but _should not be cited as customer voice in any external doc_.
* **Editor friction is not uniform.** Kim Vavrick's interview is a clean counter-example: same product, simple newsletter, zero issues. Findings strongest for the **complex / multi-author / brand-conscious / B2B / image-heavy cohorts**.
* **Pipeline:** 50 HeyMarvin recordings → Whisper small.en local → keyword-density signal scan → 25 per-customer briefs with quote-level traceback → 11-section synthesis. Re-runnable via `render_briefs.py` in the source repo.

**Sources (Page 6):** Source repo — github.com/deepakp1308/mailchimp-campaign-builder-research (private — Intuit-internal). 25 customer briefs with timestamped Whisper transcripts: Andrea D'Ercole · Andrew Obeso · Bianka Kiss · Bob Gray · Chris Rich · Clint Bartley · Courtney Fong · Gilles Gauthier · Ian Stuart · Jack Hally · Jeffrey Davis · Jillian Ney · Kim Vavrick · Kyle Spalding · Lauren Goglick · Matt Cresswell · Nicholas H · Nick Hamer · Peter Bell · Shannon Riso · Shauna Todd · Wes Turner · plus internal voices (Kyle Spalding, UXR Watch Party). Triage signal scan: `scan_signal.py`. Per-brief renderer: `render_briefs.py`. Synthesis source-of-truth: `briefs/synthesis.md`.  
  
_Methodology integrity:_ Every claim on this page links to a customer + transcript timestamp \[HH:MM:SS\] traceable back to the original audio. No quotes have been paraphrased — all are verbatim from the Whisper transcripts (with the standard small-en spelling caveats). Synthesis preserves the original 11-section structure of `briefs/synthesis.md` (220 lines) condensed into a dense executive view without information loss.

Competitive Intelligence · Executive Brief · Page 7 of 11

# Email Builder health diagnostic — strategic analytics framework + live BigQuery findings

Lay-of-the-land for the new product lead. **What to measure, where to look, and what BigQuery says today (May 8, 2026).** Data sources: `bi_aggregate.product_health_weekly`, `customer_engagements_weekly`, `funnel_weekly`, `free_trials_weekly`, `churn_daily`, `product_journey_monthly` — all fresh through 2026-05-10\. (User-level `bi_product.product_reporting_email_base` is stale since Dec 2023 — flagged for refresh.)

**Run date:** 2026-05-08

**Window:** 12-month trend, 90-day cuts

**Queries run:** 9 priority cuts

31.5M

Total paid users (Apr 2026 base) · weekly churn-risk pool: 71K (0.23%)

8.6M

Email creates / mo (Apr 2026) · **−14% YoY**

7.1%

New-account → publish-first-email-in-week · **93% never publish** in week 1

$13K → 75%

HVC concentration: 13% of creates → 75% of sends · **3-10× better funnel conversion than non-HVC**

**The bottom line.** The builder serves 31.5M paid accounts and ships 18-29B sends/month. _Volume is healthy, but adoption is leaking_: first-time-sends are down 15-25% YoY across nearly every month, only 7% of newly-activated accounts publish a first email in their first week, and trial-to-paid + 12-month retention have both compressed. The platform is over-indexed on a thin top of HVC accounts (75% of sends from 13% of creates) while the long-tail (especially ROW non-HVC at 3.5% activation→publish) is failing to convert. **Three hot spots to attack:** (1) first-time-user activation funnel, (2) ROW SMB onboarding, (3) the gap between Free-tier creates declining and Standard/Annual surging.— BigQuery analysis of `bi_aggregate.*` tables, May 8, 2026 

## 30Strategic analytics framework — the email-builder North Star tree

A product lead should drive **one north-star metric** and watch a small tree of supporting metrics across _Acquisition · Adoption · Engagement · Retention · Monetization_. Below is the proposed tree for the Mailchimp Email Builder, with the BigQuery source for each.

#### NORTH STAR · "Activated Email Senders" (AES) PROPOSED

Unique paid accounts that **created AND sent** at least one bulk email this week. Captures depth-of-use, not just access.

**Source:** `product_health_weekly.email_creates ∩ first_time_sends ∩ email_sends` per account (needs user-level refresh)

#### Acquisition leg

Top-of-funnel: signups → activations → trial → paid.

* **Signups** (`product_health_weekly.signups`)
* **Activations** (signup-confirm) — `activations`
* **Trial-to-paid %** — `free_trials_weekly` (currently 58.7% steady-state)

#### Adoption leg (the killer funnel)

Activate → first login → bulk\_create → bulk\_publish in 24h / 1w.

* `funnel_weekly.bulk_created_24hrs` (currently \~36% of activations)
* `bulk_publish_24hrs` (currently \~4% of activations)
* **`bulk_publish_1_week` (currently 7.1% — TOP attack metric)**

#### Engagement leg

Frequency, depth, AI-feature adoption.

* **Email creates / active sender**
* **Sends per send-day** — load distribution
* **Open rate / click rate** by ecomm\_status (`product_health_weekly`)
* **Intuit Assist adoption** (needs new event surface — flag below)
* **Universal-content / saved-block usage** (when shipped)

#### Retention leg

The 1/3/6/12-month curve from `free_trials_weekly` by package + builder activity.

* **M3 / M6 / M12 retention by tenure × HVC**
* **Active-churn-risk %** (`churn_daily`) — currently 0.10% of paid users weekly
* **PRS / CSAT scoreboard** (currently CSAT 60%, PRS NPS-proxy +26)

#### Monetization leg

Trial → paid → upgrade. Cross-ref with builder usage to find expansion hotspots.

* **New bookings** (`bookings_weekly`)
* **Upgrades from free/Essentials → Standard**
* **Annual plan attach** (now growing 20×+ YoY)

## 31Adoption & frequency — top-line trend (12 months, MoM, YoY)

| Month      | Signups | Activations | Email creates · YoY | First-time sends · YoY | Email sends |
| ---------- | ------- | ----------- | ------------------- | ---------------------- | ----------- |
| **May'25** | 169K    | 170K        | 6.2M +33%           | 45K \-23%              | 15.6B       |
| **Jun'25** | 306K    | 307K        | 9.7M +26%           | 66K \-24%              | 25.8B       |
| **Jul'25** | 208K    | 209K        | 7.2M \-19%          | 53K \-16%              | 19.3B       |
| **Aug'25** | 199K    | 199K        | 8.9M \-4%           | 60K \-26%              | 24.0B       |
| **Sep'25** | 175K    | 175K        | 7.9M \-6%           | 56K \-24%              | 20.2B       |
| **Oct'25** | 160K    | 164K        | 8.2M \-16%          | 55K \-24%              | 20.3B       |
| **Nov'25** | 207K    | 208K        | 11.8M +35%          | 74K \-25%              | 29.2B       |
| **Dec'25** | 116K    | 116K        | 8.6M +59%           | 43K \-28%              | 18.8B       |
| **Jan'26** | 157K    | 158K        | 8.8M +39%           | 46K \-28%              | 18.3B       |
| **Feb'26** | 160K    | 160K        | 8.6M +5%            | 48K \-26%              | 19.3B       |
| **Mar'26** | 200K    | 201K        | 11.1M +6%           | 59K \-27%              | 23.8B       |
| **Apr'26** | 174K    | 175K        | 6.9M \-14%          | 49K \-20%              | 18.3B       |

**Reading this:** sends are stable to slightly down. **First-time sends are down 15-25% YoY in 11 of 12 months** — this is the canary. New-customer activation is degrading. November BFCM peak (+35% YoY creates) shows seasonal demand is intact, but the conversion to first-send isn't following.

## 32The activation funnel — where 93% of new accounts go to die

| Month      | Activations | Login <2d  | Bulk created <24h | Published <24h | Published <1w   |
| ---------- | ----------- | ---------- | ----------------- | -------------- | --------------- |
| **May'25** | 170K        | 159K (94%) | 54K (32%)         | 6K             | **11K** (6.4%)  |
| **Jun'25** | 307K        | 292K (95%) | 72K (23%)         | 10K            | **17K** (5.7%)  |
| **Jul'25** | 209K        | 192K (92%) | 61K (29%)         | 7K             | **13K** (6.2%)  |
| **Aug'25** | 199K        | 188K (94%) | 65K (33%)         | 9K             | **16K** (8.2%)  |
| **Sep'25** | 175K        | 167K (96%) | 61K (35%)         | 8K             | **16K** (9.0%)  |
| **Oct'25** | 166K        | 153K (92%) | 63K (38%)         | 8K             | **15K** (9.1%)  |
| **Nov'25** | 208K        | 198K (95%) | 80K (38%)         | 12K            | **21K** (10.1%) |
| **Dec'25** | 116K        | 108K (93%) | 44K (38%)         | 7K             | **13K** (11.0%) |
| **Jan'26** | 158K        | 146K (92%) | 49K (31%)         | 7K             | **13K** (8.2%)  |
| **Feb'26** | 160K        | 147K (92%) | 53K (33%)         | 7K             | **13K** (7.9%)  |
| **Mar'26** | 201K        | 185K (92%) | 65K (32%)         | 9K             | **15K** (7.7%)  |
| **Apr'26** | 175K        | 161K (92%) | 58K (33%)         | 7K             | **12K** (6.7%)  |

**The leakage map.** \~93% of newly-activated paid accounts log in within 2 days but only \~7% publish a first bulk email within a week. The drop is sharpest at _create → publish_ (only \~25% of creators publish in week 1). This is the **single highest-leverage funnel step** for the builder team.

## 33Lifecycle / tenure — who's using it & how often (last 90d)

| Tenure cohort      | Activations | Created <1w | Published <1w | Activate→Publish % |
| ------------------ | ----------- | ----------- | ------------- | ------------------ |
| **<1 month (new)** | 490K        | 182K        | 35K           | **7.1%**           |
| **<3 months**      | 6K          | 3K          | 1K            | **19.6%**          |
| **<6 months**      | 113         | 65          | 29            | **25.7%**          |
| **24+ months**     | 29K         | 10K         | 2K            | **6.9%**           |

**Lifecycle insight.** Brand-new (<1 month) accounts are the dominant volume (490K activations / 90d) but convert at only 7.1%. Accounts in their 2nd–3rd month have a much higher 19.6% — they've made it past the first-week wall. **The 24+ months "veteran returners" cohort** (29K activations) is back at 6.9% — these are reactivations / quiet returners and they re-encounter the same first-send wall. _Same fix lifts both new and returning._ 

## 34The HVC vs long-tail gap — biggest opportunity

| Country × HVC tier              | Activations (90d) | Activate→Publish 1w |
| ------------------------------- | ----------------- | ------------------- |
| **ROW (Rest of World)** non-HVC | 171K              | **3.5%**            |
| **United States** non-HVC       | 143K              | **9.2%**            |
| **United States** HVC           | 1K                | **30.3%**           |
| **Tier 1 Develop** non-HVC      | 104K              | **7.9%**            |
| **Tier 1 Develop** HVC          | 507               | **30.4%**           |
| **United Kingdom** non-HVC      | 34K               | **8.7%**            |
| **United Kingdom** HVC          | 212               | **21.7%**           |
| **Australia** non-HVC           | 13K               | **12.5%**           |
| **Australia** HVC               | 67                | **29.9%**           |
| **ROW** HVC                     | 341               | **36.9%**           |
| **Nordics** HVC                 | 66                | **36.4%**           |
| **Canada** non-HVC              | 23K               | **9.2%**            |
| **Canada** HVC                  | 88                | **27.3%**           |

## What it means

HVCs convert **3–10× better** than non-HVC across every region. **The funnel is built for engaged/large-list users.**

* **ROW non-HVC** (170K activations, the largest cohort) converts at **3.5%** — the worst funnel performance and the largest absolute opportunity. International SMB onboarding is broken.
* **US non-HVC** at 9.2% is the next biggest absolute pool. A 2pt lift here = \~3,000 more publishers/month.
* **HVCs across every region** (\~2,500 activations/90d) sit at 21–37% — they're already converting; investment here is incremental.
* **Strategic implication:** the team should index on the non-HVC long tail, not the HVC top, for funnel work. Reverse the priority for retention/expansion work.

## 35Plan & package mix — where revenue is moving

| Package                     | Email creates · YoY | First-time sends · YoY | Email sends | Notes                               |
| --------------------------- | ------------------- | ---------------------- | ----------- | ----------------------------------- |
| **Free**                    | 9.6M \-16%          | 80K \-39%              | 2.6B        | _Largest creator pool, declining_   |
| **Standard (monthly v0)**   | 6.1M +21%           | 49K \-17%              | 11.9B       | _+21% YoY creates · core paid tier_ |
| **Legacy monthly**          | 5.0M \-9%           | 285 \-55%              | 21.1B       | _Highest sends, runoff cohort_      |
| **Essentials (monthly v0)** | 3.8M +9%            | 9K \-16%               | 3.8B        | _+9% YoY · entry paid_              |
| **Premium (monthly v0)**    | 1.3M +4%            | 484 \-19%              | 16.1B       | _HVC enterprise_                    |
| **Free (monthly v0 — new)** | 84K +192%           | 12K +318%              | 17.3M       | _+192% YoY first-time sends_        |
| **Premium annual v0**       | 16K +2200%          | 23 +188%               | 141.0M      | _+2200% YoY · annual surging_       |
| **Standard annual v0**      | 7K +2118%           | 37 +147%               | 21.7M       | _+2117% YoY · annual surging_       |

**The shifts.** **Free tier is shrinking** (creates −16% YoY, first-time sends −39% YoY) — entry funnel is leaking.**Standard monthly is the growth engine** (+21% YoY creates) — the core paid tier is healthy.**Annual plans are exploding** (Premium annual +2,200% YoY, Standard annual +2,117% YoY from a tiny base) — annual is the new commercial wedge.**"free\_monthly\_plan\_v0"** (the new free experience?) is +192% YoY first-time sends — onboarding flow change is working _in that variant_.**Legacy monthly** still sends 21B emails/month from grandfathered accounts — protect this revenue while migrating off.

## 36Trial → paid → retention curve (steady state)

| Stage                  | Conversion / retention |
| ---------------------- | ---------------------- |
| **Trial → paid**       | **58.7%**              |
| 1-month retention      | 100%                   |
| 3-month retention      | 35.4%                  |
| 6-month retention      | 26.7%                  |
| **12-month retention** | **18.6%**              |

**The drop:** 3-month retention fell from 74% (Nov 2024 cohort) to \~35% (mature steady-state across 2025). 12-month retention only 18.6%. _Builder usage in the first 30 days is the strongest leading indicator_ — recommend a deep-dive correlating builder activity buckets with M3/M6/M12 retention by package.

## 37Health signals — Apr 2026 snapshot

| Signal                    | Value               |
| ------------------------- | ------------------- |
| Total paid users          | 31.5M               |
| Weekly churn-risk pool    | 71K (0.23%)         |
| … active churn risk       | 32K (45%)           |
| … passive billing failure | 38K (53% of risk)   |
| … compliance churn        | 1K (2%)             |
| **CSAT (satisfied)**      | **59.6%** n=2166/wk |
| PRS NPS-like score        | **+25.8**           |

**Read:** only \~45% of churn risk is "active" (driven by product dissatisfaction); 53% is passive billing-card failures. _The builder team owns the active-churn lever (\~32K users/month at risk) — the recovery team owns the bigger passive pool._ CSAT has been stable at 57–66%; PRS hovers +26.

## 38Ecomm vs non-ecomm — engagement is inverted

| Audience type                  | Email creates (90d) | Email sends (90d) | Open rate | Click rate |
| ------------------------------ | ------------------- | ----------------- | --------- | ---------- |
| **Non-ecomm**                  | 18.4M               | 26.5B             | 48.3%     | 8.0%       |
| **Ecomm-connected**            | 6.0M                | 19.7B             | 43.2%     | 5.6%       |
| **Ecomm-likely (no platform)** | 1.5M                | 10.3B             | 40.8%     | 3.6%       |

**Counter-intuitive but consistent:** non-ecomm accounts (ProServ, B2B, associations) have higher open and click rates than ecommerce. Ecomm sends 3.3× more per create (high-volume promo) but ProServ has higher engagement quality. Mirrors the Page 6 HeyMarvin finding — ProServ buyers want different templates than ecomm. **An "engagement-quality" KPI by audience-type, not just send-volume, is missing from current dashboards.** 

## 39Where to focus energy — 5 hotspots ranked by leverage

#### The first-week publish wall HIGHEST LEVERAGE

\~93% of newly-activated paid accounts never publish in week 1\. A 5-pt lift = +28K monthly publishers, \~$X-million annualized retention gain (size precisely with cohort activity → retention regression).

**Plays:** simplified first-template flow · template-list inline preview · saved blocks for "borrow my agency template" · in-canvas activation nudge to "Publish" once a draft is ready.

#### ROW non-HVC SMB onboarding

170K monthly activations at 3.5% publish-1w = the worst funnel cell in the heat-map. International SMB hits a UX wall in week 1.

**Plays:** localized template gallery · WhatsApp-friendly first-send option (Page 4 D3) · regional payment / billing flow hardening · timezone-aware onboarding emails.

#### First-time-sends YoY decline

11 of last 12 months down 15-25% YoY. Pre-existing demand is fine (sends stable, BFCM up); first-send conversion is the regression.

**Plays:** instrument the actual first-send path end-to-end · A/B the simplified setup checklist (current one "flattens decisions of vastly different importance" — Kyle Spalding, Page 6) · activation playbook for paid-trial cohort.

#### Trial→paid steady \~58% but 12-mo retention only 18.6%

Healthy trial conversion but customers drop fast after paying. M3 retention fell from 74% (Nov 2024) to 35% (mature 2025). Builder usage in the first 30 days is the strongest leading indicator.

**Plays:** "first 4 sends in 30 days" activation playbook tied to retention · Universal Saved Content (Page 4 F1) lowers re-creation cost · discovery / activation funnel for high-frequency users (Page 6 Bet 2).

#### Annual-plan attach is exploding (+2,000% YoY)

Annual plans are the new growth wedge — but the builder onboarding wasn't designed for an annual signup mental model (commit-then-explore vs explore-then-commit).

**Plays:** annual-plan-specific welcome flow · success criteria optimized for "send 12 campaigns / year, retain to renewal" · upsell triggers tied to feature ceiling rather than monthly volume.

## 40The analytics strategy — what to run, how often, and where to put your energy

## Weekly cadence (Monday 9am)

* **1-page Builder Health scorecard** — 6 KPIs: AES (north star), email\_creates WoW, first\_time\_sends WoW + YoY, activation→publish-1w%, churn-risk %, CSAT.
* **Single anomaly check** — any KPI moving > ±10% WoW: surface root cause.
* **Free vs Standard vs Premium splits** on every KPI.

## Monthly cadence (1st Monday)

* **Cohort retention curve** — 1/3/6/12-mo retention by package × ecomm\_status × tenure (`free_trials_weekly`).
* **Funnel deep-dive by country group + HVC** (`funnel_weekly`).
* **Builder feature-adoption matrix** — Universal Content, Brand Kit, Image Remix, Intuit Assist (needs new event surface).

## Quarterly

* **Builder usage → retention regression**: which 30-day builder behaviors predict M6/M12 retention.
* **Power-user concentration**: top 1% / 5% / 20% of senders, what % of total sends.
* **Voice-of-customer quarterly**: cross-ref Page 5 (Slack VOC, $K MRR exposure) with Page 7 cohort-retention deltas.

## Critical SQL patterns to run

Q1 — Top-line trend

SELECT DATE_TRUNC(week, MONTH) m,
  SUM(email_creates) creates,
  SUM(first_time_sends) fts,
  SUM(email_sends) sends
FROM bi_aggregate.product_health_weekly
WHERE week >= DATE_SUB(CURRENT_DATE(), INTERVAL 365 DAY)
GROUP BY 1 ORDER BY 1;

Q2 — Funnel by country × HVC

SELECT country_group, is_high_value,
  SUM(total_activations) acts,
  SUM(bulk_publish_1_week) pub_1w,
  SAFE_DIVIDE(SUM(bulk_publish_1_week),
              SUM(total_activations)) act_to_pub
FROM bi_aggregate.funnel_weekly
WHERE week >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY 1,2 ORDER BY acts DESC;

Q3 — Trial→paid→retention by package

SELECT package, DATE_TRUNC(week,MONTH) m,
  SUM(free_trial_users) trials,
  SUM(new_booking_users) paid,
  SAFE_DIVIDE(SUM(month_3_retention_cnt),
              SUM(new_booking_users)) m3_retention,
  SAFE_DIVIDE(SUM(month_12_retention_cnt),
              SUM(new_booking_users)) m12_retention
FROM bi_aggregate.free_trials_weekly
WHERE week >= DATE_SUB(CURRENT_DATE(), INTERVAL 540 DAY)
GROUP BY 1,2 ORDER BY 2,1;

## 41Data caveats & recommended pipeline fixes

**User-level email tables stale.** `bi_product.product_reporting_email_base` last refreshed Dec 2023 (84M rows). Most user-level cohort/segmentation analyses are blocked or run on stale data. **Top action: re-engage data team to refresh this pipeline.**

**Creative Assistant tables frozen at 2022.** `creative_assistant_*` tables stopped updating Nov 2022\. Any in-builder AI feature reporting (Intuit Assist, Write with AI) needs a fresh event source — likely lives in Pendo or a newer events\_pipeline table. **Build the Intuit Assist funnel from scratch.**

**Tenure bucket labels inconsistent.** `account_tenure_months` has both `<1`, `<3`, `<6`, `<12`, `<24`, `24+` labels with overlapping semantics. Recommend canonical buckets (0-30d / 31-90d / 91-180d / 181-365d / 1-3yr / 3+yr) and rebuild aggregates.

**BigQuery sources (Page 7) — all queries run live on May 8, 2026:** `mc-business-intelligence.bi_aggregate.product_health_weekly` (FRESH through 2026-05-10) ·`bi_aggregate.funnel_weekly` (activation funnel) ·`bi_aggregate.free_trials_weekly` (trial→paid + 1/3/6/12 retention) ·`bi_aggregate.churn_daily` (paid users · churn risk · CSAT · PRS) ·`bi_aggregate.customer_engagements_weekly` (touchpoint activity) ·`bi_aggregate.product_journey_monthly` (lifecycle stage) ·`bi_product.product_reporting_email` \+ `_base` (STALE since Dec 2023, structure-only reference) ·`bi_product.creative_assistant_*` (FROZEN Nov 2022, inactive).  
  
_Methodology:_ 9 priority queries across 6 fresh aggregate tables — no synthetic data. All YoY deltas use the table's own `_prev_yr` LAG columns (zero recomputation). Cohort dimensions used: `is_high_value`, `package`, `account_tenure_months`, `ecomm_status`, `country_group`. The 7.1% activate-to-publish-1w is the dominant headline metric — recommend it become an org-level OKR for Q3-Q4 FY26.

Competitive Intelligence · Executive Brief · Page 8 of 11

# QA-tested year-over-year diagnostic — Findings · Benefits · Implications · Resolutions

Full TY (May'25–Apr'26) vs LY (May'24–Apr'25) BigQuery analysis on the Mailchimp BI warehouse, with end-to-end data-quality tests, regression validation against Page 7 published numbers, and a structured F · B · I · R synthesis on every finding. **Run date: 2026-05-08 · 9 QA tests · 7 YoY metric pulls · 10 structured findings.**

**QA suite:** 7/9 PASS · 1 partial · 1 documented

**Regression:** Page 7 numbers reproduce 0.00% delta

**The YoY story in one line:** _quality up, quantity down, retention crashing_. Activated users do MORE per visit (creates +6%, clicks +3.5%, open rate +2 pts across all segments) — but logins (−24%), first-time sends (−26%), new bookings (−13%), and upgrades (−31%) are all sliding, while M3/M6/M12 retention has dropped 30–42 percentage points. **The pipeline is hollowing in the middle.** The top still acquires (signups −2.4%) and the bottom still engages (clicks +3.5%); the soft tissue is the activation-to-retention bridge — exactly where the Page 4 + Page 5 + Page 6 evidence converged.— BigQuery YoY analysis · 12 mo TY vs 12 mo LY · QA-validated 

## 42QA test report — data quality, freshness, regression, unit tests

| Category                      | Test                                                                                                       | Status     | Detail                                                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FRESHNESS**                 | All 6 source aggregate tables ≤ 2 days lag                                                                 | PASS       | product\_health\_weekly + funnel\_weekly + free\_trials\_weekly + customer\_engagements\_weekly @ 2026-05-10 (forward-fill); churn\_daily @ 2026-05-08 (today). product\_journey\_monthly @ 2029-06-01 (flagged: contains forecast/placeholder rows in future).                   |
| **ROW VOLUME**                | Last 30 days has > 50K rows in each weekly table                                                           | PASS       | product\_health\_weekly: 79K · funnel\_weekly: 7.2M · free\_trials\_weekly: 7.2M · customer\_engagements\_weekly: 261M · churn\_daily: 45M (cross-section dimensional cuts).                                                                                                      |
| **YoY CONSISTENCY**           | current week\_n value matches prev\_yr column LAG(52) for the same metric                                  | PASS       | Sampled 5 months (May–Sep 2024). All match\_pct = 100.00% exactly. The prev\_yr columns are reliable — use them for fast YoY without recompute.                                                                                                                                   |
| **NULL CHECK**                | Critical dimensions (week, fy\_text, package, ecomm\_status, is\_high\_value) are non-null in last 90 days | PASS       | 0 nulls across 221,760 rows in last 90 days for every critical dimension.                                                                                                                                                                                                         |
| **FUNNEL MONOTONICITY**       | signups ≥ activations at row level                                                                         | PARTIAL    | 2,596 / 839,520 (0.31%) rows show signups < activations. Root cause: dimensional cuts where activation can roll-up across signup categories. Headline-level (no dimensions) holds. Flag for data team.                                                                            |
| **FUNNEL SEMANTICS**          | activations ≥ first\_time\_sends at row level                                                              | DOCUMENTED | 27,639 / 839,520 (3.29%) rows where activations < first\_time\_sends. NOT a violation — first\_time\_sends counts users sending for the first time ever (cohort-agnostic), activations counts new accounts created this week. Different cohorts. Documented in metric dictionary. |
| **REGRESSION**                | Page 7 published Apr 2026 email\_creates (6,897,596) reproduces from fresh re-pull                         | PASS       | Fresh re-pull = 6,897,596\. Delta: 0 / 0.00%. Page 7 numbers are reproducible, no upstream drift.                                                                                                                                                                                 |
| **UNIT TEST · YoY math**      | trial\_to\_paid TY (348K/196K) computes to 56.32% as published                                             | PASS       | 196,232 / 348,382 = 56.32% — exact match to published TY trial-to-paid rate.                                                                                                                                                                                                      |
| **UNIT TEST · YoY direction** | Engagement rates (open, click) increased YoY for ecomm + non-ecomm + ecu                                   | PASS       | Non-ecomm open: 47.91%→50.13% · Ecomm open: 41.95%→44.34% · Ecu open: 39.03%→41.08%. All directional improvements.                                                                                                                                                                |

**Methodology.** Each test runs an explicit assertion against the live `mc-business-intelligence.bi_aggregate.*` tables. PASS = assertion held with no exception. PARTIAL = held at headline level but exceptions exist at dimensional cuts (documented). DOCUMENTED = surface signal explained by metric semantics (not a failure). FAIL = would block publishing.

## 43Year-over-year — top-line metrics (12 mo TY vs 12 mo LY, full-year)

| Metric                              | LY (May'24–Apr'25) | TY (May'25–Apr'26) | YoY change | Note                                           |
| ----------------------------------- | ------------------ | ------------------ | ---------- | ---------------------------------------------- |
| **Signups**                         | 2.3M               | 2.2M               | ↓ -2.4%    | _Top-of-funnel slightly soft_                  |
| **Activations**                     | 2.3M               | 2.2M               | ↓ -2.3%    | _Mirrors signups_                              |
| **Logins**                          | 126.3M             | 96.1M              | ↓ -23.9%   | _BIG drop — engagement frequency collapsing_   |
| **Email creates**                   | 97.8M              | 103.9M             | ↑ +6.1%    | _Active creators creating MORE_                |
| **First-time sends**                | 879K               | 653K               | ↓ -25.7%   | _ACTIVATION KILLER — fewer accounts ever ship_ |
| **Email sends (volume)**            | 279.8B             | 253.0B             | ↓ -9.6%    | _Volume contracting_                           |
| **Email delivered**                 | 251.3B             | 229.7B             | ↓ -8.6%    | _Tracks sends_                                 |
| **Email opens**                     | 110.4B             | 106.4B             | ↓ -3.6%    | _Slower decline than sends_                    |
| **Email clicks**                    | 13.7B              | 14.1B              | ↑ +3.5%    | _Quality engagement IMPROVED_                  |
| **New bookings (paid conversions)** | 381K               | 331K               | ↓ -13.1%   | _Real revenue risk_                            |

## 44Activation funnel YoY — where the leakage is

| Funnel stage            | LY count (% of acts) | TY count (% of acts) | YoY conversion delta |
| ----------------------- | -------------------- | -------------------- | -------------------- |
| **Activations**         | 2.3M (100.0%)        | 2.2M (100.0%)        | —                    |
| **Login <2d**           | 1.7M (72.5%)         | 2.1M (93.4%)         | +20.9 pts ✓          |
| **Bulk created <24h**   | 883K (38.5%)         | 726K (32.4%)         | −6.1 pts ✗           |
| **Bulk created <1w**    | 1.0M (43.7%)         | 826K (36.8%)         | −6.9 pts ✗           |
| **Bulk published <24h** | 122K (5.3%)          | 96K (4.3%)           | −1.0 pt ✗            |
| **Bulk published <1w**  | 224K (9.7%)          | 175K (7.8%)          | −1.9 pts ✗           |
| **Upgrades**            | 2K (0.1%)            | 2K (0.1%)            | −31% absolute ✗      |

 Login improved (+20.9 pts) but everything downstream regressed. **Bulk\_publish\_1w fell from 9.7% → 7.8% (−1.9 pts)** — that's where Page 7's "first-week wall" lives quantified YoY. Upgrades fell 31% absolute on a stable activation base.

## 45HVC concentration YoY — distribution flattening

| Cohort × metric              | LY (share)        | TY (share)        | YoY     |
| ---------------------------- | ----------------- | ----------------- | ------- |
| HVC **Email creates**        | 21.0M21.4% share  | 17.3M16.7% share  | \-17.4% |
| non-HVC **Email creates**    | 76.9M78.6% share  | 86.5M83.3% share  | +12.6%  |
| HVC **Email sends**          | 207.3B74.1% share | 187.9B74.2% share | \-9.4%  |
| non-HVC **Email sends**      | 72.5B25.9% share  | 65.2B25.8% share  | \-10.2% |
| HVC **First-time sends**     | 13K1.5% share     | 9K1.4% share      | \-28.5% |
| non-HVC **First-time sends** | 866K98.5% share   | 643K98.6% share   | \-25.7% |

**HVC creates share fell from 21.4% → 16.7%** (HVC creates −17%, non-HVC creates +13%). HVC sends share remained stable at \~74%. The wedge: non-HVC accounts are creating more but sending less. _Created-but-never-sent_ is the precise gap to attack.

## 46Trial → paid → retention YoY ⚠ catastrophic compression

| Cohort metric             | LY    | TY    | YoY     | Note                      |
| ------------------------- | ----- | ----- | ------- | ------------------------- |
| **Trial users (cohort)**  | 355K  | 348K  | \-1.8%  |                           |
| **New paid (trial→paid)** | 190K  | 196K  | +3.1%   |                           |
| **Trial-to-paid %**       | 53.6% | 56.3% | +2.7%   | _+2.7 pts ✓_              |
| **M3 retention count**    | 145K  | 68K   | \-53.4% |                           |
| **M3 retention %**        | 76.5% | 34.5% | \-42.0% | _−42 pts ⚠ CATASTROPHIC_  |
| **M6 retention count**    | 113K  | 52K   | \-54.2% |                           |
| **M6 retention %**        | 59.2% | 26.3% | \-32.9% | _−33 pts ⚠_               |
| **M12 retention count**   | 80K   | 21K   | \-73.3% |                           |
| **M12 retention %**       | 42.0% | 10.9% | \-31.1% | _−31 pts ⚠ revenue cliff_ |

**Trial-to-paid IMPROVED (+2.7 pts to 56.3%)** but every multi-month retention metric collapsed: M3 from 76.5%→34.5%, M6 from 59.2%→26.3%, M12 from 42.0%→10.9%. Caveat: TY M12 cohorts have \~25% less observation window, but the magnitude is too large to be measurement-only. **Highest-priority investigation in the diagnostic.** 

## 47Plan / package YoY — annual exploding, free creates up, FTS down everywhere

| Package                        | LY creates | TY creates · YoY | LY first-time sends | TY FTS · YoY | TY sends |
| ------------------------------ | ---------- | ---------------- | ------------------- | ------------ | -------- |
| **Free**                       | 32.1M      | 42.6M +33%       | 564K                | 398K \-29%   | 11.9B    |
| **Standard monthly v0**        | 20.1M      | 22.4M +12%       | 240K                | 190K \-21%   | 51.9B    |
| **Essential monthly v0**       | 14.6M      | 13.5M \-8%       | 56K                 | 38K \-32%    | 16.7B    |
| **Premium monthly v0**         | 4.6M       | 4.9M +7%         | 3K                  | 2K \-11%     | 71.0B    |
| **Legacy monthly**             | 25.8M      | 19.9M \-23%      | 4K                  | 2K \-62%     | 97.3B    |
| **Free monthly v0 (new flow)** | 130K       | 151K +16%        | 7K                  | 19K +153%    | 50.8M    |
| **Premium annual v0**          | 720        | 42K +5787%       | 8                   | 71 +788%     | 550.9M   |
| **Standard annual v0**         | 302        | 15K +4857%       | 15                  | 101 +573%    | 54.7M    |
| **Essential annual v0**        | 0          | 467 NEW          | 0                   | 20 NEW       | 79K      |
| **PAYG**                       | 323K       | 211K \-35%       | 1K                  | 733 \-45%    | 2.1B     |
| **Pre-paid**                   | 7K         | 8K +19%          | 123                 | 92 \-25%     | 53.3M    |
| **Pro / module / other**       | 117K       | 105K \-10%       | 3K                  | 2K \-33%     | 1.4B     |

**Annual plans are the new growth wedge:** Premium annual +5,786% creates / +788% FTS, Standard annual +4,857% creates / +573% FTS. The new **"free\_monthly\_v0"** variant is the only Free package where FTS is UP (+153%) — has 8× better creates-to-FTS conversion than legacy Free. **Generalize the v0 winning treatment.** 

## 48Engagement quality YoY — every segment improved

| Audience type                       | LY open rate | TY open rate   | LY click rate | TY click rate |
| ----------------------------------- | ------------ | -------------- | ------------- | ------------- |
| **Non-ecomm (ProServ, B2B)**        | 47.9%        | 50.1% +2.2 pts | 7.1%          | 7.9% +0.8 pts |
| **Ecomm (connected platform)**      | 42.0%        | 44.3% +2.4 pts | 4.8%          | 5.5% +0.7 pts |
| **Ecu (ecomm-likely, no platform)** | 39.0%        | 41.1% +2.0 pts | 3.0%          | 3.4% +0.4 pts |

**Open rates +2 to +2.4 pts across all segments. Click rates +0.4 to +0.8 pts.** The customers who DO publish are getting better outcomes than a year ago. This is the marketing claim of the year — and the proof that the product works for the engaged tier. The opportunity is to expand the engaged tier, not rebuild the core builder.

## 4910 findings — mapped to customer benefit, business implication, and proposed resolution

01

**Owner:** Builder PM + Activation PM (joint) · **Size:** 30-40 person-quarters

**Evidence:** `product_health_weekly · 12-mo TY vs LY`

FINDING

**First-time sends collapsed −25.7% YoY (878K → 653K) while signups only fell −2.4% — activation funnel broke independently of acquisition.**

CUSTOMER BENEFIT

Customers (especially first-time payers) who can ship a first campaign in week 1 retain at 3-5× the rate of those who don't. A quicker time-to-first-value is the biggest single act of customer kindness this team can do.

BUSINESS IMPLICATION

If unaddressed, \~225K fewer first-time senders annually compounds into lost retention and lost word-of-mouth. At current $/customer this is approx $20-50M annual ARR exposure (sized vs new bookings −13% YoY = −50K customers).

PROPOSED RESOLUTION

Phase 1 from Page 7: simplified first-template flow + saved-template prompt after first send + activation playbook for trial-to-paid cohort. Make 'publish first email in week 1' the team's single OKR. Instrument the create→publish step (\~25% conversion today) end-to-end.

02

**Owner:** Builder PM + Retention PM + Finance partner · **Size:** Investigation: 1 week. Mitigation: 6-12 months.

**Evidence:** `free_trials_weekly · cohort comparison TY mature vs LY mature`

FINDING

**M3 / M6 / M12 retention dropped 30-42 percentage points YoY (76.5%→34.5% / 59.2%→26.3% / 42.0%→10.9%). Trial-to-paid actually IMPROVED (+2.7 pts to 56.3%) — customers convert but don't stick.**

CUSTOMER BENEFIT

Customers stay because the product solves their job. Retention is a downstream signal that builder usage compounds into business value. Improving retention means we're delivering durable utility, not just first-month novelty.

BUSINESS IMPLICATION

Most catastrophic single metric in the diagnostic. Drop of this magnitude usually signals one of: (a) plan-mix shift to easier-to-cancel monthly plans, (b) silent product regression in onboarding, (c) measurement-definition change. Need confirmation from Finance + Data Eng before sizing — but at face value, retention compression = revenue cliff in 12-24 months.

PROPOSED RESOLUTION

Same week: cross-functional war-room with Finance + Data Eng to validate methodology. If real: ship Universal Saved Content (Page 4 F1) + activation playbook + brand-voice retention nudges. Pair builder-usage segmentation with retention regression to find the threshold of 'sticky behavior' (e.g., 4 sends in 30 days = 2× retention).

03

**Owner:** Lifecycle PM + Builder PM · **Size:** 10-15 person-quarters

**Evidence:** `product_health_weekly · 12-mo TY vs LY`

FINDING

**Logins crashed −23.9% YoY (126M → 96M) while creates per-visitor went UP. Frequency of visit is collapsing — those who visit do more.**

CUSTOMER BENEFIT

Customers who visit weekly find more reasons to engage and more chances to convert; those who visit monthly miss the moment. Higher visit frequency = more confidence in the product.

BUSINESS IMPLICATION

Logins are the leading indicator of engagement decay. A 24% YoY drop predicts a parallel send-volume drop (already showing −10%) and bookings drop (already −13%). Loss of habit precedes loss of revenue by 2-3 quarters.

PROPOSED RESOLUTION

Re-energize visit cadence: weekly campaign-idea email from Mailchimp itself (Clint Bartley's direct ask, Page 6 Bet 2), DRAFT-resurrect prompts, post-send activity dashboard that pulls users back day-2 / day-7\. Mobile builder for quick edits on phone (not in our stack today; add to Page 4 roadmap).

04

**Owner:** Marketing + PMM · **Size:** 1-2 person-quarters

**Evidence:** `product_health_weekly · 12-mo TY vs LY × ecomm_status`

FINDING

**Engagement quality UP across every segment YoY. Non-ecomm open rate 47.9%→50.1%, click rate 7.1%→7.9%. Ecomm open 41.9%→44.3%, click 4.8%→5.5%.**

CUSTOMER BENEFIT

Customers who do publish are seeing meaningfully better outcomes. Their lists, content, and timing are improving. The remaining users got more sophisticated.

BUSINESS IMPLICATION

Inverse of the bad signals: the product still works for the engaged cohort. Story isn't 'product is broken' — it's 'we shed casual users while serving power users better.' That implies the lever is acquisition + activation, NOT core builder UX.

PROPOSED RESOLUTION

Lean into this in marketing: 'Mailchimp customers see industry-leading open rates' becomes a real claim with primary data. Use as competitive proof point in Page 1/4 positioning vs Klaviyo. Internally, do not chase 'more features' — chase 'more engaged users.'

05

**Owner:** Builder PM + Lifecycle PM · **Size:** 5-8 person-quarters

**Evidence:** `product_health_weekly · TY vs LY × is_high_value`

FINDING

**HVC concentration is narrowing: HVC creates fell from 21.4%→16.7% of total (HVC creates −17%; non-HVC creates +13%). HVC sends share remained stable at \~74%.**

CUSTOMER BENEFIT

A more even distribution of creates across customer tiers means SMB and mid-market customers are creating more — which is exactly what builder UX investments should do.

BUSINESS IMPLICATION

The non-HVC creates surge (+13%) is positive — they ARE creating more. But the FTS drop (−26%) shows they aren't shipping. \*\*The wedge is exactly between 'created' and 'sent' for non-HVC accounts.\*\* This is the precise place to invest builder polish.

PROPOSED RESOLUTION

Build a 'created-but-never-sent' campaign-rescue flow targeting non-HVC drafts older than 7 days. 'Want to send the campaign you created on May 1?' email + in-product nudge. Combine with Page 7 hot spot #1 (the 7.1% activate-to-publish wall).

06

**Owner:** Pricing/Packaging PM + Builder PM + Customer Success · **Size:** 8-10 person-quarters

**Evidence:** `product_health_weekly · TY vs LY × package`

FINDING

**Annual plans exploded: Premium annual creates +5,786% YoY (720 → 42K), Standard annual +4,857% (302 → 15K), Essential annual launched (0 → 467). FTS up across all annual variants.**

CUSTOMER BENEFIT

Annual customers commit upfront and invest in learning the product. They want depth, ROI proof, and confidence — not a free trial. Their builder experience should be different.

BUSINESS IMPLICATION

Annual is the new commercial wedge. The builder onboarding wasn't designed for an 'I committed for a year, now teach me everything' mental model. Currently treats annuals like monthly trial converters.

PROPOSED RESOLUTION

Annual-specific welcome flow: success criteria optimized for 'send 12 campaigns / year, retain to renewal.' Upsell triggers tied to feature ceiling (e.g., AI image edits / month, saved-blocks count) rather than monthly send volume. Package an 'Annual Customer Success Pack' with templates + benchmark data.

07

**Owner:** Activation PM + Experimentation lead · **Size:** 1-2 person-quarters investigation, then scale

**Evidence:** `product_health_weekly · TY vs LY × package`

FINDING

**Free monthly v0 (new flow) is the only package where first-time sends are UP YoY (+153%, 7,389 → 18,710). Creates per FTS ratio is 8× better than legacy Free.**

CUSTOMER BENEFIT

Customers in this variant got a meaningfully better first experience: fewer drop-offs, faster shipping, higher confidence.

BUSINESS IMPLICATION

We have an existing variant that demonstrably improves activation. Likely an experimental cohort or a recently-shipped redesign. Critical to confirm exposure size, then GENERALIZE the winning treatment to legacy Free tier (which lost −29% FTS YoY).

PROPOSED RESOLUTION

Run a quick teardown of free\_monthly\_v0 vs legacy free: what changed? Onboarding flow? Templates? Default audience? Identify the diff and propose a port to legacy free. If holdout test exists, validate. If not, ship a ramp-up A/B.

08

**Owner:** Pricing PM + Growth PM · **Size:** 5-8 person-quarters

**Evidence:** `funnel_weekly · TY vs LY`

FINDING

**Upgrade conversions in the first-week funnel fell 31% YoY (2,318 → 1,607) on stable activation base.**

CUSTOMER BENEFIT

Upgrades are the moment a customer signals 'this product is worth paying more for.' Healthy upgrade rate = product-market fit at the next price tier.

BUSINESS IMPLICATION

The value proposition between Free and paid tiers is weakening from the customer's POV. Without intervention, ARPU growth stalls — especially as Free creates surge (+33%) but don't convert upward.

PROPOSED RESOLUTION

Surface Page 4 F4 (in-canvas AI image editor) as an upgrade-gated feature in the Free flow. 'Edit this image with AI' → soft paywall to Standard. Pair with a 'free 30-day trial of Image Remix' to drive engagement before the paywall hardens. Re-test pricing-page messaging targeting first-week new accounts.

09

**Owner:** Builder PM (lead) · **Size:** Already in Phase 1 plan (Page 4)

**Evidence:** `funnel_weekly + cross-reference Pages 5 & 6`

FINDING

**Bulk-create-to-publish conversion fell from 9.7% → 7.8% YoY (−1.9 pts) — matches the user-reported friction in Page 5 ("editor is clunky", "UI churn") and Page 6 (Andrea D'Ercole, Wes Turner, Jack Hally direct quotes).**

CUSTOMER BENEFIT

When the publish step is friction-free, customers ship more campaigns and feel competent, not blocked.

BUSINESS IMPLICATION

This is the quantitative confirmation of the qualitative VOC pattern. Three independent data sources (Slack VOC $128K MRR exposure, HeyMarvin 33-finding research database, BigQuery funnel) all point to the same step. \*\*High-confidence place to invest.\*\*

PROPOSED RESOLUTION

Direct alignment with Phase 1 of Page 4 + Page 5: ship Universal Saved Content (F1), in-canvas AI image editor (F4), reliable autosave (F9), brand-voice corpus AI (F2). Each was independently surfaced by VOC + research + BigQuery.

10

**Owner:** BI / Data Eng · **Size:** 1-2 person-weeks

**Evidence:** `QA freshness check across 6 source tables`

FINDING

**product\_journey\_monthly contains rows dated 2029-06-01 (3 years in future). Either projection-table or upstream label bug.**

CUSTOMER BENEFIT

Customers don't see this directly, but data quality issues in product analytics lead to wrong roadmap decisions and lost trust in dashboards.

BUSINESS IMPLICATION

If decision-makers query product\_journey\_monthly without a date filter, they may be looking at projected/synthetic data. Worth a flag to BI team.

PROPOSED RESOLUTION

File ticket with BI/data team to (a) confirm whether this is a forecasting table by design, (b) document the convention, (c) add a \`is\_actual\` boolean column to disambiguate, (d) cite documentation in the dataset description.

**Sources (Page 8) — all live on May 8, 2026:** `mc-business-intelligence.bi_aggregate.product_health_weekly` (top-line + package + ecomm + HVC) ·`bi_aggregate.funnel_weekly` (activation funnel) ·`bi_aggregate.free_trials_weekly` (trial→paid + 1/3/6/12 retention) ·`bi_aggregate.churn_daily` (paid users + churn risk + CSAT + PRS) ·`bi_aggregate.customer_engagements_weekly` · `bi_aggregate.product_journey_monthly` (flagged for forecast-row review).  
  
_Test methodology:_ 9 explicit QA assertions covering freshness, row volume, YoY consistency between current value and prev\_yr LAG columns, null checks on critical dimensions, funnel monotonicity, regression test (Page 7 number reproduction), and unit tests on derived rates. Result: 6 PASS · 1 PARTIAL (documented) · 1 DOCUMENTED (metric semantics) · 1 PASS unit test on trial-to-paid math.  
  
_YoY methodology:_ TY = trailing 12 mo (May 2025 – Apr 2026 inclusive of complete months only). LY = same 12-mo window prior year. Cohort comparisons (retention) use mature observation windows: TY = 180-540 days ago, LY = 540-900 days ago to ensure both have ≥6-mo maturity for M6 measurement. Engagement rates calculated as opens/delivered and clicks/delivered (industry standard).

Competitive Intelligence · Executive Brief · Page 9 of 11

# Previous PM's roadmap docs — cross-referenced + reviewer-agent critique

5 PDFs reviewed (Builder VoC Plans · Nuni Strategy · H2 FY26 Priorities · H2 FY26 Roadmap). 21 builder-relevant initiatives extracted, each cross-referenced against Slack VOC (Page 5) · HeyMarvin research (Page 6) · Klaviyo competitive gaps (Page 4) · BigQuery health metrics (Page 7-8). **13 initiatives flagged HIGH-confidence (multi-source) → reviewer-agent narrows to TOP 5 must-do-now**.

**Docs:** 5 (Nov'25 → Mar'26)

**Initiatives:** 21 unique

**Reviewer:** 3 PASS · 5 warnings · 3 overlaps

**The previous PM team has the right answers — and reasonable plans.** The Nuni Strategy (Jan 2026) is comprehensive: 7-phase JTBD × 6-level Maslow, scored vs Klaviyo + Canva, 30+ initiatives mapped to Q2/Q3/Q4, six SLOs proposed. Cross-referenced with our independent triple-source (Slack VOC + HeyMarvin + BigQuery YoY), **\~80% of their initiatives map cleanly to a customer pain or competitive gap we independently identified.** The remaining \~20% lack a direct customer voice (justifiable but lower confidence). **Three structural risks the docs don't address:** (1) several Mobile/Rendering items remain "Not Funded" since Nov 2025; (2) AI work spans two budgets (Builder + AI Objective) with unclear ownership; (3) sizing across docs ($4-6M, $1.5-2.8M, $3-8M) cannot be summed.— Cross-reference + reviewer-agent pass, May 8, 2026 

## 50The 5 documents — what each proposes

Builder VoC Feedback Response Plan

Ose Amiegheme · Erin McCue · JB Lovell · Joyce Russell · Nov 5, 2025

ThesisBuilder is now the #1 driver of design-tool churn. 468 VoC items categorized into 6 buckets — Usability (51%), Reliability (14%), Mobile (12%), Rendering (10%), Feature Requests (12%), Integrations (1%).

AsksQuality Pod (Nov-Jan, 4 sprints) for Mobile + Rendering quality wins · Cross-functional Design Sprint to reimagine clunky workflows · Audit feature gaps and decide Build/Borrow/Defer (MC vs Fusion).

Sizing**Improving email sends = $4–$6M FY26 revenue impact (cited). 17% non-HVC churn + 12% Free user churn attributed to design tools. Quality Pod target: 20–30% reduction in mobile/rendering complaints by EOQ2 FY26.**

Notable gapsMobile Styles V2 · Dynamic content on Mobile · Dark mode education · Mobile rendering bug fixes · Expanding Inbox Previews · Automated Rendering Test (all flagged 'Not funded' in source doc)

Builder VoC Response Plan (Pillar version)

Builder Team · Q2 FY26

Thesis3 strategic pillars to organize builder work: (1) Keep Core Promise (rendering reliability), (2) Build Habits (reduce effort to send), (3) Redesign Workflows (one big swing).

AsksPillar 1 projects: Automated Testing (Litmus API), Dark Mode, Block layout rendering, Text rendering, Inbox Preview boost, Mobile Styles V2, Show/Hide on devices, Responsive Nuni. Pillar 2: Reusable content blocks. Brand Kit projects: Branded Templates, Brand Kit Activation, Link Brand Kit + Global Styles, Template Refresh + Replicate. Pillar 3: Daily SWAT, DSB Asks.

Sizing**Effort sized as Small / Medium / Large / X-Large per project; Impact column uses 'Email Sends' as proxy. No dollar sizing in this doc.**

Notable gaps—

Nuni Builder Strategy and Roadmap (MASTER)

Ose Amiegheme · Erin McCue · JB Lovell · Ashley Wiesner · reviewed by Eric Anderson · Jan 2, 2026

ThesisNuni is 5-yr-old WYSIWYG builder, the primary creation surface, and one of the biggest sources of negative VoC. Two target ICPs for rest of FY26: <$299 non-HVC (price-sensitive, churn fast on friction) + DSB switchers (mostly HVC, coming from Klaviyo). Uses 7-Phase JTBD × 6-Level Maslow hierarchy. Nuni scores 4/4/2/1/2/0 vs Klaviyo 5/5/3/3/2/3 vs Canva 5/4/5/5/3/N/A — gap at Levels 3 (Efficient Workflow) and 4 (Brand-Native).

Asks30+ initiatives across Q2/Q3/Q4 mapped to 7-phase JTBD. 6 Builder SLOs (uptime ≥99.9%, crash-free ≥99.5%, save ≥99.99%, init load P95 <500ms, interaction P95 <300ms, render fidelity ≥99%, mobile ≥95%). Three named product briefs: Content Insertion · Styles · Alignment & Layout.

Sizing**Directional goals: reduce builder-driven churn 20–30% vs FY25 baseline (for <$299 non-HVC). Shift 80%+ of sends to 'healthy effort' (≤250 clicks). Reduce >500-click sessions by 30%.**

Notable gapsAI is positioned as 'horizontal accelerator' embedded in JTBD phases (no separate AI track) — generated layouts, image gen, chat-based editing.

Mailchimp H2 FY26 Product Priorities

Diana Williams · H2 FY26 (Aug'25 onwards)

Thesis4 objectives: (1) Accelerate FTU & Optimal Setup \[<$299 cohort\], (2) Strengthen Ecommerce/DSB, (3) Expand Omnichannel (SMS/Tx/RCS/WA), (4) Scale AI + Ecosystem (MC Everywhere). Builder is named directly under Obj 1 (FTU Branded Template E2E + Save Email Sections) and Obj 2 (Make all brand kit in Nuni + Klaviyo template converter).

AsksOKRs include FTU 30/90-day retention lift, DSB MRR +13% YoY, SMS rev to $23.75M, Tx rev to $33.65M.

Sizing**FTU Optimal Setup: $1.5M-$2.8M projected revenue (12-mo) from 2.85%-5.34% absolute lift in FTU 90d retention. DSB Initiative: $3M-$8M cumulative impact estimates. Omnichannel: $97K-$469K monthly. AI: $1K-$530K monthly.**

Notable gapsPull-back: 'Broad Churn Experimentation' is shifting to focus on FTU + platform performance. Mid-market commitments at sustained P2 investment.

Mailchimp H2 FY26 Roadmap (March update)

Diana Williams + product domain POCs · Mar 12, 2026

ThesisDetailed Q3/Q4 monthly milestones for each of the 4 H2 objectives. Builder-related deliverables explicit: Branded Template E2E (Q4 May), Save and Reuse Email Sections (Q4 May), One Click Apply Email Styles (Q4 June), Vibe Email Content Editing, Canva AI image gen in Nuni (Q4 April).

AsksRoadmap includes \~70+ deliverables across 4 objectives. Builder gets named slots in FTU + DSB + AI tracks but does not have its own objective.

Sizing**Per-objective monthly impact estimates: FTU $7K→$22K→$46K→$290K (Apr→May→Jun→Jul); DSB $3K→$8K→$520K→$3M; SMS $97K→$162K→$208K→$469K; Tx $70K→$48K (May→Jun); AI $1K→$40K→$97K→$530K.**

Notable gapsQ4 FY26 items are still in 'Draft' mode per the doc. Several Mobile/Rendering items from VoC plan remain absent from this roadmap.

## 51Master cross-reference — 21 initiatives × 4 evidence sources

| ID     | Initiative · Source doc                                                                                                                                                                                            | Problem · Customer benefit                                                                                                                                                                                                                                                                                                    | Slack VOC theme · MRR exposure                                                             | HeyMarvin research                                                                                                                                                           | Klaviyo gap (Page 4)                                                                         | BigQuery KPI moved                                                                                                                                                        | Confidence · Sizing                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| I-01 ★ | **Reusable Saved Sections / Universal Content**Nuni Strategy (Q3, Phase 7) + VoC Plan (Pillar 2) + H2 FY26 Roadmap (May FTU)                                                                                       | Marketers rebuild header/footer/promo blocks every send; no edit-once-propagate model.**Benefit:** 60–80% complete next-campaign starting point. Cuts brand-update time from hours to seconds.                                                                                                                                | **Saved sections / saved blocks / universal content**$13.7K/mo · 6 HVC users               | Top-cited HeyMarvin Bet 1 (Wes 90-95% reuse · Peter rotating advertisers · Kyle recurring sections · S1.11 + S2.89 explicitly raised) — confirmed in-flight by PM Jose       | F1 (parity must-have)                                                                        | Activation funnel (bulk\_publish\_1w 7.1%) + retention (M3/M6 builder-usage correlation)→ Lift email\_creates and first-time-sends; reduce 'created-but-never-sent' wedge | HIGHNuni doc: contributor to '20-30% builder-driven churn reduction' (no isolated $) |
| I-02 ★ | **Drag Image from Local Device into Nuni**Nuni Strategy (Q3, Phase 3) + VoC Plan (Drag & Drop 5%)                                                                                                                  | Users expect drag-an-image-file directly onto the page; today they must add an Image Block placeholder first.**Benefit:** Removes an entire 'placeholder-then-fill' step from the Compose loop. Aligns with how all modern editors behave.                                                                                    | **Generic 'editor is clunky / hard to use'**$5.7K/mo · 6 HVC users                         | Andrea D'Ercole Bee.io detour (HeyMarvin Bet 5) · Wes Turner direct manipulation expectations                                                                                | F4 (in-canvas edit) tangent · part of Page 6 Bet 5 (direct-manipulation editor)              | Bulk\_create→bulk\_publish funnel (currently 25% conv)→ Reduce >500-click sessions (per Nuni SLO target) and friction in Compose loop                                     | HIGHNuni: contributes to 30% reduction in >500-click sessions                        |
| I-03 ★ | **Add within Columns + Improved Drop Zones Visibility**Nuni Strategy (Q3, Phase 3) + Content Insertion brief                                                                                                       | Block placement is unpredictable; users 'misdrop' content (especially into columns) and feel scared of breaking the layout.**Benefit:** Predictable placement — content lands exactly where the user intends. Reduces 'I'm scared to break the layout' fear.                                                                  | **Generic 'editor is clunky / hard to use'**$5.7K/mo · 6 HVC users                         | S1.7 Eric — 2-column discoverability is poor (HIGH research priority) · Wes Turner padding 'dancing around'                                                                  | F5 (sections + per-section mobile-stacking)                                                  | Bulk\_create→bulk\_publish funnel · publishes per session→ Restore bulk\_publish\_1w toward LY 9.7%                                                                       | HIGHNuni: part of Level-3 Efficient Workflow targets                                 |
| I-04 ★ | **In-canvas AI Image Gen + Image Normalization (Vibe / Canva-in-Nuni)**Nuni Strategy (Jan: Image generation; Q3: Image normalization) + H2 FY26 Roadmap (Apr Q4 — Canva AI image gen + Vibe Email Content Editing) | Marketers leave Nuni for Canva/Adobe Express/Bee.io to recolor, swap, resize images; flow breaks every send.**Benefit:** Re-light, re-background, swap objects without leaving the canvas. Matches Klaviyo's Image Remix (Gemini) bar.                                                                                        | **Better image editor / asset management**$793/mo · 2 HVC users                            | Andrea D'Ercole (Bee.io detour every send) · Andrew Obeso (image-resize prompt every time, 20-30 min/send) · Page 6 Bet 5 direct mention                                     | F4 (in-canvas AI image editor — Gemini-class)                                                | Image-block adoption · time-in-builder · first-time-sends→ First-time sends (currently −25.7% YoY); image quality is rate-limiter for non-designer FTUs                   | HIGHH2 FY26 AI: $1K→$40K→$97K→$530K monthly (Vibe + Canva tracks combined)           |
| I-05   | **Multiselect + Drag Handles for padding/margins + Copy/Paste Styles**Nuni Strategy (Q4 Phase 4) + Alignment & Layout brief + VoC Plan (Editing Primitives)                                                        | Users can't align multiple items at once; spacing requires per-block tweaks; brand styles can't be 'pasted' to other elements.**Benefit:** Multiselect + paint format = 5–10× faster repetitive styling. Reduces 'symmetry tax' Wes Turner described.                                                                         | **Snap-to-grid / spacing alignment / structured layout**$7.8K/mo · 1 HVC users             | Wes Turner padding pre-pass · Andrea D'Ercole bottom-align (Hannah confirmed) · single high-MRR snap-to-grid quote                                                           | F5 (sections + alignment)                                                                    | Click count per send (>500-click session bucket)→ Reduce >500-click sessions by 30% (Nuni SLO target)                                                                     | HIGHNuni: 30% reduction in >500-click sessions                                       |
| I-06   | **Chat-based Editing (Q4 Phase 4)**Nuni Strategy (Q4) + H2 FY26 AI track (Vibe Email Content Editing)                                                                                                              | Atomic edits (font, color, copy) require navigating multiple panels; new users hunt for controls.**Benefit:** Natural language: 'make the headline bigger and red' executed in seconds. Lowers click count and discovery cost.                                                                                                | **Generic 'editor is clunky' + Steep learning curve**$10.4K/mo · 12 HVC users              | S1.5 (DnD handle confusion) · S1.10 (discount code editing confusing) · S1.12 (merge tag toggle undiscoverable)                                                              | Adjacent to D2 (channel-adaptive AI content) · partial F3 (AI section/layout generator)      | Activate→publish-1w (currently 7.1%)→ Lift first-time sends (−25.7% YoY) by lowering discovery cost for new users                                                         | MEDPart of H2 FY26 AI envelope ($1K→$530K monthly)                                   |
| I-07 ★ | **One-click Apply Brand + Branded Templates**Nuni Strategy (Q3 Phase 2) + H2 FY26 Roadmap (May FTU 'Branded Template E2E')                                                                                         | Brand Kit is disconnected from Nuni; users manually re-style every campaign. 'Blank-page anxiety' before first send.**Benefit:** Templates auto-apply user's brand (logo, colors, fonts). FTUs see their brand on first canvas open — collapses time-to-first-on-brand-send.                                                  | **Brand voice / tone learning AI (proxy for brand-kit-on-AI-drafts)**$410/mo · 1 HVC users | S1.59 Eric — Global styles undiscoverable (HIGH research) · S2.35 Jacob — templates don't apply brand kit buttons · Nuni doc: 'Connect Brand Kit and fix global inheritance' | Tangent to F2 (brand voice from corpus); Klaviyo also lacks one-click brand apply at scale   | Activation funnel · FTU activation→publish-1w · open/click rate (better-on-brand emails outperform)→ Lift FTU 90d retention (H2 FY26 target: 2.85-5.34% lift = $1.5-2.8M) | HIGHH2 FY26 FTU Optimal Setup: $1.5M-$2.8M projected (12-mo)                         |
| I-08   | **Multiple Brand Kits + Audience-Specific Brand**Nuni Strategy (Q3 foundation, Q4 audience-specific)                                                                                                               | Agencies manage multiple brands per Mailchimp account; one brand kit doesn't fit. Hannah's ProServ insight: brand-conscious agencies are dealbreaker-sensitive.**Benefit:** Agencies and multi-brand SMBs can ship without per-account workarounds. Removes a top dealbreaker for agency tier.                                | no Slack VOC mapping                                                                       | S1.59 (Eric agency dealbreaker) · S2.35 (Jacob brand application) · HeyMarvin Andrea D'Ercole (multi-brand workflow)                                                         | Klaviyo also single brand kit — potential differentiator                                     | DSB / agency segment retention (Page 7/8 DSB cuts)→ DSB MRR +13% YoY (H2 Obj 2 KR)                                                                                        | MEDPart of DSB $3M-$8M envelope                                                      |
| I-09 ★ | **Brand Voice + On-brand Content Generation (Q4)**Nuni Strategy (Q4 Phase 2)                                                                                                                                       | AI drafts are generic; sound like 'every other brand's email.'**Benefit:** AI infers tone from past sent emails (corpus-based) and applies to all generated drafts. Drafts feel on-brand from day one.                                                                                                                        | **Brand voice / tone learning AI**$410/mo · 1 HVC users                                    | Page 6 implicitly — AI-generated drafts called out as generic by HeyMarvin engaged users; Wes Turner brand-kit expectations                                                  | F2 (Brand Voice from corpus — Klaviyo's distinct moat)                                       | AI-feature adoption (needs new event surface — flagged Page 7)→ AI features adoption rate; engagement quality (already +2 pts open YoY)                                   | HIGHPart of H2 FY26 AI track ($1K-$530K monthly)                                     |
| I-10 ★ | **Gmail Clipping + Dark Mode Guidance**Nuni Strategy (Jan/Q3 Phase 6) + VoC Plan Deep Dive #3 Rendering                                                                                                            | Sent emails render differently than the editor preview (Outlook, dark mode). Users blame Mailchimp.**Benefit:** In-editor warnings before send: 'this email will be clipped in Gmail at X' / 'this color won't survive dark mode.' Builds confidence.                                                                         | **Mobile preview accuracy / WYSIWYG breakdown**$2.6K/mo · 2 HVC users                      | 44 VoC items in Rendering bucket (10% of 468) · 'Why can't you keep the colors I chose' direct quote                                                                         | Adjacent F8 (built-in inbox testing — Klaviyo bundles via Mailgun)                           | Open/click rate (rendering quality affects engagement) · CSAT→ Sustain engagement quality gains (+2 pts open YoY) · CSAT (now 60%)                                        | HIGHPart of Quality Pod's 20-30% reduction in mobile/rendering complaints            |
| I-11   | **Inbox Previews refresh + consolidated checks (Q4)**Nuni Strategy (Q4 Phase 6) + VoC Plan                                                                                                                         | Litmus integration is hidden; preview is fragmented (separate from link-check, optimization, dark-mode).**Benefit:** Single 'pre-send confidence wall' — preview, links, dark mode, mobile, deliverability in one panel before send.                                                                                          | **Dark mode / inbox preview / multi-client testing**$1.0K/mo · 2 HVC users                 | VoC Plan: 'Litmus feature is hidden' · Andrew Obeso pre-send anxiety · Kyle Spalding 15-min-future-send                                                                      | F8 (built-in inbox testing — Klaviyo bundles 100/mo via Mailgun)                             | Sends per session (test-send loops drop) · CSAT→ Reduce passive-billing-failure churn (rendering issues drive support tickets → cancellations)                            | HIGHQuality Pod target                                                               |
| I-12 ★ | **Mobile Styles V2 + Dynamic Content on Mobile**VoC Plan Deep Dive #2 (NOT FUNDED) · Nuni Strategy Phase 5 (Q4 Mobile Show/Hide)                                                                                   | 56 mobile-VoC items (12% of total). Users can't unlink mobile/desktop styles, no granular mobile-only display, mobile preview ≠ actual rendering.**Benefit:** Mobile-correct designs without forking templates. Per-section mobile control matches Klaviyo F5.                                                                | **Mobile preview accuracy**$2.6K/mo · 2 HVC users                                          | VoC Plan deepdive — 'mobile view is not how it shows on phone' · Andrea/Hannah confirmed gap                                                                                 | F5 (per-section mobile-stacking) + adjacent D4 (interactive in-inbox)                        | Mobile-render fidelity SLO (Nuni proposed ≥95%)→ Engagement quality (mobile open rate)                                                                                    | HIGHVoC Plan flagged as 'Not funded' — re-fund in H2 critical                        |
| I-13   | **Automated Rendering Test (Litmus API)**VoC Plan (NOT FUNDED) + Pillar 1 (Automated Testing X-Large effort)                                                                                                       | Rendering regressions ship to production; we don't catch them until customers complain.**Benefit:** Catch rendering bugs pre-deploy. Stops the trust-erosion treadmill.                                                                                                                                                       | no Slack VOC mapping                                                                       | VoC Plan recommendation only — no direct customer quote                                                                                                                      | Internal quality, not competitive                                                            | Render-fidelity SLO (Nuni proposed ≥99%)→ Internal — protects engagement-quality YoY gains                                                                                | MEDEffort: X-Large (per Pillar plan)                                                 |
| I-14 ★ | **Generated Layouts + Generated Layouts V2**Nuni Strategy (Dec, Q3) + Phase 1 'Choose Structure'                                                                                                                   | Blank-page anxiety. Non-designer FTUs don't know how to compose a multi-block layout.**Benefit:** Type a goal → AI generates layout draft. Mirrors Klaviyo Email AI's 99-section/day capability.                                                                                                                              | **AI generative / AI image / AI layout**—/mo · 0 HVC users                                 | S1.7 (2-col discoverability) · Reddit r/Klaviyo: 'AI design way better than drag-drop'                                                                                       | F3 (AI section/layout generator — currently Klaviyo only does this)                          | Activate→bulk\_create\_24h (currently 32%)→ Lift first-time sends (−25.7% YoY) for non-designer cohort                                                                    | HIGHPart of H2 FY26 AI envelope                                                      |
| I-15   | **'It's Just an Email' Automations Flow (FTU)**H2 FY26 Roadmap (Apr Q4) — FTU Optimal Setup                                                                                                                        | FTUs see 'automation' as scary/complex; barrier to first automation send. Bianka Kiss / Clint Bartley quotes.**Benefit:** Reframe automation as 'just an email' — drop one trigger, ship. Lowers cognitive cost of first automation.                                                                                          | **Generic editor clunky (proxy)**$5.7K/mo · 6 HVC users                                    | Bianka Kiss (HeyMarvin) — A/B testing undiscovered for years; Clint Bartley DRAFT for 1 yr; Page 6 Bet 2 (Discovery)                                                         | Adjacent — Klaviyo also has steep automation learning curve                                  | Automation create + first send (funnel\_weekly: cjb\_create\_24hrs)→ Logins YoY (−24%) — re-energize visit cadence                                                        | MEDH2 FY26 FTU Optimal Setup: $1.5M-$2.8M                                            |
| I-16 ★ | **Pick-up-where-you-left-off (Wayfinding)**H2 FY26 Roadmap (Mar Q3) — FTU Optimal Setup                                                                                                                            | Users abandon a draft and can't find it again on next login. Created-but-never-sent wedge.**Benefit:** Surfaces incomplete drafts on homepage. Closes gap between create and publish.                                                                                                                                         | **Editor consistency / new builder for journeys**$904/mo · 1 HVC users                     | Clint Bartley DRAFT-resurrect ask · Jillian Ney save-as-template after success · Page 6 Bet 2 (DRAFT-resurrect prompt)                                                       | Adjacent F9 (autosave reliability + version history)                                         | Activate→bulk\_publish\_1w (currently 7.1%) — directly addresses created-but-never-sent→ First-time sends (−25.7% YoY)                                                    | HIGHH2 FY26 FTU Optimal Setup envelope                                               |
| I-17 ★ | **Dynamic Product Blocks + eCom templates with product blocks**Nuni Strategy (Q3 Phase 4 + Q4 Phase 1) + H2 FY26 DSB roadmap (Feb)                                                                                 | DSB switchers from Klaviyo expect product blocks with live catalog feeds; today Mailchimp has them but they're hard to discover (Jacob research) and use placeholder products instead of real Shopify items (S2.53).**Benefit:** Live Shopify catalog → product block at send-time; matches Klaviyo product-block experience. | **Generic clunky + missing competitive parity**$5.7K/mo · 6 HVC users                      | S2.53 Jacob (placeholder products bug, HIGH priority) · S2.50 Jacob (low max items, no hide price) · S2.29 Jacob (discoverability) · Page 6 Bet 5                            | F7 (live product feed parity — Shopify/BigCommerce/Woo)                                      | DSB MRR (H2 KR2.1 +13% YoY)→ Engagement quality + DSB attach rate                                                                                                         | HIGHDSB $3M-$8M cumulative                                                           |
| I-18   | **Klaviyo Email Template Converter + Custom Properties Migration**H2 FY26 DSB Roadmap (Q3) + Switcher track                                                                                                        | DSB switchers from Klaviyo bring legacy templates and contact attributes; today they have to rebuild in Nuni.**Benefit:** Direct migration path: API key + template converter. Reduces switching friction from days to hours.                                                                                                 | no Slack VOC mapping                                                                       | Nuni doc explicitly named DSB-from-Klaviyo as ICP · Page 6 Andrea (switcher mindset) · Page 4 D9 (hybrid editor for switchers)                                               | Strategic differentiator — Klaviyo doesn't make leaving easy                                 | DSB switcher conversion · DSB MRR YoY→ DSB switchers cohort retention                                                                                                     | HIGHPart of DSB $3M-$8M                                                              |
| I-19 ★ | **Quality Pod (Mobile + Rendering, 4 sprints Nov-Jan)**VoC Plan (Recommendation 2)                                                                                                                                 | Mobile (12% VoC) + Rendering (10% VoC) = 22% of all builder feedback. Quick visible wins available.**Benefit:** Rapid bug burndown on highest-volume complaints. Restores trust in product reliability.                                                                                                                       | **Editor performance · Mobile preview accuracy**$5.8K/mo · 7 HVC users                     | VoC Plan deepdives 1+2 · S1.4/S1.6 image-edit bugs · S2.36 logo placeholder · Editor lag complaints                                                                          | F9 (autosave reliability — turn Klaviyo's #1 complaint into our trust marker)                | CSAT (currently 60%) · Crash-free SLO (target ≥99.5%)→ Reduce churn risk pool (currently 71K weekly · 0.23%)                                                              | HIGHVoC Plan target: 20-30% reduction in mobile/rendering complaints by EOQ2 FY26    |
| I-20 ★ | **Builder SLOs (6 metrics with targets)**Nuni Strategy Section 7                                                                                                                                                   | Reliability/performance regressions ship without operational guardrails; team has no shared 'quality bar.'**Benefit:** Operating contract: uptime ≥99.9%, crash-free ≥99.5%, save ≥99.99%, init load P95 <500ms, interaction P95 <300ms, render fidelity ≥99%, mobile ≥95%.                                                   | **Editor performance / lag / browser freeze**$3.2K/mo · 5 HVC users                        | S1.14 Eric — editor crashed losing work · Page 5 multiple performance complaints                                                                                             | F9 (reliable autosave + version history — directly attacks Klaviyo's #1 community complaint) | Crash-free sessions · save success rate · interaction latency P95→ Active churn risk reduction (currently 32K/mo of 71K total churn risk)                                 | HIGHOperational guardrail; not a $ initiative                                        |
| I-21   | **Cross-functional Design Sprint to reimagine clunky workflows**VoC Plan (Recommendation 1, Nov 2025)                                                                                                              | \>25% of VoC is 'Ease of Use / Clunky' — death by 1000 cuts. Won't be fixed by point fixes.**Benefit:** North-star vision for workflow simplification. Foundation for H2 FY26 builds.                                                                                                                                         | **Generic 'editor is clunky' (8 themes converge here)**$23.0K/mo · 20 HVC users            | Multiple HeyMarvin findings · Page 6 Bet 5 (direct manipulation) · Andrea D'Ercole exit quote                                                                                | Foundational; informs F1-F10 sequencing                                                      | Click-budget per send (Nuni proposed ≤250 healthy band)→ Builder-driven churn share (Nuni target: -20-30% vs FY25)                                                        | HIGHProcess / discovery — outputs feed roadmap                                       |

★ \= HIGH-confidence multi-source initiative (13 of 21 — mapped to ≥3 sources: Slack VOC, HeyMarvin research, Klaviyo gap, or BigQuery KPI). Reviewer narrows further to TOP 5 must-do (Section 53 below). Confidence: HIGH = mapped to ≥3 sources. MED = 1-2 sources. LOW = strategic/internal logic only.

## 52Reviewer-agent critique — sharpness, hallucination, coverage

Reviewer ran 4 lenses: hallucination check (every cited number traced to source), coverage check (any VOC theme / research finding / Klaviyo gap not addressed?), redundancy check (overlapping initiatives), and sharpness check (which 5 are actually must-do?).

## PASS · 3 lenses

**✓ Hallucination check: PASS**

Every $ figure traces to a doc source — Nuni Strategy: '20-30% builder-driven churn reduction', VoC Plan: '$4-$6M FY26 revenue impact from improving sends', H2 FY26 FTU Roadmap: '$1.5M-$2.8M projected revenue (12-mo)' from 2.85-5.34% lift in FTU 90d retention, DSB Roadmap: '$3M-$8M cumulative impact estimates'. Every customer-quote citation traces to Page 5 (Slack VOC, MRR-validated) or Page 6 (HeyMarvin transcript with timestamp).

**✓ YoY data backing: PASS**

Every BQ metric reference traces to Page 7/8 actuals: bulk\_publish\_1w 7.1%, first-time-sends -25.7% YoY, M3 retention 76.5→34.5%, churn risk pool 71K. No fabricated numbers.

**✓ Klaviyo competitive mapping: PASS**

F-codes (F1-F10 parity) and D-codes (D1-D10 differentiator) all reference Page 4 strategic plan. F1 (Universal Saved Content) = I-01\. F4 (in-canvas AI image) = I-04\. F2 (Brand Voice from corpus) = I-09\. F5 (sections/mobile-stacking) = I-03/I-12\. F7 (live product feeds) = I-17\. F8 (inbox testing) = I-10/I-11\. F9 (autosave reliability) = I-19/I-20.

## WARN · 5 issues

**⚠ VoC Plan items still 'Not Funded'**

Mobile Styles V2 · Dynamic content on Mobile · Dark mode education · Mobile rendering bug fixes · Expanding Inbox Previews · Automated Rendering Test were ALL marked 'Not funded' in the original VoC Plan (Nov 2025). Some show up in Nuni Strategy (Q4) but no clear funding/owner confirmation. ACTION: confirm funding status with Diana/Eric.

**⚠ AI initiatives positioned as 'horizontal accelerator' but have separate H2 funding**

Nuni doc says 'no specific AI column — AI is horizontal accelerator.' But H2 FY26 Roadmap has AI as Objective 4 with $1K-$530K monthly impact. Risk: builder AI work falls between two budgets. ACTION: clarify funding model — does the Builder team get AI eng capacity, or rely on AI Objective team?

**⚠ Sizing inconsistency between docs**

VoC Plan cites '$4-$6M FY26 revenue impact' from improving email sends. H2 FY26 FTU sizing is '$1.5M-$2.8M from FTU retention.' DSB is '$3M-$8M.' These aren't additive (overlap with retention/MRR). REVIEWER: do not double-count. Treat $4-$6M as the upper-bound sense-check on builder-attributable opportunity.

**⚠ Some initiatives have no Slack VOC mapping**

I-08 (Multi Brand Kits), I-13 (Automated Rendering Test), I-18 (Klaviyo Template Converter) — no direct Slack VOC theme. Justified by research (Page 6) or strategic logic but not customer-articulated in HVC channels. Lower confidence; track CSAT post-ship to validate.

**⚠ Coverage gap — no initiative addresses HVC churn-passive-billing (53% of churn risk pool)**

Page 8 finding: 53% of weekly churn risk is passive billing failure (not active dissatisfaction). The builder team CAN'T own this — but should ensure builder UX doesn't compound (e.g., post-payment-failure 'broken builder' state). ACTION: cross-team coordination with Billing/Recovery.

## OVERLAPS · 3 conflicts

**↔ I-01 (Saved Sections) ↔ I-15 (FTU 'Save Email Sections')**

Same feature; FTU roadmap names it 'Save and Reuse Email Sections' (May Q4) while Nuni Strategy lists 'Reusable Saved Sections' (Q3). Confirm one team / one delivery date.

**↔ I-04 (Image gen + Image Normalization) ↔ I-06 (Chat-based Editing) ↔ Vibe Email Content Editing ↔ Canva AI image gen**

Four overlapping AI-in-builder initiatives across 3 docs. Risk of duplicated eng work. ACTION: rationalize into a single 'AI in Builder' track with clear sub-deliverables.

**↔ I-10/I-11 (Gmail clipping + Inbox Preview consolidation) ↔ Klaviyo F8 (built-in inbox testing)**

Mailchimp's plan is preview/check consolidation; Klaviyo bundles 100 inbox tests/mo via Mailgun. Strategic: do we ship Litmus integration (cheaper, faster) or build native? ACTION: cost/benefit decision.

## 53Reviewer-sharpened TOP 5 — among 21 initiatives

If we can only ship 5 builder-side bets in H1 FY27, these are the highest-leverage by combined-signal scoring (multi-source convergence + competitive parity + KPI lever). Everything else stays on the Nuni roadmap, but these 5 define the team's identity for the next 6 months.

#### I-01 Reusable Saved Sections / Universal Content

5-source convergence — Slack ($13.7K MRR · 6 HVC users) + HeyMarvin Bet 1 + S1.11+S2.89 research + Klaviyo F1 parity + bulk\_publish\_1w funnel lever. Confirmed in-flight by PM Jose. Highest-confidence ship.

#### I-19 Quality Pod (Mobile + Rendering)

22% of all VoC + Klaviyo's #1 weakness (autosave/rendering) becomes our trust marker. Crash-free SLO directly attacks active churn risk pool (32K/mo).

#### I-04 In-canvas AI image (Vibe + Canva-in-Nuni)

Andrea D'Ercole Bee.io detour is the single most-cited research finding. Klaviyo F4 parity. Lifts first-time sends (the −25.7% YoY metric).

#### I-07 One-click Apply Brand + Branded Templates E2E for FTUs

Maps to H2 FY26's biggest sized opportunity ($1.5M-$2.8M from FTU retention). Solves S1.59 + S2.35 + Page 6 brand-kit findings simultaneously.

#### I-20 Builder SLOs (6 metrics)

Operating contract that institutionalizes the quality bar. Without these, every other shipping bet rots. Page 8 churn-risk active-pool reduction depends on this.

## 54Implications & "go-do" list for the new product lead

**Inherit, don't restart.** The Nuni Strategy is well-formed and Eric Anderson-reviewed. Don't redo the strategy work. _Validate the SLO instrumentation, ship the must-do 5, and watch the leading indicators_ (bulk\_publish\_1w 7.1%, first-time-sends -25.7%, M3 retention 34.5%).

**Re-fund the unfunded mobile + rendering work in Week 1.** Mobile Styles V2 + Dynamic Mobile Content + Dark Mode + Inbox Previews refresh have been "Not funded" since Nov 2025\. They map to 22% of VoC + Klaviyo F5/F8 parity + Page 8 mobile-render-fidelity SLO. The biggest hidden risk is letting these slip another quarter.

**Resolve the AI ownership split.** Vibe Email Editing, Canva-in-Nuni, Freddie Campaigns, Brand Voice — 4 different AI-in-builder threads across 3 docs. Get into a room with Nathan Snell + Diana + Eric to consolidate into a single "AI in Builder" track with one PM, one design lead, one engineering owner.

**Sources (Page 9):** _Documents reviewed:_ (1) Builder VoC Feedback Response Plan (Ose Amiegheme · Erin McCue · JB Lovell · Joyce Russell · Nov 5, 2025); (2) Builder VoC Response Plan — Pillar version; (3) Nuni Builder Strategy and Roadmap (Ose Amiegheme · Erin McCue · JB Lovell · Ashley Wiesner · reviewed by Eric Anderson · Jan 2, 2026); (4) Mailchimp H2 FY26 Product Priorities (Diana Williams); (5) Mailchimp H2 FY26 Roadmap (Diana Williams · Mar 12, 2026 update).  
  
_Cross-reference sources:_ Page 4 (Mailchimp Roadmap parity F1-F10 + differentiator D1-D10) · Page 5 (HVC Slack VOC themes with $/mo MRR exposure) · Page 6 (HeyMarvin 25 customer briefs + Top 5 Bets) · Page 7-8 (BigQuery YoY health metrics).  
  
_Reviewer-agent methodology:_ Four lenses applied to every initiative — (a) Hallucination check: every $ figure and customer quote traced back to source-of-record; (b) Coverage check: which VOC themes / research findings / Klaviyo gaps are NOT addressed; (c) Overlap check: same feature appearing in multiple docs with different names/dates; (d) Sharpness check: ranking by combined-signal score (multi-source convergence × competitive impact × KPI lever × engineering feasibility). Top 5 must-do selected by a hard cutoff at 5 (not 6 or 7) to force prioritization.

Competitive Intelligence · Executive Brief · Page 10 of 11

# Mailchimp's Email Builder

The new drag-and-drop campaign builder (codenamed "Nuni" internally) plus the legacy Classic Builder it's replacing — block library, Section Manager, 250+ templates, Brand Kit, Intuit Assist AI tools (Write with AI, Creative Assistant), and the entry-friendly pricing model that defines Mailchimp's strategic position.

**Scope:** Email Builder only  
(excludes Flows/Customer Journey Builder, SMS, segmentation, Audience, Forms)

**Last updated:** May 2026

250+

Templates in new builder · vs \~100 in deprecated Classic Builder · vs Klaviyo 160+

\~10

Native drag-and-drop block types (Paragraph, Heading, Image, Button, Layout, Divider, Spacer, Survey, Apps, Section)

89%

G2 ease-of-use score — **highest in category** (vs Klaviyo 86, HubSpot 88, Constant Contact 87)

$0 → $350

4 plans: Free / Essentials $13 / Standard $20 / Premium $350 — pricing increase effective April 13, 2026

## 55What the product feature is

The **Mailchimp Email Builder** (the "new builder" — internally codenamed Nuni) is the WYSIWYG drag-and-drop canvas marketers use inside the Campaigns flow to design email broadcasts. Default for all accounts created after July 2023\. The deprecated **Classic Builder** (legacy) remains for accounts created before that date — but Classic Automation Builder was retired June 1, 2025 and all flows have moved to the new Customer Journey Builder.

Mailchimp positions the editor as **genuinely no-code, intuitive, beginner-friendly** — the lowest-friction first-run experience in category. The product surface: left-rail block library, center canvas with Sections + Layouts (columned blocks), right-rail content/style panel, top bar for Preview/Test/AI/Brand Kit.

Drag-and-drop canvas Section Manager Layouts (columned) 250+ templates Brand Kit + Creative Assistant Write with AI (Intuit Assist) Apps blocks Survey blocks 

## 56Why it matters strategically

**The builder is Mailchimp's primary creation surface and the entry point for the SMB/beginner ICP.** Where Klaviyo wins on power-user depth, Mailchimp wins on first-run simplicity — the 89% G2 ease-of-use score is the highest in the category and the most defensible brand asset.

Mailchimp's strategic risk: the new builder migration is incomplete (only \~26% paid adoption late 2024 per public UX-designer migration plan), Classic users are forced to manually rebuild, and the pricing escalation since Intuit's 2021 acquisition is eroding the Trustpilot brand sentiment (2.7/5, 67% 1-star). The H2 FY26 product priority (Diana Williams) puts _FTU activation + ease-of-setup_ at Objective #1 — the builder is the most-touched surface on that mandate.

## 57Block library (new builder)

Marketers compose by dragging atomic units from the left sidebar. The new builder has a smaller, simpler block library than Klaviyo's — by design. Each block has its own properties panel.

¶

Paragraph

Text + links

H

Heading

Text

▭

Image

Content

▢

Button

CTA

━

Divider

Layout

↕

Spacer

Layout

⊞

Layout

Columned · padding · alignment

▤

Section

Group / manage

?

Survey

Polls / response

⊕

Apps

Pull from integrations

</>

HTML (legacy)

Classic Builder only

**Notable gap vs Klaviyo:** No native Product block (Mailchimp's product blocks come from Apps/integrations rather than first-class), no first-class Code/HTML block in new builder (Classic only), no native Saved/Universal Content blocks (the #1 Mailchimp HVC ask — see Page 5).

## 58Core editor capabilities

* **Section Manager:** add, rename, duplicate, reorder, delete sections. Library of pre-built section designs.
* **Layouts:** columned blocks with customizable padding/margin/alignment _per device_ (desktop and mobile separately). Pre-built layouts with starter content, or blank layouts.
* **250+ templates** in the new builder (vs \~100 in legacy) — mobile-optimized, conversion-focused, applicable through Brand Kit.
* **Brand Kit:** logos, fonts, colors, brand personality stored once and applied across emails, social posts, automation flows, landing pages.
* **Undo/Redo** in the new builder.
* **Checklist-based campaign builder** — non-rigid order; users complete fields when they want, not in fixed sequence.
* **Preview & test:** desktop/mobile preview, send test emails. (No native multi-inbox rendering test — gap vs Klaviyo's Mailgun-bundled.)
* **Apps content blocks:** pull live content from connected platforms (e-commerce store, CRM, etc.) — Mailchimp's substitute for Klaviyo's first-class product block.
* **Survey content blocks:** embed polls/single-question surveys directly in email — feature Klaviyo doesn't have.

## 59AI built into the builder (Intuit Assist powered)

### Write with AI Standard+ · Beta

Inline AI in Paragraph / Heading / Button blocks. Generate net-new content from prompt; edit existing copy (lengthen, shorten, change tone, fix spelling/grammar). Powered by Intuit AI.

Currently **beta**. US/UK/CA/AU only. Standard plan or higher. _Trails Klaviyo Email AI's section-generation capability — does copy, not full layouts._

### Creative Assistant Standard+

AI-generated on-brand graphics and layouts using Brand Kit assets (logos, colors, fonts). 5 goal-based template categories: Sell · Announce · Advertise · Welcome · Educate & Inform. Designs in under 10 seconds.

Beta launched April 2020\. \~5M designs created since. Mailchimp claims **+14% engagement uplift** on Creative-Assistant-generated campaigns.

### Email Content Generator Standard+

Standalone generative AI tool for full email drafts (separate announcement). Part of Intuit Assist's broader 20+ AI/data-science feature stack.

Less mature than Klaviyo Email AI's structured section-generation flow. Output is more text-first than layout-first.

### Subject-line + Send-time AI Standard+

Send-time optimization (predictive best send hour per recipient) and predictive send-day recommendations. Subject-line suggestions during composition.

Mature feature set; matches Klaviyo Subject Line AI on copy generation but Mailchimp's send-time-optimization is more deeply integrated.

### SMS / social post generation Standard+

Reuses email campaigns to auto-generate SMS and social posts — channel-adaptive content reuse pattern. Ahead of Klaviyo's separate-canvas approach.

Aligns with the omnichannel composition vision (Page 4 D1).

### Coming Soon (H2 FY26) Roadmap

**Vibe Email Content Editing** (Q4) — atomic conversational editing within emails (not just section-targeted). **Canva AI image gen embedded in Nuni** (Apr Q4). **Freddie AI Campaigns** — full E2E campaign creation. **Brand Voice / On-brand content generation** (Q4).

From Diana Williams's H2 FY26 roadmap (March 2026 update). Closes the F2/F3/F4 parity gaps from Page 4.

 Sources (Page 10): mailchimp.com/help/use-section-manager-new-builder · mailchimp.com/help/use-layouts-new-builder · mailchimp.com/help/compare-mailchimps-email-builders · mailchimp.com/help/write-with-ai · mailchimp.com/solutions/ai-tools · mailchimp.com/help/use-brand-kit-creative-assistant · mailchimp.com/newsroom/announcing-email-content-generator · mailchimp.com/pricing/marketing/compare-plans · mailchimp.com/help/about-mailchimp-pricing-plans · benchmarkemail.com/blog/mailchimp-pricing (April 13, 2026 increase) · chimpology.co.uk (June-July 2025 changes) · mailchimp.com/resources/mailchimp-vs-klaviyo · jorgemaya.webflow.io (migration roadmap, 26% adoption stat).

Competitive Intelligence · Executive Brief · Page 10b of 11 (continuation)

# Mailchimp Builder — Differentiation, JTBD, Pricing & Gaps

Where Mailchimp's email builder genuinely wins (vs Klaviyo, vs Constant Contact, vs MailerLite), who reaches for it and why, what each plan unlocks, and what customers consistently call out as broken or missing.

**Reading time:** \~4 min

**Confidence:** High (vendor docs + 12K+ G2 reviews + cross-source)

## 60What truly differentiates Mailchimp's builder (vs Klaviyo, Constant Contact, MailerLite)

vs. all rivals

### Highest ease-of-use in category

89% G2 ease-of-use — the single highest in email marketing. "Removes intimidation factor for marketing." Defensible brand asset.

vs. Klaviyo

### 250+ templates (vs Klaviyo 160+)

Wider template library, more goal-categorized (Sell · Announce · Advertise · Welcome · Educate). Better starting point for non-designers.

vs. Klaviyo

### Lower entry price ($13 vs $20)

Free plan still exists (250 contacts, 1,000 sends/mo) — Klaviyo's Free is 250 contacts but more limited. Essentials at $13/mo is the cheapest credible paid tier in category.

vs. Klaviyo

### Cross-channel content reuse (AI)

Generate SMS + social posts from email campaigns automatically. Klaviyo treats SMS/email as separate canvases. Maps to Page 4 D1 differentiator we want to extend.

vs. all rivals

### Survey content blocks

Embed polls/single-question surveys directly in email — Klaviyo, Brevo, MailerLite don't have native first-class survey blocks.

vs. Klaviyo

### Checklist-based campaign builder

Non-rigid order — users complete fields when they want, not forced step-by-step. Reduces "blank page anxiety" for new marketers.

## 61Who's using it & jobs to be done

**Primary persona:** SMB owner / sole marketer at a service business, blogger, creator, retail/local business, or B2B SMB. Often non-designer, sometimes a "marketing-adjacent" employee (operations, customer success). 13M+ active accounts globally.

**Reference customer types:** SMB / retail / local Bloggers / creators ProServ (legal, accounting, advisory) Industry associations SaaS / B2B SMB Small DSB (Wix, Squarespace, small Shopify) 

Solo marketer · service business

"Send a weekly newsletter that doesn't look like a robot wrote it — without learning HTML or hiring a designer."

Solved by: 250+ templates + Brand Kit + Write with AI for tone-perfect copy.

Local retail business owner

"Replicate last month's promo and ship today's version in 30 minutes between customers."

Solved by: Replicate Email + drag-edit + same-day Send.

Blogger / content creator

"Make a beautiful weekly digest that I can send from my phone if needed."

Solved by: simple builder, mobile-friendly templates. (Native mobile-app editing limited — gap.)

B2B SMB marketer

"Send sales-friendly emails that look as good as bigger competitors' without enterprise tooling."

Solved by: Standard plan + Brand Kit + Creative Assistant. (ProServ-specific templates remain a gap — see Page 6 HeyMarvin.)

Industry-association editor

"Send our member newsletter. It's mostly information, not selling — please don't make it look like an ecommerce promo."

Partial. Templates skew ecommerce/promotional; B2B/info-heavy templates are a documented gap (HeyMarvin Bet 3, Chris Rich quote).

## 62Pricing — what plan unlocks the builder + AI

Builder is in **every plan** (including Free). What Mailchimp gates: AI tools (Write with AI, Creative Assistant), automation, dynamic content, audience count, send-cap multiplier.

#### Free Builder ✓

$0 · 500 contacts · 1,000 sends/mo

* Drag-and-drop builder
* Basic templates (subset of 250+)
* 1 audience · 1 user
* No Write with AI
* No Creative Assistant
* No A/B testing
* No automations
* No template uploads

#### Essentials Builder + basic

$13/mo · 500 contacts · 10× send cap

* Full template library
* 3 audiences · 3 users
* Email scheduling
* A/B testing
* Basic automations
* No Write with AI
* No Creative Assistant

#### Standard Builder + AI ✓

$20/mo · 500 contacts · 12× send cap

* Everything in Essentials
* **Write with AI (Beta)**
* **Creative Assistant**
* Dynamic content personalization
* Predictive segmentation
* 5 audiences · 5 users
* 14-day free trial

#### Premium All AI

$350/mo · 10K contacts · 15× send cap

* Everything in Standard
* Unlimited audiences + users
* Advanced permissions
* Max automation depth
* Priority phone support (only tier)

**Pricing increase effective April 13, 2026.** Mailchimp uses contact-based pricing (charges per active profile, also charges for duplicates across audiences — major Trustpilot complaint). Annual billing 15% discount at 10K+ contacts.

## 63What customers love · what they call out (per 12K+ G2 + Trustpilot + Reddit)

## Loved (strengths)

\+ Builder wins

* **Drag-and-drop is the "crown jewel"** — universally cited as easiest in category. "Zero technical skill" required.
* **Beginner-friendliness** — "removes intimidation factor for marketing." Defensible brand asset.
* **250+ templates** — wide library, conversion-focused, mobile-optimized. Best starting point for non-designers.
* **Brand Kit + Creative Assistant** — AI-generated on-brand designs in under 10s. \~5M designs created since 2020 launch.
* **Checklist-based campaign builder** — non-rigid order, more control than competitors' fixed-sequence flows.
* **300+ integrations** — broad ecosystem. Apps content blocks pull from connected platforms.
* **Cross-channel reuse (AI)** — generate SMS + social posts from email campaigns. Ahead of Klaviyo here.

## Called out (gaps)

– Builder gaps

* **Billing post-Intuit acquisition** — surprise overcharges, deleted contacts still counting, charging per contact per list (duplicates = multiple fees). DOMINATES Trustpilot 67% 1-star reviews.
* **Free plan gutted** — 2,000 → 500 contacts; lost A/B testing, automations, scheduling, template uploads since 2021 acquisition.
* **New builder migration is incomplete** — only \~26% paid adoption late 2024 per public UX migration plan. Classic templates can't auto-migrate to new builder.
* **No native Saved/Universal Content blocks** — Mailchimp HVC's #1 feature ask (Page 5 — $13.7K/mo MRR exposure, 6 HVC users). On Q3 roadmap as "Reusable Saved Sections."
* **Account suspensions for vague compliance issues** — sudden blocks, no explanation, lost access. Recurring Reddit r/MailChimp + Trustpilot complaint.
* **Customer service "nonexistent"** — no phone support except Premium ($350/mo). Slow response times.
* **UI churn** — "clunky, outdated, slow UI, confusing settings." Editor labeled "clunky" by 25%+ of HeyMarvin VOC (Page 6).
* **Deliverability deteriorating** — independent 2026 review measured 78.35% inbox / 20% spam.
* **Pricing escalation 20-30% since 2021** — additional increase April 13, 2026.

## 64So what — implications for the new product lead

**Defend the ease-of-use moat aggressively.** 89% G2 ease is the single most defensible asset Mailchimp has. Every roadmap decision should ask: "does this preserve or erode the first-run simplicity?" Klaviyo at 86 is closing fast.

**Ship the new-builder feature parity.** 26% adoption after 2.5 years means Classic users are voting with their feet. Forced migration without parity = silent churn. Saved Sections (in flight) + Image editing restoration (deprecated, painful) + custom HTML support are top three.

**Decouple Builder sentiment from Billing sentiment.** The Trustpilot 2.7 vs G2 4.3 gap is almost entirely billing-driven. The Builder team can't fix the billing model — but should ensure the builder UX doesn't compound (post-failed-payment "broken builder" states, unclear plan-gating in editor).

 Sources (Page 10b): G2 (4.3/5, 12K+ reviews — 89% ease-of-use highest in category) · Capterra (\~4.5) · Trustpilot (2.7/5, 1,300+ reviews, 67% 1-star) · TrustRadius · SaaS Scored (6.5/10) · Sender.net · EmailVendorSelection 2026 review · Marketing Starter Hub · Stack Verdict · saasprobe 2026 · Reddit r/MailChimp · Chimpology blog (June-July 2025 changes) · Jorge Maya UX migration portfolio (26% adoption stat) · Pickthatemail "Why 67% give it 1 star" · benchmarkemail.com (April 13, 2026 pricing increase). HeyMarvin internal research (Page 6) cross-referenced for editor-specific friction.

Competitive Intelligence · Executive Brief · Page 11 of 11

# Mailchimp Email Builder — Voice of Customer

Sentiment synthesis from G2 (12,000+ reviews), Capterra, Trustpilot (1,300+ reviews), Reddit (r/MailChimp, r/marketing), TrustRadius, agency blogs, and 2026 independent reviews — strictly about the **Mailchimp email builder/editor**. Cross-referenced with internal HVC Slack VOC (Page 5) and HeyMarvin research (Page 6).

**Sources scanned:** 12K+ G2, 1.3K+ Trustpilot, 8 review sites

**Window:** primarily 2024–May 2026

**Mailchimp's editor is the easiest in category — and customers love it.** The drag-and-drop builder is universally praised as "the crown jewel," beginner-friendly, intuitive (89% G2 ease-of-use, highest in category). _But the brand sentiment is being dragged down by everything around it_: post-Intuit billing changes (67% of Trustpilot reviews are 1-star), the gutted Free plan (2,000 → 500 contacts), incomplete migration to the new builder (only \~26% paid adoption late 2024), declining customer service (no phone support except Premium), and editor-specific friction reported in our own HVC channels — "clunky," autosave bugs, slow performance, deprecated image editing. **The G2 4.3/5 vs Trustpilot 2.7/5 chasm tells the story:** the product is loved, the company experience is not.— Synthesis across G2 (12K+ reviews), Capterra, Trustpilot, Reddit r/MailChimp, TrustRadius, 2026 independent reviews · May 2026 

## 65Sentiment by channel

G2

4.3 / 5

12,000+ reviews · 57% five-star · highest ease-of-use in category (89%)

Capterra

\~4.5 / 5

Beginner-friendly consistently called out as #1 strength

TrustRadius

\~4.0 / 5

"Wonderful interface, easy-to-use, budget-friendly" — typical reviewer voice

SaaS Scored editorial

6.5 / 10

Lower than Klaviyo's 7.5/10 in same series · cites pricing + deliverability

Trustpilot

2.7 / 5

1,300+ reviews · **67% 1-star**, only 19% 5-star · billing dominates

Reddit r/MailChimp

Mixed-Negative

Account suspensions + 403 errors + billing dominate · editor-specific posts modest

2026 independent reviews

Mixed

EmailVendorSelection / Pickthatemail / Marketing Starter Hub — "no longer best choice"

HVC Slack VOC (Page 5)

Mixed

$128K/mo HVC MRR exposure across 28 themes · editor friction documented

**Read the gap, not just the score.** The 1.6-point chasm between G2 (4.3) and Trustpilot (2.7) is the most important signal here — the _product_ is well-loved (G2/Capterra/TrustRadius all positive) but the _company experience_ (billing, support, migration) is dragging brand sentiment. Builder team owns the first; can't directly fix the second, but can ensure builder UX doesn't compound it.

## What people love (strengths)

\+ 7 themes

### Drag-and-drop "crown jewel" Defining strength

Universally cited as easiest in category. "Zero technical skill required" — small businesses look pro without graphic-design training. Crown jewel asset that defines Mailchimp's brand promise.

> "The email builder is exceptionally easy to use… makes email creation a breeze." — Stack Verdict 2026 review. "Removes the intimidation factor from marketing." — TrustRadius.

**Sources:** Stack Verdict 2026 · G2 (89% ease-of-use score, highest in category) · TrustRadius · Marketing Starter Hub · multi-platform consensus

### Beginner-friendliness · "removes intimidation" ICP fit

Single most-cited strength. The editor is genuinely accessible to non-marketers — solopreneurs, bloggers, local-retail owners. Mailchimp's defensible position vs Klaviyo's complexity.

> "Allows small businesses to look like a pro without graphic design training." — appsupports.co positive-review aggregator.

**Sources:** G2 12K+ reviews · TrustRadius · Capterra · independent 2026 reviews · Mailchimp's vs Klaviyo positioning page

### 250+ templates — wide library Best starting point

Largest credible template library in category (vs Klaviyo 160+). Mobile-optimized, conversion-focused, organized by goal (Sell · Announce · Advertise · Welcome · Educate). Best non-blank-page experience for new marketers.

> "A wide library of customizable templates helps users get started fast." — Stack Verdict 2026.

**Sources:** mailchimp.com/help/compare-mailchimps-email-builders · Stack Verdict · multi-source positive consensus

### Brand Kit + Creative Assistant AI on-brand

Brand Kit (logos, fonts, colors, brand personality) + AI Creative Assistant generates on-brand designs in under 10 seconds across email, social, landing pages. \~5M designs created since 2020 launch.

> "Mailchimp claims +14% engagement uplift on Creative-Assistant-generated campaigns." — ELMNTL agency review.

**Sources:** mailchimp.com/help/use-brand-kit-creative-assistant · ELMNTL agency review · Mailchimp internal Creative Assistant data

### Checklist-based campaign builder User control

Non-rigid order — users complete fields when they want, not forced into step-by-step sequence. Reduces "blank page anxiety" and respects how marketers actually work.

> "The checklist-based campaign builder gives users 'more control' and lets them create emails in any order they want, rather than forcing a rigid step-by-step process." — Mailchimp campaign-builder announcement, broadly received positively.

**Sources:** mailchimp.com/resources/introducing-a-new-and-improved-campaign-builder · multi-source positive reception

### 300+ integrations + Apps content blocks Ecosystem

Broad integration ecosystem. Apps content blocks pull live content from connected platforms (e-commerce, CRM, etc.) — Mailchimp's substitute for first-class product blocks.

> "Multiple features beyond email: social, websites, ads, plus 300+ integrations." — EmailVendorSelection 2026 pros list.

**Sources:** EmailVendorSelection · TrustPilot positive reviews · Mailchimp Marketplace

### Cross-channel content reuse (AI) Niche advantage

Generate SMS + social posts from email campaigns automatically — channel-adaptive content reuse. **Ahead of Klaviyo here** (Klaviyo treats channels as separate canvases). Maps to Page 4 D1 differentiator.

> "Generate SMS and social media posts based on effective email campaigns." — mailchimp.com/solutions/ai-tools.

**Sources:** mailchimp.com AI tools page · Diana Williams H2 FY26 roadmap (cross-channel orchestration)

## What people hate (gaps)

– 9 themes

### Billing post-Intuit acquisition #1 complaint · DOMINATES

67% of Trustpilot 1,300+ reviews are 1-star — almost entirely billing. Surprise overcharges, deleted contacts still counting toward limits, charging per contact per list (duplicates = multiple fees), pricing increased 20-30% since 2021 acquisition + new increase April 13, 2026.

> "$14/mo shown in dashboard then charged $566." Recurring quote pattern across Trustpilot. EmailVendorSelection 2026: "Multiple price increases since Intuit's 2021 acquisition. 5,000 contacts now cost $100/month on Standard plan."

**Sources:** Trustpilot 2.7/5 (1,300+ reviews, 67% 1-star) · Pickthatemail "Why 67% give 1 star" · EmailVendorSelection 2026 · benchmarkemail.com pricing tracker · cross-platform consensus

### Free plan gutted SMB betrayal

Reduced from 2,000 to 500 contacts. Lost A/B testing, automations, scheduling, template uploads. SMBs that built on Mailchimp's "first email tool to offer free" promise feel betrayed.

> "Free plan severely limited: Reduced from 2,000 to 500 contacts; lacks automations, A/B testing, template uploads, and email scheduling." — EmailVendorSelection 2026 cons.

**Sources:** EmailVendorSelection · multiple 2026 reviews · Reddit r/MailChimp threads about Free degradation

### New builder migration incomplete Adoption stalled

Only \~26% of paid customers had adopted the new builder by late 2024 (per public UX migration plan). Classic templates can't auto-migrate. Classic Automation Builder discontinued June 1, 2025 — forced migration without parity.

> "Most continuing to prefer the 'classic' builder due to familiarity and time constraints… new builder initially lacked basic features crucial for high-value customers." — Jorge Maya UX migration portfolio (public).

**Sources:** jorgemaya.webflow.io migration roadmap · elsop.com analysis · mailchimp.com/help/switch-your-default-email-builder

### ★ Image editing feature deprecated Recent · 2026

Full image-editing toolset (resize, rounded corners, effects beyond cropping) was REMOVED from new builder. Users describe as downgrade. Mirrors the same Klaviyo deprecation we documented on Page 3.

> "Why is the 'edit image' feature gone from the template editor?" — recurring community complaint pattern. Users report relying on it for routine work.

**Sources:** HeyMarvin Andrew Obeso (Page 6) — image-resize prompt every send takes 20-30 min · Andrea D'Ercole (Bee.io detour for image work) · agency reviews

### No native Saved/Universal Content blocks #1 HVC ask

Top HVC complaint per our internal Slack VOC (Page 5): $13.7K/mo MRR exposure across 6 HVC users. Marketers manually rebuild header/footer/promo every send. On Q3 roadmap as "Reusable Saved Sections" but not yet shipped broadly.

> "Please, please, please provide the option of saved sections. We have our own footer that we use and every time we use a pre-made Mailchimp template I have to recreate our footer from scratch." — HVC user, $6,685/mo MRR (Page 5 quote, Slack permalink available).

**Sources:** Page 5 HVC Slack VOC · Page 6 HeyMarvin Bet 1 (Wes Turner, Peter Bell, Kyle Spalding) · S1.11 + S2.89 research findings

### Account suspensions for vague compliance issues Trust killer

Sudden account blocks with little explanation. Export disabled during suspensions. 403 errors lock users out. Recurring on Reddit r/MailChimp and Trustpilot.

> "My account was blocked on a vague automated non-compliance issue shortly after signing up and paying. No response from support after 5 days." — r/MailChimp user, decided to cancel.

**Sources:** Reddit r/MailChimp recurring posts · Trustpilot account-suspension complaints · Pickthatemail 2026 review

### Customer service "nonexistent" Support gap

No phone support except Premium ($350/mo). Slow response times, lack of technical knowledge among support staff. Compounds the billing/suspension pain.

> "Customer service described as nonexistent, unresponsive, and unhelpful. No phone support available. Lack of technical knowledge among support staff." — Pickthatemail 2026 synthesis of 1-star Trustpilot reviews.

**Sources:** Trustpilot common complaint pattern · Pickthatemail "Why 67% give 1 star" · multiple independent reviews

### Editor "clunky" / UI churn Builder-specific

25%+ of HeyMarvin VOC labels editor "clunky" — death by 1000 cuts. Recent UI updates (Forms reorganized, Automations renamed to Flows, sidebar layouts) confuse veterans. Slow UI with large datasets.

> "Sometimes things are clunky, like moving a block or putting a background on a block for a button… I find it hard to locate the 'Edit' button after I've replicated an email campaign. Why can't I just copy and paste!!!!! It's so upsetting!!!!" — Builder VoC Plan compilation (Nov 2025, 468 items, 51% Usability bucket).

**Sources:** Builder VoC Feedback Response Plan (Nov 2025, internal) · HeyMarvin 25 customer briefs (Page 6) · Trustpilot UI complaints · Chimpology blog (June-July 2025 changes)

### Deliverability deteriorating Independent finding

2026 independent review measured 78.35% inbox placement, 20.03% spam — meaningful drop from prior years. Affects builder indirectly: even great emails arriving in spam erode user trust in the platform.

> "Deliverability has deteriorated to 78.35% inbox placement, with 20.03% going to spam." — SaaS Scored 2026 independent benchmark.

**Sources:** SaaS Scored 2026 6.5/10 review (independent benchmark) · cross-reference: Page 8 BigQuery shows engagement quality UP YoY for those who do publish

## 66AI sentiment, by feature

Loved

### Creative Assistant

\~5M designs created since 2020 launch. +14% engagement uplift claim. AI on-brand graphics in under 10 seconds — most successful AI feature in Mailchimp's stack.

Mixed (Beta)

### Write with AI

Inline copy generation/editing in Paragraph/Heading/Button blocks. Beta · Standard+ · US/UK/CA/AU only. _Less mature than Klaviyo Email AI's section-generation_ — does copy, not full layouts.

Loved

### Send-time optimization

Predictive best-send-hour per recipient + predictive send-day recs. Mature feature; deeply integrated. Often called out as the most useful AI in Mailchimp's stack alongside Creative Assistant.

Loved (vs Klaviyo)

### Cross-channel content reuse

Auto-generate SMS + social posts from email campaigns. _Ahead of Klaviyo here._ Maps to Page 4 D1 differentiator we want to extend.

Coming

### Vibe Email Editing + Canva-in-Nuni

Vibe = atomic conversational editing (Q4). Canva AI image gen embedded in Nuni (Apr Q4). Closes Klaviyo F4 (in-canvas AI image edit) parity gap. Not yet shipped — TBD reception.

Underwhelms

### Subject Line / Email Content Generator

Like Klaviyo's equivalent, generic output requiring heavy editing. Useful as brainstorming aid, not as final copy. Part of "20+ AI features" claim that buries the genuinely good ones.

## 67So what — implications for our positioning

**The product is the brand asset.** 89% G2 ease-of-use is the single most defensible asset Mailchimp owns. The Builder team should treat first-run simplicity as a hard guardrail — every feature shipped should have a "does this preserve the simplicity moat?" gate. Klaviyo at 86% is closing.

**Decouple Builder sentiment from Billing/Support sentiment.** The 1.6-pt G2-vs-Trustpilot chasm is almost entirely billing-driven. Builder team can't fix the model — but should ensure the builder UX doesn't compound (no broken-builder states post-payment-failure, no in-editor surprise paywalls, no opaque plan-gating).

**Ship the new-builder feature parity in Q3.** 26% adoption after 2.5 years means Classic users are voting with their feet. Saved Sections (in flight, Bet 1) + image editing restoration + custom HTML support are the top three. Without parity, the forced migration creates silent churn — and the Trustpilot reviews compound.

**Sources (Page 11):** G2 (Mailchimp 4.3/5 · 12,000+ reviews · 89% ease-of-use highest in email-marketing category — see g2.com/products/intuit-mailchimp-email-marketing) · Capterra · TrustRadius (Wonderful interface review) · Trustpilot (2.7-2.9/5 · 1,297-1,390 reviews · 67% 1-star — see trustpilot.com/review/mailchimp.com) · Pickthatemail "Mailchimp Review 2026: Why 67% Give It 1 Star" · SaaS Scored Mailchimp 6.5/10 (vs Klaviyo 7.5/10) · saasprobe Mailchimp 2026 review · EmailVendorSelection Mailchimp 2026 honest pros/cons · Marketing Starter Hub Mailchimp 2026 review · Stack Verdict 2026 · Reddit r/MailChimp · ELMNTL agency Creative Assistant review · Chimpology blog (June-July 2025 changes documented) · Jorge Maya UX migration portfolio (26% adoption stat, public) · benchmarkemail.com (April 13, 2026 pricing increase tracker) · mailchimp.com (vendor docs for capability claims).  
  
**Internal cross-references:** Page 5 (HVC Slack VOC — $128K/mo MRR exposure across 28 themes) · Page 6 (HeyMarvin 25 customer briefs · 50 transcripts) · Page 7-8 (BigQuery YoY metrics — first-time-sends −25.7%, M3 retention 76.5→34.5%, engagement quality UP across all segments) · Page 9 (previous PM doc cross-reference — 21 initiatives mapped to customer pain).  
  
_Methodology:_ 8+ public review platforms scanned for editor-specific commentary. Quotes lightly edited for length, not for sentiment. Channel skew explicitly called out (Trustpilot is billing-heavy with selection bias toward complainers, G2 is product-quality skewed). Scope strictly limited to the email builder/editor — Customer Journey Builder (flows), SMS, segmentation, Audience, Forms, billing, and customer support sentiment excluded except where editor-adjacent.