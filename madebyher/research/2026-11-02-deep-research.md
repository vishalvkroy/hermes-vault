# MadeByHer Deep Research — 2026-11-02

## TOP OPPORTUNITY: Approve and ship the Chhath thekua posts — they're stuck, Chhath is 13 days out

The highest-impact item this run is not a new find, it's an unblocking action. `/product/sudh-desi-ghee-thekua`
is MadeByHer's strongest existing demand signal: 552 impressions / 3 clicks over the last 28 days, position
7.56 — a page search already surfaces for "thekua online" (119 impressions, 28d) and "online thekua order",
climbing every run (394→406→478→552 impressions since 2026-10-26) while clicks crawl (2→2→2→3). The campaign
built to fix exactly this — `2026-10-29-chhath-thekua-festival-push` (Pinterest post `ef2f0140`, Instagram
carousel `a095cd49`) — was drafted 4 days ago and both posts are still sitting in `status="pending_approval"`.
`get_campaign_performance` confirms `posts_published: 0` of 2. This is not the usual Instagram/Pinterest
analytics-lag pattern seen on other posts in this vault — nothing has been published yet, so there is nothing
to collect. Chhath Puja 2026 runs 13–16 November, main day (Sandhya Arghya) 15 November, confirmed via Shuddh
Swad's own live countdown widget checked this run (see Sources note at end). With 13 days left and thekua needing a few days to ship before the festival (as the draft copy itself
says), this needs an approval decision this week, not another status check next run.

National demand context backs the urgency: an October 2025 GoKwik e-commerce analysis (reported via CNBC-TV18)
found thekua ordered from every Indian state/UT, with strongest demand in West Bengal, Maharashtra, Delhi,
Bihar and Jharkhand — i.e. demand for Bihar's Chhath sweet is no longer Bihar-only, it travels with the
diaspora and curious shoppers nationwide.[7] Reddit confirms the diaspora angle directly: a highly-engaged
r/bihar post (51 upvotes, 34 comments) from someone stuck in Bangalore for Chhath explicitly asks friends
bringing thekua back to "thora jyada le aana" (bring extra) — people away from Bihar are actively trying to
source thekua through personal networks because there's no obvious trusted place to just order it.[9]

## SEARCH INTENT (GSC + GA4, this run)

GSC (`sc-domain:madebyher.in`, 28-day window, verified via `gsc_list_sites`):

- Site-level brand queries dominate clicks: "madebyher" 118 clicks/154 impr (CTR 76.6%), "made by her" 50
  clicks/132 impr (CTR 38%) — branded search is healthy and growing position (avg pos 1.4–2.6).
- **Best-performing new content this period: `/blog/bawan-buti-saree-a-buying-guide-to-bihar-s-52-motif-weave`**
  — 13 clicks / 505 impressions, CTR 2.6%, position 8.25. This beats every other non-homepage, non-/sell page
  on the site by a wide margin and is a genuinely new winner not previously logged at this scale. Queries
  "52 buti saree" (2 clicks/237 impr) and "52 buti saree nalanda" (2/43) are both converting.
- `/product/sudh-desi-ghee-thekua`: 3 clicks / 552 impressions (28d), pos 7.56 — see Top Opportunity above.
- `/sell` (seller signup): 21 clicks / 261 impressions, CTR 8%, pos 3.99 — still the strongest acquisition
  page on the site after the homepage, consistent with prior runs.
- Persistent zero/near-zero-click-despite-traffic pages unchanged from prior runs: `/shop` (4 clicks/505
  impr, 0.8% CTR), `/blog/patharkatti-stone-craft...` (4/508, 0.8%), `/blog/maa-ki-rasoi-story` (1/304,
  0.3%) — all high-impression, low-CTR; title/meta work still the right fix, not more volume.
- "best papad brands in india" / "papad brands" queries persist (1 click/22 impr each, position 8.6/11.3) —
  `admin_search_products(q="papad")` still returns zero live products. Content-inventory mismatch flagged
  again (now 6+ consecutive runs unresolved) — Vishal sourcing decision still pending.

GA4 (property `553055822`, live property; property `0553055822` also queried): the `sessionDefaultChannelGroup`
dimension returned only a single degenerate "Direct: 16 sessions / 14 users" row across every days= value tried
(7, 14, 28, 60) this run; `pagePath` returned a small 4-row result (home 13 sessions, /shop 2, /sellers/crochet 1,
/sellers/handmade-love 1) at 60 days. This property only started receiving data ~2026-09-15 per the verified
analytics map, so these are genuinely small early numbers, not a broken pull — but they are too thin to draw
channel-mix conclusions from yet. GSC remains the reliable search-intent read this run, consistent with the
performance-log's running note that GA4 channel-group has been unreliable across several recent runs.

