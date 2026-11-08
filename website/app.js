// Silicon Wars character archive.
// All copy, ordering, artwork availability, and tuning values live in data/*.json.
(async () => {
  const SITE_URL = "data/site.json";

  const fetchJson = async (url) => {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
    return response.json();
  };

  const lookup = (object, path) => path.split(".").reduce((value, key) => value?.[key], object);
  const fill = (template, values) => template.replace(/\{(\w+)\}/g, (_, key) => values[key] ?? "");

  let site;
  let characters;
  try {
    site = await fetchJson(SITE_URL);
    ({ characters } = await fetchJson(site.paths.characters));
  } catch (error) {
    document.querySelector("main").textContent =
      `Could not load site data (${error.message}). Serve the repository root over HTTP, e.g. "py -m http.server", and open /website/.`;
    throw error;
  }

  const { behavior, assetTypes } = site;
  const assetUrl = (path) => site.paths.assetBase + path;

  // Static copy ---------------------------------------------------------------
  document.documentElement.lang = site.meta.lang;
  document.title = site.meta.title;
  document.querySelector('meta[name="description"]').content = site.meta.description;
  document.querySelector('meta[name="theme-color"]').content = site.meta.themeColor;
  document.querySelectorAll("[data-text]").forEach((element) => {
    element.textContent = lookup(site, element.dataset.text) ?? "";
  });
  document.querySelectorAll("[data-aria-label]").forEach((element) => {
    element.setAttribute("aria-label", lookup(site, element.dataset.ariaLabel) ?? "");
  });
  document.querySelector(".card-count").textContent =
    fill(site.gallery.countTemplate, { count: characters.length });

  const assetLinks = document.querySelector(".asset-links");
  assetTypes.forEach((type) => {
    const link = document.createElement("a");
    link.className = "asset-link";
    link.href = `#assets/${type.id}`;
    link.textContent = type.navLabel;
    assetLinks.append(link);
  });

  const sheetGrid = document.querySelector(".sheet-grid");
  assetTypes.filter((type) => type.profileHeading).forEach((type) => {
    const sheetCard = document.createElement("article");
    sheetCard.className = "sheet-card";
    sheetCard.dataset.sheet = type.id;
    sheetCard.innerHTML =
      '<h3></h3><div class="sheet-image-wrap"><img class="sheet-image" alt="" hidden><p class="sheet-unavailable"></p></div>';
    sheetCard.querySelector("h3").textContent = type.profileHeading;
    sheetCard.querySelector(".sheet-unavailable").textContent = site.profile.unavailable;
    sheetGrid.append(sheetCard);
  });

  // Gallery cards -------------------------------------------------------------
  const carousel = document.querySelector(".carousel");
  const track = document.querySelector(".track");
  const characterBySlug = new Map(characters.map((character) => [character.slug, character]));

  const buildCard = (character, index) => {
    const card = document.createElement("article");
    card.className = "character-card";
    card.dataset.slug = character.slug;

    const image = document.createElement("img");
    image.src = assetUrl(character.referenceCard);
    image.alt = `${character.name} — ${character.title}`;
    if (index < behavior.eagerLoadCount) image.setAttribute("fetchpriority", "high");
    else image.loading = "lazy";

    const caption = document.createElement("div");
    caption.className = "card-caption";
    const name = document.createElement("span");
    name.className = "character-name";
    name.textContent = character.name;
    const title = document.createElement("span");
    title.className = "character-title";
    title.textContent = character.title;
    caption.append(name, title);

    const blurb = document.createElement("p");
    blurb.className = "card-description";
    blurb.textContent = character.description;

    const link = document.createElement("a");
    link.className = "character-link";
    link.href = `#character/${character.slug}`;
    link.setAttribute("aria-label", fill(site.gallery.viewProfileTemplate, { name: character.name }));

    card.append(image, caption, blurb, link);
    return card;
  };

  const cards = characters.map(buildCard);
  track.append(...cards);

  // Views ---------------------------------------------------------------------
  const controls = [...document.querySelectorAll(".carousel-control")];
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const galleryView = document.querySelector("#gallery-view");
  const profileView = document.querySelector("#character-profile");
  const assetArchive = document.querySelector("#asset-archive");
  const profileBack = document.querySelector(".profile-back");
  const assetArchiveBack = document.querySelector(".asset-archive-back");
  const assetArchiveTitle = document.querySelector(".asset-archive-title");
  const assetArchiveCount = document.querySelector(".asset-archive-count");
  const assetList = document.querySelector(".asset-list");
  const profileCardImage = document.querySelector(".profile-card-image");
  const profileName = document.querySelector(".profile-card-caption .character-name");
  const profileTitle = document.querySelector(".profile-card-caption .character-title");
  const profileDescription = document.querySelector(".portfolio-description");
  const profileAbility = document.querySelector(".profile-ability");
  const profileAbilityName = profileAbility.querySelector("span");
  const profileKicker = document.querySelector(".profile-kicker");
  const assetTypeById = new Map(assetTypes.map((type) => [type.id, type]));

  const showGallery = () => {
    profileView.hidden = true;
    assetArchive.hidden = true;
    galleryView.hidden = false;
    document.title = site.meta.title;
  };

  const scrollToTop = () =>
    window.scrollTo({ top: 0, behavior: reduceMotion.matches ? "auto" : "smooth" });

  const renderProfile = (slug) => {
    const character = characterBySlug.get(slug);
    if (!character) return showGallery();

    profileCardImage.src = assetUrl(character.referenceCard);
    profileCardImage.alt = `${character.name} — ${character.title}`;
    profileName.textContent = character.name;
    profileTitle.textContent = character.title;
    profileDescription.textContent = character.description;
    profileAbility.hidden = !character.ability;
    profileAbilityName.textContent = character.ability || "";
    profileKicker.textContent = character.faction
      ? fill(site.profile.kickerWithFactionTemplate, { faction: character.faction })
      : site.profile.kicker;

    document.querySelectorAll(".sheet-card").forEach((sheetCard) => {
      const type = assetTypeById.get(sheetCard.dataset.sheet);
      const artwork = sheetCard.querySelector(".sheet-image");
      const unavailable = sheetCard.querySelector(".sheet-unavailable");
      artwork.hidden = true;
      unavailable.hidden = false;
      artwork.onload = () => {
        artwork.hidden = false;
        unavailable.hidden = true;
      };
      artwork.onerror = () => {
        artwork.hidden = true;
        unavailable.hidden = false;
      };
      artwork.alt = `${character.name} ${type.altLabel}`;
      const path = character.artwork?.[type.id];
      if (!path) {
        artwork.removeAttribute("src");
        return;
      }
      artwork.src = assetUrl(path);
    });

    galleryView.hidden = true;
    assetArchive.hidden = true;
    profileView.hidden = false;
    document.title = fill(site.meta.profileTitleTemplate, { name: character.name });
    scrollToTop();
  };

  const renderAssetArchive = (typeId) => {
    const type = assetTypeById.get(typeId);
    if (!type) return false;

    const items = characters.flatMap((character) => {
      const path = typeId === "reference_card" ? character.referenceCard : character.artwork?.[typeId];
      return path ? [{ name: character.name, path }] : [];
    });

    assetArchiveTitle.textContent = fill(site.assetArchive.titleTemplate, { title: type.archiveTitle });
    assetArchiveCount.textContent = fill(site.assetArchive.countTemplate, { count: items.length });
    assetList.replaceChildren();
    items.forEach(({ name, path }) => {
      const entry = document.createElement("article");
      entry.className = "asset-entry";
      const heading = document.createElement("h2");
      heading.textContent = name;
      const image = document.createElement("img");
      image.src = assetUrl(path);
      image.alt = `${name} ${type.altLabel}`;
      image.loading = "lazy";
      entry.append(heading, image);
      assetList.append(entry);
    });

    galleryView.hidden = true;
    profileView.hidden = true;
    assetArchive.hidden = false;
    document.title = fill(site.meta.archiveTitleTemplate, { title: type.archiveTitle });
    scrollToTop();
    return true;
  };

  const renderRoute = () => {
    const match = location.hash.match(/^#character\/([a-z0-9-]+)$/);
    const assetMatch = location.hash.match(/^#assets\/([a-z_]+)$/);
    if (match) renderProfile(match[1]);
    else if (!assetMatch || !renderAssetArchive(assetMatch[1])) showGallery();
  };

  track.addEventListener("click", (event) => {
    if (didDrag) {
      event.preventDefault();
      event.stopPropagation();
      didDrag = false;
    }
  });
  profileBack.addEventListener("click", () => {
    history.replaceState(null, "", "#characters");
    renderRoute();
  });
  assetArchiveBack.addEventListener("click", () => {
    history.replaceState(null, "", "#characters");
    renderRoute();
  });
  window.addEventListener("popstate", renderRoute);
  window.addEventListener("hashchange", renderRoute);
  renderRoute();

  // Endless carousel ----------------------------------------------------------
  const cloneCard = (card) => {
    const clone = card.cloneNode(true);
    clone.setAttribute("aria-hidden", "true");
    clone.removeAttribute("tabindex");
    clone.querySelector(".character-link").tabIndex = -1;
    clone.querySelector("img").alt = "";
    clone.querySelector("img").removeAttribute("fetchpriority");
    clone.querySelector("img").loading = "lazy";
    return clone;
  };
  // A complete copy on each side lets either direction cross the seam.
  const leading = cards.map(cloneCard);
  const trailing = cards.map(cloneCard);
  track.prepend(...leading);
  track.append(...trailing);

  let hoveredDirection = 0;
  let focusedDirection = 0;
  let previousTime = 0;
  let loopWidth = 0;
  let position = 0;
  let lastWritten = 0;
  let lastActivity = -Infinity;
  let interacting = false;
  let pointerOverCarousel = false;
  let dragX = null;
  let dragStartX = null;
  let didDrag = false;
  let clickDistance = 0;

  const normalize = (value) => loopWidth
    ? loopWidth + ((value - loopWidth) % loopWidth + loopWidth) % loopWidth
    : value;

  const renderPosition = (value) => {
    position = normalize(value);
    carousel.scrollLeft = position;
    lastWritten = carousel.scrollLeft;
  };

  const measure = () => {
    const progress = loopWidth ? (position - loopWidth) / loopWidth : 0;
    loopWidth = trailing[0].offsetLeft - cards[0].offsetLeft;
    renderPosition(loopWidth * (1 + progress));
  };

  const animate = (time) => {
    if (previousTime && !document.hidden && profileView.hidden) {
      const elapsed = Math.min(time - previousTime, behavior.maxFrameMs) / 1000;
      const direction = hoveredDirection || focusedDirection;
      const keyboardFocus = carousel.matches(":focus-visible") || carousel.querySelector(":focus-visible");
      const idle = time - lastActivity > behavior.idleDelayMs && !keyboardFocus && !pointerOverCarousel;
      const speed = reduceMotion.matches || interacting
        ? 0
        : direction ? direction * behavior.hoverSpeed : idle ? behavior.idleSpeed : 0;
      const step = Math.sign(clickDistance) * Math.min(Math.abs(clickDistance), behavior.clickScrollSpeed * elapsed);
      clickDistance -= step;
      // Keep fractional pixels here: browsers may round scrollLeft on every write.
      if (speed || step) renderPosition(position + speed * elapsed + step);
    }
    previousTime = time;
    requestAnimationFrame(animate);
  };

  controls.forEach((control) => {
    const controlDirection = Number(control.dataset.direction);
    control.addEventListener("pointerenter", () => { hoveredDirection = controlDirection; });
    control.addEventListener("pointerleave", () => { hoveredDirection = 0; });
    control.addEventListener("focus", () => {
      focusedDirection = control.matches(":focus-visible") ? controlDirection : 0;
    });
    control.addEventListener("blur", () => { focusedDirection = 0; });
    control.addEventListener("click", () => {
      const distance = controlDirection * carousel.clientWidth * behavior.clickScrollFraction;
      if (reduceMotion.matches) renderPosition(position + distance);
      else clickDistance = distance;
    });
  });

  const activity = () => { lastActivity = performance.now(); };
  carousel.addEventListener("pointerenter", () => { pointerOverCarousel = true; });
  carousel.addEventListener("pointerleave", () => { pointerOverCarousel = false; });
  window.addEventListener("pointermove", activity, { passive: true });
  carousel.addEventListener("wheel", () => { activity(); clickDistance = 0; }, { passive: true });
  carousel.addEventListener("keydown", activity);
  carousel.addEventListener("dragstart", (event) => event.preventDefault());
  carousel.addEventListener("pointerdown", (event) => {
    if (event.button !== 0) return;
    interacting = true;
    clickDistance = 0;
    activity();
    if (event.pointerType === "mouse") {
      dragX = event.clientX;
      dragStartX = event.clientX;
      didDrag = false;
      const captureTarget = event.target.closest(".character-link") || carousel;
      captureTarget.setPointerCapture(event.pointerId);
    }
  });
  carousel.addEventListener("pointermove", (event) => {
    if (dragX === null) return;
    if (Math.abs(event.clientX - dragStartX) > behavior.dragThresholdPx) {
      didDrag = true;
      carousel.classList.add("is-dragging");
    }
    renderPosition(position + dragX - event.clientX);
    dragX = event.clientX;
  });
  const endInteraction = () => {
    interacting = false;
    dragX = null;
    dragStartX = null;
    carousel.classList.remove("is-dragging");
    activity();
    if (didDrag) setTimeout(() => { didDrag = false; }, 0);
  };
  window.addEventListener("pointerup", endInteraction);
  window.addEventListener("pointercancel", endInteraction);
  carousel.addEventListener("lostpointercapture", endInteraction);
  window.addEventListener("blur", () => {
    hoveredDirection = 0;
    focusedDirection = 0;
    endInteraction();
  });
  carousel.addEventListener("scroll", () => {
    // Native swipes, wheel scrolling, and keyboard focus also wrap.
    if (Math.abs(carousel.scrollLeft - lastWritten) > 1) {
      const nativePosition = carousel.scrollLeft;
      if (Math.abs(normalize(nativePosition) - nativePosition) > 1) {
        renderPosition(nativePosition);
      } else {
        position = nativePosition;
        lastWritten = nativePosition;
      }
      activity();
    }
  }, { passive: true });
  new ResizeObserver(measure).observe(carousel);
  measure();
  requestAnimationFrame(animate);
})();
