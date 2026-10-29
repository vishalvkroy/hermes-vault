# Campaign: 2026-10-29-linkedin-posting2-validation-reddit-triage

**Campaign ID:** 2026-10-29-linkedin-posting2-validation-reddit-triage
**Timestamp:** 2026-10-29
**Brand:** RabbitLore
**Status:** LinkedIn channel = pending_approval (connected account, awaiting Vishal's approval
click). Reddit channel = NOT a new draft this week — triage-only note (see below), 5 existing
drafts remain unposted.

## Objective
Put this week's strongest external validation (Posting2's 4-source-corroborated anti-feed proof
point) on the one channel that is actually live and shipping, and stop adding supply to a Reddit
channel that has produced 5 drafts and 0 posts. Address the backlog as the real problem it is,
not another research cycle's worth of content.

## Which research finding this responds to
`research/2026-10-29.md` Top Opportunity: Posting2's organic-growth story now has 4 independent
sources (Fast Company, Afterschool Substack, YPulse — new this run, MWM app-intelligence — new
this run) within days, zero PR push behind it — "the strongest, most externally-corroborated
single proof point in this entire research line to date" for Pillar 1's private/capped-beats-
open/public macro-thesis. Research explicitly names this stronger citation material than Yope's
or Retro's funding-round mentions.

## Opportunity scoring — 3 candidates considered (per task instructions)
1. **(A) Posting2 4-source-corroborated anti-feed proof point** — research's own explicit Top
   Opportunity this week; serves Pillar 1 with the strongest external validation logged yet.
2. **(B) Guardian "intimacy economy" essay** — fresh category evidence (not a named-competitor
   update) for Pillar 3's anti-AI-companion thesis; a real first-person account of an AI chatbot
   substituting for human connection, which is exactly the "simulated vs real" line getBlend
   argues against.
3. **(C) The Reddit backlog itself** — 5 drafts (2026-09-24, 2026-10-01, 2026-10-10, 2026-10-15,
   2026-10-22), 0 posted. `strategy.md` §13 already names this "the dominant open risk to Pillar
   1's Reddit KPI," needing Vishal's direct action, not more research cycles — a case for NOT
   drafting a 6th Reddit post and redirecting effort to the live channel instead.

## council_review (flagship) question and verdict
**Question asked:** laid out candidates A (Posting2, 4-source Pillar 1 proof point), B (Guardian
essay, Pillar 3 category evidence), and C (the 5-deep, 0-posted Reddit backlog, flagged in
strategy.md as the dominant open risk needing Vishal's action, not more content) — asked which
deserves this week's drafting effort, whether to split effort, and to name the real tension
between chasing the strongest new evidence (A/B) versus the compounding risk of a stalled channel
(C).

**Verdict obtained:** 2 of 4 models answered this run (Gemini and Mistral both hit HTTP 429).
**Claude (claude-sonnet-5) and Groq (openai/gpt-oss-120b) converged, not diverged** — a genuine
agreement, reported as such, not forced. Both: (1) treat (C) as a distribution/process problem,
not a content opportunity — don't draft a 6th Reddit post into a channel that has shipped zero
of five; (2) redirect this week's strongest new evidence to LinkedIn, the channel that is
actually live and connected, where it reinforces the build-in-public register; (3) prioritize
(A) over (B) — Claude called 4-source corroboration "a trend line" versus (B)'s "good anecdote";
Groq ranked (A) above (B) on pillar fit (Pillar 1 is the Reddit-KPI-bearing pillar) and
production cost (B would need a mini case-study to land well, A is already synthesis-ready).
Both explicitly flagged (C) as needing direct escalation to Vishal with specific dates, not a
vague "please post more" note.

**Where they agreed (real signal):** don't add Reddit supply this week; move (A) to LinkedIn;
flag the backlog explicitly and specifically. Both also noted (A)'s freshness (zero PR push,
days-old 4-source confirmation) argues for using it now rather than letting it sit for a later,
healthier Reddit cycle — the citation value decays if reused weeks later as "old news."

**Where they diverged:** Claude would hold (B) back entirely for "a future Pillar 3 piece once
Reddit is flowing again," treating it as non-time-sensitive. Groq's answer (cut off by token
limit) was heading toward a similar read but didn't fully commit before truncating — not treated
as a real disagreement given the truncation, just incomplete.

