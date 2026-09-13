# LinkedIn draft (secondary channel — connected account, submitted for approval)

LinkedIn skews toward a founder/builder audience, not Gen Z end users — same underlying story as
the Reddit post, told in a shorter, more product-decision framing rather than the conversational
Reddit voice.

## Draft copy

Found a bug last week that had been quietly making our product worse for months, without a
single error or alert to show for it.

RabbitLore ranks each user's feed with a personalization vector built from a fixed category list.
When we launched, that list had 21 categories, so the ranking code checked
`vector.length === 21` before trusting it. Reasonable check, at the time.

Then the category list grew, release by release, to 29. Nobody updated the check. 29 never equals
21, so the check silently failed on every single request going forward — every "For You" feed
quietly fell back to plain popularity ranking. No crash. No spike in errors. Personalization was
computed correctly and then just never used.

Fixed the immediate bug (check the real list length, not a hardcoded number), then went one step
further: the system now detects a mismatched profile automatically and queues a rebuild, so the
same class of bug can't silently reoccur even if a future change forgets to bump a version number.

The lesson that's stuck with me: this is the kind of bug that doesn't page anyone. Nothing fails
loudly. It just fails into "fine, but quietly worse" — and that's much easier to ship by accident
and much harder to notice than an outage.

## Status

`list_accounts("rabbitlore")` returned the connected LinkedIn account (Vishal Kumar,
social_account_id `d20350bf-f728-4301-98c9-9632b4025761`). `create_draft(...)` was called with
the copy above — post id `2c7919ee-da2a-4936-984d-35bb4b8a05a9`, status `pending_approval`.
`request_publish_approval(post_id)` was then called, which pinged Vishal on Telegram. Nothing
publishes until Vishal clicks Approve — check `get_post(post_id)` for current status before
reporting this as posted.
