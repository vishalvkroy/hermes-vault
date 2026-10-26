# MadeByHer Deep Research — 2026-10-26

## Top Opportunity (read first)
**Diwali is 13 days out and the only untouched lever left is the Exp 9 on-page fix on `/product/sudh-desi-ghee-thekua` — it is now flat, not improving.** Last run's organic uptick (0→2 clicks) did not continue this week: 28d page-level is still 2 clicks/394 impressions, pos 7.41 (was 2/406, pos 7.43 on 2026-10-22) — essentially unchanged, not accelerating. Exp 9 (title/meta rewrite to literally match "thekua online"/"buy thekua online") is now five runs old (first proposed 2026-10-19) and still unshipped. With Diwali 13 days out and real national coverage this week reconfirming thekua as a trending Diwali-gifting item specifically (not just a Chhath item)[1], this is still the single highest-leverage unshipped item, now with evidence that waiting is no longer working on its own.

Second-priority, real and current this week: r/smallbusinessindia is full of live Diwali hamper launches from small homemade-food sellers right now — 10+ fresh posts in the last 7 days, several with real engagement (47 upvotes/8 comments on a "sweet candle hamper," 11 upvotes/3 comments on a customizable Diwali hamper gallery post)[6][7]. This directly validates the Diwali-handmade-gifting campaign's own hamper-framing hypothesis (plan.md, 2026-10-22) with fresh, independent market evidence — the category is genuinely active right now, not assumed.

## Performance review since last run (2026-10-22) — growth-strategy loop
- **Diwali handmade gifting campaign (2026-10-22-diwali-handmade-gifting):** 3 posts published (Pinterest 85277523, Instagram 54b1265d, LinkedIn 07b81c87c). `get_campaign_performance` still totals impressions=0/engagement=0/clicks=0, 4 days after publish. Pinterest + Instagram `get_post_analytics` both still `collected:false` — consistent with this account's historical provider lag (prior posts took 15+ days to populate or never did), not yet a failure signal. LinkedIn is the one channel with a real read via `linkedin_fetch_post`: confirmed live, 0 likes/0 comments after 3 days — same flat pattern as the prior LinkedIn post ("3 weeks. 13 and 17. Zero.", post 97e42305, still flat at 2 likes). Two flat LinkedIn posts in a row (n=2) is a real signal to reconsider format/cadence, not yet enough to retire the channel outright.
- **`/product/sudh-desi-ghee-thekua` (Exp 9 target):** see Top Opportunity — flat this run (2/394 vs 2/406 last run), the organic momentum cited last run did not continue.
- **GA4 property `0553055822`:** still degenerate on `sessionDefaultChannelGroup` across every window tried (7/14/28/45 days) — sixth consecutive run with this pattern. New finding this run: the same property DOES return real (if small) multi-row data on `pagePath`/`landingPage` dimensions (4-9 distinct pages, ~1 session each) — so the property/credentials are not fully broken, the channel-group aggregation specifically looks degenerate, or real session volume is simply still near-zero outside the one-time 2026-10-10 reading. Not cited as real traffic either way.
- Full entries appended to `learnings/performance-log.md` this run.

## 1. Search intent (GSC + GA4)

