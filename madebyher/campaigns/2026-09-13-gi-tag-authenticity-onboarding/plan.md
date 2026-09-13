# Campaign Plan: GI-Tag Authenticity for Festival Gifting

**Campaign ID:** 2026-09-13-gi-tag-authenticity-onboarding
**Date:** 2026-09-13
**Status:** drafted

## council_review call (attempted, unavailable this run)

Per the campaign-workflow and routing-and-approvals skills, this weekly pick should go through
`council_review(tier="flagship")` before committing. That tool was attempted repeatedly this run
(direct call, MCP tool_call wrapper, and a subagent dispatched to verify independently) and failed
every time with "not a deferrable tool" / not present in the model-facing tool list, even though
`hermes mcp test hermes-admin` confirms the tool exists server-side (added 2026-09-12, one day
before this run) and the cache file `~/.hermes/cache/mcp_schema_cache.json` lists it. This looks
like a stale tool-router snapshot for this session that predates the 2026-09-12 admin-server
update, not a real absence of the capability. Flagging for Vishal: **council_review could not be
reached this cycle** - the pick below is my own judgment, not a multi-model verdict. Recommend
re-running the council_review check next cycle to confirm it is now reachable.

**The question I would have asked** (recorded so next cycle can actually ask it):
"MadeByHer (women-led Bihar artisanal marketplace) has three scored opportunities from this
week's research: (1) GI-onboarding via the new Bharat GI Initiative program (score 8.5, HIGH,
time-sensitive - named govt pathway to ONDC/GeM launched 2026-08-05, only a month old) letting
MadeByHer's GI-tagged sellers (Madhubani, Sikki, Sujni, Bawan Buti) get onboarded for discovery;
(2) a fourth consecutive Diwali+Chhath gifting/Pinterest-trend campaign (score 8, IMMEDIATE, 5-day
gap between Diwali Nov 8 and Chhath Nov 13-16 this year) - already the subject of the last three
weekly campaigns (2026-08-23, 2026-08-30, 2026-09-06), which have already covered thekua, madhubani
soop, sikki jewelry, crochet nostalgia, and Pen Pals/Throwback Kid Pinterest trend tie-ins;
(3) an artisan story/SEO content hub (score 8, HIGH) - which is already running as a near-daily
blog cron per `learnings/blog-topics-log.md`. Given three consecutive cycles already spent on the
same Diwali/Chhath consumer-gifting angle, and a genuinely new, time-sensitive, named government
program that's gone unused for two research cycles running, which deserves this week's campaign
production effort: a fourth iteration of the gifting/trend angle, or a first pass at GI-tag
authenticity/provenance content that both serves the government-program opportunity's B2B lane
and gives Pinterest a new (not-yet-used) consumer angle?"

## My judgment (since council_review didn't run)

Picked a **hybrid**: GI-tag authenticity as the new Pinterest consumer angle, with the Bharat GI
Initiative program surfaced as the LinkedIn/founder story. Reasoning:

- The last three campaigns (08-23, 08-30, 09-06) already exhausted the "Diwali/Chhath gifting +
  Pinterest Predicts trend" angle - same SKUs (thekua, madhubani soop, sikki jewelry, crochet),
  overlapping hooks ("vintage," "nostalgia," "Throwback Kid," "Pen Pals"). A fourth cycle of the
  same trend-chase risks repetitive content on the same boards, not compounding reach.
- The GI-onboarding opportunity (score 8.5, the highest-scored item in this week's research) has
  been flagged for two consecutive research cycles (08-30, 09-04) without a campaign response -
  it's the most time-sensitive unaddressed item in the vault, not a new idea I'm inventing.
- GI tags map naturally to a genuinely different Pinterest angle than the last three cycles used:
  authenticity/provenance ("how to tell a real Madhubani from a mass-produced copy") rather than
  trend-chasing. This also plays directly into the research's own SEO-gap finding (vendor page
  authority, dual-sided keyword strategy) and gives festival gift-shoppers a reason to buy from
  MadeByHer over Amazon Karigar/Flipkart Samarth/generic marketplaces: legal/craft authenticity,
  not just aesthetic.
