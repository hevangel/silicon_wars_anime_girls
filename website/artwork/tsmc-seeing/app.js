"use strict";
const DONE_KEY = "tsmc-seeing-course-done-v1";
let DATA = null;
let done = new Set(JSON.parse(localStorage.getItem(DONE_KEY) || "[]"));
let lb = { images: [], idx: 0, title: "" };

const $ = (s, r = document) => r.querySelector(s);

/* ---- overlays: drawn by the page over the pictures, never baked in ----
   Coordinates are in a 400x300 space mapped over each image; placements are
   approximate, following the control image (figure left of center, head near
   (128,54), cup near (163,63), table across the right half). */
const A = "#8e2434", G = "#b98a2f", B = "#2456a6";
const line = (x1, y1, x2, y2, c, dash, w) =>
  `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${c || A}" stroke-width="${w || 2}" ${dash ? 'stroke-dasharray="6 5"' : ""}/>`;
const txt = (x, y, s, c) =>
  `<text x="${x}" y="${y}" font-size="13" font-weight="700" fill="${c || A}" font-family="Georgia,serif">${s}</text>`;
const circ = (x, y, r, c) =>
  `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="${c || A}" stroke-width="2.5"/>`;
const dot = (x, y, c) => `<circle cx="${x}" cy="${y}" r="4.5" fill="${c || A}"/>`;

