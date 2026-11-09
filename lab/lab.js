// Lab edition 3: reveals, screen reels and the language demo. Everything degrades to a static page.
(() => {
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const canHover = matchMedia("(hover: hover)").matches;

  // Blocks blur in as they enter the view; cards in one row follow each other.
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
  }, { rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll(".grid").forEach((g) => [...g.children].forEach((c, i) => c.style.setProperty("--d", i * 0.08 + "s")));
  document.querySelectorAll(".reveal").forEach((el) => (still ? el.classList.add("in") : io.observe(el)));

  // Reels: big ones play while on screen, small ones while hovered (on touch screens, while on screen).
  const SLIDE = 2400;
  document.querySelectorAll(".reel").forEach((reel) => {
    const frames = [...reel.querySelectorAll(".frames img")];
    const bars = [...reel.querySelectorAll(".bars i")];
    const glow = reel.querySelector(".glow");
    let i = 0, timer = null;
    reel.style.setProperty("--slide", SLIDE + "ms");
    const paintGlow = () => { const src = frames[i].currentSrc || frames[i].src; glow.style.setProperty("--glow", `url("${src}")`); };
    const show = (n) => {
      frames[i].classList.remove("on");
      i = (n + frames.length) % frames.length;
      frames[i].classList.add("on");
      bars.forEach((b, k) => { b.classList.toggle("done", k < i); b.classList.remove("now"); });
      if (bars[i]) { void bars[i].offsetWidth; bars[i].classList.add("now"); }
      paintGlow();
    };
    const play = () => {
      if (timer || frames.length < 2 || still) return;
      reel.classList.add("playing");
      show(i);
      timer = setInterval(() => show(i + 1), SLIDE);
    };
    const stop = (reset) => {
      clearInterval(timer); timer = null;
      reel.classList.remove("playing");
      if (reset) show(0);
    };
    frames[0].complete ? paintGlow() : frames[0].addEventListener("load", paintGlow, { once: true });
    if (frames.length < 2) return;
    // Warm the next screens so the crossfade never shows an empty frame.
    const warm = () => frames.forEach((f) => (f.loading = "eager"));
    if (reel.dataset.mode === "hover" && canHover) {
      const card = reel.closest(".card") || reel;
      card.addEventListener("pointerenter", () => { warm(); play(); });
      card.addEventListener("pointerleave", () => stop(true));
    } else {
      new IntersectionObserver(([e]) => {
        if (e.intersectionRatio >= 0.5) { warm(); play(); } else stop(false);
      }, { threshold: [0, 0.5] }).observe(reel);
    }
    document.addEventListener("visibilitychange", () => { if (document.hidden) stop(false); });
  });

  // Demo: one button, four languages.
  const demo = document.querySelector(".demo");
  if (!demo) return;
  const data = JSON.parse(document.getElementById("demo-data").textContent);
  const stage = demo.querySelector(".stage");
  const go = demo.querySelector(".go");
  const count = demo.querySelector(".count");
  const cut = demo.querySelector(".cut");
  let lang = "en", fit = "grow", fixedW = 0;

  const moveThumb = (seg) => {
    const on = seg.querySelector('[aria-checked="true"]');
    const t = seg.querySelector(".thumb");
    t.style.width = on.offsetWidth + "px";
    t.style.translate = on.offsetLeft + "px 0";
  };
  const natural = () => { // width the button needs for its current label
    // scrollWidth rounds down; the extra pixels stop a fractional overflow from showing an ellipsis.
    const prev = go.style.width; go.style.width = "max-content";
    const w = Math.ceil(go.getBoundingClientRect().width) + 2; go.style.width = prev; return w;
  };
  const size = () => {
    const need = natural();
    go.style.width = (fit === "grow" ? need : fixedW) + "px";
    // Compare against the target width: mid-transition layout still shows the old one.
    const isCut = fit === "fixed" && need > fixedW + 1;
    go.classList.toggle("is-cut", isCut);
    cut.classList.toggle("show", isCut);
  };
  const setLang = (next) => {
    if (next === lang) return;
    lang = next;
    const apply = () => {
      stage.lang = lang;
      stage.querySelectorAll("[data-k]").forEach((el) => (el.textContent = data[lang][el.dataset.k]));
      count.textContent = [...data[lang].btn].length;
      // Fonts load per script (Cyrillic, Japanese) on first use: size the button once the glyphs are in.
      const fonts = document.fonts ? document.fonts.load("500 16px Onest", data[lang].btn).catch(() => {}) : Promise.resolve();
      fonts.then(() => requestAnimationFrame(() => { size(); stage.classList.remove("swap"); }));
    };
    if (still) return apply();
    stage.classList.add("swap");
    setTimeout(apply, 180);
  };

  demo.querySelectorAll(".seg").forEach((seg) => {
    seg.addEventListener("click", (ev) => {
      const b = ev.target.closest("button"); if (!b) return;
      seg.querySelectorAll("button").forEach((x) => x.setAttribute("aria-checked", String(x === b)));
      moveThumb(seg);
      if (b.dataset.lang) setLang(b.dataset.lang);
      if (b.dataset.fit) { fit = b.dataset.fit; size(); }
    });
    seg.addEventListener("keydown", (ev) => { // arrow keys move between options, like native radios
      if (!["ArrowLeft", "ArrowRight"].includes(ev.key)) return;
      const opts = [...seg.querySelectorAll("button")];
      const k = opts.findIndex((x) => x.getAttribute("aria-checked") === "true");
      const n = opts[(k + (ev.key === "ArrowRight" ? 1 : -1) + opts.length) % opts.length];
      n.focus(); n.click(); ev.preventDefault();
    });
  });

  const init = () => {
    fixedW = natural(); // the fixed button is sized for the English label
    demo.querySelectorAll(".seg").forEach(moveThumb);
    size();
  };
  if (document.fonts) {
    const all = Object.values(data).map((d) => d.btn + d.a + d.b + d.d).join("");
    Promise.all([document.fonts.load("500 16px Onest", all), document.fonts.load("400 16px Onest", all), document.fonts.ready]).catch(() => {}).then(init);
    document.fonts.addEventListener("loadingdone", size);
  } else init();
  addEventListener("resize", () => demo.querySelectorAll(".seg").forEach(moveThumb));
})();
