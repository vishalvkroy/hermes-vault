# RabbitLore Strategy

Living strategy document. Read first by every campaign/blog/social executor. Updated by
research crons per the growth-strategy skill loop (research -> strategy -> execution ->
performance-log -> strategy).

## 1. North star + 90-day goal

**North star metric:** Night-Gated Lore Sessions × Unique Participants (NG-LS×UP) — count of
private, time-gated (11pm-4am IST) lore-sharing encounters in rooms/DMs between real users,
counting distinct participants who posted at least one lore snippet in the session. This is the
literal product mechanic the last two research cycles both named as the top opportunity
(`research/2026-09-21.md`, `research/2026-09-24.md`).

**Baseline: unknown — not instrumented here.** RabbitLore has no GA4/GSC binding and no app
analytics pipeline confirmed live (`analytics-map 2026-09-25`: RabbitLore Android streams exist
in GA4 property 538401917 but show zero data). The event data needed for NG-LS×UP already
exists as raw rows in the backend DB (room/DM opens are logged — see `rabbithole` repo,
night-gate commit `391063f`), it is just not aggregated or reported anywhere. **Action, not a
metric:** instrument this before the next strategy review — a daily cron job summing
`sessions × distinct participants` from existing DB rows would make this real within days, no
new SDK needed.

