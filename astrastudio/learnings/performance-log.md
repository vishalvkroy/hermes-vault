# Astra Studio — Performance Log

Append-only. Format: piece -> metric -> "worked / flat / failed" -> why (with evidence). Populated
by research crons per the growth-strategy skill's performance loop (Section 3) — reviewed every
run before writing new findings. As of 2026-09-24 (strategy.md creation): no campaign has completed
the approval -> publish -> analytics loop yet (all 3 LinkedIn drafts — 2026-09-05 GST cess,
2026-09-06 crash reporting, 2026-09-24 indexing fix — show "Pending" outcome in their plan.md
files). First real entries land once Vishal approves a draft and `get_post_analytics` returns data.

## 2026-10-01 review

- **2026-09-05 GST cess precision** (LinkedIn, published 2026-09-17) → `get_post_analytics` still
  `collected: false`; `get_campaign_performance` totals 0 impressions/engagement/clicks after 2
  weeks live. `linkedin_fetch_post` on the real post confirms 0 likes/comments/shares. Flat - no
  real reach yet on this account (author has no visible follower count on profile, brand-new
  posting history).
- **2026-09-06 invisible crashes** (LinkedIn, published 2026-09-17) → same picture: analytics not
  collected, 0 engagement via direct post fetch.
- **2026-09-24 indexing bug fix** (LinkedIn) → post status is `failed` in the social DB
  (`get_post` shows `status: "failed"`) despite a `published_at` timestamp and a real
  `provider_post_id`; the post genuinely exists on LinkedIn (`linkedin_fetch_post` confirms live,
  0 likes/comments 6 days on). Flag for Vishal: publish pipeline is marking a post that did reach
  LinkedIn as "failed" in our own tracking - a tooling bug worth a look, not a content failure.
- **2026-09-25 Instagram GST split carousel** → `get_post_analytics` `collected: false`;
  `get_campaign_performance` totals 0. Account is brand-new (4 followers at launch per its plan.md)
  so near-zero reach is expected this early, not yet a verdict on the content/angle.
- **Pattern so far:** every published LinkedIn post this month shows 0 real engagement at the
  numbers we can actually pull (direct LinkedIn fetch, not just our own analytics collector).
  Not enough posts yet to call the channel itself failed, but worth naming: our LinkedIn account
  has no visible audience being reported anywhere in these fetches. Don't manufacture false
  urgency from zero-data posts - note it, keep posting consistently (3+ data points needed before
  reading a channel-level trend), and separately flag the "failed" tracking-status bug for
  Vishal to check (not a content/strategy issue).

## 2026-10-09 review

- **2026-10-01 Loan Readiness "Zero score" post** (LinkedIn, `campaigns/2026-10-01-loan-readiness-
  zero-score/`) → published 2026-10-02 (`linkedin_fetch_post` confirms live, post urn
  `7511275407665455104`), real text confirmed matches the draft. 7 days live: `numLikes: 0,
  numComments: 0, numShares: 0` via direct `linkedin_fetch_post`; `get_post_analytics` still
  `collected: false`; `get_campaign_performance` totals 0 impressions/engagement/clicks. Flat -
  same zero-reach pattern as every prior post, now 5/5 LinkedIn+Instagram posts this account has
  ever made.
- **2026-10-01 "9 out of 100" indexing-bug post** (LinkedIn, published 2026-09-25, not 2026-09-17
  as read from the 2026-10-01 log - corrected date from direct fetch) → 2 weeks live, still
  `numLikes: 0, numComments: 0, numShares: 0`. Flat.
- **2026-10-01 and 2026-10-03 blog posts** (business-credit-score-loan-readiness,
  business-website-cost-india-2026) → checked via `gsc_search_analytics` filtered to each page
  URL, 2026-09-25 to 2026-10-09. Neither URL appears anywhere in GSC's query/page rows for this
  window - zero impressions, zero clicks recorded for either post yet. Too early to call failed
  (GSC indexing lag is normal, especially with the "9 out of 100 pages indexed" bug from last
  month still a live risk) but genuinely flat right now, not growing.