const OVERLAYS = {
  thirds: () => line(133, 0, 133, 300, A, 1) + line(267, 0, 267, 300, A, 1) +
    line(0, 100, 400, 100, A, 1) + line(0, 200, 400, 200, A, 1),
  gaze: () => `<path d="M146 52 L292 46" stroke="${A}" stroke-width="2.5" stroke-dasharray="2 7" stroke-linecap="round" fill="none"/><path d="M292 46 l-12 -4 M292 46 l-11 6" stroke="${A}" stroke-width="2.5" fill="none"/>
    <path d="M238 148 L352 142" stroke="${G}" stroke-width="2.5" stroke-dasharray="2 7" stroke-linecap="round" fill="none"/><path d="M352 142 l-12 -4 M352 142 l-11 6" stroke="${G}" stroke-width="2.5" fill="none"/>`,
  bms: () => `<rect x="42" y="12" width="196" height="272" rx="26" fill="none" stroke="${A}" stroke-width="3"/>
    <rect x="212" y="118" width="178" height="118" rx="10" fill="none" stroke="${G}" stroke-width="3"/>` +
    circ(163, 63, 13, B) + circ(283, 130, 11, B) + circ(322, 133, 9, B),
  graystrip: () => Array.from({ length: 9 }, (_, i) => {
    const v = Math.round(i * 255 / 8).toString(16).padStart(2, "0");
    return `<rect x="${(i * 400 / 9).toFixed(1)}" y="272" width="${(400 / 9 + 1).toFixed(1)}" height="28" fill="#${v}${v}${v}" stroke="#888" stroke-width="1"/>`;
  }).join(""),
  families: () => line(150, 14, 150, 288, A, 1) + txt(28, 30, "LIGHT", G) + txt(316, 30, "SHADOW", A),
  highlights: () => circ(163, 62, 12) + circ(122, 34, 14, G) + circ(283, 128, 11, B),
  terminator: () => `<path d="M208 18 C188 88 218 178 196 286" fill="none" stroke="${A}" stroke-width="3"/>`,
  coreshadow: () => `<path d="M214 22 C196 92 224 182 204 282" fill="none" stroke="${A}" stroke-width="2.5"/>
    <path d="M230 24 C212 94 240 184 220 280" fill="none" stroke="${A}" stroke-width="2.5"/>`,
  bar603010: () => `<rect x="0" y="268" width="240" height="32" fill="#e8ddc8"/><rect x="240" y="268" width="120" height="32" fill="#c9a86a"/><rect x="360" y="268" width="40" height="32" fill="${A}"/>` +
    txt(104, 290, "60", "#211c15") + txt(288, 290, "30", "#211c15") + txt(368, 290, "10", "#ffffff"),
  vp1: () => line(0, 122, 400, 122, G, 0, 2) + dot(200, 122) +
    line(200, 122, 36, 300, A, 1) + line(200, 122, 364, 300, A, 1) +
    line(200, 122, 22, 168, A, 1) + line(200, 122, 378, 168, A, 1) + txt(208, 114, "VP"),
  vp2: () => line(0, 122, 400, 122, G, 0, 2) + dot(6, 122) + dot(394, 122) +
    line(6, 122, 210, 300, A, 1) + line(6, 122, 250, 40, A, 1) +
    line(394, 122, 190, 300, A, 1) + line(394, 122, 150, 40, A, 1) +
    txt(12, 112, "VP") + txt(362, 112, "VP"),
  vp3: () => dot(22, 14) + dot(378, 14) + dot(200, 292) +
    line(22, 14, 200, 168, A, 1) + line(378, 14, 200, 168, A, 1) +
    line(200, 292, 120, 130, A, 1) + line(200, 292, 290, 130, A, 1) +
    txt(28, 32, "VP") + txt(348, 32, "VP") + txt(208, 288, "VP"),
  heads: () => Array.from({ length: 7 }, (_, i) => {
    const y = ((i + 1) * 300 / 7.5).toFixed(0);
    return line(0, y, 400, y, i % 2 ? G : A, 1, 1.5) + txt(378, y - 4, String(i + 1), i % 2 ? G : A);
  }).join("") + txt(330, 20, "7½ heads", G),
  landmarks: () => [[38, "eyes"], [62, "shoulders"], [120, "elbows"], [128, "waist"], [152, "hips"], [160, "wrists"], [218, "knees"]]
    .map(([y, s]) => line(0, y, 400, y, A, 1, 1.5) + txt(6, y - 4, s, G)).join(""),
  action: () => `<path d="M196 12 C118 84 268 158 168 288" fill="none" stroke="${A}" stroke-width="3.5"/>`,
  plumb: () => line(150, 26, 150, 290, A, 0, 2.5) + dot(150, 26) +
    line(118, 284, 188, 284, G, 0, 4) + txt(196, 288, "base of support", G),
  tilt: () => line(64, 74, 238, 58, A, 0, 3) + line(70, 152, 232, 172, G, 0, 3) +
    txt(246, 62, "shoulders") + txt(240, 176, "hips", G),
  triangle: () => `<polygon points="200,58 88,272 322,272" fill="none" stroke="${A}" stroke-width="3"/>`,
  eyepath: () => {
    const pts = [[88, 62], [140, 54], [186, 112], [286, 136], [152, 74]];
    const path = pts.map(p => p.join(" ")).join(" L ");
    return `<path d="M${path}" fill="none" stroke="${A}" stroke-width="2.5" stroke-dasharray="7 5"/>` +
      pts.map((p, i) => `<circle cx="${p[0]}" cy="${p[1]}" r="11" fill="#fff" stroke="${A}" stroke-width="2"/><text x="${p[0]}" y="${p[1] + 5}" font-size="13" font-weight="700" fill="${A}" text-anchor="middle" font-family="Georgia,serif">${i + 1}</text>`).join("");
  },
};

function overlaySVG(type) {
  const fn = OVERLAYS[type];
  return fn ? `<svg class="overlay" viewBox="0 0 400 300" preserveAspectRatio="none" aria-hidden="true">${fn()}</svg>` : "";
}

function saveDone() {
  localStorage.setItem(DONE_KEY, JSON.stringify([...done]));
  renderProgress();
}

function renderProgress() {
  const total = DATA.lessons.length;
  $("#progressBar").style.width = (100 * done.size / total) + "%";
  $("#progressText").textContent = `${done.size} / ${total} lessons`;
  document.querySelectorAll("#lessonNav a").forEach(a => {
    a.classList.toggle("done", done.has(a.dataset.lesson));
  });
}

