#!/usr/bin/env python3
"""Generate programmatic health SEO pages for ToolFest.

Outputs:
- health-tools/protein/index.html + protein-for-XXkg.html
- health-tools/calorie-deficit/index.html + XXX-calorie-deficit.html
- health-tools/bmi/index.html + bmi-HHcm-WWkg.html
- sitemap-programmatic-health.xml
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://toolfest.in"


def fmt_num(n: float, digits: int = 2) -> str:
    s = f"{n:.{digits}f}".rstrip("0").rstrip(".")
    return s if s else "0"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def head(title: str, desc: str, canonical_path: str, up: str = "../..") -> str:
    canonical = f"{SITE_URL}{canonical_path}"
    return f"""<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="{up}/assets/js/site-analytics.js"></script>
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />
  <meta name="robots" content="noindex, follow, max-image-preview:large" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="ToolFest" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}/assets/css/shared.css" />
  <style>
    .guide-grid {{
      max-width: 980px;
      margin: 0 auto;
      padding: 0 2rem 2.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 0.9rem;
    }}
    .guide-link {{
      display: block;
      text-decoration: none;
      color: var(--text);
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.85rem 0.95rem;
      font-size: 0.86rem;
      line-height: 1.5;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .guide-link:hover {{
      transform: translateY(-2px);
      border-color: rgba(52, 211, 153, 0.45);
    }}
    .result-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.2rem;
    }}
    .answer {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: clamp(1.35rem, 3.6vw, 1.9rem);
      color: var(--accent);
      letter-spacing: -0.03em;
      line-height: 1.3;
    }}
    .note {{
      color: var(--muted);
      font-size: 0.84rem;
      line-height: 1.6;
      margin-top: 0.7rem;
    }}
  </style>
</head>"""


def nav(up: str = "../..") -> str:
    return f"""  <nav>
    <a href="{up}/" class="logo">Tool<span>Fest</span></a>
    <ul>
      <li><a href="{up}/pdf-tools/">PDF</a></li>
      <li><a href="{up}/image-tools/">Image</a></li>
      <li><a href="{up}/finance-tools/">Finance</a></li>
      <li><a href="{up}/text-tools/">Text</a></li>
      <li><a href="{up}/generators/">Generators</a></li>
      <li><a href="{up}/convert/">Converters</a></li>
      <li><a href="{up}/health-tools/" style="color:var(--text)">Health</a></li>
      <li><a href="{up}/">Home</a></li>
    </ul>
  </nav>"""


def footer(up: str = "../..") -> str:
    return f"""  <footer>
    <div class="footer-logo">Tool<span>Fest</span></div>
    <p class="site-footer-links"><a href="{up}/health-tools/">Health tools</a> · <a href="{up}/privacy.html">Privacy</a> · <a href="{up}/terms.html">Terms</a></p>
    <p style="font-size:0.78rem;opacity:0.5;margin-top:0.75rem">© 2026 ToolFest · Informational only, not medical advice.</p>
  </footer>"""


def disclaimer_block() -> str:
    return """    <h3>Disclaimer</h3>
    <p><strong>Informational only:</strong> this page does not diagnose or treat medical conditions. Use estimates as planning inputs and consult licensed professionals for medical or therapeutic decisions.</p>"""


def build_protein_page(weight: int) -> tuple[str, str]:
    low = weight * 0.8
    mod = weight * 1.2
    high = weight * 1.6
    fname = f"protein-for-{weight}kg.html"
    path = f"/health-tools/protein/{fname}"
    html = f"""<!DOCTYPE html>
