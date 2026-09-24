# Astra Studio — Growth Strategy

Created 2026-09-24. First synthesis — per growth-strategy skill, built from all research/analysis/
competitors/docs/campaigns/repo evidence gathered through this date. Read this FIRST before any
campaign, blog, or social piece for Astra Studio.

---

## 1. North star + 90-day goal

**North star: non-branded organic clicks to astrastudio.in, GSC 28-day window.**
**Baseline (2026-09-24, GSC `sc-domain:astrastudio.in`, last 28 days): ~5 clicks/28 days from
non-branded queries** (only "gst astra" 4 clicks/119 impr and "whatsapp message template
generator" 1 click/6 impr are non-branded in the top-25 query list; every other click — 30 on
"astrastudio", 14 on "astra atlas", 10 on "atlas stock studio", 7 on "astra studio" — is branded
search from people who already know the name). Total site clicks 28d ≈ 66 (homepage 63 clicks/590
impr + /products 31/539, some overlap). Source: `gsc_search_analytics`, 2026-09-24, dimensions
query+page.

**90-day target: 50+ non-branded organic clicks/28-day window** (10x), driven by the indexing fix
recovering the 91 pages Google had dropped, plus new SEO content compounding.

**Why this metric, not something else:** GA4 (property 538401917 / www.astrastudio.in) still
shows zero rows this run despite a tag being added in code (commit 8995a77) — we are traffic-blind
on-site, so GSC clicks is the only real, non-fabricated number available to track. Council review
(2026-09-24, flagship tier, see review log) proposed an MQL/lead metric instead; rejected because
there is no lead-capture event wired to GA4/CRM yet to measure it honestly — would be "unknown,
test it," not a real baseline. Revisit north star once GA4 data flows (check next run) or once a
lead-capture event exists.

**Indexing recovery checkpoint:** commit `c34794e` (merged 2026-09-19) fixed the root cause of
"100 pages discovered, only 9 indexed" (apex-vs-www canonical mismatch, wrong robots.txt group,
stale sitemap lastmod). GSC page-level data this run (2026-09-24) shows the fix is live but
recovery is early: `/tally-alternative` already has 227 impressions/2 clicks, several `/tools/
hsn-code/*` pages have double-digit impressions (2106: 125 impr, 3006: 30 impr) that were
presumably suppressed pre-fix. No indexed-page-count API available via current GSC tool (only
search analytics, not the URL Inspection/coverage report) — track via rising impressions across
more distinct pages as the honest proxy; note this limit explicitly rather than claiming a page
count. Unknown exact indexed-page-count today — test it via Search Console UI when reviewed
manually.

---

## 2. Positioning & differentiation

One row per watchlist competitor. Claims checked against real repo code/docs, not aspiration.

| Competitor | Their claim | Our real proof | Our edge | Message we lead with |
|---|---|---|---|---|
| **Vyapar** | Established GST billing/POS leader; batch-upload GST filing, sync lag up to 30min (watchlist 2026-09-24, Council Review); "clunky" retail counter workflow, forces upgrade to "Retail Pro" tier for full barcode features (research 2026-09-18, Reddit-sourced) | Astra Atlas ships real e-invoice (IRN) and e-way bill service modules in the codebase (`backend/src/services/einvoiceService.ts`, `ewaybillService.ts` — currently integration **stubs** pending NIC API credentials, `EINVOICE_ENABLED`/`EWAYBILL_ENABLED` env flags, not yet live in production) plus a real offline sync queue (`desktop/src/components/OfflineSyncManager.tsx`, `desktop/src/lib/offlineQueue.stress.ts`) and keyboard-first command-palette navigation shipped commit `fc7d460`. Barcode scanning ships in every plan per the live pricing page copy — no separate "Retail Pro" gate found in the repo's pricing logic. | Faster retail counter (keyboard-first, no forced upgrade tier for barcodes) + offline-first architecture built for tier-2/3 connectivity, not bolted on. **Caveat: do NOT claim "real-time GST/e-invoice sync" as live today — the service exists in code as a stub, not activated in production.** Claim the architecture (offline queue, keyboard speed), not an unshipped compliance feature. | "Built for the shop floor, not the back office — barcodes in every plan, no forced upgrade, works when your internet doesn't." |
| **Khatabook** | Semi-automated GST compliance; no native POS hardware support (watchlist 2026-09-24, Council Review) | Astra Atlas is a real POS with barcode camera scanning, multi-warehouse inventory, batch/expiry tracking (live homepage copy, verified via WebSearch snapshot 2026-09-24) — a full retail counter tool, not a ledger app. | Khatabook is a bookkeeping app first; Astra Atlas is POS-hardware-native first. Different product category, not just a feature gap — lead with "built for the counter, not just the ledger." | "Khatabook tracks your money. Astra Atlas runs your counter — barcode scanning, inventory, and the ledger, in one offline-first app." |
| **General Market / regulatory (2025-26 mandate)** | Real-time GSTN invoice upload becomes mandatory for B2B sales over ₹2,000 (watchlist 2026-09-24, Council Review) | We have the code scaffolding (einvoice/e-way bill stub services with correct GSTIN validation, NIC schema awareness) ready to activate, unlike claiming a live feature we don't have. | First-mover positioning IF we ship it before competitors adapt — but only claim this once `EINVOICE_ENABLED=true` in production. Until then this is a roadmap story, not a proof point. | (Do not publish this claim yet — "we will NOT do" below.) |

