"use strict";
const DONE_KEY = "tsmc-storytelling-course-done-v1";
let DATA = null;
let done = new Set(JSON.parse(localStorage.getItem(DONE_KEY) || "[]"));
let lb = { images: [], idx: 0, title: "", lastVariant: 0 };

const $ = (s, r = document) => r.querySelector(s);
const controlById = id => DATA.controls.find(c => c.id === id);

/* ---------- shared bits ---------- */
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
    a.textContent = `${i + 1}. ${lesson.title.split("—")[0].split(":")[0].trim()}`;
    nav.appendChild(a);
  });
}

function tile(img, opts = {}) {
  const fig = document.createElement("figure");
  const wrap = document.createElement("div");
  if (img.status === "pending") {
    wrap.className = "tile-wrap pending";
    wrap.innerHTML = `<p><strong>Plate in review</strong>${img.label}<br>${img.cue}</p>`;
    fig.appendChild(wrap);
    const cap = document.createElement("figcaption");
    cap.innerHTML = `<span class="plate-label">${img.label}</span> — in review, not yet published`;
    fig.appendChild(cap);
    return fig;
  }
  wrap.className = "tile-wrap" + (opts.control ? " is-control" : "");
  const im = document.createElement("img");
  im.loading = "lazy";
  im.src = img.thumb;
  im.alt = img.alt;
  im.dataset.full = img.src;
  wrap.appendChild(im);
  fig.appendChild(wrap);
  const cap = document.createElement("figcaption");
  if (opts.control) {
    cap.innerHTML = `<span class="ctl">Control ${img.id || ""}</span> — unchanged`;
  } else {
    cap.innerHTML = `<span class="plate-label quiz-hide">${img.label}</span><span class="cue"> — ${img.cue}</span>`;
    if (img.reuse_of) cap.innerHTML += ` <em>(reused from ${img.reuse_of})</em>`;
    if (img.note) cap.innerHTML += `<br><em>${img.note}</em>`;
  }
  fig.appendChild(cap);
  if (opts.onOpen) {
    im.addEventListener("click", opts.onOpen);
  }
  return fig;
}

function openLightbox(title, images, idx) {
  lb = { images, idx, title, lastVariant: idx > 0 ? idx : 1 };
  $("#lightbox").hidden = false;
  document.body.style.overflow = "hidden";
  showLb();
}
function showLb() {
  const t = lb.images[lb.idx];
  const el = $("#lbImg");
  el.src = t.img.src;
  el.alt = t.label;
  $("#lbCaption").textContent = `${t.label} (${lb.idx + 1} of ${lb.images.length})`;
  $("#lbPrev").disabled = lb.idx <= 0;
  $("#lbNext").disabled = lb.idx >= lb.images.length - 1;
  const hasCtl = lb.images.length > 1 && lb.images[0].ctl;
  $("#lbAB").hidden = !hasCtl;
  if (lb.idx > 0) lb.lastVariant = lb.idx;
}
function closeLightbox() {
  $("#lightbox").hidden = true;
  document.body.style.overflow = "";
}
$("#lbClose").addEventListener("click", closeLightbox);
$("#lbPrev").addEventListener("click", () => { if (lb.idx > 0) { lb.idx--; showLb(); } });
$("#lbNext").addEventListener("click", () => { if (lb.idx < lb.images.length - 1) { lb.idx++; showLb(); } });
$("#lbAB").addEventListener("click", () => {
  lb.idx = lb.idx === 0 ? Math.min(lb.lastVariant, lb.images.length - 1) : 0;
  showLb();
});
$("#lightbox").addEventListener("click", e => { if (e.target.id === "lightbox") closeLightbox(); });
document.addEventListener("keydown", e => {
  if ($("#lightbox").hidden) return;
  if (e.key === "Escape") closeLightbox();
  if (e.key === "ArrowLeft") $("#lbPrev").click();
  if (e.key === "ArrowRight") $("#lbNext").click();
});

/* ---------- group renderers ---------- */
function lbList(group, lesson) {
  const ctl = controlById(group.control);
  const list = [{ img: { src: ctl.src, alt: ctl.alt }, label: `Control ${ctl.id} — ${ctl.title}`, ctl: true }];
  group.images.filter(i => i.status === "accepted").forEach(i => {
    list.push({ img: { src: i.src, alt: i.alt }, label: `${group.title} — ${i.label}` });
  });
  return list;
}

