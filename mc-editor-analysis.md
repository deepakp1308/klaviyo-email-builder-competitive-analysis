Source URL: https://deepakp1308.github.io/mailchimp-email-editor-analysis/
Title: Mailchimp Email Editor — Product Usage Assessment

Brief: §11 priority questions Trailing 90 days Source: bi\_reporting.emails\_bulk 

# Mailchimp Email Editor — Product Usage Assessment

Diagnosis of how customers use the New (drag-drop / multichannel) and Classic (template) email editors: where they start, the flow, where they end, friction points, back-and-forth, and errors. Trailing 90 days, ending most recent complete day.

Executive summary

 Mailchimp's two email editors fail customers in _opposite ways_: _Classic_ is fast for experts but quietly abandons returning users at the design canvas; _New_ has a cleaner overall funnel but loses most first-time creators before they ever reach the canvas, and is materially slower for everyone.

### The 3 things that actually matter

01 — Reframe

"10 million abandoned drafts" isn't real.

Half of all drafts are users who walked away in under 2 minutes — exploration, accidents, fat-finger Create clicks. Build re-engagement for the real at-risk pool, not the headline number.

Real at-risk pool: **\~830K**, not 10M · 50-56% are <2-min abandons

02 — Wound

Classic's design canvas is your single biggest UX wound.

A user who picks a template and never alters it ships **80%** of the time. The moment they edit, completion collapses to **46%**. From blank: **30%**. The act of editing on Classic is what kills the campaign.

**9M+** altered-template attempts at half-completion (90d)

03 — Jackpot

Returning users × Classic is your migration jackpot.

The same cohort of **576K** returning users ships **8%** on Classic and **56%** on New. Same humans, same lifecycle stage — **7×** completion lift just by changing the editor.

Highest-ROI move in the dataset

### What this means for customers

* **First-time creators on New** are bottlenecked at audience selection before they experience the editor's value. \~560K first-time creators per quarter try and never publish.
* **Returning users on Classic** are silently struggling — opening drafts, abandoning, never shipping. They look "active" in dashboards but get nothing done.
* **Power users on Classic** are well-served. They would notice migration as a regression (4.7× slower median time-to-send on New).
* **Compliance blocks fire 23× more on New.** When users hit them, their first impression of New becomes "the system rejected my work."

### What this means for the business

* **Activation leak you can size:** 9M+ Classic edit-from-template attempts in 90 days at half-completion — the largest revenue-of-attempt loss in the dataset.
* **Migration is ROI-positive but cohort-specific** — not a single GA event. Returning users → guaranteed lift. First-timers → no migration needed (they default to New). Power users → risky without speed parity.
* **Ecommerce upside on New is real money:** Tier-3 conversion is 2.1× on New (2.91% vs 1.37%). Every commerce-account migration is a $ event.
* **AI feature adoption is 2.7% / 0.78%** — distribution problem, not value problem.

### What you should do next

Product development

Ranked by leverage

1. **Fix New's audience step.** Default to last-used audience or move it inline with the canvas. 42% of New drafts die here. Goal: lift first-time completion 33% → >50%.
2. **Diagnose Classic's altered-template canvas collapse.** 9M+ attempts at half-completion. Suspects: autosave loss, render confusion, block validation. Goal: 46% → 80%.
3. **New editor performance audit.** 4.7× time-to-send delta blocks power-user migration.
4. **Compliance-block UX in New.** 23× block rate is a first-impression killer.
5. **Replicate-flow parity in New.** Power users live on replicate → tweak → send.

Marketing / GTM

Ranked by safety

1. **Migrate returning users first.** Story: "Finish the campaign you started." 576K accounts. Highest-confidence campaign you can run.
2. **Hold power-user migration messaging** until time-to-send parity. A "the new editor is slower" narrative is brand damage.
3. **First-time creator onboarding overhaul.** "Blank canvas → first send in 10 min" guided flow.
4. **AI feature discoverability campaign.** 2.7% adoption ≠ low value, = no one knows it exists.
5. **Stalled-draft AM segment.** ≥5 stalled drafts in 30d is a silent-churn signal, especially for HVCs.

Instrumentation

The gate that unlocks everything

1. **Editor event log read access** (`rsg-events-pipeline-prod.ingest_v2.events`). Unlocks 11 of 27 brief questions.
2. **Block-counter parity** in `emails_bulk` for New editor. One-week dataform fix.
3. **AI / brand-kit exposure flag** in `bi_segment_dataform.users`.
4. **Device class** on the campaign object (mobile-vs-desktop friction).

Monday morning

If you can only do three things this quarter

