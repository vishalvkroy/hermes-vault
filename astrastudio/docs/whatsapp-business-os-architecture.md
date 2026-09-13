# WhatsApp Business OS — Architecture

> **Status:** Approved for implementation  
> **Date:** 2026-07-03  
> **Author:** CTO Planning Session

---

## The Core Insight

What you have is a good WhatsApp POS. What this describes is a **WhatsApp Business OS**. The difference is direction.

```
Current:   Staff → message → sale recorded
           (WhatsApp as a terminal)

Elevated:  Staff    ↔ Atlas ↔ Customer
           Manager  ↔ Atlas ↔ Team
           System   ↔ Atlas ↔ Seller  (proactive alerts)

           (WhatsApp as a living business layer)
```

The phone number IS the identity. Staff phone = employee. Customer phone = customer profile that persists across **every Atlas-powered shop they ever visit**. That's a network effect no traditional POS can build.

---

## Part 1: WhatsApp Business OS — 7 Elevations

### The Three Principles

```
1. ZERO questions at sale time
2. Catalog taught once, sells forever
3. Customer gets invoice before seller puts the phone down
```

---

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     REGISTRATION LAYER                          │
│                                                                 │
│  Seller registers tenant  →  Atlas ingests catalog             │
│  Conflict detection: "You have 2 'Antivirus' — different prices"│
│  Auto-assigns SELL CODES:  AV-999  /  AV-1999                  │
│  Sends staff their Quick Card via WhatsApp once                 │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                      SALE TIME (ZERO FRICTION)                  │
│                                                                 │
│  Staff:  "AV-1999 x2, Rahul 9876543210, upi"                  │
│          ─── OR ───                                             │
│          "2 antivirus 1999, Rahul 9876543210, upi"             │
│                  ↓                                              │
│  Match: sell code → exact  OR  name + price hint → exact       │
│         still ambiguous? → pick by staff's own sales history   │
│                  ↓                                              │
│  Sale created → Stock deducted → Invoice sent to Rahul         │
│  Staff gets: "✅ Done. ₹3998. Invoice sent to Rahul."          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                   CUSTOMER INVOICE LAYER                        │
│                                                                 │
│  WhatsApp message to Rahul's number:                           │
│  ┌─────────────────────────┐                                   │
│  │ Invoice from XYZ Store  │                                   │
│  │ Antivirus Elite  x2     │                                   │
│  │ ₹1999 × 2 = ₹3998      │                                   │
│  │ GST (18%): ₹610.17      │                                   │
│  │ Total: ₹3998             │                                   │
│  │ Paid via: UPI ✓          │                                   │
│  │ [QR Code — UPI / Portal] │                                   │
│  └─────────────────────────┘                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### Elevation 1: Voice Notes (India-First)

Staff in Indian retail don't type — they speak.

```
Staff sends voice note: "दो एंटीवायरस एलीट, राहुल को, UPI"
                                ↓
Whisper transcription (async, <2s)
                                ↓
Same NLP pipeline → "2 Antivirus Elite, Rahul, UPI"
                                ↓
Same sale flow — staff never typed a word
```

**Architecture:**
```
wa_message_handler
  ├── type: 'text'   → existing NLP pipeline
  ├── type: 'audio'  → whisperTranscribe() → NLP pipeline
  └── type: 'image'  → future: OCR on handwritten bill
```

Whisper runs on backend (OpenAI API or self-hosted). Language auto-detected — Hindi, Hinglish, Tamil, any Indian language works natively.

---

### Elevation 2: Staff Personal Aliases

Every staff member defines their own shortcuts. Taught once, used forever.

```
Priya texts: "alias av = Antivirus Elite 1999"
Atlas: "✅ Got it Priya. 'av' now means Antivirus Elite ₹1999."

Next sale:
Priya: "av x2, rahul 9876543210, upi"
Atlas: Resolved instantly. No lookup, no ambiguity, no friction.
```

**Data model:**
```sql
CREATE TABLE wa_staff_aliases (
  id          uuid PRIMARY KEY,
  tenant_id   uuid NOT NULL,
  employee_id uuid NOT NULL,
  alias       varchar(20) NOT NULL,   -- "av"
  product_id  uuid NOT NULL,
  created_at  timestamptz DEFAULT now(),
  UNIQUE (tenant_id, employee_id, alias)
);
```

**Product resolution hierarchy (final):**
```
1. Staff personal alias     → exact, instant
2. Sell code                → exact, instant
3. Name + price hint        → near-exact
4. Exact name, one result   → auto
5. Sales history prob       → intelligent default
6. Disambiguation (rare)    → last resort, not first
```

---

### Elevation 3: Customer Identity Network

