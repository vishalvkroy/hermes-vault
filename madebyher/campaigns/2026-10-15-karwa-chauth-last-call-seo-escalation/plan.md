# Campaign Plan: Karwa Chauth Last-Call Pinterest + On-Page SEO Escalation

**Campaign ID:** 2026-10-15-karwa-chauth-last-call-seo-escalation
**Date:** 2026-10-15
**Status:** Pinterest pending_approval (see post id below). On-page SEO fix escalated to Vishal
(this agent has no DB/CMS write access - flagged, not executed). No new Instagram/LinkedIn post
this run (see Channels section for why). Blog = no new post, existing coverage sufficient.

## Festival check (campaign-workflow + festival-calendar.md)

Two festivals inside the 21-day active window as of today: Dussehra (20 Oct, 5 days out) and
Karwa Chauth (29 Oct, 14 days out). Both already got full dedicated campaigns this cycle -
Dussehra (`2026-10-01-dussehra-festive-shelf`, confirmed published Pinterest+Instagram+LinkedIn)
and Karwa Chauth (`2026-10-10-karwa-chauth-potli-keychain-push`, confirmed published: Pinterest
post `31a085ea` provider_post_id `1136596024741284409`, Instagram post `04c8dd75` provider_post_id
`18150761536547736`, LinkedIn post `97e42305` internally flagged `failed` but independently
confirmed live via `linkedin_fetch_post`, 2 likes - known tool status-check bug, not a real
publishing failure, per `performance-log.md` 2026-10-15 entry).

Because a third near-identical social push isn't a mechanical read of the brand skill (the
calendar's "within 21 days = always run a new push" default collides with 3 consecutive weeks of
flat GSC data on the campaign's own target metric), this was routed through `council_review`
tier=flagship rather than assumed.

## council_review (tier=flagship)

**Question asked:** Given both festivals already have confirmed-published campaigns, the Karwa
Chauth campaign's own target metric (`crochet rose potli bag` GSC clicks) hasn't moved in 3
consecutive weekly runs despite Google Trends showing demand still climbing (65->100 week over
week, 14 days out), and this week's research doc's own top-billed recommendation is an on-page
title/meta fix rather than more social volume — should this week's campaign be (A) a third
near-identical Karwa Chauth social push, (B) skip new Karwa Chauth/Dussehra social content and
instead center the week on flagging the on-page SEO fix to Vishal plus one genuinely fresh-angle
"last call" Pinterest push riding the trend peak, or (C) pivot the week to early Diwali prep
content since its 3-6 week custom-order lead window just opened?

**Verdict:** Claude Sonnet 5 and GPT-OSS-120B (Groq) both responded; Gemini (502) and Mistral
(429) failed with transport errors, not a disagreement. Both responding models independently and
clearly recommended **(B)**. Shared reasoning: three flat weeks of 0 clicks despite rising
impressions diagnoses an on-page/landing problem, not a reach problem — repeating the same social
creative a third time has no mechanism to produce a different result, and the research doc's own
diagnosis already said so. Diwali (C) is real but still outside the 21-day active window and
abandons a live, quantified, still-growing opportunity (Karwa Chauth demand) in favor of one that
hasn't opened its trigger window yet — queue Diwali for next week, don't let it hijack this one.
Both models agreed B's shape should be: escalate the on-page fix as the week's highest-leverage
item (even though this agent can't execute it directly), plus exactly one fresh, differentiated,
urgency-framed Pinterest push (not a repeat of the existing creative) to capture the final 14 days
of climbing trend interest. Decision: proceed with (B), as both models converged with no
divergence to adjudicate.

## Why this (evidence receipt) - growth-strategy skill

- **Strategy pillar:** Pillar 2, Giftable Handmade Products (`strategy.md`) — continuing Exp 5,
  now escalating past social-only tactics per the strategy's own Experiment Backlog entry: "Exp 5:
  ...SHIPPED 2026-10-10, NOT YET WORKING as of 2026-10-15... Needs an on-page fix next" and Exp 8
  ("On-page title/meta rewrite... time-sensitive").
- **Research basis:** `research/2026-10-15-deep-research.md` top opportunity section — GSC 7-day:
  `crochet rose potli bag` 0 clicks / 17 impressions, pos 8.29, unchanged from before the campaign
  shipped; Google Trends `karwa chauth gift` 65 (wk Oct 4-10) -> 100 (wk Oct 11-17, partial, current
  peak). The research doc's own explicit recommendation: "a title/meta/on-page fix, not a 'wait for
  Pinterest' fix."
- **Differentiator:** Named competitor - Weavehand and Discover Mithila (watchlist.md) both lean
  on direct-artisan, made-to-order positioning as their edge. This campaign's angle: the potli bag
  and keychain are made to order by one named woman artisan (Yasmin Crochet), not bulk-sourced
  inventory - a real, provable difference the copy states plainly (same claim basis as the prior
  Karwa Chauth campaign, now framed with urgency since the festival is 14 days out).
- **Success metric:** GSC clicks on `crochet rose potli bag` query and
  `/product/handmade-crochet-rose-drawstring-mini-potli-bag` page row (currently 0 clicks 7d),
  checked 2026-10-22 (after both the on-page fix, if made, and this Pinterest push have had time
  to register). Secondary: Pinterest saves/outbound clicks on this specific pin.

## On-page SEO fix (escalated to Vishal, not executed by this agent)

This agent has no CMS/DB write access to the product page. Flagging as the single highest-leverage
action this week, per both council_review models:

- **Page:** `/product/handmade-crochet-rose-drawstring-mini-potli-bag`
- **Problem:** 3 consecutive weekly GSC pulls show 0 clicks despite 7-17 impressions/week on the
  exact query "crochet rose potli bag" - title/meta currently doesn't literally contain that
  phrase in a way that's winning the click at position ~8.
- **Proposed fix:** rewrite page `<title>`/meta description to literally include "crochet rose
  potli bag" in the visible title, matching searcher wording exactly (research doc's exact
  recommendation).