**My call:** followed the converged verdict exactly — no new Reddit draft this week, (A) drafted
for LinkedIn via `linkedin-post-writer` (F19 Anecdote-Meets-Evidence Bridge — a personal noticing
plus a sourced 3-number evidence stack, fits a build-in-public Pillar-1 proof-point post well),
(B) held back per Claude's reasoning (not time-decaying, better saved for a dedicated Pillar 3
piece once Reddit backlog clears or a Reddit account gets connected), and (C) written up as an
explicit triage note in `reddit.md` (not a new post — a backlog-status memo with Vishal's
specific next action) rather than silently doing nothing about the 5 unposted drafts.

## Chosen opportunity
LinkedIn post citing Posting2's 4-source-corroborated organic growth as this week's proof point
for Pillar 1 (night-gated private lore-sharing / anti-feed thesis). No new Reddit content drafted
— `reddit.md` in this folder is a triage memo on the existing 5-draft backlog, not a 6th draft.

## Why this (evidence receipt)
- **Strategy pillar:** Pillar 1 — Night-gated private lore sharing (`strategy.md` §4), served via
  LinkedIn this week per the council verdict rather than Reddit.
- **Research basis:** `research/2026-10-29.md` Top Opportunity and Competitive Edge §3: Posting2
  crossed a 3-independent-source confirmation bar (Fast Company[2], Afterschool Substack, YPulse[1]
  — new this run) plus a 4th non-editorial data source (MWM app-intelligence[9] — 10k+ downloads,
  5.0 rating/319 ratings) within days of first discovery, zero PR push. 8,000 September downloads,
  +42% MoM (Sensor Tower via Fast Company, logged 2026-10-26).
- **Differentiator:** vs. the broader "anti-feed" category (Yope $12.3M, Retro $21M, Posting2 $0 —
  tracked not chased per `strategy.md` §7) — the macro-thesis (private/capped beats open/public)
  is now validated by a funded AND an unfunded, organically-growing example in the same window.
  RabbitLore's specific mechanic (night-gated sharing window, `rabbithole-mobile` commit
  `391063f`; peer lore-matching via `getBlend`, `rabbithole` commit `7c4e05a`) isn't duplicated by
  any of them — all three validate the macro-thesis without being feature competitors.
- **Success metric:** LinkedIn `get_post_analytics` once approved and live. Flagging: this metric
  has returned unmeasurable (`collected: false` / HTTP 500) for 10 consecutive runs on the two
  prior posts — a null result here would continue, not break, that pattern. Checked on or after
  2026-11-05.

## Target audience
Per `docs/positioning.md`: overthinkers, creative people, nerds, dreamers, gamers, writers,
programmers, history lovers, people with strange obsessions, lonely kids who grew up, people who
carry entire worlds in their heads — the LinkedIn post's register targets the founder/builder
subset of this per `strategy.md` §3 (secondary audience, but the one channel with a confirmed-
live, confirmed-published result, per Pillar 4).

## Channels
- **LinkedIn (this week's primary effort):** `linkedin.md` — Posting2 4-source validation post,
  written via `linkedin-post-writer`'s F19 Anecdote-Meets-Evidence Bridge formula, run through
  its own humanizer discipline, submitted via `create_draft` + `request_publish_approval`.
- **Reddit (not drafted this week, by design):** `reddit.md` — a triage memo, not a post. Names
  the 5-deep unposted backlog plainly and asks Vishal to post at least one before new Reddit
  content gets added to the pile.
- **Short-form video:** not pursued. Neither angle is visual-first; no `video_create_concept`
  call made.

## IMPORTANT — flag to Vishal: Reddit backlog now at 5 unposted drafts, 0 ever posted
`2026-09-24-reddit-night-gated-lore-launch`, `2026-10-01-reddit-regulatory-structural-safety`,
`2026-10-10-reddit-teen-migration-hard-numbers`, `2026-10-15-reddit-quiet-social-category`,
`2026-10-22-reddit-retro-anti-feed-validation`. Both council models this run and last run's
Claude flagged this as the dominant open risk to Pillar 1's Reddit KPI. This week deliberately
adds zero new Reddit drafts to that pile — see `reddit.md` for the specific ask.

## Metrics
Pending — LinkedIn post `9dc116d5-32b3-4347-b4cd-c3fac9ec57c0` created via `create_draft`
(status `pending_approval`), `request_publish_approval` called, Vishal notified. Metrics checked
per the Success metric date above once he approves. Reddit: no new post, nothing to measure;
backlog status unchanged until Vishal acts.

## Outcome
Pending.
