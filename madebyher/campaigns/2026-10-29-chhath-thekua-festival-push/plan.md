# Campaign: 2026-10-29-chhath-thekua-festival-push

## Trigger
Festival-calendar override (campaign-workflow skill). Chhath Puja confirmed 13-16 Nov 2026
(main day 15 Nov, Sunday) - verified live this run via web search (incredibleindia.gov.in,
drikpanchang.com, economictimes.indiatimes.com, divinehindu.in all agree on 13-16 Nov with
Sandhya Arghya on 15 Nov). 17 days out at run time (29 Oct 2026), inside the 21-day ACTIVE
window per docs/festival-calendar.md. This overrides council_review's opportunity pick entirely
per explicit instruction - no council_review run this cycle.

## Objective
Drive awareness and clicks/saves to MadeByHer's flagship Chhath product
(/product/sudh-desi-ghee-thekua) across Pinterest, Instagram, and a blog handoff note - timed
to land well before 15 Nov, not same-day.

## Hypothesis
A craft-authenticity angle ("this is where your thekua is actually made") converts better than
a generic festive post, because the product's own search demand is already real and growing
(GSC impressions 394->478, +21%, over the last two runs) while clicks stay flat at 2 - the
problem is conversion/trust, not demand. Showing the real making-process plus the real product
photo directly targets that trust gap. This also matches strategy.md's documented edge: three
independent competitor sightings (The Thekua Company, Mithila Magic, Golden Nut Goods) are all
running single-SKU discount+bundle mechanics on the same flagship item type - MadeByHer's edge
isn't price right now, it's authenticity/story depth a single-SKU D2C brand doesn't bother with.

## Target audience
Festival food/culture searchers (strategy.md audience segment 2: "sudha thekua price" 26
impressions/28d), gift buyers under Rs 3,000 doing Chhath prasad/gifting, diaspora buyers
ordering thekua shipped for Chhath.

## Why this (evidence receipt)
- Strategy pillar: Deep Bihar Culture (The "Why") - strategy.md Content Pillar 1.
- Research basis: research/2026-10-29-deep-research.md + strategy.md north-star updates
  2026-10-22 through 2026-10-29 - `/product/sudh-desi-ghee-thekua` (Exp 9 target) impressions
  climbed 394->478 (28d GSC, +21%) while clicks stayed flat at 2 for a third consecutive run -
  real, growing search demand not yet converting. Chhath Puja confirmed 13-16 Nov, 17 days out.
- Differentiator: vs Golden Nut Goods / The Thekua Company / Mithila Magic (single-SKU thekua
  D2C brands running discount+bundle mechanics, research/2026-10-22 and 2026-10-29-deep-research.md)
  - MadeByHer leads with real maker-process authenticity and marketplace breadth, not a price
    race on a mechanic Vishal hasn't approved shipping yet (Exp 10, pricing change, still pending
    his sign-off). strategy.md positioning row: "Same trusted desi-ghee thekua... order before
    15 Nov" / "One home for every Bihar craft and sweet, not one brand per recipe."
- Success metric: GSC clicks/impressions on /product/sudh-desi-ghee-thekua (currently 2/478,
  28d) and the exact query "thekua online" (currently 0 clicks per strategy.md); Pinterest/
  Instagram saves and outbound clicks. Checked next research run, 2026-11-02 or later.

## Note on Exp 9/10 (on-page fix, pricing)
This campaign is the social/content lever, not the on-page fix. Exp 9 (title/meta rewrite) and
Exp 10 (scoped discount/bundle, needs Vishal's pricing approval) remain open, unshipped backlog
items flagged separately in strategy.md - this campaign does not substitute for either, and
Vishal should still action Exp 9/10 before 15 Nov per strategy.md's own urgency flag.

## Channels
- **Pinterest** (primary channel per madebyher skill): single pin, real thekua product photo
  framed via brand_media.py (product slide type), destination link to the product page. See
  `pinterest.md`.
- **Instagram** (live since 2026-09-24): 5-slide carousel via brand_media.py - slide 1 generated
  maker-process image (hands frying thekua in a kadhai), slide 2 real product photo, slides 3-4
  text (ritual rules + order-timing urgency), slide 5 CTA. See `instagram.md`.
- **Blog**: no new post this run - two real festival posts already live in the last 48h (Karwa
  Chauth gifts for husband, 52 Buti Saree) and strategy.md's delta explicitly says "do not add
  new content... keep writing for in-stock categories only" with no new Chhath blog angle
  identified as not yet covered. Handoff note only. See `blog-handoff.md`.

## Images
- Pinterest: real product photo (admin_search_products, sudh-desi-ghee-thekua) framed on cream
  via brand_media.py `product` slide type - no AI generation needed or used, verified via
  VisionAnalyze (legible text, correct product, brand-consistent). Pollinations generate_image
  was tried first for a lifestyle shot and produced a wrong, watermarked result (pineapple
  tarts, not thekua) - real observed failure, abandoned in favor of the real-photo-first rule
  since this is a specific-product post anyway.
- Instagram slide 1: brand_media.py Gemini-via-Composio-style gen (using the script's own
  gen_image path) of a maker's hands frying thekua - verified via VisionAnalyze: correct scene,
  legible overlay text, 4:5 aspect, no garbling.
- Instagram slide 2: same real product photo as Pinterest, via `product` slide type.

## Status
- Pinterest: pending_approval, post id ef2f0140-5216-4bac-95c3-8c2d6a03fa47
- Instagram: pending_approval, post id a095cd49-debf-4949-9a99-94cad718bf75
- Blog: drafted (no-op handoff note only)
