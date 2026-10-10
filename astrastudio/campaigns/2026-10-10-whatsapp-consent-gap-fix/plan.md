# Campaign: 2026-10-10-whatsapp-consent-gap-fix

**Objective:** Founder-led LinkedIn post demonstrating a real, self-caught DPDP-compliance fix in
Astra Atlas's own POS (the WhatsApp-marketing consent checkbox was entirely absent from the
"existing customer" entry path, not just hidden) - a concrete engineering-quality story tied
directly to the existing Spark WhatsApp-consent narrative already documented in `docs/free-tools.md`.

**Hypothesis:** A specific, self-audited bug-and-fix story (real commit, real DPDP stakes, a
precise before/after) earns more trust and engagement from a founder/SMB-software audience than
a market-positioning argument built on secondhand evidence (Reddit threads), because it is
first-party, provable, and the kind of "we checked our own work" story that LinkedIn's founder
audience responds to. Tempered by the standing distribution problem below - see note.

**Target audience:** Indian SMB retailers/shopkeepers already using or evaluating WhatsApp
marketing via Spark/Astra Atlas; the "GST-Scared SMB" segment from strategy.md (compliance-anxious
buyers); secondary audience of founders/operators who engage with real build-in-public content.

**Which research finding this responds to:** `research/2026-10-09_deep-research.md`, "Internal
Ground Truth" section, commit `9c6d047` (2026-10-03) - the POS consent-checkbox gap fix, read via
real `git show`, not inferred. Cross-checked against `docs/free-tools.md`'s existing Spark/DPDP-
consent narrative - this is a continuation of a real documented product story, not an invented one.

**Decision process - council_review (tier=flagship):**
Question asked: given two real evidence-backed candidates from 2026-10-09 research - Candidate A
(SaaS: the POS WhatsApp-consent gap fix, commit 9c6d047, a genuine self-caught DPDP-compliance
hole) vs Candidate B (Services: r/IndiaBusiness freelancer-pricing-floor evidence, reinforcing the
"not a freelancer side-gig" differentiation line for the Services pricing-transparency post) -
which deserves this week's LinkedIn slot, given founder-LinkedIn fit, differentiation
strength/provability, and the account's standing zero-engagement/no-visible-follower-count
problem flagged as this week's top research priority.
**Verdict:** Only 1 of 4 models returned a usable answer (Groq/GPT-OSS-120B; Claude 502'd, Gemini
timed out, Mistral 429'd) - a genuinely degraded council run, reported plainly rather than treated
as full consensus. The one answer favored Candidate A: a verifiable, auditable commit (hash,
before/after UI behavior, a legal hook - DPDP) beats a secondhand market observation (Reddit vote
counts, no proprietary data) on credibility and shareability; it also fits founder-LinkedIn's
native "we built X, found a problem in it, fixed it" arc better than a pricing-positioning
argument. It flagged that whichever post runs, the real blocker this week is distribution/reach,
not content quality, and recommended treating the post as a reach-building vehicle (real
specificity, a genuine discussion question) rather than skipping the slot entirely.
**My call:** Went with Candidate A given the single response and because it independently matches
my own read of the two candidates' evidence quality (first-party commit vs secondhand market
chatter) - but flagging the thin council result honestly rather than presenting it as 4-model
consensus. Services/pricing (Candidate B) stays queued, not dropped - it's a real, evidence-backed
angle and can run next week if the research still supports it.

**Channels used:** LinkedIn (primary channel for this brand, per strategy.md and the brand skill).

## Why this (evidence receipt)
- **Strategy pillar:** none of strategy.md's 3 named pillars (Transparency Play, Compliance Watch,
  Intelligence > Billing) describes this exact angle precisely - it is closest to Compliance Watch
  (SaaS), extended from "GST/e-invoicing compliance" to "DPDP consent compliance," both real
  regulatory-compliance stories about the same product. Logged here as a Compliance Watch post;
  if this becomes a recurring angle (compliance-gap self-audits), worth a future strategy.md
  review to confirm the pillar should explicitly cover DPDP alongside GST.
- **Research basis:** `research/2026-10-09_deep-research.md`, Internal Ground Truth, commit
  `9c6d047` (2026-10-03) - real `git show`-verified diff: consent checkbox existed only in the
  POS "new/quick customer" entry branch; picking an existing customer from search hit a different
  code path with zero consent UI. Cross-referenced against `docs/free-tools.md`'s existing Spark/
  DPDP-consent documentation (added 2026-09-17) confirming this is a continuation of a real,
  already-documented compliance story, not a one-off invented claim.
- **Differentiator:** vs Vyapar and myBillBook (strategy.md's Positioning table) - their public
  comparison/marketing copy is entirely about billing speed, sync, and reminder automation; neither
  publicly discusses consent-collection completeness or DPDP compliance depth in their own product.
  This post doesn't claim superiority outright - it shows a real audit-and-fix, which no
  competitor has published an equivalent of.
- **Success metric:** direct `linkedin_fetch_post` likes/comments/shares, checked 2026-10-17 (7
  days post-live) and again 2026-10-24 (per the standing performance-log cadence). Given the
  account's current zero-engagement/no-follower-data pattern, this post is also implicitly a data
  point for Experiment #3 in strategy.md (distribution problem, not content problem) - record the
  result there either way, not as a verdict on this post's content quality alone.

## Standing flag carried over from research (not acted on this run, reported to Vishal)
Research explicitly named the zero-engagement/no-visible-follower-count pattern (6 LinkedIn + 1
Instagram posts, 6+ weeks, all zero) as the single highest-priority open question this week,
above picking new content. This campaign still drafts a post (per the brand's standing LinkedIn
cadence and because holding the slot indefinitely isn't itself a strategy), but the real unresolved
item - whether the LinkedIn profile has close to zero followers - needs a direct answer from
Vishal before another week of content-only responses to this problem.
