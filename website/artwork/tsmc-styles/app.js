"use strict";
const DONE_KEY = "tsmc-style-course-done-v1";
let DATA = null;
let done = new Set(JSON.parse(localStorage.getItem(DONE_KEY) || "[]"));
let lb = { images: [], idx: 0, title: "" };

const $ = (s, r = document) => r.querySelector(s);

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

function renderLessons() {
  const wrap = $("#lessons");
  DATA.lessons.forEach((lesson, li) => {
    const sec = document.createElement("section");
    sec.className = "lesson";
    sec.id = "lesson-" + lesson.id;
    sec.dataset.lessonSection = lesson.id;

    const head = document.createElement("div");
    head.className = "lesson-head";
    head.innerHTML = `
      <div class="lesson-kicker">Lesson ${li + 1} of ${DATA.lessons.length} · ${lesson.styles.length} styles</div>
      <h2>${lesson.title}</h2>
      <p class="big-idea">${lesson.bigIdea}</p>
      <p class="lesson-intro">${lesson.intro}</p>
      <div class="exercise"><strong>Try this</strong>${lesson.exercise}</div>
      <label class="lesson-done"><input type="checkbox" data-done="${lesson.id}" ${done.has(lesson.id) ? "checked" : ""}> Mark this lesson complete</label>`;
    sec.appendChild(head);

    lesson.styles.forEach(style => sec.appendChild(styleCard(style)));
    wrap.appendChild(sec);
  });
  wrap.addEventListener("change", e => {
    const id = e.target.dataset && e.target.dataset.done;
    if (!id) return;
    e.target.checked ? done.add(id) : done.delete(id);
    saveDone();
  });
}

let activeClass = "";

function renderFilters() {
  const bar = $("#classFilters");
  if (!bar || !DATA.meta.categories) return;
  bar.innerHTML = ""; // re-rendered on every click to refresh the active chip
  const counts = {};
  DATA.lessons.forEach(l => l.styles.forEach(s => (s.classes || []).forEach(c => {
    counts[c] = (counts[c] || 0) + 1;
  })));
  const all = document.createElement("button");
  all.textContent = "All styles";
  all.className = "class-chip" + (activeClass ? "" : " active");
  all.addEventListener("click", () => { activeClass = ""; renderFilters(); applyFilters(); });
  bar.appendChild(all);
  DATA.meta.categories.forEach(cat => {
    const b = document.createElement("button");
    b.className = "class-chip" + (activeClass === cat ? " active" : "");
    b.textContent = `${cat} · ${counts[cat] || 0}`;
    b.addEventListener("click", () => {
      activeClass = activeClass === cat ? "" : cat;
      renderFilters();
      applyFilters();
    });
    bar.appendChild(b);
  });
}

function applyFilters() {
  const q = $("#search").value.trim().toLowerCase();
  let anyVisible = false;
  document.querySelectorAll(".lesson").forEach(sec => {
    let lessonVisible = false;
    sec.querySelectorAll(".style-card").forEach(card => {
      const hitSearch = !q || card.dataset.search.includes(q);
      const hitClass = !activeClass || (card.dataset.classes || "").split("|").includes(activeClass);
      const hit = hitSearch && hitClass;
      card.style.display = hit ? "" : "none";
      if (hit) { lessonVisible = true; anyVisible = true; }
    });
    sec.style.display = lessonVisible ? "" : "none";
  });
  $("#noResults").hidden = anyVisible;
}

function styleCard(style) {
  const card = document.createElement("article");
  card.className = "style-card";
  card.dataset.search = (style.name + " " + style.tag + " " + style.slug + " " +
    (style.classes || []).join(" ") + " " + (style.grammar || "")).toLowerCase();
  card.dataset.classes = (style.classes || []).join("|");

  const figs = style.images.map((img, i) => `
    <figure>
      <img loading="lazy" src="${img.thumb}" alt="${style.name} — ${img.label}"
           data-full="${img.src}" data-idx="${i}">
      <figcaption>${img.label}</figcaption>
    </figure>`).join("");
  const looks = style.look.map(t => `<li>${t}</li>`).join("");
  const chips = (style.classes || []).map(c => `<span class="class-tag">${c}</span>`).join("");
  const links = (style.links || []).length
    ? `<p class="style-links"><strong>Tends to use / say:</strong> ${style.links.join(" · ")}</p>` : "";

  card.innerHTML = `
    <div class="style-head"><h3>${style.name}</h3><span class="style-tag">${style.tag}</span></div>
    <div class="class-tags">${chips}</div>
    <p class="style-blurb">${style.blurb}</p>
    <div class="style-body">
      <div class="style-images">${figs}</div>
      <aside class="look-box"><h4>What to look for</h4><ul>${looks}</ul>
        <p class="style-grammar"><strong>Its grammar:</strong> ${style.grammar || ""}</p>
        ${links}
        <a class="learn-more" href="${style.wiki}" target="_blank" rel="noopener">Learn more on Wikipedia ↗</a>
      </aside>
    </div>`;
  card.querySelectorAll("img").forEach(img => {
    img.addEventListener("click", () => openLightbox(style, Number(img.dataset.idx)));
  });
  return card;
}

/* lightbox */
function openLightbox(style, idx) {
  lb = { images: style.images, idx, title: style.name };
  $("#lightbox").hidden = false;
  document.body.style.overflow = "hidden";
  showLb();
}
function showLb() {
  const img = lb.images[lb.idx];
  const el = $("#lbImg");
  el.src = img.src;
  el.alt = `${lb.title} — ${img.label}`;
  $("#lbCaption").textContent = lb.images.length > 1
    ? `${lb.title} — ${img.label} (${lb.idx + 1} of ${lb.images.length})`
    : lb.title;
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

/* search + classification filter */
$("#search").addEventListener("input", applyFilters);

fetch("artwork.json")
  .then(r => r.json())
  .then(data => {
    DATA = data;
    renderNav();
    renderLessons();
    renderFilters();
    renderProgress();
  })
  .catch(err => {
    $("#lessons").innerHTML = "<p>Could not load the course data (artwork.json). If you opened this file directly from disk, serve the folder over HTTP instead — browsers block local JSON fetches.</p>";
    console.error(err);
  });