- **Pattern, now 6 weeks of data:** every single published post on this account (6 LinkedIn + 1
  Instagram across Sep-Oct) shows zero real engagement and zero attributable search traffic so
  far. This is now a real signal, not noise - worth stating plainly in strategy.md rather than
  waiting for a 7th zero. Most likely cause given what's checkable: the LinkedIn profile itself
  has no visible follower count in any fetch (not a content-quality problem, a distribution-zero
  problem) - a founder posting into an audience of near-zero followers will show 0 engagement
  regardless of post quality. Not acted on with a pillar change yet (needs explicit evidence the
  cause is audience size, not content), but flagged in this week's strategy review as the
  single most important unresolved question for the channel.

## 2026-10-12 review

- **2026-10-10 WhatsApp consent-gap-fix LinkedIn post** (campaigns/2026-10-10-whatsapp-consent-
  gap-fix/) → confirmed live via direct `linkedin_fetch_post`: text matches the draft exactly,
  `numLikes: 0, numComments: 0, numShares: 0`, `authorFollowers: null` (still no follower count
  surfaced in any fetch). 2 days live - too early to call, but extends the zero-engagement run to
  8/8 published pieces since late September.
- **2026-10-01 Loan Readiness "Zero score" post** → re-checked, still `numLikes: 0, numComments: 0,
  numShares: 0` 10 days live. `get_campaign_performance` totals still 0 impressions/engagement/
  clicks. Flat.
- **2026-10-03 and 2026-10-10 GST e-invoicing / dead-stock blog posts** → `gsc_search_analytics`
  (28-day window, dimensions page) shows neither `gst-e-invoicing-guide-india-2026` nor
  `dead-stock-inventory-management-india-2026` in the page-level rows yet - zero impressions,
  zero clicks recorded. Both published 2026-10-10, 2 days old; too early to score, consistent with
  the site's standing indexing-lag pattern, rechecking next run.
- **Instagram** → `INSTAGRAM_GET_USER_INSIGHTS` (reach, daily): 0 on 2026-10-10, 1 on 2026-10-11.
  First non-zero reach number since tracking started, but 1 unique view is not yet a signal -
  noting it rather than reading a trend into it.

## 2026-10-15 review

- **2026-10-10 WhatsApp consent-gap-fix LinkedIn post** (campaigns/2026-10-10-whatsapp-consent-
  gap-fix/, post id `1f24574d-3df1-4c5c-8fdb-d5b47a50130e`) → still `status: pending_approval` in
  the social DB, `provider_post_id: null`, `published_at: null`. This post has **not actually
  gone out** - it has sat in pending_approval for 5 days. Correcting last run's "8/8 published"
  count: the real published-post tally stays at 7 (6 LinkedIn + 1 Instagram), not 8. This is an
  approvals-bottleneck finding, not an engagement one - flagging directly to Vishal rather than
  quietly treating it as a flat zero-engagement data point, which it isn't (it was never
  published, so there's nothing to measure yet).
- **2026-10-01 Loan Readiness "Zero score" post** (urn `7511275407665455104`) → re-checked via
  direct `linkedin_fetch_post`, still live, still `numLikes: 0, numComments: 0, numShares: 0`,
  `authorFollowers: null`, 13 days live. Flat, consistent with every prior check.
- **GSC page-level data, 7-day and 28-day windows** → `gst-e-invoicing-guide-india-2026` now
  shows 1 click/8 impressions (28-day) - first non-zero row since publish (2026-10-10), 5 days
  in. `dead-stock-inventory-management-india-2026` still 0 clicks/5 impressions, unchanged.
  `business-website-cost-india-2026` and `business-credit-score-loan-readiness` both still flat
  (0 clicks, low single-digit-to-20s impressions) after 2 and 2.5 weeks respectively - genuinely
  not growing, not just early.