function renderNav() {
  const nav = $("#lessonNav");
  DATA.lessons.forEach((lesson, i) => {
    const a = document.createElement("a");
    a.href = "#lesson-" + lesson.id;
    a.dataset.lesson = lesson.id;
    a.textContent = `${i + 1}. ${lesson.title.split(":")[0]}`;
    nav.appendChild(a);
  });
}

function tile(img, label, isControl, overlayType) {
  const fig = document.createElement("figure");
  const wrap = document.createElement("div");
  wrap.className = "tile-wrap" + (isControl ? " is-control" : "");
  const im = document.createElement("img");
  im.loading = "lazy";
  im.src = img.thumb;
  im.alt = label;
  im.dataset.full = img.src;
  wrap.appendChild(im);
  if (overlayType && !isControl) wrap.insertAdjacentHTML("beforeend", overlaySVG(overlayType));
  const cap = document.createElement("figcaption");
  cap.innerHTML = isControl ? `<span class="ctl">Control</span> — unchanged` : label;
  fig.appendChild(wrap);
  fig.appendChild(cap);
  return fig;
}

function cardEl(lesson, card) {
  const el = document.createElement("article");
  el.className = "see-card";
  el.dataset.search = (card.name + " " + card.subtitle + " " + card.explanation + " " + lesson.title).toLowerCase();

  const head = document.createElement("div");
  head.className = "card-head";
  head.innerHTML = `<h3>${card.name}</h3><span class="card-sub">${card.subtitle}</span>`;
  el.appendChild(head);

  const blurb = document.createElement("p");
  blurb.className = "card-blurb";
  blurb.textContent = card.explanation;
  el.appendChild(blurb);

  const body = document.createElement("div");
  body.className = "card-body";
  const compare = document.createElement("div");
  compare.className = "compare";
  const all = [{ img: DATA.control, label: "The control image", ctl: true }]
    .concat(card.images.map(img => ({ img, label: `${card.name} — ${img.label}`, ctl: false })));
  all.forEach((t, i) => {
    const fig = tile(t.img, t.label, t.ctl, card.overlay);
    fig.querySelector("img").addEventListener("click", () => openLightbox(card, all, i));
    compare.appendChild(fig);
  });
  body.appendChild(compare);

  const aside = document.createElement("aside");
  aside.className = "look-box";
  aside.innerHTML = `<h4>What to look for</h4><ul>${card.look.map(t => `<li>${t}</li>`).join("")}</ul>`;
  if (card.overlay) {
    const btn = document.createElement("button");
    btn.className = "overlay-btn";
    btn.textContent = "Show overlay";
    btn.addEventListener("click", () => {
      const on = el.classList.toggle("show-overlay");
      btn.textContent = on ? "Hide overlay" : "Show overlay";
    });
    aside.appendChild(btn);
  }
  body.appendChild(aside);
  el.appendChild(body);
  return el;
}