```
Rahul buys Antivirus at XYZ Pharmacy (Atlas shop A)
Rahul buys Panadol at ABC Medical (Atlas shop B)

Both shops now know:
- Rahul's verified phone: 9876543210
- His cross-shop purchase history
- His GST number (if B2B, supplied once)
- His preferred payment method

Next time any Atlas shop serves Rahul:
- Staff types "rahul" → "Rahul Sharma 9876543210 (5 past purchases)"
- Invoice pre-fills his GSTIN if B2B
- "Rahul usually pays UPI" → payment auto-suggested
```

**Data model:**
```sql
CREATE TABLE wa_customers (
  id                uuid PRIMARY KEY,
  phone             varchar(20) UNIQUE NOT NULL,  -- THE identity key
  name              varchar(200),
  gstin             varchar(20),
  preferred_payment varchar(20),
  opt_in_marketing  boolean DEFAULT true,
  created_at        timestamptz DEFAULT now()
);

CREATE TABLE wa_customer_purchases (
  id          uuid PRIMARY KEY,
  customer_id uuid REFERENCES wa_customers(id),
  tenant_id   uuid NOT NULL,     -- which shop
  sale_id     uuid NOT NULL,
  amount      numeric,
  created_at  timestamptz DEFAULT now()
);
```

> Privacy: customers text "STOP" to opt out. DPDP/GDPR compliant. No cross-shop data shared with sellers — Atlas uses it only to improve resolution speed.

---

### Elevation 4: Credit Sale → Payment Collection Loop

The credit sale problem is where most small shops lose money. Atlas closes the loop automatically.

```
Staff: "AV-1999 x2, Rahul 9876543210, credit"
                    ↓
Sale created, payment_status = 'pending'
                    ↓
Customer Rahul receives:
  "🧾 Invoice from XYZ Pharmacy
   Antivirus Elite × 2  ₹3,998
   Due: ₹3,998
   [Pay Now — UPI QR]
   [Pay via Link]"
                    ↓
Rahul pays via UPI QR or link
                    ↓
Payment webhook hits Atlas (Razorpay/Cashfree)
                    ↓
sale.payment_status = 'paid'
                    ↓
Staff: "✅ Rahul paid ₹3,998 for invoice #1042"
Rahul: "✅ Payment confirmed. Receipt: [link]"
```

**Automated reminder if unpaid (T+3 days):**
```
Atlas → Rahul:
"Hi Rahul, friendly reminder from XYZ Pharmacy.
 ₹3,998 due for Antivirus Elite purchased on 3 Jul.
 [Pay Now]  [Contact Shop]"
```

Seller never chases manually. Atlas chases for them.

---

### Elevation 5: Proactive Intelligence (System → Seller)

The system talks to the seller proactively.

```
LOW STOCK:
"⚠️ Antivirus Elite: 2 units left.
 You sell ~3/week. You'll run out by Sunday.
 [Reorder from last supplier]  [Mark as Ordered]"

PAYMENT DUE:
"💰 5 credit sales unpaid (₹12,450 total).
 Oldest: Ramesh Medical, 7 days overdue.
 [Send reminders to all]  [View list]"

DAILY SUMMARY (7 PM):
"📊 Today's sales: ₹24,350
 Top product: Antivirus Elite (7 units)
 Staff: Priya 12 sales | Suresh 8 sales
 Credit outstanding: ₹4,200"

WEEKLY SMART INSIGHT:
"📈 Panadol 500mg sales ↑40% this week.
 Stock: 23 units. At this rate, 8 days left.
 Last order was 14 days ago from Sharma Distributors."
```

All via WhatsApp. No app to open, no dashboard to check.

---

### Elevation 6: Return Flow

```
Staff: "return AV-1999, Rahul 9876543210"
                    ↓
System: look up last sale of Antivirus Elite to 9876543210
        Found: Invoice #1042, 2 days ago, ₹3,998
                    ↓
Atlas → Staff: "Return for Rahul: Antivirus Elite ×2 ₹3,998?
               Reply 1 to confirm | 2 to cancel"
                    ↓
Staff: "1"
                    ↓
Return created, stock restored, refund recorded
Rahul: "✅ Return accepted. ₹3,998 will be refunded. Ref: RTN-042"
```

---

### Elevation 7: Manager Layer

Manager/owner gets a separate command set with elevated permissions:

```
"team"    → team sales leaderboard today
"sales"   → today's revenue, top products
"pending" → all unpaid credit sales
"stock"   → low stock alerts list
"priya"   → Priya's sales today (staff name lookup)
"report"  → weekly PDF report — generated and sent
```

---

### Complete Elevated Data Flow

