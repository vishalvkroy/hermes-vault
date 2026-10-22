# RabbitLore — Performance Log

Append-only. Each research cron run reviews what went out since the last run (blog/social posts)
and logs: piece -> metric -> worked/flat/failed -> why. Feeds back into strategy.md (§9 Review
log) per the growth-strategy skill's feedback loop.

## 2026-09-28 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384` (2026-09-06 campaign, "blend/holes/
  night-gate" build-in-public post). **Metric:** `get_post_analytics` → HTTP 500 from the analytics
  backend this run (previously `collected: false`). **Status: unknown — not measurable yet.**
  Why: analytics collection for this post still hasn't landed two runs in a row (checked
  2026-09-24 and again today); not a "failed" post, just no engagement data exists to judge it
  by. No action from this alone — keep checking, don't drop the LinkedIn cadence over it.
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc` (same campaign, second post).
  **Metric:** `get_post_analytics` → `collected: false`. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → `post_count: 2, posts_published: 1, totals: {impressions: 0, engagement: 0, clicks: 0}`.
  Reads as "no data yet," not "zero engagement," given the per-post 500/`collected:false` above.
- **Piece:** `2026-09-24-reddit-night-gated-lore-launch` (Reddit draft). **Status:** still not
  posted by Vishal as of this run (manual-only channel, no confirmation) — nothing to measure.
- **No blog URLs published for RabbitLore this cycle** (no GSC site connection exists to check
  against — RabbitLore isn't a Search Console property, see `gsc_list_sites` in this run).

## 2026-10-01 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (3rd consecutive run: 2026-09-24, 2026-09-28, 2026-10-01). **Status: unknown —
  still not measurable.** This is now a 3-run pattern, not a one-off blip — worth flagging to
  Vishal that the analytics backend for this post specifically has never once returned data since
  publication; may need a manual check outside this loop rather than continued re-checking.
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 3rd run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as last 2 runs (`post_count: 2, posts_published: 1, impressions: 0, engagement: 0,
  clicks: 0`) — still reads as "no data yet."
- **Piece:** `2026-09-24-reddit-night-gated-lore-launch` (Reddit draft). **Status:** still not
  posted by Vishal as of this run — nothing to measure, unchanged.
- **No blog URLs published for RabbitLore this cycle** (still no GSC site connection).

## 2026-10-10 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (4th consecutive run: 2026-09-24, 2026-09-28, 2026-10-01, 2026-10-10). **Status:
  unknown — still not measurable.** 4-run pattern now; repeating prior flag to Vishal this needs a
  manual check outside the automated loop — the backend has never once returned data for this post.
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 4th run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as every prior run (`post_count: 2, posts_published: 1, impressions: 0, engagement:
  0, clicks: 0`) — still reads as "no data yet," not "failed."
- **Piece:** `2026-09-24-reddit-night-gated-lore-launch` and `2026-10-01-reddit-regulatory-
  structural-safety` (both Reddit drafts). **Status:** still not posted by Vishal as of this run —
  Reddit remains manual-only for this brand (`connect_status` re-checked this run: reddit
  `connected: false`), nothing to measure on either.
- **No blog URLs published for RabbitLore this cycle** (`gsc_list_sites` re-checked — only
  madebyher.in and astrastudio.in listed, RabbitLore still not a Search Console property).
- **GA4:** RabbitLore Android streams in property 538401917 re-checked — still **no app
  analytics data**, per analytics-map 2026-09-25. Reporting the null, not inventing a number.

## 2026-10-12 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (5th consecutive run: 2026-09-24, 2026-09-28, 2026-10-01, 2026-10-10, 2026-10-12).
  **Status: unknown — still not measurable.** 5-run pattern, repeating standing flag — this needs
  Vishal's manual check outside the automated loop, the backend has never once returned data.
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 5th run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as every prior run (`post_count: 2, posts_published: 1, impressions: 0, engagement:
  0, clicks: 0`) — still reads as "no data yet," not "failed."
- **Piece:** `2026-10-10-reddit-teen-migration-hard-numbers` (new Reddit draft from last run,
  intended to supersede `2026-10-01-reddit-regulatory-structural-safety`). **Status:** not posted
  by Vishal as of this run — `connect_status` re-checked, reddit `connected: false`, unchanged.
  3 Reddit drafts now sit unposted (`2026-09-24`, `2026-10-01`, `2026-10-10`) — nothing to measure
  on any of them; flagging again that the backlog itself, not draft quality, is the open item.
- **No blog URLs published for RabbitLore this cycle** (`gsc_list_sites` re-checked — only
  madebyher.in and astrastudio.in listed, RabbitLore still not a Search Console property).

## 2026-10-15 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (6th consecutive run: 2026-09-24, 2026-09-28, 2026-10-01, 2026-10-10, 2026-10-12,
  2026-10-15). **Status: unknown — still not measurable.** 6-run pattern now, repeating standing
  flag — backend has never once returned data for this post since publication (2026-09-06).
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 6th run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as every prior run (`post_count: 2, posts_published: 1, impressions: 0, engagement:
  0, clicks: 0`) — still reads as "no data yet," not "failed."
- **Reddit:** `connect_status` re-checked — reddit `connected: false`, unchanged. 3 Reddit drafts
  (`2026-09-24`, `2026-10-01`, `2026-10-10`) still sit unposted — nothing to measure on any of
  them.
- **No blog URLs published for RabbitLore this cycle** (`gsc_list_sites` re-checked — only
  madebyher.in and astrastudio.in listed, RabbitLore still not a Search Console property).
- **GA4:** RabbitLore Android streams in property 538401917 — still **no app analytics data**,
  per the verified analytics map. Reporting the null, not inventing a number.

## 2026-10-19 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (7th consecutive run: 2026-09-24, 2026-09-28, 2026-10-01, 2026-10-10, 2026-10-12,
  2026-10-15, 2026-10-19). **Status: unknown — still not measurable.** 7-run pattern now, backend
  has never once returned data for this post since publication (2026-09-06).
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 7th run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as every prior run (`post_count: 2, posts_published: 1, totals: {impressions: 0,
  engagement: 0, clicks: 0}`) — still reads as "no data yet," not "failed."
- **Reddit:** `connect_status` re-checked — reddit `connected: false`, unchanged. 3 Reddit drafts
  (`2026-09-24`, `2026-10-01`, `2026-10-10`) still sit unposted — nothing to measure on any of
  them.
- **No blog URLs published for RabbitLore this cycle** (`gsc_list_sites` re-checked — only
  madebyher.in and astrastudio.in listed, RabbitLore still not a Search Console property).
- **GA4:** RabbitLore Android streams in property 538401917 — still **no app analytics data**,
  per the verified analytics map. Reporting the null, not inventing a number.

## 2026-10-22 review

- **Piece:** LinkedIn post `urn:li:share:7502315073433104384`. **Metric:** `get_post_analytics` →
  HTTP 500 again (8th consecutive run: 2026-09-24, 2026-09-28, 2026-10-01, 2026-10-10, 2026-10-12,
  2026-10-15, 2026-10-19, 2026-10-22). **Status: unknown — still not measurable.** 8-run pattern
  now, backend has never once returned data for this post since publication (2026-09-06).
- **Piece:** LinkedIn draft `115d7a8b-523a-4f71-8995-064b780458cc`. **Metric:** `collected: false`,
  unchanged, 8th run in a row. **Status: unknown**, same reason.
- **Campaign-level:** `get_campaign_performance` for `2026-09-06-linkedin-blend-holes-night-gate`
  → same zeros as every prior run (`post_count: 2, posts_published: 1, totals: {impressions: 0,
  engagement: 0, clicks: 0}`) — still reads as "no data yet," not "failed."
- **Reddit:** `connect_status` re-checked — reddit `connected: false`, unchanged. 3 Reddit drafts
  (`2026-09-24`, `2026-10-01`, `2026-10-10`) still sit unposted — nothing to measure on any of
  them.
- **No blog URLs published for RabbitLore this cycle** (`gsc_list_sites` re-checked — only
  madebyher.in and astrastudio.in listed, RabbitLore still not a Search Console property).
- **GA4:** `ga4_traffic_summary` attempted for RabbitLore's Android stream in property 538401917
  this run — failed on a call-shape error (string property_id required, integer passed), a
  mechanical failure, not new evidence. Standing read unchanged: **no app analytics data** for
  RabbitLore per the verified analytics map. Reporting the null, not inventing a number.
