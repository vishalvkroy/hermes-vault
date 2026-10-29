# Campaign: 2026-10-29-gst-late-fee-calculator

**Campaign ID:** 2026-10-29-gst-late-fee-calculator
**Date:** 2026-10-29
**Objective:** Founder-led LinkedIn post announcing the new, real, shipped GST Late Fee & Due
Date Calculator (astrastudio.in/tools/gst-late-fee-calculator), framed as a genuine
engineering-as-marketing build log, not a feature-demo retrospective.
**Hypothesis:** A free-tool launch post is a genre break from the 8 consecutive zero-engagement
posts this month (all SaaS feature-demo or bug-fix retrospectives) - it gives something
immediately usable with zero signup, is inherently shareable/saveable (a calculator, not a
dashboard screenshot), and tests the distribution question on a different content shape before
spending another slot on the same failing format.
**Target audience:** Indian SMB owners and accountants who personally file GST returns -
strategy.md's "GST-Scared SMB" segment - plus the existing "Frustrated Retailer" segment who
already uses Astra Atlas for billing.
**Channels used:** LinkedIn only (Astra Studio's primary channel per brand skill/strategy.md).
No blog - the free-tools.md vault doc explicitly flags duplicate "here are our tools" posts as
off-limits; this is a single-tool launch angle, not a tools-roundup, so it clears that bar, but a
blog post isn't warranted for a tool page that already has its own on-page copy and schema.
**Status:** `drafted` - Astra Studio's LinkedIn account on file is Vishal Kumar's personal member
profile (`list_accounts` confirms account_type "member", same as every prior post), not an
auto-publish integration. Vishal posts it himself manually.

## Why this (evidence receipt)
- **Strategy pillar:** Free-tools engineering-as-marketing play (`docs/free-tools.md`) feeding
  Pillar 2 (Compliance Watch) - a GST-compliance tool is the Atlas cluster's natural extension,
  same "look what we built" logic the vault doc names as "the single most natural LinkedIn
  founder-led post."
- **Research basis:** `research/2026-10-29_deep-research.md` section 1 (git ground truth, commit
  `fa93e2c`/`06f274a`, 2026-10-27) - real shipped tool, due dates computed from the filing rule
  (not hardcoded per month, so it never goes stale), late-fee/interest figures verified against
  CBIC guidance before writing. Zero marketing since ship. Research frames it as a *recurring*
  high-intent search ("gst late fee calculator", "gstr-3b due date" - repeats every filing cycle,
  not a one-time hit) distinct from a one-off feature-demo.
- **Differentiator vs named competitor:** none of the 8 tracked competitors (Vyapar, myBillBook,
  Khatabook, HelloBooks, BUSY Magic, HisabKitab, Udyog, FlowLaunch) offer a free, no-login
  late-fee/due-date calculator on their public site per this run's and prior runs' checks - this
  is a free-standing lead-gen asset, not a feature comparison claim, so the real differentiator is
  "we give this away free, with zero signup" against tools that gate GST features behind signup.
- **Success metric:** direct `linkedin_fetch_post` likes/comments/shares at 7 days (2026-11-05)
  and 14 days (2026-11-12), per the standing performance-log cadence - baseline is the current
  8-post, 6+ week run of 0/0/0 engagement. GSC impressions/clicks on
  `/tools/gst-late-fee-calculator`, first 14 days, vs the near-zero baseline every new tool page
  starts from.

## Council review (flagship, 2026-10-29)
**Question asked:** given 3 real evidenced candidates this week (SaaS Category/Department Profit
report - new feature, zero marketing, but extends the same feature-demo genre that's gone 0/0/0
on 8 straight posts; Services line outcome-framed repositioning - 0 organic traffic 9 straight
weeks, 0 leads ever, never tried outcome-framing; SaaS GST Late Fee Calculator - new free tool,
recurring high-intent search, fits the existing free-tools pillar, zero marketing yet) - which
deserves this week's LinkedIn slot, weighing differentiation, measurability given the 8/8
zero-engagement streak, and whether to try the Services line's first genuinely different angle
vs another SaaS post.
**Verdict:** Partial responses only - most calls hit provider rate limits/502s (Gemini 429 x6,
Mistral 429 x4, Claude 502 x2) despite repeated retries across both batched and single-model
calls. Two full answers landed: Groq/GPT-OSS-120B and one successful Claude Sonnet 5 call, both
independently picked the **GST Late Fee Calculator (#3)** - Claude's stated reasoning: the
Profit-report pick repeats the exact failing format 9 times without changing the variable being
tested, and the Services pick has a worse signal than "wrong framing" (zero traffic/zero leads,
meaning no one is even finding the line, so a framing change alone is unlikely to be
distinguishable from more silence). Groq's reasoning: the calculator is measurable today via GSC
and tool-page analytics independent of LinkedIn's own reach, is inherently more shareable/
discoverable than an internal reporting-screen demo, and gives a natural bridge back to both the
SaaS and Services lines in follow-up content without needing the Services funnel rebuilt first.
No model argued for the Services or Profit-report options in the responses that did complete.
Going with the **GST Late Fee Calculator** - both complete, independent verdicts agreed, and the
reasoning (don't re-run the same failing experiment a 9th time; don't bet this week's one slot on
a line with zero measured reach at all) holds up against my own read of the data above.