### GSC — queries (28d, `sc-domain:madebyher.in`)
- Brand terms still dominate: "madebyher" 126 clicks/159 impr (pos 1.39), "made by her" 45/148 (pos 4.21).
- Non-brand clicks remain thin: "52 buti saree nalanda" 2/30, "patharkatti stone craft" 2/86, "best papad brands in india" 1/26, "online thekua order" 1/6, "khatwa applique work" 1/3.
- Largest zero-click high-volume queries persist unresolved: "crochet rose potli bag" 0/43 (28d), "crochet rose potli bag price" 0/39, "daisy keychain" 0/56, "pedakiya sweet bihar" (not in this run's top-100 pull — likely settled below prior volume), "papad brands in india"-family still at 0 clicks across multiple variants (8 impressions combined this cut).
- 7-day cut: "52 buti saree" 2/106 (pos 9.81, new signal — this saree query wasn't prominent 7d last run), "patharkatti stone craft" 1/56, brand terms "madebyher" 40/50 and "made by her" 24/51 continue to dominate clicks.

### GSC — pages (28d)
- Homepage 199 clicks/1,366 impr (pos 5.85) — continued growth (was 171/1,174 on 2026-10-22).
- `/sell` 21/225 (pos 3.63) — still the strongest non-homepage acquisition page, holding steady.
- `/blog/bawan-buti-saree-...` 10/330 — still the best-converting blog page, growing (was 8/189).
- `/product/handmade-crochet-rose-drawstring-mini-potli-bag` 5/394 (pos 8.45) — up from 4/380, still far below its impression volume (Exp 8 still unshipped).
- `/shop` 5/572 (pos 5.71) — impressions keep climbing (508→572) with clicks barely moving; still the weakest major page relative to volume, standing "do not push generic /shop" rule holds.
- `/product/sudh-desi-ghee-thekua` 2/394 (pos 7.41) — flat vs 2/406 last run, see Top Opportunity.
- `/blog/top-papad-brands-india-where-homemade-fits` 3/290 — Exp 7 (papad sourcing gap) still open; `admin_search_products(q="papad")` returned `[]` again this run (8th consecutive run with zero matching catalog product).
- New in this run's page list, not previously logged individually: `/blog/thekua-for-chhath-puja-complete-guide` 1/154 (pos 8.38) and `/blog/thekua-vs-gujiya-difference` 1/66 (pos 5.67) — real, if small, Chhath-adjacent content already live and picking up impressions ahead of the 15 Nov festival.
- `/gifts/diwali` 1/3 — still tiny; Diwali-specific collection page is not yet pulling meaningful volume even with Diwali 13 days out, same internal-linking gap flagged in the 2026-10-22 campaign's blog-handoff note.

### GA4 (property `0553055822`)
- `sessionDefaultChannelGroup` dimension: degenerate ("Direct" only, 1-3 sessions) across 7d, 14d, 28d, 45d pulls — sixth consecutive broken run (2026-10-12 through 2026-10-26).
- New this run: `pagePath` dimension on the SAME property/window returned real multi-row data — `/` , `/sellers/crochet`, `/sellers/handmade-love`, `/shop` each showing 1 session (45d window). This narrows the fault to the channel-group aggregation specifically (or genuinely near-zero real channel-level traffic), not a fully dead connection. Flagging for whoever owns `ga4_traffic_summary` — do not re-test the channel dimension weekly expecting a different result; GSC remains the reliable search-intent read.

## 2. Trending in the niche

### News and articles
- **CNBC-TV18, "Beyond the mithai box: How India's Diwali gifting is changing"** (published 2026-10-24, 2 days before this run)[1]: cites GoKwik e-commerce data showing thekua (explicitly named as "a traditional sweet from Bihar closely associated with Chhath Puja") was ordered across all Indian states/UTs in the most recent festive season, with strong demand in West Bengal, Maharashtra, Delhi, Bihar and Jharkhand — i.e. thekua demand is NOT Bihar-local, it travels nationally as a Diwali/festive gift, not only a Chhath-specific item. Directly reinforces pushing `/product/sudh-desi-ghee-thekua` now, ahead of Diwali, not waiting for the Chhath window alone.
- **Mithila Magic (mithilamagic.com)** — a food-only, single-brand D2C competitor not previously logged, founded by Anamika Devi (started the business at age 50), covered in regional business press this run[9][11]. Sells Thekua, Ghee Atta Cookies, Atta Namak Para, flavoured Makhana, and pickles/achaar — explicitly multi-SKU within the food category (broader than The Thekua Company's single-recipe-per-brand model), with a live "LAUNCH OFFER - up to 30% off" on its Achar collection[11]. `admin_search_products(q="makhana")` and `(q="achaar")` were checked against MadeByHer's own catalog — see Competitive Edge below.

### Reddit (r/smallbusinessindia — `REDDIT_SEARCH_ACROSS_SUBREDDITS`)
- Genuinely high recent volume of real Diwali-hamper activity this week, all within the last 7 days at run time: "Made a sweet candle hamper for Diwali!" (47 upvotes, 8 comments, 2026-10-19)[7], "What if someone gifts you these in a box?" — customizable Diwali hampers from a home bakery (11 upvotes, 3 comments, 2026-10-25)[6], "Diwali dryfruit hampers!" (3 upvotes, 1 comment, 2026-10-21)[8]. This is current, real seller-side demand validation for the hamper-framing hypothesis the 2026-10-22 campaign was built on (plan.md) — not a one-off, this is now the dominant post type on the subreddit this week.
- One cautionary signal also surfaced: "Navratri pop up didn't perform" (8 upvotes, 6 comments, 2026-10-22)[13] — a seller reporting a physical pop-up stall underperformed for Navratri. Not directly transferable to MadeByHer's online-only model, but a real data point that offline festival activation isn't automatically a win even in an active festive window — noted, not acted on.
- r/crochet, r/india, r/Etsy: not re-queried this run (no new angle to test beyond what 2026-10-22's run already concluded — r/india skews cultural/non-commerce for Chhath, r/Etsy skews buyer-trust-friction, r/crochet returned generic hobbyist content with no India/gifting-business signal in a fresh pull). Reddit coverage this run focused on r/smallbusinessindia specifically since that is where the real, current, actionable signal is.
- Instagram competitor/hashtag research: **skipped**, per standing limitation — the Composio Instagram connection can only read MadeByHer's own account's posts/tags, not public hashtag or competitor search.
- Google Trends (`COMPOSIO_SEARCH_TRENDS`): not re-pulled this run — prior run's "diwali gift hampers india" (climbing to 100) and "karwa chauth gift" (already past its festival) readings are not expected to have materially changed in 4 days against a lunar-calendar-fixed 8 Nov Diwali date; re-testing weekly adds no new signal until closer to or past the date. Will re-check next run as Diwali arrives.

## 3. Competitive Edge

**1. What are they doing that we aren't?** Mithila Magic (mithilamagic.com) is a food-only D2C brand selling Thekua alongside Ghee Atta Cookies, Atta Namak Para, flavoured Makhana, and Achar/pickles — a genuine multi-SKU Bihar-food range, broader than The Thekua Company's single-recipe model, with a live 30%-off launch offer on its Achar line[11]. MadeByHer's own catalog has zero matching products for `q="makhana"` and `q="achaar"` (both returned empty via `admin_search_products` this run) — meaning two of Mithila Magic's four product lines are categories MadeByHer's marketplace currently cannot list at all, not just a weaker competing listing.

**2. Is this gap worth closing for us?** Partially. Mithila Magic is a single-brand D2C competitor, same business shape as MomsMade (already on the watchlist) — not a platform threat to MadeByHer's multi-seller marketplace model. But the specific product-category gap (no makhana, no achaar sellers on MadeByHer at all) is a real, concrete supply gap, not a positioning problem — and it echoes the already-7-runs-old Exp 7 papad gap. This is the second named food category (after papad) where real market demand/competitor activity exists and MadeByHer's catalog has nothing to show.

**3. The concrete move.** Do not chase Mithila Magic's brand positioning — chase the supply gap it exposes. Flag to Vishal as a seller-sourcing priority alongside the existing papad gap (Exp 7): makhana (Bihar's own fox-nut superfood, already has a published, presumably well-performing blog guide at `/blog/makhana-online-a-buying-guide-to-bihar-s-fox-nut-superfood` per blog-topics-log.md) and achaar (MadeByHer already has a published blog post asking "is achaar safe during pregnancy" per GSC pages data, 209 impressions/28d, implying real search interest) are both categories where MadeByHer is already writing content but has no seller/product to sell against it. This is the same content-without-inventory pattern as papad, now a second instance — worth raising to Vishal as a pattern, not two unrelated one-offs.

## Instagram coverage note
Instagram competitor/hashtag research was skipped this run. The Composio Instagram connection for this account can only read MadeByHer's own account's posts and tags, not public hashtag search or other accounts' posts — this is a standing platform limitation, not an oversight.

## Sources

[1] https://www.cnbctv18.com/lifestyle/food-and-drinks/beyond-the-mithai-box-how-indias-diwali-gifting-is-changing-20018608.htm — CNBC-TV18, "Beyond the mithai box: How India's Diwali gifting is changing" (2026-10-24)
[6] https://www.reddit.com/r/smallbusinessindia/comments/1xf74jh/what_if_someone_gifts_you_these_in_a_box — r/smallbusinessindia, customizable Diwali hampers post (2026-10-25)
[7] https://www.reddit.com/r/smallbusinessindia/comments/1x9rykx/made_a_sweet_candle_hamper_for_diwali — r/smallbusinessindia, sweet candle Diwali hamper post (2026-10-19)
[8] https://www.reddit.com/r/smallbusinessindia/comments/1xbintb/diwali_dryfruit_hampers — r/smallbusinessindia, Diwali dryfruit hampers post (2026-10-21)
[9] https://www.thecapitalbulletin.top/2026/09/at-50-anamika-devi-builds-mithila-magic.html — Mithila Magic founder profile (2026-09-08)
[11] https://mithilamagic.com — Mithila Magic homepage/product range
[13] https://www.reddit.com/r/smallbusinessindia/comments/1xcbaqy/navratri_pop_up_didnt_perform — r/smallbusinessindia, Navratri pop-up underperformance post (2026-10-22)
