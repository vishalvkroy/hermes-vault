# LinkedIn — 2026-09-24-indexing-bug-fix

**Formula:** F7 Odd-Precision Money/Number Ledger opener (number-first line), closing with a
genuine question per 2026 algorithm heuristics (never open with a question, -34% median likes).
**Status:** pending_approval, post id `c5a1570c-fae0-4037-b480-776df86427e9`.
**Char count:** ~1,340 (within the 900-1,300 sweet spot band, slightly over but justified by
substantive content per the "don't trim below 1,000 to hit the range" guidance).

---

9 out of 100.

That is how many pages on astrastudio.in Google actually indexed, out of 100 it had discovered. Found this in Search Console and the number stopped me.

Root cause: every canonical tag, every OG url, all 100 sitemap entries pointed at the apex domain (astrastudio.in). The site actually serves from www, and Vercel 307-redirects the apex there. So every page told Google "the real version of me lives at a URL that redirects away from itself." Google saw a hundred pages canonicalizing into a loop and quietly dropped 91 of them.

Fixed all 260 hardcoded references to point at www instead. While in there, found two more bugs riding along:

Robots.txt had a separate Googlebot-only rule group with no disallows. A crawler only obeys its most specific matching group, so Googlebot alone was walking into /api, /checkout, /payment and /account.

Sitemap lastmod was always the build timestamp, never the real edit date. That trains Google to stop trusting lastmod at all.

Shipped a blog CMS in the same pass. Posts now live in a database behind a real API, so publishing does not need a code deploy anymore.

None of this shows up in a demo. It is the kind of work that decides whether the other 260 hours of building ever get found.

What is the most boring bug you have fixed that mattered more than any feature that week?

P.S. Indexing is still climbing back. I will post the before/after numbers once Search Console catches up.

---

## Humanizer pass notes
Ran against `writing/humanizer` patterns before finalizing:
- No em dashes/en dashes present.
- No inflated-legacy language ("testament", "pivotal", "represents a shift") - kept to plain
  mechanism description.
- No vague sources - every claim traces to the real commit and repo, no "experts say" filler.
- No forced triads beyond the two real named bugs (robots.txt, sitemap) plus the CMS ship - three
  real items, not manufactured for rhythm.
- Ends on the real open item (indexing still recovering) instead of a generic positive send-off.
- One real number-first hook (9/100), no rhetorical question as opener, closing question genuine
  and answerable, P.S. carries a real follow-up commitment (not a CTA gimmick).
