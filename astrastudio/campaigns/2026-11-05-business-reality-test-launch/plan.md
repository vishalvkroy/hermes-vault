# Campaign: 2026-11-05-business-reality-test-launch

**Campaign ID:** 2026-11-05-business-reality-test-launch
**Date:** 2026-11-05
**Objective:** Founder-led LinkedIn post telling the real build story of the Business Reality
Test (astrastudio.in/business-reality-test) - the Services line's first-ever structured,
paid (₹149) lead-qualification funnel, rebuilt from a plain free-text form into a 9-question
tap-based diagnostic in a 3-day iteration (29-31 Oct 2026).
**Hypothesis:** This is a genuinely new content genre for the channel (a product-design build
log with real before/after detail, not another feature-demo retrospective) for a line that has
had zero organic traffic for 12 consecutive weeks and zero leads ever. It was already the
unanimous top pick from a fast-tier council_review on 2026-11-02 and nothing has superseded it
since - no new commits landed between 2026-11-03 and 2026-11-05 (confirmed quiet week, see
research/2026-11-05_deep-research.md).
**Target audience:** Indian businesses considering a custom website/app build without hiring
in-house (strategy.md's Services-line buyer) - also doubles as founder-credibility content for
the "Digital-First Founder" segment who's wary of being overcharged by agencies.
**Channels used:** LinkedIn only (astrastudio brand's primary channel per brand skill/strategy.md).
Account on file (`list_accounts`) is Vishal Kumar's personal member profile (`account_type:
member`), same as every prior Astra Studio LinkedIn post - not an auto-publish integration.
Vishal posts it himself manually.
**Status:** `drafted` - awaiting Vishal's manual post.

## Why this (evidence receipt)
- **Strategy pillar:** Pillar 1, The Transparency Play (Services) - strategy.md's positioning
  row names the Business Reality Test directly: "a ₹149 paid, structured, psychologically-
  designed diagnostic (commitment/consistency, goal-gradient, self-assessment framing) that
  pre-qualifies serious buyers before they ever reach a quote form" - no tracked competitor on
  either side (SaaS or Services) does this.
- **Research basis:** research/2026-11-02_deep-research.md (25 commits/3 days, commit `6216136`
  funnel build + `4f3b678` tap-based redesign, 18 files/1,718 insertions on the initial build
  alone) and research/2026-11-05_deep-research.md performance review (confirms Services line now
  at 12 consecutive zero-organic-traffic weeks, zero leads ever, and that this content candidate
  is STILL not drafted/published as of this run - nothing new superseded it). Verified directly
  against the repo this run: `git show --stat 6216136` and `4f3b678` confirm the funnel (landing
  page, Cashfree payment, server-side payment re-verification, 9-question diagnostic with a
  progress bar, confidence scale, max-2 multi-select, identity fields moved last) is real,
  shipped code, not a planned feature.
- **Differentiator vs named competitor:** all 10 tracked competitors (Vyapar, myBillBook,
  Khatabook, BUSY Magic, HisabKitab, Udyog, HelloBooks, 21bill/Arjaka/LekhaPro/399Apps,
  VoiceKhata, FlowLaunch) lead new prospects straight into a free trial, demo request, or quote
  form - none use a paid, structured, friction-deliberate qualification step
  (research/2026-11-02_deep-research.md Opportunity #1, strategy.md positioning table).
- **Success metric:** LinkedIn likes/comments/shares at 7 and 14 days vs the standing 10-post
  0/0/0 baseline (research/2026-11-05_deep-research.md Performance review); GSC impressions/
  clicks on /business-reality-test, first 14 days, vs its current near-zero baseline (still not
  in the 50-row page dump as of 2026-11-05, 6 days live) - checked on 2026-11-19.

## Council review (flagship, 2026-11-05)
**Question asked:** given 10 confirmed-published LinkedIn posts this cycle all at 0/0/0
engagement regardless of genre, does Candidate 1 (Business Reality Test build-log, carried
forward unpublished since 2026-11-02's unanimous fast-tier pick) still deserve this week's slot
over Candidate 2 (a short SaaS freshness update on the Nov 2026 GST reform rollout, building on
an already-published blog post, new angle being NASSCOM's public deferment ask) - weighing
real differentiation, measurability, whether a 3rd consecutive carry-forward is still right, and
the risk that genre alone isn't explaining the zero-engagement pattern.
**Verdict:** Partial response only - Claude Sonnet 5 hit a 502, Gemini and Mistral both hit 429
rate limits on retries. One full flagship-tier response landed (Groq/GPT-OSS-120B), which backed
Candidate 1: the Business Reality Test is the Services line's first real lead-capture mechanism
after 12 dead weeks, is measurable through a hard business metric (completions/payments) rather
than LinkedIn vanity metrics alone, and the zero-engagement streak is more plausibly an audience/
distribution issue than a genre problem since it's held across every genre tried, including the
free-tool launch. Its argument against Candidate 2: an update to an already-published post adds
brand-awareness value but doesn't move the one metric that's actually broken (Services-line
leads), and GST-reform content has a weaker head-to-head differentiation story (no tracked
competitor gap claimed, just a freshness angle). Only one full response landed, so this isn't the
full-committee read the flagship tier is meant to produce - going with it because it corroborates
both 2026-11-02's unanimous fast-tier verdict and my own read of research/2026-11-05's data (the
Services line's 12-week zero-traffic streak is a sharper, more urgent problem than a GST-content
freshness edit, and nothing shipped this week to change that ranking).

## What this is NOT
Not a feature-demo of a SaaS product capability. Not a claim that the diagnostic is AI-generated
or automated - the report is written by a person ("manual report" per the repo's own commit
message); the post does not say otherwise. Not grounded in the GST-reform angle (Candidate 2) -
that stays queued, not dropped, per research/2026-11-05's Opportunity #3 (a low-effort addendum
to the existing gst-reforms-november-2026-india post, not a new campaign slot).
