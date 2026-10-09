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