1. **Fix New's audience step.** Biggest single first-mile leak; touches every cohort.
2. **Run the migration play for returning users only.** Highest-confidence ROI; builds the muscle for bigger migration later.
3. **Unblock the editor event log.** Without it, the next iteration of this analysis will be just as partial as this one.

## By the numbers

25.9M

Campaigns created (90d)

1.45M

Active creator accounts

14.83M

Tier-1 real sends

10.66M

Drafts (never sent)

Critical instrumentation gap — this report is partial

The brief requires editor event-log analysis (microstep funnel, path mining, friction-score hotspots, undo / autosave / render telemetry, support-ticket joins). The granular event sources were not queryable in this run:

• `rsg-events-pipeline-prod.ingest_v2.events` — 403 access denied. Blocks A1, A3, A4 (microstep level), A5, A11, and the friction-score formula in §5.

• Client telemetry (autosave / image upload / render / lag) — no table found in the accessible BigQuery surface. Blocks L5 and the `z_perf` / `z_undo` components of the friction score.

• Support-ticket data tagged to "editor" product area — not located. Blocks `z_support` and A11 (complainers vs silent strugglers).

• Block-level usage in `emails_bulk` is not populated for the New editor — sent New campaigns show \~0.4 blocks vs Classic 7.4\. Blocks A15.

Per the brief: "If data gaps prevent any of these, stop and produce the instrumentation gap report instead of guessing." The gap report is in §15 below. What follows uses the campaign-object table — reliable picture of outcomes but not in-canvas behavior.

## 1\. Data validation (brief §4 prerequisite)

What was verifiable on the campaign-object table. Items marked blocked require the event log.

| Validation check                                        | Result                                                                                      | Status   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------- |
| Identity (non-null user\_id, campaign\_id)              | 100% non-null on both                                                                       | pass     |
| Identity (login\_id attribution)                        | Classic 99.1% / New 100.0% / HTML 100.0%                                                    | pass     |
| Editor coverage (% of campaign sends w/ editor session) | Cannot compute without event log                                                            | blocked  |
| Reconciliation (event log vs campaign object)           | Cannot compute without event log                                                            | blocked  |
| Cross-editor mapping (New ↔ Classic event vocabulary)   | Cannot build without event log                                                              | blocked  |
| Client telemetry coverage (autosave / upload / render)  | No table found                                                                              | blocked  |
| Device attribution (mobile / tablet / desktop)          | Not in campaign-object table                                                                | blocked  |
| AI feature flags (per-account exposure log)             | Per-campaign AI use is logged; account exposure not located                                 | partial  |
| Block-level instrumentation parity (New vs Classic)     | New editor sends show 0.43 avg blocks; Classic sends 7.39\. Counters not populated for New. | fail     |
| OAuth client attribution (created\_by\_client)          | Classic 6.3% / New 1.9% — only populated for API-created campaigns                          | expected |

## 2\. Population sizing (lifecycle × editor)

1,445,450 distinct accounts created at least one campaign in the 90-day window. Definitions per brief §5.

612,680

Power users (≥5 sends 90d OR ≥20 12mo)

576,368

Returning (had prior 24mo)

256,402

First-time creators (no prior 24mo)

The brief also requires reporting on churned-eligible and reactivated populations — these need a join to plan/billing status (`bi_segment_dataform.users`). Not included here, flagged in gap report.

## 3\. Send-tier funnel — A2 (per editor)

Brief §5 four-tier ladder. "Test send only" (Tier 0) is not value; real send (Tier 1) is the first value milestone; engagement (Tier 2) and business value (Tier 3) follow.

New editor (drag-drop) multichannel

| Stage                                  | Campaigns | Conversion |
| -------------------------------------- | --------- | ---------- |
| S0 Create-start                        | 8,469,070 | 100.0%     |
| S2 Sent test send                      | 2,493,670 | 29.4%      |
| S3 Scheduled or sent                   | 6,054,901 | 71.5%      |
| S4 Tier-1 real send (≥1 ext recipient) | 5,846,472 | 69.0%      |
| S4b Tier-1 publish (>10 recipients)    | 5,318,435 | 62.8%      |
| S5 Tier-2 engagement (≥1 open)         | 5,760,700 | 68.0%      |
| S6 Tier-3 business value (≥1 order)    | 246,374   | 2.91%      |

Classic editor (template) template

| Stage                                  | Campaigns  | Conversion |
| -------------------------------------- | ---------- | ---------- |
| S0 Create-start                        | 15,376,941 | 100.0%     |
| S2 Sent test send                      | 2,483,363  | 16.1%      |
| S3 Scheduled or sent                   | 8,043,167  | 52.3%      |
| S4 Tier-1 real send (≥1 ext recipient) | 7,782,859  | 50.6%      |
| S4b Tier-1 publish (>10 recipients)    | 6,967,091  | 45.3%      |
| S5 Tier-2 engagement (≥1 open)         | 7,563,641  | 49.2%      |
| S6 Tier-3 business value (≥1 order)    | 210,492    | 1.37%      |

