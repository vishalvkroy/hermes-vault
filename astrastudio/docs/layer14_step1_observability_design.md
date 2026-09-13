# Layer 14 — STEP 1: Observability & Logging Design

## Current State Audit

### What EXISTS
| Area | Status | Detail |
|------|--------|--------|
| Logger | Pino (via Fastify) | Configured with log level from env, pino-pretty in dev |
| Global error handler | Basic | Catches validation + 500, hides messages in prod |
| Health check | `/health` | Checks PostgreSQL + MongoDB |
| Graceful shutdown | SIGINT/SIGTERM | Closes app, DB, MongoDB |
| DB connection pool | pg Pool | min 2, max 10, idle/connection timeouts |
| Config validation | Partial | Only checks DATABASE_URL and JWT_SECRET exist |

### What's BROKEN / MISSING
| Area | Problem | Risk |
|------|---------|------|
| **203 console.log/error/warn calls** | Bypass structured logging entirely | Logs lost in production, no JSON, no correlation |
| **Zero request correlation** | No request ID generation or propagation | Cannot trace a request across service boundaries |
| **No request/response logging** | Fastify logger exists but isn't used in routes | Invisible request patterns, no latency tracking |
| **Error handler is too basic** | No error classification, no tenant context, no request context | Debugging production issues is impossible |
| **No security headers** | No helmet, CORS is `origin: true` (wildcard) | Vulnerable to XSS, clickjacking, MIME sniffing |
| **No rate limiting** | Config defines rate limit values but nothing enforces them | API abuse, DDoS, scraping all undefended |
| **No audit trail** | Business operations (sales, returns, stock changes) not logged | No forensics capability |
| **DB pool errors crash process** | `process.exit(1)` on pool error | Single connection failure kills the server |
| **No slow query detection** | No query timing or alerting | Silent performance degradation |
| **No disk/memory monitoring** | No resource consumption tracking | OOM kills with no warning |

---

## Design: Production Observability Stack

### Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                    FASTIFY APP                       │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │ Request   │  │ Business │  │ Tenant Access     │  │
│  │ Lifecycle │  │ Services │  │ Middleware         │  │
│  │ Hooks     │  │          │  │                   │  │
│  └─────┬─────┘  └─────┬────┘  └────────┬──────────┘  │
│        │              │               │              │
│        ▼              ▼               ▼              │
│  ┌─────────────────────────────────────────────────┐ │
│  │              LOGGER (Pino)                      │ │
│  │  Structured JSON · Request IDs · Tenant Context │ │
│  │  Log Levels · Child Loggers · Redaction         │ │
│  └──────────────────────┬──────────────────────────┘ │
│                         │                            │
└─────────────────────────┼────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   stdout (JSON)       │
              │   → Render logs       │
              │   → Log aggregation   │
              │   → Future: Datadog/  │
              │     Grafana/ELK       │
              └───────────────────────┘
```

### Principle: Use What's Already There

Fastify ships with Pino. We won't add Winston, Bunyan, or any other logger.
We will:
1. Configure Pino properly for production
2. Replace ALL 203 console.* calls with structured logger calls
3. Add request lifecycle hooks for automatic logging
4. Create child loggers with tenant/request context

---

## 1. Logger Configuration Enhancement

### File: `backend/src/config/logger.ts` (NEW)

```typescript
import { FastifyRequest } from 'fastify';
import pino from 'pino';

/**
 * Production logger configuration.
 *
 * RULES:
 * - JSON in production, pretty in development
 * - Request IDs auto-generated
 * - Tenant context propagated
 * - Sensitive fields redacted
 * - Serializers for requests/responses/errors
 */
