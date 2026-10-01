# MadeByHer Monthly SEO + Pricing-Accuracy Audit — 2026-10-01

Scope: pricing accuracy (page claims vs. code/DB enforcement), technical SEO
(PageSpeed, GSC), structured data, CRO spot-check on pricing/checkout.
This is the first run of this recurring audit — no prior baseline exists in
this vault folder, so GSC/backlink deltas below are flagged as "baseline
established" rather than month-over-month changes.

Repo commit audited: `d9a7f2ab3b0c06b9d9e86c626ce750ee015fa55b` (2026-09-09).

---

## 1. PRICING ACCURACY

### 1.1 CRITICAL — Commission rate: page says 8%, DB default enforces 10%

- **Issue:** `/sell` and the seller dashboard (`/seller`) both display the
  commission rate as a flat **8%** on prepaid orders. The database column
  that actually gates commission (`vendors.commission_pct`) defaults to
  **10%** for every newly approved seller, and the seller-approval code path
  never overrides it to 8.
- **Impact:** High. Same bug class as the Astra Atlas "500 products free vs
  30-product code limit" incident — a real, numeric discrepancy between
  marketing copy and enforced value, seller-facing and could mislead sellers
  about their own payout economics (prospective sellers reading `/sell`
  before applying).
- **Evidence:**
  - `yarnvi/app/sell/page.tsx:12` — `"After that, a flat 8% only on prepaid orders — COD orders stay free."`
  - `yarnvi/app/seller/page.tsx:48` — `const commissionPct = vendorRows[0]?.commission_pct ?? 8;` (fallback literal is 8, but this only fires if the DB row is literally missing — normal sellers always have a row)
  - `yarnvi/app/seller/page.tsx:233,235` — renders `{commissionPct}%` from that DB value, so a normal seller sees whatever `commission_pct` actually is in her `vendors` row
  - `yarnvi/db/schema.sql:247` — `ALTER TABLE vendors ADD COLUMN IF NOT EXISTS commission_pct integer NOT NULL DEFAULT 10;`
  - `yarnvi/app/admin/actions.ts:379-386` (seller-approval `INSERT INTO vendors`) — column list has no `commission_pct`, so every approved seller silently gets the DB default of **10**, not the 8% advertised on `/sell`.
  - Admin has a manual override UI (`app/admin/vendors/page.tsx:93-97`, `setVendorCommission` in `actions.ts:463-469`) to hand-set `commission_pct` per seller, but nothing in the approval flow applies it automatically — a seller is only at 8% if an admin manually edits her row after approval.
- **Fix:** Either (a) change the schema default from 10 to 8 (`ALTER TABLE vendors ALTER COLUMN commission_pct SET DEFAULT 8;`, plus backfill any already-approved seller still sitting at the untouched default of 10), or (b) explicitly pass `commission_pct = 8` in the `INSERT INTO vendors` at `app/admin/actions.ts:380`. Option (a) is the smaller, more robust fix — one-line schema change vs. touching the insert.
- **Priority:** High — fix before next seller cohort is approved; every seller onboarded since launch may be sitting at 10% while reading "8%" on her own dashboard.

### 1.2 Payout ledger currently always shows ₹0 commission (separate from 1.1, do not conflate)

- **Observation, not necessarily a bug:** `lib/order-lifecycle.ts:769-771` hardcodes `commission = 0` in every `seller_payouts` row (`VALUES ($1,$2,$3,0,$3,'eligible')`) — `commission_pct` is not read anywhere in the actual payout computation path. The code comment explains this is intentional: MadeByHer's real cut is a separate hidden `FULFILMENT_RESERVE` (₹40/unit) baked into customer price, not a deduction from seller payout (see `lib/products.ts:152-167`). So `commission_pct` as stored in the DB currently has **no effect on money actually paid** — it is purely the number shown to sellers on `/seller` and `/sell`, with no live enforcement mechanism behind it at all.
- **Flagging because:** this means the 8%-vs-10% mismatch in 1.1 isn't just "wrong number" — the commission system is entirely cosmetic/informational right now, so there is no downstream deduction a seller could even check in her bank account to catch the discrepancy herself. Worth a product decision: either wire `commission_pct` into the real payout math, or stop showing a specific percentage on `/sell` until it's load-bearing.
- **Priority:** Medium — not misleading about money actually withheld (nothing is withheld via this field), but it is misleading about what number will apply if/when commission deduction is ever turned on, and item 1.1 makes even the cosmetic number wrong.

