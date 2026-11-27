const sheetsGrid = document.getElementById("sheetsGrid");
const viewBtns = [...document.querySelectorAll(".view-btn[data-view]")];

viewBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const stacked = btn.dataset.view === "stacked";
    sheetsGrid?.classList.toggle("is-stacked", stacked);
    viewBtns.forEach((b) => {
      const active = b === btn;
      b.classList.toggle("is-active", active);
      b.setAttribute("aria-pressed", String(active));
    });
  });
});

const lightbox = document.getElementById("stageLightbox");
const lbKicker = document.getElementById("lbKicker");
const lbTitle = document.getElementById("lbTitle");
const lbImg = document.getElementById("lbImg");
const lbCaption = document.getElementById("lbCaption");
const lbRaw = document.getElementById("lbRaw");
const lbPrev = document.getElementById("lbPrev");
const lbNext = document.getElementById("lbNext");
const lbClose = document.getElementById("lbClose");

const triggers = [...document.querySelectorAll("[data-lightbox]")];
const items = triggers.map((el) => ({
  src: el.getAttribute("href"),
  kicker: el.dataset.kicker || "Key art",
  title: el.dataset.title || "",
  caption: el.dataset.caption || "",
  alt: el.querySelector("img")?.alt || el.dataset.title || "",
}));

let activeIndex = 0;

function showItem(index) {
  if (!items.length) return;
  activeIndex = (index + items.length) % items.length;
  const item = items[activeIndex];
  lbKicker.textContent = item.kicker;
  lbTitle.textContent = item.title;
  lbImg.src = item.src;
  lbImg.alt = item.alt;
  lbCaption.textContent = item.caption;
  lbRaw.href = item.src;
}

if (lightbox && triggers.length) {
  triggers.forEach((el, idx) => {
    el.addEventListener("click", (e) => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      showItem(idx);
      if (!lightbox.open) lightbox.showModal();
    });
  });

  document.querySelectorAll("[data-open-lightbox]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetSrc = btn.dataset.openLightbox;
      const idx = items.findIndex((it) => it.src === targetSrc);
      showItem(idx >= 0 ? idx : 0);
      if (!lightbox.open) lightbox.showModal();
    });
  });

  lbPrev?.addEventListener("click", () => showItem(activeIndex - 1));
  lbNext?.addEventListener("click", () => showItem(activeIndex + 1));
  lbClose?.addEventListener("click", () => lightbox.close());

  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) lightbox.close();
  });

  document.addEventListener("keydown", (e) => {
    if (!lightbox.open) return;
    if (e.key === "ArrowLeft") showItem(activeIndex - 1);
    else if (e.key === "ArrowRight") showItem(activeIndex + 1);
  });
}