export const loggerConfig = {
  // Log level from env, default 'info' in prod
  level: process.env.LOG_LEVEL || 'info',

  // Redact sensitive fields from logs
  redact: {
    paths: [
      'req.headers.authorization',
      'req.headers.cookie',
      'password',
      'password_hash',
      'bank_account_number',
      'bank_ifsc_code',
      'gstin',
    ],
    censor: '[REDACTED]',
  },

  // Serializers for consistent log structure
  serializers: {
    req(request: FastifyRequest) {
      return {
        method: request.method,
        url: request.url,
        hostname: request.hostname,
        remoteAddress: request.ip,
        tenant_id: (request as any).tenant_id || undefined,
      };
    },
    err: pino.stdSerializers.err,
  },

  // Generate request IDs
  genReqId: (request: FastifyRequest) => {
    return request.headers['x-request-id'] as string
      || crypto.randomUUID();
  },

  // Pretty print in development only
  transport: process.env.NODE_ENV !== 'production'
    ? {
        target: 'pino-pretty',
        options: {
          translateTime: 'HH:MM:ss Z',
          ignore: 'pid,hostname',
          colorize: true,
        },
      }
    : undefined,
};
```

### Key Decisions:
- **Redaction**: JWT tokens, passwords, bank details, GSTIN never appear in logs
- **Request IDs**: Accept `X-Request-Id` from upstream (load balancer) or generate UUID
- **Tenant context**: Every log line includes `tenant_id` when available
- **JSON in production**: Structured for log aggregation (Datadog, Grafana Loki, CloudWatch)

---

## 2. Request Lifecycle Hooks

### File: `backend/src/middleware/requestLifecycle.ts` (NEW)

```typescript
/**
 * Request lifecycle observability hooks.
 *
 * Automatically logs:
 * - Request received (method, URL, tenant)
 * - Request completed (status code, duration)
 * - Request errors (with full context)
 * - Slow requests (> threshold)
 */

// onRequest hook — log incoming request + start timer
// onResponse hook — log completion + duration + status
// onError hook — log errors with request context + tenant context

// Slow request threshold: 3000ms (configurable via env)
// Logs at 'warn' level for slow requests
// Logs at 'error' level for 5xx responses
```

### Log Output Examples:

**Normal request:**
```json
{
  "level": "info",
  "time": 1707500000000,
  "reqId": "abc-123",
  "tenant_id": "tenant-456",
  "msg": "request completed",
  "method": "POST",
  "url": "/api/v1/sales",
  "statusCode": 201,
  "durationMs": 45
}
```

**Slow request:**
```json
{
  "level": "warn",
  "time": 1707500000000,
  "reqId": "abc-789",
  "tenant_id": "tenant-456",
  "msg": "slow request detected",
  "method": "GET",
  "url": "/api/v1/reports/profit-loss",
  "statusCode": 200,
  "durationMs": 5200,
  "threshold": 3000
}
```

**Error:**
```json
{
  "level": "error",
  "time": 1707500000000,
  "reqId": "abc-999",
  "tenant_id": "tenant-456",
  "msg": "request failed",
  "method": "POST",
  "url": "/api/v1/sales",
  "statusCode": 500,
  "err": {
    "type": "Error",
    "message": "Cannot read property...",
    "stack": "..."
  }
}
```

---

## 3. Enhanced Error Handler

### File: Modify `server.ts` error handler

**Error Classification:**

| Category | HTTP Status | Log Level | Action |
|----------|-------------|-----------|--------|
| Validation | 400 | info | Return field errors |
| Auth/AuthZ | 401/403 | warn | Log attempt, return generic |
| Not Found | 404 | info | Return not found |
| Rate Limited | 429 | warn | Log tenant, return retry-after |
| SaaS Limit | 402/403/429 | info | Return upgrade prompt |
| Business Error | 409/422 | info | Return business error detail |
| Internal Error | 500 | error | Log full stack, return generic in prod |

**Structure:**
```typescript
{
  success: false,
  error: {
    code: 'STOCK_INSUFFICIENT',     // Machine-readable
    message: 'Not enough stock',     // Human-readable
    details: { ... },                // Context (dev only for 500s)
    requestId: 'abc-123',           // For support tickets
  }
}
```

---

## 4. Structured Logger Utility

### File: `backend/src/utils/logger.ts` (NEW)

Replace ALL `console.log/error/warn` with a structured logger that:
- Creates child loggers with context (`{ tenant_id, service, operation }`)
- Provides domain-specific log methods:
  - `logger.stock(...)` — stock engine operations
  - `logger.sales(...)` — sales operations
  - `logger.auth(...)` — authentication events
  - `logger.saas(...)` — SaaS enforcement events
  - `logger.db(...)` — database operations

**This is NOT a new logging library.** It's a thin wrapper around Fastify's Pino logger that adds context binding.

---

## 5. Database Query Observability

### Modify: `backend/src/database/connection.ts`

Add query-level instrumentation:

```typescript
// Wrap query() to track:
// - Query execution time
// - Slow queries (> 1000ms threshold)
// - Query errors with SQL context (redacted params)
// - Pool utilization (active/idle/waiting connections)

