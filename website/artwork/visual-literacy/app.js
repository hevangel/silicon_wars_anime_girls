"use strict";
const $ = (s, r = document) => r.querySelector(s);

const COURSES = [
  { part: "Part I", title: "The TSMC Style Course", sub: "Visual Languages and Dialects",
    href: "../tsmc-styles/", json: "../tsmc-styles/artwork.json",
    doneKey: "tsmc-style-course-done-v1",
    blurb: "One model, one café pose, 419 art styles. A style is a reusable library — a language for making pictures — and holding everything else still makes the language itself visible.",
    counts: d => `${d.lessons.length} lessons · ${d.meta.totalStyles} styles · ${d.meta.totalImages} pictures`,
    total: d => d.lessons.length },
  { part: "Part II", title: "The TSMC Seeing Course", sub: "Visual Vocabulary and Grammar",
    href: "../tsmc-seeing/", json: "../tsmc-seeing/seeing.json",
    doneKey: "tsmc-seeing-course-done-v1",
    blurb: "The experiment in reverse: style, scene and character fixed; each card changes exactly one visual decision — light, value, viewpoint, composition — and shows it beside the control.",
    counts: d => `${d.lessons.length} lessons · ${d.lessons.reduce((s, l) => s + l.cards.length, 0)} cards · ${d.lessons.reduce((s, l) => s + l.cards.reduce((a, c) => a + c.images.length, 0), 0)} pictures + the control`,
    total: d => d.lessons.length },
  { part: "Part III", title: "The TSMC Storytelling Course", sub: "Visual Semantics and Pragmatics",
    href: "../tsmc-storytelling/", json: "../tsmc-storytelling/storytelling.json",
    doneKey: "tsmc-storytelling-course-done-v1",
    blurb: "Start from an intended meaning — loneliness, authority, suspense — and choose the decisions that carry it: expressions, gestures, symbols, sequences, captions. Ends with intended vs perceived meaning.",
    counts: d => `${d.coverage.lessons} lessons · ${d.coverage.groups} groups · ${d.coverage.study_accepted + d.coverage.reuse_slots} plates · ${d.coverage.controls} controls`,
    total: d => d.lessons.length },
];

function doneCount(key) {
  try { return JSON.parse(localStorage.getItem(key) || "[]").length; } catch { return 0; }
}

async function renderCourses() {
  const wrap = $("#courses");
  for (const c of COURSES) {
    const card = document.createElement("article");
    card.className = "course-card";
    card.innerHTML = `<p class="course-part">${c.part} — ${c.sub}</p><h3>${c.title}</h3>
      <p class="course-blurb">${c.blurb}</p><p class="course-counts">Loading…</p>
      <p class="course-progress"></p><a class="course-link" href="${c.href}">Open the course →</a>`;
    wrap.appendChild(card);
    try {
      const d = await (await fetch(c.json)).json();
      card.querySelector(".course-counts").textContent = c.counts(d);
      const n = doneCount(c.doneKey), total = c.total(d);
      card.querySelector(".course-progress").textContent =
        n ? `Your progress: ${n} of ${total} lessons complete` : "Not started yet — progress is kept in your browser.";
    } catch {
      card.querySelector(".course-counts").textContent = "Counts unavailable offline.";
    }
  }
}

let CONCEPTS = [];
function renderRegistry() {
  const list = $("#conceptList");
  list.innerHTML = "";
  CONCEPTS.forEach(c => {
    const b = document.createElement("button");
    b.className = "concept-chip";
    b.dataset.search = (c.name + " " + c.refs.map(r => r.label).join(" ")).toLowerCase();
    b.innerHTML = `${c.name} <span class="chip-layer">L${c.layer}</span>`;
    b.addEventListener("click", () => showConcept(c, b));
    list.appendChild(b);
  });
}
function showConcept(c, btn) {
  document.querySelectorAll(".concept-chip").forEach(x => x.classList.toggle("active", x === btn));
  const byCourse = {};
  c.refs.forEach(r => { (byCourse[r.course] = byCourse[r.course] || []).push(r); });
  const kindText = {
    "Part I": "Styles that tend to use or carry it",
    "Part II": "Where it is taught as a decision",
    "Part III": "Where it is put to work as meaning",
  };
  const html = Object.entries(byCourse).map(([course, refs]) => `
    <h4>${course} — ${kindText[course] || ""}</h4>
    <ul>${refs.map(r => `<li><a href="${r.href}">${r.label}</a></li>`).join("")}</ul>`).join("");
  $("#conceptDetail").innerHTML = `
    <h3>${c.name}</h3>
    <p class="detail-meta">Stack layer ${c.layer} — ${c.layer_title} · a ${c.type} concept · ${c.refs.length} references across ${Object.keys(byCourse).length} course(s). Tendencies, not rules.</p>
    ${html}`;
}

$("#search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  let any = false;
  document.querySelectorAll(".concept-chip").forEach(chip => {
    const hit = !q || chip.dataset.search.includes(q);
    chip.style.display = hit ? "" : "none";
    if (hit) any = true;
  });
  document.querySelectorAll(".course-card").forEach(card => {
    const hit = !q || card.textContent.toLowerCase().includes(q);
    card.style.display = hit ? "" : "none";
    if (hit) any = true;
  });
  $("#noResults").hidden = any;
});

Promise.all([
  fetch("concepts.json").then(r => r.json()),
]).then(([reg]) => {
  $("#stack").innerHTML = reg.stack.map(l => `
    <li><span class="stack-layer">Layer ${l.layer}</span>
      <span class="stack-title">${l.title}</span>
      <span class="stack-parts">${l.parts}</span></li>`).join("");
  CONCEPTS = reg.concepts;
  renderRegistry();
}).catch(err => {
  $("#conceptList").innerHTML = "<p>Could not load the concept registry (concepts.json). Serve the folder over HTTP — browsers block local JSON fetches.</p>";
  console.error(err);
});
renderCourses();
