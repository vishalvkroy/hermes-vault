# MadeByHer — Growth Strategy

**Owner:** growth-strategy cron loop. **Created:** 2026-09-24 (first synthesis — did not exist
before this run). **Read this file FIRST in every campaign/blog/social run.**

Sources read in full for this synthesis: `research/2026-08-23` through `research/2026-09-24`
(6 weekly runs), `competitors/watchlist.md`, `analysis/2026-09-18/21/24.md`, `docs/festival-calendar.md`,
`docs/MadeByHer — Growth & Content Engine.md`, `docs/MadeByHer — Seller Packaging & Brand Enablement.md`,
`learnings/blog-topics-log.md`, all 6 `campaigns/*/plan.md`, and the repo's own founder plans:
`SEO-PLAN.md`, `MARKETPLACE-PLAN.md`, `THEKUA-CHHATH-STRATEGY.md`, `SELLER-CONTENT-SEO-PLAN.md`,
`YARNVI-ORIGINALS-KEYWORDS.md`, `MAA-KI-RASOI-KEYWORDS.md`. Plus live pulls this run:
`gsc_search_analytics` (28d, query + page dims) and `ga4_traffic_summary` (28d), both
sc-domain:madebyher.in / property 553055822, pulled 2026-09-24.

---

## 1. North star + 90-day goal

**North star: grow non-branded organic + Pinterest-referral sessions to madebyher.in from
today's effectively-zero baseline to a real, measured number — tracked via GSC non-branded
query clicks (today: ~7 clicks/28d across all non-branded queries combined, see baseline below)
and GA4 organic+referral sessions (today: 0 of 14 sessions/28d were organic or referral — all
14 were Direct).**

**90-day target: 150+ non-branded organic/Pinterest-referral sessions in a rolling 28-day window
by 2026-12-24, with at least 3 orders attributable to that traffic (GA4 e-commerce, source/medium
filtered).** This is a >20x lift over today's ~0 measured organic sessions, deliberately modest —
council_review (groq, only model that returned both times; claude/gemini/mistral failed
502/timeout/429 — see review log) proposed a ₹6L/90-day organic+Pinterest revenue target, but that
number assumes GA4 is fully wired, which it is not (see gap below). Setting the target on sessions
first, revenue second, is the honest version for where the brand actually is.

**Today's baseline (real numbers, pulled 2026-09-24):**
- GSC (28d): 81 clicks / 105 impressions on "madebyher" (branded, pos 1.26 avg); 21 clicks / 111
  impressions on "made by her" (branded, pos 3.73). Total clicks across ALL non-branded queries in
  the top-30 report: 7 (2 pedakiya, 1 sudha thekua, 1 flower jhula, 1 glam21 lip balm, 1 ha, 1
  kitna kharch). "pedakiya sweet bihar" alone: 195 impressions, 2 clicks, position 9.18 — real
  demand, page not ranking high enough to capture it.
