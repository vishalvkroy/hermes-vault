# LinkedIn draft — 2026-10-22-services-retainers-launch

**Formula:** F7-adjacent build-log (number/code-line-first opener) + honest bug confession,
closing on a genuine question. Primary goal: comments (testing whether the Services audience
engages at all, not chasing reach).
**Posting window:** Tue/Wed/Thu 7:30-9:00 AM IST (standing Astra Studio LinkedIn guidance).
**Target audience:** Indian consultants, freelancers, agency owners who bill for labour/time.
**Account:** Vishal Kumar (member profile) — manual post, not auto-published.

---

0 <= 0.

That's the line of code that decided whether a WhatsApp low-stock alert fired on every service you ever billed.

Last week I shipped a feature in Astra Atlas: mark a sale line as a service, not stock, so a consultant billing 10 hours of work doesn't get flagged as "out of stock" on something that was never stock to begin with. It reuses our GST billing engine, bills the work with a SAC code in place of an HSN code, and plugs into the retainer invoicing we already had for lump-sum drawdowns.

Building it, I found the bug above. Every service product in the system defaulted reorder_level to 0. Our low-stock check read "stock <= reorder_level." A service has 0 stock too. 0 <= 0 is always true. Every service line item, in every tenant's account, would have fired a false low-stock WhatsApp alert, every single day, forever.

Nobody reported it. It surfaced only because adding Services forced me to re-read every stock-adjacent code path in one sitting.

Four Indian SaaS tools already sell pure service-billing software to consultants and agencies. None of them also run a full retail stock engine underneath. Astra Atlas now runs both, stock and services, through the same books, same P&L, same balance sheet.

The part of shipping fast nobody warns you about: you end up reading your own old if-statements like a stranger wrote them, hoping you don't find what I found.

What's the oldest bug you've caught hiding in your own code?

P.S. The reorder_level bug is already fixed and live, same release.

#BuildInPublic #IndianSaaS #FreelanceIndia

---

**Char count:** ~1,490
**Fact check (quality gate, growth-strategy §7):**
- Feature real, shipped 2026-10-19 00:12 IST, commit `5d5ec76`, confirmed via direct `git show` this run.
- Bug real: `waAlertService.ts` fix is in the same commit (reorder_level default 0 vs stock 0 vs `<=` check). Confirmed via commit diff, not inferred.
- "Four Indian SaaS tools" = 21bill, Arjaka, LekhaPro, 399Apps — all four named and sourced in strategy.md's Positioning table / research/2026-10-19_deep-research.md, not invented.
- No price, no plan-tier claim, no overclaim about e-filing or capability not in the codebase.
- No internal jargon shown ("pillar", "experiment", competitor names used only as real market context, not an attack).
- Link: none in body (LinkedIn body-link penalty). If Vishal wants to link `/service-business-software`, put it in the first comment.

**Humanizer check:** no em/en dashes, no "testament/underscores/pivotal", no forced triads beyond
the one real list (reuses GST engine / SAC code / retainer invoicing — genuine, not padding), no
chatbot sign-off, straight quotes used throughout, one real contrast (stock-tool vs
stock+services), closing question is genuine and specific, first line is a code fact not a
question. Clean pass, no changes needed.
