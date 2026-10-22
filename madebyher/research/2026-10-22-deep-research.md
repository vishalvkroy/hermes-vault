# MadeByHer Deep Research — 2026-10-22

## Top Opportunity (read first)
**"thekua online" zero-click gap is closing on its own, but Exp 9 (on-page fix) is still unshipped and Chhath Puja is 24 days out.** `/product/sudh-desi-ghee-thekua` picked up 2 real clicks in the last 7 days (240 impressions, pos 6.75) — the first clicks this page has registered after sitting at 0/119 impressions on 2026-10-19. Google Trends for "chhath puja thekua"-adjacent gifting interest and real news coverage (PM Modi gifting Bihar thekua to a Slovak leader went viral in July 2026, still being referenced in gifting-market coverage[6]) confirm thekua is a nationally recognized, currently-trending Bihar export story. The page is moving in the right direction without intervention — an on-page title/meta rewrite to literally match "thekua online" / "buy thekua online" (Exp 9, proposed 2026-10-19, still not executed) would very likely accelerate this rather than create it from nothing. This is now the single highest-leverage unshipped item in the backlog: real demand, real page, real partial traction, zero cost to fix, festival window still open.

Second-priority: the Karwa Chauth campaign (Exp 5) can be formally closed out as a confirmed miss — 12 days live, `get_campaign_performance` still 0/0/0, and `get_post_analytics` on both Pinterest/Instagram posts now returns a 500 error (a worse failure mode than the prior "collected:false", see Competitive Edge / tooling note below). The festival passed its Trends peak a week ago. No further chase recommended; redirect effort to the still-open Chhath/thekua opportunity above and the approaching Diwali window.

## Performance review since last run (2026-10-19) — growth-strategy loop
- **Karwa Chauth campaign (2026-10-10-karwa-chauth-potli-keychain-push):** Pinterest (31a085ea) + Instagram (04c8dd75) — `get_post_analytics` now **errors (500 Internal Server Error)** on both post ids, where prior runs cleanly returned `collected:false`. Campaign totals via `get_campaign_performance` remain impressions=0/engagement=0/clicks=0, 12 days after publish. **Verdict: failed.** Target query `/product/handmade-crochet-rose-drawstring-mini-potli-bag` did register 1 real click this week (first click in 12 days, 96 impressions, pos 9.34) — too small to call the campaign a success, but the page is no longer completely dead. Exp 8 (on-page title/meta rewrite) is still not executed and remains the more likely lever than more social pushes.
- **LinkedIn "3 weeks. 13 and 17. Zero." (97e42305):** not re-checked this run — flat at 2 likes/0 comments across the last two checks (2026-10-15, 2026-10-19), no reason to expect movement. Deprioritized from weekly re-verification, same logic already applied to the stuck Instagram Chhath carousel.
- **`/product/sudh-desi-ghee-thekua`:** see Top Opportunity above — real improvement (0→2 clicks over 7 days).
- Full entries appended to `learnings/performance-log.md` this run.

## 1. Search intent (GSC + GA4)

### GSC — queries (28d, `sc-domain:madebyher.in`)
- Brand terms dominate clicks: "madebyher" 114 clicks/154 impr (pos 1.37), "made by her" 29/129.
- Non-brand clicks are thin and scattered: "52 buti saree nalanda" 2/15, "best papad brands in india" 1/28, "khatwa applique work" 1/5, "patharkatti stone craft" 1/58, "online thekua order" 1/6.
- Largest zero-click query volumes (28d): "made by" 492 impr/0 clicks (near-brand typo/confusion traffic, not actionable), "crochet rose potli bag" 50/0, "crochet rose potli bag price" 37/0, "khatwa" 36/0, "papad brands in india" 38/0, "daisy keychain" 59/0, "pedakiya sweet bihar" 76/0, "maliao skin veil foundation" 40/0 (cosmetics — product exists, title/meta likely weak), "top papad brands in india" 29/0, "daisy flower keychain" 41/0.
- 7-day pull confirms the pattern is still live and largely unchanged: "crochet rose potli bag price" 17 impr/0 clicks, "crochet rose potli bag" 8/0, "daisy flower keychain" 11/0 — same unresolved Exp 8 target.