- **Repo/code-shipped-but-unmarketed check (this run's new addition per the cron instructions):**
  10 substantial commits shipped 2026-10-12 to 2026-10-15 (platform dashboard tabs, tenant
  soft-delete+audit-log, trial-expiry revenue-leak fix, scheduled-report delivery fix, premium
  report charts across 7 report types, Atlas AI promoted to its own nav group, is_internal_test
  tenant safety flag) - see this week's research file for the full list. None of these are
  customer-facing SMB-marketing material (platform-admin/internal-tooling, or desktop-UX polish
  already covered by the existing "Intelligence > Billing" pillar) except the Atlas AI nav
  promotion, which is a real, small, demo-able "we made our own differentiator easier to find"
  beat - queued as light-weight future material, not this week's lead.
- **Pattern, now 8 weeks of data since late Sep:** 7 real published pieces (6 LinkedIn + 1
  Instagram) all show 0 real engagement at the numbers directly checkable via
  `linkedin_fetch_post`/`INSTAGRAM_GET_USER_INSIGHTS`; `authorFollowers` has never once returned a
  number across every fetch this run and every prior run. Combined with this run's discovery that
  the most recent post never actually published (stuck in pending_approval 5 days), the real,
  actionable finding this week is a **process** gap, not a content gap: posts are being drafted
  and approval-requested correctly, but something is stalling between request_publish_approval and
  Vishal clicking Approve, or between Approve and the publisher job actually firing. Worth a direct
  check with Vishal on whether the 2026-10-10 approval request was ever seen.

## 2026-10-19 review

- **2026-10-10 WhatsApp consent-gap-fix LinkedIn post** (post id `1f24574d-3df1-4c5c-8fdb-
  d5b47a50130e`) → re-checked via `get_post`, still `status: "pending_approval"`,
  `provider_post_id: null`, `published_at: null`. 9 days in pending_approval now, no change since
  the 2026-10-15 flag. Still a published-post count of 7 (6 LinkedIn + 1 Instagram), not 8. The
  approvals-pipeline stall raised last run has not resolved - repeating the flag to Vishal rather
  than letting it go stale silently.
- **2026-10-01 Loan Readiness "Zero score" post** (urn `7511275407665455104`) → re-checked via
  direct `linkedin_fetch_post`: still live, still `numLikes: 0, numComments: 0, numShares: 0`,
  `authorFollowers: null`, now 17 days live. Flat, consistent with every prior check - 9th
  consecutive zero-engagement check on this single post.
- **2026-09-24 indexing-bug-fix post** (urn `7508747457233723392`) → re-checked, still
  `numLikes: 0, numComments: 0, numShares: 0` via direct fetch, 25 days live. Flat.
- **GSC page-level data (28-day window)** → `gst-e-invoicing-guide-india-2026` now shows 3
  clicks/490 impressions (up from 1/8 at the 2026-10-15 check) - real, continuing growth on this
  blog post, the strongest page-level movement of any post tracked this cycle.
  `business-website-cost-india-2026` still 0 clicks/56 impressions (18 days since publish - now
  genuinely flat, not early). `business-credit-score-loan-readiness` still 0 clicks/7 impressions
  (18 days). `dead-stock-inventory-management-india-2026` still 0 clicks/36 impressions (9 days -
  still within normal indexing-lag window). `/tools/hsn-code/2106` remains the highest-impression
  non-homepage URL (1,149 impressions/2 clicks, 28d) - the "found, not clicked" CTR-fix opportunity
  flagged in multiple prior snapshots remains open and unactioned.
- **Repo/code-shipped check (this run, per cron instructions):** `git log origin/main --since
  '7 days ago'` shows 6 commits (2026-10-18 to 2026-10-19 00:12 IST): Zoho comparison page + 3
  Industry Pack landing pages + trust-signal strip + internal linking audit (2026-10-18); hid
  Astra Spark from all public discovery surfaces, sitemap and robots.txt (2026-10-18); gated 9
  previously-free-on-every-plan modules including the flagship AI differentiators (Money Leaks,
  Loan Readiness/`gst_risk_score`, Growth Opportunities) to GROWTH+ plan (2026-10-18); 2 new
  Growth-Opportunities detection kinds, margin-optimization and promo-timing (2026-10-18, NOT
  verified against a live Postgres run - test DB was down); fixed a real production bug where
  paying GROWTH/PRO tenants showed as still "TRIAL" in the admin panel because `tenant_state`
  was never promoted on activation, backfilled 2 affected real tenants (2026-10-18); shipped
  Services & Retainers (service line items that skip stock tracking, bill GST with SAC in the HSN
  field, new `/service-business-software` landing page) (2026-10-19 00:12 IST). See this week's
  research file for the full writeup and which of these is this week's lead opportunity.
- **Pattern, now 9+ weeks of data since late Sep:** still 7 published pieces, still 0 real
  engagement on every one directly checkable via `linkedin_fetch_post`. The one genuinely new
  movement this cycle is the GSTR-1/3B export architecture question raised 2026-10-15 (Experiment
  #5, "verify before claiming filing depth") - this run's codebase check (below, see research file)
  resolves that verification step with a real answer, not a guess.
