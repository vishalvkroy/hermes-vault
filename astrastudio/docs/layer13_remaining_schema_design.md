# Layer 13 — Remaining Schema Design

## What Already Exists (NOT touched)

- `plans` table with TRIAL/BASIC/STANDARD/ENTERPRISE
- `subscriptions` table with billing cycles
- `usage_counters` table with period-based tracking
- `devices` table with device_id, is_active, last_seen_at
- `payment_records` table with provider integration
- `tenants.tenant_state` column (TRIAL/ACTIVE/SUSPENDED/READ_ONLY/TERMINATED)
- `users.role` column (owner/admin/manager/staff)

---

## Migration 009: RBAC + Admin Audit + Webhook Logs

### 1. `roles` Table — Granular Permission Definitions

```sql
CREATE TABLE IF NOT EXISTS roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
    -- tenant_id NULL = system-defined role (Owner, Manager, Cashier, etc.)
    -- tenant_id NOT NULL = custom role created by tenant

    name VARCHAR(50) NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    description TEXT,

    -- Permissions as JSONB array
    permissions JSONB NOT NULL DEFAULT '[]',
    -- Example: ["pos:access", "inventory:read", "inventory:write",
    --           "reports:access", "reports:export", "atlas_ai:access",
    --           "settings:access", "employees:manage", "returns:approve"]

    is_system BOOLEAN NOT NULL DEFAULT false,  -- System roles can't be deleted
    is_active BOOLEAN NOT NULL DEFAULT true,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT roles_name_tenant_unique UNIQUE (tenant_id, name)
);
```

**Why JSONB permissions instead of a permissions table?**
- Simpler queries (no JOINs for auth checks)
- Permissions are a flat list, not hierarchical
- Easier to compare/diff between roles
- Aligns with JWT claims pattern

**Seeded System Roles:**

| Role | Permissions |
|------|-------------|
| OWNER | ALL permissions |
| MANAGER | pos, inventory:*, reports, employees:read, returns:approve |
| CASHIER | pos, inventory:read |
| ACCOUNTANT | reports:*, inventory:read |

### 2. `user_roles` Table — Role Assignment

```sql
CREATE TABLE IF NOT EXISTS user_roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,

    assigned_by UUID REFERENCES users(id),
    assigned_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT user_roles_unique UNIQUE (user_id, role_id)
);
```

**Design decision**: Users keep `users.role` VARCHAR as the legacy/simple field. `user_roles` is the new RBAC system. During transition, both are checked — if `user_roles` exists, it takes precedence.

### 3. `subscription_audit_log` Table — Tracks Every State Change

```sql
CREATE TABLE IF NOT EXISTS subscription_audit_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    subscription_id UUID REFERENCES subscriptions(id),

    event_type VARCHAR(50) NOT NULL,
    -- Events: CREATED, PLAN_CHANGED, ACTIVATED, SUSPENDED,
    --         CANCELLED, RENEWED, TRIAL_EXPIRED, STATE_CHANGED,
    --         LIMIT_OVERRIDDEN

    -- What changed
    previous_state JSONB,  -- { plan: "TRIAL", status: "ACTIVE" }
    new_state JSONB,       -- { plan: "BASIC", status: "ACTIVE" }

    -- Who did it
    performed_by UUID REFERENCES users(id),  -- NULL = system/automated
    performed_by_type VARCHAR(20) NOT NULL DEFAULT 'SYSTEM',
    -- SYSTEM, ADMIN, USER, WEBHOOK

    -- Context
    reason TEXT,
    metadata JSONB,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### 4. `webhook_events` Table — Payment Webhook Log

```sql
CREATE TABLE IF NOT EXISTS webhook_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Provider info
    provider VARCHAR(50) NOT NULL,  -- razorpay, stripe
    event_type VARCHAR(100) NOT NULL,  -- payment.captured, subscription.charged
    event_id VARCHAR(255),  -- Provider's event ID (for idempotency)

    -- Raw payload
    payload JSONB NOT NULL,

    -- Processing
    status VARCHAR(20) NOT NULL DEFAULT 'RECEIVED',
    -- RECEIVED, PROCESSING, PROCESSED, FAILED, IGNORED
    processed_at TIMESTAMPTZ,
    error_message TEXT,

    -- Tenant mapping (resolved during processing)
    tenant_id UUID REFERENCES tenants(id),

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT webhook_events_idempotent UNIQUE (provider, event_id)
);
```

### 5. `admin_overrides` Table — Manual Limit Overrides

```sql
CREATE TABLE IF NOT EXISTS admin_overrides (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,

    -- What's being overridden
    override_type VARCHAR(50) NOT NULL,
    -- PRODUCT_LIMIT, AI_QUERY_LIMIT, EXPORT_LIMIT, DEVICE_LIMIT,
    -- TRIAL_EXTENSION, FEATURE_FLAG

    -- Override value
    override_value JSONB NOT NULL,
    -- Examples:
    -- { "max_products": 200 }  (override product limit)
    -- { "trial_end": "2026-04-01" }  (extend trial)
    -- { "atlas_ai": true }  (enable AI for free plan)

    -- Validity
    effective_from TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    effective_until TIMESTAMPTZ,  -- NULL = permanent

    -- Who authorized
    created_by VARCHAR(100) NOT NULL,  -- Admin email or "SYSTEM"
    reason TEXT NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT true,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT admin_overrides_unique UNIQUE (tenant_id, override_type)
);
```

---

## Indexes Summary

```sql
-- Roles
CREATE INDEX idx_roles_tenant ON roles(tenant_id) WHERE is_active = true;
CREATE INDEX idx_roles_system ON roles(id) WHERE is_system = true AND is_active = true;

