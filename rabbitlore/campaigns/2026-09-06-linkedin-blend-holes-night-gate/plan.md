# Campaign: 2026-09-06-linkedin-blend-holes-night-gate

- **Campaign ID:** 2026-09-06-linkedin-blend-holes-night-gate
- **Timestamp:** 2026-09-06T10:41:40Z
- **Status:** published
- **Grounding:** Real shipped features pulled from git log, no research doc yet for RabbitLore
  (research cron hasn't run for this brand - same gap noted in the 2026-09-05 campaign).
  - `rabbithole-mobile 391063f` lore-share: night-gated (11pm-4am IST) in rooms + DMs
  - `rabbithole-mobile c12fba4` blend canvas: gravitational collision driven by match %
  - `rabbithole-mobile 93a7d75` blend: emotional redesign, story of two minds not a stats dashboard
  - `rabbithole-mobile e02977b` holes: fix count flicker + tap-to-see-who-fell-in + realtime feel
  - `rabbithole 7c4e05a` blend: getBlend returns real collisions (overlapping lores by category+tag)
  - `rabbithole 9c66801` holes: add getLikers, who fell into a hole (cap 100, public)
- **Objective:** Founder-led LinkedIn post explaining two real, shipped, unusual product decisions
  (time-gated sharing, collision-based compatibility) to a builder/founder audience.
- **Hypothesis:** Specific product-decision detail (why a feature is restricted on purpose, what
  the tradeoff cost was) reads as more credible to a LinkedIn founder audience than generic
  feature-announcement copy.
- **Target audience:** Founders/builders on LinkedIn, RabbitLore's secondary channel (Reddit is
  primary for this brand per spec section 12).
- **Which research finding it's responding to:** None yet available (research cron hasn't run) -
  responding to brand identity + real shipped-feature signal from git log, per campaign-workflow's
  fallback rule.
- **Channels used:** LinkedIn only (this campaign). Builds on the 2026-09-05 campaign's night-gate
  framing and adds the blend/holes mechanic, which that campaign only referenced in its grounding
  note, never drafted as its own post.
- **Publishing plan / what happened:** LinkedIn is a connected, live channel for RabbitLore.
  `list_accounts` returned social_account_id `d20350bf-f728-4301-98c9-9632b4025761`. Generated a
  placeholder image via `generate_image` (Pollinations) and first attempted `create_draft` with
  `media_urls` set - `publish()` failed with a 422: "LinkedIn image posts are not implemented yet
  (needs the separate Images API upload flow) - this draft has media_urls set; strip them or wait
  for that adapter update." Created a second draft, text-only, same copy, no media_urls
  (`115d7a8b-523a-4f71-8995-064b780458cc`), status `approved` (auto-publish policy). Called
  `publish()` again: succeeded. `status: published`, `provider_post_id:
  urn:li:share:7502315073433104384`, `published_at: 2026-09-06T10:41:40Z`.
- **URLs:** https://www.linkedin.com/feed/update/urn:li:share:7502315073433104384/
- **Metrics:** pending.
- **Outcome:** pending.

## Known adapter limitation (report to Vishal / future cycles)

hermes-social's LinkedIn adapter cannot publish image posts yet - it needs a separate LinkedIn
Images API upload flow, not just a media_urls field on the post. Every future LinkedIn draft with
an image attached will hit the same 422 until that adapter is built. Text-only LinkedIn posts work
fine. The generated image for this post is saved in linkedin.md but was not usable.