- GA4 (28d): 14 total sessions, ALL channel=Direct (0 Organic Search, 0 Referral, 0 Organic Social).
- **CORRECTION 2026-09-25 (verified against GA4 Admin + Data API):** the 14-session GA4 figure is NOT the real baseline. GA4 tracking on madebyher.in IS live (tag G-MS34KEZ3NK matches property 553055822's stream), but that property only started collecting ~2026-09-15. MadeByHer's real history sits in legacy property 538401917 (stream 'MadeByHer', tag G-DN9NK2DKFY): Jul-early Sep 2026 = 126 / 263 / 245 / 220 / 115 sessions per half-month (~968 sessions in 90 days: Organic Search 398, Direct 211, AI Assistant 155, Referral 97, Organic Social 77). So real baseline is ~230-260 sessions per half-month, roughly 40% organic search and ~16% AI-assistant referrals - AI-assistant traffic is a real, already-working channel worth feeding. The earlier claim that NEXT_PUBLIC_GA_ID is missing in production was wrong (it is set in web.env and on the live pages). Open question: the new property shows only 14 sessions in its first ~9 days vs ~115 per half-month before - either a real traffic drop or tracking loss after the switch; check consent-banner/tag behaviour before trusting the drop. Because GSC shows ~100 branded clicks/28d against 14 GA4 sessions, treat GA4 as under-counting until reconciled. The 90-day target above (150+ non-branded sessions) should be re-based against the legacy history at the next strategy review.

Why sessions-first, not revenue-first: with 14 total sessions/28d and unconfirmed GA4 wiring, a
revenue target this early would be guessing at a conversion rate we've never observed. Once
non-branded sessions cross ~100/28d reliably, the next strategy revision should add a revenue KPI.

---

## 2. Positioning & differentiation

One row per watchlist competitor (`competitors/watchlist.md`, 9 competitor entries). Claims are
checked against `docs/MadeByHer — Growth & Content Engine.md`, `docs/MadeByHer — Seller Packaging
& Brand Enablement.md`, and repo plans — never generic.

| Competitor | Their claim | Our real proof | Our edge | Message we lead with |
|---|---|---|---|---|
| **iTokri** | Inventory-based model (buys stock from artisans), 500+ clusters, 15,000 orders/mo, 75% revenue to artisans, launched a 100K+-SKU clothing/fabric line (watchlist, source YourStory Jul 2025 + BigNewsNetwork Mar 2026) | MadeByHer is Bihar-only (not pan-India generalist) and runs a **zero-commission first-4-months window** per `THEKUA-CHHATH-STRATEGY.md` — "every rupee of the product price goes to the women who make the food," a stronger commission claim than iTokri's 75% share (unknown, test it: iTokri's exact current commission % is not in our docs, only the 75%-to-artisan figure from Sankalp Forum re: Gaatha) | iTokri is a broad multi-state marketplace pivoting into apparel/fabric volume; MadeByHer is deliberately narrow — Bihar crafts + Bihar food, not a general "Indian handmade" catalog | "Bihar-only, by design — every product traces to one state's real artisans, not a pan-India catalog" |
| **Okhai** | 30,000+ artisans, 15+ crafts, 20+ states, physical retail (Kalaghoda Mumbai store, Oct 2024), NGO-origin trust signals (watchlist) | MadeByHer's packaging system (`Seller Packaging & Brand Enablement.md`) keeps the **seller's own brand as hero** with a QR code linking to a Meet-the-Maker story per product — Okhai's site still shows a stale 2024 copyright footer per `research/2026-09-04` (a real, sourced neglect signal, not invented) | Okhai built scale (30K artisans) but per our own research the digital experience shows neglect; MadeByHer's differentiation is depth of story per seller, not breadth of artisan count we can't match at this size | "Meet the woman, not just the marketplace — every order comes with her story, not a logo" |
| **Gaatha** | Craft documentation authority, 75% revenue to artisans, but "commercially stuck" (Sankalp Forum 2024, watchlist) | MadeByHer's `SEO-PLAN.md` already ships the commercial layer Gaatha lacks: live checkout, Razorpay, product schema, Google Merchant feed — unknown, test it whether this converts better, but the structural gap (documentation without commerce) is real and sourced | Gaatha proves storytelling-first content works for authority but not sales; MadeByHer pairs the same storytelling (Meet-the-Maker) with an actual working marketplace | "The story AND the checkout — not one or the other" |
| **Jaypore** | Curated premium marketplace, absorbed into Aditya Birla Fashion & Retail 2019, no independent growth path (watchlist) | MadeByHer is independent and Bihar-specific; Jaypore's post-acquisition curation is generic "ethnic wear," not craft-specific or region-specific | Jaypore validated that curated craft demand exists but couldn't sustain it independently — a cautionary tale, not a template. Our edge is staying narrow (Bihar) rather than broadening into generic ethnic retail | "Independent and specific — not another ethnic-wear label" |
| **MeMeraki** | High-ticket original artworks, ₹10K–₹5.25L, culture-tech positioning, highest ASP in segment (watchlist) | MadeByHer's price points sit far lower (thekua boxes ₹249–399 per `THEKUA-CHHATH-STRATEGY.md`, products in the ₹300-3000 range per blog/keyword docs) — different tier by design, not a competitor for the same buyer | MeMeraki targets art collectors; MadeByHer targets everyday festival gifters — no real overlap, not worth positioning against directly | (not a primary comparison — different buyer segment) |
| **GoCoop** | B2B2C, 80,000+ artisans, 350 cooperatives, 70 handloom clusters, ERP-based supply chain (watchlist) | MadeByHer is B2C-direct with a woman-founder consumer brand voice (Meet-the-Maker), not a B2B2C infrastructure play — unknown, test it whether GoCoop's model reaches our target buyer at all; likely serves a different customer (other businesses, not gift-shoppers) | Different business model entirely — GoCoop sells infrastructure/cooperative access, MadeByHer sells finished gifts to consumers | (not a direct consumer-facing competitor — noted for ecosystem awareness only) |
| **ExclusiveLane** | 10,000+ artisans, home decor focus, Indian Ecommerce Awards 2026 #3 (watchlist) | MadeByHer's food + crochet + jewelry + cosmetics mix is broader than ExclusiveLane's home-decor-only focus, and Bihar-specific vs their general "rural artisan" sourcing (unknown, test it — their exact sourcing geography isn't detailed in our watchlist entry) | Different category mix — home decor vs MadeByHer's food/gifting-led catalog | "Not just decor — food, craft, and jewelry your family actually asks for" |
| **Hastvikas** | AR "see how it looks in your home" visualization, "100% Authentic with Artisan name" attribution (watchlist, first noted 2026-09-21) | MadeByHer's QR-code Meet-the-Maker system (`Seller Packaging & Brand Enablement.md` §5) achieves the same artisan-attribution promise physically, at the point of unboxing, not just on-site — unknown, test it whether ours converts as well as their AR feature, no data yet either way | Hastvikas leads with tech (AR); MadeByHer can lead with a physical, tangible trust moment (QR scan reveals the real woman who made it) that costs far less to build than AR | "Scan the code, meet the woman — real authenticity, no AR gimmick needed" |
| **DTDC "Kaarigo"** | Logistics-backed artisan e-commerce platform, 16,500+ touchpoints, UP govt ODOP MoU, targeting 1,000 artisans/12mo (watchlist, first noted 2026-09-04) | Not yet Bihar-focused (UP pilot only, per watchlist) — MadeByHer's first-mover position in Bihar-specific GI-tagged crafts is still open as of this writing | A well-funded logistics entrant is a genuine future threat, not a today threat — watch for Bihar/GI expansion, no positioning claim needed yet | (monitor only — no current overlap to message against) |

