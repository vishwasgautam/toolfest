#!/usr/bin/env python3
"""Generate programmatic converter SEO pages for ToolFest.

Creates:
- convert/index.html
- convert/length/index.html + many pages
- convert/weight/index.html + many pages
- convert/temperature/index.html + many pages
- convert/data-size/index.html + many pages
- sitemap-programmatic-converters.xml
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://toolfest.in"


def fmt_num(n: float, digits: int = 4) -> str:
    text = f"{n:.{digits}f}".rstrip("0").rstrip(".")
    return text if text else "0"


def head(title: str, description: str, canonical_path: str, up: str = "..") -> str:
    canonical = f"{SITE_URL}{canonical_path}"
    return f"""<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="{up}/assets/js/site-analytics.js"></script>
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{canonical}" />
  <meta name="robots" content="noindex, follow, max-image-preview:large" />
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
  <link rel="stylesheet" href="{up}/assets/css/shared.css" />
  <style>
    .grid {{
      max-width: 980px;
      margin: 0 auto;
      padding: 0 2rem 2.75rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 0.9rem;
    }}
    .card-link {{
      display: block;
      text-decoration: none;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      color: var(--text);
      padding: 0.95rem 1rem;
      font-size: 0.88rem;
      line-height: 1.5;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .card-link:hover {{
      border-color: rgba(71, 200, 255, 0.45);
      transform: translateY(-2px);
    }}
    .result-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }}
    .answer {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: clamp(1.45rem, 3.8vw, 2rem);
      color: var(--accent);
      letter-spacing: -0.03em;
      line-height: 1.25;
    }}
    .note {{
      color: var(--muted);
      font-size: 0.86rem;
      margin-top: 0.75rem;
      line-height: 1.6;
    }}
  </style>
</head>"""


def nav(up: str = "..") -> str:
    return f"""  <nav>
    <a href="{up}/" class="logo">Tool<span>Fest</span></a>
    <ul>
      <li><a href="{up}/pdf-tools/">PDF</a></li>
      <li><a href="{up}/image-tools/">Image</a></li>
      <li><a href="{up}/finance-tools/">Finance</a></li>
      <li><a href="{up}/text-tools/">Text</a></li>
      <li><a href="{up}/generators/">Generators</a></li>
      <li><a href="{up}/convert/" style="color:var(--text)">Converters</a></li>
      <li><a href="{up}/">Home</a></li>
    </ul>
  </nav>"""


def footer(up: str = "..") -> str:
    return f"""  <footer>
    <div class="footer-logo">Tool<span>Fest</span></div>
    <p class="site-footer-links"><a href="{up}/">Home</a> · <a href="{up}/convert/">Converters</a> · <a href="{up}/about.html">About</a> · <a href="{up}/privacy.html">Privacy</a> · <a href="{up}/terms.html">Terms</a></p>
    <p style="margin-top:1rem;font-size:0.78rem;opacity:0.5">© 2026 ToolFest</p>
  </footer>"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def page_template(
    title: str,
    description: str,
    canonical_path: str,
    breadcrumb_mid: str,
    page_title: str,
    page_desc: str,
    result_html: str,
    related_links: list[tuple[str, str]],
) -> str:
    links = "\n".join([f'      <li><a href="{href}" style="color:var(--accent)">{label}</a></li>' for href, label in related_links])
    return f"""<!DOCTYPE html>
<html lang="en">
{head(title, description, canonical_path, up="../..")}
<body>
{nav(up="../..")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Converters</a> <span>›</span> {breadcrumb_mid}</div>
      <h1 class="page-title">{page_title}</h1>
      <p class="page-desc">{page_desc}</p>
    </div>
    <div class="page-hero-badge">🔁</div>
  </div>

  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Quick answer</h2>
    {result_html}
    <h3>Related converter pages</h3>
    <ul>
{links}
    </ul>
    <p>These pages provide a fast lookup answer and formula context. For broader utility workflows, explore other ToolFest tools from the main categories.</p>
  </article>
{footer(up="../..")}
</body>
</html>
"""


def category_hub(
    cat: str,
    title: str,
    description: str,
    hero: str,
    links: list[tuple[str, str]],
) -> str:
    cards = "\n".join([f'    <a class="card-link" href="{href}">{label}</a>' for href, label in links])
    return f"""<!DOCTYPE html>
<html lang="en">
{head(title, description, f"/convert/{cat}/", up="../..")}
<body>
{nav(up="../..")}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Converters</a> <span>›</span> {hero}</div>
      <h1 class="page-title">{hero} converter pages</h1>
      <p class="page-desc">{description}</p>
    </div>
    <div class="page-hero-badge">📐</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>{hero} search-intent pages</h2>
    <p>Each page targets a specific conversion query and includes the answer, conversion formula, and links to related values for quick browsing.</p>
  </article>
  <div class="grid">
{cards}
  </div>
{footer(up="../..")}
</body>
</html>
"""


