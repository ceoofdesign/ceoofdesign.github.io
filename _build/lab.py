#!/usr/bin/env python3
"""Lab edition 4: the portfolio as an open design file.
A canvas with sections and frames, a selection box that follows the cursor,
frames you can drag, and Yar's own cursor walking the visitor through the work.
Run from repo root: python3 _build/lab.py  (reuses case content from build.py)"""
import hashlib
import importlib.util
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("site", ROOT / "_build" / "build.py")
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)

CASES = {c["slug"]: c for c in site.CASES}
CONCEPTS = {c["slug"]: c for c in site.CONCEPT_PAGES}
EMAIL, LINKEDIN = site.EMAIL, site.LINKEDIN
TELEGRAM = "https://t.me/ceoofdesign"


def img(file, w=1600, depth=1):
    return site.img(file, w, depth)


def version(name):
    """Cache-busting stamp, so a new page never meets an old stylesheet."""
    return hashlib.md5((ROOT / "lab" / name).read_bytes()).hexdigest()[:8]


# Work on the canvas. Proof lines are only numbers Yar has stated himself.
# "say" is what Yar's cursor says when it points at the frame.
WORK = [
    {"slug": "playerok", "layer": "Playerok — Home", "proof": "4M+ users", "say": "The home page is mine", "span": "wide",
     "note": "Home page, seller landing and game pages of a marketplace for gamers"},
    {"slug": "design-system", "layer": "Design system — Components", "proof": "2,000+ components · 4 brands", "say": "Mockups got about 2× faster", "span": "narrow",
     "note": "One component library behind Rail Ninja, Firebird Tours, Triptile and highspeedtrains.com"},
    {"slug": "rail-ninja", "layer": "Rail Ninja — Booking", "proof": "1M+ tickets a year", "say": "Train tickets in many countries", "span": "third"},
    {"slug": "travel-ninja", "layer": "Travel Ninja — Hotels", "proof": "Built from zero", "say": "Designed end to end", "span": "third"},
    {"slug": "firebird-tours", "layer": "Firebird Tours — B2C + B2B", "proof": "Website, apps, agent tool", "say": "Travellers on one side, agents on the other", "span": "third"},
]
SIDE = [
    {"layer": "TON Learn — Concept", "title": "TON Learn", "line": "A Telegram Mini App concept that teaches Web3 basics.", "href": "../work/ton-learn/", "img": CONCEPTS["ton-learn"]["cover"]},
    {"layer": "Game — Demo", "title": "My game", "line": "A game I’m building on my own. There’s a demo with a first location and the core mechanics.", "empty": "Waiting for a screenshot or a short clip"},
    {"layer": "Everstrat — Logo", "title": "Everstrat", "line": "Logo for a DeFi product.", "empty": "Waiting for the logo files"},
]
TALKS = [
    ("Workshop", "The first steps towards your design system", "Galary Design, Tokyo. Hands-on Figma session, Oct 2025. 11 participants.",
     "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
    ("Talk", "Intro to design systems", "Galary Design, Tokyo. Online, in English with some Japanese, Sep 2025. 50 sign-ups.",
     "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
    ("Post", "When a button breaks in Russian", "A localization edge case in the Google Pixel screenshot tool, and three ways to design for it.",
     LINKEDIN + "recent-activity/all/"),
    ("Research", "Ways of the artists’ promotion in the Russian digital art market", "Bachelor’s research at HSE University, written in English, 2021.",
     "https://www.researchgate.net/publication/358564840"),
]
# One button, four languages: the localization post as a working component.
DEMO = {
    "en": {"name": "EN", "from": "From", "to": "To", "date": "Date", "a": "Lisbon", "b": "Porto", "d": "14 Mar", "btn": "Show trains"},
    "ru": {"name": "RU", "from": "Откуда", "to": "Куда", "date": "Дата", "a": "Лиссабон", "b": "Порту", "d": "14 марта", "btn": "Показать поезда"},
    "de": {"name": "DE", "from": "Von", "to": "Nach", "date": "Datum", "a": "Lissabon", "b": "Porto", "d": "14. März", "btn": "Züge anzeigen"},
    "ja": {"name": "JA", "from": "出発", "to": "到着", "date": "日付", "a": "リスボン", "b": "ポルト", "d": "3月14日", "btn": "列車を表示"},
}


def head(title, desc, depth, body_class=""):
    pre = "../" * depth
    ja = quote("".join(sorted(set("".join(v for d in DEMO.values() for v in d.values())))))
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
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500&display=swap&text={ja}" rel="stylesheet">
<link rel="stylesheet" href="{pre}lab/lab.css?v={version('lab.css')}">
<script>document.documentElement.classList.add("js")</script>
<script src="{pre}lab/lab.js?v={version('lab.js')}" defer></script>
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <a class="file" href="{pre}lab/" data-layer="Yar Luchkin">
    <svg viewBox="0 0 20 20" aria-hidden="true"><rect x="2.5" y="2.5" width="15" height="15" rx="3"/><path d="M6.5 7h7M6.5 10h7M6.5 13h4"/></svg>
    <span>Yar Luchkin <span class="dim">/ Portfolio</span></span>
  </a>
  <span class="bar-right">
    <button class="tidy" type="button" hidden>Tidy up</button>
    <a class="share" href="mailto:{EMAIL}">Write to me</a>
  </span>
</header>
<main id="main" class="canvas">
"""


def foot(depth):
    return f"""</main>
<footer class="foot">
  <p>Yar Luchkin, Belgrade. This is an experiment; the main site is at <a href="https://ceoofdesign.github.io/">ceoofdesign.github.io</a>.</p>
</footer>
<div class="sel" aria-hidden="true"><i></i><i></i><i></i><i></i><span class="sel-tag"></span></div>
<div class="tip" aria-hidden="true"></div>
<div class="yar" aria-hidden="true">
  <svg viewBox="0 0 24 24"><path d="M4 3l15 7.5-6.6 1.8L9.6 19z"/></svg>
  <span class="yar-name">Yar</span><span class="yar-say"></span>
</div>
</body>
</html>
"""


def reel(slug, w):
    c = CASES[slug]
    frames = [c["cover"]] + [f for f, _, _ in c.get("gallery", []) if f.startswith("local:") and f != c["cover"]]
    imgs = "".join(
        f'<img src="{img(f, w)}" alt="" loading="{"eager" if i == 0 else "lazy"}" width="1600" height="1000" draggable="false"{" class=on" if i == 0 else ""}>'
        for i, f in enumerate(frames))
    return f'<span class="screens">{imgs}</span>'


def frame(w):
    c = CASES[w["slug"]]
    name = c["title"].split(":")[0]
    what = c["title"].split(": ", 1)[-1]
    return f"""<article class="frame {w['span']}" data-tour="{escape(w['say'])}">
  <p class="frame-name"><span>{escape(w['layer'])}</span><span class="proof">{escape(w['proof']).replace(" · ", ", ")}</span></p>
  <a class="frame-body" href="work/{w['slug']}/" data-layer="{escape(w['layer'])}" data-drag aria-label="{escape(name)} case study">{reel(w['slug'], 2000 if w['span'] != 'third' else 1024)}</a>
  <h3><a href="work/{w['slug']}/">{escape(name)}</a></h3>
  <p class="frame-note">{escape(w.get("note") or what[0].upper() + what[1:])}</p>
</article>"""


def side_frame(s):
    if s.get("empty"):
        body = f'<span class="frame-body empty" data-layer="{escape(s["layer"])}"><span>{escape(s["empty"])}</span></span>'
        title = escape(s["title"])
    else:
        body = f'<a class="frame-body" href="{s["href"]}" data-layer="{escape(s["layer"])}" data-drag aria-label="{escape(s["title"])}"><span class="screens"><img class="on" src="{img(s["img"], 1024)}" alt="" loading="lazy" width="1600" height="900" draggable="false"></span></a>'
        title = f'<a href="{s["href"]}">{escape(s["title"])}</a>'
    return f"""<article class="frame third">
  <p class="frame-name"><span>{escape(s['layer'])}</span></p>
  {body}
  <h3>{title}</h3>
  <p class="frame-note">{escape(s['line'])}</p>
</article>"""


def demo():
    e = DEMO["en"]
    langs = "".join(f'<button type="button" role="radio" aria-checked="{"true" if k == "en" else "false"}" data-lang="{k}">{v["name"]}</button>' for k, v in DEMO.items())
    return f"""<section class="section" aria-labelledby="demo-t" data-tour="Switch it to Russian">
  <p class="section-tag" id="demo-t">One button, four languages</p>
  <div class="demo">
    <div class="demo-copy">
      <p>Russian and German labels run longer than English. In Figma terms, a button can <strong>hug</strong> its label or keep a <strong>fixed</strong> width. Switch the language and see which one survives.</p>
      <dl class="props">
        <div><dt>Language</dt><dd class="seg" role="radiogroup" aria-label="Language" data-seg="lang"><span class="thumb"></span>{langs}</dd></div>
        <div><dt>Width</dt><dd class="seg" role="radiogroup" aria-label="Button width" data-seg="fit"><span class="thumb"></span><button type="button" role="radio" aria-checked="true" data-fit="hug">Hug</button><button type="button" role="radio" aria-checked="false" data-fit="fixed">Fixed</button></dd></div>
      </dl>
      <p class="readout" aria-live="polite"><span class="count">{len(e['btn'])}</span> characters in the label<span class="cut">The label is cut off</span></p>
    </div>
    <div class="stage" lang="en" data-layer="Search bar — Component">
      <div class="field"><span class="fl" data-k="from">{e['from']}</span><span class="fv" data-k="a">{e['a']}</span></div>
      <div class="field"><span class="fl" data-k="to">{e['to']}</span><span class="fv" data-k="b">{e['b']}</span></div>
      <div class="field"><span class="fl" data-k="date">{e['date']}</span><span class="fv" data-k="d">{e['d']}</span></div>
      <span class="go"><span class="go-label" data-k="btn">{e['btn']}</span></span>
    </div>
  </div>
  <script type="application/json" id="demo-data">{json.dumps(DEMO, ensure_ascii=False)}</script>
</section>"""


def index():
    talks = "\n".join(
        f'<li><a href="{u}" data-layer="{escape(k)}"><span class="kind">{escape(k)}</span><span class="t">{escape(t)}</span><span class="d">{escape(d)}</span></a></li>'
        for k, t, d, u in TALKS)
    main_work = "\n".join(frame(w) for w in WORK)
    return head("Yar Luchkin, product designer", "Product designer in Belgrade: marketplaces, travel products and design systems.", 1, "home") + f"""
<section class="hero" data-tour="Hi! I’ll show you around">
  <h1 data-layer="Intro — Text">Hi, I’m Yar. I design marketplaces and travel products used by millions of people, build the design systems behind them, and run workshops for designers in Tokyo.</h1>
  <p class="reach">Product designer in Belgrade, Serbia. Write to me at <a href="mailto:{EMAIL}">{EMAIL}</a>, on <a href="{LINKEDIN}">LinkedIn</a> or <a href="{TELEGRAM}">Telegram</a>.</p>
  <p class="hint">Hover anything to inspect it. Drag the frames around.</p>
</section>

<section class="section" aria-labelledby="work-t">
  <p class="section-tag" id="work-t">Product work</p>
  <div class="frames">
{main_work}
  </div>
</section>

{demo()}

<section class="section" aria-labelledby="side-t">
  <p class="section-tag" id="side-t">Side projects</p>
  <div class="frames">
{''.join(side_frame(s) for s in SIDE)}
  </div>
</section>

<section class="section" aria-labelledby="talks-t" data-tour="Talks in Tokyo, in English with some Japanese">
  <p class="section-tag" id="talks-t">Talks and writing</p>
  <ul class="talks">
{talks}
  </ul>
</section>

<section class="outro">
  <p data-layer="Outro — Text">Five years in product design, before that PR and localization for game launches. I’ve studied Japanese since 2018 and work in English.</p>
  <p class="reach"><a href="mailto:{EMAIL}">{EMAIL}</a>, <a href="{LINKEDIN}">LinkedIn</a>, <a href="{TELEGRAM}">Telegram</a></p>
</section>
""" + foot(1)


def case_page(slug, c, order):
    depth = 3
    pre = "../" * depth
    nxt = CASES[order[(order.index(slug) + 1) % len(order)]] if slug in order else None
    meta = "".join(f"<div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["meta"])
    body = "\n".join(f'<section class="case-sec"><h2>{h}</h2><div class="prose">{html}</div></section>' for h, html in c["sections"])
    figs = "\n".join(
        f'<figure data-layer="{escape(cap or c["title"].split(":")[0])}"><img src="{img(f, 2000, depth)}" alt="{escape(cap or c["title"])}" loading="lazy" width="1600" height="1000">{f"<figcaption>{escape(cap)}</figcaption>" if cap else ""}</figure>'
        for f, cap, wide in c.get("gallery", []) if f != c["cover"])
    nav = f'<p class="next"><a href="../{nxt["slug"]}/"><span class="dim">Next</span> {escape(nxt["title"])}</a></p>' if nxt else ""
    return head(f"{c['title']} | Yar Luchkin", c["card"], depth, "case-page") + f"""
<article class="case">
  <p class="back"><a href="{pre}lab/">All work</a></p>
  <h1 data-layer="Title — Text">{escape(c['title'])}</h1>
  <p class="lede">{escape(c['lede'])}</p>
  <dl class="meta">{meta}</dl>
  <figure class="cover" data-layer="Cover"><img src="{img(c['cover'], 2000, depth)}" alt="{escape(c['cover_alt'])}" width="1600" height="1000" fetchpriority="high"></figure>
{body}
  <div class="gallery">
{figs}
  </div>
  {nav}
</article>
""" + foot(depth)


def main():
    lab = ROOT / "lab"
    lab.mkdir(exist_ok=True)
    (lab / "index.html").write_text(index(), encoding="utf-8")
    order = [w["slug"] for w in WORK]
    for slug, c in CASES.items():
        d = lab / "work" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(case_page(slug, c, order), encoding="utf-8")
    print("lab built")


if __name__ == "__main__":
    main()
