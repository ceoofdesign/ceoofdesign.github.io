#!/usr/bin/env python3
"""Builds the static portfolio. Run: python3 _build/build.py (from repo root)."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "yar.luchkin@protonmail.com"
LINKEDIN = "https://www.linkedin.com/in/yar-luchkin/"
SITE_URL = "https://ceoofdesign.github.io"


def img(file, w=1600):
    return f"https://framerusercontent.com/images/{file}?scale-down-to={w}"


CASES = [
    {
        "slug": "design-system",
        "title": "A design system for four travel products",
        "card": "One multi-brand component library behind Firebird Tours, Rail Ninja, Triptile and highspeedtrains.com.",
        "lede": "I built a shared design system so four booking products could look like themselves while running on one set of components.",
        "meta": [("Company", "Firebird Tours group"), ("Period", "2023–2026"), ("My role", "Product designer, led design system work"), ("Team", "1 junior designer, front-end developers, PMs")],
        "cover": "PuStnQIBGpmB9LFezK4gvB1uaQQ.png",
        "cover_alt": "Design system component sheets: date pickers, inputs, colour tokens and typography",
        "sections": [
            ("Context", "<p>The group runs several travel brands for a global audience: train tickets, tours and an internal tool for travel agents. Each product had grown its own UI. The same date picker existed in five versions, and developers rebuilt components for every brand.</p>"),
            ("Problem", "<p>Design and development were slowed down by inconsistency, not by a lack of ideas. Mockups took long to prepare, handoff needed many clarifications, and the same user pattern behaved differently from site to site.</p>"),
            ("What I did", "<ul><li><strong>Token structure.</strong> Set up colour, type and spacing tokens with themes per brand, so a component changes its look by switching a theme rather than being redrawn.</li><li><strong>Component library.</strong> Built and documented 2,000+ components and variants in Figma, from inputs and calendars to full booking blocks.</li><li><strong>Design–code link.</strong> Worked with front-end developers to match the Figma library to Storybook across different tech stacks.</li><li><strong>Workspace and rules.</strong> Reorganised the Figma workspace and wrote usage guidelines, then reviewed the junior designer’s work against them.</li></ul>"),
            ("Outcome", "<ul><li>Preparing UI mockups took the design team roughly half the time it used to, by our own estimate.</li><li>The system shipped in four consumer products and the internal agent tool.</li><li>Fewer review rounds and handoff questions, because patterns were decided once.</li></ul><p class=\"note\">Numbers are internal estimates; I no longer have access to the original dashboards.</p>"),
        ],
        "gallery": [],
    },
    {
        "slug": "rail-ninja",
        "title": "Rail Ninja: booking train tickets across countries",
        "card": "Search, timetables, seat choice and checkout for a train ticket platform handling over 1M tickets a year.",
        "lede": "I redesigned the booking flow of Rail Ninja, a platform where travellers buy train tickets in dozens of countries from one site.",
        "meta": [("Company", "Rail Ninja (Firebird Tours group)"), ("Period", "2023–2026"), ("My role", "Product designer"), ("Platforms", "Web, mobile web")],
        "cover": "6AyHvDjTIuqSqc1iORZHDbHZCwY.png",
        "cover_alt": "Rail Ninja booking app on a phone inside a train",
        "sections": [
            ("Context", "<p>Rail Ninja sells train tickets from many national carriers. Every carrier has its own data, classes and rules, and users are travellers who often book in a language that is not their own.</p>"),
            ("Problem", "<p>Multi-city routes, unfamiliar fare classes and a long checkout put a lot of load on users exactly where they were about to pay.</p>"),
            ("What I did", "<ul><li><strong>Booking flow.</strong> Redesigned search, timetables, multi-city routing, seat selection and checkout.</li><li><strong>Testing.</strong> Prepared A/B tests with the product team and checked hypotheses before full rollout.</li><li><strong>Route pages.</strong> Designed landing pages for popular routes that work as an entry point from search engines.</li><li><strong>System.</strong> Moved the product onto the shared design system so web and mobile behave the same way.</li></ul>"),
            ("Outcome", "<ul><li>Clearer steps and fewer decisions per screen in the checkout.</li><li>Faster feature delivery thanks to reusable components.</li><li>The platform handles over 1M tickets a year on this flow.</li></ul>"),
        ],
        "gallery": [
            ("71VYMYeZDAUaIoNmELOIOI4jRvc.png", "Search results with train classes and seat choice", True),
            ("dUHS8COcaiEUzhqN2MNxsSGm6w.png", "Route landing page: Lisbon to Albufeira", False),
            ("lDHcC6Oz78JUWJ53PUviQS8inCw.png", "Route page with search and travel tips", False),
            ("rZnYb7to9mORx35n2t32pHP8QrY.png", "Desktop and mobile versions of the search", True),
        ],
    },
    {
        "slug": "firebird-tours",
        "title": "Firebird Tours: tours for travellers and a tool for agents",
        "card": "Consumer website and apps for booking tours, plus AGORA, the internal tool travel agents work in every day.",
        "lede": "I designed the consumer side of Firebird Tours and the internal tool its travel agents use to plan and manage trips.",
        "meta": [("Company", "Firebird Tours"), ("Period", "2023–2026"), ("My role", "Product designer, led design for the tours line"), ("Platforms", "Web, iOS, Android, internal B2B tool")],
        "cover": "V0OKow5FVLjzJkm32BB4H40jm4.png",
        "cover_alt": "Firebird Tours website with tour search and destinations",
        "sections": [
            ("Context", "<p>Firebird Tours sells guided and custom tours, mostly to travellers from abroad. Agents build itineraries for clients in an internal tool called AGORA.</p>"),
            ("Problem", "<p>Two audiences, one product team. Customers needed a clearer way to find and book a trip; agents needed to handle many trips and clients without switching between tools.</p>"),
            ("What I did", "<ul><li><strong>Consumer experience.</strong> Redesigned the main journeys on the website and the mobile apps: discovery, tour pages and the client’s trip area.</li><li><strong>Agent tool.</strong> Designed new screens in AGORA for managing clients, bookings and schedules.</li><li><strong>Leading the line.</strong> Took tasks from business analysts, split them between me and a junior designer, and reviewed the work.</li><li><strong>Hotel booking.</strong> Designed a new hotel booking service end to end with analysts and engineers.</li><li><strong>CEO requests.</strong> Prototyped new product ideas on direct requests from the CEO.</li></ul>"),
            ("Outcome", "<ul><li>One visual language across the website, apps and internal tool.</li><li>Faster agent workflows in AGORA.</li><li>Shorter development cycles for new features thanks to the shared system.</li></ul>"),
        ],
        "gallery": [
            ("DQtDMHJFTbG56G3NKeIcmEAEg.png", "Home page with tour search", True),
            ("c6W2EP8u524zUerdFkkc6f8nM.png", "Client area with upcoming trips", False),
            ("dx5qhmIy7K21cSHNJAsblBl3u4.png", "Trips in the mobile app", False),
            ("UpsJ9kUhSCU8s5ztHs55KIINLUg.png", "AGORA: the agent tool for clients and schedules", True),
            ("hdeBNP0hZNkq55lezqRcITTJxI.png", "Campaign visuals for different markets", True),
        ],
    },
    {
        "slug": "ton-learn",
        "title": "TON Learn: learning Web3 inside Telegram",
        "card": "A concept for a Telegram Mini App that teaches newcomers the basics of the TON blockchain and keeps their wallets safe.",
        "lede": "A self-initiated concept: a Telegram Mini App that teaches people the basics of TON before they lose money to a phishing link.",
        "tag": "Concept",
        "meta": [("Type", "Personal concept"), ("Year", "2025"), ("My role", "Idea, research, UX and UI"), ("Platform", "Telegram Mini App")],
        "cover": "z6qjIoTX3oU3K5DU6TvPd8UEPsQ.png",
        "cover_alt": "TON Learn title slide",
        "sections": [
            ("Context", "<p>The idea came to me at the TON Society Balkans kick-off in Belgrade in January 2025. People new to TON kept asking the same questions, and many had already met phishing bots.</p>"),
            ("Problem", "<p>Knowledge about TON is spread across chats and docs, and newcomers learn about wallet security too late. Asking them to install another app adds one more barrier.</p>"),
            ("What I did", "<ul><li><strong>Format.</strong> Chose a Telegram Mini App so learning happens where people already are.</li><li><strong>Content structure.</strong> Broke smart contracts, wallets and jettons into short lessons with quizzes.</li><li><strong>Motivation.</strong> Designed rewards with TON Society badges for finished courses.</li><li><strong>UI.</strong> Built mobile patterns that follow Telegram’s own look.</li></ul>"),
            ("Outcome", "<p>A proof of concept and pitch presented to the community. It is not a shipped product.</p>"),
        ],
        "gallery": [
            ("nB0t5UE8o4VBlileQbR05RRyM.png", "About the project and why it matters", True),
            ("QrNj8ceb6lg3GhZkuPci09V0c8.png", "Value for the ecosystem", True),
            ("Yr0QR2b31zMxjHTkyr18AMcirWU.png", "", True),
            ("p3upPCO7aBDSXoPDITL0foRe7EM.png", "", True),
            ("zotC5hA2T0ILN5zYjBR5mGTu3Ss.png", "", True),
            ("oSv1xaabQ764oPysOmN33GEReo.png", "", True),
            ("clo5Rkb25wjEZaAHVtoLTJQUAhg.png", "", True),
        ],
    },
]

TALKS = [
    ("2025-10-01", "1 Oct 2025", "The first steps towards your design system",
     "Hands-on workshop: we built a small design system in Figma together, from foundations to the first documented components. Online, in English.",
     "11 participants", "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
    ("2025-09-02", "2 Sep 2025", "Intro to design systems",
     "What separates a UI kit from a design system, why teams need one, and how to start. Online, in English.",
     "50 sign-ups", "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
]

ROUTE = [
    ("2026–now", True, "Playerok", "Product designer · contract, remote",
     "C2C marketplace for digital goods with 4M+ users and 250k+ listings. I design the home page, event sections and catalogue screens, and audit the purchase flow with PMs and the design lead."),
    ("2023–2026", False, "Firebird Tours", "Product designer, led design for the tours line",
     "Travel-tech group behind Rail Ninja, Triptile and highspeedtrains.com. Built the multi-brand design system, a hotel booking service and worked with one junior designer."),
    ("2023", False, "Interium", "Senior project lead, then deputy director",
     "Communications agency in Moscow. Ran Design Factory 2.0, a national design competition, and led social media rebrands for federal and city public-sector clients."),
    ("2022–2023", False, "GK MRC", "In-house designer",
     "HR and staffing company. Ads, landing pages, branding and merch; also ran ad campaigns and worked with print vendors."),
    ("2021–2023", False, "Interium", "Freelance designer",
     "Presentations and social media visuals for brands like Realme, SIBUR and EuroChem."),
    ("2021", False, "LVL UP", "PR and localization, project contract",
     "Adapted English press kits for game launches by EA and Garena for the Russian-speaking market."),
]


def head(title, desc, path, depth, pre=None):
    pre = ("../" * depth) if pre is None else pre
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{img('vSUKcOv5HLFiU26d20RjwUamEXE.png', 1200)}">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=IBM+Plex+Sans+JP:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
  <a class="brand" href="{pre}">Yar Luchkin</a>
  <nav class="site-nav" aria-label="Main">
    <a href="{pre}#work">Work</a>
    <a href="{pre}#talks">Talks</a>
    <a href="{pre}#experience">Experience</a>
    <a href="{pre}#about">About</a>
    <a href="mailto:{EMAIL}">Email</a>
  </nav>
</div></header>
<main id="main">
"""