### GSC — pages (28d)
- Homepage 171 clicks/1,174 impr (pos 5.54) — continued growth (was 168/1,078 on 2026-10-19).
- `/sell` 21/211 (pos 3.54) — still the strongest non-homepage acquisition page, consistent with every prior run.
- `/blog/bawan-buti-saree-...` 8/189 — genuinely converting blog page.
- `/product/handmade-crochet-rose-drawstring-mini-potli-bag` 4/380 (pos 8.34) — up from 2/166 on 2026-10-05 but still far below its impression volume.
- `/blog/top-papad-brands-india-where-homemade-fits` 3/300 — Exp 7 (papad sourcing gap) still open, now the 7th consecutive run with zero matching catalog product (`admin_search_products(q="papad")` returned `[]` again this run).
- `/product/sudh-desi-ghee-thekua` 2/406 (pos 7.43) — the Top Opportunity page above; 7-day cut shows 2/240 (pos 6.75), i.e. both of this page's 28-day clicks happened in just the last week.
- `/shop` 4/508 (pos 5.33) — still the weakest major page relative to volume, consistent with the standing "do not push generic /shop" rule.
- `/blog/unique-diwali-gift-ideas-handmade` 1/75, `/gifts/diwali` 1/3 — both real but tiny; Diwali-specific pages are not yet pulling meaningful volume even as Diwali Trends interest peaks (see below) — a content/internal-linking gap worth a future run's attention.
- `/product/handmade-karwa-chauth-thali-set-with-channi-and-lota` 1/34, `/product/pink-pearl-designer-karwa-chauth-thali-set` 1/32 — Karwa Chauth thali products converted real clicks this period even though the crochet-potli campaign's own target page did not.

### GA4 (property `0553055822`, 28d)
- Returned only `Direct: 2 sessions, 1 user, 50% bounce` — identical degenerate result to 2026-10-12, -15, and -19. **Fourth consecutive run with this exact broken output.** Confirmed persistent tool/pipeline issue, not cited as real traffic. Real multi-channel split (Organic 382/Direct 201/AI Assistant 155) was last seen 2026-10-10, twelve days ago. This should be escalated as a standing tool defect, not re-tested weekly with the expectation of a different result.

## 2. Trending in the niche

### Google Trends (`COMPOSIO_SEARCH_TRENDS`)
- "karwa chauth gift": 13 (Sep 13-19) → 19 → 22 → 45 → 72 → **100 (Oct 18-24)**. Contrary to the 2026-10-19 read (which had this query already past its peak at 98), this week's pull shows it still rising to 100 in the most recent window — Google Trends' relative normalization shifts slightly run to run as the reference window moves, so treat the exact "has it peaked" call with caution; what's unambiguous is interest is still high in the run-up to the 29 Oct festival (7 days out as of this writing).
- "diwali gift hampers india": 0 → 0 → 0 → 21 → 65 → **100 (Oct 18-24)**. Continuing its sharp climb into the Diwali window (8 Nov, 17 days out) — the clearest accelerating-trend query tracked this run.
- "chhath puja thekua": over a 12-month window this query shows 2 (Oct 4-10) → 4 (Oct 11-17) → 3 (Oct 18-24) — a far smaller relative value than previously logged (2026-10-19 showed a within-3-month climb to 100). This is a normalization-window artifact, not a reversal: the 12-month view this run's default call returned includes last year's own Oct 2025 Chhath/Diwali peak (which itself hit 100 in the Oct 26-Nov 1, 2025 week) as the scaling reference, flattening this year's still-building numbers by comparison. Read as: real interest is building toward Chhath (15 Nov, 24 days out), consistent with real news coverage below — do not read the small absolute numbers as a decline.

