#!/usr/bin/env python3
"""Experimental edition of the portfolio, published under /lab/.
Run from repo root: python3 _build/lab.py  (reuses content from build.py)"""
import importlib.util
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("site", ROOT / "_build" / "build.py")
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)

CASES, TALKS, EMAIL, LINKEDIN = site.CASES, site.TALKS, site.EMAIL, site.LINKEDIN
NUMS = ["一", "二", "三", "四", "五", "六", "七", "八"]


def img(file, w=1600, depth=1):
    return site.img(file, w, depth)


def srcset(file, depth=1):
    return site.srcset(file, depth)


def head(title, desc, depth):
    pre = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="noindex">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Shippori+Mincho+B1:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}lab/lab.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <a class="bar-name" href="{pre}lab/">Yar Luchkin</a>
  <nav aria-label="Main">
    <a href="{pre}lab/#product">Product</a>
    <a href="{pre}lab/#craft">Craft</a>
    <a href="{pre}lab/#path">Path</a>
    <a href="{pre}lab/#questions">Questions</a>
    <a href="mailto:{EMAIL}">Email</a>
  </nav>
</header>
<main id="main">
"""


def foot():
    return f"""</main>
<footer class="colophon">
  <p>Yar Luchkin, product designer. Set in Shippori Mincho and IBM Plex Sans. Built by hand, hosted on GitHub Pages.</p>
</footer>
<script>
(function () {{
  var els = document.querySelectorAll('[data-tz]');
  function tick() {{
    els.forEach(function (el) {{
      try {{
        el.textContent = new Intl.DateTimeFormat('en-GB', {{ hour: '2-digit', minute: '2-digit', timeZone: el.dataset.tz }}).format(new Date());
      }} catch (e) {{}}
    }});
  }}
  tick(); setInterval(tick, 30000);
}})();
</script>
</body>
</html>
"""


def rail(ja, en_id=None):
    """Vertical Japanese label in the left rail: decorative, the English heading carries meaning."""
    return f'<p class="rail" lang="ja" aria-hidden="true">{ja}</p>'


CRAFT = [
    {"title": "TON Learn", "what": "Concept for a Telegram Mini App that teaches Web3 basics", "href": "../work/ton-learn/",
     "img": "z6qjIoTX3oU3K5DU6TvPd8UEPsQ.png", "alt": "TON Learn title slide"},
    {"title": "Everstrat", "what": "Logo for a DeFi product", "pending": "Needs: logo files and a sentence on the brief"},
    {"title": "Interium", "what": "Presentations and social visuals for Realme, SIBUR, EuroChem", "pending": "Needs: 3–4 slides or posts you are allowed to show"},
    {"title": "MRC", "what": "Brand style, print and merch for a recruitment company", "pending": "Needs: a few photos or mockups"},
]

FAQ = [
    ("Do you need a visa to work in Japan?",
     "Yes, a work visa sponsored by the employer. I hold a bachelor’s degree and have five years of professional design experience, which is the usual basis for it."),
    ("What language do you work in?",
     "English. My Japanese is around N4–N3: enough for daily life and simple conversations, not yet for work. I’ve been studying since 2018 and keep going."),
    ("What kind of role are you looking for?",
     "A product designer position in a product team, for the long run. I’m strongest in marketplaces, travel and e-commerce, and in teams that need a design system."),
    ("Where are you now?",
     "Belgrade, Serbia (UTC+1). I already work remotely with a team in another time zone."),
]


def index():
    product_rows = []
    for n, c in enumerate(CASES):
        meta = dict(c["meta"])
        period = meta.get("Period") or meta.get("Year") or ""
        company = meta.get("Company") or ""
        product_rows.append(f"""  <li>
    <a class="work-row" href="work/{c['slug']}/">
      <span class="num" lang="ja" aria-hidden="true">{NUMS[n]}</span>
      <span class="work-text">
        <span class="work-title">{escape(c['title'])}</span>
        <span class="work-line">{escape(c['card'])}</span>
        <span class="work-meta">{escape(company)}<span class="sep" aria-hidden="true"></span>{escape(period)}</span>
      </span>
      <span class="work-img"><img src="{img(c['cover'], 1024)}" alt="" loading="{'eager' if n == 0 else 'lazy'}" width="1600" height="1000"></span>
    </a>
  </li>""")
    craft_items = []
    for k in CRAFT:
        if k.get("pending"):
            craft_items.append(f"""  <li class="craft-item pending"><span class="craft-ph" aria-hidden="true"></span><h3>{escape(k['title'])}</h3><p>{escape(k['what'])}</p><p class="todo">{escape(k['pending'])}</p></li>""")
        else:
            craft_items.append(f"""  <li class="craft-item"><a href="{k['href']}"><span class="craft-img"><img src="{img(k['img'], 1024)}" alt="{escape(k['alt'])}" loading="lazy" width="1600" height="900"></span><h3>{escape(k['title'])}</h3><p>{escape(k['what'])}</p></a></li>""")
    path = "\n".join(f"""  <li><span class="when">{y}</span><span class="what"><strong>{escape(co)}</strong>{escape(r)}</span></li>""" for y, now, co, r, p in site.ROUTE)
    talks = "\n".join(f"""  <li><time datetime="{d}">{dl}</time><span><a href="{u}">{escape(t)}</a><br><span class="muted">Galary Design, Tokyo. {escape(n)}.</span></span></li>""" for d, dl, t, p, n, u in TALKS)
    faq = "\n".join(f"""  <details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>""" for q, a in FAQ)
    return head("Yar Luchkin, product designer", "Product designer: design systems, marketplaces and travel products for people across languages.", 1) + f"""
