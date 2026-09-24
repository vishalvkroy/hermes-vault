# Campaign: 2026-09-24-indexing-bug-fix

**Campaign ID:** 2026-09-24-indexing-bug-fix
**Timestamp:** 2026-09-24T04:40:00Z
**Status:** pending_approval (LinkedIn)

## Objective
Turn this week's real, shipped SEO/indexing fix (commit `c34794e`, merged 2026-09-19) into a
founder-led LinkedIn post that demonstrates engineering rigor to a technical Indian SMB/founder
audience, while implicitly building the credibility base the neglected Services line (custom
web/app dev) needs before it can run its own campaign.

## Hypothesis
Of three real, evidence-backed candidates this week (SaaS engineering fix, SaaS competitive
positioning vs Vyapar, Services-line pricing/positioning post), the indexing bugfix carries the
strongest verifiable evidence (a real commit, a concrete before/after mechanism, no invented
numbers), is the most distinctive on a feed full of generic SaaS claims, and - per one flagship
model's framing - doubles as the missing "case study" proof point the Services line currently
lacks (no real completed client project exists yet to cite for Services directly).

## council_review question and verdict
Asked flagship-tier models (via `council_review`, tier=flagship) to pick between: (A) the
indexing bugfix engineering story, (B) SaaS competitive positioning vs Vyapar's "barcode trap",
(C) a Services-line pricing/positioning post with no case study to cite. Gemini and Mistral
hit repeated 429 rate limits across ~10 retries and never returned a substantive answer; Claude
(cc/claude-opus-5) and Groq (openai/gpt-oss-120b) both returned full answers.

**Verdict (2/2 responding models agree):** Pick A, the indexing bugfix. Both cited evidence
strength (a real commit + concrete numbers vs. anecdotal Reddit complaints or zero data for
Services), audience credibility with a technical founder readership, and distinctiveness against
generic SaaS marketing. Claude's opus-5 response additionally framed A as an indirect proof point
for the neglected Services line ("A *is* C's missing case study... you can't sell custom dev with
no client story, but you can sell it on your own site as the proof") and recommended sequencing:
B next week (branded search demand is already being captured passively via existing landing
pages, so it can wait), C only after 2-3 posts like A have built technical-authority credibility -
never as a standalone pricing pitch with zero proof behind it.

**My call:** Followed the 2/2 agreeing verdict. Going with A this week. Noting for next cycle:
sequence B (Vyapar/barcode-trap positioning) for next week per the model's reasoning that its
demand signal is already live and can wait one cycle; revisit C (Services) only once 2+ SaaS
engineering/positioning posts have run, per the "credibility before pricing pitch" argument -
this matches the campaign-workflow skill's own guidance to weigh Competitive Edge findings, not
just react to a single week's opportunity in isolation.

## Grounded in research finding
Source: `astrastudio/research/2026-09-21_deep_research.md`, Section 3 "Internal Ground Truth &
Shipped Code" - "Recent git commits confirm active shipping of SEO content and platform
infrastructure... Blog CMS, admin panel, sitemap/robots canonicalization... deployed." Also
`astrastudio/research/2026-09-18_deep_research.md`'s note that the Services line has "zero
organic search volume... confirms the zero attention status," which is why Services was not
picked this week despite being real and live - no proof point exists yet to back a Services post,
while the indexing fix genuinely doubles as one per the council verdict above.

## Real event pulled from repo (git log)
- Commit `c34794e` (merged 2026-09-19, `fix(seo): canonicalize on www, fix sitemap/robots, add
  blog CMS and admin`): root cause of "100 pages discovered, 9 indexed" - every canonical URL, OG
  tag, and all 100 sitemap URLs pointed at the apex domain (astrastudio.in), while the site
  actually serves from www and Vercel 307-redirects the apex there. Every page canonicalized back
  to a URL that redirects away from itself; Google discarded 91 of 100 discovered pages. Fixed
  all 260 hardcoded references to use https://www.astrastudio.in.
- Also fixed in the same commit: a separate Googlebot-only robots.txt rule group had no
  disallows (a crawler obeys only its most specific matching group), so Googlebot alone could
  walk into /api, /checkout, /payment, /account; sitemap lastmod was always the build timestamp
  instead of the real edit date, teaching Google to distrust lastmod; blog index linked 9 posts
  that 404'd (now 301s, removed from index); security headers added; custom 404 page.
- Same commit shipped a real blog CMS: one shared data source (static + database posts) feeds
  index, post pages, sitemap, and JSON-LD, replacing four hand-maintained lists that had drifted
  apart. `/admin/blog` is a password-gated Markdown editor with preview, scheduling, an SEO
  checklist; publishing revalidates instantly and pings IndexNow.
- Companion commit `220886c` (`feat(backend): blog API for the marketing site`): added
  `blog_posts` table + `/api/public/blog/posts` and `/api/admin/blog/posts` routes so posts
  publish from a database without a code deploy; admin routes refuse all requests if
  `BLOG_ADMIN_KEY` is unset or under 24 chars rather than falling back open.
- Co-authored with Claude Sonnet 5, per repo convention. Real, verified via `git show --stat` on
  both commits.

## Target audience
Technical Indian SMB founders/operators evaluating SaaS tooling, plus fellow founders/engineers
who follow build-in-public technical content and judge credibility by specificity, not claims.

## Channels used
- **LinkedIn** (primary, connected account: astrastudio, provider linkedin, account "Vishal
  Kumar") - founder-led engineering post, drafted below. Post ID
  `c5a1570c-fae0-4037-b480-776df86427e9`, status `pending_approval`, approval requested from
  Vishal via `request_publish_approval` on 2026-09-24. Never called `publish()` directly - it
  correctly refuses on a fresh unapproved draft, per this skill's corrected publishing model.
- Instagram/Facebook/Reddit: not connected for this brand - no drafts produced this cycle
  (LinkedIn is Astra Studio's only live platform).

## URLs
None (native LinkedIn post, no external link in body per algorithm-heuristics guidance).

## Metrics
Pending (fill in after Vishal approves, publishes, and analytics collect).

## Outcome
Pending.