### Reddit (r/india, r/smallbusinessindia, r/Etsy — `REDDIT_SEARCH_ACROSS_SUBREDDITS`)
- r/smallbusinessindia, live Diwali-hamper threads this month: "Homemade chocolaty treats anyone? Diwali special hamper is here..." (23 upvotes, 9 comments, posted 2026-10-18)[7] — direct seller-side analogue to MadeByHer's own hamper category, confirms real current demand/activity for handmade festive hampers right now, not a stale example. "Festive Diwali Hampers for Family, Friends, and Corporate Gifting" (1 upvote, 3 comments, 2026-10-10)[8] — same pattern, lower traction, still real and current.
- r/india: Chhath Puja content on this subreddit skews cultural/photojournalism (train-travel stories, ritual photos), not commerce — confirms Chhath is a strong *cultural* story angle (consistent with the brand's "Deep Bihar Culture" content pillar) but Reddit is not where Chhath *gifting* purchase intent shows up; GSC/Trends remain the better demand signal for that.
- r/Etsy: no gifting-demand signal this run — results were dominated by buyer complaint threads (shipping-location disputes, item-not-as-described cases), several explicitly involving India-based sellers. Not actionable for MadeByHer directly, but a quiet reminder that "handmade from India" on a Western marketplace carries real trust-friction in buyer discourse — reinforces the brand's existing direct-marketplace (not Etsy-dependent) positioning rather than suggesting a new angle.
- Instagram competitor/hashtag research: **skipped**, per standing limitation — the Composio Instagram connection can only read MadeByHer's own account posts/tags, not public hashtag or competitor search.
- YouTube transcript pull: not attempted this run, consistent with prior runs' note that this channel has been a dead end for multiple consecutive weeks; not re-testing until something changes.

## 3. News and articles

- **PM Modi gifted Bihar's Thekua to Slovakia's National Council Chairman** in mid-2026; the moment went viral and was covered by at least 8 major outlets (Tribune, Moneycontrol, India Today, Times of India, ETV Bharat, Indian Express, News18, Business Today, Republic World)[6]. This is now months old but still surfaces in current gifting-market searches — thekua has unusually strong, durable national name recognition as a gift-worthy Bihar export, which directly supports pushing `/product/sudh-desi-ghee-thekua` harder (see Top Opportunity).
- **The Thekua Company / Mithila House** (`thekuacompany.com`) — a new, directly relevant competitor not previously logged. Founded by two Mithila homemakers (Neetu Yadav, Geeta Singh), explicitly positioned as a *platform* ("One Recipe. One Brand. One Homemaker. Repeat.") planning to launch a separate branded product line for each traditional Mithila recipe (thekua first, explicitly naming anarsa and gujiya as next)[1][2][3]. Current live offer: ₹229-₹599 thekua packs (250g/500g tiers) with a live Diwali discount code (`TTCDIWALI`, 15% off orders above ₹489, valid till 2 Nov)[4]. This is the first head-to-head single-SKU competitor on MadeByHer's own flagship thekua product (`/product/sudh-desi-ghee-thekua`, ₹339) found to date — see Competitive Edge section below.
- General Indian handicrafts/handmade-gifting market coverage continues at pace: a UP women's weaving collective reached Lakmé Fashion Week with water-hyacinth handicrafts[Economic Times/TOI, via web search]; global handicrafts market sizing reports (IMARC, Market Growth Reports) continue to cite strong growth (various billions-USD figures, consistent with prior runs — not re-cited individually here as the figures are unchanged market-sizing background, not new signal).
- Discover Mithila (already-logged competitor): no new material change found this run beyond the previously-logged Gift Finder feature[5] — not re-flagged as new.

## Competitive Edge

**1. What are they doing that we aren't?** The Thekua Company (`thekuacompany.com`) is building a *single-SKU-first* platform: one homemaker, one recipe, one branded product, repeated across Mithila's forgotten recipes — starting with thekua, with anarsa and gujiya named as next[1]. They've shipped real tiered packaging (250g/500g, multiple price points ₹229-599) with reviews already live (5.00/5, 4-6 reviews per SKU)[4] and an active festive discount mechanic (code-based, deadline-bound). MadeByHer sells thekua too (`sudh-desi-ghee-thekua`, ₹339, single size) but has no size-tier packaging, no visible review count on the product, and no live festive discount code on this flagship product.

**2. Is this gap worth closing for us?** Partially, and selectively. The Thekua Company's *platform* ambition (one brand per recipe) is not directly comparable to MadeByHer's multi-category marketplace model — that's a different business shape, not a feature gap to copy wholesale. But the *specific, narrow* gaps — size-tier packaging and a bounded-deadline discount code — are cheap, concrete, and directly address MadeByHer's own still-open Exp 9 zero-click/low-conversion problem on the exact same product category. This is worth closing on the thekua page specifically, not as a platform-wide strategy shift.

**3. The concrete move.** Two scoped, low-cost actions on `/product/sudh-desi-ghee-thekua` specifically: (a) ship Exp 9 (on-page title/meta rewrite matching "thekua online"/"buy thekua online") immediately — it is the cheapest, most evidence-backed unshipped item in the whole backlog and the page is already showing early organic improvement; (b) consider a time-bound Chhath-season discount/bundle test on this one product (not site-wide) to match the urgency mechanic that's clearly working for a direct single-SKU competitor, timed to the 15 Nov Chhath Puja date (24 days out) rather than copying their Diwali-specific code verbatim. Do not chase their multi-brand platform model — that's a different, larger bet research hasn't validated for MadeByHer's marketplace shape.

## Instagram coverage note
Instagram competitor/hashtag research was skipped this run. The Composio Instagram connection for this account can only read MadeByHer's own account's posts and tags, not public hashtag search or other accounts' posts — this is a standing platform limitation, not an oversight.

## Sources

[1] https://thekuacompany.com/the-house-of-mithila-the-thekua-company — The Thekua Company - Mithila House platform
[2] https://thekuacompany.com/about — The Thekua Company - About
[3] https://thekuacompany.com/about-the-homemakers — The Thekua Company - Homemakers
[4] https://thekuacompany.com/shop — The Thekua Company - Shop (pack tiers/pricing)
[5] https://www.discovermithila.com/gift-finder — Discover Mithila - Gift Finder
[6] https://www.tribuneindia.com/news/india/bihars-thekua-wins-hearts-in-slovakia-as-pm-modis-gift-to-richard-rasi-goes-viral — Bihar's Thekua wins hearts in Slovakia - Tribune
[7] https://www.reddit.com/r/smallbusinessindia/comments/1x938fu/homemade_chocolaty_treats_anyone_diwali_special — r/smallbusinessindia - Diwali hamper chocolate post
[8] https://www.reddit.com/r/smallbusinessindia/comments/1x2em3v/festive_diwali_hampers_for_family_friends_and — r/smallbusinessindia - Festive Diwali Hampers post