function renderLessons() {
  const wrap = $("#lessons");
  DATA.lessons.forEach((lesson, li) => {
    const sec = document.createElement("section");
    sec.className = "lesson";
    sec.id = "lesson-" + lesson.id;
    const count = lesson.cards.length
      ? `${lesson.cards.length} cards · ${lesson.cards.reduce((s, c) => s + c.images.length, 0)} pictures`
      : "no pictures — practice";
    const head = document.createElement("div");
    head.className = "lesson-head";
    head.innerHTML = `
      <div class="lesson-kicker">Lesson ${li + 1} of ${DATA.lessons.length} · ${count} · ${lesson.strand_title}</div>
      <h2>${lesson.title}</h2>
      <p class="big-idea">${lesson.thesis}</p>
      <p class="lesson-intro">${lesson.intro}</p>
      ${lesson.bridge_note ? `<p class="bridge-note"><strong>The bridge to Part III.</strong> ${lesson.bridge_note}</p>` : ""}
      <div class="exercise"><strong>Try this</strong>${lesson.exercise}</div>
      <label class="lesson-done"><input type="checkbox" data-done="${lesson.id}" ${done.has(lesson.id) ? "checked" : ""}> Mark this lesson complete</label>`;
    sec.appendChild(head);
    lesson.cards.forEach(card => sec.appendChild(cardEl(lesson, card)));
    if (lesson.prose) {
      const prose = document.createElement("div");
      prose.className = "prose";
      prose.innerHTML = lesson.prose;
      sec.appendChild(prose);
    }
    wrap.appendChild(sec);
  });
  wrap.addEventListener("change", e => {
    const id = e.target.dataset && e.target.dataset.done;
    if (!id) return;
    e.target.checked ? done.add(id) : done.delete(id);
    saveDone();
  });
}

/* lightbox */
function openLightbox(card, all, idx) {
  lb = { images: all, idx, title: card.name };
  $("#lightbox").hidden = false;
  document.body.style.overflow = "hidden";
  showLb();
}
function showLb() {
  const t = lb.images[lb.idx];
  const el = $("#lbImg");
  el.src = t.img.src;
  el.alt = t.label;
  $("#lbCaption").textContent = lb.images.length > 1
    ? `${t.label} (${lb.idx + 1} of ${lb.images.length})`
    : t.label;
  $("#lbPrev").disabled = lb.idx <= 0;
  $("#lbNext").disabled = lb.idx >= lb.images.length - 1;
}
function closeLightbox() {
  $("#lightbox").hidden = true;
  document.body.style.overflow = "";
}
$("#lbClose").addEventListener("click", closeLightbox);
$("#lbPrev").addEventListener("click", () => { if (lb.idx > 0) { lb.idx--; showLb(); } });
$("#lbNext").addEventListener("click", () => { if (lb.idx < lb.images.length - 1) { lb.idx++; showLb(); } });
$("#lightbox").addEventListener("click", e => { if (e.target.id === "lightbox") closeLightbox(); });
document.addEventListener("keydown", e => {
  if ($("#lightbox").hidden) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowLeft") $("#lbPrev").click();
  if (e.key === "ArrowRight") $("#lbNext").click();
});

/* search */
$("#search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  let anyVisible = false;
  document.querySelectorAll(".lesson").forEach(sec => {
    let lessonVisible = false;
    sec.querySelectorAll(".see-card").forEach(card => {
      const hit = !q || card.dataset.search.includes(q);
      card.style.display = hit ? "" : "none";
      if (hit) { lessonVisible = true; anyVisible = true; }
    });
    if (!q) lessonVisible = true;
    sec.style.display = lessonVisible ? "" : "none";
    if (lessonVisible && q) anyVisible = true;
  });
  $("#noResults").hidden = anyVisible;
});

function renderStrands() {
  const el = $("#strands");
  if (!el || !DATA.strands) return;
  const byN = {};
  DATA.lessons.forEach(l => { byN[l.n] = l; });
  el.innerHTML = DATA.strands.map(s => {
    const links = s.lessons.map(n => `<a href="#lesson-${byN[n].id}">L${n} ${byN[n].title.split(":")[0]}</a>`).join(" · ");
    return `<div class="hero-card"><h3>${s.title}</h3><p>${links}</p></div>`;
  }).join("");
}

fetch("seeing.json")
  .then(r => r.json())
  .then(data => {
    DATA = data;
    renderNav();
    renderLessons();
    renderStrands();
    renderProgress();
  })
  .catch(err => {
    $("#lessons").innerHTML = "<p>Could not load the course data (seeing.json). If you opened this file directly from disk, serve the folder over HTTP instead — browsers block local JSON fetches.</p>";
    console.error(err);
  });