```
INBOUND MESSAGES
      │
      ├─ Staff voice note  → Whisper → text
      ├─ Staff text        → direct
      └─ Customer text     → customer service handler
      ↓
IDENTITY RESOLUTION
      ├─ findStaffByPhone()    → employee + tenant
      └─ Manager check?        → elevated command set
      ↓
INTENT DETECTION
      ├─ "alias X = Y"         → wa_staff_aliases update
      ├─ "return ..."          → return flow
      ├─ "stock ..."           → stock query
      ├─ "my sales / team ..." → analytics query
      └─ everything else       → sale parse
      ↓
PRODUCT RESOLUTION (zero-friction hierarchy)
      1. Personal alias
      2. Sell code
      3. Name + price hint
      4. Name, unique
      5. History probability
      6. Disambiguation (rare)
      ↓
TRANSACTION
      ├─ createSale()
      ├─ stock deducted
      └─ payment_status: paid | pending
      ↓
OUTBOUND (parallel)
      ├─ Staff confirmation: "✅ Done. ₹X. Invoice sent."
      ├─ Customer invoice: WhatsApp message + QR + portal link
      └─ If credit: payment reminder scheduled (T+3 days)
```

---

## Part 2: WhatsApp Flows — Per-Tenant Native UI

### The Fundamental Shift

```
Text path:  "AV-1999 x2, Rahul 9876543210, upi"
            → NLP parse → sell code lookup → sale

Flow path:  Staff taps "New Sale"
            → Native WhatsApp UI opens (no browser, no app)
            → Staff picks products, qty, customer, payment
            → Submit → structured JSON arrives at Atlas
            → Zero parsing. Zero ambiguity. Zero error.
```

Flows coexist with text — text path for power users, flow path for everyone else.

---

### Two Numbers. Non-Negotiable.

**ATLAS NUMBER** handles everything seller-facing.  
**TENANT'S OWN WABA** handles everything customer-facing. Always. No exceptions.

```
┌─────────────────────────────────────────────────────────────┐
│         ATLAS NUMBER  (one, permanent, seller-only)          │
│                                                             │
│  ├── Staff sale messages, voice notes, stock queries        │
│  ├── Staff aliases, quick card, onboarding flow             │
│  ├── Owner daily summary, low stock alerts, dashboard flow  │
│  ├── Manager commands (team, sales, pending, stock)         │
│  └── Supplier reorder flows, PO confirmations               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│     TENANT'S OWN WABA  (per-tenant, Embedded Signup)        │
│                     CUSTOMER INTERACTIONS ONLY              │
│                                                             │
│  ├── Invoice FROM "XYZ Pharmacy"     → customer trusts it   │
│  ├── Customer replies TO "XYZ Pharmacy" → correct context   │
│  ├── Catalog browse flow on XYZ's number                    │
│  ├── Customer places order → staff notified on Atlas        │
│  ├── Payment QR from XYZ Pharmacy    → customer pays        │
│  └── Credit reminder from "XYZ Pharmacy" → not ignored      │
└─────────────────────────────────────────────────────────────┘
```

Customer never sees Atlas. Every customer touchpoint is the shop's own identity.

**Astra Spark is already a Meta Tech Provider with Embedded Signup ready.**  
Tenant connects their existing WhatsApp Business number in 3 minutes.  
Coexistence enabled — they keep chatting manually on the same number, Atlas adds the automated layer on top.

---

### Tenant Onboarding — WhatsApp Setup

```
Tenant signs up on Astra
        ↓
Onboarding step: "Connect your WhatsApp Business number"
        ↓
Spark's Embedded Signup opens (built, ready to use)
        ↓
Tenant authenticates with Meta (~3 minutes)
        ↓
Atlas stores: waba_id, phone_number_id → tenant_settings
        ↓
Coexistence auto-enabled — no disruption to existing usage
        ↓
Atlas registers flow templates under tenant's WABA
Customer-facing messages now go from tenant's own number
```

---

### Tier-Based WhatsApp Capability