def root_hub(category_cards: list[tuple[str, str]]) -> str:
    cards = "\n".join([f'    <a class="card-link" href="{href}">{label}</a>' for href, label in category_cards])
    return f"""<!DOCTYPE html>
<html lang="en">
{head(
    "Unit Converters — Length, Weight, Temperature, Data Size | ToolFest",
    "Free converter pages for length, weight, temperature, and data size. Quick answers with formula explanations.",
    "/convert/",
)}
<body>
{nav()}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../">ToolFest</a> <span>›</span> Converters</div>
      <h1 class="page-title">Unit <span style="color:var(--accent2)">converters</span></h1>
      <p class="page-desc">Browse converter categories with quick, specific answer pages that match common search queries.</p>
    </div>
    <div class="page-hero-badge">🔄</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Conversion categories</h2>
    <p>These pages are built for practical lookups: centimeters to feet, kilograms to pounds, Celsius to Fahrenheit, and MB to GB style data-size checks.</p>
  </article>
  <div class="grid">
{cards}
  </div>
{footer()}
</body>
</html>
"""


def generate_length() -> tuple[list[tuple[str, str]], list[str]]:
    values = [140, 145, 150, 152, 155, 160, 165, 170, 172, 175, 178, 180, 182, 185, 190, 195, 200]
    links: list[tuple[str, str]] = []
    urls: list[str] = []
    for cm in values:
        inches = cm / 2.54
        feet = int(inches // 12)
        rem_in = inches - feet * 12
        slug = f"{cm}-cm-to-feet-and-inches.html"
        path = f"/convert/length/{slug}"
        html = page_template(
            title=f"{cm} cm to feet and inches | ToolFest Converter",
            description=f"Convert {cm} cm to feet and inches with formula and decimal feet answer.",
            canonical_path=path,
            breadcrumb_mid="Length",
            page_title=f"{cm} cm to feet and inches",
            page_desc="Useful for height conversion in forms, health records, and quick reference.",
            result_html=(
                f'<div class="result-box"><div class="answer">{cm} cm = {feet} ft {fmt_num(rem_in, 2)} in</div>'
                f'<p class="note">Decimal feet: {fmt_num(cm / 30.48, 4)} ft. Formula: inches = cm / 2.54, then split into feet and inches.</p></div>'
            ),
            related_links=[
                ("170-cm-to-feet-and-inches.html", "170 cm to feet/inches"),
                ("175-cm-to-feet-and-inches.html", "175 cm to feet/inches"),
                ("180-cm-to-feet-and-inches.html", "180 cm to feet/inches"),
            ],
        )
        write(ROOT / "convert" / "length" / slug, html)
        links.append((slug, f"{cm} cm to feet and inches"))
        urls.append(f"{SITE_URL}{path}")
    return links, urls


def generate_weight() -> tuple[list[tuple[str, str]], list[str]]:
    values = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]
    links: list[tuple[str, str]] = []
    urls: list[str] = []
    for kg in values:
        lbs = kg * 2.2046226218
        slug = f"{kg}-kg-to-lbs.html"
        path = f"/convert/weight/{slug}"
        html = page_template(
            title=f"{kg} kg to lbs | ToolFest Converter",
            description=f"Convert {kg} kilograms to pounds with exact factor and quick rounded values.",
            canonical_path=path,
            breadcrumb_mid="Weight",
            page_title=f"{kg} kg to lbs",
            page_desc="Handy for gym tracking, shipping estimates, and international form conversions.",
            result_html=(
                f'<div class="result-box"><div class="answer">{kg} kg = {fmt_num(lbs, 4)} lbs</div>'
                f'<p class="note">Formula: pounds = kilograms × 2.2046226218. Rounded practical value: {fmt_num(lbs, 2)} lbs.</p></div>'
            ),
            related_links=[
                ("60-kg-to-lbs.html", "60 kg to lbs"),
                ("75-kg-to-lbs.html", "75 kg to lbs"),
                ("100-kg-to-lbs.html", "100 kg to lbs"),
            ],
        )
        write(ROOT / "convert" / "weight" / slug, html)
        links.append((slug, f"{kg} kg to lbs"))
        urls.append(f"{SITE_URL}{path}")
    return links, urls


