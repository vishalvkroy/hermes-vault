# MadeByHer Research Findings — 2026-10-01

## High-Impact Opportunity: Fix the "/sell" funnel's organic lead and stop losing the comparison-intent pages

**Evidence:**
- GSC 28d: `/sell` (seller signup) already converts organic search at 11.6% CTR (22 clicks / 189 impressions,
  avg position 2.7) [1] — second best-performing page on the whole site after the homepage. Nobody is actively
  optimizing this page right now; it is converting on its own merit.
- `/guides/thekua-comparison` converts at 15% CTR (3/20) [1] — the single best-performing guide, because its
  title literally matches the "X vs Y" search shape. By contrast `/blog/pedakiya-vs-gujiya-comparison` sits at
  650 impressions but only 5 clicks (0.77% CTR) [1] — same comparison-intent query pattern, same topic family,
  position ~6.3, but a different title/meta structure and it is failing to convert at 20x worse than the guide
  page with near-identical intent.
- This is the second research cycle flagging the "pedakiya vs gujiya" CTR problem (first flagged 2026-09-28)
  with zero change: 653→650 impressions, 5→5 clicks. The fix window judged worth taking THIS cycle, not kept
  as background noise.

**Concrete Move:**
1. Rewrite the meta title/description of `/blog/pedakiya-vs-gujiya-comparison` to match the proven
   `/guides/thekua-comparison` pattern (literal "X vs Y: which to pick" phrasing, price in the title) — this is
   a 10-minute SEO-copy fix, not a new content push.
2. Give `/sell` a small push: it is converting organically without a dedicated campaign. A LinkedIn post or
   blog CTA pointing sellers there compounds a channel that is already working, cheaper than starting a new one.

## 1. Search Intent & Demand (GSC, 28 days, sc-domain:madebyher.in)
- Brand queries lead clicks as usual: "madebyher" (96 clicks/133 imp), "made by her" (28/115) [1].
- Zero-click high-impression gaps persist: "pedakiya sweet bihar" 146 imp / 1 click (0.68% CTR, position 9.0),
  "anarsa online" 23 imp / 0 clicks (position 9.3), "best papad brands in india" 12 imp / 0 clicks [1].
- New 7-day signal: "khatwa applique work" climbing (15 imp in 28d, 5 of those in the last 7 days alone) [1] —
  worth a faster SEO fix on `/blog/khatwa-applique-a-buying-guide-to-bihar-s-cut-cloth-craft` (currently 262 imp
  / 2 clicks, 0.76% CTR over 28d) [1] since the khatwa guide has exactly the same conversion problem as pedakiya.
- Page-level (28d): homepage 140 clicks/643 imp; `/sell` 22/189; `/shop` 6/343 (1.7% CTR — underperforming its
  impression volume badly relative to `/sell`); `/about` 2/190 (1.05%) [1].

## 2. GA4 Traffic (property 553055822, "madebyher", 28 days)
- Only 16 sessions total in the reporting window, 100% Direct channel, 14 active users, 87.5% bounce rate [3].
  This property only started receiving data ~2026-09-15 per the verified analytics map — the low volume is
  expected for a brand-new stream, not a traffic collapse. No Organic Search sessions recorded yet in GA4 despite
  GSC showing real impressions/clicks — likely a GA4/GSC linking or tagging gap worth a technical check, flagged
  here rather than guessed at.
- Landing pages: `/` (13 sessions), `/sellers/crochet`, `/sellers/handmade-love`, `/shop` (1 each) [3]. Too thin
  a sample to draw channel-mix conclusions yet; treat as a baseline data point, not a trend.

## 3. Niche Trends & Market Signals
- **Google Trends ("thekua", 12mo via Composio SEARCH_TRENDS):** low but genuinely rising — index 4-5 through
  mid-summer, climbing to 7-8 by Sep 6-19, 2026, holding at 6-7 into the current week (Sep 27-Oct 3) [6]. Real
  seasonal search lift starting now, ahead of Chhath (Nov 15) — confirms the lead-time logic in
  `docs/festival-calendar.md` is correct, not just a calendar assumption.
