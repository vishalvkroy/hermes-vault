# Campaign: 2026-10-22-diwali-handmade-gifting

## Trigger
Festival-calendar override (campaign-workflow skill): Diwali / Lakshmi Puja confirmed 8 Nov 2026 (Sunday) - verified live via web search this run (drikpanchang.com, timeanddate.com, news18.com all agree), 17 days out at run time (22 Oct 2026), inside the 21-day ACTIVE window per docs/festival-calendar.md. This overrides the week's council_review opportunity pick per explicit instruction - no council_review was run this cycle.

Karwa Chauth (29 Oct, 7 days out) is also technically inside the 21-day window, but strategy.md closed that exact campaign (Exp 5, crochet-potli push) as a confirmed FAILED experiment this same morning (2026-10-22 update) - 12 days live, 0/0/0 on get_campaign_performance, analytics endpoint now 500-erroring. Re-chasing the same SKU via social this week would contradict that closure. Diwali is MadeByHer's single biggest gifting window (festival-calendar.md) and has no dedicated social push yet this year - picked over Karwa Chauth.

## Objective
Drive clicks/saves to Diwali-relevant product pages (thekua, Madhubani coasters, resin aarti set) and the /gifts/diwali collection, ahead of the 8 Nov festival, across Pinterest, Instagram, LinkedIn.

## Hypothesis
A cross-category hamper framing (food + craft + pooja items together, not one SKU) converts better than a single-product push, because it matches MadeByHer's real competitive edge (marketplace breadth) against The Thekua Company's single-SKU model, and Google Trends shows "diwali gift hampers india" climbing sharply (21->65->100) into this window.

## Target audience
Gift buyers under Rs 3,000 (strategy.md audience segment 1, 84% of Indian gift searches per research/2026-10-01), festival food/culture searchers, visual handmade gift shoppers.

## Why this (evidence receipt)
- Strategy pillar: Deep Bihar Culture + Giftable Handmade Products (strategy.md Content Pillars 1 & 2)
- Research basis: research/2026-10-22-deep-research.md - `/product/sudh-desi-ghee-thekua` moved 0/119 -> 2 clicks/406 impressions (28d) organically this week; Google Trends "diwali gift hampers india" 21->65->100 climbing into 8 Nov; new direct competitor The Thekua Company confirmed on same flagship SKU.
- Differentiator: vs The Thekua Company (single-recipe-per-brand platform, no cross-category hamper) - strategy.md positioning row: "One home for every Bihar craft and sweet, not one brand per recipe." vs Discover Mithila (Madhubani-only, no food category).
- Success metric: GSC clicks/impressions on /product/sudh-desi-ghee-thekua, /product/madhubani-peacock-coasters-with-holder-set-of-6, /gifts/diwali; Pinterest/Instagram saves and outbound clicks; checked next research run, 2026-10-26 or later.

## Channels
- **Pinterest** (primary channel per madebyher skill): single pin, real thekua product photo, destination link to product page. See `pinterest.md`.
- **Instagram** (live since 2026-09-24): 5-slide carousel built via brand_media.py using 3 real product photos (thekua, Madhubani coasters, resin aarti set). See `instagram.md`.
- **LinkedIn**: founder-voice post, contrarian/receipts angle on the new Thekua Company competitor, drafted via linkedin-post-writer approach. See `linkedin.md`.
- **Blog**: no new post - two real Diwali posts already live (19 Oct, 21 Oct). Internal-linking gap flagged instead. See `blog-handoff.md`.

## Image note
Both image-generation paths failed this run and are real, observed blockers, not worked around:
- `generate_image` (Pollinations.ai, hermes-video MCP): 402 Payment Required.
- `brand_media.py image` (Composio GEMINI_GENERATE_IMAGE fallback): 402, "prepayment credits are depleted" (Google AI Studio project).
Both need Vishal's attention (Pollinations account/payment, Gemini AI Studio credits) - flagging, not guessing a workaround. Used real product photos instead (brand_media.py's `product`/`text`/`cta` slide types, no generator call needed) - this is consistent with the skill's own stated preference for real product photos over AI-generated ones on product-specific posts, so the campaign is not weakened by the outage, just missing a lifestyle/mood cover shot it didn't strictly need.

## Status
- Pinterest: pending_approval (post id in todo.md once created)
- Instagram: pending_approval (post id in todo.md once created)
- LinkedIn: pending_approval (post id in todo.md once created)
- Blog: drafted (no-op decision, handoff note only)
