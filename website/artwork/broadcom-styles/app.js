import { CHAPTERS, VARIANT_LABELS } from "./data/chapters.js";
import { STYLES_1 } from "./data/styles-1.js";
import { STYLES_2 } from "./data/styles-2.js";
import { STYLES_3 } from "./data/styles-3.js";

const ALL_STYLES = [...STYLES_1, ...STYLES_2, ...STYLES_3];
const STYLE_MAP = new Map(ALL_STYLES.map((s) => [s.id, s]));
const CHAPTER_MAP = new Map(CHAPTERS.map((c) => [c.id, c]));

const state = {
  filter: "all",
  query: "",
  selectedVariant: new Map(),
  pinned: [],
  activeStudyId: null,
  activeStudyVariant: 1,
};

const els = {
  chapterNav: document.getElementById("chapterNav"),
  catalogRoot: document.getElementById("catalogRoot"),
  searchInput: document.getElementById("searchInput"),
  filterBtns: [...document.querySelectorAll(".filter-btn")],
  statusLine: document.getElementById("statusLine"),
  themeToggle: document.getElementById("themeToggle"),
  openCompareBtn: document.getElementById("openCompareBtn"),
  compareCount: document.getElementById("compareCount"),
  studyDialog: document.getElementById("studyDialog"),
  studyChapter: document.getElementById("studyChapter"),
  studyTitle: document.getElementById("studyTitle"),
  studyImg: document.getElementById("studyImg"),
  studyVariants: document.getElementById("studyVariants"),
  studyVariantNote: document.getElementById("studyVariantNote"),
  studyEra: document.getElementById("studyEra"),
  studyHook: document.getElementById("studyHook"),
  studyHow: document.getElementById("studyHow"),
  studyLookFor: document.getElementById("studyLookFor"),
  studyTryIt: document.getElementById("studyTryIt"),
  studyTags: document.getElementById("studyTags"),
  studyCompareBtn: document.getElementById("studyCompareBtn"),
  prevStyleBtn: document.getElementById("prevStyleBtn"),
  nextStyleBtn: document.getElementById("nextStyleBtn"),
  closeStudyBtn: document.getElementById("closeStudyBtn"),
  compareDialog: document.getElementById("compareDialog"),
  compareGrid: document.getElementById("compareGrid"),
  clearCompareBtn: document.getElementById("clearCompareBtn"),
  closeCompareBtn: document.getElementById("closeCompareBtn"),
};

function imagePath(style, variant = 1) {
  if (style.variants === 1) return `images/${style.id}.webp`;
  return `images/${style.id}-v0${variant}.webp`;
}

function getCardVariant(style) {
  return state.selectedVariant.get(style.id) || 1;
}

function matchesQuery(style, query) {
  if (!query) return true;
  const hay = [
    style.name,
    style.era,
    style.hook,
    style.howItWorks,
    ...style.tags,
    ...style.lookFor,
    CHAPTER_MAP.get(style.chapter)?.title || "",
  ]
    .join(" ")
    .toLowerCase();
  return hay.includes(query);
}

function filteredStyles() {
  const q = state.query.trim().toLowerCase();
  return ALL_STYLES.filter((style) => {
    if (state.filter === "4" && style.variants !== 4) return false;
    if (state.filter === "1" && style.variants !== 1) return false;
    return matchesQuery(style, q);
  });
}

function renderChapterNav() {
  els.chapterNav.innerHTML = CHAPTERS.map(
    (ch) => `<a class="chapter-pill" href="#${ch.id}"><strong>${ch.number}</strong>${ch.title}</a>`
  ).join("");
}

function togglePin(styleId) {
  const idx = state.pinned.indexOf(styleId);
  if (idx >= 0) {
    state.pinned.splice(idx, 1);
  } else {
    if (state.pinned.length >= 2) state.pinned.shift();
    state.pinned.push(styleId);
  }
  updateCompareControls();
  renderCatalog();
  if (state.activeStudyId === styleId) {
    updateStudyPinButton();
  }
}

function updateCompareControls() {
  els.compareCount.textContent = String(state.pinned.length);
  els.openCompareBtn.disabled = state.pinned.length < 2;
}