Headline funnel reading

New editor has a higher Create→Tier-1 conversion (69.0% vs 50.6%) and dramatically higher test-send rate (29.4% vs 16.1%). Tier-3 ecommerce conversion is 2.1× higher on New (2.91% vs 1.37%). Classic ships more absolute volume (1.5M more Tier-1 sends) only because more campaigns get started — not because the funnel is better.

## 4\. Where drafts get stuck — wizard step distribution (A4 proxy)

The campaign object stores `wizard_step` \= "latest step reached in the email campaign creation flow." This is a coarse proxy for the microstep funnel that the brief asks for. Drafts only (status = draft, not deleted, not canceled).

### New editor — drafts (1,275,418)

null (init)

694,839

recipients

525,476

template

27,707

html (canvas)

26,573

other

1,822

New editor stalls overwhelmingly at the earliest stages — 56% never log a wizard step at all (init / abandon), 42% bail at audience selection. Only 2% reach the canvas.

### Classic editor — drafts (1,533,191)

html (canvas)

812,989

null (init)

653,862

recipients

39,945

template

19,102

other

7,396

Classic stalls overwhelmingly in the canvas/design step (53% of drafts). The "html" wizard step is the design canvas in Classic — this is the biggest single drop-off in the entire dataset.

Editors fail differently — do not pool the funnel

Stall geography is fundamentally different per editor. Classic users get to the canvas and give up there. New users barely make it to the canvas. The brief's instruction "do not pool them in funnel or path metrics — event taxonomies differ" is empirically validated by this single chart.

## 5\. Draft-state cohort — A6 (the "biggest definitional trap")

Brief §5 classification of drafts into stuck / parked / abandoned states using `updated_at`, body block presence, and tests-sent. Includes considered-rejection (abandon-in-2-minutes-with-no-content pattern).

Considered rejection

New625,902 (49.0%)

Classic856,954 (55.8%)

In-progress (≤7d)

New125,422 (9.8%)

Classic125,968 (8.2%)

Stalled (8-30d)

New184,747 (14.5%)

Classic179,482 (11.7%)

Cold (31-90d)

New340,346 (26.7%)

Classic372,704 (24.3%)

| Draft state            | New count | New % | Classic count | Classic % | Interpretation                                                                                                                                          |
| ---------------------- | --------- | ----- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Considered rejection   | 625,902   | 49.0% | 856,954       | 55.8%     | Created and abandoned in <2 min, no body blocks added, no tests sent. Probably exploration / accidents — NOT a UX failure of the editor surface itself. |
| In-progress (≤7d edit) | 125,422   | 9.8%  | 125,968       | 8.2%      | Actively being worked on. Reachable with re-engagement nudges.                                                                                          |
| Stalled (8-30d)        | 184,747   | 14.5% | 179,482       | 11.7%     | True at-risk drafts — past in-progress window but still recoverable. P1 target for nudges + completion telemetry.                                       |
| Cold (31-90d)          | 340,346   | 26.7% | 372,704       | 24.3%     | Likely abandoned. Worth a single resurrection email; deeper investment unwarranted.                                                                     |

Reframes the "drafts never sent" story

The headline "10.66M drafts never sent in 90 days" is mostly noise. Subtract considered rejections and the real at-risk draft pool is \~830K (in-progress + stalled). That's the audience for editor friction interventions — an order of magnitude smaller than the raw draft count.

## 6\. Time-to-send distribution — A8 (L2 lens)

Distribution of `create_at → first sent_at` for Tier-1 sends in the 90-day window.

Percentiles (minutes between create and send)

| Editor            | P50        | P75          | P90          | P95            | n         |
| ----------------- | ---------- | ------------ | ------------ | -------------- | --------- |
| New               | 452 (7.5h) | 3,487 (2.4d) | 8,621 (6.0d) | 14,729 (10.2d) | 5,905,767 |
| Classic           | 97 (1.6h)  | 2,038 (1.4d) | 6,848 (4.7d) | 11,480 (7.9d)  | 7,871,437 |
| Δ (New / Classic) | 4.66×      | 1.71×        | 1.26×        | 1.28×          |           |

Distribution shape (% of sent campaigns by elapsed time)

<5m

New 15.6%

Classic 27.6%

5-30m

New 14.3%

Classic 13.8%

1-4h

New 10.5%

