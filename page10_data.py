"""Page 10 — Mailchimp Email Builder Executive 2-Pager.
Mirrors Page 1+2 structure (Klaviyo) but for Mailchimp's email builder specifically.
"""
from pathlib import Path

ROOT = Path("/Users/dprabhakara/cursor/klaviyo-email-builder-competitive-analysis")
OUT = ROOT / "page10_fragment.html"

fragment = """
  <!-- ============ PAGE 10 — MAILCHIMP EMAIL BUILDER EXECUTIVE 2-PAGER ============ -->
  <section class="page" id="page10">
    <div class="page-head">
      <div>
        <div class="eyebrow">Competitive Intelligence · Executive Brief · Page 10 of 11</div>
        <h1>Mailchimp's Email Builder</h1>
        <div class="subtitle">The new drag-and-drop campaign builder (codenamed "Nuni" internally) plus the legacy Classic Builder it's replacing — block library, Section Manager, 250+ templates, Brand Kit, Intuit Assist AI tools (Write with AI, Creative Assistant), and the entry-friendly pricing model that defines Mailchimp's strategic position.</div>
      </div>
      <div class="meta">
        <div><strong>Scope:</strong> Email Builder only<br/><span style="color:#9aa0a6">(excludes Flows/Customer Journey Builder, SMS, segmentation, Audience, Forms)</span></div>
        <div style="margin-top:6px;"><strong>Last updated:</strong> May 2026</div>
      </div>
    </div>

    <!-- KPI strip -->
    <div class="kpi-row" style="margin-bottom:16px;">
      <div class="kpi">
        <div class="v">250+</div>
        <div class="l">Templates in new builder · vs ~100 in deprecated Classic Builder · vs Klaviyo 160+</div>
      </div>
      <div class="kpi">
        <div class="v">~10</div>
        <div class="l">Native drag-and-drop block types (Paragraph, Heading, Image, Button, Layout, Divider, Spacer, Survey, Apps, Section)</div>
      </div>
      <div class="kpi">
        <div class="v">89%</div>
        <div class="l">G2 ease-of-use score — <strong>highest in category</strong> (vs Klaviyo 86, HubSpot 88, Constant Contact 87)</div>
      </div>
      <div class="kpi">
        <div class="v">$0 → $350</div>
        <div class="l">4 plans: Free / Essentials $13 / Standard $20 / Premium $350 — pricing increase effective April 13, 2026</div>
      </div>
    </div>

    <!-- TWO COLUMN: What it is | Why it matters -->
    <div class="grid cols-5-3" style="margin-bottom:16px;">
      <div>
        <h2><span class="num">55</span>What the product feature is</h2>
        <p>The <strong>Mailchimp Email Builder</strong> (the "new builder" — internally codenamed Nuni) is the WYSIWYG drag-and-drop canvas marketers use inside the Campaigns flow to design email broadcasts. Default for all accounts created after July 2023. The deprecated <strong>Classic Builder</strong> (legacy) remains for accounts created before that date — but Classic Automation Builder was retired June 1, 2025 and all flows have moved to the new Customer Journey Builder.</p>
        <p>Mailchimp positions the editor as <strong>genuinely no-code, intuitive, beginner-friendly</strong> — the lowest-friction first-run experience in category. The product surface: left-rail block library, center canvas with Sections + Layouts (columned blocks), right-rail content/style panel, top bar for Preview/Test/AI/Brand Kit.</p>
        <div class="chips">
          <span class="chip">Drag-and-drop canvas</span>
          <span class="chip">Section Manager</span>
          <span class="chip">Layouts (columned)</span>
          <span class="chip">250+ templates</span>
          <span class="chip">Brand Kit + Creative Assistant</span>
          <span class="chip">Write with AI (Intuit Assist)</span>
          <span class="chip">Apps blocks</span>
          <span class="chip">Survey blocks</span>
        </div>
      </div>
      <div>
        <h2><span class="num">56</span>Why it matters strategically</h2>
        <div class="card tinted">
          <p style="margin-bottom:6px;"><strong>The builder is Mailchimp's primary creation surface and the entry point for the SMB/beginner ICP.</strong> Where Klaviyo wins on power-user depth, Mailchimp wins on first-run simplicity — the 89% G2 ease-of-use score is the highest in the category and the most defensible brand asset.</p>
          <p style="margin-bottom:0;">Mailchimp's strategic risk: the new builder migration is incomplete (only ~26% paid adoption late 2024 per public UX-designer migration plan), Classic users are forced to manually rebuild, and the pricing escalation since Intuit's 2021 acquisition is eroding the Trustpilot brand sentiment (2.7/5, 67% 1-star). The H2 FY26 product priority (Diana Williams) puts <em>FTU activation + ease-of-setup</em> at Objective #1 — the builder is the most-touched surface on that mandate.</p>
        </div>
      </div>
    </div>

    <!-- BLOCK TYPES + CORE CAPABILITIES -->
    <div class="grid cols-2" style="margin-bottom:16px;">
      <div>
        <h2><span class="num">57</span>Block library (new builder)</h2>
        <p style="margin-bottom:8px;">Marketers compose by dragging atomic units from the left sidebar. The new builder has a smaller, simpler block library than Klaviyo's — by design. Each block has its own properties panel.</p>
        <div class="block-grid">
          <div class="block-tile"><span class="ic">¶</span><div class="nm">Paragraph</div><div class="tg">Text + links</div></div>
          <div class="block-tile"><span class="ic">H</span><div class="nm">Heading</div><div class="tg">Text</div></div>
          <div class="block-tile"><span class="ic">▭</span><div class="nm">Image</div><div class="tg">Content</div></div>
          <div class="block-tile"><span class="ic">▢</span><div class="nm">Button</div><div class="tg">CTA</div></div>
          <div class="block-tile"><span class="ic">━</span><div class="nm">Divider</div><div class="tg">Layout</div></div>
          <div class="block-tile"><span class="ic">↕</span><div class="nm">Spacer</div><div class="tg">Layout</div></div>
          <div class="block-tile"><span class="ic">⊞</span><div class="nm">Layout</div><div class="tg">Columned · padding · alignment</div></div>
          <div class="block-tile"><span class="ic">▤</span><div class="nm">Section</div><div class="tg">Group / manage</div></div>
          <div class="block-tile"><span class="ic">?</span><div class="nm">Survey</div><div class="tg">Polls / response</div></div>
          <div class="block-tile"><span class="ic">⊕</span><div class="nm">Apps</div><div class="tg">Pull from integrations</div></div>
          <div class="block-tile"><span class="ic">&lt;/&gt;</span><div class="nm">HTML <small>(legacy)</small></div><div class="tg">Classic Builder only</div></div>
        </div>
        <p style="font-size:11.5px; color:var(--muted); margin-top:8px;">
          <strong>Notable gap vs Klaviyo:</strong> No native Product block (Mailchimp's product blocks come from Apps/integrations rather than first-class), no first-class Code/HTML block in new builder (Classic only), no native Saved/Universal Content blocks (the #1 Mailchimp HVC ask — see Page 5).
        </p>
      </div>

      <div>
        <h2><span class="num">58</span>Core editor capabilities</h2>
        <ul>
          <li><strong>Section Manager:</strong> add, rename, duplicate, reorder, delete sections. Library of pre-built section designs.</li>
          <li><strong>Layouts:</strong> columned blocks with customizable padding/margin/alignment <em>per device</em> (desktop and mobile separately). Pre-built layouts with starter content, or blank layouts.</li>
          <li><strong>250+ templates</strong> in the new builder (vs ~100 in legacy) — mobile-optimized, conversion-focused, applicable through Brand Kit.</li>
          <li><strong>Brand Kit:</strong> logos, fonts, colors, brand personality stored once and applied across emails, social posts, automation flows, landing pages.</li>
          <li><strong>Undo/Redo</strong> in the new builder.</li>
          <li><strong>Checklist-based campaign builder</strong> — non-rigid order; users complete fields when they want, not in fixed sequence.</li>
          <li><strong>Preview &amp; test:</strong> desktop/mobile preview, send test emails. (No native multi-inbox rendering test — gap vs Klaviyo's Mailgun-bundled.)</li>
          <li><strong>Apps content blocks:</strong> pull live content from connected platforms (e-commerce store, CRM, etc.) — Mailchimp's substitute for Klaviyo's first-class product block.</li>
          <li><strong>Survey content blocks:</strong> embed polls/single-question surveys directly in email — feature Klaviyo doesn't have.</li>
        </ul>
      </div>
    </div>

    <!-- AI BLOCK -->
    <h2><span class="num">59</span>AI built into the builder (Intuit Assist powered)</h2>
    <div class="grid cols-3" style="margin-bottom:14px;">
      <div class="ai-card">
        <h3>Write with AI <span class="gate paid">Standard+ · Beta</span></h3>
        <p>Inline AI in Paragraph / Heading / Button blocks. Generate net-new content from prompt; edit existing copy (lengthen, shorten, change tone, fix spelling/grammar). Powered by Intuit AI.</p>
        <div class="meta-line">Currently <strong>beta</strong>. US/UK/CA/AU only. Standard plan or higher. <em>Trails Klaviyo Email AI's section-generation capability — does copy, not full layouts.</em></div>
      </div>
      <div class="ai-card">
        <h3>Creative Assistant <span class="gate paid">Standard+</span></h3>
        <p>AI-generated on-brand graphics and layouts using Brand Kit assets (logos, colors, fonts). 5 goal-based template categories: Sell · Announce · Advertise · Welcome · Educate &amp; Inform. Designs in under 10 seconds.</p>
        <div class="meta-line">Beta launched April 2020. ~5M designs created since. Mailchimp claims <strong>+14% engagement uplift</strong> on Creative-Assistant-generated campaigns.</div>
      </div>
      <div class="ai-card">
        <h3>Email Content Generator <span class="gate paid">Standard+</span></h3>
        <p>Standalone generative AI tool for full email drafts (separate announcement). Part of Intuit Assist's broader 20+ AI/data-science feature stack.</p>
        <div class="meta-line">Less mature than Klaviyo Email AI's structured section-generation flow. Output is more text-first than layout-first.</div>
      </div>
      <div class="ai-card">
        <h3>Subject-line + Send-time AI <span class="gate paid">Standard+</span></h3>
        <p>Send-time optimization (predictive best send hour per recipient) and predictive send-day recommendations. Subject-line suggestions during composition.</p>
        <div class="meta-line">Mature feature set; matches Klaviyo Subject Line AI on copy generation but Mailchimp's send-time-optimization is more deeply integrated.</div>
      </div>
      <div class="ai-card">
        <h3>SMS / social post generation <span class="gate paid">Standard+</span></h3>
        <p>Reuses email campaigns to auto-generate SMS and social posts — channel-adaptive content reuse pattern. Ahead of Klaviyo's separate-canvas approach.</p>
        <div class="meta-line">Aligns with the omnichannel composition vision (Page 4 D1).</div>
      </div>
      <div class="ai-card">
        <h3>Coming Soon (H2 FY26) <span class="gate paid">Roadmap</span></h3>
        <p><strong>Vibe Email Content Editing</strong> (Q4) — atomic conversational editing within emails (not just section-targeted). <strong>Canva AI image gen embedded in Nuni</strong> (Apr Q4). <strong>Freddie AI Campaigns</strong> — full E2E campaign creation. <strong>Brand Voice / On-brand content generation</strong> (Q4).</p>
        <div class="meta-line">From Diana Williams's H2 FY26 roadmap (March 2026 update). Closes the F2/F3/F4 parity gaps from Page 4.</div>
      </div>
    </div>

    <div class="source">
      Sources (Page 10): mailchimp.com/help/use-section-manager-new-builder · mailchimp.com/help/use-layouts-new-builder · mailchimp.com/help/compare-mailchimps-email-builders · mailchimp.com/help/write-with-ai · mailchimp.com/solutions/ai-tools · mailchimp.com/help/use-brand-kit-creative-assistant · mailchimp.com/newsroom/announcing-email-content-generator · mailchimp.com/pricing/marketing/compare-plans · mailchimp.com/help/about-mailchimp-pricing-plans · benchmarkemail.com/blog/mailchimp-pricing (April 13, 2026 increase) · chimpology.co.uk (June-July 2025 changes) · mailchimp.com/resources/mailchimp-vs-klaviyo · jorgemaya.webflow.io (migration roadmap, 26% adoption stat).
    </div>
  </section>

  <!-- ============ PAGE 10b — MAILCHIMP STRATEGY / DIFFERENTIATION / JTBD / PRICING ============ -->
  <section class="page" id="page10b">
    <div class="page-head">
      <div>
        <div class="eyebrow">Competitive Intelligence · Executive Brief · Page 10b of 11 (continuation)</div>
        <h1>Mailchimp Builder — Differentiation, JTBD, Pricing &amp; Gaps</h1>
        <div class="subtitle">Where Mailchimp's email builder genuinely wins (vs Klaviyo, vs Constant Contact, vs MailerLite), who reaches for it and why, what each plan unlocks, and what customers consistently call out as broken or missing.</div>
      </div>
      <div class="meta">
        <div><strong>Reading time:</strong> ~4 min</div>
        <div style="margin-top:6px;"><strong>Confidence:</strong> High (vendor docs + 12K+ G2 reviews + cross-source)</div>
      </div>
    </div>

    <!-- DIFFERENTIATORS -->
    <h2><span class="num">60</span>What truly differentiates Mailchimp's builder (vs Klaviyo, Constant Contact, MailerLite)</h2>
    <div class="grid cols-3" style="margin-bottom:14px;">
      <div class="diff">
        <div class="vs">vs. all rivals</div>
        <h3>Highest ease-of-use in category</h3>
        <p>89% G2 ease-of-use — the single highest in email marketing. "Removes intimidation factor for marketing." Defensible brand asset.</p>
      </div>
      <div class="diff">
        <div class="vs">vs. Klaviyo</div>
        <h3>250+ templates (vs Klaviyo 160+)</h3>
        <p>Wider template library, more goal-categorized (Sell · Announce · Advertise · Welcome · Educate). Better starting point for non-designers.</p>
      </div>
      <div class="diff">
        <div class="vs">vs. Klaviyo</div>
        <h3>Lower entry price ($13 vs $20)</h3>
        <p>Free plan still exists (250 contacts, 1,000 sends/mo) — Klaviyo's Free is 250 contacts but more limited. Essentials at $13/mo is the cheapest credible paid tier in category.</p>
      </div>
      <div class="diff">
        <div class="vs">vs. Klaviyo</div>
        <h3>Cross-channel content reuse (AI)</h3>
        <p>Generate SMS + social posts from email campaigns automatically. Klaviyo treats SMS/email as separate canvases. Maps to Page 4 D1 differentiator we want to extend.</p>
      </div>
      <div class="diff">
        <div class="vs">vs. all rivals</div>
        <h3>Survey content blocks</h3>
        <p>Embed polls/single-question surveys directly in email — Klaviyo, Brevo, MailerLite don't have native first-class survey blocks.</p>
      </div>
      <div class="diff">
        <div class="vs">vs. Klaviyo</div>
        <h3>Checklist-based campaign builder</h3>
        <p>Non-rigid order — users complete fields when they want, not forced step-by-step. Reduces "blank page anxiety" for new marketers.</p>
      </div>
    </div>

    <!-- JTBD -->
    <div class="grid cols-2" style="margin-bottom:14px;">
      <div>
        <h2><span class="num">61</span>Who's using it &amp; jobs to be done</h2>
        <p style="margin-bottom:6px;"><strong>Primary persona:</strong> SMB owner / sole marketer at a service business, blogger, creator, retail/local business, or B2B SMB. Often non-designer, sometimes a "marketing-adjacent" employee (operations, customer success). 13M+ active accounts globally.</p>
        <p style="margin-bottom:10px;"><strong>Reference customer types:</strong>
          <span class="chips" style="display:inline-flex;">
            <span class="chip gray">SMB / retail / local</span>
            <span class="chip gray">Bloggers / creators</span>
            <span class="chip gray">ProServ (legal, accounting, advisory)</span>
            <span class="chip gray">Industry associations</span>
            <span class="chip gray">SaaS / B2B SMB</span>
            <span class="chip gray">Small DSB (Wix, Squarespace, small Shopify)</span>
          </span>
        </p>

        <div class="jtbd">
          <div class="role">Solo marketer · service business</div>
          <div class="quote">"Send a weekly newsletter that doesn't look like a robot wrote it — without learning HTML or hiring a designer."</div>
          <div class="why">Solved by: 250+ templates + Brand Kit + Write with AI for tone-perfect copy.</div>
        </div>
        <div class="jtbd">
          <div class="role">Local retail business owner</div>
          <div class="quote">"Replicate last month's promo and ship today's version in 30 minutes between customers."</div>
          <div class="why">Solved by: Replicate Email + drag-edit + same-day Send.</div>
        </div>
        <div class="jtbd">
          <div class="role">Blogger / content creator</div>
          <div class="quote">"Make a beautiful weekly digest that I can send from my phone if needed."</div>
          <div class="why">Solved by: simple builder, mobile-friendly templates. (Native mobile-app editing limited — gap.)</div>
        </div>
        <div class="jtbd">
          <div class="role">B2B SMB marketer</div>
          <div class="quote">"Send sales-friendly emails that look as good as bigger competitors' without enterprise tooling."</div>
          <div class="why">Solved by: Standard plan + Brand Kit + Creative Assistant. (ProServ-specific templates remain a gap — see Page 6 HeyMarvin.)</div>
        </div>
        <div class="jtbd">
          <div class="role">Industry-association editor</div>
          <div class="quote">"Send our member newsletter. It's mostly information, not selling — please don't make it look like an ecommerce promo."</div>
          <div class="why">Partial. Templates skew ecommerce/promotional; B2B/info-heavy templates are a documented gap (HeyMarvin Bet 3, Chris Rich quote).</div>
        </div>
      </div>

      <div>
        <h2><span class="num">62</span>Pricing — what plan unlocks the builder + AI</h2>
        <p style="margin-bottom:8px;">Builder is in <strong>every plan</strong> (including Free). What Mailchimp gates: AI tools (Write with AI, Creative Assistant), automation, dynamic content, audience count, send-cap multiplier.</p>

        <div class="price-grid" style="margin-bottom:10px;">
          <div class="price">
            <h4>Free <span class="pill partial">Builder ✓</span></h4>
            <div class="p">$0 · 500 contacts · 1,000 sends/mo</div>
            <ul>
              <li>Drag-and-drop builder</li>
              <li>Basic templates (subset of 250+)</li>
              <li>1 audience · 1 user</li>
              <li class="cross">No Write with AI</li>
              <li class="cross">No Creative Assistant</li>
              <li class="cross">No A/B testing</li>
              <li class="cross">No automations</li>
              <li class="cross">No template uploads</li>
            </ul>
          </div>
          <div class="price">
            <h4>Essentials <span class="pill partial">Builder + basic</span></h4>
            <div class="p">$13/mo · 500 contacts · 10× send cap</div>
            <ul>
              <li>Full template library</li>
              <li>3 audiences · 3 users</li>
              <li>Email scheduling</li>
              <li>A/B testing</li>
              <li>Basic automations</li>
              <li class="cross">No Write with AI</li>
              <li class="cross">No Creative Assistant</li>
            </ul>
          </div>
          <div class="price spotlight">
            <h4>Standard <span class="pill included">Builder + AI ✓</span></h4>
            <div class="p">$20/mo · 500 contacts · 12× send cap</div>
            <ul>
              <li>Everything in Essentials</li>
              <li><strong>Write with AI (Beta)</strong></li>
              <li><strong>Creative Assistant</strong></li>
              <li>Dynamic content personalization</li>
              <li>Predictive segmentation</li>
              <li>5 audiences · 5 users</li>
              <li>14-day free trial</li>
            </ul>
          </div>
          <div class="price">
            <h4>Premium <span class="pill included">All AI</span></h4>
            <div class="p">$350/mo · 10K contacts · 15× send cap</div>
            <ul>
              <li>Everything in Standard</li>
              <li>Unlimited audiences + users</li>
              <li>Advanced permissions</li>
              <li>Max automation depth</li>
              <li>Priority phone support (only tier)</li>
            </ul>
          </div>
        </div>
        <p style="font-size:11px; color:var(--muted); margin:0;">
          <strong>Pricing increase effective April 13, 2026.</strong> Mailchimp uses contact-based pricing (charges per active profile, also charges for duplicates across audiences — major Trustpilot complaint). Annual billing 15% discount at 10K+ contacts.
        </p>
      </div>
    </div>

    <!-- LOVED / GAPS -->
    <h2><span class="num">63</span>What customers love · what they call out (per 12K+ G2 + Trustpilot + Reddit)</h2>
    <div class="grid cols-2" style="margin-bottom:14px;">
      <div class="card col-loved">
        <div class="col-head"><h2>Loved <span style="font-weight:400; color:var(--muted); font-family:Inter; font-size:12px;">(strengths)</span></h2><span class="count">+ Builder wins</span></div>
        <ul>
          <li><strong>Drag-and-drop is the "crown jewel"</strong> — universally cited as easiest in category. "Zero technical skill" required.</li>
          <li><strong>Beginner-friendliness</strong> — "removes intimidation factor for marketing." Defensible brand asset.</li>
          <li><strong>250+ templates</strong> — wide library, conversion-focused, mobile-optimized. Best starting point for non-designers.</li>
          <li><strong>Brand Kit + Creative Assistant</strong> — AI-generated on-brand designs in under 10s. ~5M designs created since 2020 launch.</li>
          <li><strong>Checklist-based campaign builder</strong> — non-rigid order, more control than competitors' fixed-sequence flows.</li>
          <li><strong>300+ integrations</strong> — broad ecosystem. Apps content blocks pull from connected platforms.</li>
          <li><strong>Cross-channel reuse (AI)</strong> — generate SMS + social posts from email campaigns. Ahead of Klaviyo here.</li>
        </ul>
      </div>
      <div class="card col-hated">
        <div class="col-head"><h2>Called out <span style="font-weight:400; color:var(--muted); font-family:Inter; font-size:12px;">(gaps)</span></h2><span class="count">– Builder gaps</span></div>
        <ul>
          <li><strong>Billing post-Intuit acquisition</strong> — surprise overcharges, deleted contacts still counting, charging per contact per list (duplicates = multiple fees). DOMINATES Trustpilot 67% 1-star reviews.</li>
          <li><strong>Free plan gutted</strong> — 2,000 → 500 contacts; lost A/B testing, automations, scheduling, template uploads since 2021 acquisition.</li>
          <li><strong>New builder migration is incomplete</strong> — only ~26% paid adoption late 2024 per public UX migration plan. Classic templates can't auto-migrate to new builder.</li>
          <li><strong>No native Saved/Universal Content blocks</strong> — Mailchimp HVC's #1 feature ask (Page 5 — $13.7K/mo MRR exposure, 6 HVC users). On Q3 roadmap as "Reusable Saved Sections."</li>
          <li><strong>Account suspensions for vague compliance issues</strong> — sudden blocks, no explanation, lost access. Recurring Reddit r/MailChimp + Trustpilot complaint.</li>
          <li><strong>Customer service "nonexistent"</strong> — no phone support except Premium ($350/mo). Slow response times.</li>
          <li><strong>UI churn</strong> — "clunky, outdated, slow UI, confusing settings." Editor labeled "clunky" by 25%+ of HeyMarvin VOC (Page 6).</li>
          <li><strong>Deliverability deteriorating</strong> — independent 2026 review measured 78.35% inbox / 20% spam.</li>
          <li><strong>Pricing escalation 20-30% since 2021</strong> — additional increase April 13, 2026.</li>
        </ul>
      </div>
    </div>

    <!-- SO WHAT -->
    <h2><span class="num">64</span>So what — implications for the new product lead</h2>
    <div class="grid cols-3">
      <div class="card warm">
        <p style="margin:0;"><strong>Defend the ease-of-use moat aggressively.</strong> 89% G2 ease is the single most defensible asset Mailchimp has. Every roadmap decision should ask: "does this preserve or erode the first-run simplicity?" Klaviyo at 86 is closing fast.</p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Ship the new-builder feature parity.</strong> 26% adoption after 2.5 years means Classic users are voting with their feet. Forced migration without parity = silent churn. Saved Sections (in flight) + Image editing restoration (deprecated, painful) + custom HTML support are top three.</p>
      </div>
      <div class="card warm">
        <p style="margin:0;"><strong>Decouple Builder sentiment from Billing sentiment.</strong> The Trustpilot 2.7 vs G2 4.3 gap is almost entirely billing-driven. The Builder team can't fix the billing model — but should ensure the builder UX doesn't compound (post-failed-payment "broken builder" states, unclear plan-gating in editor).</p>
      </div>
    </div>

    <div class="source">
      Sources (Page 10b): G2 (4.3/5, 12K+ reviews — 89% ease-of-use highest in category) · Capterra (~4.5) · Trustpilot (2.7/5, 1,300+ reviews, 67% 1-star) · TrustRadius · SaaS Scored (6.5/10) · Sender.net · EmailVendorSelection 2026 review · Marketing Starter Hub · Stack Verdict · saasprobe 2026 · Reddit r/MailChimp · Chimpology blog (June-July 2025 changes) · Jorge Maya UX migration portfolio (26% adoption stat) · Pickthatemail "Why 67% give it 1 star" · benchmarkemail.com (April 13, 2026 pricing increase). HeyMarvin internal research (Page 6) cross-referenced for editor-specific friction.
    </div>
  </section>
"""

OUT.write_text(fragment.strip())
print(f"Wrote {OUT} ({len(fragment):,} chars)")
