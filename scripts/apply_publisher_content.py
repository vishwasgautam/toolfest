#!/usr/bin/env python3
"""One-off: remove ad-slot placeholders; insert unique publisher HTML for AdSense policy."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Unique articles per URL path (relative to ROOT)
ARTICLES: dict[str, str] = {}

def A(slug: str, html: str) -> None:
    ARTICLES[slug] = html.strip()

A("pdf-tools/merge-pdf.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Merge PDF files online without uploading them</h2>
    <p itemprop="description">Merging PDFs is one of the most common document tasks for students, freelancers, and small businesses in <strong>India</strong> and the <strong>United States</strong>. You might combine bank statements for a loan application, attach annexures to a tender, or bundle lecture notes before sharing them on email or WhatsApp. ToolFest lets you join multiple PDFs into a single file entirely in your browser at <strong>toolfest.in</strong>, which means your contracts and personal papers are not uploaded to our servers.</p>
    <p>Use the arrows to reorder files before merging: the file at the top becomes the first section of the new PDF. If a file fails, it is often password-protected or corrupted; unlock or repair it locally first. For very large bundles, merge in smaller batches to keep your device responsive.</p>
    <h3>Questions people ask</h3>
    <ul>
      <li><strong>Is merging PDFs free here?</strong> Yes. There is no account and no paywall for this tool.</li>
      <li><strong>Does the order of files matter?</strong> Yes. Top to bottom is the order of pages in the output.</li>
      <li><strong>Can I merge scanned PDFs?</strong> Usually yes, if they are valid PDFs. Image-only scans tend to produce larger files than text PDFs.</li>
    </ul>
  </article>""")

A("pdf-tools/split-pdf.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Split a PDF into separate page files</h2>
    <p>Splitting is useful when you only need to email one chapter, upload a single form page, or archive each page separately. Courts, universities, and employers often ask for <strong>individual PDFs per page</strong> instead of one long document. This tool creates one PDF per page and packs them into a ZIP so you can download everything at once.</p>
    <p>Processing stays on your computer. We do not store filenames or page contents. If your PDF is encrypted, use the password in your desktop reader first, then split an unlocked copy here.</p>
    <h3>Quick tips</h3>
    <ul>
      <li>Rename the ZIP after download so you remember the case or project it belongs to.</li>
      <li>Multi-hundred-page PDFs can take time; close other heavy tabs while splitting.</li>
    </ul>
  </article>""")

A("pdf-tools/compress-pdf.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Reduce PDF file size in the browser</h2>
    <p>Email providers and government portals often enforce <strong>strict upload limits</strong>. Compressing a PDF can make the difference between an accepted application and a bounced message. ToolFest re-saves your PDF with efficient object streams where possible. Results vary: text-heavy office PDFs usually shrink more than scanned photo pages, which are already compressed images.</p>
    <p>Compare the before and after sizes shown on the page. If the file grows, your PDF may already be optimised; in that case try reducing image resolution at scan time or use an image tool first.</p>
    <h3>When to use this</h3>
    <ul>
      <li>Applying for jobs or college seats with attachment size caps.</li>
      <li>Sharing reports with colleagues in India or abroad over slow mobile data.</li>
    </ul>
  </article>""")

A("pdf-tools/jpg-to-pdf.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Turn JPG and PNG images into one PDF</h2>
    <p>Many official processes still expect a <strong>single PDF attachment</strong> even when your originals are phone photos of ID cards, marksheets, or invoices. Ordering matters: put the cover page first, then supporting pages, exactly as you would staple a physical file. WebP and PNG are supported; very high resolution photos create large PDFs, so consider compressing images first using our image tools.</p>
    <p>This workflow is common for <strong>rent agreements, KYC updates, and US visa or school forms</strong> where each photo must appear as a sequential page.</p>
  </article>""")

A("pdf-tools/pdf-to-jpg.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Export PDF pages as JPG images</h2>
    <p>Designers, teachers, and social media managers often need <strong>slide-quality images</strong> from a PDF deck. Rasterising each page to JPG makes it easy to drop visuals into presentations or chat apps. We render at 2× scale for reasonable sharpness; adjust JPEG quality if you need smaller files.</p>
    <p>Multi-page documents download as a ZIP of numbered images. Single-page PDFs download one JPG directly. Encrypted PDFs must be unlocked before conversion.</p>
  </article>""")

A("pdf-tools/word-to-pdf.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Convert Word (.docx) toward a print-ready PDF</h2>
    <p>Word documents reflow on every screen, which is why employers and government sites ask for <strong>PDF</strong> instead. ToolFest reads your .docx locally, builds a clean preview, and uses your browser’s print dialog so you can save as PDF. Complex layouts, embedded fonts, and rare Word features may not match Microsoft Word pixel-perfect; for legal filings always double-check the preview.</p>
    <p>We never upload your manuscript, resume, or contract. That matters for NDAs, unpublished writing, and personal medical forms.</p>
    <h3>Best practices</h3>
    <ul>
      <li>Use heading styles in Word so the preview keeps logical structure.</li>
      <li>For .doc (legacy), save as .docx in Word or LibreOffice first.</li>
    </ul>
  </article>""")

A("image-tools/compress.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Compress JPG, PNG, and WebP for the web</h2>
    <p>Large images slow down blogs, Shopify stores, and school assignment portals. Compressing before upload keeps <strong>Core Web Vitals</strong> healthier and saves mobile data for visitors in India and elsewhere. Our compressor uses the browser canvas so pixels stay on your device—useful for client photos, product shots, and confidential screenshots.</p>
    <p>Batch mode compares before/after for the first file and can ZIP everything when you process many images at once. Try WebP output when transparency is not required; it often beats JPEG at the same visual quality.</p>
  </article>""")

