#!/usr/bin/env python3
"""Lab edition 2: a personal, work-first page in one narrow column.
Run from repo root: python3 _build/lab.py  (reuses case content from build.py)"""
import importlib.util
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

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
# One label, four languages: a working demo of the localization post.
DEMO = {
    "en": {"name": "English", "from": "From", "to": "To", "date": "Date", "a": "Lisbon", "b": "Porto", "d": "14 Mar", "btn": "Show trains"},
    "ru": {"name": "Русский", "from": "Откуда", "to": "Куда", "date": "Дата", "a": "Лиссабон", "b": "Порту", "d": "14 марта", "btn": "Показать поезда"},
    "de": {"name": "Deutsch", "from": "Von", "to": "Nach", "date": "Datum", "a": "Lissabon", "b": "Porto", "d": "14. März", "btn": "Züge anzeigen"},
    "ja": {"name": "日本語", "from": "出発", "to": "到着", "date": "日付", "a": "リスボン", "b": "ポルト", "d": "3月14日", "btn": "列車を表示"},
}
ARROW = '<svg class="arr" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h9M8.5 4l4 4-4 4" pathLength="1"/></svg>'
ARROW_OUT = '<svg class="arr" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11l6-6M6 5h5v5" pathLength="1"/></svg>'


def words(text, start=0.1, step=0.03):
    """Split a sentence into words that blur in one after another."""
    return " ".join(f'<span class="w" style="--d:{start + i * step:.2f}s">{escape(w)}</span>' for i, w in enumerate(text.split()))


def reel(slug, big):
    """Cover plus the case screens, stacked; lab.js crossfades them."""
    c = CASES[slug]
    frames = [c["cover"]] + [f for f, _, _ in c.get("gallery", []) if f.startswith("local:") and f != c["cover"]]
    w = 2000 if big else 1024
    imgs = "".join(
        f'<img src="{img(f, w)}"{srcset(f) if big else ""} alt="" loading="{"eager" if i == 0 and big else "lazy"}" width="1600" height="1000"{" class=on" if i == 0 else ""}>'
        for i, f in enumerate(frames))
    bars = "" if len(frames) < 2 else '<span class="bars">' + "".join("<i><b></b></i>" for _ in frames) + "</span>"
    return f'<a class="media reel{" big" if big else ""}" href="work/{slug}/" tabindex="-1" aria-hidden="true" data-mode="{"view" if big else "hover"}"><span class="glow"></span><span class="frames">{imgs}</span>{bars}</a>'


def demo():
    langs = "".join(f'<button type="button" role="radio" aria-checked="{"true" if k == "en" else "false"}" data-lang="{k}" lang="{k}">{escape(v["name"])}</button>' for k, v in DEMO.items())
    e = DEMO["en"]
    return f"""<section class="demo" aria-labelledby="demo-t">
  <h2 class="section-title reveal" id="demo-t">One button, four languages</h2>
  <p class="sub demo-lede">Russian and German labels run longer than English. Switch the language, then compare a button with a fixed width and one that grows with its label.</p>
  <div class="demo-box">
    <div class="demo-controls">
      <div class="seg" role="radiogroup" aria-label="Language" data-seg="lang"><span class="thumb"></span>{langs}</div>
      <div class="seg" role="radiogroup" aria-label="Button width" data-seg="fit"><span class="thumb"></span><button type="button" role="radio" aria-checked="true" data-fit="grow">Grows with label</button><button type="button" role="radio" aria-checked="false" data-fit="fixed">Fixed width</button></div>
    </div>
    <div class="stage" lang="en">
      <div class="field"><span class="fl" data-k="from">{e['from']}</span><span class="fv" data-k="a">{e['a']}</span></div>
      <div class="field"><span class="fl" data-k="to">{e['to']}</span><span class="fv" data-k="b">{e['b']}</span></div>
      <div class="field"><span class="fl" data-k="date">{e['date']}</span><span class="fv" data-k="d">{e['d']}</span></div>
      <span class="go"><span class="go-label" data-k="btn">{e['btn']}</span></span>
    </div>
    <p class="demo-read" aria-live="polite"><span class="count">{len(e['btn'])}</span> characters in the label<span class="cut">The label is cut off</span></p>
  </div>
  <script type="application/json" id="demo-data">{json.dumps(DEMO, ensure_ascii=False)}</script>
</section>"""


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
    JA_TEXT = quote("".join(sorted(set("".join(DEMO["ja"].values())))))
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
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&display=swap&text={JA_TEXT}" rel="stylesheet">
<script>document.documentElement.classList.add("js")</script>
<script src="{pre}lab/lab.js" defer></script>
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
    return f"""<article class="feature reveal">
  <header class="feature-head">
    <div><h2><a href="work/{slug}/">{escape(c['title'].split(':')[0])}</a></h2><p class="sub">{escape(c['card'])}</p></div>
    <div class="chips">{chips(proof)}</div>
  </header>
  {reel(slug, True)}
</article>"""