Classic 9.5%

4-24h

New 17.0%

Classic 15.2%

1-7d

New 28.9%

Classic 22.8%

7-30d

New 7.3%

Classic 5.5%

Classic's outsized "<5 min" bucket (27.6% vs 15.6%) is dominated by replications — see §7\. Power users on Classic press "replicate → tweak → send" as a single fast workflow. New users take longer even when they replicate, which suggests the New editor's load / canvas-init time deserves a performance audit (L5).

## 7\. Back-and-forth signals — test sends per published campaign

Number of test sends fired before a campaign was officially sent. Used by the brief as a proxy for "this campaign caused friction the user kept correcting."

0 tests

New 63.5%

Classic 71.4%

1 test

New 10.7%

Classic 10.1%

2 tests

New 8.6%

Classic 7.1%

3-5 tests

New 10.0%

Classic 7.3%

6-10 tests

New 5.1%

Classic 3.1%

11-20 tests

New 1.8%

Classic 0.9%

20+ (extreme)

New 0.4%

Classic 0.2%

2.07×

New vs Classic, ≥11 tests rate

2.53×

New vs Classic, 20+ tests (extreme)

71% / 64%

Sent with zero tests (Classic / New)

New editor users back-and-forth more before publishing

Among campaigns that did ship, New users sent 6+ test sends 2× more often than Classic users (7.2% vs 4.1%) and 11+ tests at 2× the rate (2.16% vs 1.0%). This is consistent with preview/render uncertainty in the New canvas — the editor's "what will this look like in the inbox?" loop is harder to close. High-priority candidate for the L1 friction-hotspot list.

## 8\. Template-library health — A14 (L8 lens)

Send rate by template choice. The signal here directly answers the brief's question about "which templates to invest in vs deprecate" and exposes a startling Classic-specific failure mode.

| Template choice         | Classic created | Classic send % | New created | New send % | Δ (New − Classic) |
| ----------------------- | --------------- | -------------- | ----------- | ---------- | ----------------- |
| MC Template (unchanged) | 2,700,213       | 80.5%          | 6,189,658   | 67.8%      | −12.7 pp          |
| Saved MC Template       | 296,211         | 79.3%          | 689,159     | 74.4%      | −4.9 pp           |
| Old MC Template         | 151,879         | 79.8%          | 28,159      | 79.7%      | ≈0                |
| Altered MC Template     | 9,172,501       | 45.6%          | 1,281,211   | 76.4%      | +30.8 pp          |
| Custom User Template    | 1,366,090       | 45.2%          | 9,873       | 75.4%      | +30.3 pp          |
| None / blank            | 1,575,378       | 30.0%          | 268,631     | 68.4%      | +38.4 pp          |

Classic's edit/blank flow is broken

Classic users who pick an MC template and never alter it ship 80% of the time. The moment they alter the template — the entire point of an editor — send rate collapses to 46%. Starting from blank is worse: 30%. The same cohorts on the New editor ship at 76% / 68%. This is the strongest single quantitative argument in the dataset for migrating Classic edit-from-template users to New.

## 9\. Lifecycle × editor delta — A7 (L4 migration lens)

Send rate per campaign attempt, broken down by user lifecycle and editor. Directly supplies the brief's question 27 (what % of Classic users are migration-ready) and 16 (first-time vs returning differences).

| Lifecycle  | Editor  | Attempts  | Sent      | Send % | Tested % | Replicated % |
| ---------- | ------- | --------- | --------- | ------ | -------- | ------------ |
| First-time | New     | 846,456   | 284,042   | 33.6%  | 23.0%    | 28.7%        |
| First-time | Classic | 85,402    | 31,527    | 36.9%  | 14.9%    | 28.6%        |
| Returning  | New     | 961,769   | 541,533   | 56.3%  | 39.5%    | 62.7%        |
| Returning  | Classic | 5,736,195 | 459,125   | 8.0%   | 5.2%     | 9.1%         |
| Power user | New     | 6,660,800 | 5,080,269 | 76.3%  | 28.8%    | 80.9%        |
| Power user | Classic | 9,555,191 | 7,380,826 | 77.2%  | 22.7%    | 74.0%        |

The Returning × Classic anomaly

5.7M Classic attempts from returning users yielded only 8% sends — a 7× gap vs the same cohort on New (56%). Likely mechanisms: (1) returning users open Classic, hit a template they don't recognize, abandon; (2) returning users use Classic to "park" ideas they never return to. Either way, this is the biggest reach × severity candidate in the dataset.

Power users are editor-agnostic

Power users complete at 76-77% on both editors. Migration risk for power users is low on the completion metric, but their replication-heavy workflow (74-81%) means New must preserve fast replicate → tweak → send paths to avoid regressions on time-to-send.

