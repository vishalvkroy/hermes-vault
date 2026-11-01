# MadeByHer Monthly SEO + Pricing-Accuracy Audit — 2026-11-01

Scope: pricing accuracy (page claims vs. code/DB enforcement), technical SEO
(PageSpeed, GSC vs. prior-month baseline), structured data, CRO spot-check on
pricing/checkout. Second run of this recurring audit — compared against the
2026-10-01 baseline in this same vault folder.

Repo commit audited: `365df5787b82696ed8135b6adeaecc8b43ee3e78` (2026-10-30).
Note: browser tool (Chromium) was unavailable this run (`browser-harness`
daemon failed to start) — structured-data checks below used raw HTML/curl on
Next.js SSR output, same fallback method and same caveat as the 2026-10-01
run (reliable here since this site server-renders JSON-LD, but Rich Results
Test should still be the authoritative check when a browser is available).

---

## 1. PRICING ACCURACY

### 1.1 CRITICAL, STILL UNFIXED — Commission rate: page says 8%, DB default enforces 10%

Unchanged since the 2026-10-01 audit. Re-verified against current commit:

- `yarnvi/app/sell/page.tsx:13,30` and `yarnvi/lib/seller-agreement.ts:67` still
  advertise a flat **8%** commission (+2% gateway fee) on prepaid orders.
- `yarnvi/db/schema.sql:280` still: `ALTER TABLE vendors ADD COLUMN IF NOT
  EXISTS commission_pct integer NOT NULL DEFAULT 10;`
- `yarnvi/app/admin/actions.ts:258-263` (`saveVendor`, the live seller-upsert
  path) and the 403-day-old `app:403` insert path both still omit
  `commission_pct` from their `INSERT INTO vendors` column lists — every
  seller approved since the last audit is still silently defaulting to
  **10%**, not the 8% shown on `/sell` and `/seller`.
- Confirmed live on site: `/sell` pricing table currently renders "8% + 2%
  payment-gateway fee" (checked via direct fetch of `https://madebyher.in/sell`,
  2026-11-01).
- No commit touching `yarnvi/db/schema.sql` or `yarnvi/app/admin/actions.ts`
  exists since 2026-09-09 — this was never fixed, not re-broken.
- **Priority: still Critical.** One sellers cohort has now gone a full month
  with this live. Needs the same one-line schema fix recommended last cycle:
  `ALTER TABLE vendors ALTER COLUMN commission_pct SET DEFAULT 8;` plus a
  backfill query for any vendor row still sitting at the untouched 10.

### 1.2 Payout ledger still always ₹0 commission (cosmetic-only field) — unchanged

`lib/order-lifecycle.ts:1095` still hardcodes `commission = 0` in every
`seller_payouts` insert; `commission_pct` still has no live effect on money
paid. Same observation as 2026-10-01, re-confirmed, no code change in this
area. Still a pending product decision, not re-flagging as new.

### 1.3 HIGH (upgraded), STILL UNFIXED — Checkout names PhonePe, live gateway is Cashfree

Unchanged since 2026-10-01: `app/checkout/CheckoutClient.tsx:532` —
*"Secure checkout via PhonePe. Always free delivery, no COD fee."* — while
`PAYMENT_GATEWAY=cashfree` is the live config (`lib/payments.ts:31-32`,
`deploy/web.env.example:101`). No commit touching
`CheckoutClient.tsx` payment-method copy since 2026-09-09 (only a mobile
layout/overflow fix in `689f327`, unrelated to this string).
- **Upgrading priority Medium → High this cycle**: this has now sat unfixed
  through a full audit cycle with zero code movement, and it names the wrong
  payment processor to every customer at the exact moment she is entering
  payment details — a trust-at-checkout issue, not just stale copy.
- **Fix is still a one-line change** (gateway-neutral copy, or render off
  `activeGateway()`).

### 1.4 Fee/delivery numbers re-checked, still accurate

Platform fee ₹9, COD fee ₹19, free-delivery threshold ₹799/₹35 flat below it,
and "no listing fees" all still match between `lib/products.ts` constants and
the live `/sell`, `/offers`, and checkout copy. No drift found.