**Interim proxy metric (has a real baseline today):** published build-in-public/founder posts
on the one connected, live channel (LinkedIn). Baseline as of 2026-09-24: **2 posts published**
(`campaigns/2026-09-06-linkedin-blend-holes-night-gate/plan.md`, published
2026-09-06T10:41:40Z, urn:li:share:7502315073433104384; a second LinkedIn draft
`115d7a8b-523a-4f71-8995-064b780458cc` also published per that campaign's log). Post-level
engagement is itself unknown — `get_post_analytics` returned `"collected": false` for the
checked post as of this write. Reddit: **0 posts published** — Reddit has no connected
`hermes-social` account for this brand; all Reddit content is drafted and must be posted by
Vishal by hand (`campaigns/2026-09-05-*`, `2026-09-06-reddit-curiosity-ranker-was-dead`,
`2026-09-24-reddit-night-gated-lore-launch` — 3 drafts, 0 confirmed live).

**90-day goal:** (1) instrument NG-LS×UP so a real baseline exists, (2) get at least 3 Reddit
posts actually live (posted by Vishal from drafts) in communities that fit the audience, (3)
keep LinkedIn build-in-public cadence going without repeating an angle already used.

## 2. Positioning & differentiation

Every watchlist competitor (`competitors/watchlist.md`, 5 entries as of 2026-10-10), one row
each. Claims checked against `docs/positioning.md` and real shipped commits — nothing here is
aspirational. **Coverstar (new 2026-10-10)** is tracked on the watchlist but deliberately not
given its own row here — see Competitive Edge in `research/2026-10-10.md`: different audience
(Gen Alpha children, not RabbitLore's adult/young-adult base) and different mechanic (public
video feed, not private peer-matching), so no differentiation claim is needed yet.

| Competitor | Their claim | Our real proof | Our edge | Message we lead with |
|---|---|---|---|---|
| **Yope** | London-based private "micro-community" app — no algorithmic feed, no ads, accounts private by default, $12.3M Series A, ~15M users/~500M photos since 2024 launch (`research/2026-10-01.md` [1][2]) — proof-at-scale that "private beats public" works for young users, but built around friend-group photo/chat sharing + AI memory recaps, not lore-matching or avatar-as-record | `getBlend` real peer-to-peer lore-category/tag overlap (`rabbithole 7c4e05a`); night-gate time-boxed sharing (`rabbithole-mobile 391063f`); constellation star-map avatar record (`rabbithole-mobile bd3b252`) — none of these exist in a general friend-photo-sharing app | Yope validates the macro-thesis (private > public) at scale, which is reassurance, not a reason to copy its feature set — RabbitLore's differentiator is matching strangers who share your specific lore/obsessions, not keeping your existing friend group's photos private | "Not another private photo album for people who already know each other. A place where a stranger turns out to think the same weird thoughts you do." (internal framing only — not yet drafted as outward copy this run) |
| **Zentara** | AI-powered avatars/VTubers for virtual companions, cross-platform connectivity, creator monetization — a public, commercial creator platform (`research/2026-09-18.md` [21]); **2026-10-29:** Tracxn confirms Zentara remains fully unfunded, ranked 914th of 1,348 tracked social-network competitors, Tracxn Score 16/100 (`research/2026-10-29.md`) — a numeric basis for the "no real traction" read, not just an absence of news | Night-gate (11pm-4am IST) locks lore-sharing in rooms+DMs (`rabbithole-mobile 391063f`); `getBlend` matches by real overlapping lore category+tag between two actual users, not an AI companion (`rabbithole 7c4e05a`) | Zentara sells visibility and monetized creator personas; RabbitLore sells private, human-to-human recognition with no follower count attached | "No AI companion pretending to care. Two real people whose lore actually overlaps." |
| **ZenFriend** | AI virtual friend targeting Gen Z loneliness/anxiety — a simulated bot relationship (`research/2026-09-18.md` [11]). **2026-10-29 context (not a ZenFriend-specific update, category evidence):** a Guardian "intimacy economy" essay gives a sharper first-person account of the exact behavior ZenFriend's category sells into — a 27-year-old confiding in an AI chatbot more than human friends while calling it, in his own words, "a business product" (`research/2026-10-29.md`) | `getBlend` collision is peer-to-peer (real user-to-user tag/category overlap, `rabbithole 7c4e05a`); "holes" mechanic (`getLikers`, `rabbithole 9c66801`) shows who — a real person — fell into your lore, capped at 100, public | ZenFriend's "friend" is a simulation; ours is a stranger who turns out to think the same weird thoughts you do — the actual emotional payoff positioning.md names ("I thought I was the only one") | "Not a bot pretending to understand. A real person who already gets it." |
| **Highrise / ZEPETO** | Deep avatar customization, fashion-forward, K-style/streetwear aesthetic, public social integration — aspirational look-and-be-seen (`research/2026-09-18.md` [27], `research/2026-09-21.md` [5]) | Constellation star-map turns *logged lore* (not outfits) into the visible artifact — deterministic, append-stable layout, one star per lore entry (`rabbithole-mobile bd3b252`, `1513283`); avatar customization here pairs with content, not clout. **New 2026-09-28:** no public room/DM surface for strangers to find a user in, by design (`rabbithole-mobile` night-gate `391063f`) — real, checkable structural fact, not a comparison claim | Highrise/ZEPETO customization is external performance (what you look like to strangers); RabbitLore customization is internal record (what you've actually carried inside you). **New:** Highrise's public rooms carry real, current user-reported trust costs (minors DMed by adults, gambling-style "casino" rooms, account hacks — `research/2026-09-28.md` §2/§3, watchlist.md) that a private, no-public-room app structurally doesn't have to defend against. **New 2026-10-12:** Apple's App Store 13+ social-media declaration rule (effective Sept 2026) structurally exempts DM/private-room-only apps — feeds and discovery surfaces trigger the 13+ floor, one-to-one DMs/private rooms do not (`research/2026-10-12.md` [3]) — a second, independent structural reason (regulatory/compliance, not just trust-cost) a public-feed/room model like Highrise's carries a real cost RabbitLore's architecture doesn't, stated as a design/compliance fact, not a claim about any specific enforcement action | "Your avatar isn't a fit check. It's a map of what's in your head." (Reddit copy may add, only when the "why is this different" question comes up organically: "there's no public room here for a stranger to find you in" — framed as what we built, never as a Highrise callout, per `research/2026-09-28.md` Competitive Edge §3) |

## 3. Audience segments

Per `docs/positioning.md` (only source — no GSC/GA4 query data exists to add real search terms
yet, flagged so nobody invents queries): overthinkers, creative people, nerds, dreamers, gamers,
writers, programmers, history lovers, people with strange/niche obsessions, "lonely kids who
grew up," people who carry entire inner worlds. Where they are: Reddit communities adjacent to
indie-dev/app-design, journaling, overthinking/mental-health-adjacent, and avatar/customization
culture (exact subreddits need Vishal's live judgment per `reddit.md` notes in each campaign —
mod tolerance for app mentions shifts); LinkedIn for the founder/builder audience (secondary,
not the core Gen Z user, but where authentic build-in-public content performs per
`campaigns/2026-09-06-linkedin-blend-holes-night-gate/plan.md`, the one published, trackable
result).

## 4. Content pillars

Executors only make content that maps to one of these 4. Each requires 2+ research snapshots or
a real shipped-feature commit as evidence — no pillar here rests on a single week's signal.

### Pillar 1 — Night-gated private lore sharing
- **Evidence:** Top Opportunity independently in both `research/2026-09-21.md` and
  `research/2026-09-24.md` (2 consecutive snapshots, the bar `campaigns/2026-09-24-*` already
  applied); shipped in `rabbithole-mobile 391063f`. **2026-09-28:** Google Trends showed a
  2-week non-zero reading for "faceless creator app" (0 → 14 → 12) after a flat year.
  **2026-10-01 correction:** that reading reverted to 0 the following week — a decayed spike, not
  a sustained trend; the pillar's evidentiary weight now rests on the 2 repeated Top-Opportunity
  research calls and the shipped feature, not on this trends data point, which should not be
  re-cited as "rising" going forward. **2026-10-01, separately:** Yope's $12.3M raise / 15M users
  (`research/2026-10-01.md`, `watchlist.md`) is real external proof-at-scale that the broader
  "private beats public" macro-thesis behind this pillar is commercially validated, even though
  Yope's own product (friend-group photo/chat sharing) is a different mechanic than RabbitLore's
  peer lore-matching — treat as reassurance on direction, not evidence for the specific mechanic.
  **2026-10-10 correction:** "private social app" and "close friends app" Google Trends readings
  (the broader category search terms, not RabbitLore-specific) have now declined for 2 consecutive
  weekly snapshots each — "private social app" 56→28→7→5, "close friends app" 70→38→18→16, both
  down from a 100-peak in late May/early June 2026. This category-level search interest is
  cooling, not rising; do not cite "category interest accelerating" as supporting evidence for
  this pillar going forward — the pillar's evidentiary weight stays on the 2 repeated
  Top-Opportunity research calls, the shipped feature, and Yope's funding/regulatory validation,
  none of which this trends data affects. **2026-10-12:** the decline has flattened (not reversed)
  for one partial week ("private social app" 9→5→3, "close friends app" 2→2→1) — not a confirmed
  trend change, standing correction unchanged. **2026-10-15 correction:** those partial-week
  numbers were undercounts — the now-closed week reads "private social app" 5 (not 3) and "close
  friends app" 21 (not 1), with "close friends app" moving up off the Oct 4-10 floor (16→21), the
  opposite direction from what the partial read implied. One closed week is still short of the
  2-consecutive-reading bar for calling a reversal, so this pillar's "don't claim category
  acceleration" correction stays in force — but the exact numbers logged 2026-10-12 for that week
  are superseded, not repeated (`research/2026-10-15.md`). Separately, new structural evidence this run: Apple's
  App Store 13+ social-media declaration rule (Sept 2026) exempts DM/private-room-only apps like
  RabbitLore while targeting public-feed/room models (`research/2026-10-12.md` [3]) — a real,
  checkable compliance fact that strengthens this pillar's non-attack positioning line without
  changing the pillar itself. **2026-10-19 addition:** two independent pieces of external evidence
  this run further corroborate the macro-thesis (not the specific mechanic): (1) a "Posting Zero"/
  ghost-posting Gen Z behavioral trend, documented in two dated articles 8 months apart
  (Moneycontrol, Jan 2026; Globe and Mail, Sep 2026) — real Gen Z users moving public posting into
  private DMs, Close Friends lists, and group chats while leaving public grids empty
  (`research/2026-10-19.md` [5][6]); (2) Meta's Night Mode — a midnight-6am Instagram/Facebook
  access block for under-18 users, required within 6 months of an ~$18B multi-state settlement
  (TechCrunch — corrects the $17B figure logged in the 2026-10-01 review-log entry below, which
  should be read as superseded) — the largest social platform in the world now structurally
  restricting after-midnight teen access, the same hours RabbitLore's own night-gate already
  restricts (`research/2026-10-19.md` [3][4]). Platform-policy and named-behavior validation,
  not a competitor move — no pillar or claim changes, evidentiary weight stays primarily on the
  2 repeated Top-Opportunity research calls and the shipped feature. **2026-10-22 addition:**
  Retro — a friends-only photo-journal app built by ex-Instagram engineers — closed a $21M
  Series A (Field Ventures, Thrive Capital, Aug 2026) and by mid-October reported 7M downloads
  on that raise (`research/2026-10-22.md` [1][2][3]), a second independently-funded "anti-feed"
  competitor alongside Yope validating the same macro-thesis bracket, not RabbitLore's specific
  mechanic — same track-not-chase treatment. Separately, a balancing nuance from MIDiA Research
  (Oct 21 2026): their Q2 2026 consumer survey found "entertainment" has overtaken "connecting
  with friends" as Western users' top social-media motive, with the market bifurcating into
  entertainment-first vs. peer-to-peer apps (`research/2026-10-22.md` [4]) — RabbitLore sits in
  the peer-to-peer half, so this doesn't contradict Pillar 1, but future copy should not overclaim
  "private is simply winning everywhere" — the real picture is a split market, not a one-way
  swing. **2026-10-26 addition:** Posting2 — a Chicago-built, no-algorithm, chronological-feed
  app explicitly compared to "old Instagram" — grew from ~1,600 beta users (April 2026) to
  ~36,671-37,000 users by Oct 21-22 2026, +42% month-over-month downloads in September, confirmed
  by two independently-dated sources (Fast Company; Afterschool Substack) (`research/2026-10-26.md`
  [1][2][3]). This is the **third** anti-feed macro-thesis proof point and the **first unfunded**
  one in the set — Yope raised $12.3M, Retro raised $21M, Posting2 grew to ~37,000 users on $0 in
  funding, purely word-of-mouth plus user donations/tips (364 of 37,732 users, 1.0%, pay monthly
  per the app's own site). Still track-not-chase: Posting2's open, scaling friends-of-friends
  feed is structurally the opposite of RabbitLore's capped, night-gated design. Genuinely useful
  addition: a cited Posting2 early-user complaint about strangers commenting as the app scales
  ("Posting2 needs to decide what it wants to be," `research/2026-10-26.md` [1]) is a concrete,
  citable argument for why RabbitLore's structural caps (night-gate, `getBlend` matching, the
  100-cap on "holes") solve a real problem rather than an invented one — usable almost verbatim
  as a Reddit devlog hook for a builder/dev audience skeptical of funding-round PR.
  **2026-10-29 addition:** Posting2's growth story cleared a 3-independent-source confirmation
  bar within 3 days — a 3rd editorial source (YPulse, Oct 27 2026) independently covered the same
  story (framed explicitly as a Finsta/Close-Friends-list alternative), and a 4th, non-editorial
  data source (MWM app intelligence: 10k+ downloads, 5.0 rating, 319 ratings) corroborated it from
  a different angle than Fast Company or the app's own site (`research/2026-10-29.md`). This is
  now the strongest multi-source-corroborated proof point in this entire research line — stronger
  anchor citation for the next Reddit devlog than Yope's or Retro's funding-round figures, because
  three separate outlets covered the same organic story with no PR push behind it.
- **Channel/format:** Reddit (primary — genuine contribution posts, not ads), short-form video
  concept (secondary, gated on Vishal's go-ahead before any generation spend).
  Council-review flagged (see §6) as the strongest anti-virality proof point: scarcity via a
  closing time window, not share counts. **2026-09-28 copy note:** when a Reddit thread/reply
  organically raises "why is this different from other avatar apps," the structural "no public
  room for a stranger to find you in" point (see §2 Highrise/ZEPETO row) is available as a
  non-attack, positioning-only answer — do not lead with it, do not name Highrise.
- **KPI:** Reddit posts actually posted by Vishal (currently 0/5+ drafted); once instrumented,
  NG-LS×UP session counts.

### Pillar 2 — Narrative avatar / story-tokens (not fashion)
- **Evidence:** Constellation star-map shipped (`rabbithole-mobile bd3b252`, `1513283`,
  `0e2f6de` — deterministic append-stable layout, one star per logged lore entry); positions
  directly against Highrise/ZEPETO's fashion-aspirational model (§2 row 3). Council review (§6)
  independently named this as pillar #2.
- **Channel/format:** LinkedIn (founder-story angle: why avatars here work differently),
  in-app UI itself is the primary "content" — no separate campaign needed until a screenshot-led
  post is drafted.
- **KPI:** unknown — instrument avatar-customization-per-active-user; until then, qualitative
  (does copy get comments recognizing the "not a fit check" framing).

### Pillar 3 — Human "blend" matching (anti-AI-companion)
- **Evidence:** `getBlend` real collision detection by overlapping lore category+tag
  (`rabbithole 7c4e05a`), gravitational blend canvas (`rabbithole-mobile c12fba4`), emotional
  redesign away from a stats dashboard (`93a7d75`). Directly undercuts Zentara and ZenFriend's
  AI-companion/creator-monetization positioning (§2 rows 1-2).
- **Channel/format:** Reddit (comparison-adjacent posts in loneliness/anxiety-support-adjacent
  threads, framed as genuine contribution, never "we're better than X"), LinkedIn (product-
  decision framing).
- **KPI:** unknown — instrument blend-match-accepted rate; interim proxy is qualitative comment
  sentiment on published posts.

### Pillar 4 — Build-in-public engineering honesty
- **Evidence:** `2026-09-06-reddit-curiosity-ranker-was-dead` campaign — real postmortem, the
  For You feed silently fell back to popularity-only ranking for an unknown period because a
  hardcoded `21` gate never matched the real 29-dim vector (`rabbithole 57b0f59`, self-healing
  fix `f3a9868`). This angle already produced one published LinkedIn post
  (`campaigns/2026-09-06-linkedin-blend-holes-night-gate` — published, urn:li:share:
  7502315073433104384) — the only pillar with a confirmed-published, non-pending result so far.
- **Channel/format:** Reddit (indie-dev/webdev/programming communities), LinkedIn
  (founder/builder audience).
- **KPI:** posts published (baseline 2/2 LinkedIn drafts this angle attempted → published);
  engagement unknown, `get_post_analytics` not yet collected.

*(4 pillars, within the skill's 3-5 range. A 5th — "faceless-creator wave" — was considered
from `research/2026-09-21.md`/`2026-09-24.md` but rejected: it describes what Picsart Persona
and the TikTok caricature trend are doing, which research/2026-09-21's own Competitive Edge
section says explicitly is NOT worth chasing for RabbitLore — see §7.)*

## 5. Channel plan

| Channel | Role | Cadence | Formats | Status |
|---|---|---|---|---|
| Reddit | Primary — genuine community contribution, brand's stated channel priority (spec section 12) | One well-placed post per campaign, no mass-posting | Devlog/postmortem posts, feature-explainer posts | **Manual** — no connected `hermes-social` Reddit account for this brand; Vishal posts by hand from drafts (`reddit.md` in each campaign folder) |
| LinkedIn | Secondary — founder/builder story | As campaigns produce real shipped-feature material, not on a fixed schedule | Text-only (image posts 422 — adapter limitation, see `campaigns/2026-09-06-linkedin-blend-holes-night-gate/plan.md` known-limitation note) | **Live** — connected account `d20350bf-f728-4301-98c9-9632b4025761`, 2 posts published |
| Short-form video | Secondary — scene concepts only | Per campaign, generation gated | Concepts saved via `video_create_concept`, no jobs submitted yet (HeyGen 0/3 used as of last check) | **Approval-gated** — needs Vishal's explicit go-ahead before spending quota/money |
| Instagram / Facebook / Pinterest | Not applicable to this brand's plan currently | — | — | **Not connected** (`connect_status` checked 2026-09-24: all three `connected: false` for `rabbitlore`) |

## 6. Experiment backlog

Hypothesis -> evidence -> metric -> status. At most 2 running.

1. **LinkedIn build-in-public founder posts convert to real profile/brand credibility with a
   builder audience better than generic feature-announcement copy.**
   Evidence: `campaigns/2026-09-06-linkedin-blend-holes-night-gate/plan.md` (published) +
   `2026-09-06-reddit-curiosity-ranker-was-dead` (LinkedIn draft submitted same angle).
   Metric: post engagement via `get_post_analytics` (checked 2026-09-24: `collected: false`,
   not yet available).
   **Status: running.**

2. **Night-gated private lore-sharing, positioned as anti-virality (a closing window, not a
   share count), earns genuine non-promotional Reddit engagement from the overthinker/lonely-
   Gen-Z audience.**
   Evidence: repeated Top Opportunity across `research/2026-09-21.md` and `research/2026-09-24.md`;
   council-review confirmed (§7) as strongest positioning fit of 3 candidates.
   Metric: Reddit post actually posted + upvotes/comments once Vishal posts from
   `campaigns/2026-09-24-reddit-night-gated-lore-launch/`.
   **Status: proposed** (drafted, not yet live — Reddit is manual-only for this brand, so this
   is not "running" until Vishal posts it).

3. **Instrumenting NG-LS×UP from existing DB rows (no new SDK) will produce a usable baseline
   within one cron cycle.**
   Evidence: room/DM open events already logged per night-gate commit `391063f`; the gap is
   aggregation/reporting, not data collection.
   Metric: does a NG-LS×UP number exist in the next `analysis/<date>.md` snapshot.
   **Status: proposed** — not started, flagged here so it gets picked up, not lost.

## 7. We will NOT do

- **Build Yope-style AI "memory recap" or mini-game features to compete on friend-group photo/
  chat sharing.** Evidence: `research/2026-10-01.md` Competitive Edge — Yope's $12.3M-funded,
  15M-user product solves a different core loop (existing-friend-group photo albums) than
  RabbitLore's peer-to-peer lore matching (`getBlend`, `rabbithole 7c4e05a`); copying its features
  would blur RabbitLore's actual differentiator for a feature serving someone else's use case.
- **Chase the "faceless creator" / TikTok-3D-caricature / Picsart-Persona wave as a pillar.**
  Evidence: `research/2026-09-21.md` and `research/2026-09-24.md` Competitive Edge sections both
  explicitly conclude this gap is "not worth closing" — those tools sell external clout and mass
  visibility, which contradicts RabbitLore's stated positioning ("Not social media. Not
  algorithms. Not followers. Not virality." — `docs/positioning.md`).
- **Build a "Lore Map" spatial-mapping feature or "Identity Lore Tokens" matching mechanic as a
  near-term content pillar.** Evidence: both were one-off candidates named only in
  `research/2026-09-18.md`, never repeated in the two later snapshots — per the
  content-strategy 2+-snapshot rule, treated as unconfirmed signal, not a pattern
  (`campaigns/2026-09-24-reddit-night-gated-lore-launch/plan.md` already made this call once;
  strategy affirms it).
- **Compete with Highrise/ZEPETO on breadth of fashion customization.** Evidence: §2 positioning
  row 3 — that is their pole, not ours; positioning.md explicitly frames customization as
  internal record, not external performance. Chasing fashion-depth would blur the differentiator.
- **Attach vanity metrics (follower counts, virality framing) to any published copy.** Evidence:
  `docs/positioning.md` — "RabbitLore sells connection," not reach; contradicting that in copy
  undercuts the one differentiator no competitor can credibly claim.
- **Report or act on RabbitLore GA4 numbers.** Evidence: `analytics-map 2026-09-25` — RabbitLore
  Android streams in GA4 property 538401917 show zero data; report "no app analytics data," never
  invent a number.

## 8. Council review — north star + top pillars (2026-09-24, flagship tier)

`council_review` called once, tier=flagship, question covering: the no-baseline problem, the
repeated research signal, the anti-virality positioning, and the 3 watchlist competitors —
asking (1) what 90-day north star to set with no app analytics, and (2) the top 3 content
pillars defensible against named competitors.

**What responded:** Claude (opus-5) — 502 error, no answer. Gemini — timed out, no answer.
Mistral — 429 rate-limited, no answer. **Groq (openai/gpt-oss-120b) answered fully** — the only
model that returned a verdict this run.

**Verdict obtained (single model, not a consensus — reported honestly, same as the
2026-09-24 campaign's own council call which also got partial coverage):** north star =
Night-Gated Lore Sessions × Unique Participants, with Daily Night-Gated Active Users as the
interim proxy, both explicitly tied to data RabbitLore already logs in its own DB (no new SDK
needed) rather than a vanity install count. Top 3 pillars named: (1) intimate night-gated
storytelling, defended against Zentara's public/AI-amplified model; (2) narrative-driven avatar
co-creation ("story-tokens," avatars that evolve only when you share, never public), defended
against Highrise/ZEPETO's fashion-trophy model; (3) human-centric peer-to-peer lore matching via
the real `getBlend` overlap engine, defended against ZenFriend's simulated-bot-companion model.

**Where this matched the plain research read, no divergence:** the single model's answer landed
on exactly the same pillar set the research files + positioning doc already supported
independently — night-gating as the #1 pillar (matches 2 consecutive Top Opportunity calls),
avatar-as-record vs avatar-as-fashion (matches §2 row 3), and peer matching vs AI companion
(matches §2 rows 1-2). No second/third model opinion exists to compare against, so "where they
diverged" cannot be reported this run — only one verdict exists.

**My call:** adopted the model's north star framing and its 3 pillars as strategy §1/§4 above,
plus added a 4th pillar (build-in-public engineering honesty) that the model wasn't asked about
directly but that already has a real, published, confirmed-live result
(`campaigns/2026-09-06-linkedin-blend-holes-night-gate`) — the strongest evidence of any pillar
in this document, so it earned inclusion even though the council question didn't probe it.

## 9. Review log

- **2026-09-24 (this file created):** First strategy.md for RabbitLore, built from 3 research
  snapshots (`2026-09-18`, `2026-09-21`, `2026-09-24`), 3 analysis snapshots (all: GSC/GA4
  unavailable, RabbitLore not instrumented), `competitors/watchlist.md` (3 entries), 4 campaign
  plans (2 published LinkedIn, 3 Reddit drafts pending Vishal, 0 confirmed Reddit posts live),
  `docs/positioning.md`, and git log of both wired repos (`rabbithole-mobile`, `rabbithole`).
  North star set to NG-LS×UP (unknown baseline, flagged for instrumentation) per council review
  §8. 4 content pillars set, 2 experiments live/proposed, "faceless creator wave" and
  spatial-map/token mechanics explicitly rejected per §7 evidence.
- **2026-09-28:** Performance loop — LinkedIn post analytics still not collected (`get_post_analytics`
  500/`collected:false` on both existing posts, 2nd run in a row this happened), Reddit drafts
  still 0/3 live (`learnings/performance-log.md`). Research: first RabbitLore analysis snapshot
  with real pulled numbers (`analysis/2026-09-28.md`) — Google Trends "faceless creator app"
  went 0 (all year) → 14 → 12 (last two weeks), and real Reddit evidence surfaced current
  Highrise trust problems (minor-safety DM complaints, gambling-room backlash, account-hack
  reports) plus ZEPETO monetization friction (`research/2026-09-28.md`). Updated §2 Highrise/
  ZEPETO row with the new structural (non-attack) differentiator and §4 Pillar 1 with a scoped
  Reddit-copy guidance note; no pillar added or removed — evidence corroborates Pillar 1, doesn't
  create a new one. Zentara/ZenFriend: still zero Reddit/news footprint, unchanged.
- **2026-10-01:** Performance loop — LinkedIn post analytics still not collected, 3rd consecutive
  run (`learnings/performance-log.md`), now flagged as a pattern worth Vishal's manual check
  rather than continued automated re-checking. Research: corrected last run's "faceless creator
  app" trend read — the 2-week spike (14, 12) reverted to 0, so it's a decayed single-event
  signal, not a sustained rise; updated §4 Pillar 1 to stop citing it as "rising." Added **Yope**
  to `competitors/watchlist.md` and §2 positioning table — a new, well-funded ($12.3M Series A,
  ~15M users) private-social competitor that validates RabbitLore's "private beats public" macro-
  thesis at scale, though its actual product (friend-group photo/chat + AI memory recaps) is a
  different mechanic than RabbitLore's peer lore-matching; no pillar changed, no copycat feature
  added — see Competitive Edge in `research/2026-10-01.md` for the explicit "not worth chasing the
  feature, worth tracking the thesis-validation" call. Real regulatory news (California teen
  social-media law, Meta $17B settlement, EU/UK under-13 bans) reinforces the existing read that
  public-feed models face accelerating structural pressure RabbitLore's night-gated, no-public-
  room design sits outside of — same direction as the Apple Screen Time note from 2026-09-28, now
  with more corroborating jurisdictions, no action needed beyond noting it.
- **2026-10-10:** Performance loop — LinkedIn post analytics still not collected, 4th consecutive
  run (`learnings/performance-log.md`), repeating the standing flag for Vishal's manual check.
  Research: "private social app" and "close friends app" Google Trends readings both declined for
  2 consecutive weekly snapshots (56→28→7→5 and 70→38→18→16), down from a 100-peak in late
  May/early June 2026 — corrected §4 Pillar 1 to stop implying category interest is rising or
  accelerating; evidentiary weight stays on the 2 Top-Opportunity research calls, the shipped
  feature, and Yope's funding/regulatory validation. Added **Coverstar** to
  `competitors/watchlist.md` — a Gen Alpha (9-16) short-video app named alongside Yope/Lemon8 in
  dated news coverage of Australia's under-16 ban migration wave (which removed 4.7M accounts
  across 10 platforms, a new hard number); tracked but deliberately given no §2 differentiation
  row — see Competitive Edge in `research/2026-10-10.md` for the "different audience, different
  mechanic, not worth chasing" call. UK PM's 2026-06-15 under-16 ban announcement adds a second
  major jurisdiction to the regulatory-pressure read already in this log; no pillar change beyond
  noting it. Reddit searches (Yope, Highrise, lonely-gen-z, private-friend-group queries) returned
  zero on-topic results this run, same null pattern as recent prior runs.
- **2026-10-12:** Performance loop — LinkedIn post analytics still not collected, 5th consecutive
  run (`learnings/performance-log.md`), repeating the standing flag for Vishal's manual check.
  3 Reddit drafts now sit unposted (2026-09-24, 2026-10-01, 2026-10-10) with the 2026-10-10 draft
  intended to supersede 2026-10-01 — flagging that the backlog, not draft quality, is the open
  item. Research: new structural finding — Apple's App Store 13+ social-media declaration rule
  (effective Sept 2026) exempts DM/private-room-only apps from the 13+ floor while targeting
  public-feed/discovery-surface apps; added to §2 Highrise/ZEPETO row and §4 Pillar 1 as a second,
  independent structural reason behind the existing non-attack "no public room" positioning line —
  a real, checkable compliance fact, not a new claim about any specific competitor's compliance
  status. Watchlist: Coverstar's Google Trends search-interest shape changed from isolated one-day
  summer spikes to a sustained daily climb this week (22→33→28→34→36→45→69, Oct 6-12) — updated
  the watchlist entry, no change to the "track but don't chase" Competitive Edge call (still
  Gen Alpha audience, public-video mechanic, different from RabbitLore's). Highrise: new dated
  safety complaint (New Worlds open-mic rooms, no age-gating, predatory-targeting fear) added to
  watchlist, same underlying public-room-trust-cost pattern as 2026-09-28's findings, new specific
  instance. "Private social app"/"close friends app" trend decline flattened (not reversed) for
  one partial week — standing Pillar 1 correction (don't claim category acceleration) unchanged.
- **2026-10-15:** Performance loop — LinkedIn post analytics still not collected, 6th consecutive
  run (`learnings/performance-log.md`), repeating the standing flag for Vishal's manual check.
  Research: corrected 2026-10-12's partial-week Google Trends reads for "private social app" and
  "close friends app" — the now-closed week reads 5 and 21 (not the previously logged partial 3
  and 1), with "close friends app" moving up off the Oct 4-10 floor rather than continuing to
  decline. One closed week alone doesn't clear the 2-reading bar for a reversal call, so Pillar 1's
  standing correction (don't claim category acceleration) stays as-is, but the specific 2026-10-12
  numbers for that week are now superseded. Coverstar's Google Trends series set a new high (Oct
  15: 75) continuing the sustained-climb shape first flagged 2026-10-12; a new parent-safety
  article (virtual-addiction.com, Oct 5 2026) added to its watchlist entry. Yope's watchlist entry
  gained a context note (The Edge Malaysia "quiet social" roundup naming SetLog, Locket Widget,
  BeReal, MoodStream alongside it) — no new standalone competitor entries, no real metrics exist
  for the two previously-unlisted names. No pillar, positioning row, or "we will NOT do" item
  changed this run — a correction-and-maintenance week.
- **2026-10-19:** Performance loop — LinkedIn post analytics still not collected, 7th consecutive
  run (`learnings/performance-log.md`), repeating the standing flag for Vishal's manual check.
  Research: two new pieces of external validation for Pillar 1's macro-thesis, added to §4 — a
  "Posting Zero"/ghost-posting Gen Z behavioral trend corroborated across two dated articles 8
  months apart (Moneycontrol Jan 2026, Globe and Mail Sep 2026), and Meta's Night Mode (midnight-
  6am Instagram/Facebook teen curfew, part of an ~$18B multi-state settlement) — the first major
  platform structurally restricting after-midnight teen access, the same hours RabbitLore's
  night-gate already restricts. Correction: the Meta settlement figure is ~$18B per TechCrunch's
  own reporting, not the $17B logged in the 2026-10-01 entry above — that number is superseded,
  not repeated. Coverstar: full 90-day Trends re-pull shows the series' true all-time peak is 100
  (Sep 19, 2026, an isolated spike), with the daily floor since Oct 3 continuing to climb (Oct 17-
  19: 19→15→32) — updated the watchlist entry; no change to "track, don't chase." "Private social
  app"/"close friends app": the Oct 11-17 closed-week uptick did not continue into the Oct 18-24
  partial week (15 and 2 respectively) — partial-week numbers are not citable as a trend direction
  per the standing 2026-10-15 methodological rule, so no reversal or continuation claim is made.
  Reddit searches (RabbitLore, Yope, Highrise, private-social-genz queries) returned zero on-topic
  results again, same null pattern as every recent run. No pillar, positioning row, or "we will
  NOT do" item changed beyond the Pillar 1 evidence addition and the $17B->$18B correction.
- **2026-10-22:** Performance loop — LinkedIn post analytics still not collected, 8th consecutive
  run (`learnings/performance-log.md`), repeating the standing flag for Vishal's manual check.
  Research: added **Retro** to `competitors/watchlist.md` — a second independently-funded
  "anti-feed" competitor ($21M Series A, 7M downloads) alongside Yope, strengthening Pillar 1's
  macro-thesis evidence without introducing a new mechanic to chase (`research/2026-10-22.md`).
  Added a balancing nuance to Pillar 1 from MIDiA Research: the social-media market is
  bifurcating into entertainment-first vs. peer-to-peer, not converging on "private wins
  everywhere" — a caution against overclaiming, not a reversal. ZYMIX (UK superapp,
  consolidation-direction, flagged with a real Chinese-blacklisted-server security story)
  explicitly NOT added to the watchlist — wrong direction (consolidation, not privacy/atomization)
  and wrong audience (UK university students, payments-led). Coverstar's Google Trends re-pull
  showed a much larger pull-to-pull rescale than prior runs for the same calendar days — flagged
  as a data-quality caveat affecting comparability, not a real swing; the underlying "sustained
  non-zero floor" shape call stands unchanged. "Private social app"/"close friends app" closed-week
  readings matched last run's figures exactly (a consistency check); partial weeks still not
  citable. Reddit searches (RabbitLore, Yope, Highrise, private-social-genz queries) returned
  zero on-topic results again, same null pattern as every recent run. No pillar, positioning row,
  or "we will NOT do" item removed this run — one addition (Retro) and one nuance (MIDiA) to
  Pillar 1.
- **2026-10-26:** Performance loop — LinkedIn posts `urn:li:share:7502315073433104384` and
  `115d7a8b-523a-4f71-8995-064b780458cc` still unmeasurable (HTTP 500 / `collected:false`, 9th
  consecutive run); a new 3rd LinkedIn post `e3f4a2d2-fdc9-4a06-84dd-80948308398f` from the
  2026-10-22 cycle logged as `pending_approval`, not yet published. Reddit still
  `connected: false`, LinkedIn confirmed `connected: true`. Research: Posting2 — a Chicago-built,
  no-algorithm chronological-feed app — confirmed via two independently-dated sources (Fast
  Company, Afterschool Substack) growing from ~1,600 beta users to ~36,671-37,000 users (+42%
  MoM downloads in September), the first **unfunded** anti-feed macro-thesis proof point
  alongside funded Yope/Retro (`research/2026-10-26.md`). Added to watchlist. Retro's figures
  refined with a new MAU number (1.7M, via Mintz). **Data-gathering gap this run:** the
  `composio_search` toolkit (Google Trends, Composio news/web) returned a session-level
  `ToolkitDisabled` restriction for every call attempted — substituted general web_search for the
  news/web step, but no substitute exists for the Google Trends time-series specifically, so
  "private social app"/"close friends app"/"Coverstar app" trend readings have a genuine gap this
  week (not a null reading — flagged for next run to escalate to Vishal if still blocked).
  Zentara/ZenFriend news searches confirmed zero on-topic results again via a different tool, same
  null pattern since 2026-09-18. No pillar, positioning row, or "we will NOT do" item removed this
  run — one watchlist addition (Posting2) and one evidentiary strengthening (Retro MAU) to
  Pillar 1.
- **2026-10-29:** Performance loop — LinkedIn posts `urn:li:share:7502315073433104384` and
  `115d7a8b-523a-4f71-8995-064b780458cc` still unmeasurable (HTTP 500 / `collected:false`, 10th
  consecutive run); third LinkedIn post `e3f4a2d2-fdc9-4a06-84dd-80948308398f` still
  `pending_approval`, unchanged. Research: Posting2's growth story cleared a 3-independent-source
  bar — a 3rd editorial source (YPulse, Oct 27) and a 4th, non-editorial data source (MWM app
  intelligence) independently corroborated the organic-growth figures first logged 2026-10-26,
  the strongest multi-source-confirmed proof point in this research line to date. Added to §4
  Pillar 1 and the watchlist entry. Zentara's "no traction" read gained a hard number (Tracxn:
  914th/1,348, Score 16/100) via re-confirmation, same call, stronger evidence — added to §2.
  ZenFriend's row gained a category-level citation (Guardian "intimacy economy" essay, a sharper
  first-person account of AI-chatbot-over-human-friend behavior) — not a ZenFriend-specific
  update, flagged as such. **Data-gathering escalation:** `composio_search` (Google Trends,
  Composio news/web) returned the identical `ToolkitDisabled` restriction for a 2nd consecutive
  run (2026-10-26, 2026-10-29) — per the 2026-10-26 run's own standing instruction, this is now
  escalated to Vishal in this run's Telegram report rather than substituted a third time. No
  pillar, positioning row, or "we will NOT do" item removed this run — one Pillar 1 evidence
  strengthening, two §2 refinements (Zentara, ZenFriend), zero watchlist additions/removals.