## TRENDING IN THE NICHE

**Reddit** (Composio `REDDIT_SEARCH_ACROSS_SUBREDDITS`, across r/bihar, r/smallbusiness, r/smallbusinessindia,
r/crochet, r/Etsy, r/india, r/IndianFashionAddicts):

- r/smallbusinessindia has multiple live threads this week from a seller offering "Handmade Embroidery,
  Crochet & Personalized Gifts | PAN India Delivery" (cross-posted to r/CrochetInIndia, r/CraftyCommerce,
  r/MakeMoneyIndia on 2026-11-01) — confirms handmade-gift PAN-India D2C sellers are actively using Reddit for
  demand generation right now, a channel MadeByHer itself already works via the seller-prospecting campaigns
  in this vault.
- A real, detailed r/smallbusiness thread ("Started a handmade candle business in India...struggling to get
  customers", 71 upvotes, many real replies) surfaced the same buyer-trust pain point repeatedly: viewers watch
  reels but don't know *how* to buy — top advice was "put the price in every reel caption & a one-tap WhatsApp/
  order link," and "candles sell on smell, nobody can smell a reel" — i.e. a reminder that social discovery
  without a frictionless, obvious path to purchase (price + clear CTA) stalls conversion even with real reach.
  Directly relevant to MadeByHer's own Instagram captions, which already do put price and "link in bio" in the
  caption per the existing playbook — this is validation the current approach is right, not a new gap.[10]
- No r/crochet/r/Etsy thread this week carried a Bihar/India-specific signal beyond generic crochet-gifting
  discourse (gift fatigue, handmade-tag etiquette) — nothing actionable there this run.

**YouTube** (agent-reach, real view-count verification): A Satish K Videos podcast interview with the Shuddh
Swad co-founders ("This 17 Years Old Boy Made Thekua Brand from Reels!") has 506,018 real views, 6,774 likes,
235 comments — genuine viral traction in exactly MadeByHer's category.[12] The related Instagram reel from the
same creator (@satishkvideos) has 59K likes/115 comments.[14] The underlying story, also covered by Times of
India, is concrete: two teenagers started with ₹20,000, built thekua-only brand Shuddh Swad on Instagram Reels
documenting their own struggles (not polished ads), hit ₹45,000 on launch day, and reached ~₹1 crore in sales
within about a year — the growth engine was explicitly "behind-the-scenes" documentary-style reels, not
traditional marketing.[5] This is a format signal, not just a competitor data point — MadeByHer's own carousel/
reel content has leaned polished-product rather than founder-journey-documentary; worth testing the latter for
at least one piece this cycle (see Competitive Edge below).

**Composio search_trends**: unavailable this run — `COMPOSIO_SEARCH_TRENDS` returned `[Session Restriction]
Toolkit 'composio_search' is disabled for this session`. Flagging as a genuine tool gap, not a finding — no
trend-direction number is claimed from this source this run.

**Instagram competitor research**: explicitly skipped per standing instruction — MadeByHer's own Composio
Instagram connection can only read our own account's posts/tags, not public hashtag or competitor search.

## NEWS AND ARTICLES

- CNBC-TV18: India's Diwali/festive gifting is visibly shifting from the traditional mithai box toward
  regional specialties (thekua) and global-fusion treats (kunafa chocolate) discovered via social media and
  online retail — explicitly names thekua as a national-reach regional sweet now, not a Bihar-only item.[7]
- Startuppedia profile of The Thekua Company (Neetu Yadav & Geeta Singh, two Bihar mompreneurs, incorporated
  27 May 2026 after a November 2025 Chhath pilot): now fulfils 20–30 weekly shipments via its own D2C site plus
  Amazon India; four SKUs (jaggery, jaggery+dry fruit, sugar, sugar+dry fruit); explicit "regional homemaker/
  artisan marketplace" ambition in founder quotes — directly overlaps MadeByHer's own positioning language.[6]
- Asianet Newsable: Veena Devi's MomsMade (Bengaluru, thekua-origin snack brand) now cited at ₹15 crore revenue,
  1,000+ daily orders, ~50 women employed — a third independent thekua-first brand (after Shuddh Swad and The
  Thekua Company) reaching meaningful scale from the same festival-snack starting point, reinforcing that
  thekua-as-D2C-category is a proven, not speculative, opportunity.[8]

## COMPETITIVE EDGE

**Shuddh Swad** (watchlist-tracked) — what they're doing that we aren't: pure founder-documentary content
format (506K-view podcast interview, viral "watch us struggle and fix it" reels) as the entire customer-
acquisition engine, with zero paid marketing spend claimed.[12][5] Is this worth closing? Partially. MadeByHer
is a multi-seller marketplace, not a single-founder single-SKU brand — a direct copy of "founder vlogs his own
struggle" doesn't map cleanly onto a platform with 14+ independent sellers. But the content FORMAT (raw,
behind-the-scenes, documentary pacing, specific numbers stated on camera) is portable: MadeByHer's existing
carousels are polished-product-and-copy, not documentary. Concrete move: for the next Instagram piece tied to
an actual seller (not a generic brand post), shoot/caption it in documentary voice — a real number, a real
struggle, a real moment — rather than another polished product-benefit carousel. Low cost, directly testable
against the existing performance-log pattern of flat LinkedIn/Instagram engagement on polished-format posts.

