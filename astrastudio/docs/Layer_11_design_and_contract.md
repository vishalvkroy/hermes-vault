Layer 11 — AI Business Assistant

for Astra Atlas

This is not feature fluff. This is an overlay intelligence system designed to sit safely on top of a stock-critical core.

LAYER 11 — AI BUSINESS ASSISTANT

(Read-Only, Reasoning-Only, Trust-Preserving Layer)

1. PURPOSE & POSITIONING (WHY THIS LAYER EXISTS)
What Layer 11 IS

A conversational decision assistant that helps business owners understand and act on computed business facts.

It answers questions like:

“Why did profit drop this week?”

“Which products should I reorder now?”

“What happens if I increase prices by 5%?”

“Can I afford to hire another staff member next month?”

What Layer 11 IS NOT

❌ Not a reporting engine
❌ Not a data source
❌ Not a stock modifier
❌ Not an authority on numbers
❌ Not allowed to invent, guess, or estimate business data

Layer 11 explains reality — it does not create it.

2. LAYER PLACEMENT IN SYSTEM ARCHITECTURE
┌──────────────────────────────┐
│        Desktop App           │
│   (Chat UI / Insights UI)    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   AI Business Assistant      │  ← LAYER 11
│   (Reasoning Engine)         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Intelligence Service       │  ← Layer 10 (READ-ONLY)
│   (Profit, Reorder, Demand)  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Core Transaction Service   │  ← Layers 4–9
│   (Stock, Sales, Purchases)  │
└──────────────────────────────┘

⚠️ Layer 11 NEVER talks to core tables directly

3. NON-NEGOTIABLE SYSTEM CONSTRAINTS (HARD RULES)

These are laws, not guidelines.

🔒 Constraint 1 — READ-ONLY GUARANTEE

Layer 11:

❌ Cannot mutate stock

❌ Cannot create/update sales

❌ Cannot write to ledger

❌ Cannot trigger workflows

Enforcement

Database user: READ-ONLY

API gateway blocks write routes

No access to mutateStock()

🔒 Constraint 2 — FACTS COME ONLY FROM LAYER 10

Layer 11 may only consume:

Profit summaries

Demand forecasts

Reorder suggestions

Aggregated metrics

❌ Never raw tables
❌ Never live transactional queries

If a metric does not exist → Assistant must say it cannot answer

🔒 Constraint 3 — NO NUMBER HALLUCINATION

If a number is:

Missing

Delayed

Outdated

Not computed yet

The assistant MUST respond with:

“I don’t have enough computed data to answer this reliably.”

This is intentional honesty, not a failure.

🔒 Constraint 4 — EXPLAINABILITY IS MANDATORY

Every answer that includes a conclusion MUST include:

Source metrics used

Time range

Assumptions

Confidence level (high / medium / low)

No black-box answers.

🔒 Constraint 5 — AI NEVER DECIDES, ONLY ADVISES

Layer 11:

May recommend

May simulate

May explain consequences

❌ May NOT auto-execute actions
❌ May NOT trigger purchases
❌ May NOT approve sales

4. DATA CONTRACT (WHAT LAYER 11 CAN SEE)
Allowed Inputs (STRICT)

Layer 11 may query only these interfaces:

GET /intelligence/profit
GET /intelligence/reorder
GET /intelligence/demand
GET /intelligence/inventory-summary
GET /intelligence/cashflow
GET /intelligence/tax-summary

Each response MUST include:

computed_at

time_range

confidence_score

source_version

Forbidden Inputs

❌ products table
❌ stock_ledger
❌ sales / purchases
❌ Any mutable endpoint

5. QUERY → RESPONSE FLOW (DETERMINISTIC PIPELINE)
Example: “Why did profit drop this week?”
User Query
   ↓
Intent Classification
   ↓
Metric Dependency Resolution
   ↓
Fetch Precomputed Metrics (Layer 10)
   ↓
Consistency Check (timestamps, completeness)
   ↓
Reasoning + Explanation
   ↓
Natural Language Response

⚠️ If any dependency fails, response is blocked.

6. RESPONSE CONTRACT (MANDATORY FORMAT)

Every response MUST follow this structure internally:

Answer:
- Direct answer (plain language)


Reasoning:
- Metrics used
- Comparisons made
- Trends detected


Evidence:
- Profit delta
- Cost delta
- Volume delta


Confidence:
- High / Medium / Low


Limitations:
- Missing data
- Assumptions

If the model cannot fill all sections, it must refuse.

7. SAFE QUESTION CATEGORIES (ALLOWED)
✅ Allowed

“Explain”

“Compare”

“Forecast (based on existing demand model)”

“What-if simulation (read-only)”

“Summarize business health”

❌ Forbidden

“Fix my stock”

“Place an order”

“Change prices”

“Override GST”

“Hide losses”

“Ignore this discrepancy”

8. WHAT-IF SIMULATION CONTRACT

Layer 11 may simulate ONLY by:

Copying Layer 10 metrics

Applying temporary deltas

NEVER persisting results

Example:

“If you increase price by 5%, estimated margin increases by X% assuming volume remains constant.”

⚠️ Must clearly state:

This is a simulation

Assumptions used

No real data changed

9. FAILURE & SAFETY BEHAVIOR
Must Refuse When:

Ledger reconciliation pending

Profit engine behind schedule

Stock discrepancies detected

Metrics confidence < threshold

Must Surface Warnings:

“Some data is still syncing. Insights may be incomplete.”

10. AUDITABILITY & LOGGING

Every AI interaction must log:

User ID

Tenant ID

Question

Metrics accessed

Response confidence

Timestamp

Logs are immutable and reviewable.

11. SECURITY & TENANT ISOLATION

Tenant context injected before reasoning

No cross-tenant reasoning

No global benchmarking unless explicitly allowed

Model prompt NEVER contains other tenant data

12. SUCCESS CRITERIA (WHEN LAYER 11 IS “DONE”)

Layer 11 is production-ready ONLY if:

It has zero write access

It refuses unsafe questions

It never invents numbers

It explains every answer

It degrades gracefully

It can be turned OFF without affecting core system

FINAL ARCHITECT VERDICT

Layer 11 is:

An advisor

A translator

A simulator

A business explainer

It is not:

A controller

A shortcut

A decision maker

You’ve done the right thing by designing this after Layer 10.