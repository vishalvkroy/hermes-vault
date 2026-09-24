# Campaign Plan: Thekua Diaspora Gifting ("Taste of Home")

**Campaign ID:** 2026-09-24-thekua-diaspora-gifting
**Date:** 2026-09-24
**Status:** pending_approval (Pinterest + LinkedIn), drafted (blog angle handoff)

## Festival calendar check

Checked `docs/festival-calendar.md`. Nearest festival is Dussehra, 20 Oct 2026 - 26 days out as
of today (2026-09-24), outside the 21-day active window. No festival override applies this week.
Proceeding with the normal research-driven pick per campaign-workflow.

## Research grounding

Read `docs/MadeByHer — Growth & Content Engine.md` (positioning: "Maker Story" layer over
product-first marketing, tagline "Real women. Real stories. Made by hand.", Meet the Maker
system) and `docs/MadeByHer — Seller Packaging & Brand Enablement.md` (QR maker-story card
system) before drafting - both inform the copy's framing below.

Read latest research file `research/2026-09-24-deep-research.md`. Its Opportunity Scoring
section listed three real candidates:

1. **"Taste of Home" Thekua diaspora gifting** - GSC: "pedakiya sweet bihar" (195 impressions),
   "sudha thekua price" (17 impressions). Thekua is the only regional sweet with sales recorded
   in every Indian state/UT, driven by Bihari migrants in West Bengal, Maharashtra, Delhi. A
   competitor built a ₹75cr thekua D2C brand on "home kitchen authenticity" + pan-India shipping.
2. **Crochet "Everlasting Florals"** - GSC "3d rose bag crochet" (9 impressions only); trend
   reports call crochet flower bouquets the #1 trending gift for 2026.
3. **"Micro-Story Gifting" Maker-First Bundle** - own Competitive Edge finding: competitors
   (Fabindia, IGP) are moving toward storytelling/provenance but none bundle a physical QR
   maker-story card. No direct search-demand evidence of its own.

## council_review (tier=flagship)

Asked the 3-way tradeoff (search evidence vs differentiation vs this-week feasibility) twice.
Infra was degraded this run: across both calls, 3 of 4 models (claude, gemini, mistral) failed
with 502/429 errors from the underlying gateway - not a disagreement, an availability problem.
Only groq (openai/gpt-oss-120b) returned a full answer both times it was tried.

**Groq's verdict:** pick #1 (Thekua diaspora box) - strongest real search evidence, an existing
competitor proof-point at scale, and it needs no new product or photography (real product +
image already in the catalog) - all real advantages for a same-week execution window. Groq
recommended folding in #3's maker-story angle as a differentiator layered onto #1 rather than
running it standalone, since #3 has no direct search evidence of its own and would need new
packaging/print lead time this week doesn't have.

**My call:** going with groq's verdict as the only real signal returned. It matches the
research file's own framing (opportunity #1 is literally titled the executive-summary "Top
Opportunity" in `2026-09-24-deep-research.md`), a real product photo already exists in the
catalog (see below - no generate_image gap-fill needed), and the maker-story framing layers in
naturally from the brand's own positioning doc without requiring the physical QR-card production
(#3) that a single week can't turn around. Flagging for Vishal: council_review had degraded
availability this run (3/4 models down) - worth a retry on a future genuinely split decision
before trusting a single-model verdict again.

## Objective

Drive Pinterest saves/traffic and blog SEO for "thekua" nostalgia/diaspora gifting search terms,
positioning Thekua not as a Chhath-season-only item but as a year-round "send a taste of home"
gift for Bihari families living outside Bihar.

## Hypothesis

GSC shows real, growing search intent for "pedakiya sweet bihar" and "sudha thekua price" outside
the Chhath festival window. A diaspora-gifting frame (not festival-only) can capture that demand
now, ahead of the Nov festival rush, and builds SEO authority on "thekua gift" terms before
competitor thekua D2C brands (per research, a ₹75cr scaled player already exists) crowd the term
further.

## Target audience

Bihari/Purvanchali diaspora in Indian metros (Delhi-NCR, Mumbai, Bengaluru, Kolkata) and abroad,
25-45, gifting for family/homesickness occasions - not waiting for a specific festival.

## Research finding this responds to

`research/2026-09-24-deep-research.md`, "High-Impact Opportunity: Pan-India 'Nostalgia' Gifting
for Thekua" (Executive Summary top pick) + its Competitive Edge section (Micro-Story Gifting,
folded in as secondary framing per council_review above).

## Real product used

`admin_search_products(q="thekua")` returned two real listings. Using:
**Sudh Desi Ghee Thekua** - ₹339, slug `sudh-desi-ghee-thekua`, real Cloudinary photo:
https://res.cloudinary.com/cznwz5ot/image/upload/f_auto,q_auto/v1784017781/madebyher/products/nlv9u6awi1ez0s6ocpib.jpg
Its own listing copy already says "shipped fresh across India" - a real basis for the diaspora
angle, not an invented claim.

## Channels

- **Pinterest** (primary, connected account) - product pin using the real photo above.
- **LinkedIn** (connected account) - founder/brand-building angle via linkedin-post-writer.
- **Blog** - SEO angle handoff note for the next blog-writer cron run (not written in full here,
  per campaign-workflow scope - this campaign drafts social, hands off the blog angle).
