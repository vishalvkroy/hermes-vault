# Reddit draft (final, humanized)

**Target subreddit type:** r/technology, r/privacy, r/socialmedia, or r/OutOfTheLoop — this is a
policy/industry-trend discussion post, not a lore/overthinker personal-story post like the
2026-09-24 draft. Vishal should pick the specific subreddit, check its self-promo rules, and post
from a personal account with real history, not a brand account. A policy-news subreddit is a
better fit for this angle than r/GenZ or r/overthinkers — those suit the personal-story register,
this suits a "did anyone else notice this pattern" register.

**Suggested title:** The last six months quietly turned "public feed app for teenagers" into a
legal and PR liability. Is anyone else tracking this?

**Post body:**

I've been half-following social media regulation news for a side project and the pile-up this
year is bigger than I expected once I actually listed it out:

- California passed a law in September banning "addictive" social media features for minors.
- Meta settled with a group of states for $17 billion over teen safety in August, with new limits
  on how feeds can target teens.
- The EU is moving toward banning under-13s from social platforms entirely.
- The UK passed its own teen social media restrictions back in June.
- And this one's easy to miss: Apple now makes developers declare whether an app has "social
  media capabilities" (a public feed, algorithmic content discovery), and if you say yes, the app
  gets pulled into parental Screen Time limits automatically, regardless of what category you're
  listed under in the App Store.

None of these are proposals anymore. They're all live or already settled. And they're all aimed
at the same mechanic: a public feed, algorithmically surfacing content from strangers, to an
audience that includes minors.

What's interesting to me is how structural the fix requirement is. You can't really patch your
way out of "has a public feed" with a content moderation team. Either the feed exists or it
doesn't.

I bring this up because I've been building something (RabbitLore, an app for sharing the weird
private stuff you usually only tell strangers online at 2am) and we made a call early on, mostly
for product reasons, to not have a public feed or public rooms at all. Everything's private,
peer-to-peer, no stranger can land in your space uninvited. At the time that felt like we were
giving up the easy growth lever every other app uses. Looking at this regulatory stack now, it
looks less like we gave something up and more like we just never built the thing that's currently
getting legislated against.

Not trying to sell anyone here, genuinely asking: is this actually going to force a real design
shift across the industry, or will most apps just add an age gate and keep the public feed
underneath it? Feels like the age-gate approach doesn't actually solve what the laws are
targeting.

---

## Notes for Vishal
- Framing check: no competitor named anywhere in the draft. The regulatory facts stand on their
  own (CA law, Meta settlement, EU/UK bans, Apple Screen Time change) — RabbitLore's design choice
  is mentioned once, as a structural fact about what was built and why, not as a comparison or
  callout. This matches the rule from `research/2026-09-28.md` Competitive Edge: the "no public
  room" point is available as positioning, never as an attack.
- Post reads as genuine industry-trend discussion first, product mention second — the kind of
  thing that stands up even with the product paragraph deleted. That's the point: if it only works
  with the pitch in it, it's not a real contribution.
- Pick ONE subreddit, read its self-promo/no-ads rule first. A policy-discussion subreddit
  (r/technology, r/privacy) may have stricter "no self-promo at all" rules than a personal-story
  sub — check before posting, this may need the product paragraph trimmed further or moved to a
  comment reply if someone asks "wait what app" rather than sitting in the original post.
  Vishal's call on the day, based on the specific subreddit's actual rule text.
  - Do not post this and the still-unposted 2026-09-24 draft in the same subreddit or week — reads
    as a pattern once someone checks post history.
- All five regulatory facts and the Apple Screen Time change are dated, sourced items from
  `research/2026-09-28.md` and `research/2026-10-01.md` (sources [1]-[6] in the 09-28 file) — the
  copy was checked against those exact dates, nothing here is invented.

## Humanizer pass notes
Removed: no em/en dashes found in the draft (checked). Replaced an early "showcasing a structural
advantage" type line with a plain statement of what happened. Kept the bulleted regulatory list —
these are five distinct real facts, not a padded AI triad, so the list stays as a list rather than
being forced into prose. Kept the first-person, slightly uncertain voice ("What's interesting to
me," "is anyone else tracking this") to match the brand's established personal-post register from
the prior Reddit draft, rather than switching to corporate voice. No invented facts, dates, or
figures beyond what the research files cite.