**The Thekua Company** (watchlist-tracked, per 2026-10-26 LinkedIn post already flagged by Vishal) — their
visible, time-bound, single-product discount code is the thing already identified as worth copying scoped
narrowly (Exp 10, "Chhath discount test" in the performance-log, still unshipped). Not re-litigating that
decision here; just confirming the competitor fact: Thekua Company ships via its own site, Amazon India, and
quick-commerce, four flavour SKUs, live customer reviews.[6] MadeByHer's own Chhath thekua product page has no
visible discount/urgency element yet — this remains the single highest-leverage unshipped experiment on the
site, now compounding with the pending-approval blocker on the social push for the same product (see Top
Opportunity).

**Shuddh Swad's own shopfront** (checked live this run): aggressive anchor-pricing claims — "Rs. 299 (was
Rs. 599, 50% off)" on every SKU, with review counts in the tens of thousands (38,003 / 13,501 / 13,504) shown
per product.[4] Those review-count numbers are implausibly high for a single-SKU
regional snack brand at this scale and should be read as a storefront display artifact, not verified sales
volume — not citing it as a real competitor metric, flagging only that the anchor-discount pattern itself (50%
off framed against an inflated "regular price") is their visible conversion lever, same underlying tactic as
Thekua Company's discount code, just executed differently. Not recommending MadeByHer copy a 50%-off-against-
an-inflated-anchor pattern — that's a trust-eroding tactic inconsistent with the brand's honest-pricing
positioning (see strategy.md differentiation row) — but confirms discount/urgency framing generally is a live
lever competitors are using across the category and MadeByHer currently is not.

## Competitors genuinely new/changed this week (watchlist update)

Updated `competitors/watchlist.md` with: Shuddh Swad's confirmed ₹1cr/~3 lakh-follower scale and documentary-
reel acquisition model (new detail, prior watchlist entry only had the brand name/product); MomsMade's ₹15cr/
1,000-daily-orders milestone (new); The Thekua Company's live SKU count and distribution channels (Amazon
India, quick-commerce) confirmed via a second independent source this run.

## Sources

[4] https://shuddhswad.shop/collections/all — Shuddh Swad shop
[5] https://timesofindia.indiatimes.com/life-style/people/when-17-year-old-jayanta-and-kailash-started-their-chhath-puja-snack-venture-they-had-just-20000-he-used-to-wake-up-at-6am-to-sell-water-bottles-today-their-thekua-business-is-worth-1-crore/articleshow/134328346.cms — TOI Jayanta Kailash Shuddh Swad thekua 1 crore
[6] https://startuppedia.in/her-story/the-thekua-company-two-mothers-take-mithilas-forgotten-food-across-india-12426894 — Startuppedia Thekua Company profile
[7] https://www.cnbctv18.com/lifestyle/food-and-drinks/beyond-the-mithai-box-how-indias-diwali-gifting-is-changing-20018608.htm — CNBC TV18 Diwali gifting shift, thekua national demand
[8] https://newsable.asianetnews.com/gallery/karnataka-news/from-retired-teacher-to-entrepreneur-bihar-woman-builds-15-crore-snack-brand-bengaluru-8dn6x9k — MomsMade 15cr update
[9] https://www.reddit.com/r/bihar/comments/1xee9p8/all_this_struggle_just_to_spend_diwali_and_chhath — r/bihar diaspora Chhath thekua post
[10] https://www.reddit.com/r/smallbusiness/comments/1xiy8bq/title_started_a_handmade_candle_business_in_india — r/smallbusiness India handmade candle struggle thread
[12] https://socialcounts.org/youtube-video-live-view-count/j0RCZF3ZH4M — Shuddh Swad YouTube interview real view count 506K
[14] https://instagram.com/reel/DXwCzvVt9a-?hl=en — Satish K Videos Instagram reel, 59K likes
