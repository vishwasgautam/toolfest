#!/usr/bin/env python3
"""Generate programmatic finance SEO pages (EMI + GST) for ToolFest.

This script creates:
- finance-tools/emi-guides/index.html
- finance-tools/gst-guides/index.html
- finance-tools/emi-guides/*.html
- finance-tools/gst-guides/*.html
- sitemap-programmatic-finance.xml
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://toolfest.in"


@dataclass(frozen=True)
class EmiCase:
    principal_lakh: int
    annual_rate: float
    years: int


@dataclass(frozen=True)
class GstCase:
    amount: int
    rate: int


def money(n: float) -> str:
    return f"{n:,.2f}"


def emi(principal: float, annual_rate: float, years: int) -> float:
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def finance_head(title: str, description: str, canonical_path: str) -> str:
    canonical = f"{SITE_URL}{canonical_path}"
    return f"""<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="../../assets/js/site-analytics.js"></script>
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{canonical}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="ToolFest" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/css/shared.css" />
  <style>
    .guide-grid {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 2rem 2.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 0.9rem;
    }}
    .guide-link {{
      display: block;
      text-decoration: none;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      color: var(--text);
      padding: 0.9rem 1rem;
      font-size: 0.87rem;
      line-height: 1.5;
    }}
    .guide-link:hover {{
      border-color: rgba(167, 139, 250, 0.45);
      background: rgba(167, 139, 250, 0.06);
    }}
    .result-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }}
    .result-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    .result-chip {{
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.85rem;
      font-size: 0.85rem;
      color: var(--muted);
    }}
    .result-chip strong {{
      display: block;
      color: var(--text);
      font-size: 0.98rem;
      margin-top: 0.15rem;
    }}
    .result-note {{
      color: var(--muted);
      font-size: 0.82rem;
      margin-top: 0.75rem;
      line-height: 1.55;
    }}
  </style>
</head>"""


def nav(active_label: str) -> str:
    def mark(label: str) -> str:
        return ' style="color:var(--text)"' if label == active_label else ""

    return f"""  <nav>
    <a href="../../" class="logo">Tool<span>Fest</span></a>
    <ul>
      <li><a href="../../pdf-tools/">PDF</a></li>
      <li><a href="../../image-tools/">Image</a></li>
      <li><a href="../../finance-tools/"{mark("Finance")}>Finance</a></li>
      <li><a href="../../text-tools/">Text</a></li>
      <li><a href="../../generators/">Generators</a></li>
      <li><a href="../../">Home</a></li>
    </ul>
  </nav>"""


def footer() -> str:
    return """  <footer>
    <div class="footer-logo">Tool<span>Fest</span></div>
    <p class="site-footer-links"><a href="../../">Home</a> · <a href="../../about.html">About</a> · <a href="../../privacy.html">Privacy</a> · <a href="../../terms.html">Terms</a></p>
    <p style="margin-top:1rem;font-size:0.78rem;opacity:0.5">© 2026 ToolFest · Educational estimates only; not financial advice.</p>
  </footer>"""


def emi_filename(case: EmiCase) -> str:
    rate = str(case.annual_rate).replace(".", "-")
    return f"emi-{case.principal_lakh}-lakh-{rate}-percent-{case.years}-years.html"


def build_emi_page(case: EmiCase) -> tuple[str, str]:
    principal = case.principal_lakh * 100000
    monthly = emi(principal, case.annual_rate, case.years)
    months = case.years * 12
    total = monthly * months
    interest = total - principal
    filename = emi_filename(case)
    path = f"/finance-tools/emi-guides/{filename}"

    title = (
        f"EMI for Rs {case.principal_lakh} Lakh at {case.annual_rate}% for "
        f"{case.years} Years | ToolFest"
    )
    description = (
        f"Check monthly EMI for Rs {case.principal_lakh} lakh loan at "
        f"{case.annual_rate}% over {case.years} years with total interest "
        "and repayment breakup."
    )

    body = f"""<!DOCTYPE html>