---

## 2. TECHNICAL SEO

### 2.1 PageSpeed (mobile) — vs. 2026-10-01 baseline

| Page | Perf (prior → now) | LCP (prior → now) | CLS (prior → now) |
|---|---|---|---|
| Home (`/`) | 71 → 70 | 4.1s → **6.1s (worse)** | 0.204 → **0.001 (fixed)** |
| `/sell` | 90 → 96 | 3.4s → 1.8s (improved) | 0 → 0 |

- **CLS is now effectively fixed on the homepage** (0.204 → 0.001, well under
  the 0.1 threshold) — real improvement since last cycle, no corresponding
  commit identified (likely an image-dimension or font-loading fix bundled in
  general homepage work, e.g. `0ef47d2`/`10f9cb3`).
- **LCP got worse, not better** (4.1s → 6.1s) — homepage Largest Contentful
  Paint now fails the 2.5s "good" threshold by a wider margin than last
  month. Still the single highest-traffic page site-wide (1,676 impressions /
  211 clicks in the last 28 days per GSC, by far the top page), so this
  regression has the broadest reach of any finding this cycle.
- **Priority: High.** Needs a dedicated LCP trace (Chrome DevTools/WebPageTest
  waterfall) next — not re-guessing the cause a second cycle running without
  one.

### 2.2 Search Console — 28-day snapshot vs. 2026-10-01 baseline (real ranking-drop signal found)

**Ranking-drop / cannibalization finding, high confidence:**

- `/blog/pedakiya-vs-gujiya-comparison` — impressions **collapsed from 650 to
  138** (−79%), clicks 5 → 2, average position worsened **6.3 → 7.3**.
- A second, newer post on the same topic — `/blog/pedakiya-bihar-s-gujiya-
  and-where-to-actually-buy-it-online` — appeared in the sitemap with
  `lastmod 2026-09-25T06:06:03Z` (i.e. published after the 2026-10-01 audit's
  GSC pull) and is now pulling 341 impressions / 5 clicks at position 7.6.
- Both pages have correct, distinct, self-referencing canonical tags (no
  canonicalization bug — confirmed via direct fetch) and are genuinely
  different content (text-similarity ratio 0.35, not a near-duplicate), so
  this is not a canonical/duplicate-content bug. It is **keyword
  cannibalization**: two separate blog posts now compete for the same
  "pedakiya vs gujiya" query space, and the **combined** average position
  (138 impr @ pos 7.3 + 341 impr @ pos 7.6) is worse than the single old
  post's prior position of 6.3 — net effect is a worse SERP position for this
  topic cluster than before the second post existed, not an added-reach win.
- **Fix:** pick one of the two as the canonical answer for "pedakiya vs
  gujiya" / "pedakiya buying guide" intent, 301 the other into it (or
  differentiate titles/intent sharply enough that Google stops treating them
  as competing for the same query — e.g. one strictly comparison-intent, one
  strictly where-to-buy-intent, with internal links disambiguating). This is
  a content/IA decision for whoever runs the blog pipeline, not a code bug —
  flagging here because it is a genuine impression/ranking loss this cycle.
- **Priority: High** — single largest impression-pool page on the blog, now
  measurably worse off than the pre-audit baseline.

**Other movement, not alarming:**
- Homepage impressions rose sharply (643 → 1,676) with position easing
  slightly (4.6 → 6.0) — net clicks still rose (140 → 211), reads as more
  total search demand, not a ranking problem.
- `/shop` impressions kept climbing (343 → 526) while clicks fell (6 → 4,
  CTR 1.7% → 0.76%) — continuation of the CTR-gap problem flagged last cycle,
  now worse, not yet fixed. Same recommendation stands: stop routing campaigns
  to `/shop`, favor product/collection pages.
- `/sell` — 189→255 impressions, 22→21 clicks, CTR 11.6%→8.2%. Slight CTR
  softening but still the strongest non-homepage acquisition page; not
  flagging as a drop worth investigating on its own this cycle.

### 2.3 Backlinks (Bing Webmaster Tools)

