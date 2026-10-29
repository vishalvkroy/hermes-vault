# MadeByHer Deep Research — 2026-10-29

## Top Opportunity (don't bury this)

**Golden Nut Goods (goldennutgoods.com) is a THIRD head-to-head competitor on MadeByHer's own flagship
SKU, Patna-based, single-employee, founded 2026 — and it is running a live -20% discount on its
jaggery thekua (₹399 → ₹319) plus two bundled combo packs, shipping nationwide (Patna, Delhi, Mumbai,
Bangalore, Hyderabad, Chennai, Pune, Kolkata).[4][5] This is now the THIRD
single-SKU thekua D2C brand found in five research runs (The Thekua Company 2026-10-22, Mithila Magic
2026-10-26, Golden Nut Goods this run) — thekua-as-a-standalone-brand is a confirmed, repeating pattern
in this market, not a one-off. MadeByHer's own flagship thekua page
(`/product/sudh-desi-ghee-thekua`) still has **no size-tier packaging, no visible reviews, and no live
discount mechanic** — three runs after Exp 9 (on-page fix) was first proposed and two after Exp 10
(scoped Chhath discount) was proposed, neither has shipped. Chhath Puja 2026 falls 13-16 November —
17 days out from this run — so the window to ship either before the festival's main day (15 Nov) is
narrowing fast.[2]

## Search Intent (GSC + GA4)

**GSC (`sc-domain:madebyher.in`, 28-day pull):**
- Top queries: `madebyher` (118 clicks / 147 impr, pos 1.36), `made by her` (43 / 146, pos 4.08),
  `52 buti saree` (2 / 178), `52 buti saree nalanda` (2 / 33), `patharkatti stone craft` (2 / 111),
  `best papad brands in india` (1 / 25), `online thekua order` (1 / 10), `papad brands` (1 / 23),
  `thekua gujiya` (1 / 3).
- Top pages: `/` (193 / 1,436), `/sell` (24 / 228), `/blog/bawan-buti-saree-...` (13 / 415),
  `/product/handmade-crochet-rose-drawstring-mini-potli-bag` (6 / 392), `/blog/pedakiya-...` (5 / 288),
  `/shop` (5 / 557, still weakest major page relative to volume), `/product/sudh-desi-ghee-thekua`
  (2 / 478 — impressions UP from 394 last run, clicks still flat at 2).
- `/product/sudh-desi-ghee-thekua` 7-day pull: not isolated this run at 7d granularity (28d page-level
  shown above); impressions continuing to climb (478 vs 394 on 2026-10-26, +21%) with clicks still
  pinned at 2 — the zero-click-majority gap is **widening**, not closing, while competitor activity on
  the same query space intensifies (see Top Opportunity).
- New pages in this pull not seen in the 2026-10-26 snapshot: `/blog/top-papad-brands-india-where-homemade-fits`
  (3 / 273), `/blog/wedding-return-gifts-under-300` (3 / 314), `/about` (2 / 229),
  `/blog/dussehra-gift-hampers-online-...` (2 / 59), `/blog/karwa-chauth-gifts-for-wife-...` (2 / 141),
  `/blog/pedakiya-vs-gujiya-comparison` (2 / 137), `/blog/unique-diwali-gift-ideas-handmade` (2 / 95),
  `/product/handmade-crochet-tasbih-prayer-beads` (2 / 26), `/product/handmade-floral-tealight-candle-gift-box-pack-of-4`
  (2 / 8, 25% CTR — small base but notable), `/product/handmade-resin-shubh-labh-aarti-thali-diya-gift-set`
  (2 / 25), new `/bihar-specials/<city>` pages picking up first impressions (Bangalore, Delhi-NCR,
  Mumbai, Pune) — all at 1 click apiece on tiny volume, too early to call a trend but worth watching
  next run as a possible new city-landing-page opportunity.
- Two newly live blog posts confirmed this run (both published 2026-10-27/28 per blog-topics-log.md,
  not yet in GSC at meaningful volume): `karwa-chauth-gifts-for-husband-handmade-meaningful-ideas-from-bihar`
  and `the-52-buti-saree-bihar-s-quiet-luxury-for-diwali-and-chhath-gifting`. Both read as genuine,
  humanized content (verified by direct fetch) — the saree post explicitly cross-links to the Karwa
  Chauth post, closing an internal-linking gap the 2026-10-22 research flagged.

**GA4 (property `0553055822`):** Broken again this run — `sessionDefaultChannelGroup` dimension
returned zero rows (not even a degenerate "Direct" row) at both 7-day and 28-day windows; `pagePath`
dimension also returned zero rows this run, which is a **regression from 2026-10-26**, where `pagePath`
at least returned real multi-row data even though `sessionDefaultChannelGroup` didn't. Seventh
consecutive run with channel-group data unusable, and the one dimension that worked last run (pagePath)
failed this time too — not citing any GA4 number this run; GSC is the only real search/traffic read.