def small_card(slug, proof):
    c = CASES[slug]
    return f"""<article class="card reveal">
  {reel(slug, False)}
  <div class="card-body">
    <h3><a href="work/{slug}/">{escape(c['title'].split(':')[0])}</a></h3>
    <p class="sub">{escape(c['title'].split(': ', 1)[-1].capitalize())}</p>
    <div class="chips">{chips(proof)}</div>
    <a class="btn" href="work/{slug}/">{ARROW}<span>Read the case study</span></a>
  </div>
</article>"""


def index():
    side = []
    for s in SIDE:
        if s.get("pending"):
            side.append(f"""<article class="card pending reveal"><span class="media ph" aria-hidden="true"></span><div class="card-body"><h3>{escape(s['title'])}</h3><p class="sub">{escape(s['line'])}</p><p class="todo">{escape(s['pending'])}</p></div></article>""")
        else:
            side.append(f"""<article class="card reveal"><a class="media" href="{s['href']}" tabindex="-1" aria-hidden="true"><img src="{img(s['img'], 1024)}" alt="" loading="lazy" width="1600" height="900"></a><div class="card-body"><h3><a href="{s['href']}">{escape(s['title'])}</a></h3><p class="sub">{escape(s['line'])}</p><a class="btn" href="{s['href']}">{ARROW}<span>{escape(s['cta'])}</span></a></div></article>""")
    talks = "\n".join(f"""<li><a href="{u}"><span class="kind">{k}</span><span class="t">{escape(t)}</span><span class="sub">{escape(d)}</span><span class="meta">{escape(m)}{ARROW_OUT}</span></a></li>""" for k, t, d, u, m in TALKS)
    return head("Yar Luchkin", "Product designer in Belgrade: marketplaces, travel products and design systems.", 1) + f"""
<section class="intro">
  <p class="hello">{words("Hi, I’m Yar. I’m a product designer in Belgrade, Serbia. I design marketplaces and travel products used by millions of people, build the design systems behind them, and run workshops for designers in Tokyo.")}</p>
  <p class="reach rise">Look through the work below, or write to me at <a href="mailto:{EMAIL}">{EMAIL}</a>, on <a href="{LINKEDIN}">LinkedIn</a> or <a href="https://t.me/ceoofdesign">Telegram</a>.</p>
</section>

<section aria-labelledby="work">
  <h2 class="section-title reveal" id="work">Product work</h2>
  {big_card(*FEATURED[0])}
  {big_card(*FEATURED[1])}
  <div class="grid">
    {''.join(small_card(*s) for s in STUDIES)}
  </div>
</section>

{demo()}

<section aria-labelledby="side">
  <h2 class="section-title reveal" id="side">Side projects</h2>
  <div class="grid">
    {''.join(side)}
  </div>
</section>

<section aria-labelledby="talks">
  <h2 class="section-title reveal" id="talks">Talks and writing</h2>
  <ul class="list reveal">
{talks}
  </ul>
</section>

<section class="outro">
  <p class="hello reveal">Five years in product design, before that PR and localization for game launches. I’ve studied Japanese since 2018 and work in English.</p>
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
