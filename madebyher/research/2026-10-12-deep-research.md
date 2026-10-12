# MadeByHer Research Findings — 2026-10-12

## High-impact opportunity: papad demand hits a 4th consecutive run with zero product, and GLAM21 lip balm's 75% CTR holds up on a slightly bigger base

`best papad brands in india` (1 click / 19 impressions, 28d) and `papad brands` (1 click / 23
impressions, 28d) are still landing on `/blog/top-papad-brands-india-where-homemade-fits` (4
clicks / 310 impressions this period) — real, repeated, search-confirmed demand with still zero
matching product in the catalogue (`admin_search_products` returns zero results for
"papad").[1] This is the fourth straight weekly snapshot (2026-10-01, 2026-10-05, 2026-10-10,
2026-10-12) to show this exact pattern — it has moved past "worth flagging" into "the single
longest-running unresolved gap in this research series," longer-running than Exp 5 (crochet
potli/keychain) was before the Karwa Chauth campaign finally shipped against it.[1]

At the same time, `/product/product-name-glam21-love-tinted-lip-balm` held its 75% CTR from
2026-10-10 (now 3 clicks / 4 impressions, same raw numbers — the 28-day window hasn't rolled past
that activity yet) and the Karwa Chauth campaign built around it published on both Pinterest and
Instagram on 2026-10-10, directly acting on last run's recommendation to scale it.[1]

**Concrete move this week:** (a) Vishal decision still outstanding and now 4 runs old — either
source a papad seller (there is a ready 310-impression blog post to link from on day one) or make
an explicit call to retire/redirect that blog post's targeting; (b) the Karwa Chauth campaign is
live and GSC-measurable from ~2026-10-19 (per its own evidence receipt) — check that first before
starting a new push on the same two products.

## 1. Search intent & demand (GSC + GA4)

### 28-day GSC (sc-domain:madebyher.in)
- Branded search still dominant and ticking up: `madebyher` 107 clicks / 143 impressions (74.8%
  CTR, pos 1.40, up from 102/141 on 2026-10-10); `made by her` 29/141 (20.6% CTR, pos 3.70).[1]
- Repeated low-CTR demand unchanged in shape: `sudha thekua price` 1/28 (3.6% CTR, pos 8.0, was
  1/24), `khatwa applique work` 1/15 (6.7%, pos 9.3, flat), `papad brands` 1/23 (4.3%, pos 12.0,
  was 1/19), `best papad brands in india` 1/19 (5.3%, pos 7.6, was 1/18) — all four queries present
  again, same pages, same non-conversion.[1]
- Best-converting non-branded query this period unchanged: `glam 21 love swipe lip balm brownie
  fudge` 2/3 (66.7% CTR); `sell handmade items online free in india` 1/1 at position 1 again.[1]
