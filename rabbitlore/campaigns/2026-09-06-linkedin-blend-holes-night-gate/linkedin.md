# LinkedIn draft (RabbitLore) - published

**Status:** published. post_id `115d7a8b-523a-4f71-8995-064b780458cc`, provider_post_id
`urn:li:share:7502315073433104384`, published_at 2026-09-06T10:41:40Z.
https://www.linkedin.com/feed/update/urn:li:share:7502315073433104384/

Image generation and a first draft attempt with media_urls set both worked, but `publish()` on
the image draft failed: 422, "LinkedIn image posts are not implemented yet (needs the separate
Images API upload flow)". Re-drafted text-only (same copy) and published that instead. See
plan.md for full detail.

**Grounding:** git log, rabbithole-mobile and rabbithole (backend) repos.
- `391063f lore-share: night-gated (11pm-4am IST) in rooms + DMs`
- `c12fba4 blend canvas: gravitational collision driven by match % (not just 80+)`
- `93a7d75 blend: emotional redesign - story of two minds, not a stats dashboard`
- `e02977b holes: fix count flicker + tap-to-see-who-fell-in + realtime feel`
- backend `7c4e05a blend: getBlend returns real 'collisions' (overlapping lores by category+tag)`
- backend `9c66801 holes: add getLikers - who fell into a hole (cap 100, public)`

Builds on the existing 2026-09-05 campaign's night-gate framing, adds the blend/holes mechanic
that campaign only referenced in its research note, not in a drafted post.

## Draft copy

We shipped a feature this month that only works for five hours a day, on purpose.

RabbitLore is a social app where people post short personal stories, "lore," and build an avatar
around them. This month we shipped two things worth explaining.

First: lore-sharing inside DMs and group rooms only works from 11pm to 4am IST. Most of the raw,
unfiltered posts on the app already happen late at night, so we gated the sharing feature to that
window on purpose, to see if it would push people toward sharing the heavier stuff instead of
daytime filler. Early read: share volume in that window is a small slice of total messages, but
what gets shared there is noticeably more personal. The cost is real: users who open the feature
at 2pm hit a locked screen with no explanation, and some leave.

Second: we rebuilt "blend," the feature that shows two users' compatibility, as a gravitational
collision canvas instead of a percentage score. The backend now computes real collisions,
overlapping lore by category and tag, not a single match number. When two people's lore overlaps
enough, it opens a "hole," and tapping it shows who fell in (public, capped at 100 people).

Both changes came from the same question: does restricting or reframing a feature change what
people actually do, or does it just add friction? For the night gate, the restriction seems to be
working. For blend, we don't have enough data yet to say the same.

Curious how other builders think about intentional friction like this: a feature that works
better because it doesn't work all the time.

## Image

Generated via Pollinations (hermes-video generate_image), placeholder tier: abstract dark
midnight-blue/purple illustration of two glowing orbs colliding into stardust, evoking the
blend/collision mechanic without literal UI screenshot.