A("image-tools/resize.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Resize images to exact pixels or percentage</h2>
    <p>Every platform publishes different size guidelines: Instagram posts, LinkedIn banners, PDF inserts, and e-commerce thumbnails all expect specific dimensions. Lock aspect ratio when you want a photo to stay natural; unlock it only when you intentionally need to stretch or squash for a template.</p>
    <p>Output format and quality sliders help balance sharpness against file weight. Processing is local, which is ideal when images include faces, addresses, or proprietary UI captures.</p>
  </article>""")

A("image-tools/convert.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Convert between JPEG, PNG, and WebP</h2>
    <p>Format choice affects transparency and file size. PNG preserves sharp edges and alpha channels; JPEG is smaller for photographs; WebP combines good compression with modern browser support. Use this converter when a portal rejects your upload type or when you need a consistent format for a slide deck.</p>
    <p>All conversion happens in your browser—no queue, no watermark from ToolFest.</p>
  </article>""")

A("image-tools/crop.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Crop images with a draggable frame</h2>
    <p>Cropping removes distractions, enforces aspect ratios for passports or profile photos, and prepares screenshots for documentation. Drag the highlighted region and resize from the corner handle, then download the cropped bitmap. For identity documents, follow the official aspect ratio and head-size rules for your country.</p>
    <p>Your original file never leaves the device; only the cropped result is saved when you click download.</p>
  </article>""")

A("finance-tools/emi-calculator.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Understand EMI before you sign a loan</h2>
    <p><strong>EMI (Equated Monthly Installment)</strong> is the fixed cash outflow that pays down both principal and interest on home loans, car loans, and personal credit lines across Indian banks and US lenders. The reducing-balance formula here matches what most amortisation schedules use: early payments skew toward interest, later ones toward principal.</p>
    <p>Enter rupees or dollars mentally—the calculator only needs consistent numbers. Compare total interest when you change tenure: shorter loans cost less interest but higher EMI. This page is <strong>educational</strong>; always verify numbers with your lender’s official statement.</p>
    <h3>Disclaimer</h3>
    <p>ToolFest does not provide financial advice. Processing fees, insurance, and floating rates are not modelled here.</p>
  </article>""")

A("finance-tools/sip-calculator.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Project SIP wealth for mutual fund planning</h2>
    <p>A <strong>systematic investment plan (SIP)</strong> deducts a fixed amount monthly into funds or baskets. This calculator assumes end-of-month contributions and a constant annual return so you can sanity-check marketing brochures. Real markets fluctuate: use conservative return assumptions for long-term goals like retirement or a child’s education in India.</p>
    <p>Increasing SIP by 10% yearly (step-up SIP) is popular but not simulated here; run multiple rows manually if you need that scenario.</p>
  </article>""")

A("finance-tools/gst-calculator.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>GST calculations for Indian invoices</h2>
    <p>Goods and Services Tax in India uses multiple slabs—commonly <strong>5%, 12%, 18%, and 28%</strong> depending on the supply. Use “exclusive” mode when your price list excludes tax and you need the total to bill a customer. Use “inclusive” mode when a receipt shows one round number and you must back out tax for accounting.</p>
    <p>Tax law changes; always confirm the applicable rate for your goods or services with a qualified accountant or the official CBIC notifications.</p>
  </article>""")

A("text-tools/word-counter.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Word and character counts for writers and SEO</h2>
    <p>Editors, students, and content marketers track <strong>word count</strong> for essays, meta descriptions, and ad copy limits. Reading time uses a 200 words-per-minute default—a middle ground for English non-fiction. Adjust expectations for Hindi, Tamil, or other languages if your audience reads slower or faster.</p>
    <p>Text is analysed locally, which is safer for unpublished chapters, legal drafts, and client briefs you should not paste into random cloud apps.</p>
  </article>""")

A("text-tools/json-formatter.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Format and validate JSON safely</h2>
    <p>API responses, config files, and mobile app payloads are easier to debug when JSON is indented consistently. Beautify for reading, minify before embedding in production bundles, and validate when an integration throws cryptic errors. Parsing uses the browser’s built-in <code>JSON.parse</code>, so secrets in your payload are not sent to ToolFest.</p>
    <p>Never paste live production keys into unknown websites; this page is meant for non-sensitive samples or already-public responses.</p>
  </article>""")