function renderCatalog() {
  const visible = filteredStyles();
  const totalPlates = visible.reduce((sum, s) => sum + s.variants, 0);
  els.statusLine.textContent = `Showing ${visible.length} of ${ALL_STYLES.length} styles (${totalPlates} plates). Click any plate to read the beginner lesson, or pin 2 styles to compare side by side.`;

  if (!visible.length) {
    els.catalogRoot.innerHTML = `<div class="empty-state"><p>No art styles matched <strong>${escapeHtml(state.query)}</strong>. Clear the search box or switch filters to see all 105 styles.</p></div>`;
    return;
  }

  const byChapter = new Map(CHAPTERS.map((ch) => [ch.id, []]));
  for (const style of visible) {
    byChapter.get(style.chapter)?.push(style);
  }

  const frag = document.createDocumentFragment();
  for (const ch of CHAPTERS) {
    const items = byChapter.get(ch.id) || [];
    if (!items.length) continue;

    const section = document.createElement("section");
    section.className = "chapter-section";
    section.id = ch.id;

    section.innerHTML = `
      <header class="chapter-head">
        <div>
          <p class="chapter-head__num">Chapter ${ch.number} · ${items.length} ${items.length === 1 ? "style" : "styles"}</p>
          <h2>${escapeHtml(ch.title)}</h2>
          <p class="chapter-head__sub">${escapeHtml(ch.subtitle)}</p>
        </div>
        <div>
          <p class="chapter-head__intro">${escapeHtml(ch.intro)}</p>
          <p class="chapter-head__goal"><strong>Beginner focus:</strong> ${escapeHtml(ch.skillGoal)}</p>
        </div>
      </header>
    `;

    const grid = document.createElement("div");
    grid.className = "style-grid";

    for (const style of items) {
      const currentV = getCardVariant(style);
      const isPinned = state.pinned.includes(style.id);
      const card = document.createElement("article");
      card.className = "style-card";
      card.dataset.styleId = style.id;

      const variantStrip =
        style.variants === 4
          ? `<div class="variant-strip" role="group" aria-label="Variants for ${escapeHtml(style.name)}">
              ${VARIANT_LABELS.map(
                (v, i) =>
                  `<button type="button" class="variant-chip ${currentV === i + 1 ? "is-active" : ""}" data-variant="${i + 1}" title="${escapeHtml(v.title)}">${i + 1} · ${escapeHtml(v.short)}</button>`
              ).join("")}
            </div>`
          : "";

      card.innerHTML = `
        <div class="style-card__media">
          <img src="${imagePath(style, currentV)}" width="780" height="1040" loading="lazy" alt="Broadcom in ${escapeHtml(style.name)} style${style.variants === 4 ? `, variant ${currentV}` : ""}">
          <span class="style-card__count">${style.variants === 4 ? `4 variants · v0${currentV}` : "1 study"}</span>
        </div>
        ${variantStrip}
        <div class="style-card__body">
          <p class="style-card__era">${escapeHtml(style.era)}</p>
          <h3 class="style-card__title">${escapeHtml(style.name)}</h3>
          <p class="style-card__hook">${escapeHtml(style.hook)}</p>
          <div class="style-card__actions">
            <button type="button" class="card-btn card-btn--primary" data-action="study">Study guide</button>
            <button type="button" class="card-btn ${isPinned ? "is-pinned" : ""}" data-action="pin">${isPinned ? "Pinned ✓" : "Compare"}</button>
          </div>
        </div>
      `;

      const imgEl = card.querySelector("img");
      imgEl.addEventListener("click", () => openStudy(style.id, getCardVariant(style)));

      card.querySelectorAll(".variant-chip").forEach((btn) => {
        btn.addEventListener("click", () => {
          const v = Number(btn.dataset.variant);
          state.selectedVariant.set(style.id, v);
          imgEl.src = imagePath(style, v);
          imgEl.alt = `Broadcom in ${style.name} style, variant ${v}`;
          card.querySelector(".style-card__count").textContent = `4 variants · v0${v}`;
          card.querySelectorAll(".variant-chip").forEach((b) => b.classList.toggle("is-active", Number(b.dataset.variant) === v));
        });
      });

      card.querySelector('[data-action="study"]').addEventListener("click", () => openStudy(style.id, getCardVariant(style)));
      card.querySelector('[data-action="pin"]').addEventListener("click", () => togglePin(style.id));

      grid.appendChild(card);
    }

    section.appendChild(grid);
    frag.appendChild(section);
  }

  els.catalogRoot.innerHTML = "";
  els.catalogRoot.appendChild(frag);
}

function updateStudyPinButton() {
  if (!state.activeStudyId) return;
  const pinned = state.pinned.includes(state.activeStudyId);
  els.studyCompareBtn.textContent = pinned ? "Pinned to Compare ✓" : "Pin to Compare";
  els.studyCompareBtn.setAttribute("aria-pressed", String(pinned));
}

function renderStudyVariant(style, variant) {
  state.activeStudyVariant = variant;
  els.studyImg.src = imagePath(style, variant);
  els.studyImg.alt = `Broadcom in ${style.name}${style.variants === 4 ? ` — ${VARIANT_LABELS[variant - 1].title}` : ""}`;
  if (style.variants === 4) {
    const info = VARIANT_LABELS[variant - 1];
    els.studyVariantNote.textContent = `${info.title}: ${info.note}`;
    els.studyVariants.innerHTML = VARIANT_LABELS.map(
      (v, i) =>
        `<button type="button" class="variant-tab ${variant === i + 1 ? "is-active" : ""}" data-variant="${i + 1}">${i + 1} · ${escapeHtml(v.short)}</button>`
    ).join("");
    els.studyVariants.querySelectorAll(".variant-tab").forEach((btn) => {
      btn.addEventListener("click", () => renderStudyVariant(style, Number(btn.dataset.variant)));
    });
  } else {
    els.studyVariants.innerHTML = "";
    els.studyVariantNote.textContent = "Single study plate — one focused demonstration of the medium.";
  }
}