- Diwali/Chhath timing still applies (8 weeks out) - this isn't abandoning the festival window,
  it's a different creative angle on the same commercial season, avoiding repeating the last three
  weeks' specific hooks and boards.

## Objective
Build a Pinterest-led authenticity/provenance narrative around MadeByHer's GI-tagged and
heritage Bihar crafts (Madhubani, Sikki, Sujni, and the traditional-but-less-known crafts already
covered on the live blog: Manjusha, Tikuli, Khatwa, Lac Bangles) ahead of Diwali/Chhath gifting,
differentiating from mass-produced "ethnic decor" competitors. Secondary: one LinkedIn founder
post using the new Bharat GI Initiative (Aug 5, 2026 MSME+DPIIT program) as a first-mover
positioning story - the program is one month old and MadeByHer hasn't acted on it publicly yet.

## Hypothesis
Festival gift buyers increasingly can't tell a genuine GI-tagged Madhubani/Sikki/Sujni piece from
a mass-produced import claiming the same aesthetic. A Pinterest series that teaches buyers what to
look for (motifs, materials, GI certification, artisan-made tells) builds trust ahead of purchase
and gives MadeByHer a differentiated angle its competitor set (iTokri, Okhai, Gaatha, Jaypore) has
not used - none of their tracked content in `competitors/watchlist.md` runs an authenticity-education
angle. Unlike the last three campaigns' trend-surfing approach, this content also compounds as
evergreen SEO/Pinterest search fodder ("real vs fake madhubani painting," "how to tell authentic
sikki grass jewelry") rather than one aesthetic-trend cycle.

## Target Audience
- Primary: Festival gift buyers (women 25-45, India + diaspora) who want to give something real
  and are wary of mass-produced "ethnic" décor - searching "authentic madhubani painting," "real
  sikki grass jewelry," "handmade vs machine made gifts."
- Secondary: Gen Z/millennial Pinterest users interested in craft provenance and slow-made goods
  as part of the broader "vintage/thrift authenticity" search behavior already noted in research
  (thrift searches +127% YoY).
- Tertiary (LinkedIn): MSME/artisan-economy watchers, ONDC/GeM ecosystem players, potential GI
  program partners - founder-voice audience, not consumer.

## Research Finding This Responds To
From `2026-09-04-deep-research.md`:
- Delta table row 1 (Bharat GI Initiative): "Government now actively onboarding GI-registered
  collectives/producers onto ONDC and GeM... Check eligibility to have MadeByHer's GI-tagged
  sellers/products (Madhubani, Sikki, Sujni, Bawan Buti) onboarded... direct continuation of the
  GI opportunity already scored 8.5."
- Opportunity Scoring: "GI-onboarding via Bharat GI Initiative (ONDC+GeM)" - score 8.5, HIGH,
  "time-sensitive, program is 1 month old."
From `2026-08-30-deep-research.md` (carried forward, unchanged):
- "GI-tagged product lines (13 tags incl 3 NEW Jun 2026)" - score 8.5 - "Legal defensibility,
  premium pricing, export-ready HS codes, new 2026 GI tags (Bawan Buti, Patharkatti, Pidiya)."
- Section 4.1 SEO gap: "Vendor page authority diluted... vernacular/regional keyword gap" -
  addressed here by authenticity-education content, not just product listings.

## Channels Used
1. **Pinterest** (primary, live account @madebyher001) - 6 pin drafts, authenticity/provenance
   angle across Madhubani, Sikki, Sujni, and heritage crafts already covered on the live blog.
2. **LinkedIn** (secondary, live account, Vishal Kumar) - one founder post positioning MadeByHer
   against the one-month-old Bharat GI Initiative, drafted via `linkedin-post-writer` formula F7
   (odd-precision number opener), goal = comments/credibility with MSME-adjacent audience.
3. **Instagram** (secondary, not connected - manual draft for Vishal to post by hand).

## Publishing status
Pinterest and LinkedIn drafts were created via `hermes-social` `create_draft` (both landed as
`pending_approval`, not pre-approved - see note below) and this cycle also attempted `publish()`
per the campaign-workflow's stated auto-publish behavior. The real API response contradicted that
documentation: `publish()` returned a 403 refusal ("status 'pending_approval', not 'approved'"),
not a `provider_post_id`. **Nothing was published.** This is a live discrepancy between what the
campaign-workflow skill describes (auto-publish, no approval queue) and what the `hermes-social`
gateway actually enforces (still gates on an `approved` status) - flagging for Vishal to reconcile.
Called `request_publish_approval()` on both real drafts so they surface in his Telegram approval
queue:

- Pinterest draft `a6cbcad2-e4e4-4039-808d-a8d9e4ed9c78` (Pin 1, Madhubani authenticity) - pending
  Vishal's approval. Note: text-only, no image attached (see Image gap below) - attach a real
  Madhubani product photo before approving/posting if possible.
- LinkedIn draft `93cc78d4-6547-48f4-afc6-0e3be11a58a2` (Bharat GI Initiative founder post) -
  pending Vishal's approval.
- Pins 2-6 and the Instagram concept are file-only drafts in this folder (not yet pushed through
  `create_draft`) - only pushed the lead Pinterest pin and the LinkedIn post as real drafts this
  cycle to keep the approval queue reviewable; push the remaining Pinterest pins as real drafts
  once Vishal has reacted to pin 1's angle and confirmed the direction.

Instagram draft is a plain file, no account connected, Vishal posts manually.

**Housekeeping:** a diagnostic test draft (`dc8cf846-5b98-4864-ad1f-e69b8eb96688`, campaign_id
`test-diagnostic-ignore`, text "diagnostic test - do not publish") was created early in this run
to verify the create_draft/publish mechanics before committing to real copy. It sits in
`pending_approval` too but was never sent for approval - safe to ignore or delete, not part of
this campaign.

## Image gap this cycle
`admin_search_products` (for real Cloudinary product photos) and `generate_image` (Pollinations
fallback) are both newer tools added in the same 2026-09-12 admin-server update as
`council_review`, and both hit the same stale-tool-router wall this run. Pinterest/Instagram
drafts below are text-only - Vishal needs to attach real product photos before posting (real
Madhubani/Sikki/Sujni product shots strongly preferred per the campaign-workflow skill, since
these pins are about specific craft categories, not a general brand post).

## Other flags from this research cycle (not part of this campaign, noted for visibility)
- **Blog backlog:** `learnings/blog-topics-log.md` shows 5 posts (Chhath Puja Gifts, Madhubani
  Buying Guide, Sikki Grass Jewelry, Sujni Embroidery, Thekua Buying Guide - dated Aug 25 through
  Sep 6) still sitting in `Draft` status, while every post from Sep 7 onward auto-publishes. These
  five were the exact posts the 2026-09-04 research recommended publishing "before mid-Sep" for
  the 6-8 week pre-festival lead time competitors like iTokri use - that date has now passed
  (today is Sep 13) with all five still unpublished. Worth a look outside this campaign cycle.

## Success Metrics (pending)
- Pinterest: impressions, saves, outbound clicks per pin, board follower growth on the
  authenticity-angle pins vs the last three cycles' trend-angle pins (comparison point for
  learning loop).
- LinkedIn: impressions, reactions, comments, profile visits, any inbound from MSME/ONDC-adjacent
  accounts.
- Instagram (once posted): reach, saves, profile visits.

## Outcome
Pending - Phase 4 will fill in metrics and outcome once Vishal approves and posts run.
