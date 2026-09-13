# Campaign: 2026-09-06-reddit-curiosity-ranker-was-dead

- **Campaign ID:** 2026-09-06-reddit-curiosity-ranker-was-dead
- **Timestamp:** 2026-09-06T07:52Z
- **Status:** drafted
- **Grounding note:** `rabbitlore/research/` is still empty — the weekly research cron has not
  run for this brand yet (same gap as last cycle's campaign). Per the campaign-workflow rule,
  this campaign is not built on invented market signals. It's grounded in a real, verifiable
  shipped event pulled from `git log` in the wired backend repo (`rabbithole`):
  - `57b0f59` — "fix: curiosity ranker was dead — vector is 29-dim, gates checked === 21".
    The recommendation taxonomy (`CATEGORY_ORDER`) grew from 21 to 29 categories over time, but
    the personalization gate in `getForYou` and two holes feeds still hardcoded
    `curiosityVector.length === 21`. Since real vectors were always 29-dim after the taxonomy
    grew, that condition was never true — every "For You" feed silently fell back to
    popularity-only ranking. No error, no crash, just quietly worse personalization for however
    long the taxonomy had been out of sync with the gate.
  - `f3a9868` — same-day follow-up making the fix self-healing: `shouldRecompute` now treats a
    vector-dimension mismatch as stale (rebuilds automatically even if a future dimension change
    forgets to bump the version), and `getForYou` enqueues a debounced recompute on a stale
    profile instead of just falling back silently again.
  - This is a different feature/story than last cycle's campaign (`2026-09-05-reddit-devlog-
    night-gated-lore-share`, which covered the night-gated lore-share feature and the "holes"
    mechanic) — deliberately not repeating that angle.
  - Recommend the actual research cron run before next cycle so campaigns start reacting to real
    market/competitor signal instead of repo activity alone two cycles running.
- **Objective:** Build authentic Reddit presence for RabbitLore via honest, technical
  build-in-public content — per spec section 12, this brand grows through genuine community
  contribution, not campaigns shaped like ads.
- **Hypothesis:** A humble "our own recommendation system was silently broken and nobody noticed"
  post reads as authentic engineering content, not promo — technical/indie-dev Reddit audiences
  respond well to honest postmortems with a concrete root cause (a hardcoded number vs. a growing
  taxonomy), especially with a self-healing fix, more than to any feature-announcement framing.
- **Target audience:** Gen Z / indie-dev / SaaS-builder Reddit communities interested in real
  engineering postmortems (e.g. r/webdev, r/programming, r/SideProject — exact subreddit choice
  needs Vishal's judgment on current rules/mod tolerance for app-adjacent postmortems, see note
  in reddit.md).
- **Which research finding it's responding to:** None yet available — research cron hasn't run
  for this brand across two cycles now. Responding to a real shipped-fix signal from the backend
  repo instead, as noted above.
- **Channels used:** Reddit (primary, manual post — no connected account for RabbitLore, drafted
  only), LinkedIn (secondary, connected account — draft submitted, pending Vishal's approval),
  short-form video concept (secondary, concept saved, no generation job submitted).
- **Publishing plan:** Reddit has no connected `hermes-social` account for RabbitLore — plain
  draft file, Vishal reads `reddit.md`, picks the subreddit(s), posts by hand. LinkedIn is
  connected (`list_accounts` returned account `d20350bf-f728-4301-98c9-9632b4025761`, Vishal
  Kumar) — `create_draft` submitted, `request_publish_approval` pinged Vishal on Telegram.
  Nothing publishes until Vishal clicks Approve in the admin UI — post id
  `2c7919ee-da2a-4936-984d-35bb4b8a05a9`, see linkedin.md for status to check later.
- **Video plan:** Concept saved via `video_create_concept` (id
  `014ab6c6-aa76-4c14-ac62-8f9636f9ccd8`) — scene breakdown in `video-concept.md`. No generation
  job (HeyGen or Kling) submitted — per the skill, that step
  needs Vishal's explicit go-ahead since it spends a scarce free-tier slot or real money.
  `video_heygen_usage()` checked: 0/3 used, 3 remaining this month.
- **Copy quality note:** The `humanizer` skill (writing category) was requested for this job but
  is not present in this Hermes instance's skill set (not found when searched/loaded) — copy
  below was written directly for plain, non-hyped voice and manually re-read for AI-writing tells
  (throat-clearing, "delve"/"leverage"-style filler, overuse of em-dashes/rule-of-three lists),
  but the automated humanizer pass could not run. Flagging this so Vishal knows it's a manual
  pass, not the usual pipeline step.
- **URLs:** none yet (nothing posted; LinkedIn draft pending approval, not live).
- **Metrics:** pending.
- **Outcome:** pending.
