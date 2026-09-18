# Campaign Plan: Dussehra Early-Lead Pinterest Push

**Campaign ID:** 2026-09-19-dussehra-early-lead-pinterest
**Date:** 2026-09-19
**Status:** see per-channel outcomes below

## Why this run exists (override note)

Vishal explicitly requested this campaign today (2026-09-19) for Dussehra (20 Oct 2026), 31 days
out - beyond the normal 21-day festival-active threshold in `docs/festival-calendar.md`. Treated
as this run's active-festival override, same as the calendar rule would trigger once inside 21
days. The extra lead time is deliberate: sellers need to prep stock and content well before the
window, not scramble inside it. This is a one-off early run, not a change to the 21-day rule
itself - that rule stays as written in `festival-calendar.md` for every other festival/cycle.

## council_review

Not triggered. This is a mechanical, explicit-instruction run (Vishal named the festival, the
date, and the channel priorities directly) - not an ambiguous weekly pick between competing
opportunities. Per routing-and-approvals, council_review is for genuine judgment calls, not a
direct read of an explicit instruction.

## Objective

Get Dussehra-timed Pinterest content live now (31 days out) so it has time to accumulate saves
and search impressions before the date, and queue one LinkedIn post if a genuine non-generic
angle exists. Dussehra itself is a modest gifting occasion for MadeByHer's categories (home
decor, small idols/torans) but its real value per `festival-calendar.md` is as the **lead-in to
the festive season** - shoppers start festive browsing/purchasing from Dussehra through Diwali.

## Hypothesis

Pinterest search volume for festive home-decor and small-gift terms starts climbing at Dussehra,
before the Diwali spike. A pin live 31 days ahead has time to get indexed and accumulate saves
before that search volume peaks, unlike a pin posted inside the usual 21-day window that's still
competing for initial traction as search interest is already rising. Getting there first, while
competitors (per `competitors/watchlist.md`) are still running only Rakhi/Teej content, is a
real first-mover gap - none of the tracked competitor set has a live Dussehra-specific angle as
of this run.

## Target Audience

Festival gift/home-decor shoppers (women 25-45, India + diaspora) starting their festive-season
browsing at Dussehra - early planners who buy across Dussehra through Diwali rather than
single-festival shoppers who wait for Diwali week itself.

## Research Finding This Responds To

`docs/festival-calendar.md` Dussehra row (confirmed 2026-09-19 via drikpanchang.com/samvat.in):
"Marks the start of the festive gifting season lead-in to Diwali - home decor, small
idols/torans, gift-ready packaging as shoppers begin festive purchases; also genuine window for
Durga Puja-adjacent craft angles if sourcing supports it."

No dedicated MadeByHer research file has scored a Dussehra-specific opportunity yet (the
2026-09-04 research run's Opportunity Scoring table covers GI-onboarding and the compressed
Diwali+Chhath window, not Dussehra individually) - this campaign is grounded in the festival
calendar doc's own relevance notes plus the explicit ask, per the campaign-workflow rule to draft
from the brand's static/documented context when no fresher research covers the specific angle.

No `## Competitive Edge` section exists in the latest research file for this cycle.

## Channels Used

1. **Pinterest** (primary, live account @madebyher001) - see `pinterest.md`, outcome below.
2. **LinkedIn** (secondary, live account Vishal Kumar) - see `linkedin.md`. Genuine angle found:
   the real gap between Dussehra (20 Oct) and Diwali (8 Nov) this year is 19 days - a concrete,
   verifiable production-lead-time fact for artisan sellers, distinct from the prior
   Diwali-Chhath 5-day-gap post (2026-09-06) which covered a different pair of festivals.
3. **Blog** - no post drafted this run (daily blog cron owns full posts). Wrote a concrete
   topic-queue note in `blog-angle-note.md` instead, per this run's instructions.
4. **Instagram** - not connected for MadeByHer per `hermes-social` `list_accounts` check this
   run. Skipped; no plain-file draft written since Pinterest already carries the visual channel
   for this campaign and Instagram isn't part of this run's explicit channel list.

## Image sourcing

Checked `admin_search_products` first for a real Dussehra-relevant product photo (idols, torans,
home decor, wall art, Ganesh) - no matching real product in the catalog this run (searches for
"toran", "idol", "wall art", "ganesh", "decor" all returned empty; catalog is presently weighted
toward Madhubani coasters/organizers, crochet items, Laddu Gopal jhulas, and beauty/wellness
items, not Dussehra-specific decor). Per campaign-workflow, fell back to `generate_image`
(Pollinations) using the `docs/visual-references/festival-border-template.png` folk-art frame
style (peacock, lotus, fish, Ganesh-and-elephant corner, Warli village strip, cream/red/green/
gold, aged-paper texture, blank text-safe center, no in-image text requested) rather than a
generic AI composition - matches MadeByHer's documented visual-reference guidance for festival
posts needing a text/product overlay.

## Real outcome this run (2026-09-19)

**Pinterest** - draft `293dbc89-41a9-4a12-af19-f1ac582af5f8` created via `create_draft` with the
generated folk-art image attached. `publish()` was attempted immediately per the campaign-workflow
skill's stated auto-publish behavior; the live `hermes-social` gateway refused with a 403:
`"status 'pending_approval', not 'approved' - publish refused. Use social.request_publish_approval()
first."` This is the same gateway-vs-skill-doc discrepancy already flagged in the
2026-09-13-gi-tag-authenticity-onboarding campaign - the gateway still gates on an `approved`
status Vishal has to set manually, contradicting the campaign-workflow skill's "posts are created
pre-approved now" note. **Nothing published.** Called `request_publish_approval()` so it surfaces
in Vishal's Telegram approval queue.

**LinkedIn** - draft `b9fe2877-cc43-4c28-a70c-b4e480493bc3` created, same 403 on `publish()`, same
`request_publish_approval()` fallback. **Nothing published.**

**Blog** - no post drafted (by design, daily cron owns full posts). `blog-angle-note.md` written
with a concrete Dussehra-Diwali timing angle queued for tomorrow's run.

**Instagram** - skipped, not connected for MadeByHer (`list_accounts` confirms only pinterest +
linkedin connected).

## Flag for Vishal

Second cycle in a row (09-13, now 09-19) where `publish()` is refused with `pending_approval` even
though the campaign-workflow skill describes auto-publish/pre-approved posts as current behavior.
Worth reconciling the skill doc against actual gateway behavior, or confirming the gateway's
approval gate is the intended real state and the skill note is stale.

## Outcome
Pending Vishal's approval action in the Telegram queue - Phase 4 fills in metrics once posts are
approved, actually publish, and run long enough to measure.
