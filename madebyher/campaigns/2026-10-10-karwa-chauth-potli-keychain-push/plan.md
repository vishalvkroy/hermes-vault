# Campaign Plan: Karwa Chauth — Potli Bag + Daisy Keychain Push

**Campaign ID:** 2026-10-10-karwa-chauth-potli-keychain-push
**Date:** 2026-10-10
**Status:** Pinterest + Instagram + LinkedIn pending_approval (see post IDs below). Blog angle note queued, no new post written this run.

## Festival override (campaign-workflow + festival-calendar.md)

Two festivals sit inside the 21-day active window as of today (2026-10-10): Dussehra (20 Oct,
10 days out) and Karwa Chauth (29 Oct, 19 days out). Dussehra was already fully campaigned and
published across Pinterest, Instagram, and LinkedIn last week
(`2026-10-01-dussehra-festive-shelf` — all three posts confirmed `published` via `get_post`
today, provider_post_ids on file). Karwa Chauth has had zero campaign activity this season.

Date verified fresh via real web search today (not read off the calendar file blind):
drikpanchang.com confirms **29 October 2026 (Thursday)** for Karwa Chauth — matches the existing
`festival-calendar.md` entry. No discrepancy found.

Because the festival override by itself doesn't resolve which of two simultaneously-active
festivals gets this week's effort, and because Dussehra is a direct rerun risk while Karwa Chauth
also happens to be the natural vehicle for the strategy's highest-priority unshipped backlog item,
this was treated as a genuine judgment call and routed through `council_review` (tier=flagship)
rather than picked by assumption.

## council_review (tier=flagship)

**Question asked:** Given Dussehra is already fully published (last week) and Karwa Chauth (29
Oct, 19 days out) is unstarted, and given strategy.md's Exp 5 (product-SEO + Pinterest push for
crochet rose potli bag + daisy keychain, flagged 3 consecutive weekly research runs, real GSC
impressions/zero clicks) maps naturally onto Karwa Chauth's real product page — should this week's
campaign (A) revisit Dussehra with a new angle, or (B) pivot to Karwa Chauth and use it to finally
ship Exp 5?

**Verdict:** Both models that returned a response (Claude Sonnet 5, GPT-OSS-120B via Groq;
Gemini and Mistral both failed with provider errors this run, not a disagreement, a transport
failure) independently and clearly recommended **(B) — pivot to Karwa Chauth, ship Exp 5 inside
it**. No divergence to adjudicate. Core reasoning from both: Dussehra is fully spent for this
cycle (re-running it risks self-cannibalizing feed attention, not a genuine new content gap);
Karwa Chauth is inside the window, untouched, and lands on `/gifts/karwa-chauth`, which GSC/
analysis/2026-10-10.md already flags as the single best-converting page on the site this period
(`/product/product-name-glam21-love-tinted-lip-balm`, 75% CTR); and Exp 5's two products (potli
bag, daisy keychain) have real repeated search demand with zero clicks purely because they've
never had a dedicated push — a diagnosed, fixable gap, not a new hypothesis. Decision: proceed
with (B).

## Why this (evidence receipt) - growth-strategy skill