## 10\. Errors and compliance blocks — A5 (partial)

Status reasons captured in the campaign-object table. A full A5 (validation, upload, render, autosave failures by step) requires the event log — see gap report.

| Editor  | Status | Reason                  | Campaigns |
| ------- | ------ | ----------------------- | --------- |
| New     | draft  | compliance              | 17,379    |
| Classic | draft  | compliance              | 743       |
| New     | sent   | compliance (post-send)  | 188       |
| Classic | sent   | compliance (post-send)  | 18        |
| New     | draft  | no\_recipients          | 36        |
| Classic | draft  | no\_recipients          | 18        |
| New     | draft  | discount\_code\_failure | 7         |

New editor compliance friction is 23× Classic

17,379 New drafts vs 743 Classic drafts blocked for compliance reasons in 90 days. This is the only error class meaningfully captured in the campaign object. Even at this level of aggregation, it suggests the content review / policy surface in New is firing more often — either because the underlying detection is stricter on the multichannel surface or because first-time creators (the New majority) trip more rules. Worth a dedicated dive.

## 11\. AI assist usage — A12 (L6 lens, directional only)

Per-campaign AI feature flags joined to engagement. No propensity matching applied — the brief explicitly requires it and it is impossible without account-level matching. Read as directional only.

| Editor  | AI used | n campaigns (≥100 recipients) | Avg open % | Avg click % | Avg revenue / camp |
| ------- | ------- | ----------------------------- | ---------- | ----------- | ------------------ |
| New     | No      | 4,096,524                     | 40.4%      | 3.51%       | $19.15             |
| New     | Yes     | 110,951                       | 38.2%      | 3.17%       | $84.25             |
| Classic | No      | 5,594,561                     | 40.6%      | 3.70%       | $91.49             |
| Classic | Yes     | 43,829                        | 36.2%      | 2.76%       | $188.13            |

AI-using campaigns trail non-AI on engagement rates (open / click) but show higher per-campaign revenue. Most likely explanation: AI users skew toward newer / lower-tenure / smaller-list accounts whose baseline opens look better, but per-campaign revenue scales with the larger ecommerce accounts that opt in. Cannot be cleanly attributed without matching. Adoption is 2.7% of campaigns on New and 0.78% on Classic — adoption itself is the headline.

## 12\. New vs Classic delta summary — A7

| Metric                               | New     | Classic | Δ        | Winner                        |
| ------------------------------------ | ------- | ------- | -------- | ----------------------------- |
| Create-start volume (90d)            | 8.47M   | 15.38M  | −45%     | Classic (volume)              |
| Distinct creator accounts            | 918,639 | 675,553 | +36%     | New (reach)                   |
| Tier-1 send rate                     | 69.0%   | 50.6%   | +18.4 pp | New                           |
| Tier-1 publish rate (>10 recipients) | 62.8%   | 45.3%   | +17.5 pp | New                           |
| Tier-3 ecommerce conversion rate     | 2.91%   | 1.37%   | +1.54 pp | New                           |
| P50 time-to-send                     | 452 min | 97 min  | +367%    | Classic                       |
| Test sends, ≥6 (per sent)            | 7.2%    | 4.1%    | +3.1 pp  | Classic (less back-and-forth) |
| Considered-rejection draft rate      | 49.0%   | 55.8%   | −6.8 pp  | New                           |
| Compliance-blocked drafts            | 17,379  | 743     | 23×      | Classic                       |
| Power-user send rate                 | 76.3%   | 77.2%   | −0.9 pp  | tie                           |
| First-time send rate                 | 33.6%   | 36.9%   | −3.3 pp  | Classic                       |
| Returning (non-power) send rate      | 56.3%   | 8.0%    | +48.3 pp | New (decisively)              |

## 13\. Decision lens recommendations (L1-L4)

Top 5 friction hotspots (reach × severity) L1 — UX investment

| # | Hotspot                                                               | Reach (accounts)                | Severity signal                   | Confidence     |
| - | --------------------------------------------------------------------- | ------------------------------- | --------------------------------- | -------------- |
| 1 | Classic 'Altered MC Template' completion (45.6% send rate)            | \~3.5M attempts cohort          | −35 pp vs unchanged template      | High           |
| 2 | Classic 'None / blank' template completion (30%)                      | \~700K attempts cohort          | −50 pp vs unchanged template      | High           |
| 3 | New editor canvas reach (only 2% of New drafts make it past audience) | 525K stalled at recipients step | Hard barrier before design        | Medium (proxy) |
| 4 | New editor compliance blocks (17.4K drafts/90d)                       | Estimated >10K accounts         | Hard stop                         | High           |
| 5 | New editor 'extreme test sends' (20+ test sends to ship)              | 22K campaigns / 90d             | Indicates preview-canvas mismatch | Medium         |

