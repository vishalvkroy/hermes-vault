# Hermes Research Vault

Durable knowledge store per spec section 6 (Memory + Low Token Consumption) - the
"Knowledge" tier: large reference material retrieved on demand instead of
injected into every prompt, and the "Episodic memory" tier: outcomes like
which content formats worked and which experiments failed.

## Structure
Each brand folder has:
- `research/` - market/competitor/trend findings (spec section 7 output: evidence-first, timestamped, source-aware)
- `campaigns/` - campaign records (spec section 15: campaign ID, timestamp, channel, hypothesis, outcome)
- `learnings/` - what worked / what failed, feeding the next cycle
- `competitors/` - per-competitor watchlist notes (spec section 14)

`_cross-brand/` is for findings that legitimately span brands - keep this rare;
default to filing under the specific brand.

Write notes here via the `obsidian-markdown` / `obsidian-cli` skills. Don't
inject vault contents wholesale into context - retrieve specific notes on
demand, matching the low-token-consumption principle this exists to serve.

## Cadence
Daily research cron jobs run staggered mornings (UTC):
- MadeByHer: 06:00
- RabbitLore: 06:15
- Astra Studio: 06:30

Each follows the Deep Research Engine flow (spec section 7): Research -> Evidence
extraction -> Source comparison -> Change detection -> Opportunity scoring ->
Recommendations -> Structured findings -> Feed strategy -> Measure outcome -> Store
learning. Findings land in <brand>/research/ as dated notes; competitor watchlist
entries land in <brand>/competitors/. Telegram gets a message only when something is
actually actionable — silence most days is the healthy/correct default, not a bug.