-- User Roles
CREATE INDEX idx_user_roles_user ON user_roles(user_id);
CREATE INDEX idx_user_roles_tenant ON user_roles(tenant_id);

-- Subscription Audit Log
CREATE INDEX idx_sub_audit_tenant ON subscription_audit_log(tenant_id);
CREATE INDEX idx_sub_audit_event ON subscription_audit_log(event_type);
CREATE INDEX idx_sub_audit_created ON subscription_audit_log(created_at);

-- Webhook Events
CREATE INDEX idx_webhook_status ON webhook_events(status) WHERE status != 'PROCESSED';
CREATE INDEX idx_webhook_tenant ON webhook_events(tenant_id);
CREATE INDEX idx_webhook_created ON webhook_events(created_at);

-- Admin Overrides
CREATE INDEX idx_overrides_tenant ON admin_overrides(tenant_id) WHERE is_active = true;
CREATE INDEX idx_overrides_type ON admin_overrides(tenant_id, override_type) WHERE is_active = true;
```

---

## Permission Definitions

These are the granular permissions stored in `roles.permissions` JSONB:

```
pos:access          — Can use POS screen
inventory:read      — Can view inventory
inventory:write     — Can add/edit products, adjust stock
purchases:read      — Can view purchases
purchases:write     — Can create/edit purchase orders
returns:read        — Can view returns
returns:write       — Can initiate returns
returns:approve     — Can approve returns
reports:access      — Can view reports
reports:export      — Can export CSV/PDF
atlas_ai:access     — Can use Atlas AI
employees:read      — Can view employees
employees:manage    — Can add/edit/remove employees
settings:access     — Can view/edit settings
settings:billing    — Can manage subscription/billing
admin:tenant_manage — Internal admin: manage tenants
admin:override      — Internal admin: override limits
```

---

## What This Schema Does NOT Change

- `plans` table — UNCHANGED
- `subscriptions` table — UNCHANGED
- `usage_counters` table — UNCHANGED
- `devices` table — UNCHANGED
- `payment_records` table — UNCHANGED
- Stock engine — NEVER TOUCHED
- Business services — NEVER TOUCHED
- Ledger invariants — NEVER TOUCHED

---

## Enforcement Points (Code Changes After Schema Approval)

### Backend (New Files)
1. `deviceRepository.ts` — CRUD for devices table
2. `roleRepository.ts` — CRUD for roles + user_roles
3. `webhookLogRepository.ts` — Webhook event logging
4. `adminOverrideRepository.ts` — Override management
5. `deviceService.ts` — Registration, fingerprint validation, limit check
6. `rbacMiddleware.ts` — Route-level permission checking
7. `adminRoutes.ts` — Internal admin API endpoints
8. `deviceRoutes.ts` — Device registration + listing
9. `webhookRoutes.ts` — Payment webhook handler

### Backend (Modified Files)
1. `tenantAccessService.ts` — Check admin_overrides, integrate RBAC
2. `reportsRoutes.ts` — Apply REPORT_EXPORT middleware
3. `server.ts` — Register new routes

### Frontend (New Files)
1. `BillingScreen.tsx` — Plan comparison + upgrade flow
2. `UpgradeModal.tsx` — In-context upgrade prompts

### Background Jobs (New Files)
1. `trialExpiryJob.ts` — Check and expire trials
2. `usageResetJob.ts` — Monthly counter reset
3. `subscriptionRenewalJob.ts` — Renewal + grace period checks

---

## Implementation Order (After Schema Approval)

1. **Write migration 009** — Apply schema
2. **Device management** — Repository + routes + desktop registration
3. **RBAC** — Repository + middleware + seed system roles
4. **Admin API** — Routes for tenant/subscription management
5. **Report export gating** — Apply middleware to existing routes
6. **Background jobs** — Trial expiry + usage reset
7. **Frontend upgrade UI** — Billing screen + modal
8. **Tests** — Enforcement, isolation, edge cases