- **"chhath puja gifts" and "diwali gifts handmade" Google Trends queries returned empty** (SerpAPI: "Google
  Trends hasn't returned any results for this query") [6] — these specific phrasings have too low volume to
  register; do not use them as keyword targets, use the real GSC long-tail queries instead ("pedakiya sweet
  bihar", "thekua vs gujiya") which DO have real impression volume.
- **India Gift-Search Index 2026** (real search-impression data, Jul-Aug 2026, Gifting Matrix): birthday is 42%
  of all Indian gift search volume, Diwali only 1% and Raksha Bandhan 7% [5] — a reminder that festival-specific
  content is a smaller slice of total gift search than always-on occasions. Also: 84% of all Indian gift searches
  are for items ₹3,000 or under [5], which directly supports MadeByHer's existing mid-range product pricing
  (Thekua ₹339-389, crochet bags ₹689-1,540) rather than suggesting a push upmarket.
- **Real competitor success story:** Bihar-origin thekua brand "MomsMade" (Veena Devi + son Sameer, Bengaluru)
  scaled from 4 home stoves to a reported ₹75 crore valuation / 1,000+ orders per day, using pure ghee/jaggery,
  no maida or palm oil, as their differentiator [8]. This is proof-of-market at scale for exactly MadeByHer's
  category (homemade, traditional-method thekua) — not a direct competitor (different city, chain-of-custody
  model, not Bihar-artisan-direct) but strong validation the market opportunity is real.
- **Etsy platform signal (Reddit r/Etsy, real thread, 423 points / 873 comments):** "Thousands of Etsy Shops
  Lost ALL Traffic Since Nov 6" [7] — a live seller complaint thread about a platform algorithm/traffic change.
  Relevant to MadeByHer's own `/sell` seller-acquisition page: sellers unhappy with Etsy's platform risk are a
  real, searchable audience for "alternative to Etsy India" / "sell handmade without platform risk" positioning —
  worth testing as a seller-acquisition angle given `/sell` is already MadeByHer's second-best-converting page.
- Reddit search for direct Bihar/MadeByHer-specific buyer discussion returned no on-topic real threads this
  cycle (subreddit searches on r/india, r/crochet surfaced unrelated general-India and general-crochet content,
  not Bihar-craft-specific buyer discussion) — reporting the null result rather than stretching unrelated threads
  to fit.

## 4. Competitor Moves
See Competitive Edge section below and `competitors/watchlist.md` for the full iTokri entry update.

## Competitive Edge
**Gap:** iTokri just announced (2026-09-28, 2 days old) its Festive 2026 collection organized by *craft technique*
(Bandhani, Banarasi) rather than by occasion-wear category, timed to the actual 2026 festival calendar shift
(Navratri Oct 11-19, Dussehra Oct 20, Diwali pushed late to Nov 8 due to an extra lunar month) [4].

**Is it worth closing?** Partially. iTokri's technique-first taxonomy is a genuine site-architecture and content
pattern worth studying, but MadeByHer's "Deep Bihar" regional-origin positioning (per strategy.md) is a different
and already-differentiated axis — copying iTokri's technique-first navigation wholesale would dilute MadeByHer's
sharper regional story. Not worth a full site-nav rebuild.

**Concrete move:** Borrow the *timing discipline*, not the taxonomy. iTokri is already organizing festive content
around the verified late-Diwali 2026 calendar (Nov 8, not the usual late-Oct date) — MadeByHer's
`docs/festival-calendar.md` already has this right, so no calendar fix needed, but this is confirmation to start
Diwali-specific content in early-to-mid October, not wait for a "normal year" Oct 20-25 window. Second: iTokri
names its shelves by craft technique as a secondary filter — MadeByHer could add technique-based tags (Madhubani,
Sujni, Sikki, Tikuli) as a secondary filter on top of its existing Bihar-regional framing, additive not a
replacement.

## Sources

[1] https://search.google.com/search-console — GSC madebyher.in 28d queries
[3] https://analytics.google.com/analytics/web/553055822 — GA4 madebyher property 553055822 28d
[4] https://www.sangritoday.com/spotlight/business/itokri-opens-festive-2026-with-the-technique-as-the-collection-bandhani-to-banarasi-every-shelf-named-by-its-craft — iTokri Opens Festive 2026 (Sangri Today, 2026-09-28)
[5] https://giftingmatrix.in/india-gift-search-index-2026 — India Gift-Search Index 2026 (Gifting Matrix)
[6] https://trends.google.com/trends/explore?q=thekua — Google Trends: thekua (Composio SEARCH_TRENDS)
[7] https://www.reddit.com/r/Etsy/comments/1ov508n/thousands_of_etsy_shops_lost_all_traffic_since — r/Etsy: Thousands of Etsy Shops Lost ALL Traffic Since Nov 6
[8] https://www.businesstoday.in/latest/trends/story/from-4-stoves-to-rs75-crore-empire-r-madhavan-applauds-bihar-mother-son-duos-thekua-success-story-545275-2026-07-26 — MomsMade Thekua Rs75cr story (BusinessToday)
