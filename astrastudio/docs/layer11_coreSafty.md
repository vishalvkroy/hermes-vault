LAYER 11 — CORE SAFETY & CONTROL SPEC
Part 1: Intent Classification Taxonomy
Part 2: Confidence Scoring Rules
Part 3: AI Refusal Policies

These three together form the safety cage around your AI assistant.

PART 1 — INTENT CLASSIFICATION TAXONOMY
Goal

Convert natural language into a bounded, auditable intent, so the AI never “freestyles” actions or reasoning.

❗ The AI NEVER reasons before intent is classified.

1.1 Intent Classification Pipeline
User Input
   ↓
Intent Detection
   ↓
Intent Validation (Allowed / Restricted / Forbidden)
   ↓
Metric Dependency Mapping
   ↓
Confidence Gate
   ↓
Answer or Refusal

If any stage fails → REFUSE.

1.2 Canonical Intent Categories (ENUM)
enum AssistantIntent {
  EXPLAIN_METRIC,        // "Why did profit drop?"
  COMPARE_PERIODS,       // "Compare this week vs last week"
  SUMMARIZE_STATE,       // "How is my business doing?"
  FORECAST_BASED,        // "What will demand look like next month?"
  WHAT_IF_SIMULATION,    // "What if I increase prices by 5%?"
  RISK_ALERT_EXPLANATION,// "Why is this product risky?"
  CLARIFICATION,         // "What does dead stock mean?"
  DATA_AVAILABILITY,     // "Do I have data for X?"
  OUT_OF_SCOPE,          // Unknown but harmless
  FORBIDDEN_ACTION       // Must refuse
}
1.3 Allowed Intents (SAFE)
Intent	Description
EXPLAIN_METRIC	Explain already computed numbers
COMPARE_PERIODS	Compare two completed time ranges
SUMMARIZE_STATE	High-level health summary
FORECAST_BASED	Forecast using Layer 10 outputs only
WHAT_IF_SIMULATION	Hypothetical, read-only scenarios
CLARIFICATION	Definitions, explanations
1.4 Restricted Intents (Require Extra Checks)
Intent	Extra Validation
WHAT_IF_SIMULATION	Must declare assumptions
FORECAST_BASED	Must have confidence ≥ threshold
RISK_ALERT_EXPLANATION	Must reference existing alerts
1.5 Forbidden Intents (AUTO-REFUSE)

These must never reach reasoning.

enum ForbiddenIntent {
  MODIFY_STOCK,
  CREATE_SALE,
  CREATE_PURCHASE,
  OVERRIDE_GST,
  HIDE_LOSSES,
  DELETE_RECORDS,
  BYPASS_RULES,
  MANIPULATE_REPORTS,
  EXECUTE_ACTION,
  PROVIDE_LEGAL_EVASION
}

Examples

“Ignore this stock mismatch”

“Place an order for 50 units”

“Adjust GST to reduce tax”

“Can you fix this inventory error?”

⛔ Immediate refusal (see Part 3).

1.6 Intent → Metric Dependency Matrix

Each intent declares exact metric dependencies.

Example:

EXPLAIN_METRIC → [
  profit_summary,
  sales_volume,
  cost_changes
]

If any dependency missing → REFUSE.

PART 2 — CONFIDENCE SCORING RULES
Goal

Ensure AI answers are trustworthy, bounded, and honest.

Confidence is not how sure the AI feels — it is data completeness + freshness + consistency.

2.1 Confidence Inputs

Each answer computes confidence from:

Factor	Description
Data Completeness	All required metrics present
Data Freshness	Metrics computed recently
Ledger Consistency	No reconciliation errors
Forecast Stability	Volatility within bounds
Time Coverage	Full period available
2.2 Confidence Scoring Formula (Deterministic)
confidence_score =
  completeness_score (0–40)
+ freshness_score    (0–20)
+ consistency_score  (0–20)
+ stability_score    (0–20)

Max = 100

2.3 Confidence Levels (ENUM)
enum ConfidenceLevel {
  HIGH,    // ≥ 85
  MEDIUM,  // 65–84
  LOW,     // < 65
  INVALID  // Missing critical data
}
2.4 Confidence Gates (HARD RULES)
Confidence	Behavior
HIGH	Full answer allowed
MEDIUM	Answer + explicit caveats
LOW	Partial answer + warning
INVALID	Refuse to answer
2.5 Mandatory Confidence Disclosure

Every response MUST include:

Confidence: HIGH / MEDIUM / LOW
Reason: (why)

No exception.

2.6 Examples

HIGH

“Profit dropped 12% mainly due to increased supplier costs.”

MEDIUM

“Profit likely dropped due to rising costs, but some sales data is still syncing.”

LOW

“I can’t reliably explain the profit change yet — sales data is incomplete.”

PART 3 — AI REFUSAL POLICIES
Goal

Ensure the assistant never becomes dangerous, misleading, or authoritative.

Refusal is a feature, not a failure.

3.1 Refusal Categories
enum RefusalReason {
  FORBIDDEN_INTENT,
  INSUFFICIENT_DATA,
  LOW_CONFIDENCE,
  OUT_OF_SCOPE,
  SYSTEM_UNSAFE,
  DATA_INCONSISTENT,
  PERMISSION_DENIED
}
3.2 Refusal Tone Rules (VERY IMPORTANT)

A refusal must be:

Calm

Non-judgmental

Clear

Professional

Helpful without bypassing rules

❌ Never say “I’m just an AI”
❌ Never blame the user

3.3 Refusal Response Template
I can’t help with that request right now.


Reason:
<clear explanation>


What I can help with instead:
<safe alternatives>
3.4 Mandatory Refusal Scenarios

The AI MUST refuse if:

Intent is forbidden

Required metric missing

Ledger reconciliation pending

Confidence = INVALID

User asks to bypass system rules

User asks to execute changes

3.5 Example Refusals

Forbidden action

“I can’t place orders or change stock.
I can help explain which products are running low.”

Insufficient data

“Sales data for this period is still syncing, so I can’t explain profit changes reliably yet.”

System safety

“There’s a stock discrepancy under investigation. I can’t provide recommendations until it’s resolved.”

3.6 Refusal Logging (MANDATORY)

Each refusal logs:

{
  "tenant_id": "...",
  "user_id": "...",
  "intent": "...",
  "refusal_reason": "...",
  "confidence": "...",
  "timestamp": "..."
}
FINAL ARCHITECT SUMMARY

With these three pieces:

✅ Intent is bounded
✅ Reasoning is deterministic
✅ Confidence is explicit
✅ Unsafe requests are blocked
✅ Trust is preserved

This is enterprise-grade AI governance, not chatbot behavior.