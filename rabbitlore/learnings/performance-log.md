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