- **Strategy pillar:** Pillar 2, Giftable Handmade Products ("crochet potli bags, daisy
  keychains, handmade flowers, return gifts, custom colours" — `strategy.md`). This is the
  pillar's first dedicated campaign push since it was added 2026-10-05.
- **Research basis:** `strategy.md` Experiment Backlog, Exp 5 — "Product SEO + Pinterest push for
  crochet potli/keychain pages... still highest priority, now two runs unshipped (daisy keychain
  7d impressions rose 11->17 with 0 clicks both runs; analysis/2026-10-10.md)." Confirmed again
  in `research/2026-10-10-deep-research.md` 7-day GSC: `crochet rose potli bag` 0/13 impressions,
  `daisy flower keychain` 0/11, `daisy keychain` 0/17 (up from 11) — zero clicks, three
  consecutive runs now, this is a real repeated pattern, not noise. Separately,
  `/product/product-name-glam21-love-tinted-lip-balm` is this week's single best-converting page
  (3 clicks / 4 impressions, 75% CTR, position 1.25) — a small base, but the strongest signal on
  the site this period, and the research doc itself recommends "a small Pinterest pin set for it
  — worth scaling."
- **Differentiator:** MomsMade / generic mass gifting platforms (watchlist.md) sell "pamper"
  items as inventory SKUs with no maker story. MadeByHer's edge for this shelf: every piece is a
  named individual seller (Yasmin_Crochet for the potli bag and keychain) who makes to order, not
  a bulk-sourced accessory — a real difference the copy can state plainly rather than imply.
- **Success metric:** GSC clicks on `crochet rose potli bag` / `daisy flower keychain` queries and
  on `/product/handmade-crochet-rose-drawstring-mini-potli-bag` and
  `/product/handmade-daisy-flower-keychain` page rows (currently 0 clicks on both 7d), checked
  2026-10-17. Secondary: Pinterest/Instagram saves on this post.

## Real product basis (admin_search_products, prices confirmed live today)

- Handmade Crochet Rose Drawstring mini potli bag — Rs 689 (seller: Yasmin Crochet). Live on
  `/gifts/karwa-chauth` today (WebExtract).
- Handmade daisy flower keychain — Rs 190 (seller: Yasmin Crochet). Live on `/gifts/karwa-chauth`
  today.
- GLAM21 Love Tinted Lip Balm — Rs 179 (seller: Dream cart). Live on `/gifts/karwa-chauth` today,
  and this week's best-converting page site-wide per GSC.

All three are real, currently-catalogued, in-stock products confirmed via both
`admin_search_products` and a live WebExtract of `/gifts/karwa-chauth` today — not invented stock.
Sargi/pooja thali sets (Rs 2,000-3,000) also live on that page but not featured this run — they're
higher-ASP ritual items already well-covered by the page's own merchandising; this campaign's job
is specifically to push the two zero-click Exp 5 products plus the proven lip balm, not to
re-describe the whole page.

## Channels

1. **Pinterest (primary, per skill's channel priority)** - see `pinterest.md`. Real generated
   hero image (brand_media.py Gemini path, UGC flatlay register per visual-content-prompts),
   cropped to Pinterest-native 1000x1500 via Cloudinary transform.
2. **Instagram (live since 2026-09-24)** - 6-slide carousel (`instagram.md`) built via
   `brand_media.py carousel`: 1 generated lifestyle hook photo + 3 real product photos (DB
   prices) + 1 text slide + 1 CTA slide.
3. **LinkedIn** - `linkedin.md`, founder-voice angle on shipping an overdue, data-backed fix
   (the Exp 5 story itself: real GSC demand with zero clicks, now acted on) rather than a
   generic festival post.
4. **Blog** - no new post this run. No Karwa Chauth blog post exists yet in
   `learnings/blog-topics-log.md` (checked) — a genuine content gap, but writing a full SEO blog
   post is the daily blog cron's job, not this weekly campaign's. Queued a handoff note in
   `blog-angle-note.md` for that cron: "sargi thali + pamper gift" buying guide angle, 19 days of
   lead time.

## Image sourcing (visual-content-prompts skill)

First attempt: `generate_image` (Pollinations), UGC flatlay prompt (potli bag, daisy keychain,
lip balm, diya, marigolds, no hands/people). Checked with VisionAnalyze: visible
"pollinations.ai" watermark, malformed/melting crochet texture, keychain and lip balm not
actually rendered — rejected, not used anywhere. Fell back to `brand_media.py image` (Gemini via
Composio) with the same scene description. Result passed VisionAnalyze: no watermark, no
distortion, all three products clearly recognisable, diya/marigold styling reads as genuine
Karwa Chauth context. Used as the Instagram carousel hook slide (native 1080x1350) and cropped to
1000x1500 (Cloudinary `c_fill,g_auto` transform) for the Pinterest pin — crop checked separately,
no key element cut off.

One carousel product slide (crochet rose potli bag) has a minor framing issue flagged by
VisionAnalyze: one of the two drawstring heart tassels is cropped at the frame's bottom edge.
Headline/price text and the product itself are still fully legible and recognisable — judged
acceptable to ship rather than block the run, but flagging here for whoever revisits
`brand_media.py`'s product-slide cropping logic.

## Real outcome this run (2026-10-10)

**Pinterest** - account `madebyher001` (social_account_id `0443dcf2-8727-44b1-b057-d637e76afc88`).
Post id `31a085ea-a1bd-4342-9a12-9002e33d8404`, status `pending_approval`, approval requested.

**Instagram** - account `madebyher.1n` (social_account_id `60b853e9-ccbc-4555-80d5-12718532515b`).
Post id `04c8dd75-32fe-4cba-9e1a-28c42070723d`, status `pending_approval`, approval requested.
6-slide carousel, see `instagram.md`.

**LinkedIn** - account Vishal Kumar (social_account_id `890ba5ea-37e0-4449-a15a-f2dab3c05538`).
Post id `97e42305-4b26-4856-b424-5926127584a4`, status `pending_approval`, approval requested.
See `linkedin.md`.

**Blog** - no post published or drafted this run; `blog-angle-note.md` queued for the daily blog
cron.

Per campaign-workflow's corrected mechanism: `create_draft` always lands `pending_approval`;
`publish()` is never called on a fresh draft. Nothing is "published" until Vishal's own click in
social.madebyher.in sets it and a `provider_post_id` is confirmed via a later `get_post` check.
See `todo.md` for the exact post IDs and per-channel completion state.