def foot():
    return f"""</main>
<footer class="site-foot" id="contact"><div class="wrap">
  <div>
    <h2>Let’s talk</h2>
    <p>Open to product design roles in Japan, with relocation.</p>
  </div>
  <div class="links">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="{LINKEDIN}">LinkedIn</a>
    <a href="https://t.me/ceoofdesign">Telegram</a>
  </div>
</div></footer>
</body>
</html>
"""


def index():
    cards = []
    for c in CASES:
        tag = f'<span class="tag">{c["tag"]}</span>' if c.get("tag") else ""
        period = dict(c["meta"]).get("Period") or dict(c["meta"]).get("Year")
        company = dict(c["meta"]).get("Company") or dict(c["meta"]).get("Type")
        cards.append(f"""  <a class="case-card" href="work/{c['slug']}/">
    <figure><img src="{img(c['cover'], 1024)}" alt="{escape(c['cover_alt'])}" loading="lazy" width="1600" height="1200"></figure>
    <h3>{escape(c['title'])}{tag}</h3>
    <p>{escape(c['card'])}</p>
    <p class="meta">{escape(company)}, {escape(period)}</p>
  </a>""")
    talks = "\n".join(
        f"""  <li><time datetime="{d}">{dl}</time><div><h3><a href="{u}">{escape(t)}</a></h3><p>{escape(p)}</p></div><span class="count">{n}</span></li>"""
        for d, dl, t, p, n, u in TALKS)
    route = "\n".join(
        f"""  <li class="{'now' if now else ''}"><span class="years">{y}</span><span class="stop" aria-hidden="true"></span><div><h3>{escape(co)}</h3><p class="role">{escape(r)}</p><p>{escape(p)}</p></div></li>"""
        for y, now, co, r, p in ROUTE)
    return head("Yar Luchkin, product designer", "Product designer for marketplaces and travel products. Design systems, booking flows, products for a global audience. Relocating to Japan.", "/", 0) + f"""<div class="wrap">

<section class="sign" aria-label="Introduction">
  <div class="sign-body">
    <span class="sign-number" aria-hidden="true">PD<b>01</b></span>
    <p class="sign-kana" lang="ja">ヤル・ルチキン</p>
    <h1 class="sign-roman">Yar Luchkin</h1>
    <p class="sign-sub"><span lang="ja">プロダクトデザイナー</span> · Product designer</p>
  </div>
  <div class="sign-bar">
    <span class="from"><small lang="ja">ベオグラード</small><strong>Belgrade</strong></span>
    <span class="here" aria-hidden="true"></span>
    <span class="to"><small lang="ja">東京</small><strong>Tokyo</strong></span>
  </div>
</section>

<section class="intro" aria-label="About me in short">
  <div>
    <p class="lede">I design marketplaces and travel products used by millions of people, and the design systems that keep them consistent.</p>
    <p>Right now I work on Playerok, a marketplace for digital goods with 4M+ users. Before that I led product design for the tours line at Firebird Tours, the group behind Rail Ninja, and built their multi-brand design system.</p>
    <p>My background is in advertising and intercultural communication, so I design for people who use a product in their second or third language. I’m looking for a product design role in Japan.</p>
    <div class="actions">
      <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
      <a class="btn" href="{LINKEDIN}">LinkedIn</a>
    </div>
  </div>
  <dl class="facts">
    <div><dt>Based in</dt><dd>Belgrade, Serbia</dd></div>
    <div><dt>Looking for</dt><dd>Product design roles in Japan, with relocation</dd></div>
    <div><dt>Focus</dt><dd>Design systems, booking and checkout flows, marketplaces</dd></div>
    <div><dt>Languages</dt><dd>English, professional<br>Japanese, intermediate (N4–N3) and improving<br>Russian, native</dd></div>
    <div><dt>Education</dt><dd>BA in Advertising and PR, HSE University, Moscow</dd></div>
  </dl>
</section>

<section class="section" id="work">
  <h2>Selected work</h2>
  <p class="section-note">Three products I worked on for over two years and one personal concept.</p>
  <div class="work">
{chr(10).join(cards)}
  </div>
</section>

<section class="section" id="talks">
  <h2>Talks and workshops</h2>
  <p class="section-note">I speak at <a href="https://www.meetup.com/galary-ux-ui-design-community/">Galary Design</a>, a Tokyo community of about 660 UX/UI designers.</p>
  <ul class="talks">
{talks}
  </ul>
</section>

<section class="section" id="experience">
  <h2>Experience</h2>
  <p class="section-note">Five years, from communications to product design.</p>
  <ol class="route">
{route}
  </ol>
</section>

<section class="section about" id="about">
  <figure>
    <img src="{img('OZzROdC4GEyMwq6nO2KbI7fP9Vs.jpg', 1024)}" alt="Yar sitting next to a cat" loading="lazy" width="1024" height="1301">
    <figcaption>Me, and a cat who did not ask to be in the picture.</figcaption>
  </figure>
  <div>
    <h2 style="font-size:clamp(26px,3.4vw,36px);margin:0 0 16px;font-weight:600;letter-spacing:-0.02em">About</h2>
    <p>I started in PR and advertising, localizing game launches and running campaigns, and moved into design through agency work. That path shows in how I work: I care about who reads the screen, in which language, and what they need to decide.</p>
    <p>In product teams I usually sit between design and engineering. I like turning a messy set of screens into a system that a team can grow without me.</p>
    <p>I’ve been to Japan twice and study Japanese every week. I work in English and Figma, and I’m comfortable with ProtoPie, Framer and Adobe tools.</p>
  </div>
</section>

</div>
""" + foot()


