(() => {
  const preview = document.querySelector("#study-preview");
  const image = preview.querySelector("img");
  let activeTrigger;
  let activePopup;
  let pinned = false;
  let closeTimer;

  function hidePopup() {
    clearTimeout(closeTimer);
    if (!activePopup) return;

    activePopup.hidden = true;
    if (activeTrigger.matches("button")) activeTrigger.setAttribute("aria-expanded", "false");
    activePopup = undefined;
    activeTrigger = undefined;
    pinned = false;
  }

  function positionPopup() {
    if (!activePopup) return;

    const anchor = activeTrigger.getBoundingClientRect();
    const { clientWidth: width, clientHeight: height } = document.documentElement;
    if (anchor.bottom <= 0 || anchor.top >= height) {
      hidePopup();
      return;
    }

    const margin = 8;
    const gap = 5;
    const { offsetWidth: popupWidth, offsetHeight: popupHeight } = activePopup;
    const left = anchor.left + (anchor.width - popupWidth) / 2;
    const below = anchor.bottom + gap;
    const above = anchor.top - gap - popupHeight;
    const useBelow = below + popupHeight <= height - margin || height - anchor.bottom >= anchor.top;
    const top = useBelow ? below : above;

    activePopup.style.left = `${Math.max(margin, Math.min(left, width - popupWidth - margin))}px`;
    activePopup.style.top = `${Math.max(margin, Math.min(top, height - popupHeight - margin))}px`;
  }

  function closeWhenOutside() {
    clearTimeout(closeTimer);
    closeTimer = setTimeout(() => {
      if (!pinned && !activeTrigger?.matches(":hover, :focus-visible") && !activePopup?.matches(":hover")) {
        hidePopup();
      }
    }, 140);
  }

  function bindPopup(trigger, popup, prepare) {
    const isAnswer = trigger.matches("button");
    function showPopup() {
      clearTimeout(closeTimer);
      if (activeTrigger !== trigger) hidePopup();
      activeTrigger = trigger;
      activePopup = popup;
      prepare?.();
      if (isAnswer) trigger.setAttribute("aria-expanded", "true");
      popup.hidden = false;
      positionPopup();
    }

    trigger.addEventListener("pointerenter", event => {
      if (event.pointerType === "mouse") showPopup();
    });
    trigger.addEventListener("pointerleave", closeWhenOutside);
    trigger.addEventListener("focus", () => {
      if (trigger.matches(":focus-visible")) showPopup();
    });
    trigger.addEventListener("blur", closeWhenOutside);
    trigger.addEventListener("click", () => {
      if (!isAnswer || (activeTrigger === trigger && pinned)) {
        hidePopup();
      } else {
        showPopup();
        pinned = activeTrigger === trigger;
      }
    });
  }

  for (const link of document.querySelectorAll(".style-reading a[data-preview]")) {
    const artwork = document.getElementById(link.hash.slice(1))?.querySelector(".style-board img");
    if (!artwork) continue;
    bindPopup(link, preview, () => {
      preview.dataset.crop = link.dataset.preview;
      const src = artwork.currentSrc || artwork.src;
      if (image.src !== src) image.src = src;
    });
  }

  for (const button of document.querySelectorAll(".study-answer-button")) {
    bindPopup(button, document.getElementById(button.getAttribute("aria-controls")));
  }

  for (const popup of document.querySelectorAll(".study-preview, .study-answer")) {
    popup.addEventListener("pointerenter", () => clearTimeout(closeTimer));
    popup.addEventListener("pointerleave", closeWhenOutside);
  }

  window.addEventListener("scroll", positionPopup, { passive: true });
  window.addEventListener("resize", positionPopup);
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") hidePopup();
  });
  document.addEventListener("pointerdown", event => {
    if (activePopup && !activePopup.contains(event.target) && !activeTrigger.contains(event.target)) {
      hidePopup();
    }
  });
})();