---

## 3. Audience segments

1. **Tier-2/3 Indian retail shop owners** (kirana, medical, apparel, electronics) evaluating a
   Tally/Vyapar/Khatabook switch — real GSC queries: "alternative for tally prime", "best tally
   alternative", "tally vs vyapar", branded "astra atlas"/"gst astra". Found via comparison pages
   already live (`/tally-alternative`, `/blog/astra-atlas-vs-tally-vs-vyapar`).
2. **Technical founders/operators** who follow build-in-public content — the existing LinkedIn
   audience for the 3 campaigns run to date (indexing fix, crash reporting, GST cess precision).
   Evidence: all 3 prior campaigns targeted this segment per their `plan.md` files.
3. **Indian SMBs wanting a website/app built** without an in-house dev team (Services line) — zero
   organic search evidence yet (GSC shows no non-branded services queries in top ~50 rows this
   run); this segment is real (live pricing page, real WhatsApp/email contact channel) but
   currently reached through zero active channel. Same buyer type as segment 1 at a different
   stage, per brand context.

---

## 4. Content pillars (3-5)

### Pillar 1 — Founder-led engineering credibility (LinkedIn, primary channel)
- **Evidence:** 3 campaigns already run this pattern successfully as drafts (indexing bugfix
  2026-09-24, crash reporting 2026-06/09-06, GST cess precision 2026-09-05) — each grounded in a
  real commit, each following the brand's stated LinkedIn priority ("founder-led content: building
  in public, Indian SMB problems, technical insights"). Council review (2026-09-24) ranked this
  pattern's evidence strength highest of any candidate this cycle ("a real commit vs anecdotal
  Reddit complaints or zero data").
- **Channel/format:** LinkedIn native post, no external link (per existing campaign convention),
  1x/week cadence tied to a real shipped commit.
- **KPI:** LinkedIn post impressions/engagement via `get_post_analytics` — unknown baseline yet,
  test it (no prior post has completed the approval→publish→analytics loop as of this writing per
  all 3 campaign files showing "Pending" outcome).

### Pillar 2 — SEO recovery + comparison/alternative content (blog, secondary channel)
- **Evidence:** indexing bug fix (commit `c34794e`) just restored eligibility for 91 previously-
  suppressed pages; GSC 2026-09-24 snapshot already shows early recovery signal on
  `/tally-alternative` (227 impressions) and `/tools/hsn-code/2106` (125 impressions) — pages that
  were structurally blocked from indexing until 5 days before this snapshot. Research
  (2026-09-18/21) confirms the comparison-page format already matches real search intent
  ("alternative for tally prime", "best tally alternative", "tally vs vyapar").
- **Channel/format:** blog posts + free tools (13 already live, `astrastudio/docs/free-tools.md`)
  continuing the comparison/alternative and use-case page pattern already proven to attract
  impressions.
- **KPI:** non-branded organic clicks (north star metric above), tracked via `gsc_search_analytics`
  dimensions query+page, monitored weekly.

### Pillar 3 — Real-time GST compliance narrative, gated on shipping
- **Evidence:** competitor watchlist (2026-09-24) names Vyapar/Khatabook's batch-upload lag as a
  real, cited gap, and a real 2025-26 regulatory mandate creates urgency. BUT: repo evidence shows
  `einvoiceService.ts`/`ewaybillService.ts` are explicitly labeled `STATUS: STUB` pending NIC API
  credentials — not live in production today.
- **Channel/format:** hold this pillar in backlog until `EINVOICE_ENABLED=true` ships to
  production; then it becomes a Pillar-1-style LinkedIn engineering post (same pattern, strongest
  possible proof point once real) and a comparison blog post.
