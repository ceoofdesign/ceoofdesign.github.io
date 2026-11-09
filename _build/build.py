#!/usr/bin/env python3
"""Builds the static portfolio. Run: python3 _build/build.py (from repo root)."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "yar.luchkin@protonmail.com"
LINKEDIN = "https://www.linkedin.com/in/yar-luchkin/"
SITE_URL = "https://ceoofdesign.github.io"


def img(file, w=1600, depth=0):
    if file.startswith("local:"):
        name = file[6:]
        suffix = "-1000" if w <= 1024 else ""
        return f"{'../' * depth}assets/img/{name}{suffix}.webp"
    return f"https://framerusercontent.com/images/{file}?scale-down-to={w}"


def srcset(file, depth=0):
    if file.startswith("local:"):
        return f' srcset="{img(file, 1000, depth)} 1000w, {img(file, 2000, depth)} 2000w" sizes="(max-width: 820px) 100vw, 1080px"'
    return ""


CASES = [
    {
        "slug": "playerok",
        "title": "Playerok: the storefront of a marketplace for gamers",
        "card": "The home page, seller landing and game pages of a C2C marketplace for in-game items, accounts and top-ups with 4M+ users.",
        "lede": "I own the design of Playerok’s home page and work on the pages that bring buyers and sellers in: the seller landing and the game and app pages.",
        "meta": [("Company", "Playerok"), ("Period", "2026–now"), ("My role", "Product designer, contract"), ("Team", "Design lead, product managers, developers")],
        "cover": "local:playerok/home",
        "cover_alt": "Playerok home page with a prize draw banner and a row of games",
        "sections": [
            ("Context", "<p>Playerok is a marketplace where players buy and sell in-game currency, accounts, items, subscriptions and top-ups. It serves the Russian-speaking market, has more than 4 million users and over 250,000 listings across 1,200+ games and apps.</p>"),
            ("Problem", "<p>One home page has to work for two very different visits. Some people come for a quick top-up and want to pay in seconds. Others browse thousands of offers from different sellers. Sellers, in turn, need a reason to list here rather than somewhere else.</p>"),
            ("What I did", "<ul><li><strong>Home page.</strong> I’m responsible for its structure: event banners on top, a row of popular games, a quick top-up block, category tabs and the listing grid, plus the sections for seasonal events.</li><li><strong>Seller landing.</strong> Work on the page that turns buyers into sellers: what you can sell, the games available and how much you earn after the commission.</li><li><strong>Game and app pages.</strong> Pages like PUBG Mobile UC combine Playerok’s own instant offers at the top with the full list of seller offers, filters and sorting below.</li><li><strong>Consistency.</strong> Audit the purchase flow and core sections with the PMs and the design lead to remove inconsistencies.</li></ul>"),
            ("Outcome", "<p>Everything shown here is live at <a href=\"https://playerok.com/\">playerok.com</a>. The screenshots were taken from the production site in November 2026.</p>"),
        ],
        "gallery": [
            ("local:playerok/seller", "Seller landing: the main offer", True),
            ("local:playerok/seller-calc", "Seller landing: earnings calculator and premium listing", True),
            ("local:playerok/category", "Game page: PUBG Mobile UC with an instant purchase block", True),
        ],
    },
    {
        "slug": "design-system",
        "title": "A design system for four travel products",
        "card": "One multi-brand component library behind Rail Ninja, Firebird Tours, Triptile and highspeedtrains.com.",
        "lede": "I built a shared design system so four booking products could look like themselves while running on one set of components.",
        "meta": [("Company", "Firebird Tours, Rail Ninja"), ("Period", "2023–2026"), ("My role", "Product designer, led design system work"), ("Team", "1 junior designer, front-end developers, PMs")],
        "cover": "PuStnQIBGpmB9LFezK4gvB1uaQQ.png",
        "cover_alt": "Design system component sheets: date pickers, inputs, colour tokens and typography",
        "sections": [
            ("Context", "<p>The group runs several travel brands for a global audience: train tickets, tours and an internal tool for travel agents. Each product had grown its own UI, and developers often rebuilt the same component for every brand.</p>"),
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
        "lede": "I redesigned the booking flow of Rail Ninja, a platform where travellers buy train tickets in many countries from one site.",
        "meta": [("Company", "Rail Ninja (Firebird Tours group)"), ("Period", "2023–2026"), ("My role", "Product designer"), ("Platforms", "Web, mobile web")],
        "cover": "local:rail-ninja/cover",
        "cover_alt": "Rail Ninja booking app on a phone inside a train",
        "sections": [
            ("Context", "<p>Rail Ninja sells train tickets from many national carriers. Every carrier has its own data, classes and rules, and users are travellers who often book in a language that is not their own.</p>"),
            ("Problem", "<p>Multi-city routes, unfamiliar fare classes and a long checkout put a lot of load on users exactly where they were about to pay.</p>"),
            ("What I did", "<ul><li><strong>Booking flow.</strong> Redesigned search, timetables, multi-city routing, seat selection and checkout.</li><li><strong>Testing.</strong> Prepared A/B tests with the product team and checked hypotheses before full rollout.</li><li><strong>Route pages.</strong> Designed landing pages for popular routes that work as an entry point from search engines.</li><li><strong>System.</strong> Moved the product onto the shared design system so web and mobile behave the same way.</li></ul>"),
            ("Outcome", "<ul><li>Clearer steps and fewer decisions per screen in the checkout.</li><li>Faster feature delivery thanks to reusable components.</li><li>The platform handles over 1M tickets a year on this flow.</li></ul>"),
        ],
        "gallery": [
            ("local:rail-ninja/search", "Home page and the mobile search", True),
            ("local:rail-ninja/seats", "Timetable with classes, seats and prices on one screen", True),
            ("local:rail-ninja/route", "Route landing page: Lisbon to Albufeira", False),
            ("local:rail-ninja/route-detail", "Route page with trains, travel time and popular routes", False),
        ],
    },
    {
        "slug": "travel-ninja",
        "title": "Travel Ninja: hotel booking built from scratch",
        "card": "A new hotel booking service for the Rail Ninja family: from search and the hotel page to choosing a room and paying.",
        "lede": "I designed Travel Ninja, the group’s new hotel booking service, end to end: search, hotel pages, rooms and checkout.",
        "meta": [("Company", "Firebird Tours group"), ("Period", "2023–2026"), ("My role", "Product designer"), ("Team", "Business analysts, developers")],
        "cover": "local:travel-ninja/cover",
        "cover_alt": "Travel Ninja home page with hotel search",
        "sections": [
            ("Context", "<p>Rail Ninja customers already booked trains through the group. Travel Ninja added hotels, with inventory from Expedia, so travellers could plan the rest of the trip in the same place.</p>"),
            ("Problem", "<p>A hotel search has to show a lot at once: price, location, rating, room types and the rules of each rate. People compare many options and leave if paying feels risky.</p>"),
            ("What I did", "<ul><li><strong>Search.</strong> Results list with a map, filters by price, rating and property type, and clear total prices.</li><li><strong>Hotel page.</strong> Gallery, amenities, location and reviews in one view, with the reserve button always in reach.</li><li><strong>Rooms.</strong> Room cards that show beds, size, view and cancellation rules side by side.</li><li><strong>Checkout.</strong> A one-page booking form with the order summary next to it and a clear breakdown of taxes and fees.</li><li><strong>System.</strong> Built on the shared design system, so the product launched with the same components as Rail Ninja.</li></ul>"),
            ("Outcome", "<p>The service launched as part of the group’s products. The live site has changed since then; these are my original designs.</p>"),
        ],
        "gallery": [
            ("local:travel-ninja/home", "Home page with search and popular destinations", True),
            ("local:travel-ninja/search", "Search results for Tokyo with filters and a map", True),
            ("local:travel-ninja/hotel", "Hotel page: gallery, amenities and location", True),
            ("local:travel-ninja/rooms", "Choosing a room", True),
            ("local:travel-ninja/checkout", "Secure booking: guest details, payment and price summary", True),
        ],
    },
    {
        "slug": "firebird-tours",
        "title": "Firebird Tours: tours for travellers and a tool for agents",
        "card": "Consumer website and apps for booking tours, plus AGORA, the internal tool travel agents work in every day.",
        "lede": "I designed the consumer side of Firebird Tours and the internal tool its travel agents use to plan and manage trips.",
        "meta": [("Company", "Firebird Tours"), ("Period", "2023–2026"), ("My role", "Product designer, led design for the tours line"), ("Platforms", "Web, iOS, Android, internal B2B tool")],
        "cover": "local:firebird/cover",
        "cover_alt": "Firebird Tours website: home page, tour pages and the client area",
        "sections": [
            ("Context", "<p>Firebird Tours sells guided and custom tours, mostly to travellers from abroad. Agents build itineraries for clients in an internal tool called AGORA.</p>"),
            ("Problem", "<p>Two audiences, one product team. Customers needed a clearer way to find and book a trip; agents needed to handle many trips and clients without switching between tools.</p>"),
            ("What I did", "<ul><li><strong>Consumer experience.</strong> Redesigned the main journeys on the website and the mobile apps: discovery, tour pages and the client’s trip area.</li><li><strong>Agent tool.</strong> Designed new screens in AGORA for managing clients, bookings and schedules.</li><li><strong>Leading the line.</strong> Took tasks from business analysts, split them between me and a junior designer, and reviewed the work.</li><li><strong>Hotel booking.</strong> Designed a new hotel booking service end to end with analysts and engineers.</li><li><strong>CEO requests.</strong> Prototyped new product ideas on direct requests from the CEO.</li></ul>"),
            ("Outcome", "<ul><li>One visual language across the website, apps and internal tool.</li><li>Faster agent workflows in AGORA.</li><li>Shorter development cycles for new features thanks to the shared system.</li></ul>"),
        ],
        "gallery": [
            ("local:firebird/home", "Home page with tour search and destinations", True),
            ("local:firebird/trips", "Client area with booked trips", False),
            ("local:firebird/mobile", "Trips and tour style quiz in the mobile app", False),
            ("local:firebird/agora", "AGORA: offers, orders, schedule and payouts for a guide", True),
        ],
    }
]

CONCEPT_PAGES = [
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

CONCEPTS = [
    {
        "id": "novi-prostor",
        "title": "Novi Prostor",
        "what": "Website for a premium real estate developer in Belgrade",
        "text": "A dark, quiet site where the properties do the talking: a curated portfolio, the services behind each sale, and a refurbishment case told in numbers. I wanted to see how far restraint can go on a page that sells million-euro flats.",
        "images": [("local:concepts/novi-1", "Home page"), ("local:concepts/novi-2", "Portfolio of properties"), ("local:concepts/novi-3", "Services"), ("local:concepts/novi-4", "Project story")],
    },
    {
        "id": "zrno-tok",
        "title": "Zrno & Tok",
        "what": "Brand identity for a speciality coffee roaster",
        "text": "Logo, colour, type and packaging for an imaginary Belgrade roaster. The system pairs a classic serif with a technical mono, so the same brand can feel warm on a cup and precise on a roast label.",
        "images": [("local:concepts/zrno-1", "Logo and grid"), ("local:concepts/zrno-2", "Colour and typography"), ("local:concepts/zrno-3", "Packaging"), ("local:concepts/zrno-4", "Cups, menu and loyalty card")],
    },
    {
        "id": "routify",
        "title": "Routify",
        "what": "Landing page for a logistics SaaS",
        "text": "A B2B landing page for fleet dispatch software in the Balkans. The challenge was to explain a dense product without a wall of features: one metric dashboard, one dispatch view, and every claim tied to a screen.",
        "images": [("local:concepts/routify-1", "First screen"), ("local:concepts/routify-2", "Metrics"), ("local:concepts/routify-3", "Dispatch workspace"), ("local:concepts/routify-4", "Automation features")],
    },
]

TALKS = [
    ("2025-10-01", "1 Oct 2025", "The first steps towards your design system",
     "Hands-on workshop: we built a small design system in Figma together, from foundations to the first documented components. Online, in English, with Japanese where it helped participants.",
     "11 participants", "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
    ("2025-09-02", "2 Sep 2025", "Intro to design systems",
     "What separates a UI kit from a design system, why teams need one, and how to start. Online, in English, with Japanese where it helped participants.",
     "50 sign-ups", "https://www.meetup.com/galary-ux-ui-design-community/events/?type=past"),
]

ROUTE = [
    ("2026–now", True, "Playerok", "Product designer, contract, remote",
     "C2C marketplace for in-game items and top-ups with 4M+ users. I own the home page and work on the seller landing and game pages with the PMs and the design lead."),
    ("2023–2026", False, "Rail Ninja, Firebird Tours", "Product designer, led design for the tours line",
     "Travel-tech group behind Rail Ninja, Travel Ninja, Triptile and highspeedtrains.com. Built the multi-brand design system and the Travel Ninja hotel booking service; guided one junior designer. Hybrid, Belgrade."),
    ("2023", False, "Interium", "Senior project lead, then deputy director",
     "Communications agency in Moscow. Ran Design Factory 2.0, a national design competition, and led social media rebrands for federal and city public-sector clients."),
    ("2022–2023", False, "MRC (Alliance LLC)", "In-house designer",
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
    <p>Write to me about product design work.</p>
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
    for n, c in enumerate(CASES):
        tag = f'<span class="tag">{c["tag"]}</span>' if c.get("tag") else ""
        period = dict(c["meta"]).get("Period") or dict(c["meta"]).get("Year")
        company = dict(c["meta"]).get("Company") or dict(c["meta"]).get("Type")
        cards.append(f"""  <a class="case-card{' featured' if n == 0 else ''}" href="work/{c['slug']}/">
    <figure><img src="{img(c['cover'], 1024)}" alt="{escape(c['cover_alt'])}" loading="lazy" width="1600" height="1200"></figure>
    <h3>{escape(c['title'])}{tag}</h3>
    <p>{escape(c['card'])}</p>
    <p class="meta">{escape(company)}, {escape(period)}</p>
  </a>""")
    concept_blocks = []
    ton = CONCEPT_PAGES[0]
    concept_blocks.append(f"""  <article class="concept" id="ton-learn">
    <div class="concept-text"><h3><a href="work/{ton['slug']}/">TON Learn</a></h3><p class="what">Telegram Mini App that teaches Web3 basics</p><p>{escape(ton['card'])}</p><p><a href="work/{ton['slug']}/">Read the case</a></p></div>
    <figure><img src="{img(ton['cover'], 1024)}" alt="{escape(ton['cover_alt'])}" loading="lazy" width="1600" height="900"></figure>
  </article>""")
    for k in CONCEPTS:
        figs = "".join(f'<figure><img src="{img(f, 1000)}"{srcset(f)} alt="{escape(k["title"] + ": " + cap)}" loading="lazy" width="1600" height="880"><figcaption>{escape(cap)}</figcaption></figure>' for f, cap in k["images"])
        concept_blocks.append(f"""  <article class="concept" id="{k['id']}">
    <div class="concept-text"><h3>{escape(k['title'])}</h3><p class="what">{escape(k['what'])}</p><p>{escape(k['text'])}</p></div>
    <div class="concept-images">{figs}</div>
  </article>""")
    concepts = "\n".join(concept_blocks)
    talks = "\n".join(
        f"""  <li><time datetime="{d}">{dl}</time><div><h3><a href="{u}">{escape(t)}</a></h3><p>{escape(p)}</p></div><span class="count">{n}</span></li>"""
        for d, dl, t, p, n, u in TALKS)
    route = "\n".join(
        f"""  <li class="{'now' if now else ''}"><span class="years">{y}</span><span class="stop" aria-hidden="true"></span><div><h3>{escape(co)}</h3><p class="role">{escape(r)}</p><p>{escape(p)}</p></div></li>"""
        for y, now, co, r, p in ROUTE)
    return head("Yar Luchkin, product designer", "Product designer for marketplaces and travel products: design systems, booking flows and products for people across languages.", "/", 0) + f"""<div class="wrap">