- **2026-10-29 (campaign cycle):** council_review (flagship) run on 3 candidates — Posting2's
  4-source Pillar 1 proof point, the Guardian intimacy-economy essay (Pillar 3 category
  evidence), and the 5-deep/0-posted Reddit backlog. Claude and Groq converged (Gemini/Mistral
  429): don't draft a 6th Reddit post into a dead channel, put the strongest new evidence
  (Posting2) on LinkedIn instead, escalate the backlog to Vishal explicitly. Drafted LinkedIn
  post `9dc116d5-32b3-4347-b4cd-c3fac9ec57c0` (F19 Anecdote-Meets-Evidence Bridge, Posting2
  4-source citation), submitted for approval. Wrote a Reddit triage memo (not a new post) naming
  all 5 unposted drafts and asking Vishal to post one. Full writeup:
  `campaigns/2026-10-29-linkedin-posting2-validation-reddit-triage/plan.md`.

## 10. Strategy delta (2026-10-22)

1. Pillar 1 gained a second funded "anti-feed" competitor (Retro, $21M Series A / 7M downloads)
   alongside Yope — same macro-thesis validation, no new mechanic to chase — plus a balancing
   nuance (MIDiA: market bifurcating entertainment-first vs. peer-to-peer, not one-way private
   dominance) that future copy should respect, not overclaim past.