- **KPI:** not yet applicable — gated on a real ship event, not a calendar date.

### Pillar 4 — Services-line proof-by-association (LinkedIn + Services landing page, low cadence)
- **Evidence:** Services line has zero organic search share (confirmed again this run — no
  non-branded services query in top ~50 GSC rows) and zero backlinks (Bing Webmaster: 0 for
  astrastudio.in). No completed client case study exists to cite yet. Council verdict from the
  2026-09-24 campaign cycle (`campaigns/2026-09-24-indexing-bug-fix/plan.md`): Services needs
  credibility built via 2-3 successful Pillar-1 posts before it can run a standalone pricing pitch
  — "you can't sell custom dev with no client story, but you can sell it on your own site as the
  proof."
- **Channel/format:** do not run standalone Services posts yet. Fold Services mentions into
  Pillar-1 posts as a soft cross-sell line (the 3-months-Atlas-free hook) once 2+ engineering posts
  have published and produced measurable engagement.
- **KPI:** unknown, test it — no baseline exists until Pillar 1 has run long enough to lend it
  credibility.

---

## 5. Channel plan

| Channel | Role | Cadence | Formats | Status |
|---|---|---|---|---|
| LinkedIn | Primary — founder-led technical credibility (Pillar 1, eventually 3 & 4) | 1x/week, tied to a real shipped commit | Native text post, no external link | Live, approval-gated (Vishal approves every draft via `request_publish_approval`) |
| Blog (astrastudio.in/blog) | Secondary — SEO recovery, comparison content (Pillar 2) | As shipped/research-justified, not fixed calendar | Long-form comparison/use-case posts, free-tool companion posts | Live, publishes via blog CMS + admin panel (commit c34794e) |
| Free tools (astrastudio.in/tools) | Supporting — lead-gen/engineering-as-marketing | Already 13 live; extend only with genuinely new tool ideas | Interactive calculators/generators | Live |
| Directory listings (SaaSHub, AlternativeTo, G2, IndiaMART, Dev.to) | Supporting — backlinks (currently 0) + discovery | One-time setup, needs Vishal's business email/GST verification | Structured listings | Drafted (`campaigns/2026-09-19-directory-submissions/plan.md`), blocked on Vishal action |
| Instagram/Facebook/Reddit | Not active | — | — | Not connected for this brand |

---

## 6. Experiment backlog

Hypothesis → evidence → metric → status. Max 2 running at once.

1. **LinkedIn founder-led engineering posts drive measurable engagement for a technical SMB SaaS
   audience.** Evidence: 3 campaigns drafted (Sep 5, 6, 24) using real commits; brand context names
   LinkedIn as high-priority. Metric: `get_post_analytics` impressions/reactions per post once
   Vishal approves and publishes. **Status: running** (posts pending Vishal's approval as of
   2026-09-24; no published post yet to measure).
2. **The indexing fix (commit c34794e) recovers non-branded organic clicks within 90 days.**
   Evidence: GSC 2026-09-24 snapshot shows early impression recovery on previously-suppressed pages
   (`/tally-alternative` 227 impr, `/tools/hsn-code/2106` 125 impr) just 5 days post-fix. Metric:
   non-branded clicks (north star). **Status: running** (this IS the north star tracking, treated
   as the second concurrent experiment slot).
3. **Directory listings (SaaSHub, AlternativeTo, G2, IndiaMART) generate real backlinks.** Evidence:
   Bing backlinks currently 0; kit fully drafted 2026-09-19. Metric: Bing Webmaster backlink count.
   **Status: proposed** — blocked on Vishal providing business email/GST verification per the
   campaign's "What's still needed from Vishal" section; not started, don't count as a running slot
   until unblocked.
4. **Real-time GST compliance ("we sync faster than Vyapar/Khatabook") as a differentiator claim.**
   Evidence: competitor gap is real (watchlist 2026-09-24) but our own feature is an unactivated
   code stub. Metric: n/a. **Status: proposed, explicitly gated** — do not start until
   `EINVOICE_ENABLED=true` ships to production (see "We will NOT do" below).

---

## 7. We will NOT do

- **Claim live real-time GSTN e-invoice/e-way bill sync today.** The code exists
  (`einvoiceService.ts`, `ewaybillService.ts`) but is explicitly a stub pending NIC API
  credentials — publishing this as a shipped differentiator against Vyapar/Khatabook would be a
  false claim the moment a prospect tests it. Evidence: direct repo read, both files' header
  comments, 2026-09-24.
