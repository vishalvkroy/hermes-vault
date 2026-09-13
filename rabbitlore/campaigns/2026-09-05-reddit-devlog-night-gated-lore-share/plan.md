# Campaign: 2026-09-05-reddit-devlog-night-gated-lore-share

- **Campaign ID:** 2026-09-05-reddit-devlog-night-gated-lore-share
- **Timestamp:** 2026-09-05T07:00Z
- **Status:** drafted
- **Grounding note:** No research file exists yet in `rabbitlore/research/` (directory is empty — the
  weekly research cron hasn't run for this brand). Per the campaign-workflow rule, this campaign is
  NOT built on invented market signals. It's grounded instead in (a) the brand's static identity
  (avatars, customization, community, Gen Z audience) and (b) real, verifiable shipped features
  pulled from `git log` in the wired repos — actual product events, not fabricated ones:
  - Mobile: night-gated lore-share (11pm-4am IST) in rooms/DMs, gravitational "blend" collision
    canvas driven by match %, "holes" (tap to see who fell in), constellation star-map for logged
    lore, realtime like/notification sweep.
  - Backend: `getBlend` real collision detection (overlapping lores by category+tag), `getLikers`
    (who fell into a hole, public, capped 100), curiosity ranker fix (For You feed was silently
    dead — 29-dim vector vs 21 gates checked), user blocking system, Play Store child-safety page.
  Recommend the actual research cron run before next cycle so future campaigns react to real
  market/competitor findings instead of repo activity alone.
- **Objective:** Build authentic Reddit presence for RabbitLore ahead of any paid or growth push —
  per spec section 12, this brand grows through genuine community contribution, not campaigns that
  look like ads.
- **Hypothesis:** Gen Z / indie-app / journaling-adjacent Reddit communities respond to specific,
  behind-the-scenes product detail (a real bug fix, a real design choice, a screenshot) far better
  than generic app-promo copy. The night-gated lore-share feature and the "holes" mechanic are
  distinctive enough to earn genuine discussion rather than get flagged as promo.
- **Target audience:** Gen Z users active in app-design / indie-dev / late-night-journaling-adjacent
  Reddit communities (e.g. r/SideProject, r/InternetIsBeautiful, r/androidapps, r/AppIdeas — exact
  subreddit choice needs Vishal's judgment on current rules/mod tolerance for app mentions, see note
  in reddit.md).
- **Which research finding it's responding to:** None yet available (research cron hasn't run for
  this brand) — responding to brand identity + real shipped-feature signal instead, as noted above.
- **Channels used:** Reddit (primary, manual post — no connected account, drafted only), LinkedIn
  (secondary, connected account — draft submitted, pending Vishal's approval), short-form video
  concept (secondary, concept saved, no generation job submitted).
- **Publishing plan:** Reddit has no connected `hermes-social` account for RabbitLore — this stays a
  plain draft file. Vishal reads `reddit.md`, picks the subreddit(s), and posts by hand.
  LinkedIn is connected: `create_draft` submitted post id `6b4fe486-9261-451c-bb6f-6ee8749de18e`
  (status `pending_approval`), `request_publish_approval` pinged Vishal on Telegram. Nothing
  publishes until Vishal clicks Approve in the admin UI.
- **Video plan:** Concept saved via `video_create_concept` (id
  `cecc601e-abe7-41bf-8f37-b07756b50d51`) — scene breakdown in `video-concept.md`. No generation
  job (HeyGen or Kling) submitted — per the skill, that step needs Vishal's explicit go-ahead
  since it spends a scarce free-tier slot or real money. `video_heygen_usage()` checked: 0/3 used,
  3 remaining this month.
- **URLs:** none yet (nothing posted; LinkedIn draft pending approval, not live).
- **Metrics:** pending.
- **Outcome:** pending.