## Trending in the Niche (Reddit, Google Trends, YouTube)

**Composio Google Trends (`COMPOSIO_SEARCH_TRENDS`) and Composio web/news search
(`COMPOSIO_SEARCH_WEB`/`COMPOSIO_SEARCH_NEWS`) were unavailable this run** — the `composio_search`
toolkit is session-disabled this run ("[Session Restriction] Toolkit 'composio_search' is disabled for
this session. You cannot execute tools from this toolkit.", confirmed via direct CLI execute and schema
fetch both succeeding but execute failing). Used the general-purpose web_search tool as a substitute
for market/news signal instead — flagging explicitly per the no-fabrication rule, not silently omitting.

**Reddit (r/smallbusinessindia, via Composio `REDDIT_SEARCH_ACROSS_SUBREDDITS`, real connected
account, ACTIVE status confirmed):**
- Strong continuing volume of real Diwali-hamper seller posts this week: "Heard your girl likes
  lavender colour | Pick a Diwali Hamper for her" (3 upvotes/1 comment, 2026-10-27)[8], "Diwali gifting
  on a budget? Sharing some cute festive hampers starting at just ₹350 | Mumbai" (4/1, 2026-10-27)[9],
  "Iss Diwali kuch meetha ho jaye!" — a Zova Bakes Diwali dessert hamper post explicitly targeting
  diet-conscious gifters with "3 different sizes" (1/1, 2026-10-28)[10]. Same hamper-framing pattern
  validated three runs in a row now (2026-10-22, 2026-10-26, this run) — independent sellers are
  converging on tiered/sized hamper offers for Diwali, which is exactly the product-page mechanic
  (Exp 9/10) still sitting unshipped on MadeByHer's own thekua page.
- r/crochet and r/IndianFashionAddicts searched for gifting/Diwali crossover: no Bihar-specific or
  marketplace-relevant signal this week beyond general festive-outfit chatter — not cited as evidence
  for any claim.
- r/india and r/Etsy searched for Bihar/handmade/thekua crossover: no new relevant threads this week
  (results were generic India/Etsy complaint threads, not gifting-specific) — confirms absence, not
  fabricated as a finding.

**YouTube transcript pull:** Not completed this run — time was reallocated to resolving the
composio_search toolkit restriction and the GA4 regression investigation, both of which needed direct
diagnosis before the run's higher-priority search-intent and competitor findings could be trusted.
Flagging as a gap for next run rather than skipping silently.

**Instagram competitor coverage: skipped**, per standing limitation — the Composio Instagram
connection can only read MadeByHer's own account posts/tags, not public hashtag or competitor search.

## News and Articles

- Chhath Puja 2026 confirmed across multiple independent sources (divinehindu.in[11], giva.co, jivisa.in,
  soultheory.in) as **13-16 November 2026**, with the main Sandhya Arghya evening offering on **15
  November** — this is the authoritative date MadeByHer's existing Chhath content and Exp 10's "15 Nov"
  framing should anchor to; no date conflict found across sources.
- The Thekua Company's blog post "Thekua and Chhath Puja: What the Prasad Means" (2026) confirms their
  live Diwali code TTCDIWALI (15% off, ≥₹489, valid till 2 Nov) is still active and they have already
  published Chhath-specific content ahead of the 15 Nov date[2] — they are moving into the Chhath window
  before MadeByHer has shipped its own on-page response.
- myehaat.in (My E-Haat, an HCL Foundation CSR initiative, not a commercial competitor in the pure
  sense) surfaced in gifting-guide search results with Madhubani/Bihar-craft gift boxes (Madhubani Box
  ₹2,575, Madhubani Mandala Jhola Bag) — reaches 5,500+ artisans across 40+ districts, ₹5 crore+ revenue
  generated[6][7]. Its non-profit/CSR structure and national (not Bihar-exclusive) craft scope make it a
  different shape from MadeByHer (commercial marketplace, Bihar-specific); noting as a watch, not adding
  to the direct-competitor watchlist rows this run — see Competitive Edge below for the reasoning.

## Competitive Edge

**New competitor logged (direct, same flagship SKU): Golden Nut Goods.**
1. **What are they doing that we aren't?** Live -20% discount pricing (₹399→₹319) AND two bundled combo
   packs (plain+jaggery thekua, 800g) AND broader delivery-city copy naming 8 cities by name in their
   product copy.[4][5] MadeByHer's thekua page has none of these three mechanics.
