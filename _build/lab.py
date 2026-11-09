#!/usr/bin/env python3
"""Lab edition 2: a personal, work-first page in one narrow column.
Run from repo root: python3 _build/lab.py  (reuses case content from build.py)"""
import importlib.util
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("site", ROOT / "_build" / "build.py")
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)

CASES = {c["slug"]: c for c in site.CASES}
EMAIL, LINKEDIN = site.EMAIL, site.LINKEDIN


def img(file, w=1600, depth=1):
    return site.img(file, w, depth)


def srcset(file, depth=1):
    return site.srcset(file, depth)


# Proof shown on each card: only numbers Yar has stated himself.
FEATURED = [
    ("playerok", ["4M+ users", "Home page owner"]),
    ("design-system", ["2,000+ components", "4 brands", "Mockups ~2× faster"]),
]
STUDIES = [
    ("rail-ninja", ["1M+ tickets a year"]),
    ("travel-ninja", ["Built from zero"]),
    ("firebird-tours", ["B2C + B2B"]),
]
SIDE = [
    {"title": "TON Learn", "line": "Concept for a Telegram Mini App that teaches Web3 basics", "href": "../work/ton-learn/",
     "img": "z6qjIoTX3oU3K5DU6TvPd8UEPsQ.png", "cta": "See the concept"},
    {"title": "My game", "line": "A game I’m building on my own. There’s a demo with a first location and the core mechanics.",
     "pending": "Needs: name, one screenshot or GIF, one line about it"},
    {"title": "Everstrat", "line": "Logo for a DeFi product", "pending": "Needs: logo files and the brief in a sentence"},
]
TALKS = [
    ("Workshop", "The first steps towards your design system", "Galary Design, Tokyo. Hands-on Figma session, Oct 2025.",
     "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past", "11 participants"),
    ("Talk", "Intro to design systems", "Galary Design, Tokyo. Online, in English with some Japanese, Sep 2025.",
     "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past", "50 sign-ups"),
    ("Post", "When a button breaks in Russian", "A localization edge case in the Google Pixel screenshot tool, and three ways to design for it.",
     LINKEDIN + "recent-activity/all/", "LinkedIn"),
    ("Research", "Ways of the artists’ promotion in the Russian digital art market", "Bachelor’s research at HSE University, written in English, 2021.",
     "https://www.researchgate.net/publication/358564840", "ResearchGate"),
]


def head(title, desc, depth):
    pre = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="robots" content="noindex">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}lab/lab.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<main id="main" class="col">
"""


def foot():
    return f"""</main>
<footer class="col foot">
  <p>Yar Luchkin, Belgrade. Lab edition: an experiment, the main site is at <a href="https://ceoofdesign.github.io/">ceoofdesign.github.io</a>.</p>
</footer>
</body>
</html>
"""


def chips(items):
    return "".join(f'<span class="chip">{escape(t)}</span>' for t in items)


def big_card(slug, proof):
    c = CASES[slug]
    return f"""<article class="feature">
  <header class="feature-head">
    <div><h2><a href="work/{slug}/">{escape(c['title'].split(':')[0])}</a></h2><p class="sub">{escape(c['card'])}</p></div>
    <div class="chips">{chips(proof)}</div>
  </header>
  <a class="media" href="work/{slug}/" tabindex="-1" aria-hidden="true"><img src="{img(c['cover'], 2000)}"{srcset(c['cover'])} alt="" loading="lazy" width="1600" height="1000"></a>
</article>"""


def small_card(slug, proof):
    c = CASES[slug]
    return f"""<article class="card">
  <a class="media" href="work/{slug}/" tabindex="-1" aria-hidden="true"><img src="{img(c['cover'], 1024)}" alt="" loading="lazy" width="1600" height="1000"></a>
  <div class="card-body">
    <h3><a href="work/{slug}/">{escape(c['title'].split(':')[0])}</a></h3>
    <p class="sub">{escape(c['title'].split(': ', 1)[-1].capitalize())}</p>
    <div class="chips">{chips(proof)}</div>
    <a class="btn" href="work/{slug}/">Read the case study</a>
  </div>