<section class="hero">
  <div class="hero-main">
    <h1>Yar Luchkin</h1>
    <p class="hero-line">Product designer. I design marketplaces and travel products for people who use them in many languages, and the design systems that hold them together.</p>
  </div>
  <p class="hero-vertical" lang="ja" aria-hidden="true">プロダクトデザイナー</p>
  <dl class="hero-facts">
    <div><dt>Now</dt><dd>Playerok, home page</dd></div>
    <div><dt>Before</dt><dd>Rail Ninja, Firebird Tours</dd></div>
    <div><dt>Belgrade</dt><dd><time data-tz="Europe/Belgrade">--:--</time></dd></div>
    <div><dt>Tokyo</dt><dd><time data-tz="Asia/Tokyo">--:--</time></dd></div>
  </dl>
</section>

<section class="part" id="product">
  {rail("第一部　プロダクト")}
  <div class="part-body">
    <header class="part-head">
      <h2>Product</h2>
      <p>Work shipped in product teams: a marketplace, train and hotel booking, and the design system behind them.</p>
    </header>
    <ol class="work-list">
{chr(10).join(product_rows)}
    </ol>
  </div>
</section>

<section class="part" id="craft">
  {rail("第二部　クラフト")}
  <div class="part-body">
    <header class="part-head">
      <h2>Craft</h2>
      <p>Identity, visuals and concepts. Smaller pieces that show how I work with type, colour and an idea.</p>
    </header>
    <ul class="craft">
{chr(10).join(craft_items)}
    </ul>
  </div>
</section>

<section class="part" id="path">
  {rail("経歴")}
  <div class="part-body">
    <header class="part-head"><h2>Path</h2><p>From PR and localization to product design.</p></header>
    <ol class="path">
{path}
    </ol>
    <div class="two">
      <div>
        <h3 class="small-head">Talks</h3>
        <ul class="plain">
{talks}
        </ul>
      </div>
      <div>
        <h3 class="small-head">Writing</h3>
        <ul class="plain">
  <li><time datetime="2021-05">May 2021</time><span><a href="https://www.researchgate.net/publication/358564840">Ways of the artists’ promotion in the Russian contemporary digital art market</a><br><span class="muted">Bachelor’s research at HSE University, in English.</span></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="part" id="questions">
  {rail("よくある質問")}
  <div class="part-body">
    <header class="part-head"><h2>Questions recruiters ask</h2></header>
    <div class="faq">
{faq}
    </div>
  </div>
</section>

<section class="part contact" id="contact">
  {rail("連絡")}
  <div class="part-body">
    <h2 class="contact-title">Write to me</h2>
    <p class="contact-links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{LINKEDIN}">LinkedIn</a><a href="https://t.me/ceoofdesign">Telegram</a></p>
  </div>
</section>
""" + foot()


def case_page(i, c):
    depth = 3
    pre = "../" * depth
    nxt = CASES[(i + 1) % len(CASES)]
    meta = "\n".join(f"<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["meta"])
    body = "\n".join(f'<section class="case-sec"><h2>{h}</h2><div class="prose">{html}</div></section>' for h, html in c["sections"])
    figs = "\n".join(
        f'<figure><img src="{img(f, 2000, depth)}"{srcset(f, depth)} alt="{escape(cap or c["title"])}" loading="lazy" width="1600" height="1000">{f"<figcaption>{escape(cap)}</figcaption>" if cap else ""}</figure>'
        for f, cap, wide in c.get("gallery", []))
    n = NUMS[i] if c in CASES else ""
    return head(f"{c['title']} | Yar Luchkin", c["card"], depth) + f"""
<article class="case">
  <header class="case-top">
    <p class="crumb"><a href="{pre}lab/#product">Product</a></p>
    <span class="case-num" lang="ja" aria-hidden="true">{n}</span>
    <h1>{escape(c['title'])}</h1>
    <p class="case-lede">{escape(c['lede'])}</p>
    <dl class="case-meta">{meta}</dl>
  </header>
  <figure class="case-cover"><img src="{img(c['cover'], 2000, depth)}"{srcset(c['cover'], depth)} alt="{escape(c['cover_alt'])}" width="1600" height="1000" fetchpriority="high"></figure>
  <div class="case-body">
{body}
  </div>
  <div class="case-gallery">
{figs}
  </div>
  <nav class="case-next" aria-label="Next case"><a href="../{nxt['slug']}/"><span class="muted">Next</span>{escape(nxt['title'])}</a></nav>
</article>
""" + foot()


def main():
    lab = ROOT / "lab"
    lab.mkdir(exist_ok=True)
    (lab / "index.html").write_text(index(), encoding="utf-8")
    for i, c in enumerate(CASES):
        d = lab / "work" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(case_page(i, c), encoding="utf-8")
    print("lab built")


if __name__ == "__main__":
    main()