// Pool health metrics exposed via /health/detailed:
{
  pool: {
    total: 10,
    idle: 7,
    active: 3,
    waiting: 0,
  },
  slowQueries: {
    last5min: 2,
    threshold: 1000,
  }
}
```

**CRITICAL**: Pool error handler must NOT `process.exit(1)`. Instead:
- Log the error at 'fatal' level
- Attempt reconnection
- Only exit if reconnection fails 3 times

---

## 6. Audit Event Logger

### File: `backend/src/utils/auditLogger.ts` (NEW)

Structured audit trail for business-critical operations:

```typescript
// Logs (NOT stored in DB — goes to structured log output)
// These can be ingested by log aggregation for compliance

interface AuditEvent {
  event_type: string;        // SALE_CREATED, RETURN_PROCESSED, STOCK_ADJUSTED
  tenant_id: string;
  user_id: string;
  entity_type: string;       // sale, return, product, stock
  entity_id: string;
  action: string;            // create, update, delete, approve
  metadata: Record<string, any>;  // Amounts, quantities, etc.
  ip_address?: string;
  timestamp: string;
}
```

**Events to Audit:**
| Event | Trigger |
|-------|---------|
| SALE_CREATED | New sale recorded |
| RETURN_PROCESSED | Return approved/processed |
| STOCK_ADJUSTED | Manual stock adjustment |
| PURCHASE_CREATED | New purchase order |
| USER_LOGIN | Successful login |
| USER_LOGIN_FAILED | Failed login attempt |
| PLAN_CHANGED | Subscription upgrade/downgrade |
| TENANT_STATE_CHANGED | TRIAL→ACTIVE, ACTIVE→SUSPENDED, etc. |
| EXPORT_GENERATED | CSV/PDF report exported |
| AI_QUERY_MADE | Atlas AI query executed |
| DEVICE_REGISTERED | New device registered |
| ADMIN_OVERRIDE | Admin manually overrides limits |

---

## 7. console.* Replacement Strategy

**203 console.* calls across 30 files** must be replaced. Strategy:

### Phase 1: Critical path (services + middleware)
Replace in:
- `stockEngine.ts` (5 calls) → `logger.stock()`
- `salesService.ts` (4 calls) → `logger.sales()`
- `returnsService.ts` (5 calls) → `logger.returns()`
- `purchaseService.ts` (5 calls) → `logger.purchase()`
- `tenantAccessService.ts` (4 calls) → `logger.saas()`
- `tenantAccessMiddleware.ts` (3 calls) → `logger.saas()`

### Phase 2: Infrastructure
Replace in:
- `connection.ts` (7 calls) → `logger.db()`
- `mongoConnection.ts` (4 calls) → `logger.db()`
- `server.ts` (13 calls) → `app.log.*`
- `migrate.ts` (13 calls) → `logger.db()`

### Phase 3: Routes + repositories
Replace remaining calls in route handlers and repositories.

### Phase 4: Test files
Test files keep `console.log` — that's acceptable for test output.

---

## 8. Enhanced Health Check

### Current `/health` — Basic (stays)
### New `/health/detailed` — Full system status (admin only)

```typescript
{
  status: 'healthy' | 'degraded' | 'unhealthy',
  timestamp: '2026-02-10T...',
  version: '1.0.0',
  uptime_seconds: 86400,

  checks: {
    postgresql: {
      status: 'healthy',
      latency_ms: 2,
      pool: { total: 10, idle: 7, active: 3, waiting: 0 },
    },
    mongodb: {
      status: 'healthy',
      latency_ms: 15,
    },
    memory: {
      rss_mb: 128,
      heap_used_mb: 95,
      heap_total_mb: 150,
      external_mb: 12,
    },
    event_loop: {
      lag_ms: 1.2,
    },
  },

  // Only in development
  debug: {
    node_version: '20.x',
    platform: 'linux',
    env: 'production',
  }
}
```

---

## 9. Security Headers

### Via `@fastify/helmet` plugin:

```typescript
// Headers added:
// - X-Content-Type-Options: nosniff
// - X-Frame-Options: DENY
// - X-XSS-Protection: 0 (deprecated, but CSP covers this)
// - Strict-Transport-Security: max-age=31536000; includeSubDomains
// - Content-Security-Policy: default-src 'self'
// - Referrer-Policy: strict-origin-when-cross-origin
```

### CORS hardening:

```typescript
// Replace origin: true with explicit allow list:
origin: [
  'http://localhost:1420',        // Tauri dev
  'https://astraatlas.com',       // Production website
  'tauri://localhost',            // Tauri production
],
```

---

## 10. Rate Limiting

### Via `@fastify/rate-limit`:

| Endpoint Category | Limit | Window | Scope |
|-------------------|-------|--------|-------|
| Auth (login) | 5 | 15 min | per IP |
| Auth (register) | 3 | 1 hour | per IP |
| Atlas AI | Plan-based | 1 month | per tenant |
| API general | 100 | 1 min | per tenant |
| Public endpoints | 30 | 1 min | per IP |
| Health check | 60 | 1 min | per IP |

---

## Files to Create / Modify

### New Files
| File | Purpose |
|------|---------|
| `backend/src/config/logger.ts` | Pino logger config with redaction + serializers |
| `backend/src/middleware/requestLifecycle.ts` | Request timing, logging, slow detection |
| `backend/src/utils/logger.ts` | Structured logger utility (domain child loggers) |
| `backend/src/utils/auditLogger.ts` | Business event audit trail |

### Modified Files
| File | Changes |
|------|---------|
| `server.ts` | Enhanced error handler, security headers, rate limiting, lifecycle hooks |
| `connection.ts` | Query timing, pool metrics, reconnection logic |
| `config.ts` | New config sections for observability thresholds |
| `package.json` | Add `@fastify/helmet`, `@fastify/rate-limit` |
| All 30 files with console.* | Replace with structured logger calls |

### NOT Modified
| File | Reason |
|------|--------|
| Stock engine logic | Layer 7 is IMMUTABLE |
| Sales/purchase/returns service logic | Business logic untouched |
| Database schema | No schema changes for observability |
| Frontend | Layer 14 is backend-only for Step 1 |

---

## New Dependencies

```
@fastify/helmet    — Security headers
@fastify/rate-limit — API rate limiting
```

No new logging dependencies. Pino is already included via Fastify.

---

## Implementation Order (After Approval)

1. Install `@fastify/helmet` + `@fastify/rate-limit`
2. Create `config/logger.ts` — logger configuration
3. Create `utils/logger.ts` — structured logger utility
4. Create `utils/auditLogger.ts` — business audit logger
5. Create `middleware/requestLifecycle.ts` — request hooks
6. Enhance `server.ts` — error handler, helmet, rate-limit, hooks
7. Enhance `database/connection.ts` — query timing, pool metrics, reconnection
8. Update `config.ts` — add observability config section
9. Replace `console.*` in all 30 files (Phase 1→4)
10. Add `/health/detailed` endpoint
11. Build + test compilation