- **Run a standalone Services-line pricing/positioning post with no case study to cite.** Council
  review during the 2026-09-24 campaign cycle explicitly rejected this sequencing — Services has
  zero organic, zero backlinks, and no completed client project to reference yet; a pricing pitch
  with no proof reads as generic. Fold Services into engineering-credibility posts instead
  (Pillar 4).
- **Quote GA4 traffic numbers for astrastudio.in.** Property 538401917 / stream www.astrastudio.in
  still returns zero rows this run despite a tag being added in code — per the verified 2026-09-25
  analytics map, astrastudio.in currently has Search Console only. Do not infer GA4 session numbers
  from the MadeByHer legacy property or any other source.
- **Publish a generic "here are our free tools" post.** Per `docs/free-tools.md`, 3 blog posts
  already cover all 13 tools' clusters — a 4th generic tools post would be redundant; only a
  genuinely new angle (single-tool deep dive, comparison, how-to) qualifies.
- **Pursue a full Product Hunt Tier-1 launch now.** Per the directory-submissions kit (2026-09-19):
  "doing it half-prepared burns the one-shot advantage" — no 60-90s demo video exists yet: revisit
  once Services has a warm audience.

---

## 8. Review log

- **2026-09-24 — strategy.md created from scratch.** First synthesis for this brand (per
  growth-strategy skill, none existed before). Built from: 5 research files (2026-09-04 x2,
  2026-09-18, 2026-09-21, 2026-09-24), 3 analysis snapshots (2026-09-18/21/24), competitor
  watchlist (2026-09-24 entry), 4 campaign plans (2026-09-05, 2026-09-06, 2026-09-19, 2026-09-24),
  docs/PROJECT_OVERVIEW.md, docs/free-tools.md, live GSC pull (query+page dimensions, 28 days),
  live repo grep of einvoice/ewaybill/offline-sync code, live GA4 property check (zero data
  confirmed again), live Bing backlinks check (zero confirmed), live WebSearch site: crawl
  (confirms which pages are actually indexed/showing in results).
  - **North star chosen:** non-branded organic GSC clicks, baseline ~5/28-day window. Chose this
    over an MQL/lead metric because no lead-capture event is wired to measure MQLs honestly yet.
  - **Council review (flagship tier) result:** Asked for north star + top-3 pillars given the same
    evidence. 2 of 4 models errored (Claude: 502 Bad Gateway; Gemini and Mistral: 429 rate-limited
    after retries) — only Groq (`openai/gpt-oss-120b`) returned a substantive answer, so this is a
    **1-model result, not a consensus** — treat with appropriately lower confidence than the
    2/2-agreement precedent set by the 2026-09-24 campaign's own council call.
    - **Groq's proposal:** North star = "30 organic-qualified-lead (MQL) conversions/month,
      baseline 0" — rejected here because no tracking exists to measure it honestly (would violate
      the skill's "no number, no claim" rule; an MQL count is currently unmeasurable, not just
      currently zero).
    - **Groq's top pillar:** "SEO Recovery & Authority-Building" — sitemap resubmission, canonical
      fix verification, content-cluster rollout (4 pillar pages: real-time GST compliance, POS/
      inventory, WhatsApp CRM, legal-tech), link-building outreach, technical SEO lockdown
      (structured data). This **matches** Pillar 2 here directly, and its GST-compliance pillar
      idea is why Pillar 3 exists in this file — but Groq's framing treated real-time GST
      compliance as ready to publish; this file explicitly gates that pillar behind the stub-vs-
      shipped distinction found in the actual codebase, which Groq's answer did not have access to
      verify (the question described the mandate but not the stub status in enough force to
      override it). **Where I diverged:** kept LinkedIn/Pillar-1 (founder-led engineering
      credibility) as the top-ranked pillar rather than SEO-first, because (a) it's the brand's
      explicitly stated priority channel per `astrastudio` skill context, (b) it already has 3
      real drafted campaigns with proven evidence-grounding discipline and zero published output
      yet to disprove it, and (c) the SEO recovery pillar's own success (Pillar 2 here) depends on
      content that already exists and just needs the fixed indexing to take effect — it doesn't
      need a new campaign motion the way LinkedIn does. Both pillars are kept, ranked 1 (LinkedIn)
      and 2 (SEO), consistent with Groq's SEO substance but reordered against the brand's own
      stated channel priority. Real-time GST compliance kept explicitly gated (not published) per
      direct repo evidence Groq's answer couldn't see.
  - **Action:** strategy.md is now the required first-read for every future Astra Studio campaign/
    blog/social task per the growth-strategy skill.
