# Campaign: 2026-09-06-invisible-crashes

**Campaign ID:** 2026-09-06-invisible-crashes
**Timestamp:** 2026-09-06T08:13:00Z
**Status:** drafted

## Objective
Turn this week's real Astra Atlas desktop shipment (crash reporting, commit 3e018f9, Sep 6 2026) into a founder-led LinkedIn post that backs up the "offline-first, built for tier-2/3 reliability" claim with an engineering detail most competitors don't talk about: what happens when the app breaks on a shopkeeper's machine that nobody is watching.

## Hypothesis
Research (both the Sept 4 baseline and the Sept 4 update, which reconfirms it unchanged) names offline-first architecture as Astra Atlas's clearest differentiator against cloud-first competitors like GoFrugal and Posist, with an explicit message opportunity: "Works without internet" positioning for tier-2/3. That claim is usually made as a feature bullet. A concrete story about closing the gap between "it works offline" and "we find out when it breaks" - including a real bug the fix caught (returning sessions silently skipping the tag that would identify which shop and user hit the crash) - makes the reliability claim specific and credible instead of generic, matching the update doc's separate finding that generic claims ("AI-powered," and by extension "reliable") are no longer differentiating on their own.

## Grounded in research finding
Source: `astrastudio/research/2026-09-04-market-signals.md`, Opportunities & Strategic Insights #1, "Offline-first architecture is becoming differentiator" - "Astra Atlas' real offline-first design... aligns with real tier-2/3 pain... Competitors still cloud-first... Message opportunity: 'Works without internet' positioning in tier-2/3 marketing."

Reconfirmed unchanged in `astrastudio/research/2026-09-04-market-signals-update.md` ("Astra Atlas positioning: Offline-first architecture continues to address tier-2/3 connectivity constraint. No new competitor launches in this space detected.") and supported by that same doc's Finding #3, "AI Adoption is Baseline, Not Story," which argues generic capability claims need specific, demonstrated backing rather than a feature-list mention.

## Real event pulled from repo (git log)
- Commit `3e018f9` (Sep 6 2026): "feat: crash reporting for the desktop app" - added Sentry to the Tauri desktop client (backend has had it for a while; desktop never did). Wired at three points: `ErrorBoundary.componentDidCatch` (covers every screen in one call site, no per-screen wiring), `main.tsx`'s existing `window.onerror` / `unhandledrejection` handlers (catches crashes before React even mounts), and `appStore`'s `setCurrentUser`/`logout` (tags events with tenant_id and user_id).
- Real bug caught while building it: a returning session restores its persisted user straight into the store's initial state, bypassing `setCurrentUser` entirely - so a crash on a normal "already signed in" app restart (the common case, not the rare one) would have reported with no tenant or user attached, defeating the whole point for the most frequent scenario.
- Scrubs the Authorization header before anything leaves the machine; separate Sentry project from the backend's. Needs `DESKTOP_SENTRY_DSN` added as a GitHub Actions secret before it starts reporting anything - shipped, not yet switched on in production.
- Co-authored with Claude Sonnet 5, per repo convention.

## Target audience
Indian SMB retailers and owner-operators running Astra Atlas on shop-floor Windows machines, especially in tier-2/3 towns with unreliable connectivity and no in-house IT support. Secondary: SaaS founders/engineers following build-in-public technical content.

## Channels used
- **LinkedIn** (primary, connected account: astrastudio, provider linkedin, account "Vishal Kumar") - founder-led post, drafted below. Post ID `98a07402-b4b7-4d4b-9fcc-5e898396f335`, status `pending_approval`, approval requested from Vishal via Telegram on 2026-09-06.
- Instagram/Facebook/Reddit: not connected for this brand - no drafts produced this cycle (LinkedIn is Astra Studio's only live platform).

## URLs
None (native LinkedIn post, no external link).

## Metrics
Pending (fill in after Vishal approves, publishes, and analytics collect).

## Outcome
Pending.