<section class="sign" aria-label="Introduction">
  <div class="sign-body">
    <span class="sign-number" aria-hidden="true">PD<b>01</b></span>
    <p class="sign-kana" lang="ja">ヤル・ルチキン</p>
    <h1 class="sign-roman">Yar Luchkin</h1>
    <p class="sign-sub"><span lang="ja">プロダクトデザイナー</span>&emsp;Product designer</p>
  </div>
  <div class="sign-bar" aria-hidden="true"></div>
  <div class="sign-stations">
    <p class="st-prev"><span class="arrow">◀</span><span><span class="kana" lang="ja">ベオグラード</span><span class="roman">Belgrade</span></span></p>
    <p class="st-next"><span><span class="kana" lang="ja">東京</span><span class="roman">Tokyo</span></span><span class="arrow">▶</span></p>
  </div>
</section>

<section class="intro" aria-label="About me in short">
  <div>
    <p class="lede">I design marketplaces and travel products used by millions of people, and the design systems that keep them consistent.</p>
    <p>Right now I own the home page of Playerok, a marketplace for in-game items with 4M+ users. Before that I designed for Rail Ninja and its sister products: a multi-brand design system and Travel Ninja, a hotel booking service built from scratch.</p>
    <p>My background is in advertising and intercultural communication. Most products I’ve worked on are used by people from many countries, often in a language that isn’t their own.</p>
    <div class="actions">
      <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
      <a class="btn" href="{LINKEDIN}">LinkedIn</a>
    </div>
  </div>
  <dl class="facts">
    <div><dt>Based in</dt><dd>Belgrade, Serbia</dd></div>
    <div><dt>Japan</dt><dd>Design system workshops for Galary Design, Tokyo<br>Studying Japanese since 2018, starting with a summer course in Tokyo</dd></div>
    <div><dt>Focus</dt><dd>Design systems, booking and checkout flows, marketplaces</dd></div>
    <div><dt>Languages</dt><dd>English, professional<br>Japanese, intermediate (N4–N3) and improving<br>Russian, native</dd></div>
    <div><dt>Education</dt><dd>BA in Advertising and PR, HSE University, Moscow</dd></div>
  </dl>