- Top pages 28d: homepage 156 clicks / 854 impressions (up from 149/780); `/sell` 24/174 (13.8%
  CTR, impressions recovering from last run's 165 dip); `/blog/wedding-return-gifts-under-300`
  6/198; `/blog/pedakiya-vs-gujiya-comparison` 4/538 (0.74% CTR — still flat, same unresolved
  pattern flagged every run since 2026-09-28); `/blog/top-papad-brands-india-where-homemade-fits`
  4/310 (1.29% CTR); `/shop` 4/439 (0.91% CTR — still the weakest major page, consistent with the
  strategy.md "do not push /shop" rule); `/product/handmade-crochet-rose-drawstring-mini-potli-bag`
  3/283 (1.06% CTR); `/product/product-name-glam21-love-tinted-lip-balm` 3/4 (75% CTR,
  unchanged).[1]

### 7-day GSC
- Karwa Chauth campaign's own target page now shows direct 7-day movement:
  `/product/handmade-karwa-chauth-thali-set-with-channi-and-lota` 1 click / 8 impressions — new
  in this week's 7-day page table, consistent with the thali/sargi merchandising on
  `/gifts/karwa-chauth` that the campaign's own plan.md referenced as present but not featured.[1]
  Also new this week: `/product/handmade-crochet-sunflower-bouquet` 1/3 and
  `/product/handmade-flowers` 1/1 (100% CTR, tiny base) — both plausibly downstream of the same
  campaign's product push onto the crochet-gifts shelf, though GSC's own ~3-day lag means this is
  a 2-day-old campaign only partially visible yet, not a confirmed result.[1]
- The two Exp-5 target queries from the campaign itself (`crochet rose potli bag`, `daisy flower
  keychain`) have rolled out of this week's top-25 7-day query list entirely — too early to read
  as "fixed," since the campaign published only 2 days ago and GSC's own lag window hasn't fully
  cleared; check again next run before concluding anything.[1]
- `/sell` 7d: 6 clicks / 44 impressions (13.6% CTR) — consistent with its established
  high-CTR acquisition pattern.[1]

### GA4 (property 553055822)
GA4 did not return usable data this run. Every `days=` value tried (1, 3, 7, 10, 14, 28, 35, 40,
45, 60, 90) returned an identical single row — "Direct: 2 sessions, 1 active user, 50% bounce" —
regardless of window size, which is itself evidence the tool returned a stale/cached result
rather than a real differently-scoped query; repeated calls then tripped the MCP server's
same-failure guard and it went unreachable.[2] This is a clear regression from 2026-10-10, where
the identical property/format combination (`"0553055822"`) returned a real 28-day channel split
(Organic Search 382, Direct 201, AI Assistant 155, etc.) in the same research series.[2] Treating
this run's "2 sessions" as real traffic would contradict the brand's own prior verified numbers
from two days ago — flagged as a tool issue, not reported as a traffic collapse. GSC, which is a
separate system, shows no site-wide anomaly (homepage impressions actually rose 780→854), so this
looks GA4-tool-specific, not a real-world drop.[1][2]

## 2. Niche trends & market signals

Google Trends (via Composio `COMPOSIO_SEARCH_TRENDS`) on three seed terms over the last several
weeks: "handmade gifts india" stayed flat-to-negligible (0-14 on Google's 0-100 relative scale,
most recent full week at 0) with no clear seasonal lift yet;[3] "chhath puja gifts" returned no
Google Trends data at all ("hasn't returned any results for this query" — the term itself may be
too narrow/compound for Trends' own indexing, not evidence of zero interest); "karwa chauth gift"
is climbing sharply and recently — 14 (week of Aug 30), 14, 22, 41, 43, 78, then 100 (the week of
Oct 11-17, the current week) on Google's relative 0-100 scale — a real, currently-peaking search
trend landing in the exact week the Karwa Chauth campaign published.[4] This corroborates, with an
independent source, that the campaign's timing call (19 days out from the 29 Oct festival,
decided via council_review on 2026-10-10) lined up with real rising search interest rather than
an assumed festival-calendar date alone.[4]

Reddit's r/smallbusinessindia has fresh (within 24-48h) Diwali 2026 gifting activity: a post titled
"Diwali gift ideas under ₹549" (30 upvotes, 32 comments — the highest-engagement thread seen in
this subreddit across this research series to date)[5] and a maker's personal story of handmade
clay/pipe-cleaner diyas going from hobby to a sold-out office exhibition stall (6 upvotes, 22
comments)[6], plus a separate ask for "Diwali-themed, college-friendly gifting options under ₹40
per piece" with bulk-order interest (1 upvote, 5 comments)[7]. All three are seller-side/community
chatter (vendors and hobbyists talking to each other, not consumer demand signal), but the ₹549
and sub-₹40 price anchors both sit inside or below MadeByHer's existing low-ASP gifting range, and
the volume/engagement on the ₹549 thread is a new high-water mark worth noting for how active this
specific community currently is around Diwali.[5][6][7]

r/crochet in the same window skewed toward hobbyist content (a beginner's granny-square project at
34 upvotes, a $3.27 Walmart Halloween crochet kit teardown at 55 upvotes) rather than anything
India-specific or commerce-relevant — no useful signal for MadeByHer's crochet-product angle this
run.[search via Composio REDDIT_SEARCH_ACROSS_SUBREDDITS, no citable individual claim beyond the
general observation above]

YouTube transcript pull was not attempted this run, consistent with the prior two runs' noted
yt-dlp bot-check block (2026-10-05, 2026-10-10) — not re-attempted without a new mitigation.
Instagram competitor research was again skipped: the Composio Instagram connection reads only
MadeByHer's own account, not public hashtags or competitor accounts (unchanged limitation, same as
every prior run).

## 3. News and articles

**New competitor found this run: Discover Mithila (Mithila Dharohar).** Founded 2026, a dedicated
Madhubani/Mithila heritage marketplace headquartered with dual Delhi + Bihar fulfillment hubs,
explicitly positioned against "the predatory middleman economy in rural Bihar" where "master women
artists were traditionally paid pennies while third-party commercial distributors sold
machine-printed replicas online at 10x markups."[8][9] Its own fact sheet claims 200+ women
artisans directly associated across 4 primary districts in Northern Bihar (Rasidpur and Rajnagar
in Madhubani district specifically named for the Kachni fine-line painting tradition), and 70%+ of
proceeds allocated to artisans.[9] This is the first time a competitor matching MadeByHer almost
exactly on region (Bihar), craft focus (women artisans, Madhubani among others), and founding year
(2026) has surfaced in this research series — see Competitive Edge below for what's actually
different.