### 1.3 Checkout page still names "PhonePe" though the live gateway is Cashfree

- **Issue:** `/checkout` copy: *"Secure checkout via PhonePe. Always free delivery, no COD fee."* (`app/checkout/CheckoutClient.tsx:485`). The payment gateway was switched from PhonePe to Cashfree on 2026-08-07 (`a225357`), confirmed live config: `deploy/web.env.example` sets `PAYMENT_GATEWAY=cashfree`. This string is the one UI-visible leftover; `lib/payments.ts` and other PhonePe references are internal code/comments, not shopper-facing.
- **Impact:** Low-medium — not a pricing number, but a false claim about which processor handles the customer's money, at the exact moment of payment. Trust-relevant at checkout specifically (the cro skill flags "objection handling"/trust signals as high-impact at this exact page).
- **Fix:** One-line copy change to a gateway-neutral phrase ("Secure checkout via UPI / cards / wallets") or wire it off `activeGateway()` so it never drifts again.
- **Priority:** Medium (quick, isolated fix; real but not financial-accuracy-critical).

### 1.4 Fee/delivery numbers that WERE checked and are accurate
No mismatch found — reporting as explicitly checked, not assumed:
- Platform fee ₹9 (`PLATFORM_FEE`, `lib/products.ts:158`) — matches `CheckoutClient.tsx:135` and the fee line rendered at checkout.
- COD fee ₹19 (`COD_FEE`, `lib/products.ts:163`) — matches `CheckoutClient.tsx:136` and the copy strings at lines 511/513/617.
- Free delivery threshold ₹799 / flat ₹35 below it (`FREE_DELIVERY_THRESHOLD`, `FLAT_DELIVERY`, `lib/products.ts:157,159`) — matches `/offers` page copy and `CheckoutClient.tsx` banner/line items.
- Original badge price ₹1,999 one-time (`ORIGINAL_BADGE_PRICE`, `lib/products.ts:167`) — matches `/seller/badge` page display exactly, and code comment confirms "no commission discount, no placement boost" (badge page copy says the same).
- "No listing fees" claim on `/sell` and `/offers` — confirmed no listing-fee charge anywhere in `place-order.ts` or schema; accurate.
- "COD orders stay free" (no commission on COD) — confirmed: `lib/order-lifecycle.ts` only ever creates payout rows with `commission = 0` regardless of payment method (see 1.2), so this claim holds trivially (commission isn't charged on anything currently, COD included).

---

## 2. TECHNICAL SEO

### 2.1 PageSpeed (mobile, PageSpeed Insights API)

| Page | Perf | A11y | Best Practices | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|
| Home (`/`) | 71 | 100 | 96 | 100 | 4.1 s | **0.204** | 20 ms |
| `/sell` | 90 | 100 | 96 | 100 | 3.4 s | 0 | 10 ms |

- **Finding:** Homepage LCP (4.1s) exceeds the 2.5s good threshold, and CLS
  (0.204) exceeds the 0.1 good threshold — both core web vitals fail on the
  homepage specifically; `/sell` passes both. Perf score 71 vs 90.
- **Likely cause (not yet root-caused in this pass):** homepage carries
  hero imagery/carousel that `/sell` doesn't — worth a dedicated pass with
  Chrome DevTools/WebPageTest waterfall to pin the exact shifting element
  for CLS and the LCP resource, rather than guessing further here.
- **Priority:** Medium-high — homepage is the single highest-traffic,
  highest-impression page site-wide (643 impressions/140 clicks in last 28
  days per GSC, by far the top page) so a CWV fail here has the broadest
  reach of any page on the site.

### 2.2 Search Console — 28-day snapshot (first baseline, no prior-month comparison available)

Top pages by clicks (28d, `sc-domain:madebyher.in`):
- `/` — 140 clicks / 643 impr / 4.6 avg position
- `/sell` — 22 clicks / 189 impr / 2.7 avg position
- `/shop` — 6 clicks / 343 impr / 5.1 avg position
- `/blog/pedakiya-vs-gujiya-comparison` — 5 clicks / **650 impressions** / pos 6.3
- `/blog/wedding-return-gifts-under-300` — 5 clicks / 134 impr / pos 10.9

Notable zero/near-zero-click, high-impression pages (CTR gap, not a ranking
drop since no prior month exists yet — flagging as current-state
opportunity):
- `/blog/top-papad-brands-india-where-homemade-fits` — 202 impr, 1 click, pos 8.5
- `/blog/pedakiya-vs-gujiya-comparison` — 650 impr, 5 clicks, pos 6.3 — biggest absolute impression pool on the whole site after `/`, sitting outside page-1-equivalent position; title/meta-description rework here has the single largest potential-click upside site-wide.
- `/blog/is-achaar-safe-during-pregnancy` — 225 impr, 2 clicks, pos 6.5
- `/blog/khatwa-applique-a-buying-guide...` — 262 impr, 2 clicks, pos 8.2
- `https://madebyher.in/` (non-www, no HTTPS-www canonical hit) — 265 impr, **0 clicks**, pos 4.1 — same content as `https://www.madebyher.in/` but tracked as a distinct GSC page entry; worth confirming the non-www→www redirect/canonical is airtight (0 clicks across 265 impressions on an otherwise well-ranking page is consistent with a redirect working correctly and GSC still attributing impressions pre-redirect, but worth one explicit check next cycle now that this baseline exists).

**No ranking-drop investigation triggered this cycle** — this is the first
audit, there is no prior-month GSC pull in this vault to diff against. Next
month's run should diff against these numbers and investigate any page
losing impressions/clicks materially.

### 2.3 Backlinks (Bing Webmaster Tools)

- `bing_get_backlinks` for `https://madebyher.in/` returned **zero backlinks**
  (`{"Links": [], "TotalPages": 0}`). This is either a genuine zero-backlink
  state (plausible for a young regional marketplace) or a Bing-side
  indexing/crawl gap — cannot distinguish from this tool alone. Flagging as
  baseline; no backlink profile existed to compare against, so no "change"
  to report, but zero backlinks site-wide is itself worth noting as a gap
  given Pinterest is the brand's named high-priority distribution channel
  (co-marketing/content with Pinterest-sourced traffic typically does
  generate some referring domains over time — worth checking back next
  cycle to see if this moves off zero).

---

## 3. STRUCTURED DATA (schema)

Browser tool was unavailable this run (no Chromium running in the sandbox —
`chrome-not-running` error), so checked via raw SSR HTML fetch instead
(Next.js server-renders JSON-LD into initial HTML here, confirmed by finding
it in curl output — this is a reasonably reliable proxy for this specific
site, though the Rich Results Test is the authoritative tool and should be
used to double check next cycle once a browser is available).

- **Home (`/`) and `/sell`:** `Organization` + `WebSite` JSON-LD present,
  both well-formed with required fields (name, url; Organization also has
  logo/image/sameAs). No issues.
- **Product page** (`/product/sudh-desi-ghee-thekua`, sampled): `Product` +
  `BreadcrumbList` JSON-LD present. `Product` schema is notably thorough —
  `AggregateOffer` with price range/currency/availability, `shippingDetails`
  (rate + handling/transit time), `hasMerchantReturnPolicy`, and
  `aggregateRating`/`review`. All schema.org-required `Product` fields
  (name, image, offers) present. No errors found in this sample.
- **Gap:** `/sell` and home carry no `FAQPage`/`BreadcrumbList` schema, and
  a prior commit (`0c1b929`, 2026-07-11: "Remove deprecated HowTo and
  FAQPage schema (SEO audit fixes)") shows FAQPage schema was deliberately
  *removed* site-wide previously — so its absence on `/offers` (which has an
  actual visible FAQ block: "Is there a MadeByHer coupon code right now?" /
  "How do I use a MadeByHer coupon code?") is likely intentional policy, not
  an oversight. Not flagging as a bug, noting for context in case that
  policy is revisited.
- Only one product page was spot-checked (curl-based, not an exhaustive
  crawl) — recommend a full Screaming Frog or Rich Results Test batch pass
  across all product pages next cycle for full coverage; this result should
  not be read as "all product pages validated."

---

## 4. CRO SPOT-CHECK — pricing/checkout pages only

Scope: genuinely broken/confusing moments, not a redesign critique, per the
cro skill's guidance for this audit.

- **Checkout payment-method label names the wrong processor** — see 1.3
  above (PhonePe vs. Cashfree). This is a trust-signal issue at exactly the
  payment-decision moment, which the cro framework flags as high-impact
  (trust signals + objection handling placement "near CTAs"). Filed once
  under pricing accuracy (1.3) rather than duplicated here.
- **No other broken/confusing moment found** in the checkout fee breakdown
  itself — delivery fee, platform fee, COD fee, and the "pay online to
  save ₹X" prompt (`CheckoutClient.tsx:617`, `prepaidSavings` correctly
  summing `codDeliveryFee + COD_FEE`) are all internally consistent and
  match the constants in `lib/products.ts`. The savings nudge toward
  prepaid is a legitimate pricing-psychology pattern (anchoring the COD
  cost against the free prepaid option), not a dark pattern — it states the
  real fee difference accurately.
- **`/sell` commission claim (1.1) is itself a CRO-relevant trust issue**,
  not just a pricing-accuracy one — a prospective seller who later
  discovers her actual rate is 10%, not the 8% she applied under, is a
  direct trust/retention risk for the seller-acquisition funnel. Filed under
  1.1, flagged here for visibility.

---

## Prioritized action plan

1. **Critical/High:** Fix seller commission default mismatch (1.1) — change
   `commission_pct` DB default from 10 to 8, or set it explicitly at
   seller-approval insert time. Audit existing approved sellers for any
   still sitting at the untouched default of 10.
2. **Medium:** Decide whether `commission_pct` should actually drive payout
   deduction (currently always ₹0, cosmetic-only) (1.2) — product/business
   decision, not a pure code fix.
3. **Medium:** Swap "PhonePe" wording on `/checkout` for the live gateway or
   gateway-neutral copy (1.3) — isolated one-line fix.
4. **Medium-high:** Investigate homepage LCP (4.1s) and CLS (0.204) failing
   Core Web Vitals — highest-traffic page site-wide (2.1).
5. **Quick win:** Title/meta rework on `/blog/pedakiya-vs-gujiya-comparison`
   (650 impressions, pos 6.3, only 5 clicks) and
   `/blog/top-papad-brands-india-where-homemade-fits` (202 impressions, 1
   click) — biggest CTR-gap opportunities in this snapshot (2.2).
6. **Low:** Confirm non-www→www canonical/redirect is fully airtight given
   `https://madebyher.in/` shows 265 impressions / 0 clicks as a distinct
   GSC entry (2.2).
7. **Ongoing:** Zero backlinks via Bing (2.3) — not actionable as a "fix,"
   flagged for awareness given Pinterest-distribution priority; re-check
   next cycle.

All findings above are read-only observations against code at commit
`d9a7f2ab`. No site code was edited. Any fix goes through normal branch →
PR → Vishal review, per repo rules.
