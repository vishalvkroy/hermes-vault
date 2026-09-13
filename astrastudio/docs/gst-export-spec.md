# GST Export Module — Architecture Spec

Status: DRAFT (spec only, no implementation)
Scope: Produce all necessary Indian GST exports — GSTR-1 (all sections), GSTR-3B,
GSTR-2B reconciliation — as **portal-ready GSTN JSON** plus Tally XML / Excel / CSV / PDF.
Extensible to GSTR-9 and CMP-08.

---

## 1. Design principles

1. **Compute once, serialize many.** Each return is computed into a single canonical
   in-memory model (e.g. `Gstr1Return`). Format serializers (JSON/XML/Excel/CSV/PDF)
   consume that model. No format re-queries the DB. This is the export-format abstraction.
2. **Trust the sale-time tax snapshot.** `sale_items` / `invoices` already store
   `cgst_amount / sgst_amount / igst_amount` computed at sale time (salesService). The
   export layer **reads these**, never recomputes GST. igst>0 ⇒ inter-state; else intra.
3. **Reuse what exists.** `gstr3bService`, `gstr2bService`, `einvoiceService`,
   `ewaybillService`, `tallyExportService` stay. We add `gstr1Service` + a serializer layer
   and wrap 3B/2B output in the same export abstraction.
4. **Read-only, tenant-scoped.** Every query filters `tenant_id`. Routes gated
   `reports:view`. No writes except marking a return as "filed" (audit only).

---

## 2. Module structure

```
backend/src/
├── routes/
│   └── gstrRoutes.ts                 # EXTEND: add GSTR-1 + export endpoints
├── services/
│   ├── gstr1Service.ts               # NEW: compute Gstr1Return canonical model
│   ├── gstr3bService.ts              # EXISTS: wrap output in exporter
│   └── gstr2bService.ts              # EXISTS: recon → exporter
├── repositories/
│   └── gstReturnsRepository.ts       # NEW: section-wise SQL aggregations
├── lib/gst/
│   ├── model/                        # NEW: canonical models (TS types)
│   │   ├── gstr1.ts                  #   Gstr1Return, B2BInvoice, HsnSummaryRow, …
│   │   └── gstr3b.ts
│   ├── schema/                       # NEW: GSTN JSON builders (schema-exact)
│   │   ├── gstr1Json.ts              #   Gstr1Return → GSTN GSTR-1 JSON
│   │   └── gstr3bJson.ts
│   ├── serializers/                  # NEW: format abstraction
│   │   ├── index.ts                  #   GstExporter interface + registry/factory
│   │   ├── gstnJson.ts
│   │   ├── tallyXml.ts               #   reuse tallyExportService building blocks
│   │   ├── excel.ts                  #   GST Offline-Utility-compatible workbook
│   │   ├── csv.ts                    #   per-section CSV (zip)
│   │   └── pdf.ts                    #   human-readable
│   ├── period.ts                     # NEW: MMYYYY <-> {month,year}, fiscal-year helpers
│   └── gstUtils.ts                   # EXISTS: rounding (round-half-up), paise<->rupee
```

Desktop side (phase B): `desktop/src/api/gst.ts` + `screens/Reports/` GST tab.

---

## 3. Export-format abstraction

```ts
export type GstFormat = 'gstn_json' | 'tally_xml' | 'excel' | 'csv' | 'pdf';

export interface GstExportResult {
  filename: string;          // e.g. GSTR1_27ABCDE1234F1Z5_062026.json
  contentType: string;       // application/json | application/xml | …
  bytes: Buffer | string;
}

export interface GstExporter<TModel> {
  format: GstFormat;
  serialize(model: TModel, ctx: ExportCtx): GstExportResult;
}

interface ExportCtx { gstin: string; period: string; legalName: string; }
```

A `serializerRegistry[returnType][format]` factory picks the serializer. Adding a new
return type (GSTR-9) = add a model + its JSON builder + register serializers. No route churn.

---

## 4. Canonical model — `Gstr1Return`

```ts
interface Gstr1Return {
  gstin: string;            // tenant_settings.gstin
  fp: string;               // filing period "MMYYYY"
  b2b:   B2BParty[];        // §4A/4B — to registered
  b2cl:  B2CLInvoice[];     // §5     — B2C inter-state, invoice value > ₹1,00,000
  b2cs:  B2CSRow[];         // §7     — B2C consolidated (rate × POS)
  cdnr:  CDNRParty[];       // §9B    — credit/debit notes to registered
  cdnur: CDNURNote[];       // §9B    — credit/debit notes to unregistered (large/export)
  exp:   ExportInvoice[];   // §6A    — exports (WPAY/WOPAY)
  nil:   NilSupplies;       // §8     — nil-rated, exempt, non-GST
  hsn:   HsnSummaryRow[];   // §12    — MANDATORY HSN-wise summary
  docs:  DocIssued[];       // §13    — documents issued (ranges + cancelled)
}
```