A("generators/password-generator.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Strong passwords from cryptographic randomness</h2>
    <p>Password reuse is still the fastest way to lose email, banking, and gaming accounts. This generator pulls randomness from <code>crypto.getRandomValues</code>, which is far stronger than <code>Math.random</code>. Mix uppercase, lowercase, digits, and symbols unless a site forbids certain characters.</p>
    <p>Copy passwords into a <strong>password manager</strong>; human memory cannot safely track dozens of unique secrets. ToolFest does not log generated strings.</p>
  </article>""")

A("generators/qr-code-generator.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>QR codes for menus, payments, and Wi‑Fi</h2>
    <p>Quick Response codes bridge print and mobile: restaurants link to digital menus, shops embed UPI payment strings, and offices share Wi‑Fi credentials without spelling passwords aloud. Paste any UTF-8 text; the preview updates when you generate. Download the PNG for posters or stickers.</p>
    <p>Test the code with your phone camera before mass printing. Very long payloads reduce scannability; use a short URL when possible.</p>
  </article>""")

HUB_PDF = r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Free PDF utilities hosted at toolfest.in</h2>
    <p>This hub collects every PDF workflow we ship today: <strong>Word to PDF</strong>, merging and splitting, JPG to PDF and PDF to JPG, plus a lightweight compress pass. Each tool explains its limits in plain language because PDF engines behave differently on encrypted files, forms, and scanned books.</p>
    <p>We built ToolFest for people who want <strong>privacy</strong>—students submitting coursework, lawyers handling drafts, and small business owners filing GST or IRS paperwork—without uploading sensitive files to unknown servers. If a tool errors, try printing to PDF from your desktop app as a fallback.</p>
    <h3>How to pick a tool</h3>
    <ul>
      <li>Need one file from many? Use merge.</li>
      <li>Need many files from one? Use split or PDF to JPG.</li>
      <li>Need smaller email attachments? Try compress, then split if still too large.</li>
    </ul>
  </article>"""

A("pdf-tools/index.html", HUB_PDF)

A("image-tools/index.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Image tools for creators and ecommerce sellers</h2>
    <p>Photography, social content, and marketplace listings all depend on <strong>fast-loading images</strong>. ToolFest offers compression, resizing, format conversion, and cropping without sending pixels to our infrastructure. That is important when images show products, children, or confidential UI.</p>
    <p>Start with compression when files are huge; resize when dimensions are wrong for the target platform; convert when the upload form rejects your MIME type.</p>
  </article>""")

A("finance-tools/index.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Finance calculators for loans and Indian GST</h2>
    <p>The EMI and SIP pages help you model cash flows before talking to a bank or mutual fund distributor. The GST page supports both tax-exclusive and tax-inclusive math that small shops and freelancers use daily. Numbers here are <strong>illustrative</strong>; always confirm with licensed professionals and official circulars.</p>
    <p>ToolFest (toolfest.in) publishes these calculators as general education, not regulated financial advice.</p>
  </article>""")

A("text-tools/index.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Text and JSON helpers for everyday work</h2>
    <p>Writers track word counts; developers pretty-print JSON from failing APIs. These tools run offline-capable JavaScript in your tab, which reduces the temptation to paste sensitive prose into untrusted “free formatter” sites.</p>
    <p>Bookmark this hub if you ship content or code from India, the US, or anywhere with strict data-handling expectations.</p>
  </article>""")

A("generators/index.html", r"""
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Generators for passwords and QR codes</h2>
    <p>Security and marketing teams both need quick assets: random passwords for staging accounts, QR codes for campaign landing pages. ToolFest keeps generation client-side so interim secrets are not stored in our logs.</p>
    <p>Rotate passwords after sharing QR posters publicly, and regenerate codes if URLs change.</p>
  </article>""")


def strip_ad_slots(html: str) -> str:
    html = re.sub(
        r"\s*<div class=\"ad-slot\"[^>]*>.*?</div>\s*",
        "\n",
        html,
        flags=re.DOTALL,
    )
    return html


def insert_article(path: Path, article: str) -> str:
    html = path.read_text(encoding="utf-8")
    html = strip_ad_slots(html)
    rel = path.relative_to(ROOT).as_posix()

    n1 = "  </div>\n\n  <div class=\"tool-layout\">"
    n2 = "  </div>\n\n  <div class=\"hub-grid\">"
    if n1 in html:
        return html.replace(n1, "  </div>\n\n" + article + "\n\n  <div class=\"tool-layout\">", 1)
    if n2 in html:
        return html.replace(n2, "  </div>\n\n" + article + "\n\n  <div class=\"hub-grid\">", 1)
    print("WARN: no insert point", rel)
    return html


def main() -> None:
    for rel, article in ARTICLES.items():
        p = ROOT / rel
        if not p.exists():
            print("missing", rel)
            continue
        new_html = insert_article(p, article)
        p.write_text(new_html, encoding="utf-8")
        print("updated", rel)

    # Strip ad slots from any remaining HTML (e.g. index handled separately)
    for p in ROOT.rglob("*.html"):
        if "scripts" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        t2 = strip_ad_slots(t)
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            print("stripped ads", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