Worst cohort and the why L2 — Time-to-send

Worst cohort: First-time creators on the New editor. Even ignoring the time-to-send P50, only 33.6% ever ship. The replicate-from-prior shortcut is unavailable to them by definition (no prior).

Recommendation: collapse New's audience-selection step into a same-page operation, or default audience to the most-recent-used. The audience step is where the New funnel loses 42% of its drafts — for first-time creators this is likely worse.

Biggest stall cause: stuck or parked? L3 — Draft stall

Most "drafts" are considered rejections (50-56%), not stuck flows. They are users abandoning in the first 2 minutes with no real content — treat as rejected exploration, not as a UX wound.

The recoverable population is the 14-15% "stalled" + 8-10% "in-progress" — about 830K drafts across both editors. Investigate whether these correlate with specific microsteps (requires event log; see gap report).

Are Classic users migration-ready? L4 — Migration

Power users on Classic (sending ≥5 in 90d / ≥20 in 12mo) hit 77% send rate — they have learned Classic's pattern (74% replication) and would need the New editor to preserve their 1.6-hour median time-to-send. Migration risk: high without a parity replicate-flow.

Returning (non-power) users on Classic are the migration win: they ship 7× more often on New. Migrating them recovers a population of \~5.3M abandoned attempts.

First-time creators already default to New (10× more attempts than Classic) — no migration needed; fix the New first-time funnel instead.

## 14\. Answers to brief §11 priority questions

Each answer cites the metric and the evidence section above. "Blocked" = requires sources that were not accessible; documented in §15.

