# SEO Draft — Chhath Collection Landing Pages

**Target: Foundation-Layer Keywords (Month 1-6, KD <20, Volume 100-500)**
Per Madsun Media pyramid — these are winnable for a new or low-authority domain with 4-8 quality pieces a month.

## Page 1: /chhath-gifting-collection
**Primary Keyword:** "chhath gifts online delivery india" (est. 320/mo, KD 18)
**Secondary:** "chhath puja gift boxes", "bihari festival gifts", "thekua gift box online", "madhubani soop buy"
**Intent:** Transactional + informational — buyers comparing options, diaspora sending home

**Content Structure:**
- H1: Chhath Gifting Collection — Handmade in Bihar, Ships Pan-India
- Hero: 3-column value props (Women artisans • 48hr dispatch • COD + prepaid)
- Section: Hero SKUs with schema Product markup (Thekua Box, Madhubani Soop, Sikki Set, Sujni Stole, Metallic Soop)
- Section: "Why MadeByHer for Chhath?" — artisan photos, GI tags, natural dyes, women-led
- Section: Shipping timeline table (Standard/Express/International cutoff dates)
- Section: Corporate/bulk order CTA → inquiry form
- FAQ schema: "When is Chhath 2026?", "Do you ship to US/UK?", "Can I include a note?", "What if it arrives damaged?"
- Breadcrumb schema: Home > Festival Gifting > Chhath Collection
- LocalBusiness schema: MadeByHer, Patna, Bihar — serves India + international

**Technical:**
- Canonical: self
- Noindex faceted filter URLs (?sort=, ?price=, ?color=)
- Image alt text: descriptive + keyword ("thekua gift box madhubani packaging")
- Internal links: /artisan/sunita-thekua, /craft/madhubani-painting, /shipping/india
- Page speed: under 3s LCP, optimize hero images (WebP, lazy-load below fold)

## Page 2: /madhubani-soop-chhath
**Primary Keyword:** "madhubani painting soop buy online" (est. 180/mo, KD 15)
**Secondary:** "chhath soop decoration", "madhubani art on bamboo fan", "gi tagged madhubani products"
**Intent:** Commercial investigation — specific product search, high conversion potential

**Content Structure:**
- H1: Madhubani-Painted Soop — GI-Tagged Art for Chhath Ritual & Home
- Hero: Gallery (ritual use → wall art → gift boxed) + price range ₹1,500–5,000
- Section: "The Craft" — 3-step process (bamboo prep → pencil sketch → natural pigment) with artisan video embed
- Section: "Meet the Artist" — Dulari Devi profile, 40 years painting, signed pieces
- Section: Variants table (Traditional round / Square floral / Custom motif) with schema Product variants
- Section: "Post-Chhath Care" — framing tips, cleaning, storage
- FAQ schema: "Is it GI-authenticated?", "Can I choose the motif?", "International shipping?"
- Review schema: AggregateRating from verified buyers

**Technical:**
- ImageObject schema for each gallery image (alt, caption, license)
- VideoObject schema for process video
- Canonical to collection page if near-duplicate risk
- Internal links: /artist/dulari-devi, /craft/madhubani-painting, /chhath-gifting-collection

## Page 3: /artisan-stories-chhath-makers
**Primary Keyword:** "women artisans bihar handmade crafts" (est. 210/mo, KD 22)
**Secondary:** "bihar women handicraft makers", "artisan stories india", "buy directly from artisans bihar"
**Intent:** Informational + navigational — builds trust, supports dual-sided keyword strategy (buyer + seller terms)

**Content Structure:**
- H1: Meet the Women Behind Your Chhath Gifts
- Intro: 120+ women across 4 collectives in Muzaffarpur, Darbhanga, Bhusura, Kishanganj
- Profile cards (schema Person + WorksFor):
  1. Sunita Devi — Thekua Collective Lead, Muzaffarpur
  2. Lakshmi Kumari — Sikki Grass Artisan, Darbhanga
  3. Pramila Devi — Sujni Master Embroiderer, Bhusura
  4. Rukmini Devi — Basket Weaver, Kishanganj
- Each card: photo, craft, years experience, income impact quote, link to their products
- Section: "How Your Purchase Flows" — visual: Order → Artisan paid → Material sourced → Made → Shipped
- Section: "Join as Artisan" — seller-acquisition CTA (dual-sided keyword: "sell handmade crafts bihar")
- Article schema: author=MadeByHer, datePublished, dateModified

**Technical:**
- Author profile pages with Person schema + sameAs (social links if any)
- Internal links: each artisan → their product collection
- Noindex thin profile pages if under 300 words — merge into this hub
- Vernacular keywords in H2s: "महिला कारीगर बिहार", "हस्तशिल्प बिहार"

## Schema Markup Checklist (All Pages)
- [ ] Product: name, image, description, sku, brand, offers (price, availability, seller), aggregateRating
- [ ] CollectionPage: mainEntity ItemList of Products
- [ ] BreadcrumbList: all levels
- [ ] FAQPage: 5-8 questions per page
- [ ] LocalBusiness: MadeByHer, address, geo, openingHours, priceRange, areaServed
- [ ] Organization: logo, sameAs (social), contactPoint
- [ ] Article/BlogPosting: for process/content pages
- [ ] Person: for artisan profiles
- [ ] VideoObject: for Reels/process videos embedded

## Content Production Targets (This Cycle)
- 3 collection pages (above) — Week 1
- 4 artisan profile pages — Week 2
- 2 process blog posts (Madhubani making, Sikki harvest) — Week 2
- 1 shipping/FAQ hub — Week 1
- 1 corporate gifting landing page — Week 3

## Link Building Targets (Foundation Layer)
- GI authority sites (GI Registry, EPCH, Bihar govt craft portals)
- Craft blogs (Gaatha, Sahapedia, Craftmark)
- Diaspora forums/communities (Bihari associations in US/UK/Canada/Australia)
- Wedding/festival planning sites (WedMeGood, ShaadiSaga — Chhath sections)
- Local news (Patna Press, ETV Bharat, Dainik Jagran Bihar) — pitch artisan stories

## Technical Audit Actions (Week 1)
- Crawl madebyher.com (Screaming Frog / Sitebulb)
- Flag: duplicate product descriptions, missing canonical, thin vendor pages, missing alt text, faceted filter bloat
- Fix: enforce unique description rule for sellers, noindex low-value facets, add canonical tags, batch alt text audit
- Validate: Rich Pins, Google Merchant Center feed, Search Console coverage