---

## 5. GSTR-1 section → source-table mapping

All "invoice" rows = `invoices` where `source_type='SALE'` (the GST snapshot), joined to
`sale_items` for rate-wise lines. Period filter: `invoice_date` within month.
Inter/intra is read from stored `igst_amount > 0`.

| Section | Source | Filter | Group / shape |
|---|---|---|---|
| **B2B** (4A) | invoices + sale_items | `party_gstin IS NOT NULL` | by `party_gstin` → list of invoices → rate-wise items (`rt`, `txval`, `iamt`/`camt`+`samt`) |
| **B2CL** (5) | invoices + sale_items | `party_gstin IS NULL` AND `igst_amount>0` (inter) AND `total_amount > 100000` | by `place_of_supply` (state code) → invoices → rate-wise |
| **B2CS** (7) | sale_items via invoices | `party_gstin IS NULL` AND NOT B2CL (intra, or inter ≤ ₹1L) | **consolidated** by (`pos` state, `rt` rate, `sply_ty` INTER/INTRA) → sum `txval`, `iamt`/`camt`/`samt`. No invoice detail. |
| **CDNR** (9B) | credit_notes / debit_notes | `party_gstin IS NOT NULL` | by `party_gstin` → notes (`ntty` C/D, `nt_num`, `nt_dt`, orig inv ref) → rate-wise |
| **CDNUR** (9B) | credit_notes / debit_notes | `party_gstin IS NULL` AND (inter large OR export) | flat list (`typ` B2CL/EXPWP/EXPWOP) |
| **EXP** (6A) | invoices + sale_items | export type (customer state = overseas / `invoice_type` export) | `exp_typ` WPAY/WOPAY, port/shipping bill if present. *(May be empty today → emit `[]`.)* |
| **Nil/Exempt** (8) | sale_items | `gst_rate = 0` (split nil vs exempt vs non-GST by product flag) | totals by inter/intra × reg/unreg |
| **HSN** (12) | sale_items | all in period | by (`hsn_code`, `rt`, `unit`) → `qty`, `txval`, `iamt`/`camt`/`samt`, `csamt` |
| **Docs** (13) | invoices / sale_number_sequences | period | issued range (from/to num), total, cancelled count, net |

**Notes / data-capture gaps to flag for build:**
- **B2CS place-of-supply**: needs the customer's *state code*. For registered → from GSTIN
  (first 2 digits). For walk-in/unregistered → we currently don't capture customer state.
  Default rule: if `igst_amount=0` ⇒ intra ⇒ POS = tenant `state_code`; only inter-state
  unregistered (rare at POS) needs an explicit state. **Recommend**: add optional
  `place_of_supply` capture in POS for unregistered inter-state sales; otherwise default to home state.
- **EXP / CDNUR-export**: only relevant if the tenant exports. Emit empty arrays; build later.
- **Nil vs Exempt vs Non-GST**: needs a product-level classification flag. If absent, treat
  `gst_rate=0` as "exempt" and note the limitation.

---

## 6. Intra vs inter-state determination (authoritative)

Do **not** re-derive from GSTINs at export time — use the persisted snapshot:
- Line is **inter-state** ⟺ `igst_amount > 0`. `sply_ty = 'INTER'`. POS = customer state code.
- Line is **intra-state** ⟺ `cgst_amount + sgst_amount > 0`. `sply_ty = 'INTRA'`. POS = tenant state code.
- Customer state code = `party_gstin[0:2]` when registered; else `place_of_supply` column;
  else tenant `state_code` (intra default).
- Tenant state code = `tenant_settings.state_code` (validate present before any export; block with a clear error if missing — GSTN JSON is invalid without it).

This matches what salesService already stored, so GSTR-1 will reconcile with GSTR-3B
(which `gstr3bService` computes from the same columns).

---

## 7. GSTN JSON schema (GSTR-1 top level)