2. **Is this gap worth closing?** Yes, more urgently than last run — this is the THIRD single-SKU thekua
   brand found doing exactly this (discount + bundle + reviews-or-social-proof), and MadeByHer's own
   page impressions on this exact query space grew another 21% this run (394→478) while clicks stayed
   flat at 2. The gap is not hypothetical competitive noise; it is the same unshipped fix blocking
   conversion on MadeByHer's own, independently-growing demand.
3. **Concrete move:** Ship Exp 9 (on-page title/meta match to "thekua online"/"buy thekua online") and
   Exp 10 (scoped, time-bound Chhath discount + a simple 2-pack bundle option) together, before 15
   November. Both experiments are already written up in strategy.md and have been open 2-3 runs; this
   run adds no new experiment, it adds urgency — three repeat observations of the identical competitor
   mechanic (discount+bundle) is no longer a "maybe," it is the one thing proven to matter in this
   specific sub-market, independent of marketplace-vs-D2C positioning debates.

**My E-Haat (myehaat.in): not worth chasing as a competitive response this week.** It is a CSR
initiative (HCL Foundation), not a commercial marketplace competing for the same purchase intent or
margin structure as MadeByHer — its ₹2,575 Madhubani Box price point and national (non-Bihar-exclusive)
craft scope put it in a different buyer segment. Logging the sighting here for the record, but not
adding a watchlist row or a new experiment — no urgency manufactured where none exists.

## Delta vs 2026-10-26 Snapshot

- `/product/sudh-desi-ghee-thekua`: 2 clicks / 394 impressions → 2 clicks / 478 impressions (28d) — a
  third consecutive flat-click, rising-impression run. The gap between demand and conversion widened
  this run (impressions +21%), not narrowed.
- Diwali handmade gifting campaign LinkedIn post confirmed via direct `linkedin_fetch_post` (not the
  unreliable `get_post` status, consistent with the established workaround): still live, still **0
  likes / 0 comments / 0 shares**, now 6 days after publish[12] — a third flat LinkedIn post in a row
  (after 97e42305 and this one), now a clear pattern, not noise.
- `get_campaign_performance` for `2026-10-22-diwali-handmade-gifting`: still 0/0/0 totals across all
  3 published posts, 7 days after publish.
- GA4: regressed further — last run's partial recovery (pagePath dimension returning real data) did not
  hold; this run both tested dimensions returned zero rows. Seventh consecutive broken run.
- New competitor (Golden Nut Goods) is the first new watchlist entry since Mithila Magic on 2026-10-26.
- Two new blog posts went live since the last run (Karwa Chauth gifts for husband, 52 Buti Saree) — first
  non-research content shipped in several runs; good sign the content pipeline itself is active even
  while the product-page experiments remain stuck.

## Known gaps this run (stated explicitly, not silently omitted)
- Composio Google Trends/News/Web search tools unavailable (session-restricted toolkit) — substituted
  general web_search for market signal, flagged inline above.
- YouTube transcript pull not completed — deprioritized behind diagnosing the composio_search
  restriction and the GA4 regression.
- GA4 traffic/channel data not citable this run (zero rows on both tested dimensions).

## Sources

[2] https://thekuacompany.com/blog/thekua-chhath-puja — Thekua and Chhath Puja blog
[4] https://goldennutgoods.com/product/home-made-jaggery-thekua — Golden Nut Goods Jaggery Thekua
[5] https://cards.keenable.ai/w/01a18538-8399-7a21-9be0-9badddcd5fff — Golden Nut Goods company profile
[6] https://www.myehaat.in/pages/about — My E-Haat about (HCL Foundation)
[7] https://myehaat.in/products/madhubani-mandala-jhola-bag — My E-Haat Madhubani Mandala Jhola Bag
[8] https://www.reddit.com/r/smallbusinessindia/comments/1xgofli/sell_heard_your_girl_likes_lavender_colour_pick_a — r/smallbusinessindia Diwali hamper lavender
[9] https://www.reddit.com/r/smallbusinessindia/comments/1xgxxpp/diwali_gifting_on_a_budget_sharing_some_cute — r/smallbusinessindia budget Diwali hampers
[10] https://www.reddit.com/r/smallbusinessindia/comments/1xhrc5b/iss_diwali_kuch_meetha_ho_jaye — r/smallbusinessindia Diwali hamper dessert
[11] https://www.divinehindu.in/blogs/news/chhath-puja-2026-date-vidhi-four-day-rituals — Chhath Puja 2026 dates
[12] https://www.linkedin.com/posts/vishal-kumar11103_diwali-handmadeinindia-womenledbusiness-activity-7518878046620131330-d3mI — MadeByHer LinkedIn Diwali post (live, 0 engagement)