**Unresolved / no real number yet:** exact organic conversion rate, iTokri's current live commission
%, whether QR maker-cards actually outperform AR for trust — all marked "unknown, test it" above,
not invented.

---

## 3. Audience segments

From real GSC queries (28d) + repo keyword research docs, not assumption:

1. **Bihar/Purvanchali diaspora gift-buyers (25-45, metro India + abroad).** Real search evidence:
   "pedakiya sweet bihar" (195 impr), "sudha thekua price" (17 impr) — both low-CTR, meaning
   demand exists but current pages/rankings aren't converting it. Confirmed by `THEKUA-CHHATH-STRATEGY.md`
   and the MomsMade Rs75cr case study (`research/2026-08-30`). Where: Google search, WhatsApp/FB
   diaspora groups (per `THEKUA-CHHATH-STRATEGY.md` channel plan), Pinterest.
2. **Festival gift-shoppers, broader (not Bihar-specific), 25-45.** Real evidence: "flower jhula for
   janmashtami", "light jhula for laddu gopal" both position-1 queries (small volume but converting
   at 100% CTR when they hit) — festival/occasion-specific product search works when the page
   exists and ranks. `docs/festival-calendar.md` confirms Q4 2026 has 5 major festivals in an
   8-week span (Dussehra Oct 20 → Chhath Nov 13-16).