<html lang="en">
{head(f"Protein for {weight}kg Body Weight | ToolFest", f"Daily protein estimate for {weight}kg body weight with common g/kg ranges.", path)}
<body>
{nav()}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Health</a> <span>›</span> Protein</div>
      <h1 class="page-title">Protein for <span style="color:var(--text-tool-color)">{weight}kg</span></h1>
      <p class="page-desc">Quick daily gram targets based on body weight and common activity profiles.</p>
    </div>
    <div class="page-hero-badge">🥚</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Protein range estimate</h2>
    <div class="result-box">
      <div class="answer">{fmt_num(low, 0)}g to {fmt_num(high, 0)}g / day</div>
      <p class="note">General health: {fmt_num(low, 0)}g (0.8 g/kg). Active baseline: {fmt_num(mod, 0)}g (1.2 g/kg). Strength training range: {fmt_num(high, 0)}g (1.6 g/kg).</p>
    </div>
    <p>For detailed planning with your own weight and target, use the interactive protein calculator.</p>
{disclaimer_block()}
    <p><a href="../protein-calculator.html" style="color:var(--accent)">Open protein calculator →</a></p>
  </article>
{footer()}
</body>
</html>
"""
    return fname, html


def build_deficit_page(deficit: int) -> tuple[str, str]:
    weekly = deficit * 7
    fname = f"{deficit}-calorie-deficit.html"
    path = f"/health-tools/calorie-deficit/{fname}"
    html = f"""<!DOCTYPE html>
<html lang="en">
{head(f"{deficit} Calorie Deficit Per Day | ToolFest", f"Understand a {deficit} calorie daily deficit and weekly energy gap estimate.", path)}
<body>
{nav()}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Health</a> <span>›</span> Calorie deficit</div>
      <h1 class="page-title">{deficit} calorie <span style="color:var(--text-tool-color)">deficit</span></h1>
      <p class="page-desc">Daily energy gap planning reference with a simple weekly breakdown.</p>
    </div>
    <div class="page-hero-badge">📉</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Deficit breakdown</h2>
    <div class="result-box">
      <div class="answer">{deficit} kcal/day</div>
      <p class="note">Weekly deficit equivalent: {weekly} kcal. Actual body-composition change depends on adherence, activity, NEAT, and metabolic adaptation.</p>
    </div>
{disclaimer_block()}
    <p><a href="../calorie-deficit-calculator.html" style="color:var(--accent)">Open calorie deficit calculator →</a></p>
  </article>
{footer()}
</body>
</html>
"""
    return fname, html


def bmi_category(v: float) -> str:
    if v < 18.5:
        return "Underweight range"
    if v < 25:
        return "Healthy range"
    if v < 30:
        return "Overweight range"
    return "Obesity range"


def build_bmi_page(height_cm: int, weight_kg: int) -> tuple[str, str]:
    h = height_cm / 100
    bmi = weight_kg / (h * h)
    cat = bmi_category(bmi)
    fname = f"bmi-{height_cm}cm-{weight_kg}kg.html"
    path = f"/health-tools/bmi/{fname}"
    html = f"""<!DOCTYPE html>
<html lang="en">
{head(f"BMI for {height_cm}cm and {weight_kg}kg | ToolFest", f"Check BMI for {height_cm}cm height and {weight_kg}kg weight.", path)}
<body>
{nav()}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Health</a> <span>›</span> BMI</div>
      <h1 class="page-title">BMI for <span style="color:var(--text-tool-color)">{height_cm}cm / {weight_kg}kg</span></h1>
      <p class="page-desc">Pre-calculated BMI value for a specific height and weight pair.</p>
    </div>
    <div class="page-hero-badge">⚖️</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>BMI result</h2>
    <div class="result-box">
      <div class="answer">{fmt_num(bmi, 1)}</div>
      <p class="note">Category: {cat}. Formula used: weight(kg) / height(m)^2.</p>
    </div>
{disclaimer_block()}
    <p><a href="../bmi-calculator.html" style="color:var(--accent)">Open BMI calculator with custom inputs →</a></p>
  </article>
{footer()}
</body>
</html>
"""
    return fname, html


def build_hub(
    slug: str,
    title: str,
    desc: str,
    hero_badge: str,
    links: list[tuple[str, str]],
) -> str:
    cards = "\n".join([f'    <a class="guide-link" href="{href}">{label}</a>' for href, label in links])
    return f"""<!DOCTYPE html>