function openStudy(styleId, variant = 1) {
  const style = STYLE_MAP.get(styleId);
  if (!style) return;
  state.activeStudyId = styleId;
  const ch = CHAPTER_MAP.get(style.chapter);
  els.studyChapter.textContent = ch ? `Chapter ${ch.number} · ${ch.title}` : "";
  els.studyTitle.textContent = style.name;
  els.studyEra.textContent = style.era;
  els.studyHook.textContent = style.hook;
  els.studyHow.textContent = style.howItWorks;
  els.studyLookFor.innerHTML = style.lookFor.map((cue) => `<li>${escapeHtml(cue)}</li>`).join("");
  els.studyTryIt.textContent = style.tryIt;
  els.studyTags.innerHTML = style.tags.map((t) => `<span class="tag-chip">${escapeHtml(t)}</span>`).join("");

  renderStudyVariant(style, style.variants === 4 ? variant : 1);
  updateStudyPinButton();

  if (history.replaceState) {
    history.replaceState(null, "", `#${style.id}`);
  }
  if (!els.studyDialog.open) {
    els.studyDialog.showModal();
  }
}

function stepStudy(delta) {
  const list = filteredStyles();
  if (!list.length || !state.activeStudyId) return;
  const idx = list.findIndex((s) => s.id === state.activeStudyId);
  const next = list[(idx + delta + list.length) % list.length];
  openStudy(next.id, getCardVariant(next));
}

function openCompare() {
  if (state.pinned.length < 2) return;
  els.compareGrid.innerHTML = state.pinned
    .map((id) => {
      const style = STYLE_MAP.get(id);
      if (!style) return "";
      const v = getCardVariant(style);
      return `
        <article class="compare-col">
          <img src="${imagePath(style, v)}" alt="Broadcom in ${escapeHtml(style.name)}">
          <p class="style-card__era">${escapeHtml(style.era)}</p>
          <h3>${escapeHtml(style.name)}</h3>
          <p><strong>Core idea:</strong> ${escapeHtml(style.hook)}</p>
          <ul>${style.lookFor.map((cue) => `<li>${escapeHtml(cue)}</li>`).join("")}</ul>
        </article>
      `;
    })
    .join("");
  els.compareDialog.showModal();
}

function escapeHtml(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

// Event bindings
els.searchInput.addEventListener("input", (e) => {
  state.query = e.target.value;
  renderCatalog();
});

els.filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    state.filter = btn.dataset.filter;
    els.filterBtns.forEach((b) => b.classList.toggle("is-active", b === btn));
    renderCatalog();
  });
});

els.themeToggle.addEventListener("click", () => {
  const root = document.documentElement;
  const dark = root.getAttribute("data-theme") !== "dark";
  root.setAttribute("data-theme", dark ? "dark" : "light");
  els.themeToggle.setAttribute("aria-pressed", String(dark));
  els.themeToggle.textContent = dark ? "Light gallery" : "Dark gallery";
});

els.openCompareBtn.addEventListener("click", openCompare);
els.clearCompareBtn.addEventListener("click", () => {
  state.pinned = [];
  updateCompareControls();
  renderCatalog();
  els.compareDialog.close();
});
els.closeCompareBtn.addEventListener("click", () => els.compareDialog.close());

els.prevStyleBtn.addEventListener("click", () => stepStudy(-1));
els.nextStyleBtn.addEventListener("click", () => stepStudy(1));
els.closeStudyBtn.addEventListener("click", () => els.studyDialog.close());
els.studyCompareBtn.addEventListener("click", () => {
  if (state.activeStudyId) togglePin(state.activeStudyId);
});

els.studyDialog.addEventListener("click", (e) => {
  if (e.target === els.studyDialog) els.studyDialog.close();
});
els.compareDialog.addEventListener("click", (e) => {
  if (e.target === els.compareDialog) els.compareDialog.close();
});

document.addEventListener("keydown", (e) => {
  if (!els.studyDialog.open) return;
  if (e.key === "ArrowLeft") stepStudy(-1);
  else if (e.key === "ArrowRight") stepStudy(1);
  else if (["1", "2", "3", "4"].includes(e.key)) {
    const style = STYLE_MAP.get(state.activeStudyId);
    if (style && style.variants === 4) renderStudyVariant(style, Number(e.key));
  }
});

renderChapterNav();
updateCompareControls();
renderCatalog();

const initialHash = location.hash.replace(/^#/, "");
if (STYLE_MAP.has(initialHash)) {
  openStudy(initialHash, 1);
}