def generate_temperature() -> tuple[list[tuple[str, str]], list[str]]:
    values = [-10, -5, 0, 5, 10, 20, 25, 30, 37, 40, 50, 60, 80, 100, 120]
    links: list[tuple[str, str]] = []
    urls: list[str] = []
    for c in values:
        f = c * 9 / 5 + 32
        slug = f"{str(c).replace('-', 'minus-')}-c-to-f.html"
        path = f"/convert/temperature/{slug}"
        html = page_template(
            title=f"{c} C to F | ToolFest Temperature Converter",
            description=f"Convert {c} degrees Celsius to Fahrenheit with formula and quick result.",
            canonical_path=path,
            breadcrumb_mid="Temperature",
            page_title=f"{c} C to F",
            page_desc="Quick weather, cooking, and science conversion reference.",
            result_html=(
                f'<div class="result-box"><div class="answer">{c} C = {fmt_num(f, 2)} F</div>'
                f'<p class="note">Formula: Fahrenheit = (Celsius × 9/5) + 32.</p></div>'
            ),
            related_links=[
                ("0-c-to-f.html", "0 C to F"),
                ("37-c-to-f.html", "37 C to F"),
                ("100-c-to-f.html", "100 C to F"),
            ],
        )
        write(ROOT / "convert" / "temperature" / slug, html)
        links.append((slug, f"{c} C to F"))
        urls.append(f"{SITE_URL}{path}")
    return links, urls


def generate_data_size() -> tuple[list[tuple[str, str]], list[str]]:
    values = [1, 5, 10, 25, 50, 100, 200, 500, 700, 1024, 2048, 4096, 8192]
    links: list[tuple[str, str]] = []
    urls: list[str] = []
    for mb in values:
        gb_decimal = mb / 1000
        gib_binary = mb / 1024
        slug = f"{mb}-mb-to-gb.html"
        path = f"/convert/data-size/{slug}"
        html = page_template(
            title=f"{mb} MB to GB | ToolFest Data Size Converter",
            description=f"Convert {mb} MB to GB with decimal and binary-style values.",
            canonical_path=path,
            breadcrumb_mid="Data Size",
            page_title=f"{mb} MB to GB",
            page_desc="Useful for file upload limits, storage plans, and app settings.",
            result_html=(
                f'<div class="result-box"><div class="answer">{mb} MB = {fmt_num(gb_decimal, 4)} GB (decimal)</div>'
                f'<p class="note">Binary equivalent: {fmt_num(gib_binary, 4)} GiB-style (using 1024). Decimal GB uses 1000 MB = 1 GB.</p></div>'
            ),
            related_links=[
                ("100-mb-to-gb.html", "100 MB to GB"),
                ("500-mb-to-gb.html", "500 MB to GB"),
                ("1024-mb-to-gb.html", "1024 MB to GB"),
            ],
        )
        write(ROOT / "convert" / "data-size" / slug, html)
        links.append((slug, f"{mb} MB to GB"))
        urls.append(f"{SITE_URL}{path}")
    return links, urls


def main() -> None:
    urls = [f"{SITE_URL}/convert/"]
    category_cards = [
        ("length/", "Length converter pages (cm ↔ feet/inches)"),
        ("weight/", "Weight converter pages (kg ↔ lbs)"),
        ("temperature/", "Temperature converter pages (C ↔ F)"),
        ("data-size/", "Data size converter pages (MB ↔ GB)"),
    ]
    write(ROOT / "convert" / "index.html", root_hub(category_cards))

    length_links, length_urls = generate_length()
    weight_links, weight_urls = generate_weight()
    temp_links, temp_urls = generate_temperature()
    data_links, data_urls = generate_data_size()

    write(
        ROOT / "convert" / "length" / "index.html",
        category_hub(
            "length",
            "Length Converter Pages — cm to feet and inches | ToolFest",
            "Common height conversions from centimeters to feet and inches for forms and everyday reference.",
            "Length",
            length_links,
        ),
    )
    write(
        ROOT / "convert" / "weight" / "index.html",
        category_hub(
            "weight",
            "Weight Converter Pages — kg to lbs | ToolFest",
            "High-intent kilograms to pounds pages for quick everyday conversion.",
            "Weight",
            weight_links,
        ),
    )
    write(
        ROOT / "convert" / "temperature" / "index.html",
        category_hub(
            "temperature",
            "Temperature Converter Pages — C to F | ToolFest",
            "Quick Celsius to Fahrenheit conversions with clear formula breakdown.",
            "Temperature",
            temp_links,
        ),
    )
    write(
        ROOT / "convert" / "data-size" / "index.html",
        category_hub(
            "data-size",
            "Data Size Converter Pages — MB to GB | ToolFest",
            "Useful MB to GB lookups for upload limits, storage plans, and app settings.",
            "Data Size",
            data_links,
        ),
    )

    urls.extend([
        f"{SITE_URL}/convert/length/",
        f"{SITE_URL}/convert/weight/",
        f"{SITE_URL}/convert/temperature/",
        f"{SITE_URL}/convert/data-size/",
    ])
    urls.extend(length_urls + weight_urls + temp_urls + data_urls)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "  <!-- Programmatic converter URLs are noindex and intentionally omitted. -->",
    ]
    lines.append("</urlset>")
    write(ROOT / "sitemap-programmatic-converters.xml", "\n".join(lines) + "\n")

    print(f"Generated {len(urls)} converter SEO URLs.")


if __name__ == "__main__":
    main()