| Tier | Staff (Atlas #) | Customer (Own WABA) |
|---|---|---|
| **STARTER** | Sale recording, stock queries, alerts | Invoice as web link only (no WA delivery yet) |
| **GROWTH** | + Voice notes, aliases, onboarding flow | Invoice via WA from shop's number, standard flows |
| **PRO** | + Manager layer, dashboard flow, reorder | Catalog browse flow, payment collection, credit reminders |
| **ENTERPRISE** | + Multi-location, custom commands | Multi-location WABAs, custom flow screens, supplier network |

---

### The 6 Flows Per Tenant

---

#### Flow 1: Staff Sale Flow

**Trigger:** Staff opens chat → taps "New Sale" quick reply

```
Screen 1: PRODUCT SEARCH
┌─────────────────────────────┐
│  🛒 New Sale                 │
│  XYZ Pharmacy               │
│  Search product:            │
│  [________________]         │
│  Or browse:                 │
│  ● Medicines                │
│  ● Electronics  ● FMCG      │
└─────────────────────────────┘

Screen 2: PRODUCT LIST (dynamic — served from Atlas)
┌─────────────────────────────┐
│  Results for "antivirus"    │
│  ○ Antivirus Elite  ₹1,999 │
│    SKU: AV-1999 | 14 left  │
│  ○ Antivirus Basic  ₹999   │
│    SKU: AV-999  | 6 left   │
└─────────────────────────────┘

Screen 3: QUANTITY + CUSTOMER
┌─────────────────────────────┐
│  Antivirus Elite ₹1,999    │
│  Quantity: [─] 2 [+]        │
│  Total: ₹3,998              │
│  Customer phone (optional): │
│  [________________]         │
│  Add more products? ○ Yes   │
└─────────────────────────────┘

Screen 4: PAYMENT + CONFIRM
┌─────────────────────────────┐
│  Order Summary              │
│  Antivirus Elite ×2  ₹3,998│
│  Total: ₹3,998              │
│  Payment:                   │
│  ● Cash ○ UPI ○ Card ○ Credit│
│  [    Confirm Sale    ]      │
└─────────────────────────────┘
```

---

#### Flow 2: Customer Invoice Flow

**Trigger:** Customer receives invoice → taps "View Invoice"

```
Screen 1: INVOICE DETAIL
┌─────────────────────────────┐
│  🧾 XYZ Pharmacy            │
│  GSTIN: 27XXXXX             │
│  Invoice #1042 · 3 Jul 2026 │
│  Antivirus Elite ×2  ₹3,998│
│  Taxable: ₹3,388            │
│  GST 18%:   ₹610            │
│  Total:    ₹3,998            │
│  Status: ⏳ Payment Pending  │
└─────────────────────────────┘

Screen 2: PAYMENT
┌─────────────────────────────┐
│  Pay ₹3,998                 │
│  [  Pay via UPI QR  ]       │
│  [  Pay via UPI ID  ]       │
│  [  I've already paid ]     │
│  UPI ID: xyz@paytm          │
└─────────────────────────────┘

Screen 3: CONFIRMATION
┌─────────────────────────────┐
│  ✅ Payment Noted           │
│  Shop will confirm receipt. │
│  [  Download PDF Receipt ]  │
│  [  Contact Shop       ]    │
└─────────────────────────────┘
```

---

#### Flow 3: Customer Catalog Browse + Order

**Trigger:** Customer texts "browse" or shop shares catalog

```
Screen 1: CATEGORY
┌─────────────────────────────┐
│  🏪 XYZ Pharmacy            │
│  ● Medicines                │
│  ● Vitamins & Supplements   │
│  ● Personal Care            │
│  [Search by name]           │
└─────────────────────────────┘

Screen 2: PRODUCT LIST (dynamic, paginated)
┌─────────────────────────────┐
│  □ Panadol 500mg   ₹5      │
│    □ 1  □ 2  □ 5  □ 10    │
│  □ Antivirus Elite ₹1,999  │
│    □ 1  □ 2  □ 5           │
│  [ View Cart (0) → ]        │
└─────────────────────────────┘

Screen 3: CART + DELIVERY
┌─────────────────────────────┐
│  Panadol ×2         ₹10    │
│  Antivirus Elite ×1 ₹1,999 │
│  Total: ₹2,009              │
│  ● Pickup  ○ Delivery       │
│  [   Place Order   ]        │
└─────────────────────────────┘
```

Customer order → staff gets WhatsApp notification → staff confirms → customer gets update.

---

#### Flow 4: Owner Dashboard Flow

**Trigger:** Owner texts "stats" or taps button in daily summary

```
Screen 1: TODAY SNAPSHOT
┌─────────────────────────────┐
│  📊 3 Jul 2026 — Live       │
│  Revenue:     ₹24,350       │
│  Sales count: 47            │
│  Cash: ₹12,000  UPI: ₹8,350│
│  Credit: ₹4,000 ⚠️          │
│  [Staff] [Products] [Credit]│
└─────────────────────────────┘

Screen 2: STAFF LEADERBOARD
┌─────────────────────────────┐
│  🥇 Priya    ₹11,200 / 22  │
│  🥈 Suresh   ₹8,750  / 18  │
│  🥉 Anil     ₹4,400  / 7   │
│  [Send team summary]        │
└─────────────────────────────┘

Screen 3: PENDING CREDIT
┌─────────────────────────────┐
│  Ramesh Medical  ₹2,500     │
│  Last reminded: 3 days ago  │
│  Rahul Sharma    ₹1,500     │
│  Last reminded: Today       │
│  [Remind All]  [View All]   │
└─────────────────────────────┘
```

---

#### Flow 5: Staff Onboarding Flow

**Trigger:** New staff first texts shop's number

```
Screen 1: WELCOME + SETUP
┌─────────────────────────────┐
│  👋 Welcome to XYZ Pharmacy │
│  Your name: [____________]  │
│  Role: ● Staff ○ Manager    │
└─────────────────────────────┘

Screen 2: VERIFY (4-digit code from manager)
┌─────────────────────────────┐
│  [  ] [  ] [  ] [  ]       │
│  Ask manager: Atlas → Team  │
│  → Add Staff → Get Code     │
└─────────────────────────────┘

Screen 3: QUICK CARD SENT
┌─────────────────────────────┐
│  ✅ You're set up, Priya!   │
│  Your product quick-codes   │
│  have been sent below.      │
│  [  New Sale  ]             │
└─────────────────────────────┘
```

---

#### Flow 6: Supplier Reorder Flow

**Trigger:** System detects low stock → alert with "Reorder" button

```
Screen 1: LOW STOCK ALERT
┌─────────────────────────────┐
│  ⚠️ Antivirus Elite: 2 left │
│  You sell ~3/week           │
│  Run out: ~Sunday           │
│  Last: Sharma Dist. ₹1,600  │
│  [  Reorder Now  ]          │
└─────────────────────────────┘

Screen 2: ORDER FORM
┌─────────────────────────────┐
│  Order from Sharma Dist.    │
│  Qty: [─] 10 [+]            │
│  Est. cost: ₹16,000         │
│  ● Shop address (default)   │
│  [  Send Order  ]           │
└─────────────────────────────┘

Screen 3: SENT
┌─────────────────────────────┐
│  ✅ Order Sent              │
│  Sharma Distributors        │
│  notified via WhatsApp.     │
│  Expected: 2 days           │
│  Ref: PO-2026-047           │
└─────────────────────────────┘
```

Supplier also receives a WhatsApp message with order details. Full supply chain on WhatsApp.

---

### Dynamic Flow Data — Technical Core

Meta calls Atlas at flow render time to inject tenant-specific data:

```
┌──────────────┐  1. Staff opens flow   ┌──────────────┐
│  WhatsApp    │ ─────────────────────▶ │    META      │
│  (Staff)     │                        │  Flow Engine │
└──────────────┘                        └──────┬───────┘
                                               │ 2. Request data
                                               │ POST /api/wa/flows/data
                                        ┌──────▼───────┐
                                        │    ATLAS      │
                                        │ Reads tenant  │
                                        │ wa_catalog    │
                                        │ Returns JSON  │
                                        └──────┬───────┘
                                               │ 3. Tenant's products
                                        ┌──────▼───────┐
                                        │ Flow renders  │
                                        │ with XYZ's   │
                                        │ products      │
                                        └──────────────┘
```

**One flow template → all tenants → each sees their own data.**

```typescript
// Atlas dynamic data endpoint
// POST /api/wa/flows/data
// Request:
{
  flow_token: "eyJ...",        // encodes tenant_id + flow_type
  screen: "PRODUCT_LIST",
  action: "SEARCH",
  data: { query: "antivirus" }
}

// Atlas response:
{
  screen: "PRODUCT_LIST",
  data: {
    products: [
      { id: "uuid", name: "Antivirus Elite", price: 1999, stock: 14, sell_code: "AV-1999" },
      { id: "uuid", name: "Antivirus Basic",  price: 999,  stock: 6,  sell_code: "AV-999"  }
    ]
  }
}
```

---

### Three Input Modalities, One Backend

```
STAFF POWER USER  → Text:  "AV-1999 x2, rahul 9876543210, upi"
STAFF NORMAL      → Flow:  tap through 4 screens, submit
STAFF VOICE       → Voice: "do antivirus, rahul ko, UPI"

CUSTOMER ORDER    → Flow:  browse catalog, add to cart, checkout
CUSTOMER INVOICE  → Flow:  view invoice, tap to pay

OWNER             → Flow:  daily stats, credit, staff leaderboard
REORDER           → Flow:  low stock alert, tap to reorder supplier
```

All three arrive at Atlas as structured data. Same transaction layer handles all.

---

## New Data Models Summary

```sql
-- WhatsApp-ready catalog snapshot per tenant
CREATE TABLE wa_catalog (
  id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id      uuid NOT NULL REFERENCES tenants(id),
  product_id     uuid NOT NULL REFERENCES products(id),
  sell_code      varchar(20) NOT NULL,        -- "AV-1999"
  conflict_group varchar(100),                -- non-null if same name exists
  created_at     timestamptz DEFAULT now(),
  UNIQUE (tenant_id, sell_code)
);

-- Staff personal shorthand per product
CREATE TABLE wa_staff_aliases (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id   uuid NOT NULL,
  employee_id uuid NOT NULL,
  alias       varchar(20) NOT NULL,           -- "av"
  product_id  uuid NOT NULL,
  created_at  timestamptz DEFAULT now(),
  UNIQUE (tenant_id, employee_id, alias)
);

-- Cross-shop customer identity
CREATE TABLE wa_customers (
  id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  phone             varchar(20) UNIQUE NOT NULL,
  name              varchar(200),
  gstin             varchar(20),
  preferred_payment varchar(20),
  opt_in_marketing  boolean DEFAULT true,
  created_at        timestamptz DEFAULT now()
);

-- Customer purchase history (cross-shop)
CREATE TABLE wa_customer_purchases (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id uuid REFERENCES wa_customers(id),
  tenant_id   uuid NOT NULL,
  sale_id     uuid NOT NULL REFERENCES sales(id),
  amount      numeric,
  created_at  timestamptz DEFAULT now()
);

-- Invoice delivery tracking
CREATE TABLE wa_invoices_sent (
  id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id      uuid NOT NULL,
  sale_id        uuid NOT NULL REFERENCES sales(id),
  customer_phone varchar(20) NOT NULL,
  sent_at        timestamptz DEFAULT now(),
  status         varchar(20) DEFAULT 'sent'   -- sent | delivered | failed
);

-- Tenant WhatsApp settings
ALTER TABLE tenant_settings
  ADD COLUMN IF NOT EXISTS upi_qr_url            text,
  ADD COLUMN IF NOT EXISTS wa_invoice_header      text,
  ADD COLUMN IF NOT EXISTS wa_catalog_synced_at   timestamptz,
  ADD COLUMN IF NOT EXISTS waba_id                text,   -- per-tenant WhatsApp Business Account
  ADD COLUMN IF NOT EXISTS wa_phone_number_id     text;   -- per-tenant phone number ID
```

---

## Build Roadmap

### Infrastructure Status
```
✓ Meta Tech Provider verified (Astra Spark)
✓ Embedded Signup built and ready (Spark)
✓ Coexistence enabled
✓ App Review submitted — waiting approval
✓ Atlas backend always-on (Render paid plan)
✓ Basic WA POS working (text sale → confirm → createSale)
✓ AWAITING_DISAMBIGUATION built
✓ pgvector semantic search working
```

---

### Phase 0 — Tenant WABA Onboarding
*Connects Spark's Embedded Signup to Atlas. Unlocks all customer-facing features.*

```
What Spark does:
  Tenant clicks "Connect WhatsApp" in Spark
  Meta OAuth popup opens (Spark handles entirely)
  Tenant selects their WhatsApp Business Account
  Meta returns: { waba_id, phone_number_id, access_token }
  Spark calls Atlas:
    POST /api/tenant/wa/connect
    Authorization: Bearer {tenant JWT}
    { waba_id, phone_number_id, access_token }

What Atlas builds:
  POST /api/tenant/wa/connect endpoint
    → verify JWT → extract tenant_id
    → store waba_id + phone_number_id + access_token in tenant_settings
    → return { success: true }

  sendFromTenantWABA(tenantId, to, message)
    → reads credentials from tenant_settings
    → POST graph.facebook.com/v20.0/{phone_number_id}/messages
    → message arrives FROM tenant's own number

No shared DB between Spark and Atlas. One API call is the entire integration.
```

**Done when:** Tenant connects their WhatsApp in settings, customer invoice goes from shop's own number.

---

### Phase 1 — Catalog Foundation
*Eliminates the same-name ambiguity problem at source. Staff never guesses wrong product again.*

```
wa_catalog table:
  product_id, tenant_id, sell_code, conflict_group

syncProductToWACatalog()
  → runs on every product save/update/delete
  → detects conflicts: same display name, different price/id
  → auto-generates sell codes: "AV-999", "AV-1999"
  → notifies seller on WhatsApp when conflict detected:
     "⚠️ You have 2 products named 'Antivirus':
      AV-999  → Antivirus Basic  ₹999
      AV-1999 → Antivirus Elite  ₹1999
      Staff can sell by code: 'AV-1999 x1, Rahul'"

Staff Quick Card (sent on first sale):
  Top 20 products with sell codes, grouped by category
  Re-sent when new conflict product added
```

**Done when:** Staff types "AV-1999 x2" → resolves instantly, zero ambiguity.

---

### Phase 2 — Smart Resolution
*Replaces current single-attempt matchProducts with 6-tier hierarchy.*

```
resolveProducts() hierarchy:
  1. Personal alias lookup    → wa_staff_aliases table (Phase 3 builds this)
  2. Sell code exact match    → wa_catalog lookup
  3. Name + price hint        → extract price from message → filter
     e.g. "antivirus 1999" → name match + price ≈ 1999 → one result
  4. Exact name, one result   → existing vector search, auto-select
  5. Sales history prob       → sale_items JOIN employees
     → which of the ambiguous products does this staff sell most?
     → pick highest frequency, flag as "auto-resolved" in sale record
  6. Disambiguation           → existing flow, now fires only as last resort

No new tables for tiers 2–5. Uses wa_catalog + existing sale_items.
```

**Done when:** 95%+ of sales resolve without any back-and-forth.

---

### Phase 3 — Voice Notes + Staff Aliases
*India-first. Staff don't need to type. Power users get personal shortcuts.*

```
Voice notes:
  Detect audio message type in webhook handler
  Download audio from Meta → whisperTranscribe(audioUrl)
  OpenAI Whisper API → transcript text
  Feed into existing NLP pipeline → same sale flow
  Language auto-detected: Hindi, Hinglish, Tamil, any Indian language

Staff aliases:
  wa_staff_aliases table:
    tenant_id, employee_id, alias (varchar 20), product_id

  Intent: "alias av = Antivirus Elite 1999"
    → parse → lookup product → store alias
  Intent: "remove alias av" → delete
  Intent: "aliases" → list all personal shortcuts
  Plugs into Phase 2 hierarchy as tier 1 (fastest resolution)
```

**Done when:** "दो एंटीवायरस, राहुल को, UPI" via voice note → sale recorded. "av x2" → instant.

---

### Phase 4 — Customer Invoice
*First customer-facing feature. Invoice from shop's own number.*

```
Parse customer phone from sale message:
  NLP already extracts customer_name
  Add phone extraction: "Rahul 9876543210" → name + phone
  Phone optional — if missing, no invoice sent

wa_customers table:
  phone (unique), name, gstin, preferred_payment, opt_in_marketing

wa_invoices_sent table:
  tenant_id, sale_id, customer_phone, sent_at, status

Invoice WhatsApp template:
  Submit to Meta for approval (required for outbound messages)
  Template: shop name, invoice number, items, total, GST, payment status
  UPI QR image / UPI ID from tenant_settings

Staff confirmation after sale:
  "✅ Done. ₹3,998. Invoice sent to Rahul (+91 98765 43210)"
```

**Done when:** Staff includes customer phone → customer gets WhatsApp invoice from "XYZ Pharmacy."

---

### Phase 5 — WhatsApp Flows
*Native UI inside WhatsApp. Zero text parsing. Requires App Review approval.*

```
Dynamic data endpoint:
  POST /api/wa/flows/data
  { flow_token, screen, action, data }
  → decode flow_token → tenant_id + context
  → return tenant-specific data (products, invoice, etc.)
  One endpoint serves all tenants, all flows.

Flow 1: Staff Sale Flow (4 screens)
  Screen 1: Product search + category browse
  Screen 2: Product list (dynamic from wa_catalog)
  Screen 3: Quantity + customer phone
  Screen 4: Payment method + confirm
  → Structured JSON arrives at Atlas → same createSale() path

Flow 2: Customer Invoice Flow (3 screens)
  Screen 1: Invoice detail (items, GST, total, status)
  Screen 2: Payment options (UPI QR, UPI ID, "already paid")
  Screen 3: Confirmation + download receipt link
  → Served from tenant's own WABA

Flow 3: Customer Catalog Browse (3 screens)
  Screen 1: Category selection
  Screen 2: Product list with quantity picker (dynamic)
  Screen 3: Cart + pickup/delivery preference
  → Customer order → staff notified on Atlas number

Register each flow under tenant's WABA via Flows API on onboarding.
```

**Done when:** Staff taps "New Sale" → native WA UI → sale. Customer taps "View Invoice" → native WA UI → pay.

---

### Phase 6 — Credit Payment Loop
*Shops stop losing money to unpaid credit. Automated collections.*

```
Credit sale flow:
  Staff: "AV-1999 x2, Rahul 9876543210, credit"
  → sale created, payment_status = 'pending'
  → generate Razorpay/Cashfree payment link
  → customer invoice includes [Pay Now] button + UPI QR
  → customer pays → payment webhook → sale.payment_status = 'paid'
  → staff notified: "✅ Rahul paid ₹3,998 for invoice #1042"
  → customer gets: "✅ Payment confirmed. Receipt: [link]"

wa_payment_reminders table:
  sale_id, customer_phone, scheduled_at, sent_at, status

Reminder scheduler:
  T+3 days unpaid → WhatsApp reminder to customer from tenant's number
  T+7 days unpaid → second reminder
  T+14 days → owner notified: "Ramesh Medical ₹2,500 overdue 14 days"
```

**Done when:** Credit sale auto-collects without seller manually chasing.

---

### Phase 7 — Manager Layer + Proactive Alerts
*Business runs itself. Owner never needs to open Atlas desktop.*

```
Owner command set (texts Atlas number):
  "team"    → staff leaderboard today
  "sales"   → revenue, top products, payment breakdown
  "pending" → all unpaid credit sales with amounts
  "stock"   → low stock items list
  "priya"   → specific staff member's sales today
  "report"  → triggers weekly PDF → sent to owner's WhatsApp

Proactive alerts (system-initiated):
  Low stock: when product hits reorder_level
    "⚠️ Antivirus Elite: 2 left. ~3/week sold. Run out Sunday.
     [Reorder from Sharma Dist.]  [Mark as Ordered]"

  Daily summary: 7 PM cron
    "📊 Today: ₹24,350 · 47 sales
     Top: Antivirus Elite (7 units)
     Staff: Priya 12 | Suresh 8
     Credit outstanding: ₹4,200"

  Weekly insight: Monday 9 AM
    "📈 Panadol 500mg ↑40% this week.
     Stock: 23 units, ~8 days left.
     Last ordered 14 days ago."

Flow 4: Owner Dashboard Flow
  Today snapshot → staff leaderboard → pending credit

Flow 6: Supplier Reorder Flow
  Low stock alert button → order form → send to supplier WA
```

**Done when:** Owner gets daily summary without opening app. Low stock never surprises them.

---

### Phase 8 — Full Lifecycle
*Return flow, staff onboarding, cross-shop customer identity.*

```
Return flow:
  "return AV-1999, Rahul 9876543210"
  → lookup last sale of that product to that phone
  → "Return for Rahul: Antivirus Elite ×2 ₹3,998 (2 days ago)? 1/2"
  → confirm → return created, stock restored, refund recorded
  → customer notified: "✅ Return accepted. ₹3,998 refunded. RTN-042"

Staff Onboarding Flow (Flow 5):
  New staff texts Atlas number
  Welcome screen → name + role → 4-digit manager code → verified
  Quick Card sent immediately

Cross-shop customer identity:
  wa_customer_purchases table (customer_id, tenant_id, sale_id)
  Customer Rahul buys from shop A + shop B → full history in Atlas
  Any Atlas shop sees: "Rahul (5 purchases, prefers UPI)"
  Customer texts "STOP" → opt_in_marketing = false (DPDP compliant)
  Customer context routing: fresh inbound → recent shops → pick one
```

**Done when:** Full transaction lifecycle covered. Customer identity works across network.

---

### Priority Order

```
Phase 0  → Tenant WABA onboarding       FOUNDATION — unblocks customer features
Phase 1  → Catalog + sell codes         FIXES the original bug
Phase 2  → Smart resolution             MAKES text selling frictionless
Phase 3  → Voice + aliases              INDIA-FIRST, high adoption impact
Phase 4  → Customer invoice             FIRST visible customer value
Phase 5  → WhatsApp Flows               PREMIUM UX (needs App Review live)
Phase 6  → Credit payment loop          DIRECT revenue impact for tenants
Phase 7  → Manager layer + alerts       STICKINESS — owner never churns
Phase 8  → Full lifecycle               COMPLETE product
```

---

## What This Becomes

This is no longer a POS over WhatsApp. This is **the operating system for Indian small retail, running entirely inside an app 500 million people already have open all day.**

| Capability | Impact |
|---|---|
| Sell codes + aliases | Zero-friction, zero-ambiguity product resolution |
| Voice notes | Staff don't need to type — India-native |
| Per-tenant flows | Each shop has its own branded WhatsApp experience |
| Dynamic flow data | One template scales to 10,000 tenants instantly |
| Customer phone as identity | Network-wide purchase history — no traditional POS has this |
| Credit → payment loop | Automated collections — shops stop losing money to credit |
| Proactive alerts | Business runs itself from WhatsApp |
| Full lifecycle | Sell, reorder, return, collect — entire operation in one chat |

No app to install. No training required. No computer needed.
