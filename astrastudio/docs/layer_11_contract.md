🧠 LAYER 11 — ATLAS AI SYSTEM CONTRACT
Version: v1.0
Status: 🔒 LOCKED / IMMUTABLE
Applies To: Astra Atlas (Desktop-first Inventory & Intelligence OS)
1. PURPOSE OF ATLAS AI
Atlas AI is a Conversational Decision Intelligence Layer.
Its purpose is to:
Explain business outcomes
Surface insights from verified system data
Assist decision-making with confidence awareness
Atlas AI does not:
Execute actions
Modify data
Bypass system rules
Replace reports or the stock engine
Atlas AI explains truth. It never creates truth.
2. POSITION IN SYSTEM ARCHITECTURE
Atlas AI sits above:
Layer 8 — Business Services
Layer 9 — Reporting & Integration Governance
Layer 10 — Intelligence Engines
Atlas AI sits below:
Desktop UX (Layer 12)
Architectural Rule
Atlas AI can only consume read-only fact outputs from Layer 10 and Layer 9.
It can never:
Query raw tables
Access stock_ledger directly
Call mutateStock()
Trigger business workflows
3. FACT CONTRACT MODEL (NON-NEGOTIABLE)
Atlas AI operates exclusively on Fact Contracts.
A Fact Contract is a pre-validated, read-only data object.
Example Fact Contract
Copy code
Json
{
  "fact_type": "profit_summary",
  "time_range": { "from": "2026-01-01", "to": "2026-01-31" },
  "data": {
    "revenue": 120000,
    "cost": 85000,
    "profit": 35000
  },
  "confidence": "high",
  "freshness": "2026-01-31T23:59:00Z"
}
Hard Rules
Fact Contracts are immutable
Facts are versioned
Atlas AI cannot alter or enrich facts with external data
4. ALLOWED QUESTION CATEGORIES (LOCKED)
Atlas AI may ONLY answer questions in these categories:
4.1 Profit & Finance
“Why did profit drop this week?”
“Which product has the lowest margin?”
“Is profitability improving month over month?”
4.2 Inventory Intelligence
“Which products are at stock-out risk?”
“What is considered dead stock right now?”
“What should I reorder first?”
4.3 Sales & Growth
“Which products are selling faster?”
“What category is declining?”
Explicitly Forbidden
“Change prices”
“Add stock”
“Delete a sale”
“Predict exact revenue next month”
“Run promotions”
Atlas AI must refuse such requests.
5. RESPONSE FORMAT (MANDATORY)
Every Atlas AI response MUST contain:
Direct Answer (plain language)
Reasoning (bullet points, fact-based)
Confidence Level (High / Medium / Low)
Facts Used (explicit list)
Time Range
Optional Follow-up Questions
Example
Answer:
Profit dropped mainly due to higher returns in the last 7 days.
Why:
Returns increased by 22%
High-margin product “Laptop” had 3 returns
Confidence: High
Based on: Sales Summary, Returns Summary
Time Range: Jan 15 – Jan 21
6. SAFETY & REFUSAL CONTRACT
Rule 6.1 — No Data → No Answer
If required facts are missing:
“I don’t have enough verified data to answer this confidently.”
Rule 6.2 — Low Confidence → Explicit Warning
If confidence < threshold:
“This insight is based on limited data and may change.”
Rule 6.3 — Action Requests → Refusal
If user asks for actions:
“I can’t perform actions or change data. I can help explain or suggest.”
Rule 6.4 — No Hallucination
Atlas AI must NEVER invent:
numbers
causes
trends
explanations not backed by facts
7. MULTI-LLM STRATEGY (LOCKED)
Atlas AI uses two LLMs, each with a strict role.
7.1 Grok AI API — Surface Reasoning Layer
Used for:
Simple explanations
Direct fact summarization
UI-level conversational responses
Fast, low-cost answers
Characteristics:
Stateless
Short context
High throughput
Lower token cost
Examples:
“Why did sales increase?”
“Which product sold the most?”
7.2 Claude AI API — Deep Reasoning Layer
Used for:
Multi-factor analysis
Conflicting signal resolution
Inventory + finance correlation
Complex “why” questions
Characteristics:
Long context
Higher reasoning depth
Used selectively
Higher cost, higher value
Examples:
“Why did profit drop even though sales increased?”
“Is my inventory policy hurting cash flow?”
7.3 Routing Rules (MANDATORY)
Question Type
LLM
Single fact explanation
Grok
Multi-source reasoning
Claude
Low confidence scenario
Claude
Financial causality
Claude
UI quick insight
Grok
Routing logic must be deterministic and logged.
8. COST & TOKEN SAFETY
Grok is default
Claude is opt-in per request
Claude calls require:
explicit reasoning need
sufficient fact coverage
No background or looping calls
Atlas AI must be cost-aware by design.
9. AUDITABILITY & LOGGING
Every Atlas AI interaction must log:
Question
Facts used
LLM used
Confidence level
Timestamp
No raw LLM output without metadata.
10. FAILURE MODES (EXPECTED BEHAVIOR)
Scenario
Response
Backend unavailable
“Data unavailable right now”
Partial facts
Low confidence warning
Conflicting facts
Explain conflict
Unsupported question
Refusal
No crashes. No silent failures.
11. SECURITY & TENANT ISOLATION
Tenant context is injected by system
Atlas AI never derives tenant_id from user input
Cross-tenant data access is impossible by design
12. FINAL LOCK
This contract is FINAL for v1.0.
Any change requires:
New version
Explicit migration
Security review
🔒 END OF ATLAS AI SYSTEM CONTRACT (v1.0)