</section>

<section class="section" id="work">
  <h2>Selected work</h2>
  <p class="section-note">Products I designed in production teams, from a marketplace to train and hotel booking.</p>
  <div class="work">
{chr(10).join(cards)}
  </div>
</section>

<section class="section" id="concepts">
  <h2>Concepts</h2>
  <p class="section-note">Self-initiated work, made quickly to try domains I hadn’t worked in. None of these are client projects.</p>
  <div class="concepts">
{concepts}
  </div>
</section>

<section class="section" id="talks">
  <h2>Talks and workshops</h2>
  <p class="section-note">I speak at <a href="https://www.meetup.com/galary-ux-ui-design-community/">Galary Design</a>, a Tokyo community of about 660 UX/UI designers.</p>
  <ul class="talks">
{talks}
  </ul>
</section>

<section class="section" id="writing">
  <h2>Writing</h2>
  <ul class="talks">
  <li><time datetime="2021">2021</time><div><h3><a href="https://www.researchgate.net/publication/358564840_Ways_of_the_Artists%27_Promotion_in_the_Russian_Contemporary_Digital_Art_Market">Ways of the artists’ promotion in the Russian contemporary digital art market</a></h3><p>My bachelor’s research at HSE University, written in English: how digital artists build an audience and sell their work online.</p></div><span class="count">Research paper</span></li>
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
    <p>I’ve been to Japan twice, the first time in 2018 for a month of Japanese classes in Tokyo, and I’m still learning. I work in English and Figma, and I’m comfortable with ProtoPie, Framer and Adobe tools.</p>
  </div>
