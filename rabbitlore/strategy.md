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

Every watchlist competitor (`competitors/watchlist.md`, 3 entries as of 2026-09-24), one row
each. Claims checked against `docs/positioning.md` and real shipped commits — nothing here is
aspirational.

| Competitor | Their claim | Our real proof | Our edge | Message we lead with |
|---|---|---|---|---|
| **Zentara** | AI-powered avatars/VTubers for virtual companions, cross-platform connectivity, creator monetization — a public, commercial creator platform (`research/2026-09-18.md` [21]) | Night-gate (11pm-4am IST) locks lore-sharing in rooms+DMs (`rabbithole-mobile 391063f`); `getBlend` matches by real overlapping lore category+tag between two actual users, not an AI companion (`rabbithole 7c4e05a`) | Zentara sells visibility and monetized creator personas; RabbitLore sells private, human-to-human recognition with no follower count attached | "No AI companion pretending to care. Two real people whose lore actually overlaps." |
| **ZenFriend** | AI virtual friend targeting Gen Z loneliness/anxiety — a simulated bot relationship (`research/2026-09-18.md` [11]) | `getBlend` collision is peer-to-peer (real user-to-user tag/category overlap, `rabbithole 7c4e05a`); "holes" mechanic (`getLikers`, `rabbithole 9c66801`) shows who — a real person — fell into your lore, capped at 100, public | ZenFriend's "friend" is a simulation; ours is a stranger who turns out to think the same weird thoughts you do — the actual emotional payoff positioning.md names ("I thought I was the only one") | "Not a bot pretending to understand. A real person who already gets it." |
| **Highrise / ZEPETO** | Deep avatar customization, fashion-forward, K-style/streetwear aesthetic, public social integration — aspirational look-and-be-seen (`research/2026-09-18.md` [27], `research/2026-09-21.md` [5]) | Constellation star-map turns *logged lore* (not outfits) into the visible artifact — deterministic, append-stable layout, one star per lore entry (`rabbithole-mobile bd3b252`, `1513283`); avatar customization here pairs with content, not clout | Highrise/ZEPETO customization is external performance (what you look like to strangers); RabbitLore customization is internal record (what you've actually carried inside you) | "Your avatar isn't a fit check. It's a map of what's in your head." |

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
  applied); shipped in `rabbithole-mobile 391063f`.
- **Channel/format:** Reddit (primary — genuine contribution posts, not ads), short-form video
  concept (secondary, gated on Vishal's go-ahead before any generation spend).
  Council-review flagged (see §6) as the strongest anti-virality proof point: scarcity via a
  closing time window, not share counts.
- **KPI:** Reddit posts actually posted by Vishal (currently 0/3 drafted); once instrumented,
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