Still **zero backlinks** for `https://madebyher.in/` via `bing_get_backlinks`
— unchanged from the 2026-10-01 baseline. No new finding; not re-flagging as
actionable, logged for continuity only.

---

## 3. STRUCTURED DATA (schema)

- **Home, `/sell`, `/offers`:** `Organization` + `WebSite` JSON-LD present,
  well-formed, unchanged from last cycle.
- **`/shop`:** now confirmed carrying `ItemList` JSON-LD in addition to
  `Organization`/`WebSite` — matches the `8828e1a` commit ("SEO: crawlable
  shop/category HTML, ItemList, WebSite schema") shipped before the last
  audit; this is the first cycle it was spot-checked directly. No errors
  found in the sampled markup.
- **Product page** (`/product/sudh-desi-ghee-thekua`, same page re-sampled
  for continuity): `Product` + `BreadcrumbList` present and unchanged —
  `AggregateOffer` (price range ₹339–₹379, INR, InStock), `shippingDetails`
  (₹49 rate, 1–4 day handling, 2–7 day transit), `hasMerchantReturnPolicy`
  (7-day finite window, free return by mail), and `aggregateRating`/`review`
  all still present and internally consistent with visible page content.
  Source-verified in `yarnvi/app/product/[slug]/page.tsx:245-283` — the ₹49
  shipping rate is documented in-code as a deliberate representative/display
  value for rich results (actual rate is computed per-pincode at checkout),
  not a live bug.
- **No FAQPage/HowTo schema** on `/sell` or `/offers` — still consistent with
  the deliberate removal noted in commit `0c1b929` last cycle; not re-flagging.
- Still only one product page spot-checked directly plus `/shop` — full
  Screaming Frog / Rich Results Test batch pass across all product pages
  remains a recommended follow-up, not done this cycle either (browser tool
  was unavailable this run specifically).

---

## 4. CRO SPOT-CHECK — pricing/checkout pages only

- **PhonePe-vs-Cashfree mismatch (1.3) is the only CRO-relevant finding**,
  carried forward and upgraded to High this cycle for the reason given above
  (a full cycle unfixed, at the exact payment-decision moment).
- Checkout page itself could not be re-rendered this cycle: `/checkout` now
  redirects to `/account/login?next=/checkout` for an unauthenticated
  fetch — consistent with requiring a logged-in session/cart, not a new bug,
  just means this cycle's checkout-fee-breakdown re-check relied on the
  source code (`lib/products.ts` constants, confirmed unchanged, see 1.4)
  rather than a fresh render. Recommend a logged-in browser pass next cycle
  once the browser tool is available again.
- `/sell` commission mismatch (1.1) remains the standing seller-trust risk,
  now a full month old.

---

## Prioritized action plan (this cycle)

1. **Critical, unfixed 1 full cycle:** Seller commission default (1.1) — same
   fix as last audit, still not shipped. Every seller approved in the last
   month should be checked for `commission_pct = 10`.
2. **High, new this cycle:** Investigate homepage LCP regression (6.1s, up
   from 4.1s) — CLS is fixed, LCP got worse; needs a waterfall trace, not
   another guess.
3. **High, new this cycle:** Resolve pedakiya keyword cannibalization —
   two live blog posts now split rankings for the same query space, net
   position worse than the single-post baseline. Pick a canonical angle for
   one, differentiate or redirect the other.
4. **High (upgraded from Medium), unfixed 1 full cycle:** Swap "PhonePe" copy
   on `/checkout` for the live Cashfree/gateway-neutral wording — still a
   one-line fix, still not shipped.
5. **Medium:** `/shop` CTR continues to worsen (343→526 impr, 1.7%→0.76%
   CTR) — keep routing campaigns to product/collection pages instead.
6. **Medium, unchanged:** Decide whether `commission_pct` should drive real
   payout deduction (1.2) — product decision, not a code fix.
7. **Low, unchanged:** Zero backlinks via Bing (2.3) — awareness only.

All findings above are read-only observations against code at commit
`365df578`. No site code was edited. Any fix goes through normal branch →
PR → Vishal review, per repo rules.
