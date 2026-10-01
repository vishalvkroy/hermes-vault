# Campaign: 2026-10-01-loan-readiness-zero-score

**Objective:** Founder-led LinkedIn post demonstrating Loan Readiness (shipped 2026-09-26) as a
concrete, provable differentiator against Vyapar and myBillBook, neither of which sells credit-
readiness intelligence - only billing/invoicing.

**Hypothesis:** A founder post demoing a real shipped feature (with test-count receipts) outperforms
a generic GST-explainer post on engagement, because it is a specific, undefended claim competitors
cannot currently match - and because 4/4 posts this month show zero engagement, this week's bet
should maximize content-quality odds rather than lean on a market-research angle with secondhand
receipts.

**Target audience:** Indian SMB retailers/shopkeepers evaluating billing software, plus the
"GST-Scared SMB" and "Frustrated Retailer" segments from strategy.md's audience table; secondary
audience is other founders/operators who engage with build-in-public LinkedIn content.

**Which research finding this responds to:** `research/2026-10-01_deep-research.md`, Opportunity #1
([SAAS, High Priority] Money Leaks + Loan Readiness) and Competitive Edge #2 in the same file.

**Decision process - council_review (tier=flagship):**
Question asked: given three scored opportunities this week - (1) [SAAS] Money Leaks + Loan
Readiness (two real shipped features, zero marketing yet, direct undefended "intelligence vs
billing" differentiator vs Vyapar/myBillBook), (2) [SERVICES] fixed-price web/app dev packages vs
Indian agency market chaos (5 pricing guides + live r/IndiaBusiness demand + new cyberdefence.org.in
hyper-local SEO competitive signal), (3) [SAAS, monitoring only] thin non-branded search demand
(weak, not actionable) - which deserves this week's LinkedIn campaign effort, weighing
differentiation strength, provability/credibility, LinkedIn audience fit, and which bet compounds
best given the zero-engagement baseline on all 4 posts published so far this month.

**Verdict:** 2 of 2 responding models (Claude Sonnet 5, GPT-OSS-120B; Gemini and Mistral returned
provider errors, not counted) independently picked candidate 1 (Money Leaks/Loan Readiness).
Agreement: candidate 1's receipts are first-party and demo-able (test counts, a printable report,
a refusal rule) versus candidate 2's secondhand market-research receipts (pricing guides, one
Reddit thread); candidate 1 is a sharper, harder-to-copy differentiator (a shipped capability vs a
bundling/pricing argument a competitor could copy by editing a line of ad copy); candidate 1 fits
founder-led LinkedIn's native "we built X, here's proof" arc better than a market-chaos argument.
Both models agreed candidate 3 is correctly sidelined as noise. One model (Claude) flagged a real
caveat: if services revenue is the actual near-term bottleneck, candidate 2 could be reconsidered -
but on content strength and audience fit specifically, both favored candidate 1.
**My call:** went with the consensus (candidate 1, specifically Loan Readiness over Money Leaks as
the sharper single-post hook - the "refuses to score, that's the feature" framing is a cleaner,
single-idea hook than covering both features in one post). Money Leaks gets its own future post per
strategy.md's existing guidance against combining both into one generic post. Services/pricing
(candidate 2) stays queued for next week - it did not lose value, it just lost the tie-break this
week on content-quality grounds given the zero-engagement baseline.

**Channels used:** LinkedIn (primary, per strategy.md Channel Plan and brand skill priority).

## Why this (evidence receipt)
- **Strategy pillar:** "Intelligence > Billing (SaaS)" - Pillar 3 in `strategy.md`'s Content
  Pillars, which exists specifically to showcase Money Leaks/Loan Readiness as the post-POS step.
- **Research basis:** `research/2026-10-01_deep-research.md`, Opportunity #1 and Competitive Edge
  #2 - Loan Readiness shipped 2026-09-26 (commit `bcdd40a`), 11 tests, refuses to score under 3
  months of sales data; neither Vyapar nor myBillBook's public comparison pages mention credit-
  readiness scoring or trapped-capital detection anywhere[7][8] (per strategy.md's positioning
  table, confirmed again in this week's research).
- **Differentiator:** vs Vyapar and myBillBook (both on the strategy.md watchlist) - "A billing app
  tells you what you sold. We tell you if you're about to run out of cash" / "whether you're
  bankable" - the real edge is the live positioning-table line for Pillar 3, now backed by a real
  shipped feature instead of a roadmap promise.
- **Success metric:** LinkedIn post engagement (likes + comments + shares) via `get_post_analytics`
  and a direct `linkedin_fetch_post` check, against the 0-engagement baseline set by the 4 posts
  published so far this month (see `learnings/performance-log.md`, 2026-10-01 entry) - check on or
  after 2026-10-08 (one week live).

## Real code basis (git ground truth, not inferred)
`git -C ~/.hermes/workspace/repos/AstraAtlas-AstraStudio log origin/main --oneline --since='7 days ago'`
confirms commit `bcdd40a` (2026-09-26, Vishal Kumar): "feat(finance): Loan Readiness - business
credit profile from sales history" - 0-100 score from consistency/trend/track record/traceable
payments/collections/returns/GST registration; indicative working-capital range by tier, clearly
not an offer; refuses to score under 3 months of sales; per-factor detail and how to improve it;
printable lender-style report; consent-based request for offers, stored with a frozen profile; 11
tests. Diff: 9 files changed, 771 insertions (new `creditProfileService.ts`, `financeRoutes.ts`,
`LoanReadiness` screen, a DB migration for loan interest requests, and the test file). This is a
real, tested, shipped capability - not a vault doc claim and not an inferred milestone.

**Status:** pending_approval. Post id `a2204478-0f2a-4f2a-91a3-1ab2124445f5`, created via
`create_draft`, approval requested via `request_publish_approval` - Vishal notified on Telegram.
Not published - awaiting his click in the admin UI.