</article>"""


def index():
    side = []
    for s in SIDE:
        if s.get("pending"):
            side.append(f"""<article class="card pending"><span class="media ph" aria-hidden="true"></span><div class="card-body"><h3>{escape(s['title'])}</h3><p class="sub">{escape(s['line'])}</p><p class="todo">{escape(s['pending'])}</p></div></article>""")
        else:
            side.append(f"""<article class="card"><a class="media" href="{s['href']}" tabindex="-1" aria-hidden="true"><img src="{img(s['img'], 1024)}" alt="" loading="lazy" width="1600" height="900"></a><div class="card-body"><h3><a href="{s['href']}">{escape(s['title'])}</a></h3><p class="sub">{escape(s['line'])}</p><a class="btn" href="{s['href']}">{escape(s['cta'])}</a></div></article>""")
    talks = "\n".join(f"""<li><a href="{u}"><span class="kind">{k}</span><span class="t">{escape(t)}</span><span class="sub">{escape(d)}</span><span class="meta">{escape(m)}</span></a></li>""" for k, t, d, u, m in TALKS)
    return head("Yar Luchkin", "Product designer in Belgrade: marketplaces, travel products and design systems.", 1) + f"""
<section class="intro">
  <p class="hello">Hi, I’m Yar. I’m a product designer in Belgrade, Serbia. I design marketplaces and travel products used by millions of people, build the design systems behind them, and run workshops for designers in Tokyo.</p>
  <p class="reach">Look through the work below, or write to me at <a href="mailto:{EMAIL}">{EMAIL}</a>, on <a href="{LINKEDIN}">LinkedIn</a> or <a href="https://t.me/ceoofdesign">Telegram</a>.</p>
</section>

<section aria-labelledby="work">
  <h2 class="section-title" id="work">Product work</h2>
  {big_card(*FEATURED[0])}
  {big_card(*FEATURED[1])}
  <div class="grid">
    {''.join(small_card(*s) for s in STUDIES)}
  </div>
</section>

<section aria-labelledby="side">
  <h2 class="section-title" id="side">Side projects</h2>
  <div class="grid">
    {''.join(side)}
  </div>
</section>

<section aria-labelledby="talks">
  <h2 class="section-title" id="talks">Talks and writing</h2>
  <ul class="list">
{talks}
  </ul>
</section>

<section class="outro">
  <p class="hello">Five years in product design, before that PR and localization for game launches. I’ve studied Japanese since 2018 and work in English.</p>
  <p class="reach"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{LINKEDIN}">LinkedIn</a> · <a href="https://t.me/ceoofdesign">Telegram</a></p>
</section>
""" + foot()


def case_page(slug, c):
    depth = 3
    pre = "../" * depth
    order = [s for s, _ in FEATURED + STUDIES]
    nxt = CASES[order[(order.index(slug) + 1) % len(order)]]
    meta = "".join(f"<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["meta"])
    body = "\n".join(f'<section class="case-sec"><h2>{h}</h2><div class="prose">{html}</div></section>' for h, html in c["sections"])
    figs = "\n".join(
        f'<figure><img src="{img(f, 2000, depth)}"{srcset(f, depth)} alt="{escape(cap or c["title"])}" loading="lazy" width="1600" height="1000">{f"<figcaption>{escape(cap)}</figcaption>" if cap else ""}</figure>'
        for f, cap, wide in c.get("gallery", []) if f != c["cover"])
    return head(f"{c['title']} | Yar Luchkin", c["card"], depth) + f"""
<p class="back"><a href="{pre}lab/">← All work</a></p>
<article class="case">
  <h1>{escape(c['title'])}</h1>
  <p class="hello">{escape(c['lede'])}</p>
  <dl class="meta-grid">{meta}</dl>
  <figure class="cover"><img src="{img(c['cover'], 2000, depth)}"{srcset(c['cover'], depth)} alt="{escape(c['cover_alt'])}" width="1600" height="1000" fetchpriority="high"></figure>
{body}
  <div class="gallery">
{figs}
  </div>
  <p class="next"><a href="../{nxt['slug']}/"><span class="sub">Next</span>{escape(nxt['title'])}</a></p>
</article>
""" + foot()


def main():
    lab = ROOT / "lab"
    lab.mkdir(exist_ok=True)
    (lab / "index.html").write_text(index(), encoding="utf-8")
    for slug, c in CASES.items():
        d = lab / "work" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(case_page(slug, c), encoding="utf-8")
    print("lab built")


if __name__ == "__main__":
    main()
