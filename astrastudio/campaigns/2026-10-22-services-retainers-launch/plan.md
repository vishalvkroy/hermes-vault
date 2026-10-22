# Campaign: 2026-10-22-services-retainers-launch

**Campaign ID:** 2026-10-22-services-retainers-launch
**Date:** 2026-10-22
**Objective:** First founder-led LinkedIn post marketing the real, shipped Services & Retainers
feature (service-business billing, no stock tracking, retainer draw-down invoicing) three days
after it went live with zero marketing, framed as a build-in-public engineering story including a
real bug caught in the same sweep.
**Hypothesis:** A genre-break post (a real feature launch + an honest bug confession, not another
SaaS self-audit/compliance post) aimed at a different, never-before-addressed audience (Services
buyers: consultants/freelancers/agencies) will be more diagnostically useful than an 8th SaaS post,
because it tests a different axis of the standing zero-engagement problem (audience + genre, not
just topic) on a line that currently has zero LinkedIn data.
**Target audience:** Indian consultants, freelancers, and small agencies who bill for labour/
time, not stock — the segment currently served by 21bill, Arjaka, LekhaPro, and 399Apps.
Secondary: the "Digital-First Founder" segment in strategy.md who might also need the Services
dev-package line.
**Channels used:** LinkedIn only (Astra Studio's primary channel per brand skill/strategy.md). No
blog/Instagram this week — the evidence (a single fresh feature + bug story) is LinkedIn-native;
a blog post on this would be premature with zero search demand yet measured on
`/service-business-software` (3 days old).
**Status:** `drafted` — Astra Studio's LinkedIn account on file is Vishal Kumar's personal member
profile, not an auto-publish `hermes-social` integration for this content type (confirmed again
this run via `list_accounts`: account_type "member"). Same as every prior Astra Studio LinkedIn
post, Vishal posts it himself manually.

## Why this (evidence receipt)
- **Strategy pillar:** "The Transparency Play (Services)" — Pillar 1, strategy.md Content
  Pillars — extended here from pricing-transparency to product-transparency (a real build log,
  including an admitted bug), same pillar's underlying "build trust by showing real work" logic.
- **Research basis:** `research/2026-10-19_deep-research.md` Opportunity #1 and git ground truth
  (commit `5d5ec76`, 2026-10-19 00:12 IST) — Services & Retainers shipped with a dedicated
  `/service-business-software` landing page, zero marketing since. `research/2026-10-22_deep-
  research.md` confirms zero new commits this week (nothing fresher to lead with) and reconfirms
  the Services line still shows 0 organic search traffic (7th consecutive run) and the lone prior
  Services LinkedIn post (2026-10-15) has no recorded outcome — both cited directly in the
  council_review question below.
- **Differentiator vs named competitors:** 21bill, Arjaka, LekhaPro, 399Apps (strategy.md
  Positioning table, service-billing-only SaaS tools) — all four serve consultants/agencies but
  none run a full retail stock engine underneath; Astra Atlas now runs stock and services through
  one accounting engine (same P&L, balance sheet, trial balance) per the strategy.md positioning
  row added 2026-10-19.
- **Success metric:** direct `linkedin_fetch_post` likes/comments/shares, checked 2026-10-29 (7
  days) and 2026-11-05 (14 days, per the standing performance-log cadence) — baseline is the
  current 7-post, 6+ week run of 0/0/0 engagement on every checkable post. This post is also a
  direct data point for strategy.md Experiment #3 (distribution vs. content problem): because it
  changes audience AND genre simultaneously, any non-zero result argues against pure distribution
  failure; another zero strengthens (not proves) the distribution hypothesis instead of adding a
  9th ambiguous SaaS data point.

## council_review record (tier=flagship)
**Question asked:** given 3 ranked, evidence-backed candidates from this week + last week's
research — (A) SaaS/Compliance: GSTN's 16 Oct 2026 RCM e-invoicing advisory (real, dated, zero
competitor coverage, but narrow ₹5cr+ turnover audience, must stay forward-looking since
`einvoiceService.ts` has no RCM support yet); (B) Services: the real shipped Services & Retainers
feature (2026-10-19) with a genuine "why we built this" story including a real bug caught in the
same sweep (WhatsApp low-stock alerts firing daily on every service product); (C) SaaS/Compliance-
depth: a verified, cleared-for-use counter-claim that Astra Atlas's GSTR-1/3B/2B export is real
shipped code, not spec-only, directly countering HelloBooks' "others only generate bills, they
don't file" claim — which deserves this week's LinkedIn slot, given 7 straight zero-engagement
posts and an unresolved distribution-vs-content question, and would picking B meaningfully help
resolve that question versus A/C extending the same flat SaaS series?
**Verdict:** 2/4 models responded (Gemini timed out, Mistral rate-limited — reported as a real
partial result). Claude Sonnet 5 and GPT-OSS-120B (Groq) **both independently picked B**. Shared
reasoning: A and C are both more SaaS/compliance content in the exact channel that's already flat
on 7 posts — a 9th data point in that series is diagnostically inert (can't tell if the problem is
distribution or content because nothing about the stimulus changes enough to test anything).
B changes audience (Services buyers, never addressed before), genre (feature launch + honest bug
confession, not a self-audit or compliance notice), and tests a line with genuinely zero prior
data — any result (engagement or none) adds real information the other two candidates can't.
Claude added that the honest bug admission is itself the thing that makes the post shareable in a
way a compliance notice structurally cannot be. No real divergence between the two models that
responded. Went with B.

## My call
Followed both models' convergent recommendation — picked B (Services & Retainers launch). This
matches my own read: candidates A and C are both narrow-audience SaaS/compliance plays layered on
top of an already-flat channel, while B is the first-ever opportunity to test whether the Services
audience behaves differently, which is strategically more valuable right now than a 9th SaaS post
regardless of engagement outcome. Framed the post as an honest build-log (real bug, real fix,
real reason the feature exists) rather than a feature-announcement pitch, per both models' shared
point that manufactured hype would undercut the one thing that makes this post diagnostically
useful: genuine specificity.

## Notes for next run
- A (RCM e-invoicing forward-looking piece) and C (GSTR filing-depth counter-claim) both stay
  queued, not dropped — both are real, evidence-backed, cleared for use whenever the Services
  genre-break has had a week to be read.
- The still-open process flag from research (2026-10-15 Services-vs-FlowLaunch post has no
  recorded post_id/URL — unverifiable) is a separate, already-raised item; not blocking this draft.
- If this post does get engagement, strategy.md Experiment #3 should be updated to reflect
  content/genre as at least a partial explanation, not pure distribution. If it also lands at
  zero, record it as the second genuinely different-axis data point toward the distribution
  hypothesis, not a third identical SaaS zero.
