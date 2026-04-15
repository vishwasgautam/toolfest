# Health Tools Indexing Checklist (2-Week Loop)

This checklist is for monitoring health-tool discovery and index coverage in Search Console after publishing.

## Day 0 (Publish Day)

1. Confirm these URLs return HTTP 200:
   - `/health-tools/`
   - `/health-tools/bmi-calculator.html`
   - `/health-tools/bmr-tdee-calculator.html`
   - `/health-tools/protein-calculator.html`
   - `/health-tools/calorie-deficit-calculator.html`
   - `/health-tools/macro-calculator.html`
   - `/health-tools/water-intake-calculator.html`
2. Confirm sitemap URLs return HTTP 200:
   - `/sitemap.xml`
   - `/sitemap-programmatic-health.xml`
3. In Search Console > Sitemaps submit:
   - `https://toolfest.in/sitemap-programmatic-health.xml`
4. Request indexing only for high-level pages:
   - `/health-tools/`
   - `/health-tools/bmi/`
   - `/health-tools/protein/`
   - `/health-tools/calorie-deficit/`

## Days 1-7

- Check Search Console > Pages:
  - Indexed count trend
  - "Discovered - currently not indexed"
  - "Crawled - currently not indexed"
- Do not manually request indexing for every long-tail page.
- Improve internal links if discovered count grows but indexed stays flat:
  - link from hub pages to top examples
  - keep links in homepage quick-action strip

## Days 8-14

- In Search Console > Performance (last 7 days):
  - Filter `Page` contains `/health-tools/`
  - Note impressions, clicks, top queries
- Upgrade underperforming pages (highest impressions, low clicks):
  - tighten title/description for exact query wording
  - add 2-3 FAQ items
  - add related links to sibling pages
- Re-request indexing for only 5-10 improved URLs.

## KPI Targets (First 2 Weeks)

- Health pages indexed: 20-35% of health sitemap URLs
- Search impressions on health URLs: increasing week-over-week
- First clicks from long-tail health queries

## Safety Review (YMYL Guardrails)

- Keep "Informational only" and "Not medical advice" text on all health pages.
- Do not add treatment claims, disease cures, or diagnosis language.
- Keep formulas transparent and visible where results are shown.
