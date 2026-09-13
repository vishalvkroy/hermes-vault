# Reddit draft (primary channel)

**Status:** draft only. No connected Reddit account for RabbitLore in hermes-social. Vishal posts
this by hand after picking subreddit(s) and checking current self-promo rules there.

**Suggested subreddits (Vishal to confirm current rules/mod mood before posting):**
- r/webdev or r/programming (postmortem/root-cause story, low promo risk, framed as an
  engineering lesson not an app pitch)
- r/SideProject (if framed with a line or two of context on what RabbitLore is)
- Skip general Gen Z / social-app subs for this one — it's a technical postmortem, not a feature
  story, wrong fit for those audiences.

Post once, in one sub first. Watch response before considering a second sub. Do not cross-post
the same text.

---

## Title
Our recommendation feed was silently broken for months. The bug was a single hardcoded number.

## Body

I work on RabbitLore, an app where people post short personal stories and get a personalized
"For You" feed based on what they engage with.

Found something embarrassing last week: our personalization had been quietly turned off for a
while, and nothing ever errored or alerted on it.

Here's what happened. The feed ranks content using a "curiosity vector" built from a fixed list
of categories. Early on there were 21 categories, so the code checked `vector.length === 21`
before trusting the personalized ranking — a totally reasonable sanity check at the time. Then we
added more categories over a few releases, the list grew to 29, and nobody touched that check.

29 does not equal 21. So the check just... never passed. Ever. From that point on, every "For
You" feed silently fell back to plain popularity ranking. No crash, no error log, no alert —
personalization just quietly stopped happening. The code computing the vector still ran fine
every time, it just never got used.

The fix itself is boring: check against the actual length of the category list instead of a
hardcoded 21, so it can't drift again. The more interesting part was making it self-healing —
if a user's stored profile is a stale dimension (built under an older, shorter category list),
we now detect that and queue a rebuild automatically instead of quietly falling back again.

The part that stuck with me: this is exactly the kind of bug that doesn't page anyone. It's not
downtime, nothing throws, no metric obviously craters. It's just a feature slowly doing nothing,
correctly, for as long as no one happens to look at the actual numbers going into the check.

Anyone else have a bug like this? A silent no-op that only survives because it fails gracefully
into "fine, but worse" instead of failing loudly?

(Happy to talk through the fix or the app if anyone's curious — not trying to sell anything here,
just sharing a bug that taught me something about how quietly personalization can rot.)
