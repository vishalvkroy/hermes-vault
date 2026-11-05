# MadeByHer Deep Research — 2026-11-05

## TOP OPPORTUNITY: Chhath thekua posts still unpublished, now 8 days out and the status tool itself just broke

Same unblocking action flagged on 2026-11-02, now more urgent and with a new wrinkle. The Chhath
thekua campaign (`2026-10-29-chhath-thekua-festival-push`, Pinterest post `ef2f0140` + Instagram
carousel `a095cd49`) has sat in `pending_approval` for 7 days — `get_campaign_performance` confirms
`posts_published: 0` of 2. This run, `get_post` on both post ids returned a 500 Internal Server
Error instead of the clean `pending_approval` status seen on 2026-11-02 — the status-check tool
itself has regressed on top of the pre-existing approval block. Chhath Puja 2026 runs 13-16
November (main day 15 Nov), confirmed again this run via Divine Hindu's festival guide.[8] 8 days
out, and the posts' own copy says thekua "needs a few days to ship and settle before puja" — this
is now critically late. This needs Vishal's approval decision today, not another check next run.

Underlying demand signal is unchanged and still real: `/product/sudh-desi-ghee-thekua` sits at 3
clicks / 558 impressions (28d GSC), essentially flat vs 2026-11-02's 3/552 — the organic click
movement seen two runs ago has plateaued. Exp 9 (on-page title/meta rewrite) and Exp 10 (scoped
Chhath discount test) remain unshipped after 5+ consecutive runs flagged — see Competitive Edge.

## SEARCH INTENT (GSC + GA4, this run)

GSC (`sc-domain:madebyher.in`, 28-day window, verified via `gsc_list_sites`):

- Branded search still dominant and healthy: "madebyher" 118 clicks/159 impr (CTR 74.2%, pos 1.45),
  "made by her" 58/139 (CTR 41.7%, pos 3.50).
- **`/blog/bawan-buti-saree-a-buying-guide-to-bihar-s-52-motif-weave` confirmed a real, continuing
  winner, not a one-week spike**: 16 clicks / 583 impressions (28d), CTR 2.74%, up from 13/505 on
  2026-11-02 — second consecutive run of real growth. "52 buti saree" (3 clicks/280 impr) and
  "52 buti saree nalanda" (3/49) both converting.
- `/product/sudh-desi-ghee-thekua`: 3 clicks / 558 impressions (28d), pos ~7.5 — flat vs last run's
  3/552 (+1.1% impressions, clicks unchanged). See Top Opportunity.
- `/sell` (seller signup): 23 clicks / 280 impressions, pos 4.03 — still the strongest acquisition
  page on the site after the homepage, consistent with every prior run.
- Persistent high-impression/low-CTR pages unchanged in character from prior runs: `/shop` (5
  clicks/509 impr, 0.98% CTR), `/blog/patharkatti-stone-craft...` (5/569, 0.88%) — title/meta work
  still the right fix, not more volume.
- "best papad brands in india" / "papad brands" still appearing (1 click/20 impr, 1/18) —
  `admin_search_products(q="papad")` still returns zero live products; same for "makhana" — both
  sourcing gaps (Exp 7, Exp 11) unchanged, now 8+ consecutive runs unresolved.

GA4 (property `553055822`): both `sessionDefaultChannelGroup` and `pagePath` dimensions at 28 days
returned zero data rows this run — no error thrown, just an empty result. This is a regression from
2026-11-02 (which at least returned a degenerate single "Direct: 16/14" row). No GA4 channel/traffic
number is cited this run; GSC remains the only reliable search/traffic read, consistent with the
performance-log's running note that this property's channel-group reporting has been unreliable
across most of the last month.

## TRENDING IN THE NICHE

**Reddit** (Composio `REDDIT_SEARCH_ACROSS_SUBREDDITS`, across r/bihar, r/india, r/smallbusiness,
r/smallbusinessindia, r/crochet, r/Etsy, time_filter=month): no new Bihar-handmade-gifting-specific
signal this run. Threads found were general Chhath-travel-home sentiment — tickets scarce, people
anxious to get home[4], a Chhath-themed painting post[2] — rather than gifting/buying behavior, and
a handmade-candle seller still struggling to convert reel views to sales[3] mirrors a pattern
already logged, not a new finding; r/crochet/r/Etsy carried only generic crochet-project/feedback
posts with no India/Bihar angle. Logged as a genuine "nothing new" week for this channel rather than
manufacturing a weak finding.

**Composio Google Trends**: unavailable again this run — `COMPOSIO_SEARCH_TRENDS` returned
`[Session Restriction] Toolkit 'composio_search' is disabled for this session`. This is the fourth
consecutive run with this restriction (2026-10-29, 11-02, and now 11-05). Flagging as a persistent
tool gap, not a finding — no trend-direction number claimed from this source again this run.

**Instagram competitor research**: explicitly skipped per standing instruction — MadeByHer's own
Composio Instagram connection can only read our own account's posts/tags, not public hashtag or
competitor search.

## NEWS AND ARTICLES

Composio search toolkit being session-restricted (above), news/web coverage came from web_search
(partially rate-limited mid-run on one backend, picked up by an alternate backend for the rest) and
web_extract:

