# Campaign Plan: Dussehra Festive Shelf (Madhubani + Puja decor)

**Campaign ID:** 2026-10-01-dussehra-festive-shelf
**Date:** 2026-10-01
**Status:** Pinterest + LinkedIn pending_approval (see post IDs below); Instagram pending_approval; Blog = angle note queued, no new post this run.

## Festival override (campaign-workflow + festival-calendar.md)

Dussehra / Vijayadashami falls **Tuesday, 20 October 2026** - 19 days from today (2026-10-01), inside
the 21-day active window. Verified fresh via real search today (not read off the calendar file
blind, per instruction to re-check any unconfirmed date before publishing time-sensitive content):
drikpanchang.com, timeanddate.com, and divinehindu.in all independently confirm 20 Oct 2026
(Tuesday) for the primary/Delhi-reckoning date that matches `festival-calendar.md`'s existing entry
and the prior 2026-09-19 campaign's verified date. (temples.bio and a Facebook snippet showed
22/21 Oct for Bengal-rule regional variants - not the primary date for MadeByHer's audience,
consistent with the existing calendar note.) Festival active -> council_review's opportunity pick
is skipped this run per the override instruction; this campaign is built around Dussehra across
Pinterest, blog(note), and Instagram, with LinkedIn carrying the competitive-differentiation angle.

## Why this (evidence receipt) - growth-strategy skill

- **Strategy pillar:** Pillar 3, Heritage Gifting ("create high-ASP bundles... Heritage Gifting"),
  secondary touch on Pillar 1, Deep Bihar Culture (`strategy.md`). This campaign bundles puja/home-decor
  pieces (Madhubani coasters, organizer, crochet puja mat) as a themed "festive shelf," not a single SKU.
- **Research basis:** `research/2026-10-01-deep-research.md` Competitive Edge section - iTokri opened
  its Festive 2026 collection (Sangri Today, 2026-09-28) organized by craft technique, explicitly timed
  to the real 2026 lunar-shifted calendar (Navratri Oct 11-19, Dussehra Oct 20, Diwali pushed to Nov 8).
  Research's own concrete move: "borrow the timing discipline, not the taxonomy" - start festive content
  in early-to-mid October, not late Oct, and lean on MadeByHer's already-differentiated regional-origin
  story rather than copying technique-first navigation.
- **Differentiator:** iTokri (competitors/watchlist.md) - pan-India inventory-model catalog organized by
  craft technique (Bandhani, Banarasi). MadeByHer's edge: everything on this shelf is Bihar-only
  (Madhubani/Mithila), real women-maker-direct, not an inventory buy from anywhere in India.
- **Success metric:** GSC clicks/impressions on `/gifts/dussehra` landing page (currently folded into
  homepage traffic, no dedicated row yet) + Pinterest/Instagram saves on this post, checked 2026-10-08.

## Real product basis (admin_search_products, prices confirmed live today)

- Handmade Crochet Table Mat, puja cover - Rs 289 (also confirmed live on /gifts page, "Handpicked for
  Dussehra" section)
- Madhubani Peacock Coasters with Holder (Set of 6) - Rs 799
- Madhubani Fish Coaster Set with Stand (Set of 6) - Rs 799
- Madhubani Art Multipurpose Organizer Set with Tray & Holders - Rs 1,690

All four are real, currently-catalogued products, confirmed on the live `/gifts/dussehra` section of
madebyher.in today (WebExtract) - not invented stock.

## Channels

1. **Pinterest (primary, per skill's channel priority)** - see `pinterest.md`. Real generated
   hero image (brand_media.py Gemini path), resized/uploaded as a 1000x1500 Pinterest-native asset.
2. **Instagram (live since 2026-09-24)** - 7-slide carousel (`instagram.md`) built via
   `~/.hermes/scripts/brand_media.py carousel`: 1 generated lifestyle hook photo + 4 real product
   photos (DB prices) + 1 text slide (why-this-shelf) + 1 CTA slide.
3. **LinkedIn** - `linkedin.md`, founder-voice differentiation angle vs iTokri's technique-first
   Festive 2026 move, drafted via linkedin-post-writer's formula/voice rules.
4. **Blog** - no new post this run. Two Dussehra posts already live
   (`dussehra-gift-hampers-online-...` 2026-09-21, `dussehra-home-decor-ideas-...` 2026-09-30 per
   `learnings/content-decisions.md` and `blog-topics-log.md`) - a third generic Dussehra post this
   week would cannibalize, not add a content gap. Wrote `blog-angle-note.md` queuing a genuinely
   different angle (seller-readiness for the Dussehra-Diwali window, tied to the `/sell` experiment
   already in `strategy.md`'s backlog) instead of forcing a duplicate festival post.

## Image sourcing (visual-content-prompts skill)

First attempt: `generate_image` (Pollinations) with a UGC-register prompt (hands styling a festive
table). Checked the result with VisionAnalyze: watermark visible, hands malformed - rejected, not
used anywhere. Per the skill's own guidance, fell back to `brand_media.py image` (Gemini via
Composio) with a prop-only flatlay prompt (no hands/people, since Pollinations' hand rendering is
the known failure mode) - result passed a second VisionAnalyze brand-grade check (no watermark, no
distortion, correct earthy Madhubani palette, 1080x1350 native). Cropped/re-hosted to Pinterest's
native 1000x1500 for the pin specifically; used as-is (1080x1350, Instagram's own native ratio) for
the carousel hook slide.

## council_review

Not triggered. Festival override applies (Dussehra within 21 days) - the campaign-workflow
instruction explicitly says skip council_review's opportunity pick when a festival is active. No
other Yellow-tier judgment call in this run was ambiguous enough to warrant it separately.

## Real outcome this run (2026-10-01)

**Pinterest** - account `madebyher001` (social_account_id `0443dcf2-8727-44b1-b057-d637e76afc88`).
`create_draft` -> post id `5e421697-aa9e-4912-a4ef-cf69b409b04c`, status `pending_approval`.
`request_publish_approval` called successfully. Nothing published yet.

**Instagram** - account `madebyher.1n` (social_account_id `60b853e9-ccbc-4555-80d5-12718532515b`).
`create_draft` with 7-slide carousel -> post id `ee8bce91-3196-45d3-994a-74deddf43e09`, status
`pending_approval`. `request_publish_approval` called successfully. Nothing published yet.

**LinkedIn** - account Vishal Kumar (social_account_id `890ba5ea-37e0-4449-a15a-f2dab3c05538`).
`create_draft` -> post id `0c7132ec-2771-4dcc-b37c-c4e8f3cf9a51`, status `pending_approval`.
`request_publish_approval` called successfully. Nothing published yet.

**Blog** - no post published or drafted this run; `blog-angle-note.md` queued for the daily blog
cron.

Per campaign-workflow's corrected mechanism: `create_draft` always lands `pending_approval`;
`publish()` was never called on any fresh draft. Nothing is "published" until Vishal's own click in
social.madebyher.in sets it and a `provider_post_id` is actually confirmed via a later `get_post`
check.