function renderCompare(group, lesson, container) {
  const ctl = controlById(group.control);
  const grid = document.createElement("div");
  grid.className = "compare " + (group.control === "C01" ? "grid-face" : group.control === "C02" ? "grid-body" : "grid-land");
  const list = lbList(group, lesson);
  grid.appendChild(tile({ ...ctl, status: "accepted" }, {
    control: true,
    onOpen: () => openLightbox(group.title, list, 0),
  }));
  group.images.forEach((img, i) => {
    grid.appendChild(tile(img, {
      onOpen: img.status === "accepted"
        ? () => openLightbox(group.title, list, list.findIndex(x => x.label.endsWith(img.label)))
        : null,
    }));
  });
  container.appendChild(grid);
  const dialogue = group.images.find(i => i.dialogue);
  if (dialogue) {
    const d = document.createElement("div");
    d.className = "dialogue-line";
    d.innerHTML = `<span class="bubble">&ldquo;${dialogue.dialogue}&rdquo;</span>
      <p>The same line of dialogue, rendered by this page — never baked into the art — under every plate. Toggle the labels above to guess first.</p>`;
    container.appendChild(d);
  }
}

function renderLadder(group, lesson, container) {
  const imgs = group.images;
  const view = document.createElement("div");
  view.className = "ladder-view";
  const figWrap = document.createElement("div");
  view.appendChild(figWrap);
  const ctlRow = document.createElement("div");
  ctlRow.className = "ladder-ctl";
  const prev = document.createElement("button"); prev.textContent = "‹ Prev";
  const next = document.createElement("button"); next.textContent = "Next ›";
  const range = document.createElement("input");
  range.type = "range"; range.min = 0; range.max = imgs.length - 1; range.step = 1; range.value = 0;
  range.setAttribute("aria-label", "Intensity step");
  ctlRow.append(prev, range, next);
  view.appendChild(ctlRow);
  const lab = document.createElement("p");
  lab.className = "ladder-label";
  view.appendChild(lab);
  container.appendChild(view);
  let cur = 0;
  const list = lbList(group, lesson);
  function show(i) {
    cur = Math.max(0, Math.min(imgs.length - 1, i));
    range.value = cur;
    figWrap.innerHTML = "";
    figWrap.appendChild(tile(imgs[cur], {
      onOpen: imgs[cur].status === "accepted"
        ? () => openLightbox(group.title, list, list.findIndex(x => x.label.endsWith(imgs[cur].label)))
        : null,
    }));
    lab.innerHTML = `<span class="quiz-hide">${imgs[cur].label}</span> — step ${cur + 1} of ${imgs.length}: ${imgs[cur].cue}`;
    prev.disabled = cur <= 0;
    next.disabled = cur >= imgs.length - 1;
  }
  prev.addEventListener("click", () => show(cur - 1));
  next.addEventListener("click", () => show(cur + 1));
  range.addEventListener("input", () => show(+range.value));
  show(0);
}

function renderSequence(group, lesson, container) {
  const ctl = controlById(group.control);
  const note = document.createElement("p");
  note.className = "source-note";
  note.textContent = `Staging control ${ctl.id} (${ctl.title}) anchors this sequence; the frames below tell the story in order.`;
  container.appendChild(note);
  const strip = document.createElement("div");
  strip.className = "sequence";
  const ordered = [...group.images].sort((a, b) => (a.sequence_order || 99) - (b.sequence_order || 99));
  const list = lbList(group, lesson);
  ordered.forEach((img, i) => {
    const fig = tile(img, {
      onOpen: img.status === "accepted"
        ? () => openLightbox(group.title, list, list.findIndex(x => x.label.endsWith(img.label)))
        : null,
    });
    fig.dataset.orig = i;
    const role = document.createElement("span");
    role.className = "seq-role";
    role.textContent = img.label;
    fig.insertBefore(role, fig.firstChild);
    const capLabel = fig.querySelector(".plate-label");
    if (capLabel) capLabel.textContent = `Frame ${i + 1}`;
    if (i > 0 && i < ordered.length - 1) fig.classList.add("seq-mid");
    const move = document.createElement("div");
    move.className = "seq-move";
    const left = document.createElement("button"); left.textContent = "←"; left.setAttribute("aria-label", "Move frame earlier");
    const right = document.createElement("button"); right.textContent = "→"; right.setAttribute("aria-label", "Move frame later");
    left.addEventListener("click", () => { const p = fig.previousElementSibling; if (p) strip.insertBefore(fig, p); });
    right.addEventListener("click", () => { const n = fig.nextElementSibling; if (n) strip.insertBefore(n, fig); });
    move.append(left, right);
    fig.appendChild(move);
    strip.appendChild(fig);
  });
  container.appendChild(strip);
  const ctlRow = document.createElement("div");
  ctlRow.className = "seq-ctl";
  const hideBtn = document.createElement("button");
  hideBtn.textContent = "Hide the middle frames";
  hideBtn.addEventListener("click", () => {
    const on = strip.classList.toggle("seq-hidden");
    hideBtn.textContent = on ? "Reveal the middle frames" : "Hide the middle frames";
  });
  const resetBtn = document.createElement("button");
  resetBtn.textContent = "Reset the order";
  resetBtn.addEventListener("click", () => {
    [...strip.children].sort((a, b) => a.dataset.orig - b.dataset.orig)
      .forEach(f => strip.appendChild(f));
  });
  ctlRow.append(hideBtn, resetBtn);
  container.appendChild(ctlRow);
}