- A Rukam Capital-YouGov survey of 4,002 respondents aged 18-29 across 18 states (reported by The
  Economic Times) gives real behavioral numbers directly relevant to MadeByHer's audience segments:
  60% spent more during festivals this year, 74% buy gifts for parents/family, ~30% self-gift, 1 in
  4 used AI chatbots for gift ideas, 41% used online search to find gifts. A Rukam Capital partner is
  quoted naming "regional specialities and fusion mithai" and "homegrown brands" specifically as the
  categories gaining interest among this cohort — a national-scale number corroborating the
  Bihar-regional-sweet demand pattern already tracked via GSC and the thekua-competitor cluster.[1]
- Patna Press reports Bhagalpur's Manjusha-art Chhath "soops" (decorated bamboo winnowing trays used
  in the puja ritual) have real orders — 100-200 pieces — including demand from the US diaspora this
  season.[7] This extends the diaspora-ships-Bihar-craft-for-Chhath pattern (previously documented
  for thekua via the r/bihar "thora jyada le aana" post, 2026-11-02) to a second, non-food craft
  category — the diaspora-gifting angle is not food-specific.
- Indian Railways confirmed 6,200 special train trips for Diwali/Chhath travel, a 30% YoY increase
  from 4,666 trips last year — further real-number corroboration of the scale of homeward/festive
  travel and demand around this exact festival window.[9]
- No new named competitor or pricing/discount move surfaced this run on The Thekua Company's own
  site (checked directly) — still describes itself as made-fresh-after-order, no-stock-kept[5],
  same positioning already logged in the watchlist; nothing new to add there.
- MAATI (Mithila Art & Artisan Transformation Initiative, run by Kadam India with Tata Trusts
  backing) continues scaling its own Madhubani-artisan-to-market pipeline — over 150 women artisans
  currently, a stated goal of 100 artisan enterprises and 1,000 artisans over three years.[6] This
  is adjacent, not competitive — MAATI runs its own gallery/exhibition circuit and institutional
  buyers rather than a consumer e-commerce storefront — logged as background, not a watchlist add.

## COMPETITIVE EDGE

**Nothing genuinely new rises to "worth closing" this week.** The watchlist's existing open items
(Exp 9/10 thekua on-page fix + discount test, Exp 7/11 papad/makhana sourcing, Exp 12 approve-the-
stuck-campaign, Exp 13 documentary-content test) already cover every real gap surfaced across the
last six runs, and no new competitor move or named brand appeared this week to add a new row. Per
this skill's own rule, a silent/no-new-gap week is the correct and honest output here — the highest-
priority actionable item remains Exp 12 (unblock the stuck campaign), which is not a new "edge"
finding but an execution blocker now compounding with a tool regression (get_post 500-erroring on
both post ids). Re-flagging it in Top Opportunity above rather than inventing a new competitive
angle to fill this section.

One real, if modest, addition to the evidence base: the Rukam Capital/YouGov survey[1] and the
Manjusha-soops diaspora order data[7] both independently corroborate strategy.md's existing
"regional specialties travel with the diaspora" thesis (first established via the thekua-specific
Reddit/CNBC evidence on 2026-11-02) — this is evidence reinforcement for an existing pillar, not a
new competitor or a new gap, so it is folded into strategy.md's Content Pillar 1 evidence rather than
written up as a separate Competitive Edge item.

## Competitors genuinely new/changed this week (watchlist update)

None. Checked The Thekua Company's live site directly — no change from the existing watchlist entry.
No new competitor name surfaced via Reddit, web search, or site checks this run.
`competitors/watchlist.md` was NOT touched this run (first unchanged run since 2026-10-29, which is
itself informative — the cluster of new thekua-brand sightings from mid-October through early
November appears to have settled for now).

## Sources

[1] https://m.economictimes.com/comment/135410223.cms — ET: Gen Z rewrites festive gifting with AI-assisted picks, artisanal hampers and self-gifting
[2] https://www.reddit.com/r/bihar/comments/1xnilhs/chhath_puja_painting — r/bihar Chhath Puja Painting post
[3] https://www.reddit.com/r/smallbusiness/comments/1xiy8bq/title_started_a_handmade_candle_business_in_india — r/smallbusiness handmade candle business India struggling
[4] https://www.reddit.com/r/bihar/comments/1xn7ard/i_badly_wish_to_see_chhath_puja_this_year_but — r/bihar Chhath Puja tickets thread
[5] https://thekuacompany.com/?srsltid=AYCX9vKqlHAmfXMLZj4WmEnflEWYYXrKUwQSaqUkaMykHV24ChsN-apP — The Thekua Company homepage - made fresh after order, no stock kept
[6] https://yourstory.com/2026/08/heritage-design-mithila-transformation-artisans-creativity-photography — YourStory: MAATI Mithila Art Artisan Transformation Initiative, 150+ women artisans
[7] https://patnapress.com/bhagalpurs-manjusha-art-heads-to-the-us-on-chhath-puja-soops — Patna Press: Bhagalpur Manjusha art soops exported to US for Chhath, 100-200 orders
[8] https://www.divinehindu.in/blogs/news/chhath-puja-2026-date-vidhi-four-day-rituals — Divine Hindu: Chhath Puja 2026 dates 13-16 Nov, thekua as signature prasad, diaspora spread
[9] https://widgets.economictimes.com/topic/made-in-bihar/news — ET: Delhi friends auto-rickshaw 1200km to Bihar for Chhath; 6200 special trains for Diwali/Chhath