</section>

</div>
""" + foot()


def case_page(i, c, pool=None):
    pool = pool or CASES
    nxt = pool[(i + 1) % len(pool)] if len(pool) > 1 else CASES[0]
    meta = "\n".join(f"    <div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["meta"])
    body = "\n".join(f'  <h2>{h}</h2>\n  <div class="block">{html}</div>' for h, html in c["sections"])
    gallery = ""
    if c["gallery"]:
        figs = []
        for f, cap, wide in c["gallery"]:
            capt = f"<figcaption>{escape(cap)}</figcaption>" if cap else ""
            alt = cap or f"{c['title']}, slide"
            figs.append(f'  <figure class="{"wide" if wide else ""}"><img src="{img(f, 2000, 2)}"{srcset(f, 2)} alt="{escape(alt)}" loading="lazy" width="1600" height="1200">{capt}</figure>')
        gallery = '<div class="gallery">\n' + "\n".join(figs) + "\n</div>"
    tag = f' <span class="tag">{c["tag"]}</span>' if c.get("tag") else ""
    return head(f"{c['title']} | Yar Luchkin", c["card"], f"/work/{c['slug']}/", 2) + f"""<div class="wrap">
<header class="case-head">
  <p class="crumb"><a href="../../#{'work' if pool is CASES else 'concepts'}">{'Work' if pool is CASES else 'Concepts'}</a>{tag}</p>
  <h1>{escape(c['title'])}</h1>
  <p class="lede">{escape(c['lede'])}</p>
  <dl class="case-meta">
{meta}
  </dl>
</header>
<figure class="case-cover"><img src="{img(c['cover'], 2000, 2)}"{srcset(c['cover'], 2)} alt="{escape(c['cover_alt'])}" width="1600" height="1200" fetchpriority="high"></figure>
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
    for i, c in enumerate(CONCEPT_PAGES):
        d = ROOT / "work" / c["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(case_page(i, c, CONCEPT_PAGES), encoding="utf-8")
    (ROOT / "404.html").write_text(
        head("Page not found | Yar Luchkin", "Page not found", "/404.html", 0, pre="/")
        + '<div class="wrap"><section class="section"><h2>This page doesn’t exist</h2><p class="section-note">The link may be from the old site. <a href="/">Go to the home page</a>.</p></section></div>' + foot(),
        encoding="utf-8")
    print("built")


if __name__ == "__main__":
    main()