function renderCaptionExperiment(group, lesson, container) {
  const wrap = document.createElement("div");
  wrap.className = "caption-exp";
  const figHolder = document.createElement("div");
  wrap.appendChild(figHolder);
  const plateBtns = document.createElement("div");
  plateBtns.className = "caption-plates";
  wrap.appendChild(plateBtns);
  const capText = document.createElement("p");
  capText.className = "caption-text";
  wrap.appendChild(capText);
  const capBtns = document.createElement("div");
  capBtns.className = "caption-btns";
  wrap.appendChild(capBtns);
  container.appendChild(wrap);
  let plate = 0, cap = 0;
  function show() {
    const img = group.images[plate];
    figHolder.innerHTML = "";
    figHolder.appendChild(tile(img, {}));
    plateBtns.innerHTML = "";
    group.images.forEach((im, i) => {
      const b = document.createElement("button");
      b.textContent = im.label;
      b.setAttribute("aria-pressed", i === plate);
      b.addEventListener("click", () => { plate = i; cap = 0; show(); });
      plateBtns.appendChild(b);
    });
    const caps = (group.captions || {})[img.job] || [];
    capText.textContent = caps[cap] ? `“${caps[cap]}”` : "";
    capBtns.innerHTML = "";
    caps.forEach((c, i) => {
      const b = document.createElement("button");
      b.textContent = `Caption ${i + 1}`;
      b.setAttribute("aria-pressed", i === cap);
      b.addEventListener("click", () => { cap = i; show(); });
      capBtns.appendChild(b);
    });
  }
  show();
}

const RENDERERS = {
  "compare": renderCompare,
  "ladder": renderLadder,
  "sequence": renderSequence,
  "caption-experiment": renderCaptionExperiment,
};

function groupEl(lesson, group) {
  const el = document.createElement("article");
  el.className = "group" + (lesson.quiz ? " self-quiz" : "");
  el.id = "group-" + group.id;
  el.dataset.search = (lesson.title + " " + group.title + " " + group.learn + " " + group.meaning + " " +
    group.images.map(i => i.label + " " + i.cue).join(" ")).toLowerCase();

  const head = document.createElement("div");
  head.className = "group-head";
  head.innerHTML = `<h3>${group.title}</h3><span class="group-ctl">against control ${group.control}</span>`;
  el.appendChild(head);

  const changes = group.images.map(i => i.label).join(" · ");
  const fc = document.createElement("div");
  fc.className = "fixed-changes";
  fc.innerHTML = `<div><h4>What stays fixed</h4><p>${group.fixed}</p></div>
    <div><h4>What changes</h4><p>${changes}</p></div>`;
  el.appendChild(fc);

  const learn = document.createElement("p");
  learn.className = "group-learn";
  learn.textContent = group.learn;
  el.appendChild(learn);

  const body = document.createElement("div");
  body.className = "group-body";
  const stage = document.createElement("div");
  (RENDERERS[group.layout] || renderCompare)(group, lesson, stage);
  body.appendChild(stage);

  const aside = document.createElement("aside");
  aside.className = "look-box";
  aside.innerHTML = `<h4>What to look for</h4><ul>${group.observe.map(t => `<li>${t}</li>`).join("")}</ul>
    <p class="meaning quiz-hide"><strong>Intended meaning</strong>${group.meaning}</p>
    <p class="alt quiz-hide"><strong>Another reading:</strong> ${group.alternatives}</p>
    <div class="concepts">${group.concepts.map(c => `<span>${c}</span>`).join("")}</div>
    <p class="tip"><strong>In a prompt:</strong> ${group.prompt_tip}</p>`;
  body.appendChild(aside);
  el.appendChild(body);

  const prompts = group.images.filter(i => i.prompt);
  if (prompts.length) {
    const det = document.createElement("details");
    det.className = "prompt-details";
    det.innerHTML = `<summary>Generation prompts (${prompts.length})</summary>` +
      prompts.map(i => `<p><strong>${i.label}</strong></p><pre></pre>`).join("");
    det.querySelectorAll("pre").forEach((pre, i) => { pre.textContent = prompts[i].prompt; });
    el.appendChild(det);
  }

  const reveal = document.createElement("button");
  reveal.className = "reveal-btn";
  reveal.textContent = "Reveal names and meanings";
  reveal.hidden = !lesson.quiz;
  reveal.addEventListener("click", () => {
    el.classList.add("revealed");
    reveal.hidden = true;
  });
  el.appendChild(reveal);
  return el;
}