A separate web search also surfaced **Mithila Melange**, described as an early-2026-launched D2C
brand selling handcrafted Mithila art products for corporate and festive gifting.[10] This is a
single-brand D2C player (similar in shape to MomsMade for thekua), not a multi-seller marketplace
like MadeByHer or Discover Mithila — logged as an adjacent watch, not a head-to-head competitor,
pending more evidence of its actual scale.

Weavehand (already on the watchlist) is running an active Diwali-season B2B/corporate gifting push
on LinkedIn as of mid-September, pairing handloom textiles with Madhubani and Tikuli art and
explicitly soliciting bulk corporate orders — a continuation of its existing Corporate
Gifts/Festivals category strategy already logged 2026-10-05, not a new capability, but confirms
that push is currently live and active, not dormant.[11] iTokri's Festive 2026 technique-first
collection (first flagged 2026-09-28/10-01) continues to generate press coverage into October,
confirming it's still the live current campaign, not a one-off launch announcement.[12]

## Competitive Edge

### 1. Gap: Discover Mithila directly contests MadeByHer's sharpest claimed differentiator (Bihar-origin, women-artisan-direct)

MadeByHer's own strategy.md leads with "Deep regional focus (Mithila/Magadh/Bihar food/craft)" and
"direct Bihar women-led brands" as its primary edge over generalist marketplaces.[research basis:
strategy.md] Discover Mithila makes almost the identical claim — direct-to-artisan, Bihar/Mithila
region specifically, women artisan collectives, anti-middleman positioning — down to naming actual
Madhubani districts (Rasidpur, Rajnagar) the way MadeByHer's own copy names Aurangabad.[8][9]

**Worth closing?** Yes, but carefully — Discover Mithila's current range (per its own homepage) is
narrower: paintings, clothing, religious items, and gift boxes, all under the Madhubani/Mithila art
umbrella specifically, not MadeByHer's broader food + craft + jewelry + cosmetics mix across 15
women-led shops.[8] MadeByHer's real edge isn't "we are also Bihar" (no longer unique) — it's the
multi-category marketplace breadth (food like thekua/nimki alongside craft) that Discover Mithila
doesn't currently offer, per its own site.[8]

**Concrete move:** Sharpen positioning copy (site, social, blog) away from "we are a Bihar women's
marketplace" (now contested) toward the specific thing Discover Mithila's own site shows it does
NOT do: homemade food alongside craft, and a wider multi-craft mix (crochet, jewelry, cosmetics)
beyond Madhubani art specifically. This is a copy/positioning fix, not a product gap — don't
invent urgency to add a Madhubani-only vertical to compete head-on; compete on breadth instead,
which is a real, provable difference today.[8]

### 2. Gap carried forward, now 4 consecutive runs old: papad search demand with no product (see High-impact opportunity above)

Same gap as 2026-10-01/10-05/10-10, now with a fourth consecutive confirmation and no change in
status. **Worth closing?** Depends on seller sourcing — outside this agent's remit, flagging again
to Vishal rather than manufacturing a content-only fix for a fourth time. **Concrete move if
sourced:** unchanged — the existing 310-impression blog post is a ready internal-link target.[1]

## Sources

[1] https://search.google.com/search-console
[2] https://analytics.google.com/analytics/web/553055822
[3] https://trends.google.com/trends/explore?q=handmade%20gifts%20india
[4] https://trends.google.com/trends/explore?q=karwa%20chauth%20gift
[5] https://www.reddit.com/r/smallbusinessindia/comments/1x378yo/diwali_gift_ideas_under_549
[6] https://www.reddit.com/r/smallbusinessindia/comments/1x0ixhi/my_wife_started_making_handmade_diwali_diyas_at
[7] https://www.reddit.com/r/smallbusinessindia/comments/1x388t1/diwalithemed_collegefriendly_gifting_options
[8] https://www.discovermithila.com
[9] https://www.discovermithila.com/about
[10] https://yourstory.com/companies/mithila-melange
[11] https://www.linkedin.com/posts/weavehand_corporategifting-diwaligifting-b2bgifts-activity-7506736125730848768-GPj2
[12] https://www.tribuneindia.com/news/business/itokri-opens-festive-2026-with-the-technique-as-the-collection-bandhani-to-banarasi-every-shelf-named-by-its-craft
