# Campaign: 2026-11-05-chhath-diaspora-gifting

## Trigger / festival check
Chhath Puja confirmed 13-16 Nov 2026 (main day Sunday 15 Nov) - re-verified live this run via
web search (Economic Times, drikpanchang.com, timeanddate.com, News18 all agree on 13-16 Nov,
Sandhya Arghya 15 Nov). 10 days out at run time (5 Nov 2026) - inside the 21-day ACTIVE window
per docs/festival-calendar.md. Per the campaign-workflow override, this is a festival-active
week: council_review's opportunity pick is only used to decide the ANGLE and channel mix this
run (see below), not whether to run a campaign at all - the festival itself sets that.

## council_review question asked (tier=fast - see note)
Note: the campaign-workflow skill's flagship-tier council_review call is reserved for picking
WHICH research opportunity to act on - not applicable this run because the festival-calendar
override (Chhath, 10 days out) already decided the opportunity, per explicit instruction to
skip that pick entirely when a festival is active. The question below is a separate Yellow-tier
channel-mix judgment call (routing-and-approvals skill's aggressive council_review trigger),
correctly run at the default fast tier.

Asked: given the existing Chhath thekua campaign (Pinterest ef2f0140 + Instagram carousel
a095cd49, same flagship product) is stuck in pending_approval for 7 days and now critically
late, should this week's new campaign add ANOTHER Instagram carousel on the same product/
festival (stacking a second unapproved Chhath Instagram ask in Vishal's queue), or stick to
Pinterest + LinkedIn only for the new diaspora angle, deferring a second Instagram post until
the first is resolved?

**Verdict: Claude, Groq, and Gemini all agreed independently** - stick to Pinterest + LinkedIn
this week, do not add a second Instagram carousel on the same festival/product while the first
sits unresolved. Reasoning convergent across all three: stacking two Chhath/thekua Instagram
asks in the same queue creates decision ambiguity and raises the real risk Vishal defers or
conflates both rather than approving either, at a point where the clock (10 days to Chhath) has
no room left for that. Mistral errored (429, rate limited) - 3 of 4 models responded, no
disagreement among them. Followed the verdict: this run ships Pinterest + LinkedIn only. The
stuck Pinterest+Instagram pair's resolution is flagged separately below, not re-raised as new
Instagram content.

## Objective
Convert the diaspora/"ship Chhath home" demand signal (real this week, see evidence) into a
Pinterest pin and a LinkedIn post - two channels that don't collide with the still-pending
first Chhath campaign's Instagram ask - driving clicks/saves to the flagship thekua product
page before the 15 Nov shipping cutoff.

## Hypothesis
The diaspora-gifting angle ("send Chhath home to someone who can't be there") is a genuinely
different hook from the first campaign's "authenticity/maker-process" angle on the same
product - it targets a different trigger (distance/guilt/connection) rather than trust, so it
can run in parallel without being a duplicate message, even on the same SKU.

## Target audience
Diaspora/relocated Bihari buyers (strategy.md audience segments + new evidence below) and
LinkedIn's broader Indian-gifting-trend audience (relevant to seller-acquisition story too,
since MadeByHer's own differentiator is women-led Bihar sellers).

## Why this (evidence receipt)
- Strategy pillar: Deep Bihar Culture (The "Why") - strategy.md Content Pillar 1, whose
  evidence base this run explicitly reinforces (strategy.md 2026-11-05 update: "Reinforced
  Content Pillar 1's diaspora-gifting evidence").
- Research basis: research/2026-11-05-deep-research.md - a Rukam Capital/YouGov survey of 4,002
  respondents (74% buy festival gifts for parents/family; a Rukam Capital partner specifically
  named "regional specialities and fusion mithai" and "homegrown brands" as the categories
  gaining interest) plus Patna Press's report of 100-200 real Manjusha-art Chhath soop orders
  shipped to US-based diaspora buyers this season. Both independently corroborate the thesis
  first established 2026-11-02 via the r/bihar "thora jyada le aana" post and GoKwik/CNBC
  national thekua-demand data - this is now evidenced across two non-food and food categories
  and two separate research runs, not a one-off.
- Differentiator: vs single-SKU thekua D2C brands (The Thekua Company, Mithila Magic, Golden
  Nut Goods, Shuddh Swad - strategy.md positioning table) - none of their public positioning
  leads with diaspora/distance-shipping as the hook; MadeByHer's own product page already states
  "Living outside Bihar and missing home-style Thekua for Chhath? We ship pan-India" (verified
  via live site fetch, madebyher.in/product/sudh-desi-ghee-thekua) - a real, already-true claim
  this campaign surfaces rather than invents.
- Success metric: GSC clicks/impressions on /product/sudh-desi-ghee-thekua (currently 3/558,
  28d per strategy.md 2026-11-05 update) and Pinterest/LinkedIn saves, outbound clicks, and
  engagement. Checked next research run (2026-11-09 or later).

## Note on the still-stuck first Chhath campaign (Exp 12)
This is a SEPARATE, new campaign, not a replacement for the still-unresolved
2026-10-29-chhath-thekua-festival-push campaign (Pinterest ef2f0140, Instagram a095cd49, both
pending_approval 7+ days, get_post now 500-erroring per research/2026-11-05-deep-research.md).
That campaign needs Vishal's approval decision independently - flagged again in the Telegram
summary below, not fixed by this run's new drafts.

## Channels this run
- **Pinterest** (primary channel per madebyher skill): new pin, real product photo framed via
  brand_media.py (product slide type), diaspora-shipping angle copy, destination link to the
  product page. See `pinterest.md`.
- **LinkedIn**: new post using the diaspora/regional-gifting data (Rukam Capital/YouGov survey +
  Manjusha soops), framed as a brand/market-trend story rather than a product pitch, one soft
  mention of MadeByHer's own pan-India shipping as the natural conclusion. See `linkedin.md`.
- **Instagram**: deliberately NOT drafted this run per the council_review verdict above - the
  existing Chhath Instagram ask (a095cd49) is still unresolved; a second one would stack the
  approval queue rather than help it. Resume Instagram cadence next run once a095cd49 is
  resolved either way.
- **Blog**: no new post this run. Two Chhath/Diwali-adjacent posts already shipped in the last
  10 days (52 Buti Saree, Crochet Rose Potli Bag) and strategy.md's 2026-11-05 delta says keep
  writing the heritage/GI-tag angle, not add more festival volume - no new blog angle identified
  as uncovered this run.

## Images
- Pinterest: real product photo (admin_search_products, sudh-desi-ghee-thekua, Rs 339 database
  price) framed on cream via brand_media.py `product` slide type - headline "Sudh Desi Ghee
  Thekua", sub "Order by 10 Nov - ships pan-India for Chhath, Rs 339". Verified via
  VisionAnalyze: product photo sharp and well-styled, headline/sub fully legible, correct price
  and date, cream background brand-consistent. One minor cosmetic note: the real product
  photo's own baked-in kraft-tag label is cropped at the frame edge ("Sudh Desi...") - this is
  inside the sourced photo itself, not something this run's compositing added, and doesn't
  affect the overlaid marketing text.
- LinkedIn: text-only, no image - the post is a market-trend/data story, not a product pin, and
  linkedin-post-writer's own convention is real-photo-first only when illustration genuinely
  helps; a data-led LinkedIn post doesn't need one here.

## Status
- Pinterest: pending_approval, post id bad147d3-9b01-4681-8087-7312a8604223
- LinkedIn: pending_approval, post id 4002236f-312e-4cd2-8d7c-811ed10e8d2a
- Instagram: not drafted this run (see Channels above)
- Blog: no new post this run (handoff: none needed)
