// Lab edition 4: selection box, draggable frames, screen reels, Yar's cursor and the language demo.
// Without JavaScript, or with reduced motion, the page stays a plain readable portfolio.
(() => {
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const $ = (q, el = document) => el.querySelector(q);
  const $$ = (q, el = document) => [...el.querySelectorAll(q)];
  const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const pageRect = (el) => { const r = el.getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }; };
  const pointer = { x: -999, y: -999, px: -999, py: -999 }; // viewport and page coordinates

  /* ---------- Frames drop onto the canvas as they come into view ---------- */
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
  }, { rootMargin: "0px 0px -8% 0px" });
  $$(".home .frames").forEach((g) => $$(":scope > .frame", g).forEach((f, i) => {
    f.style.setProperty("--d", (i % 3) * 90 + "ms");
    still ? f.classList.add("in") : io.observe(f);
  }));

  /* ---------- Dot grid drifts a little against the cursor ---------- */
  let gx = 0, gy = 0;
  const drift = () => {
    const tx = -(pointer.x / innerWidth - 0.5) * 14, ty = -(pointer.y / innerHeight - 0.5) * 14;
    gx += (tx - gx) * 0.08; gy += (ty - gy) * 0.08;
    document.body.style.setProperty("--gx", gx.toFixed(2) + "px");
    document.body.style.setProperty("--gy", gy.toFixed(2) + "px");
    requestAnimationFrame(drift);
  };
  addEventListener("pointermove", (e) => { pointer.x = e.clientX; pointer.y = e.clientY; pointer.px = e.pageX; pointer.py = e.pageY; }, { passive: true });
  if (fine && !still) requestAnimationFrame(drift);

  /* ---------- Selection box glides to whatever layer is under the cursor ---------- */
  const sel = $(".sel"), selTag = $(".sel-tag"), tip = $(".tip");
  let target = null, dragging = null;
  const place = (el, jump) => {
    const r = pageRect(el);
    sel.classList.toggle("jump", !!jump);
    sel.style.translate = `${r.x}px ${r.y}px`;
    sel.style.width = r.w + "px"; sel.style.height = r.h + "px";
    selTag.textContent = `${el.dataset.layer}  ${Math.round(r.w)} × ${Math.round(r.h)}`;
  };
  if (fine) {
    document.addEventListener("pointerover", (e) => {
      if (dragging) return;
      const el = e.target.closest("[data-layer]");
      if (el === target) return;
      const wasOn = !!target;
      target = el;
      if (!el) { sel.classList.remove("on"); tip.classList.remove("on"); return; }
      place(el, !wasOn);
      sel.classList.add("on");
      const canOpen = el.matches("a[data-drag]");
      tip.textContent = canOpen ? "Open, or drag to move" : "";
      tip.classList.toggle("on", canOpen);
    });
    addEventListener("scroll", () => target && place(target, true), { passive: true });
    addEventListener("resize", () => target && place(target, true));
    // The cursor tag trails the pointer with a little lag.
    let tx = 0, ty = 0;
    const trail = () => {
      tx += (pointer.x + 14 - tx) * 0.25; ty += (pointer.y + 18 - ty) * 0.25;
      tip.style.translate = `${tx}px ${ty}px`;
      requestAnimationFrame(trail);
    };
    requestAnimationFrame(trail);
  }

  /* ---------- Frames can be dragged around the canvas ---------- */
  const tidy = $(".tidy");
  const settle = (f) => { f.style.transition = "translate 600ms cubic-bezier(0.22, 1, 0.36, 1), rotate 600ms cubic-bezier(0.22, 1, 0.36, 1)"; };
  if (fine && !still) {
    $$("[data-drag]").forEach((handle) => {
      const f = handle.closest(".frame");
      let sx, sy, ox = 0, oy = 0, lastX, moved = false, rot = 0;
      handle.addEventListener("pointerdown", (e) => {
        if (e.button !== 0) return;
        sx = e.clientX; sy = e.clientY; lastX = e.clientX; moved = false;
        const t = (f.style.translate || "0px 0px").split(" ");
        ox = parseFloat(t[0]) || 0; oy = parseFloat(t[1]) || 0;
        handle.setPointerCapture(e.pointerId);
        const move = (ev) => {
          const dx = ev.clientX - sx, dy = ev.clientY - sy;
          if (!moved && Math.hypot(dx, dy) < 5) return;
          if (!moved) { moved = true; dragging = f; f.classList.add("lifted"); f.style.transition = "none"; tip.textContent = "Moving"; }
          rot += (Math.max(-7, Math.min(7, (ev.clientX - lastX) * 0.5)) - rot) * 0.2; lastX = ev.clientX;
          f.style.translate = `${ox + dx}px ${oy + dy}px`;
          f.style.rotate = rot.toFixed(2) + "deg";
          if (target) place(target, true);
        };
        const up = () => {
          handle.removeEventListener("pointermove", move);
          handle.removeEventListener("pointerup", up);
          handle.removeEventListener("pointercancel", up);
          if (!moved) return;
          settle(f); f.style.rotate = "0deg"; rot = 0;
          f.classList.remove("lifted"); dragging = null; tidy.hidden = false;
          tip.textContent = "Open, or drag to move";
          setTimeout(() => target && place(target, true), 620);
        };
        handle.addEventListener("pointermove", move);
        handle.addEventListener("pointerup", up);
        handle.addEventListener("pointercancel", up);
      });
      // A drag is not a click.
      handle.addEventListener("click", (e) => { if (moved) { e.preventDefault(); moved = false; } });
    });
    tidy?.addEventListener("click", () => {
      $$(".frame").forEach((f) => { settle(f); f.style.translate = "0px 0px"; f.style.rotate = "0deg"; });
      tidy.hidden = true;
      setTimeout(() => target && place(target, true), 620);
    });
  }

  /* ---------- Each frame flips through its case screens ---------- */
  $$(".frame-body .screens").forEach((box) => {
    const imgs = $$("img", box);
    if (imgs.length < 2 || still) return;
    let i = 0, timer = null;
    const step = () => { imgs[i].classList.remove("on"); i = (i + 1) % imgs.length; imgs[i].classList.add("on"); };
    const play = (ms) => { if (timer) return; imgs.forEach((im) => (im.loading = "eager")); step(); timer = setInterval(step, ms); };
    const stop = () => { clearInterval(timer); timer = null; };
    const host = box.closest(".frame");
    if (fine) {
      host.addEventListener("pointerenter", () => play(1400));
      host.addEventListener("pointerleave", stop);
    } else {
      new IntersectionObserver(([e]) => (e.intersectionRatio > 0.6 ? play(2200) : stop()), { threshold: [0, 0.6] }).observe(box);
    }
  });

  /* ---------- Yar's cursor walks the visitor through the work ---------- */
  const yar = $(".yar"), say = $(".yar-say");
  const stops = $$("[data-tour]");
  if (yar && stops.length && !still && fine) { // a cursor only makes sense where there is one
    let pos = { x: 0, y: 0 }, at = -1, busy = false, lastHello = 0;
    const set = (p) => { pos = p; yar.style.translate = `${p.x}px ${p.y}px`; };
    const spot = (el) => { // where on a stop the cursor rests
      const anchor = el.querySelector(".frame-body, h1, .stage, .section-tag") || el;
      const r = pageRect(anchor);
      if (anchor.matches("h1")) { // beside the last line of the intro, kept on screen
        const x = Math.min(r.x + r.w + 20, scrollX + innerWidth - 240);
        return { x, y: r.y + r.h - (x < r.x + r.w ? -14 : 34) };
      }
      if (anchor.matches(".section-tag")) return { x: r.x + r.w + 18, y: r.y + 4 };
      return { x: r.x + r.w * 0.62, y: r.y + r.h * 0.38 };
    };
    const visible = (el) => { const r = el.getBoundingClientRect(); return r.bottom > innerHeight * 0.15 && r.top < innerHeight * 0.8; };
    const fly = (to, text, done) => {
      busy = true; yar.classList.remove("talk");
      const from = { ...pos };
      const dist = Math.hypot(to.x - from.x, to.y - from.y);
      const dur = Math.min(1300, 500 + dist * 0.6);
      // A curved path, like a hand moving a mouse, not a straight tween.
      const c = { x: (from.x + to.x) / 2 + (to.y - from.y) * 0.18, y: (from.y + to.y) / 2 - (to.x - from.x) * 0.18 };
      const t0 = performance.now();
      const frame = (now) => {
        const t = ease(Math.min(1, (now - t0) / dur)), u = 1 - t;
        set({ x: u * u * from.x + 2 * u * t * c.x + t * t * to.x, y: u * u * from.y + 2 * u * t * c.y + t * t * to.y });
        if (t < 1) return requestAnimationFrame(frame);
        say.textContent = text;
        yar.classList.toggle("flip", pos.x + 300 > scrollX + innerWidth); // keep the bubble on screen
        yar.classList.add("talk"); busy = false; done && done();
      };
      requestAnimationFrame(frame);
    };
    const next = () => {
      if (busy || document.hidden) return;
      const n = stops.length;
      for (let k = 1; k <= n; k++) {
        const j = (at + k) % n;
        if (visible(stops[j])) {
          if (j === at && visible(stops[at])) return; // only one stop on screen: stay put
          at = j; fly(spot(stops[j]), stops[j].dataset.tour); return;
        }
      }
      yar.classList.remove("talk"); // nothing of note on screen: stay quiet
    };
    setTimeout(() => {
      const h = spot(stops[0]);
      set({ x: h.x + 160, y: h.y + 120 });
      yar.classList.add("on");
      at = 0; fly(h, stops[0].dataset.tour);
      setInterval(next, 4200);
    }, 1100);
    // Say hello when the visitor's cursor comes close, then move on.
    addEventListener("pointermove", () => {
      if (busy || Date.now() - lastHello < 6000) return;
      if (Math.hypot(pointer.px - pos.x, pointer.py - pos.y) < 56) {
        lastHello = Date.now();
        fly({ x: pos.x + 40, y: pos.y - 36 }, "Oh, hi");
      }
    }, { passive: true });
    let st;
    addEventListener("scroll", () => { clearTimeout(st); st = setTimeout(next, 350); }, { passive: true });
  }

  /* ---------- Demo: one button, four languages ---------- */
  const demo = $(".demo");
  if (!demo) return;
  const data = JSON.parse($("#demo-data").textContent);
  const stage = $(".stage", demo), go = $(".go", demo), count = $(".count", demo), cut = $(".cut", demo);
  let lang = "en", fit = "hug", fixedW = 0;
  const moveThumb = (seg) => {
    const on = $('[aria-checked="true"]', seg), t = $(".thumb", seg);
    t.style.width = on.offsetWidth + "px"; t.style.translate = on.offsetLeft + "px 0";
  };
  const natural = () => { // width the button needs for its label; ceil plus 2px so rounding never shows an ellipsis
    const prev = go.style.width; go.style.width = "max-content";
    const w = Math.ceil(go.getBoundingClientRect().width) + 2; go.style.width = prev; return w;
  };
  const size = () => {
    const need = natural();
    go.style.width = (fit === "hug" ? need : fixedW) + "px";
    const isCut = fit === "fixed" && need > fixedW + 1; // compare with the target, not the mid-transition width
    go.classList.toggle("is-cut", isCut); cut.classList.toggle("show", isCut);
  };
  const setLang = (nextLang) => {
    if (nextLang === lang) return;
    lang = nextLang;
    const apply = () => {
      stage.lang = lang;
      $$("[data-k]", stage).forEach((el) => (el.textContent = data[lang][el.dataset.k]));
      count.textContent = [...data[lang].btn].length;
      // Fonts load per script on first use, so size the button once the glyphs are in.
      const fam = lang === "ja" ? '"Noto Sans JP"' : '"Golos Text"';
      (document.fonts ? document.fonts.load(`500 16px ${fam}`, data[lang].btn).catch(() => {}) : Promise.resolve())
        .then(() => requestAnimationFrame(() => { size(); stage.classList.remove("swap"); }));
    };
    if (still) return apply();
    stage.classList.add("swap"); setTimeout(apply, 170);
  };
  $$(".seg", demo).forEach((seg) => {
    seg.addEventListener("click", (ev) => {
      const b = ev.target.closest("button"); if (!b) return;
      $$("button", seg).forEach((x) => x.setAttribute("aria-checked", String(x === b)));
      moveThumb(seg);
      if (b.dataset.lang) setLang(b.dataset.lang);
      if (b.dataset.fit) { fit = b.dataset.fit; size(); }
    });
    seg.addEventListener("keydown", (ev) => { // arrow keys move between options, like native radios
      if (!["ArrowLeft", "ArrowRight"].includes(ev.key)) return;
      const opts = $$("button", seg), k = opts.findIndex((x) => x.getAttribute("aria-checked") === "true");
      const n = opts[(k + (ev.key === "ArrowRight" ? 1 : -1) + opts.length) % opts.length];
      n.focus(); n.click(); ev.preventDefault();
    });
  });
  const init = () => { fixedW = natural(); $$(".seg", demo).forEach(moveThumb); size(); };
  if (document.fonts) {
    const all = Object.values(data).map((d) => d.btn + d.a + d.b + d.d).join("");
    Promise.all([document.fonts.load('500 16px "Golos Text"', all), document.fonts.ready]).catch(() => {}).then(init);
    document.fonts.addEventListener("loadingdone", size);
  } else init();
  addEventListener("resize", () => $$(".seg", demo).forEach(moveThumb));
})();
