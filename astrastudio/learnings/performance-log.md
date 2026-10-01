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
