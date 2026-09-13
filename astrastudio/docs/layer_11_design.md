🔹 LAYER 11 — ATLAS AI
Conversational Decision Intelligence
Status: DESIGN + SAFETY CONTRACT (v1.0)
Platform: Desktop (Tauri + React)
Audience: Business owners, operators, accountants
Goal: Turn verified system facts into understandable decisions
1️⃣ What Atlas AI IS (and is NOT)
✅ Atlas AI IS
A decision explanation layer
A business reasoning assistant
A question-answering system grounded in facts
A confidence-aware advisor
❌ Atlas AI IS NOT
A reporting engine
A chatbot that invents numbers
A system that mutates data
A free-form LLM playground
Atlas AI never acts. It only explains, warns, and suggests.
2️⃣ Atlas AI UI DESIGN (DESKTOP-FIRST)
🔹 Entry Point
Persistent “Atlas” button in TopBar
Keyboard shortcut: Ctrl + Space
Opens a side panel, not a modal.
Why:
Non-blocking
Context-preserving
Professional (like IDE assistants)
🔹 Layout Structure
Copy code

┌──────────────────────────────┐
│ Atlas AI                     │
│ “Business Intelligence”      │
├──────────────────────────────┤
│ Context Header               │
│ • Store: Demo Business       │
│ • Period: Last 30 days       │
│ • Data freshness: ✔ Live     │
├──────────────────────────────┤
│ Conversation Area            │
│                              │
│ Q: Why did profits drop?     │
│ A: … explanation …           │
│                              │
├──────────────────────────────┤
│ Confidence / Source Footer   │
│ • Confidence: High           │
│ • Based on: Sales, Returns  │
├──────────────────────────────┤
│ Input Box                    │
│ [ Ask Atlas… ]   [Send]     │
└──────────────────────────────┘
🔹 Visual Tone
Dark graphite background
Subtle gradients
No emojis
No “chatty” style
Calm, advisory voice
Feels like:
Talking to a senior analyst, not a chatbot
3️⃣ HOW ATLAS AI THINKS (CRITICAL)
Atlas AI never queries raw tables directly.
Instead, it uses Fact Contracts.
🔹 Fact Contracts
A Fact Contract is a pre-validated, read-only dataset, such as:
Profit summary (Layer 10)
Inventory health report
Sales trends
Return reasons
Reorder suggestions
Each fact includes:
Copy code
Ts
{
  data: number | object,
  time_range: { from, to },
  freshness: timestamp,
  confidence: "high" | "medium" | "low"
}
4️⃣ ALLOWED QUESTION TYPES (LOCKED)
Atlas AI ONLY answers questions in these categories:
✅ Profit & Finance
“Why did profit drop this week?”
“Which product has lowest margin?”
“Is my cash flow improving?”
✅ Inventory Intelligence
“Which items are at stock-out risk?”
“What is dead stock?”
“What should I reorder?”
✅ Sales & Growth
“What products are selling faster?”
“Which category grew the most?”
❌ NOT ALLOWED
“Change my prices”
“Delete a sale”
“Add stock”
“Predict exact revenue next month”
Atlas AI cannot mutate state.
5️⃣ RESPONSE FORMAT (STRICT)
Every Atlas AI response MUST contain:
1. Direct Answer (Plain English)
Short, clear, human.
2. Reasoning (Bullet Points)
Based on facts, not guesses.
3. Confidence Level
High / Medium / Low
4. Data Sources Used
Example:
“Based on Sales (last 30 days), Returns, Inventory Ledger”
5. Optional Follow-ups
Suggested clarifying questions.
6️⃣ SAFETY & REFUSAL CONTRACT (NON-NEGOTIABLE)
🔒 Rule 1 — No Data → No Answer
If required facts are missing:
“I don’t have enough data to answer this confidently.”
Never hallucinate.
🔒 Rule 2 — Uncertain Data → Explicit Warning
If confidence < threshold:
“This insight is based on limited data and may change.”
🔒 Rule 3 — Out-of-Scope Requests → Refusal
Example:
“I can’t perform actions or change data. I can help explain or suggest.”
🔒 Rule 4 — Time Awareness
Atlas AI must always state:
Time range used
Data freshness
7️⃣ AUDITABILITY & TRUST
Every AI response must be:
Deterministic for same facts
Reproducible
Logged (question + facts used)
No black box answers.
8️⃣ FAILURE MODES (DESIGNED)
Scenario
Behavior
Backend unavailable
“Data unavailable right now”
Partial data
Low confidence + warning
Conflicting signals
Explain conflict
User confusion
Ask clarifying question
9️⃣ WHY THIS DESIGN IS A MOAT
Most apps:
Show dashboards
Dump numbers
Add a chatbot later
Astra Atlas:
Locks correctness first
Builds intelligence
Adds explainable AI
This makes Atlas AI:
Trustworthy
Auditable
Business-grade
Hard to copy
🔒 FINAL LOCK (v1.0)
Atlas AI:
Read-only
Fact-contract driven
Confidence-aware
Refusal-capable
Explainable by design
No changes without v2.0.