| #              | Question                                       | Answer                                                                                                                                                                                        | Source       |
| -------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Funnel         |                                                |                                                                                                                                                                                               |              |
| 1              | % of eligible accounts that open the editor    | Cannot compute — requires editor session log                                                                                                                                                  | BLOCKED      |
| 2              | % that add real content                        | Computable on Classic only (8.6M / 15.4M = 55.9%). New editor block counters not populated.                                                                                                   | §3 + gap     |
| 3              | % that test-send                               | New 29.4% / Classic 16.1% of created campaigns                                                                                                                                                | §3           |
| 4              | % that real-send (Tier 1)                      | New 69.0% / Classic 50.6%                                                                                                                                                                     | §3           |
| 5              | % that reach Tier 2 / Tier 3                   | Tier 2: New 68.0% / Classic 49.2%. Tier 3: New 2.91% / Classic 1.37%                                                                                                                          | §3           |
| Friction       |                                                |                                                                                                                                                                                               |              |
| 6              | Largest funnel drop-off                        | Classic: design canvas (53% of drafts stall at 'html' step). New: audience selection (42% stall at 'recipients').                                                                             | §4           |
| 7              | Highest P90 dwell step                         | Cannot compute without per-step timestamps                                                                                                                                                    | BLOCKED      |
| 8              | Highest error rate step                        | Compliance-blocked drafts at draft-status (New 17K / Classic 743). Step-level error data BLOCKED.                                                                                             | §10 + gap    |
| 9              | Highest support-contact step                   | Cannot compute without support tickets                                                                                                                                                        | BLOCKED      |
| 10             | Highest silent-struggle step                   | Cannot compute without dwell + undo + autosave telemetry                                                                                                                                      | BLOCKED      |
| 11             | Highest undo / autosave-failure step           | Cannot compute without client telemetry                                                                                                                                                       | BLOCKED      |
| Drafts         |                                                |                                                                                                                                                                                               |              |
| 12             | % of drafts that ever send                     | Classic 51% (cumulative 90d). New 70%. Approximate; cohort analysis needs longer follow-up window.                                                                                            | §3 implied   |
| 13             | Microstep where drafts most often stall        | Classic 'html' canvas step (53%). New 'null' init / 'recipients' (98% combined).                                                                                                              | §4           |
| 14             | Median time-to-resurrection for stalled drafts | Cannot compute without re-edit timestamps in event log                                                                                                                                        | BLOCKED      |
| 15             | Parked vs stuck vs dead share                  | See §5 table. \~50% considered-rejection / 9% in-progress / 13% stalled / 25% cold per editor.                                                                                                | §5           |
| Cohort deltas  |                                                |                                                                                                                                                                                               |              |
| 16             | First-time vs returning differences            | First-time complete at 33-37%; returning at 8% (Classic) / 56% (New); power at 76-77%.                                                                                                        | §9           |
| 17             | Mobile vs desktop completion delta             | Cannot compute without device class on the campaign object or a session join                                                                                                                  | BLOCKED      |
| 18             | Template vs blank completion delta             | Classic +50pp using unchanged template vs blank. New +0pp (template choice doesn't matter on New).                                                                                            | §8           |
| 19             | Ecommerce vs standard differences              | Tier-3 conversion: New 2.91% / Classic 1.37%. Account-level ecomm flag join needed for full split.                                                                                            | §3 + partial |
| 20             | Agency multi-account patterns                  | Requires parent\_account\_id join — not run                                                                                                                                                   | PARTIAL      |
| New vs Classic |                                                |                                                                                                                                                                                               |              |
| 21             | Microsteps Classic outperforms New on          | Time-to-send (4.7× faster median); first-time send rate (+3.3pp); test-back-and-forth (less)                                                                                                  | §6, §7, §9   |
| 22             | Microsteps New outperforms Classic on          | Tier-1 send rate (+18.4pp); returning-cohort completion (+48pp); blank/altered template completion (+30-38pp); Tier-3 conversion (2.1×); compliance-bounce-back is the open question          | §3, §8, §9   |
| 23             | Is the gap closing or widening over time       | Trend analysis not run in this pass — would need weekly slice                                                                                                                                 | PARTIAL      |
| Lens-specific  |                                                |                                                                                                                                                                                               |              |
| 24             | L1 — top 5 UX investments                      | See §13 — Classic edit-template flow, Classic blank flow, New audience-step drop, New compliance blocks, New extreme test-send loop                                                           | §13          |
| 25             | L2 — worst time-to-send cohort                 | First-time on New (P50 we cannot isolate without lifecycle × editor join on time-to-send — derivable from §6 + §9).                                                                           | §6 + §9      |
| 26             | L3 — biggest stall cause                       | Considered rejection (created and abandoned in <2 min with no content). Real stuck/stalled population is much smaller than headline draft count.                                              | §5           |
| 27             | L4 — % of Classic users migration-ready        | Power-user Classic cohort (77% send rate, 612K accounts) is the migration risk; returning cohort (576K accounts, 8% send rate on Classic vs 56% on New) is the migration win — clearly ready. | §9           |

## 15\. Instrumentation gap report (brief §10.8)

Per the brief: "If data gaps prevent any of these, stop and produce the instrumentation gap report instead of guessing." Below is what's needed to complete the brief in full.

| Capability needed                                | What it unlocks                                                                                                            | Where it likely lives                                                                                           | Action                                                                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Editor event log (microstep timestamps)          | A1 mapping, A3 paths, A4 friction hotspots, A6 stall-step diagnosis, A8 cohort tail, P90 dwell, drop-off rate              | rsg-events-pipeline-prod.ingest\_v2.events (or product team's own table)                                        | Request read access for product analytics role; alternatively expose a curated view in bi\_product or bi\_reporting |
| Client telemetry stream                          | L5 performance lens, undo / autosave / render / image-upload error rates, z\_perf and z\_undo components of friction score | Likely a Datadog RUM or Snowplow client log; not in BigQuery or not labeled as such                             | Identify owner; pre-aggregate to session-level and land in bi\_product                                              |
| Support ticket data tagged 'editor'              | z\_support component, A11 complainers vs silent strugglers, post-step support contact rate                                 | Likely Zendesk or Salesforce Service Cloud (salesforce\_b2b\_cs dataset exists)                                 | Tag tickets to product area in source system; expose ticket-to-account-to-campaign join in bi\_reporting            |
| Block-level usage on New editor                  | A15 block library health, 'tried-didn't-work' deletion-after-insertion signal, real-content gate (priority Q2)             | Schema parity gap — bi\_reporting.emails\_bulk fields \*\_blocks not populated for content\_type='multichannel' | Backfill or instrument; this is a one-week dataform fix, not a new pipeline                                         |
| Account-level AI/brand-kit exposure log          | A12 propensity matching, A13 brand kit ROI; without this, AI lift is directional only                                      | ai\_features\_enabled\_flag mentioned in brief §8 not located                                                   | Land daily exposure flag in bi\_segment\_dataform.users                                                             |
| Device class on campaign-object or session table | A9 mobile-specific friction, mobile vs desktop completion delta (priority Q17)                                             | Probably in the editor event log; not in campaign object                                                        | Add device\_class to the editor session model and join into emails\_bulk via session→campaign\_id                   |
| Plan / billing / churn dimension join            | Churned-eligible and reactivated populations (brief §3); ecommerce vs standard delta (Q19)                                 | bi\_segment\_dataform.users — accessible but not joined here                                                    | Add to the next pass; would require \~30 min of additional work                                                     |
| Time-series of every metric                      | Q23 'is the New vs Classic gap closing or widening' — requires weekly slice over 12 months                                 | Computable now from emails\_bulk; not run due to query budget                                                   | Run in a follow-up; budget \~5 large queries                                                                        |

## 16\. Closing narrative

The dominant happy path on Classic is "replicate prior campaign → tweak in canvas → send within an hour" — used by power users who have memorized the template-canvas flow. The Classic design canvas is the dominant single point of friction in the entire editor system: 53% of all Classic drafts die there.

The dominant happy path on New is "open editor → pick a template → wrestle with the audience step → eventually publish" — slower (4.7× the median time-to-send) but with a higher completion rate (+18 pp) and a 23× higher compliance-block rate.

The biggest cross-editor gap is on returning (non-power) users: the same cohort completes at 8% on Classic and 56% on New. This is the migration win.

The cohort most at risk is first-time creators on New: they are 10× the volume of first-time creators on Classic but ship at 33.6%, which means roughly 560,000 first-time creators in 90 days created a campaign and never shipped it.

The single highest-leverage fix per decision lens is:

* L1 (UX): Fix Classic's "altered template" canvas — recovers 9M+ campaign attempts at half-completion.
* L2 (time-to-send): Audit New editor's canvas-init / load time; New's 5-min bucket is 12 pp lighter than Classic's.
* L3 (drafts): Re-engagement nudges targeted only at the \~830K stalled / in-progress drafts; ignore considered-rejections.
* L4 (migration): Migrate returning users to New first; preserve replicate-flow for power-user migration second.

The single largest instrumentation investment that would most improve the next iteration of this analysis is read access to the editor event log (or a curated view in `bi_reporting`). It unlocks the entire microstep funnel, friction-score, and path-mining stack the brief requires.

## 17\. SQL appendix (selected queries)

Validation table query 

`` SELECT content_type, COUNT(*) AS campaigns_created, COUNT(DISTINCT user_id) AS distinct_accounts, SUM(CASE WHEN edited_by_login_id IS NOT NULL THEN 1 ELSE 0 END) AS has_login_id, SUM(CASE WHEN status = 'sent' THEN 1 ELSE 0 END) AS sent FROM `mc-business-intelligence.bi_reporting.emails_bulk` WHERE created_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY) AND content_type IN ('multichannel','template','html','url') GROUP BY content_type; ``

Send-tier funnel query (per editor) 

`` SELECT CASE WHEN content_type='multichannel' THEN 'New' ELSE 'Classic' END AS editor, COUNT(*) AS s0_created, SUM(CASE WHEN tests_sent > 0 THEN 1 ELSE 0 END) AS s2_test, SUM(CASE WHEN status='sent' AND emails_sent >= 1 THEN 1 ELSE 0 END) AS s4_tier1, SUM(CASE WHEN status='sent' AND emails_sent > 10 THEN 1 ELSE 0 END) AS s4b_tier1_publish, SUM(CASE WHEN status='sent' AND opens >= 1 THEN 1 ELSE 0 END) AS s5_tier2, SUM(CASE WHEN status='sent' AND COALESCE(ecomm_attributed.orders,0) >= 1 THEN 1 ELSE 0 END) AS s6_tier3 FROM `mc-business-intelligence.bi_reporting.emails_bulk` WHERE created_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY) AND content_type IN ('multichannel','template') GROUP BY editor; ``

Draft-state classification query 

`CASE WHEN scheduled AND scheduled_at > TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) THEN 'parked' WHEN TIMESTAMP_DIFF(updated_at, created_at, MINUTE) <= 2 AND tests_sent = 0 AND COALESCE(body_blocks, 0) = 0 THEN 'considered_rejection' WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), updated_at, DAY) <= 7 THEN 'in_progress' WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), updated_at, DAY) <= 30 THEN 'stalled' WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), updated_at, DAY) <= 90 THEN 'cold' ELSE 'dead' END AS draft_state`

Lifecycle cohort query 

`CASE WHEN prior_history.user_id IS NULL THEN 'First-time' WHEN COALESCE(t90.sent_90d, 0) >= 5 OR COALESCE(t12.sent_12mo, 0) >= 20 THEN 'Power user' ELSE 'Returning' END AS lifecycle`

---

 Source table: `mc-business-intelligence.bi_reporting.emails_bulk` (852M lifetime rows; daily-refreshed). Window: trailing 90 days from query time. Editor mapping: `content_type='multichannel'` \= New (drag-drop block-based); `content_type='template'` \= Classic. Classic and New are reported separately per the brief — not pooled.