<html lang="en">
{finance_head(title, description, path)}
<body>
{nav("Finance")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Finance</a> <span>›</span> EMI Guides</div>
      <h1 class="page-title">EMI for Rs {case.principal_lakh} lakh at <span style="color:var(--finance-color)">{case.annual_rate}%</span></h1>
      <p class="page-desc">Quick monthly installment estimate for a {case.years}-year loan tenure. Use this as a planning baseline before bank-specific charges and insurance.</p>
    </div>
    <div class="page-hero-badge">₹</div>
  </div>

  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Result summary</h2>
    <div class="result-box">
      <div class="result-highlight">Rs {money(monthly)} / month</div>
      <div class="result-grid">
        <div class="result-chip">Principal<strong>Rs {money(principal)}</strong></div>
        <div class="result-chip">Total interest<strong>Rs {money(interest)}</strong></div>
        <div class="result-chip">Total repayment<strong>Rs {money(total)}</strong></div>
        <div class="result-chip">Tenure<strong>{months} months</strong></div>
      </div>
      <p class="result-note">Formula used: EMI = P × r × (1+r)^n / ((1+r)^n - 1), where P is principal, r is monthly interest, and n is number of months.</p>
    </div>

    <h3>How to use this result</h3>
    <ul>
      <li>Compare this EMI against your monthly take-home and existing obligations.</li>
      <li>Run adjacent scenarios with different rates or tenures in our calculator.</li>
      <li>Treat this as an estimate: lender processing fee, insurance, and prepayment rules can change final cost.</li>
    </ul>
    <p><a href="../emi-calculator.html" style="color:var(--accent)">Open full EMI calculator with custom inputs →</a></p>
    <p><a href="./index.html" style="color:var(--accent)">Browse all EMI scenario pages →</a></p>
  </article>
{footer()}
</body>
</html>
"""
    return filename, body


def build_gst_page(case: GstCase) -> tuple[str, str]:
    tax = case.amount * case.rate / 100
    inclusive = case.amount + tax
    filename = f"gst-{case.rate}-percent-on-{case.amount}.html"
    path = f"/finance-tools/gst-guides/{filename}"

    title = f"{case.rate}% GST on Rs {case.amount} | GST Breakdown ToolFest"
    description = (
        f"Calculate {case.rate}% GST on Rs {case.amount}. Get tax amount, "
        f"exclusive value, and inclusive total instantly."
    )

    body = f"""<!DOCTYPE html>
<html lang="en">
{finance_head(title, description, path)}
<body>
{nav("Finance")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Finance</a> <span>›</span> GST Guides</div>
      <h1 class="page-title">{case.rate}% GST on <span style="color:var(--finance-color)">Rs {case.amount}</span></h1>
      <p class="page-desc">Fast GST math for invoices and quotations. Works for exclusive-base pricing and quick tax-inclusive checks.</p>
    </div>
    <div class="page-hero-badge">🧾</div>
  </div>

  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>GST calculation result</h2>
    <div class="result-box">
      <div class="result-highlight">Tax amount: Rs {money(tax)}</div>
      <div class="result-grid">
        <div class="result-chip">Base amount<strong>Rs {money(case.amount)}</strong></div>
        <div class="result-chip">GST rate<strong>{case.rate}%</strong></div>
        <div class="result-chip">GST amount<strong>Rs {money(tax)}</strong></div>
        <div class="result-chip">Total (incl. GST)<strong>Rs {money(inclusive)}</strong></div>
      </div>
      <p class="result-note">Simple method: GST amount = Base × Rate / 100. Inclusive total = Base + GST.</p>
    </div>

    <h3>When this helps</h3>
    <ul>
      <li>Generating quick quotations with GST added.</li>
      <li>Checking invoice calculations before sharing with clients.</li>
      <li>Comparing tax impact across 5%, 12%, 18%, and 28% slabs.</li>
    </ul>
    <p><a href="../gst-calculator.html" style="color:var(--accent)">Open full GST calculator (inclusive + exclusive modes) →</a></p>
    <p><a href="./index.html" style="color:var(--accent)">Browse all GST scenario pages →</a></p>
  </article>
{footer()}
</body>
</html>
"""
    return filename, body


def build_emi_hub(cases: list[EmiCase]) -> str:
    links = "\n".join(
        [
            f'    <a class="guide-link" href="{emi_filename(c)}">EMI for Rs {c.principal_lakh} lakh at {c.annual_rate}% for {c.years} years</a>'
            for c in cases
        ]
    )
    title = "EMI Scenario Pages — Loan Examples by Amount, Rate, Tenure | ToolFest"
    description = (
        "Browse long-tail EMI examples by loan amount, annual interest, and tenure. "
        "Each page includes formula breakdown and links to the interactive calculator."
    )
    return f"""<!DOCTYPE html>
<html lang="en">
{finance_head(title, description, "/finance-tools/emi-guides/")}
<body>
{nav("Finance")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Finance</a> <span>›</span> EMI Guides</div>
      <h1 class="page-title">EMI scenario <span style="color:var(--finance-color)">guides</span></h1>
      <p class="page-desc">Pre-calculated EMI pages for common loan amounts and tenures searched in India. Use these pages for quick planning, then refine with the full calculator.</p>
    </div>
    <div class="page-hero-badge">🏠</div>
  </div>

  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>How these pages are useful</h2>
    <p>Each URL answers one specific search intent: principal amount + interest rate + tenure. The output includes monthly EMI, total interest, and full repayment so you can compare options quickly.</p>
    <p><a href="../emi-calculator.html" style="color:var(--accent)">Open interactive EMI calculator →</a></p>
  </article>

  <div class="guide-grid">
{links}
  </div>
{footer()}
</body>
</html>
"""


def build_gst_hub(cases: list[GstCase]) -> str:
    links = "\n".join(
        [
            f'    <a class="guide-link" href="gst-{c.rate}-percent-on-{c.amount}.html">{c.rate}% GST on Rs {c.amount}</a>'
            for c in cases
        ]
    )
    title = "GST Scenario Pages — 5%, 12%, 18%, 28% Examples | ToolFest"
    description = (
        "Browse ready GST calculations for common invoice amounts and slabs. "
        "Each page shows base amount, tax amount, and inclusive total."
    )
    return f"""<!DOCTYPE html>
<html lang="en">
{finance_head(title, description, "/finance-tools/gst-guides/")}
<body>
{nav("Finance")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Finance</a> <span>›</span> GST Guides</div>
      <h1 class="page-title">GST scenario <span style="color:var(--finance-color)">guides</span></h1>
      <p class="page-desc">Common GST calculations for India-focused pricing. Find quick 5%, 12%, 18%, and 28% tax examples by amount.</p>
    </div>
    <div class="page-hero-badge">₹</div>
  </div>

  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>What these pages include</h2>
    <p>Every page provides a clear tax breakdown with formula and practical invoice context. Use them for quick checks before sending quotations and bills.</p>
    <p><a href="../gst-calculator.html" style="color:var(--accent)">Open interactive GST calculator →</a></p>
  </article>

  <div class="guide-grid">
{links}
  </div>
{footer()}
</body>
</html>
"""


def generate_emi_cases() -> list[EmiCase]:
    principals = [5, 7, 10, 12, 15, 20, 25, 30, 40, 50]
    rates = [7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
    years = [5, 10, 15, 20]
    cases: list[EmiCase] = []
    for p in principals:
        for r in rates:
            for y in years:
                cases.append(EmiCase(p, r, y))
    return cases[:60]


def generate_gst_cases() -> list[GstCase]:
    amounts = [500, 1000, 1500, 2000, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 50000]
    rates = [5, 12, 18, 28]
    return [GstCase(a, r) for a in amounts for r in rates]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    emi_cases = generate_emi_cases()
    gst_cases = generate_gst_cases()

    emi_dir = ROOT / "finance-tools" / "emi-guides"
    gst_dir = ROOT / "finance-tools" / "gst-guides"
    emi_dir.mkdir(parents=True, exist_ok=True)
    gst_dir.mkdir(parents=True, exist_ok=True)

    urls: list[str] = [
        f"{SITE_URL}/finance-tools/emi-guides/",
        f"{SITE_URL}/finance-tools/gst-guides/",
    ]

    for case in emi_cases:
        fname, html = build_emi_page(case)
        write(emi_dir / fname, html)
        urls.append(f"{SITE_URL}/finance-tools/emi-guides/{fname}")

    for case in gst_cases:
        fname, html = build_gst_page(case)
        write(gst_dir / fname, html)
        urls.append(f"{SITE_URL}/finance-tools/gst-guides/{fname}")

    write(emi_dir / "index.html", build_emi_hub(emi_cases))
    write(gst_dir / "index.html", build_gst_hub(gst_cases))

    sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        sitemap_lines.append(
            f"  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.6</priority></url>"
        )
    sitemap_lines.append("</urlset>")
    write(ROOT / "sitemap-programmatic-finance.xml", "\n".join(sitemap_lines) + "\n")

    print(f"Generated {len(urls)} finance SEO URLs.")


if __name__ == "__main__":
    main()
