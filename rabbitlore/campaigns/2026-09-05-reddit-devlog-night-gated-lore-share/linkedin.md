# LinkedIn draft (secondary channel — connected account, submitted for approval)

**Status:** submitted. `list_accounts("rabbitlore")` returned the connected LinkedIn account
(Vishal Kumar, social_account_id `d20350bf-f728-4301-98c9-9632b4025761`). `create_draft(...)` was
called with the copy below — post id `6b4fe486-9261-451c-bb6f-6ee8749de18e`, status
`pending_approval`. `request_publish_approval(post_id)` was then called, which pings Vishal on
Telegram. Nothing publishes until Vishal clicks Approve — check `get_post(post_id)` for current
status before reporting this as posted.

LinkedIn skews toward founder/builder audience rather than Gen Z end users, so this is a smaller,
more technical version of the same story, framed as a product-decision post rather than the
conversational Reddit voice.

## Draft copy

We shipped a feature this month that only works for five hours a day, on purpose.

RabbitLore lets people share personal stories ("lore") they've posted with friends in DMs or group
chats. We gated that specific feature to 11pm-4am IST only.

The idea came from a pattern we'd already seen: most of the unfiltered, personal posts on the app
happen late at night. We wanted to know if narrowing the sharing window to match would change what
people actually chose to share, or if it would just annoy them.

Early read: share volume in that window is a small share of total messages, but what gets shared
there is noticeably more personal than the daytime average. The cost is real too, users who try the
feature at 2pm hit a locked screen with no explanation yet, and some just leave.

Small feature, real product tradeoff: does a time-gated feature need to explain itself, or does the
restriction lose value the moment you explain it?