- **Why now:** Google Trends shows "karwa chauth gift" interest still peaking (100/100) with 14
  days left before the festival passes - a fix made this week still has a window to matter.
- **Status:** Flagged in Telegram summary below. Not attempted via any workaround - Yellow/Red
  tier (production content change outside this agent's access), needs Vishal or an engineer.

## Real product basis (admin_search_products, prices confirmed live today)

- Handmade Crochet Rose Drawstring mini potli bag — Rs 689 (23% off from Rs 899), seller Yasmin
  Crochet. Confirmed live via WebExtract of the product page today - made to order, one of one,
  customisable, Deep Red colour shown.
- Handmade daisy flower keychain — Rs 190 (36% off from Rs 299), seller Yasmin Crochet. Confirmed
  live via WebExtract today - made to order.

Both are the same real, in-stock, currently-catalogued products as the 2026-10-10 campaign - no
new SKU needed, this is a fresh creative angle on the same two products, not a new product claim.

## Channels

1. **Pinterest (primary, per skill's channel priority)** — see `pinterest.md`. New "last call,
   14 days left" urgency framing, NOT a copy of the 2026-10-10 pin. New generated hero image
   (brand_media.py Gemini path, UGC flatlay register, countdown/urgency visual cue), cropped to
   1000x1500 Pinterest-native.
2. **Instagram** — skipped this run. The Karwa Chauth carousel (6 slides, published 2026-10-10)
   is 5 days old and per the social-SEO playbook's cadence guidance (3-4x/week max, quality over
   volume), posting a second Karwa Chauth carousel this soon on the same products without a
   meaningfully different format would risk feed fatigue on a still-small, new account rather than
   adding real reach - council_review's verdict was explicitly "one Pinterest push," not a
   full repeat across every channel.
3. **LinkedIn** — skipped this run. The founder-voice LinkedIn post about this exact gap ("3
   weeks. 13 and 17. Zero.") already ran 2026-10-10 and is confirmed live. A second LinkedIn post
   restating the same unresolved number five days later would read as repetitive, not a fresh
   founder angle - no genuinely new LinkedIn-native story this week.
4. **Blog** — no new post. No new angle beyond what's already covered; this week's real content
   gap is the on-page fix on an existing page, not a new article.

## Image sourcing (visual-content-prompts skill)

UGC-register flatlay prompt via `brand_media.py image` (Gemini path) directly - skipping the
Pollinations first-attempt step since the prior two campaigns both hit real, documented
Pollinations failures (watermark, malformed crochet texture) on this same product category;
going straight to the proven fallback saves a wasted call. Scene: the crochet rose potli bag in
Deep Red and the daisy keychain, styled with a small paper "14 days to Karwa Chauth" countdown
card (text composited in training data risk - avoided, see result), diya and marigold petals,
warm natural window light, shot-on-phone framing, slightly off-center. Checked result with VisionAnalyze before using: no watermark, no garbled text, both products
clearly recognisable, no hands/people, minor rustic imperfections (stray petal debris, frayed
cloth edge) judged as acceptable UGC-register texture, not defects. Cropped to 1000x1500 via
Cloudinary `c_fill,g_auto` transform, re-verified 200 OK after crop.

## Real outcome this run (2026-10-15)

**Pinterest** - account `madebyher001` (social_account_id `0443dcf2-8727-44b1-b057-d637e76afc88`).
Post id `1cc5041b-9724-47a2-a906-185cc1ddc6cf`, status `pending_approval`, `request_publish_approval`
called successfully. Nothing published yet.

(Note: an earlier `create_draft` call in this run, post id `062f4ebd-28a6-4ddb-a8a6-ae5830c09a9b`,
was made with title-only text content before the full caption was ready - superseded by
`1cc5041b` above, no `request_publish_approval` was called on it, it sits inert and can be
ignored or deleted by Vishal if the admin UI shows it as a stray duplicate.)

**Instagram / LinkedIn** - deliberately skipped this run, see Channels section above.

**On-page SEO fix** - not executed (no CMS/DB write access). Flagged to Vishal in the Telegram
summary.

Per campaign-workflow's corrected mechanism: `create_draft` always lands `pending_approval`;
`publish()` was never called. Nothing is "published" until Vishal's own click in
social.madebyher.in sets it and a `provider_post_id` is confirmed via a later `get_post` check.