```jsonc
{
  "gstin": "27ABCDE1234F1Z5",
  "fp": "062026",                       // MMYYYY
  "version": "GST3.1.6",                // current GSTN schema version (configurable)
  "hash": "hash",
  "b2b":  [ { "ctin":"…", "inv":[ { "inum","idt","val","pos","rchrg":"N","inv_typ":"R",
                                    "itms":[ {"num":1,"itm_det":{"rt":18,"txval":1000,
                                              "iamt":180,"camt":0,"samt":0,"csamt":0}} ] } ] } ],
  "b2cl": [ { "pos":"29", "inv":[ {"inum","idt","val","itms":[…]} ] } ],
  "b2cs": [ { "sply_ty":"INTRA","pos":"27","typ":"OE","rt":18,"txval":5000,"camt":450,"samt":450,"iamt":0,"csamt":0 } ],
  "cdnr": [ { "ctin":"…","nt":[ {"ntty":"C","nt_num","nt_dt","val","itms":[…]} ] } ],
  "cdnur":[ { "typ":"B2CL","ntty":"C","nt_num","nt_dt","val","pos","itms":[…] } ],
  "exp":  [ { "exp_typ":"WPAY","inv":[ {"inum","idt","val","itms":[{"txval","rt","iamt","csamt"}]} ] } ],
  "nil":  { "inv":[ {"sply_ty":"INTRB2C","expt_amt":0,"nil_amt":0,"ngsup_amt":0} ] },
  "hsn":  { "data":[ {"num":1,"hsn_sc":"1006","desc":"Rice","uqc":"KGS","qty":100,
                      "rt":5,"txval":5000,"iamt":0,"camt":125,"samt":125,"csamt":0} ] },
  "doc_issue": { "doc_det":[ {"doc_num":1,"docs":[{"num":1,"from":"INV/…/0001","to":"INV/…/0042","totnum":42,"cancel":0,"net_issue":42}]} ] }
}
```

Field-name mapping (canonical → GSTN keys) lives in `lib/gst/schema/gstr1Json.ts`.
Amounts: numbers, `round-half-up` to 2 decimals (`gstUtils`). `csamt` = cess (0 unless cess products).

---

## 8. Routes (extend `gstrRoutes.ts`, prefix `/api/v1`)

```
GET /gst/r1?month=&year=                          → compute Gstr1Return (JSON preview for UI)
GET /gst/r1/export?month=&year=&format=gstn_json  → download (gstn_json|tally_xml|excel|csv|pdf)
GET /gst/r1/hsn?month=&year=                       → HSN summary (own view; also embedded in r1)
GET /gst/3b/export?month=&year=&format=            → wrap gstr3bService output
GET /gst/2b/export?period=&format=                 → reconciliation result export (mismatches)
POST /gst/r1/mark-filed  {period, arn?}            → audit-only: record filing + ARN
```
All `reports:view`. `?format` defaults to `gstn_json`. Export endpoints stream a file
(Content-Disposition). CSV "format" returns a zip of per-section CSVs.

---

## 9. ADRs (decisions)

- **ADR-1 — Canonical model + serializer split.** Compute the return once into a typed model;
  serializers convert to each format. *Why:* GSTN JSON, Tally XML, Excel, CSV, PDF must all
  show identical numbers; a shared model guarantees that and isolates GSTN schema-version
  churn to one file. *Rejected:* per-format SQL (drift + 5× query maintenance).
- **ADR-2 — Read persisted cgst/sgst/igst, never recompute.** *Why:* the sale-time snapshot is
  legally authoritative and already reconciles with 3B; recomputing risks rounding drift and
  mismatched returns. *Rejected:* recompute from rate at export (could disagree with what was billed).
- **ADR-3 — New `gstReturnsRepository`, not `reportsRepository`.** *Why:* GST section
  aggregations are large, schema-version-coupled, and read-heavy; isolating them keeps
  reports analytics independent. *Trade-off:* one more repo, accepted.
- **ADR-4 — Live under existing `/gst/*` surface.** *Why:* consistency with 3B/2B/e-invoice
  already there; one mental model for the GST tab.
- **ADR-5 — GSTN schema version is config, not hardcoded.** Store `GST_SCHEMA_VERSION` in env/
  config; GSTN bumps it periodically. *Why:* avoid a code change every portal update.

---

## 10. Build order (phase B)

1. `period.ts` + `model/gstr1.ts` (types) + `gstReturnsRepository` (the SQL — biggest piece).
2. `gstr1Service.compute()` → canonical model; `GET /gst/r1` preview.
3. `schema/gstr1Json.ts` + `serializers/gstnJson.ts` → **GSTN JSON export** (the must-have).
4. CSV + Excel + PDF serializers; Tally XML via existing `tallyExportService`.
5. Wrap GSTR-3B + GSTR-2B in the exporter.
6. Desktop Reports GST tab (use `/ui-ux-pro-max` skill) with section preview + export buttons +
   the GSTN-JSON button (the one missing from the current mockup).
7. (Later) GSTR-9, CMP-08 by adding models + serializers — no architectural change.

---

## 11. Validation checklist before "Ready to export"

- tenant_settings.gstin present + valid (einvoiceService.validateGSTIN).
- tenant_settings.state_code present.
- No invoice in period with missing place_of_supply where inter-state.
- HSN code present on every line (GSTN rejects blank HSN for B2B). Surface a "fix these N
  products" list if not — block export with actionable error, never emit invalid JSON.
- GSTR-1 totals tie out to GSTR-3B Table 3.1 for the same period (cross-check, warn on drift).