3. **Pinterest-native aesthetic shoppers (Gen Z/millennial, India + global).** Real evidence:
   "3d rose bag crochet" (9 impr, 0 clicks yet — page ranks position 7, room to climb) plus six
   consecutive weekly research runs scoring Pinterest 9-9.5/10 on India MAU growth (28-35M),
   96% unbranded search share, Product Pins +320% YoY (`research/2026-08-30`). Where: Pinterest.
4. **Craft-authenticity/provenance seekers.** Evidence is thinner — `research/2026-09-18` and
   `2026-09-21` both flag GI-tag/authenticity as a competitive gap (Hastvikas AR+attribution,
   Bharat GI Initiative govt program) but we have no direct GSC query evidence yet of buyers
   searching "authentic madhubani" etc. at volume. **Unknown, test it** — this segment is a
   hypothesis from competitive-edge analysis, not confirmed search demand. Treat as B2B/PR
   audience (MSME/ONDC ecosystem, journalists) until consumer search evidence appears.

---

## 4. Content pillars (council_review-informed)

**council_review(tier="flagship")** was called once this run per instruction, asking which 3 of 4
recurring themes (festival/diaspora gifting, GI-tag/Bharat-GI authenticity, Pinterest trend-riding,
maker-story/E-E-A-T hub) should be top content pillars for a brand this early, plus what the 90-day
north star should be. **Infra was degraded both attempts**: claude failed 502 both times, mistral
failed 429 both times, gemini timed out both times — only groq (openai/gpt-oss-120b) returned a
full answer, both times.

**Groq's verdict (both runs, consistent):** top 3 = (1) Festival/diaspora gifting — "fastest revenue
lever," proven competitor model, seasonal urgency with the Nov 8-16 window; (2) Pinterest
trend-riding — "primary discovery channel... generates referral sessions that feed directly into
the north-star"; (3) GI-tag/Bharat-GI authenticity — builds E-E-A-T/trust signal layered onto the
gifting pages, not standalone. Groq explicitly dropped **maker-story/E-E-A-T hub** to 4th, reasoning
it "requires heavier content-production cadence... longer SEO ramp-up" than a 90-day sprint affords.

**Where I'd expect real experts to agree:** festival/diaspora gifting as the #1 pillar is close to
unanimous-obvious given the concrete Nov 8-16 deadline, an actual comparable (MomsMade Rs75cr), and
existing GSC demand signal (pedakiya/thekua queries) — low disagreement risk here.

**Where they'd likely diverge:** Pinterest vs maker-story for the #2/#3 slots. A content-marketing
purist could reasonably argue maker-story/E-E-A-T is the compounding, defensible asset (SEO + AI
citation value per `SEO-PLAN.md` §7) while Pinterest trend-chasing risks always reacting to someone
else's named trend rather than building owned authority. Groq's own answer implicitly hedges this
by folding GI-authenticity content INTO the Pinterest/gifting pillars rather than running it
standalone — a reasonable middle path, not a clean resolution of the tension.

