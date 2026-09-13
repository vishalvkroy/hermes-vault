# Campaign: 2026-09-05-gst-cess-precision

**Campaign ID:** 2026-09-05-gst-cess-precision
**Timestamp:** 2026-09-05T07:07:00Z
**Status:** drafted

## Objective
Turn a real Astra Atlas engineering fix (GST Compensation Cess support, shipped Aug 17-18 2026) into a founder-led LinkedIn post that demonstrates the specific, worked-example depth the research doc says Astra's messaging currently lacks.

## Hypothesis
Indian SMB buyers evaluating POS/CRM tools are numb to generic "AI-powered" claims (62-97% SMB AI adoption per research, now table stakes per finding #3). A concrete, technically specific story about how the product handles a real GST edge case (cess on carbonated drinks, why it's a second levy and not a 40% slab) builds more trust and differentiation with tier-2/3 retailers than another feature-list post. It also demonstrates the "cross-channel timeline" integration positioning gap (finding #2) indirectly by showing how one accounting decision threads through product, purchase, sale, and GST filing.

## Grounded in research finding
Source: `astrastudio/research/2026-09-04-market-signals-update.md`
- Finding #3, "AI Adoption is Baseline, Not Story" - "Atlas has AI features" is insufficient; specificity needed on which use cases, which SMB segments benefit.
- Supporting context: Finding #2, cross-channel timeline messaging gap - Atlas/Spark/Lens need clearer positioning as one integrated system rather than three separate products.

## Real event pulled from repo (git log)
- Commit `85c6f0c` (Aug 17 2026): "feat: GST Compensation Cess — a second levy, not a 40% GST rate" - added cess as its own ledger line (not merged into the GST rate) after a Coke/carbonated-drinks retailer couldn't bill correctly under the existing 28% GST cap. 1162 tests passing, 49 suites.
- Commit `8baf874` (Aug 18 2026): "feat: compensation cess on purchases (input credit)" - closed the other half of the same bug: cess paid on purchases had nowhere to record as input credit, so retailer liability read high and credit went unclaimed.
- Both commits co-authored with Claude Opus 5, per repo convention.

## Target audience
Indian SMB retailers and owner-operators evaluating POS/billing software, particularly those selling cess-liable goods (carbonated drinks, tobacco, aerated beverages) who've hit this exact GST filing problem elsewhere. Secondary: other SaaS founders/engineers who follow build-in-public content.

## Channels used
- **LinkedIn** (primary, connected account: astrastudio, provider linkedin, account "Vishal Kumar") - founder-led post, drafted below. Post ID `e602f17a-8723-44a2-a3f6-9a5b0ead6ebd`, status `pending_approval`, approval requested from Vishal via Telegram on 2026-09-05.
- Instagram/Facebook/Reddit: not connected for this brand yet: no drafts produced this cycle (per campaign-workflow skill, stay draft-only once connected, but Astra Studio's only live platform is LinkedIn).

## URLs
None (no external link in this post; keeps it native to LinkedIn feed).

## Metrics
Pending (fill in after Vishal approves and publishes, and analytics collect).

## Outcome
Pending.
