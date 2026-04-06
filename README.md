# ToolFest

Free online tools for PDFs, images, finance (EMI, SIP, GST), text/JSON, passwords, and QR codes — built for static hosting on **GitHub Pages** with **Google AdSense**-friendly page URLs.

## Structure

```
toolfest/
├── index.html                 # Homepage (relative links — works on github.io/repo/ or custom domain)
├── privacy.html               # Privacy policy (helpful for AdSense)
├── assets/css/shared.css      # Shared styles for tool pages
├── pdf-tools/                 # Word→PDF, merge, split, compress, JPG↔PDF, PDF→JPG
├── image-tools/               # Compress, resize, convert, crop
├── finance-tools/             # EMI, SIP, GST (India)
├── text-tools/                # Word counter, JSON formatter
└── generators/                # Password, QR code
```

## GitHub Pages

1. Push the repo to GitHub.
2. **Settings → Pages**: deploy from branch (e.g. `main`), folder `/ (root)`.
3. Site URL: `https://<user>.github.io/<repo>/` or add a custom domain in Pages settings.
4. This repo includes **`CNAME`** with `toolfest.in`. In GitHub: **Settings → Pages → Custom domain** set to `toolfest.in`, then configure DNS at your registrar (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)).

Links use **relative paths** (e.g. `pdf-tools/word-to-pdf.html`) so they work both on project Pages and at the domain root. **Canonical URLs** in every page still point to `https://toolfest.in/...` for search engines.

## Google AdSense & Analytics

Publisher ID and GA4 are centralized in **`assets/js/site-analytics.js`** (currently `ca-pub-1957013406466053` and `G-Y6CJS2NH91`). Every HTML page loads this file right after the viewport meta tag.

1. Apply with your live URL and sufficient content (this site includes multiple tool pages + privacy policy).
2. **Auto ads:** enable in the AdSense panel; the global script is enough.
3. **Manual display units:** create units in AdSense, then replace each **Ad slot** placeholder with your `<ins class="adsbygoogle" data-ad-client="…" data-ad-slot="…">` snippet and the `(adsbygoogle = window.adsbygoogle || []).push({});` line ([AdSense docs](https://support.google.com/adsense/answer/9274634)).

To change IDs later, edit only `assets/js/site-analytics.js`.

**`ads.txt`** at the repo root authorizes Google to sell your inventory. After deploy, confirm it loads at `https://toolfest.in/ads.txt`. If you change publisher ID, update this file to match.

## SEO (toolfest.in)

- **`sitemap.xml`** lists canonical URLs under `https://toolfest.in/`. Submit it in [Google Search Console](https://search.google.com/search-console) (and Bing Webmaster Tools) after you connect the custom domain.
- **`robots.txt`** points crawlers to that sitemap.
- Every HTML page includes **canonical**, **Open Graph**, **Twitter Card**, and **hreflang** (`en-IN`, `en-US`, `x-default`) tags. The homepage adds **JSON-LD** (`WebSite`, `Organization`, `ItemList`).
- After verifying the site in Search Console, uncomment or add the `google-site-verification` meta tag in `index.html` (see comment in `<head>`).

No one can guarantee #1 rankings; focus on useful tools, fast pages, and earning links over time.

High-intent URLs for ads: `pdf-tools/word-to-pdf.html`, `finance-tools/emi-calculator.html`, `image-tools/compress.html`, etc.

## Stack notes

- **pdf-lib** (CDN): merge, split, JPG→PDF, compress/resave.
- **PDF.js** (CDN): PDF→JPG rasterization.
- **JSZip** (CDN): batch ZIP downloads.
- **QRCode.js** (CDN): QR image generation.

## Disclaimer

Finance calculators are for education only, not financial or tax advice. GST slabs and rules change; verify with official sources.
