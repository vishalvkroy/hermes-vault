# Campaign: 2026-10-22-reddit-retro-anti-feed-validation

**Campaign ID:** 2026-10-22-reddit-retro-anti-feed-validation
**Timestamp:** 2026-10-22
**Brand:** RabbitLore
**Status:** Reddit channel = drafted (manual-only, no connected hermes-social Reddit account).
LinkedIn channel = pending_approval (connected account, awaiting Vishal's approval click).

## Objective
Add one more research-grounded, non-promotional Reddit contribution to the night-gated-lore
thesis, while directly naming and acting on the growing unposted-draft backlog on the one live
channel (LinkedIn) instead of letting it go unaddressed for a third consecutive week.

## Hypothesis
(Reddit) A second, independently-funded "anti-feed" competitor (Retro) reaching 7M downloads is
a more concrete, citable proof point for "private beats public" than a single funding
announcement, and will read as genuine trend-reporting, not a product pitch, to a
tech/privacy-adjacent subreddit.
(LinkedIn) Naming the backlog itself, honestly, with a committed next step, fits this brand's one
confirmed-working content pillar (build-in-public engineering honesty) better than silence, and
is more useful to Vishal than one more draft he has no time to act on.

## Which research finding this responds to
`research/2026-10-22.md` Top Opportunity: Retro's $21M Series A / 7M downloads / ex-Instagram
engineers / subscription model, as a second independently-dated "anti-feed" funded competitor
alongside Yope — the explicit research recommendation for this week's Reddit angle. Strategy
pillar served: Pillar 1 (night-gated private lore sharing, `strategy.md` §4) for the Reddit
piece; Pillar 4 (build-in-public engineering honesty, `strategy.md` §4) for the LinkedIn piece.

## Opportunity scoring — 3 candidates considered (per task instructions)
1. **(A) New Reddit devlog citing Retro** — research's own explicit Top Opportunity this week;
   serves Pillar 1 with a stronger, second data point than Yope alone.
2. **(B) LinkedIn backlog-transparency post** — serves Pillar 4, the one channel with a live
   account and 2 published posts; directly addresses the growing (now 4-deep) unposted Reddit
   draft problem both prior flagship council runs flagged.
3. **(C) MIDiA bifurcation-nuance content piece** — a caution in the research (market splitting
   entertainment-first vs peer-to-peer), not a strong standalone angle per the research file's
   own framing ("a balancing nuance... not a reversal").

## council_review (flagship) question and verdict
**Question asked:** given the now-4-deep unposted Reddit backlog (0 of 4 drafts since 2026-09-24
actually posted) and last week's genuine flagship divergence on whether to keep adding Reddit
supply (Groq: yes, drafting and shipping are separate problems; Claude: no, stop until the
backlog clears) — which of the 3 candidates above deserves this week's campaign effort, and
should drafting continue adding Reddit supply or redirect to LinkedIn backlog-transparency, or
some combination?

**Verdict obtained:** 2 of 4 models failed this run — Claude (claude-sonnet-5) returned a 502
error, Mistral hit HTTP 429. **Gemini also timed out.** Only **Groq (openai/gpt-oss-120b)**
returned a full answer. Groq recommended **B as this week's primary effort** ("the LinkedIn post
... directly tackles the backlog problem"), paired with **publishing 1-2 of the existing Reddit
drafts instead of writing new ones**, framing Option A (the new Retro devlog) as valuable but
conditional on the Reddit channel being "healthy" first — posting a fifth idea into a dead
channel, in Groq's reasoning, has a low signal-to-noise ratio and risks "looking busy while
producing no output." Groq explicitly ranked C (MIDiA) lowest: real but not urgent, and still
blocked on the same dead Reddit channel for distribution.

**Where this matched the prior week's divergence:** notably, Groq flipped its own prior-week
position. On 2026-10-15, Groq argued for continuing to add Reddit supply because drafting and
shipping are separate problems; this run, facing the same backlog one week further along with no
improvement, Groq's own answer shifted to prioritizing the transparency post and explicitly
recommended NOT writing a new Reddit draft this week. No second model responded to confirm or
contradict this shift, so it is reported as a single model's answer, not a consensus — but it is
a notable, self-consistent escalation given the backlog got worse, not better, since the last
check.

**My call:** followed Groq's core recommendation (B as primary effort) but did not fully drop A.
Reasoning: Groq's own caveat is that a new Reddit draft is low-value only because the channel is
"dead" (nothing shipping), not because the Retro evidence itself is weak — and the Retro evidence
is genuinely stronger than anything already sitting in the backlog (a second independently-dated
funded competitor is new, not a repeat of existing drafts). Writing both costs one extra draft
file, no extra risk, and gives Vishal a fresh, highest-quality option alongside the explicit ask
to clear the backlog — which is the actual blocking problem per Groq's own diagnosis. The
Telegram summary and this plan both lead with the backlog, not with "here's another draft,"
honoring the substance of Groq's (and last week's Claude's) warning even where the output
differs slightly from "stop drafting entirely."

## Chosen opportunity
Dual effort this week: (1) Reddit devlog draft citing Retro's $21M raise / 7M downloads as a
second funded "anti-feed" validation point, written as genuine trend-reporting with RabbitLore
mentioned once, factually, not as a pitch. (2) LinkedIn build-in-public post naming the 4-deep
unposted Reddit backlog honestly and committing to posting one specific draft
(2026-10-10-reddit-teen-migration-hard-numbers, per that campaign's own "prefer this one" note).

## Why this (evidence receipt)
- **Strategy pillar:** Pillar 1 — Night-gated private lore sharing (Reddit draft) and Pillar 4 —
  Build-in-public engineering honesty (LinkedIn draft), both in `strategy.md` §4.
- **Research basis:** `research/2026-10-22.md` Top Opportunity and Competitive Edge §3(e):
  Retro's $21M Series A (Field Ventures, Thrive Capital, announced 2026-08-28) and 7M downloads
  by mid-October 2026[1][2][3], explicitly recommended as this week's strongest Reddit citation.
- **Differentiator:** vs. the broader "anti-feed" category (Yope + Retro, tracked not chased per
  `strategy.md` §7) — RabbitLore's specific mechanic (night-gated sharing window,
  `rabbithole-mobile` commit `391063f`; peer lore-matching via `getBlend`, `rabbithole` commit
  `7c4e05a`) is not duplicated by either funded competitor; both validate the macro-thesis
  (private beats public) without being feature competitors.
- **Success metric:** Reddit — upvotes/comments if Vishal posts, checked manually (no connected
  account) on or after 2026-11-05. LinkedIn — `get_post_analytics` once approved and live;
  flagging now that this metric has returned unmeasurable (`collected: false` / HTTP 500) for 8
  consecutive runs on the two prior posts, so a null result on this post would continue, not
  break, that pattern — checked on or after 2026-10-29.

## Target audience
Per `docs/positioning.md`: overthinkers, creative people, nerds, dreamers, gamers, writers,
programmers, history lovers, people with strange obsessions, lonely kids who grew up, people who
carry entire worlds in their heads (Reddit draft's core audience). LinkedIn draft's audience is
the founder/builder crowd per `strategy.md` §3 (secondary, not the core Gen Z user, but where
Pillar 4 content has actually published and performed before).

## Channels
- **Reddit (primary, per brand-channel priority):** `reddit.md` — Retro/anti-feed-validation
  devlog post, RabbitLore mentioned once, factually, no pitch, no competitor attack.
- **LinkedIn:** `linkedin.md` — backlog-transparency post (F4 Time-Anchor Confession), drafted via
  `linkedin-post-writer`'s formula approach, run through its own humanizer discipline, to be
  submitted via `hermes-social` `create_draft` + `request_publish_approval` per the
  campaign-workflow skill (never auto-published).
- **Short-form video:** not pursued this cycle — neither angle is visual-first; no
  `video_create_concept` call made.

## IMPORTANT — flag to Vishal: Reddit backlog now at 5 unposted drafts
`2026-09-24-reddit-night-gated-lore-launch`, `2026-10-01-reddit-regulatory-structural-safety`,
`2026-10-10-reddit-teen-migration-hard-numbers`, `2026-10-15-reddit-quiet-social-category`, and
this run's `reddit.md` — all unposted. This week's LinkedIn draft directly names this and commits
to a specific pick (2026-10-10's draft) as the one to post first. If Vishal posts a different one
instead, that's fine — the point of the LinkedIn post is the honest acknowledgment and a forcing
function, not dictating which exact draft wins.

## Metrics
Pending — Reddit is draft-only (no connected account); LinkedIn post `e3f4a2d2-fdc9-4a06-84dd-80948308398f`
is `pending_approval` as of this run (created via `create_draft`, `request_publish_approval`
called — Vishal notified), metrics checked per the Success metric dates above once he approves.

## Outcome
Pending.
