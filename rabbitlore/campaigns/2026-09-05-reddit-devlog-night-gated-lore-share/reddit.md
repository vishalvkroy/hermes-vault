# Reddit draft (primary channel)

**Status:** draft only. No connected Reddit account for RabbitLore in hermes-social. Vishal posts
this by hand after picking subreddit(s) and checking current self-promo rules there.

**Suggested subreddits (Vishal to confirm current rules/mod mood before posting):**
- r/SideProject (self-promo generally tolerated if framed as a build story, not an ad)
- r/AppIdeas or r/androidapps (only if the specific sub currently allows dev posts about live apps)
- Avoid general Gen Z / social-app subs for this post, too promo-shaped for those. This fits better
  as a "here's a decision we made and why" build-in-public post.

Post once, in one sub first. Watch response before considering a second sub. Do not cross-post the
same text.

---

## Title
We made our app's "share a story" feature only work between 11pm and 4am. Here's why that actually worked.

## Body

I build RabbitLore, an app where people post short personal stories ("lore") and build an avatar
that reflects their profile.

A few weeks ago we added lore-sharing inside DMs and group rooms: you can send someone a story
you've already posted, not just link it, but drop it into the chat as its own card. Straightforward
feature. Then we gated it to only work between 11pm and 4am IST.

The reasoning wasn't mystical. Most of the raw, unfiltered stories on the app get posted late at
night anyway, so we were curious whether restricting the sharing window to match would push people
toward sharing the heavier stuff instead of the safe daytime posts. It did, more than we expected.
Share volume in that window is a small fraction of total DMs sent, but the stories getting shared
are noticeably more personal than what gets shared in the rest of the day.

The tradeoff: a decent chunk of users open the feature at 2pm, hit a locked screen, and leave
confused. We're still deciding whether to add a "why is this locked" tooltip or just accept the
friction as part of the feature's identity.

Curious if anyone else has shipped an intentionally-restricted feature like this. Did it hold up
after the novelty wore off, or did people just route around it?

(Happy to answer questions about the app or the decision. Not trying to sell anything here, just
sharing a weird design choice that worked better than the boring version.)