/* ---------- lessons ---------- */
function renderLessons() {
  const wrap = $("#lessons");
  let lastModule = null;
  DATA.lessons.forEach((lesson, li) => {
    if (lesson.module !== lastModule) {
      lastModule = lesson.module;
      const mod = DATA.modules.find(m => m.id === lesson.module);
      const mh = document.createElement("div");
      mh.className = "module-head";
      mh.dataset.module = lesson.module;
      mh.innerHTML = `<h2>${mod.title}</h2><p>${mod.lessons.length} lessons</p>`;
      wrap.appendChild(mh);
    }
    const sec = document.createElement("section");
    sec.className = "lesson";
    sec.id = "lesson-" + lesson.id;
    sec.dataset.module = lesson.module;
    const nPlates = lesson.groups.reduce((s, g) => s + g.images.length, 0);
    const head = document.createElement("div");
    head.className = "lesson-head";
    head.innerHTML = `
      <div class="lesson-kicker">Lesson ${li + 1} of ${DATA.lessons.length} · ${lesson.module_title} · ${lesson.groups.length} groups · ${nPlates} plates</div>
      <h2>${lesson.title}</h2>
      <p class="big-idea">${lesson.objective}</p>
      <p class="lesson-intro">${lesson.intro}</p>
      <p class="source-note">${lesson.source_note}</p>
      <div class="exercise"><strong>Try this</strong>${lesson.exercise}
        <details class="answer"><summary>Answer guidance</summary><p>${lesson.exercise_answer}</p></details></div>
      <label class="lesson-done"><input type="checkbox" data-done="${lesson.id}" ${done.has(lesson.id) ? "checked" : ""}> Mark this lesson complete</label>`;
    sec.appendChild(head);
    lesson.groups.forEach(g => sec.appendChild(groupEl(lesson, g)));
    wrap.appendChild(sec);
  });
  wrap.addEventListener("change", e => {
    const id = e.target.dataset && e.target.dataset.done;
    if (!id) return;
    e.target.checked ? done.add(id) : done.delete(id);
    saveDone();
  });
}

/* ---------- search + quiz ---------- */
$("#search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  let anyVisible = false;
  document.querySelectorAll(".lesson").forEach(sec => {
    let lessonVisible = false;
    sec.querySelectorAll(".group").forEach(g => {
      const hit = !q || g.dataset.search.includes(q);
      g.style.display = hit ? "" : "none";
      if (hit) lessonVisible = true;
    });
    if (!q) lessonVisible = true;
    sec.style.display = lessonVisible ? "" : "none";
    if (lessonVisible) anyVisible = true;
  });
  document.querySelectorAll(".module-head").forEach(mh => {
    const next = mh.nextElementSibling;
    mh.style.display = "none";
    let n = mh.nextElementSibling;
    while (n && !n.classList.contains("module-head")) {
      if (n.classList.contains("lesson") && n.style.display !== "none") { mh.style.display = ""; break; }
      n = n.nextElementSibling;
    }
  });
  $("#noResults").hidden = anyVisible;
});
$("#quizMode").addEventListener("change", e => {
  document.body.classList.toggle("quiz", e.target.checked);
  document.querySelectorAll(".group .reveal-btn").forEach(b => { b.hidden = false; });
});

/* ---------- boot ---------- */
fetch("storytelling.json")
  .then(r => r.json())
  .then(data => {
    DATA = data;
    const cov = data.coverage;
    $("#coverageLine").textContent =
      `${cov.lessons} lessons · ${cov.groups} comparison groups · ` +
      `${cov.study_accepted + cov.reuse_slots} published plates (${cov.study_accepted} new studies + ${cov.reuse_slots} deliberate reuses) · ` +
      `${cov.controls} controls` + (cov.study_pending ? ` · ${cov.study_pending} plate in review` : "") + `.`;
    const strip = $("#controlStrip");
    data.controls.filter(c => c.id !== "C00").forEach(c => {
      const fig = document.createElement("figure");
      fig.innerHTML = `<img src="${c.thumb}" alt="${c.alt}"><figcaption>${c.id} — ${c.title}</figcaption>`;
      strip.appendChild(fig);
    });
    renderNav();
    renderLessons();
    renderProgress();
  })
  .catch(err => {
    $("#lessons").innerHTML = "<p>Could not load the course data (storytelling.json). If you opened this file directly from disk, serve the folder over HTTP instead — browsers block local JSON fetches.</p>";
    console.error(err);
  });