2. New watchlist entry: Retro (tracked, not chased). ZYMIX considered and explicitly rejected as
   a watchlist addition — wrong direction, wrong audience.
3. Executors this week: campaign-workflow can cite Retro's download-growth/subscription figures
   as a stronger, more concrete "people pay for anti-feed" line than a bare funding-round mention
   for the next Reddit devlog angle; LinkedIn/Reddit cadence otherwise unchanged, and the 8-run
   LinkedIn analytics gap still needs Vishal's manual check outside this loop.

## 11. Campaign: 2026-10-22-reddit-retro-anti-feed-validation

council_review (flagship) run on 3 candidates (Reddit/Retro devlog, LinkedIn backlog-
transparency, MIDiA-bifurcation piece) — only Groq answered (Claude 502, Gemini timeout, Mistral
429). Groq recommended LinkedIn backlog-transparency as primary effort, notably flipping its own
2026-10-15 position (then: keep adding Reddit supply; now: stop until the channel ships
something) given the backlog went from 3 to 4 unposted drafts with zero movement. My call: wrote
both — Reddit/Retro devlog (research's own Top Opportunity, genuinely new evidence) and the
LinkedIn transparency post (Groq's pick, serves Pillar 4) — since the Retro evidence itself is
strong regardless of channel health, while still honoring Groq's core point by leading the
Telegram/plan with the backlog, not the new draft. LinkedIn post `e3f4a2d2-fdc9-4a06-84dd-
80948308398f` drafted and submitted for approval. Reddit backlog now 5 deep
(2026-09-24, 2026-10-01, 2026-10-10, 2026-10-15, 2026-10-22), still 0 posted — this is now the
dominant open risk to Pillar 1's Reddit-channel KPI and needs Vishal's direct action, not more
research cycles.

## 12. Strategy delta (2026-10-26)

1. Pillar 1 gained a third "anti-feed" proof point (Posting2, ~37,000 users, +42% MoM downloads,
   $0 raised) — the first unfunded instance alongside Yope ($12.3M) and Retro ($21M), plus a
   citable early-user complaint about strangers commenting as the app scales, usable as a
   concrete argument for RabbitLore's own structural caps. Retro's figures refined with a new
   MAU number (1.7M).
2. New watchlist entry: Posting2 (tracked, not chased — same treatment as Yope/Retro). No
   competitor removed or demoted this run.
3. Executors this week: campaign-workflow should prioritize the still-unposted Reddit backlog
   (now 5+ drafts, 0 live) over drafting new LinkedIn content — Posting2's organic-growth angle
   is strong material for the *next* Reddit post once the backlog moves, not a reason to add a
   6th draft to a stalled channel. The `composio_search` outage means next run must either
   confirm the toolkit is restored or escalate to Vishal — do not silently keep substituting
   web_search for Trends data for a third run in a row without flagging it again.

## 13. Strategy delta (2026-10-29)

1. Pillar 1's Posting2 proof point is now corroborated by 4 independent sources (Fast Company,
   Afterschool Substack, YPulse, MWM app intelligence) within 3 days of first discovery — the
   strongest multi-source evidence of any proof point tracked so far, and the recommended anchor
   citation for the next Reddit devlog post over Yope's/Retro's funding-round mentions.
2. No watchlist competitor added or removed. Two existing entries (Zentara, ZenFriend)
   strengthened with harder evidence (a numeric unfunded-rank for Zentara; a sharper first-person
   category citation for ZenFriend's AI-companion thesis), not new names.
3. Executors this week: campaign-workflow should lead the next Reddit post with Posting2's
   4-source-corroborated organic growth, not Retro's or Yope's raise amounts — it's the stronger,
   more skeptic-proof citation. Separately: the composio_search/Google Trends outage is now a
   confirmed 2-run block — flag to Vishal directly, this needs his attention on the Composio
   account/session config, not another research-cron workaround. The 5-deep, 0-live Reddit
   backlog remains the dominant open risk to Pillar 1's Reddit KPI, unchanged from last run.

## 14. Campaign: 2026-10-29-linkedin-posting2-validation-reddit-triage

council_review (flagship) run on 3 candidates (Posting2's 4-source Pillar 1 proof point, the
Guardian intimacy-economy essay for Pillar 3, and the 5-deep/0-posted Reddit backlog as a
process issue). Claude and Groq both answered this run and converged, not diverged: don't draft
a 6th Reddit post into a channel that has shipped zero of five, redirect this week's strongest
evidence (Posting2) to LinkedIn where it's actually live, and escalate the backlog to Vishal by
name rather than quietly carrying it forward again. My call followed the converged verdict
exactly. LinkedIn post `9dc116d5-32b3-4347-b4cd-c3fac9ec57c0` (F19 Anecdote-Meets-Evidence
Bridge, citing Posting2/Yope/Retro's three different funding levels landing on the same
structural bet) drafted and submitted for approval. No new Reddit draft written — instead wrote
a triage memo naming all 5 unposted drafts plainly and asking Vishal to post one this week. The
Guardian essay (Pillar 3 evidence) held back for a dedicated piece later, per Claude's reasoning
that it isn't time-decaying the way Posting2's days-old 4-source confirmation is.