def case_page(i, c):
    nxt = CASES[(i + 1) % len(CASES)]
    meta = "\n".join(f"    <div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["meta"])
    body = "\n".join(f'  <h2>{h}</h2>\n  <div class="block">{html}</div>' for h, html in c["sections"])
    gallery = ""
    if c["gallery"]:
        figs = []
        for f, cap, wide in c["gallery"]:
            capt = f"<figcaption>{escape(cap)}</figcaption>" if cap else ""
            alt = cap or f"{c['title']}, slide"
            figs.append(f'  <figure class="{"wide" if wide else ""}"><img src="{img(f)}" alt="{escape(alt)}" loading="lazy" width="1600" height="1200">{capt}</figure>')
        gallery = '<div class="gallery">\n' + "\n".join(figs) + "\n</div>"
    tag = f' <span class="tag">{c["tag"]}</span>' if c.get("tag") else ""
    return head(f"{c['title']} | Yar Luchkin", c["card"], f"/work/{c['slug']}/", 2) + f"""<div class="wrap">
<header class="case-head">
  <p class="crumb"><a href="../../#work">Work</a>{tag}</p>
  <h1>{escape(c['title'])}</h1>
  <p class="lede">{escape(c['lede'])}</p>
  <dl class="case-meta">
{meta}
  </dl>
</header>
<figure class="case-cover"><img src="{img(c['cover'])}" alt="{escape(c['cover_alt'])}" width="1600" height="1200"></figure>
<div class="case-body">
{body}
</div>
{gallery}
<nav class="next" aria-label="More work">
  <a href="../../#work"><small>Back</small>All work</a>
  <a href="../{nxt['slug']}/" style="text-align:right"><small>Next case</small>{escape(nxt['title'])}</a>
</nav>
</div>
""" + foot()


def main():
    (ROOT / "index.html").write_text(index(), encoding="utf-8")
    for i, c in enumerate(CASES):
        d = ROOT / "work" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(case_page(i, c), encoding="utf-8")
    (ROOT / "404.html").write_text(
        head("Page not found | Yar Luchkin", "Page not found", "/404.html", 0, pre="/")
        + '<div class="wrap"><section class="section"><h2>This page doesn’t exist</h2><p class="section-note">The link may be from the old site. <a href="/">Go to the home page</a>.</p></section></div>' + foot(),
        encoding="utf-8")
    print("built")


if __name__ == "__main__":
    main()
