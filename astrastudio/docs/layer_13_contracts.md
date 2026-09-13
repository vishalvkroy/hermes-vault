1. PURPOSE OF LAYER 13
Layer 13 governs who can access Astra Atlas, at what scale, and under what commercial terms, without ever risking:
stock correctness
ledger integrity
seller trust
Layer 13 does not add features.
It controls access and monetization.
2. CORE PHILOSOPHY (NON-NEGOTIABLE)
2.1 Adoption Before Monetization
Sellers must be able to run their business fully before being asked to pay.
2.2 Never Block Selling
Sales creation must never be blocked by plan limits, except in extreme governance states.
2.3 Monetize Insight, Not Survival
Sellers pay for clarity, scale, and convenience, not for basic operation.
3. SYSTEM ROLES (LOCKED)
Astra Studio (Website)
Account creation
Authentication
Subscription & billing
Plan selection
Usage visibility
Astra Atlas (Desktop App)
Business execution
Inventory, sales, reports, AI
Enforces plan limits
Never handles payments
There is one identity system shared across both.
4. TENANT LIFECYCLE (LOCKED)
Each tenant MUST be in exactly one state:
State
Meaning
TRIAL
Default for all new users
ACTIVE
Paid subscription
SUSPENDED
Payment / abuse issue
READ_ONLY
All writes blocked
TERMINATED
Soft-deleted
Rules
❌ No hard deletes
❌ No silent state changes
✅ READ_ONLY blocks all mutations, not just sales
5. PLAN MODEL (TRIAL-FIRST)
🟢 TRIAL (DEFAULT — ₹0)
Designed to build daily habit.
✅ Unlimited sales
✅ Unlimited purchases & returns
✅ Inventory management
✅ POS + offline mode
✅ Ledger & basic reports
❌ Exports
❌ Integrations
Soft limits only (non-blocking):
Products: 100
Devices: 1
Atlas AI: 5 queries / month
🔵 BASIC (₹299–₹499)
Unlimited sales
Products: 500
Devices: 1
Atlas AI: 50 / month
Full reports
Limited exports
🟣 STANDARD (₹999)
Unlimited sales
Products: 5,000
Devices: 3
Atlas AI: 300 / month
Advanced reports
Integrations: 1
🟡 ENTERPRISE
Custom limits
SLA
Priority support
Custom AI quotas
6. SALES GOVERNANCE (CRITICAL)
🔒 RULE (LOCKED)
Sales creation is NEVER hard-limited by plan.
Backend logic:
Copy code
Text
IF tenant_state == READ_ONLY
  → block ALL writes
ELSE
  → allow sale creation
No other sales blocking is allowed.
7. WHAT CAN BE HARD-LIMITED
Hard limits are allowed ONLY on cost drivers:
Atlas AI queries
Devices
Integrations
Report exports
API rate limits
These are transparent and expected.
8. ADVANCED REPORTS — DEFINITION (LOCKED)
Always Free
Daily / weekly sales totals
Stock snapshot
Basic profit
Returns summary
GST summary (view only)
Paid (Advanced)
Historical comparisons (MoM, YoY)
Product / category profitability
Inventory turnover & dead stock aging
Trend analysis
Exports (PDF / Excel)
Scheduled reports
Basic visibility must NEVER be paywalled.
9. ATLAS AI GOVERNANCE
Atlas AI is quota-based
Quota exhaustion → graceful refusal
AI never mutates data
AI limits are plan-dependent
10. TRANSPARENCY REQUIREMENTS
Every tenant MUST see:
Current plan
Usage vs limits
Reset dates
Upgrade path
No dark patterns. No surprise blocks.
11. CHANGE POLICY
Any change to:
Sales governance
Trial generosity
Hard limits
Requires:
New contract version
Backward compatibility review
Explicit communication