<html lang="en">
{head(title, desc, f"/health-tools/{slug}/")}
<body>
{nav()}
  <div class="page-hero">
    <div class="page-hero-text">
      <div class="breadcrumb"><a href="../../">ToolFest</a> <span>›</span> <a href="../">Health</a> <span>›</span> {slug.replace('-', ' ').title()}</div>
      <h1 class="page-title">{slug.replace('-', ' ').title()} <span style="color:var(--text-tool-color)">guides</span></h1>
      <p class="page-desc">{desc}</p>
    </div>
    <div class="page-hero-badge">{hero_badge}</div>
  </div>
  <article class="publisher-content" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="author" content="ToolFest" />
    <h2>Search-intent pages</h2>
    <p>These pages answer specific queries in a concise format and link back to interactive calculators for custom values.</p>
{disclaimer_block()}
  </article>
  <div class="guide-grid">
{cards}
  </div>
{footer()}
</body>
</html>
"""


def main() -> None:
    health = ROOT / "health-tools"
    protein_dir = health / "protein"
    deficit_dir = health / "calorie-deficit"
    bmi_dir = health / "bmi"
    for d in [protein_dir, deficit_dir, bmi_dir]:
        d.mkdir(parents=True, exist_ok=True)

    urls: list[str] = [
        f"{SITE_URL}/health-tools/protein/",
        f"{SITE_URL}/health-tools/calorie-deficit/",
        f"{SITE_URL}/health-tools/bmi/",
    ]

    protein_weights = list(range(45, 125, 5))  # 16 pages
    deficit_values = list(range(200, 1050, 50))  # 17 pages
    bmi_heights = [150, 155, 160, 165, 170, 175, 180, 185]
    bmi_weights = [50, 60, 70, 80, 90]  # 40 pages

    protein_links: list[tuple[str, str]] = []
    for w in protein_weights:
        fname, html = build_protein_page(w)
        write(protein_dir / fname, html)
        protein_links.append((fname, f"Protein for {w}kg body weight"))
        urls.append(f"{SITE_URL}/health-tools/protein/{fname}")

    deficit_links: list[tuple[str, str]] = []
    for d in deficit_values:
        fname, html = build_deficit_page(d)
        write(deficit_dir / fname, html)
        deficit_links.append((fname, f"{d} calorie deficit per day"))
        urls.append(f"{SITE_URL}/health-tools/calorie-deficit/{fname}")

    bmi_links: list[tuple[str, str]] = []
    for h in bmi_heights:
        for w in bmi_weights:
            fname, html = build_bmi_page(h, w)
            write(bmi_dir / fname, html)
            bmi_links.append((fname, f"BMI for {h}cm and {w}kg"))
            urls.append(f"{SITE_URL}/health-tools/bmi/{fname}")

    write(
        protein_dir / "index.html",
        build_hub(
            "protein",
            "Protein Guides by Body Weight | ToolFest",
            "Find daily protein gram estimates by body weight and common activity factors.",
            "🥚",
            protein_links,
        ),
    )
    write(
        deficit_dir / "index.html",
        build_hub(
            "calorie-deficit",
            "Calorie Deficit Guides by Daily Target | ToolFest",
            "Browse common daily deficit levels with quick weekly energy-gap context.",
            "📉",
            deficit_links,
        ),
    )
    write(
        bmi_dir / "index.html",
        build_hub(
            "bmi",
            "BMI Guides by Height and Weight | ToolFest",
            "Pre-calculated BMI examples for common height and weight combinations.",
            "⚖️",
            bmi_links,
        ),
    )

    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "  <!-- Programmatic health URLs are noindex and intentionally omitted. -->",
    ]
    sitemap_lines.append("</urlset>")
    write(ROOT / "sitemap-programmatic-health.xml", "\n".join(sitemap_lines) + "\n")

    print(f"Generated {len(urls)} programmatic health URLs.")


if __name__ == "__main__":
    main()