**My call:** followed groq's verdict (only real signal returned) with one adjustment: keep
maker-story as an explicit 4th pillar rather than dropping it, because the brand's own founder doc
(`Growth & Content Engine.md`) treats it as core identity, not optional content, and it's cheap to
produce alongside Pillar 1 (thekua/Chhath campaign already needs a maker photo/story per
`THEKUA-CHHATH-STRATEGY.md`'s own packaging plan). Running it as a 4th pillar costs little extra
since it piggybacks on Pillar-1 content already being made.

### Pillar 1 — Festival & Diaspora Gifting
- **Evidence:** `research/2026-09-24` executive summary (top opportunity), `THEKUA-CHHATH-STRATEGY.md`
  (MomsMade Rs75cr comp), GSC "pedakiya sweet bihar" 195 impr/2 clicks, "sudha thekua price" 17
  impr/1 click, `docs/festival-calendar.md` (5 major festivals Q4 2026, 21-day active-window rule).
- **Channel/format:** Blog buying guides (already 20 published, see `learnings/blog-topics-log.md`) +
  Pinterest product/lifestyle pins + WhatsApp/FB diaspora group outreach per `THEKUA-CHHATH-STRATEGY.md`.
- **KPI:** GSC clicks on festival/product query cluster (thekua, pedakiya, jhula, gift-hamper terms)
  month over month; position improvement on "pedakiya sweet bihar" (today: pos 9.18, target: top 5).

### Pillar 2 — Pinterest Discovery (trend-tied, product-anchored)
- **Evidence:** 6/6 weekly research runs score Pinterest 9-9.5/10 (`research/2026-08-23` through
  `09-24`); India MAU 28-35M, 96% unbranded search, Product Pins +320% YoY (`research/2026-08-30`);
  GSC shows "3d rose bag crochet" already at position 7 with 9 impressions — room to climb, not
  starting from zero.
- **Channel/format:** Pinterest pins (product + lifestyle), tied to named 2026 trends only when a
  real product maps to them (crochet → Granny Chic/Throwback Kid; gifting → Pen Pals) — never a
  trend-tie invented without a real SKU behind it.
- **KPI:** Pinterest impressions/saves/outbound clicks per pin (via `get_post_analytics`); GA4
  Organic Social / Referral sessions from pinterest.com (today: 0 — any real number is progress).

### Pillar 3 — GI-Tag & Craft Authenticity (layered onto Pillars 1 & 2, not standalone)
- **Evidence:** Bharat GI Initiative govt program (Aug 5 2026, MSME+DPIIT, `research/2026-09-04`),
  13 Bihar GI tags incl. 3 new Jun 2026, Hastvikas AR+attribution competitor move
  (`competitors/watchlist.md`), `competitive-edge` gap analysis in `research/2026-09-18/21`.
  **No direct consumer search-volume evidence yet** — this pillar rides on Pillars 1/2's traffic,
  it doesn't generate its own yet. Flagged "unknown, test it": whether a standalone authenticity
  angle converts on its own.
- **Channel/format:** Authenticity/provenance framing woven into festival blog posts and Pinterest
  captions (GI-tag callouts, "real vs mass-produced" framing) + one LinkedIn founder post on the
  Bharat GI Initiative program itself (B2B/press audience, not consumer).
- **KPI:** LinkedIn impressions/comments on GI-program post; qualitative — track if any press/MSME
  inbound results (no real number yet, this is a trust/PR play more than a traffic play).

### Pillar 4 — Maker Story / Meet-the-Maker (piggybacks on Pillar 1 production)
- **Evidence:** `docs/MadeByHer — Growth & Content Engine.md` (full Meet-the-Maker system already
  spec'd, not yet executed in social), `docs/MadeByHer — Seller Packaging & Brand Enablement.md`
  QR-code system, `SEO-PLAN.md` §7 (seller stories = "exactly what AI engines quote").
- **Channel/format:** Instagram (@madebyher.1n, approval-gated) short maker-story posts/reels
  produced alongside Pillar-1 festival content (same shoot, same seller) — not a separate
  production cycle. Blog: expand existing seller-profile word floor (2,000 words) per `SEO-PLAN.md`.
- **KPI:** Instagram saves/shares (not follower vanity, per growth-strategy skill §5 sanity limits —
  account is single-digit followers, optimize for saves/shares); GSC branded+seller-name query
  growth over time.

---

## 5. Channel plan

| Channel | Role | Cadence | Formats | Status |
|---|---|---|---|---|
| **Pinterest** | Primary discovery/distribution (Pillar 2, high priority per brand rule) | 3-4 pins/week | Product pins, lifestyle/festival pins, Rich Pins | Live account, approval-gated per campaign cron |
| **Blog** (`/blog`) | SEO/organic search capture (Pillars 1, 3, 4) | ~1 post/day currently (per blog-topics-log — note: bridge auto-publishes without draft review, flagged to Vishal twice, see review log) | Buying guides, festival guides, seller stories | Live, publishing (with the known auto-publish bug) |
| **Instagram** (@madebyher.1n) | Maker-story/visual proof (Pillar 4) | 3-4x/week per growth-strategy skill sanity limit (not daily — single-digit followers) | Single image, carousel (product+story mix) | New, approval-gated (Vishal approves via admin panel) |
| **LinkedIn** (Vishal's account) | B2B/founder credibility (Pillar 3, GI/Bharat-GI program) | ~1 post/campaign cycle | Founder-voice posts | Live, approval-gated |
| **WhatsApp/FB diaspora groups** | Direct diaspora outreach (Pillar 1) | Per `THEKUA-CHHATH-STRATEGY.md` — manual, Vishal-run | Broadcast/community posts | Manual, not automated — status per founder doc, unconfirmed if active |
| **ONDC/GeM (Bharat GI Initiative)** | B2B discovery channel (Pillar 3) | N/A — onboarding evaluation, not content cadence | Seller/catalog onboarding | Not yet evaluated — action item, not live |

---

## 6. Experiment backlog

Hypothesis → evidence → metric → status. **Max 2 running at once** per growth-strategy skill.

| # | Hypothesis | Evidence | Metric | Status |
|---|---|---|---|---|
| 1 | A dedicated Diwali+Chhath combined gifting page (not two separate campaigns) will outperform generic festival pages because the 2026 calendar compresses both into a 5-day gap, forcing/rewarding single coordinated shopping | `research/2026-09-04` delta table row 1; `campaigns/2026-09-06-diwali-chhath-pinterest-predicts/plan.md` already drafted Pinterest/LinkedIn content on this | GSC clicks + GA4 sessions to the combined festival page vs prior single-festival pages | **RUNNING** (campaign live since 2026-09-06, results not yet checked — first performance-log entry pending next cron) |
| 2 | Thekua/pedakiya diaspora-gifting framing (not festival-only) captures search demand outside the Nov festival window, ahead of competitor thekua D2C brands crowding the term | `campaigns/2026-09-24-thekua-diaspora-gifting/plan.md`, GSC "pedakiya sweet bihar" 195 impr / "sudha thekua price" 17 impr, both low-CTR — real demand, poor capture | GSC position + CTR on "pedakiya sweet bihar" and "sudha thekua price" specifically (today: pos 9.18 / pos 6.4) | **RUNNING** (campaign live since 2026-09-24, real product used, Pinterest+LinkedIn drafts pending_approval) |
| 3 | GI-tag authenticity/provenance content (Madhubani, Sikki, Sujni "how to tell real from fake") differentiates from competitors who don't run this angle, and compounds as evergreen SEO vs one-off trend content | `campaigns/2026-09-13-gi-tag-authenticity-onboarding/plan.md` — Pinterest drafts pending_approval; no watchlist competitor runs an authenticity-education angle (checked) | Pinterest saves/impressions on authenticity-angle pins vs trend-angle pins (comparison point) | **PROPOSED / stalled** — plan drafted 2026-09-13 but council_review was unreachable that cycle and image-generation tools also failed (stale tool-router, per that plan's own notes); pins are text-only, not yet approved. Needs a real re-check before calling it "running." |
| 4 | Fixing the GA4 prod env var gap (`NEXT_PUBLIC_GA_ID` not live per `SEO-PLAN.md` §10) will reveal organic traffic GSC impressions suggest already exists but GA4 isn't counting | `SEO-PLAN.md` §10 (🟡 partial status, explicit gap noted) vs GSC showing real impressions (105-236 per top pages) against GA4's 14-session/all-Direct total | GA4 Organic Search session count, before/after fix | **PROPOSED** — not yet started, needs Vishal to confirm/deploy the env var; blocks accurate measurement of pillars 1-3 |

**Lost experiments (record, don't delete):** none yet — this is the first strategy.md, no completed
experiment cycle exists to grade as lost. Experiment #3 above is closer to stalled-by-infra than
lost-on-evidence; re-run once image tools and council_review are confirmed reachable.

---

## 7. We will NOT do

- **Chase a 4th consecutive Diwali/Chhath "trend tie-in" campaign identical in structure to the
  last three cycles (08-23, 08-30, 09-06).** Evidence: `campaigns/2026-09-13-gi-tag-authenticity-onboarding/plan.md`
  itself flagged this — three prior cycles already used the same SKUs (thekua, madhubani soop, sikki
  jewelry, crochet) and overlapping hooks ("vintage," "nostalgia," "Throwback Kid," "Pen Pals").
  Repetition risk on the same Pinterest boards, not compounding reach.
- **Treat maker-story/E-E-A-T as a standalone weekly content pillar with its own production cycle
  this quarter.** Evidence: council_review (groq) explicitly ranked it 4th of 4 for a 90-day sprint,
  citing heavier production cadence than the window affords. We keep it (see Pillar 4) but only
  piggybacked on Pillar-1 shoots, not as independent output.
- **Set a revenue-based 90-day north star yet.** Evidence: GA4 shows 14 sessions/28d and an
  unconfirmed production env-var gap (`SEO-PLAN.md` §10) — no reliable conversion-rate baseline
  exists to build a revenue target on. Sessions-first is honest; revenue-first would be guessing
  (this directly overrides council_review's groq suggestion of a ₹6L/90-day target — flagged in
  §1 and the review log below).
- **Position against MeMeraki or GoCoop as direct competitors.** Evidence: watchlist shows MeMeraki
  is a high-ticket art-collector platform (₹10K-5.25L ASP) and GoCoop is B2B2C infrastructure — 
  neither serves the same buyer as MadeByHer's festival-gifting consumer. No message needed.
- **Publish blog posts through the current auto-publish bridge without a receipt.** Evidence:
  `learnings/blog-topics-log.md` shows repeated flags ("cron instruction asked for draft-only,
  bridge has no draft path, flagged to Vishal") on 2026-09-19 and 2026-09-24 entries — this is a
  known platform gap, not something content strategy should route around by pretending it's fine.

---

## 8. Review log

- **2026-09-24** — strategy.md created from scratch (first synthesis). Read all 6 research runs,
  full watchlist, 3 analysis snapshots, both brand docs, blog-topics-log, all 6 campaign plans, and
  6 repo founder-plan docs. Pulled real GSC (query+page, 28d) and GA4 (28d) baselines live via
  `gsc_search_analytics`/`ga4_traffic_summary` (note: both tools required string-typed args, not
  list/int — `dimensions="query"` not `["query"]`, `property_id="553055822"` not `553055822` —
  the MCP server also returned transient "unreachable after 3 failures" on the first attempt,
  resolved after a 60s wait and retry).
  - **council_review(tier="flagship") called twice** (question refined once for clarity) on the
    90-day north star + top-3-pillar decision. Both times: claude 502, mistral 429, gemini timeout —
    only groq answered, consistently, both times. Recorded where I followed groq (top-3 pillar order:
    festival/diaspora > Pinterest > GI-authenticity, with maker-story kept as a 4th piggyback pillar
    rather than dropped) and where I diverged (rejected groq's ₹6L/90-day revenue target in favor of
    a sessions-based target, because GA4's own wiring gap — `SEO-PLAN.md` §10 — makes a revenue
    number today a guess, not a measurement). This divergence is the single most consequential
    editorial call in this document; recorded here per the task's own requirement.
  - Positioning table built against all 9 watchlist competitors (added Hastvikas and DTDC Kaarigo
    rows, both newer entries not in the original 7-competitor watchlist core).
  - Flagged (not fixed — out of scope for this synthesis): the blog auto-publish bridge bypassing
    draft review (`learnings/blog-topics-log.md`, flagged twice already by prior crons), and the
    GA4 `NEXT_PUBLIC_GA_ID` prod gap (`SEO-PLAN.md` §10) — both block clean measurement of this
    strategy's own KPIs and should be Vishal's next infra fix, not a content decision.
  - Created `learnings/performance-log.md` and `learnings/content-decisions.md` (did not exist
    before this run) with header/format lines per the growth-strategy skill.
