# LinkedIn — 2026-10-01-loan-readiness-zero-score

**Formula:** F7 Odd-Precision Money Ledger family (number-first opener, "Zero" as the odd/stark
number), closing with a genuine question per 2026 algorithm heuristics (never open with a
question, -34% median likes). Pulled from `marketing/linkedin/skills/linkedin-post-writer`.
**Status:** pending_approval, post id `a2204478-0f2a-4f2a-91a3-1ab2124445f5`.
**Char count:** 1,330 (within the 900-1,300 sweet spot band, slightly over, justified by the
substantive factor list - consistent with prior posts' own "don't trim below 1,000" guidance).

---

Zero.

That's the credit score we give a shop with two months of sales data. Not low. None. The refusal is the feature.

We shipped Loan Readiness last week: a 0-100 business credit score built only from a shop's own sales history. No bank statement, no CIBIL pull. It weighs consistency, trend, track record, traceable payments, collections, returns, and GST registration, then refuses to score anything under three months old. 11 tests sit behind that logic, including the one that checks we say no instead of guessing.

What comes out is a printable report, the kind a lender actually reads, plus an indicative working-capital range labelled clearly as not an offer. Requesting one is consent-based, and the request is stored against a frozen profile so nothing shifts under the owner later.

Vyapar and myBillBook both do billing well. Neither turns a shop's own sales history into something a lender can read. A billing app tells you what you sold. We're trying to tell you whether you're bankable.

We also shipped Money Leaks the same week, which puts a rupee number on stock that isn't moving and catches supplier price rises before they eat margin. Separate post, separate number.

What would you want a lender to see about your business that a bank statement alone never shows?

#buildinpublic #IndianSMB #SaaS #Fintech

---

## Humanizer pass notes
Ran against `writing/humanizer` patterns before finalizing:
- No em dashes/en dashes present (checked with grep on the raw text file).
- No inflated-legacy language ("testament", "pivotal", "represents a shift") - stayed to plain
  mechanism description (what the score weighs, what it refuses to do).
- No vague sources - every claim traces to the real commit (`bcdd40a`) and its real test count
  (11), not an invented number.
- No forced triads - the factor list (consistency, trend, track record, etc.) is the real list
  of inputs from the commit message, not manufactured for rhythm.
- No "not only X but Y" construction; one real contrast kept ("A billing app tells you what you
  sold. We're trying to tell you whether you're bankable.") per the Density rule (one contrast
  max).
- No chatbot sign-off, no generic positive ending - ends on the real open question, not a send-off.
- No sales language ("boasts", "cutting-edge", "game-changer") anywhere in the draft.
- One real number-first hook ("Zero"), no rhetorical question as opener, closing question genuine
  and answerable by a real shop owner reader.
