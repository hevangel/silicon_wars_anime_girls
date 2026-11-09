// Silicon Wars character archive.
// All copy, ordering, artwork availability, and tuning values live in data/*.json.
(async () => {
  const SITE_URL = "data/site.json";

  const fetchJson = async (url) => {
    const response = await fetch(url, { cache: "no-cache" });
    if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
    return response.json();
  };

  const lookup = (object, path) => path.split(".").reduce((value, key) => value?.[key], object);
  const fill = (template, values) => template.replace(/\{(\w+)\}/g, (_, key) => values[key] ?? "");

  // Inline the supplied artwork so its outline can share the circuit's neon color.
  // Keep the source SVG intact; remove its white artboard only in this display copy.
  const loadLogo = async () => {
    const image = document.querySelector("[data-logo] .title-art");
    const response = await fetch(image.getAttribute("src"));
    if (!response.ok) throw new Error(`Logo: HTTP ${response.status}`);
    const documentSvg = new DOMParser().parseFromString(await response.text(), "image/svg+xml");
    if (documentSvg.querySelector("parsererror") || documentSvg.documentElement.localName !== "svg") {
      throw new Error("Invalid logo SVG");
    }
    const logo = document.importNode(documentSvg.documentElement, true);
    logo.querySelector(':scope > rect[width="100%"][height="100%"]')?.remove();
    logo.setAttribute("class", "title-art");
    logo.setAttribute("aria-hidden", "true");
    logo.setAttribute("focusable", "false");
    image.replaceWith(logo);
  };
  loadLogo().catch((error) => console.warn("Using the static logo:", error));

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


  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const galleryView = document.querySelector("#gallery-view");
  const profileView = document.querySelector("#character-profile");
  const assetArchive = document.querySelector("#asset-archive");
  const assetList = document.querySelector(".asset-list");
  const assetArchiveTitle = document.querySelector(".asset-archive-title");
  const assetArchiveCount = document.querySelector(".asset-archive-count");
  const profileCardImage = document.querySelector(".profile-card-image");
  const profileName = document.querySelector(".profile-card-caption .character-name");
  const profileTitle = document.querySelector(".profile-card-caption .character-title");
  const profileDescription = document.querySelector(".portfolio-description");
  const profileAbility = document.querySelector(".profile-ability");
  const profileAbilityName = profileAbility.querySelector("span");
  const profileKicker = document.querySelector(".profile-kicker");
  const characterBySlug = new Map(characters.map((character) => [character.slug, character]));
  const assetTypeById = new Map(assetTypes.map((type) => [type.id, type]));
  const breadcrumb = document.querySelector(".breadcrumb-current");
  const menu = document.querySelector("#site-menu");
  const menuToggle = document.querySelector(".menu-toggle");
  const viewer = document.querySelector(".art-viewer");
  const viewerImage = document.querySelector(".viewer-image");
  let selectedGroup = "";
  let selectedSort = site.sorting.default;
  let viewerItems = [];
  let viewerIndex = 0;

  // Gallery cards -------------------------------------------------------------
  const carousel = document.querySelector(".carousel");
  const track = document.querySelector(".track");

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

  // Shared navigation stays available in every view.
  const closeMenu = () => {
    menu.hidden = true;
    menuToggle.setAttribute("aria-expanded", "false");
  };
  [{ href: "#characters", label: site.navigation.homeLabel },
    ...assetTypes.map((type) => ({ href: `#assets/${type.id}`, label: type.archiveTitle }))
  ].forEach(({ href, label }) => {
    const link = document.createElement("a");
    link.href = href;
    link.textContent = label;
    menu.append(link);
  });
  menuToggle.addEventListener("click", () => {
    menu.hidden = !menu.hidden;
    menuToggle.setAttribute("aria-expanded", String(!menu.hidden));
  });
  document.addEventListener("click", (event) => {
    if (!menu.contains(event.target) && !menuToggle.contains(event.target)) closeMenu();
  });
  menu.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !menu.hidden) {
      closeMenu();
      menuToggle.focus();
    }
  });

  const setPage = (view, title = "") => {
    document.body.dataset.view = view;
    breadcrumb.textContent = title;
    breadcrumb.hidden = !title;
    menu.querySelectorAll("a").forEach((link) => {
      const current = link.hash === location.hash || (view === "home" && link.hash === "#characters");
      if (current) link.setAttribute("aria-current", "page");
      else link.removeAttribute("aria-current");
    });
    closeMenu();
  };
  const scrollToTop = () =>
    window.scrollTo({ top: 0, behavior: reduceMotion.matches ? "auto" : "smooth" });

  // The viewer fills the viewport; native dialog handles focus and Escape.
  const updateViewer = () => {
    const { character, path, alt } = viewerItems[viewerIndex];
    viewerImage.src = assetUrl(path);
    viewerImage.alt = alt;
    document.querySelector("#viewer-title").textContent = `${character.name} · ${viewerIndex + 1} / ${viewerItems.length}`;
    document.querySelector(".viewer-profile").href = `#character/${character.slug}`;
    document.querySelector(".viewer-previous").disabled = viewerItems.length < 2;
    document.querySelector(".viewer-next").disabled = viewerItems.length < 2;
  };
  const openViewer = (items, index) => {
    viewerItems = items;
    viewerIndex = index;
    updateViewer();
    viewer.showModal();
    document.body.classList.add("viewer-open");
  };
  const moveViewer = (direction) => {
    viewerIndex = (viewerIndex + direction + viewerItems.length) % viewerItems.length;
    updateViewer();
  };
  document.querySelector(".viewer-close").addEventListener("click", () => viewer.close());
  document.querySelector(".viewer-previous").addEventListener("click", () => moveViewer(-1));
  document.querySelector(".viewer-next").addEventListener("click", () => moveViewer(1));
  viewer.addEventListener("close", () => document.body.classList.remove("viewer-open"));
  viewer.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      event.preventDefault();
      moveViewer(event.key === "ArrowLeft" ? -1 : 1);
    }
  });
  document.querySelector(".viewer-profile").addEventListener("click", () => viewer.close());

  // Image-only grids: names already appear in the artwork.
  const compareCharacters = (a, b) => {
    const curated = (a.sort?.curatedOrder ?? characters.indexOf(a)) - (b.sort?.curatedOrder ?? characters.indexOf(b));
    if (selectedSort === "name") return a.name.localeCompare(b.name, site.meta.lang) || curated;
    const field = selectedSort === "founded" ? "foundedYear" : "marketCapUsd";
    if (selectedSort === "founded" || selectedSort === "marketCap") {
      const left = a.sort?.[field];
      const right = b.sort?.[field];
      const hasLeft = Number.isFinite(left) && left > 0;
      const hasRight = Number.isFinite(right) && right > 0;
      if (hasLeft !== hasRight) return hasLeft ? -1 : 1;
      if (hasLeft && left !== right) return selectedSort === "marketCap" ? right - left : left - right;
    }
    return curated;
  };
  const filteredCharacters = (typeId) => characters
    .filter((character) => !selectedGroup || character.groups?.includes(selectedGroup))
    .sort(typeId === "reference_card" ? compareCharacters : (a, b) =>
      (a.sort?.curatedOrder ?? characters.indexOf(a)) - (b.sort?.curatedOrder ?? characters.indexOf(b)));
  const makeItems = (typeId) => filteredCharacters(typeId).flatMap((character) => {
    const path = typeId === "reference_card" ? character.referenceCard : character.artwork?.[typeId];
    const type = assetTypeById.get(typeId);
    return path ? [{ character, path, alt: `${character.name} — ${type.altLabel}` }] : [];
  });
  const gridStates = new WeakMap();
  const renderGrid = (container, items) => {
    let state = gridStates.get(container);
    if (!state) {
      state = { cards: new Map(), items: [] };
      gridStates.set(container, state);
    }
    state.items = items;
    const nodes = items.map((item, index) => {
      const key = `${item.character.slug}:${item.path}`;
      if (state.cards.has(key)) return state.cards.get(key);
      const button = document.createElement("button");
      button.type = "button";
      button.className = "art-card";
      button.dataset.slug = item.character.slug;
      button.setAttribute("aria-label", fill(site.viewer.expandTemplate, { artwork: item.alt }));
      const image = document.createElement("img");
      image.src = assetUrl(item.path);
      image.alt = item.alt;
      image.decoding = "async";
      if (item.path === item.character.referenceCard) {
        // All reference cards are 2:3; reserve space before lazy images load.
        image.width = 1024;
        image.height = 1536;
      }
      if (index < behavior.eagerLoadCount) image.fetchPriority = "high";
      else image.loading = "lazy";
      button.append(image);
      button.addEventListener("click", () => {
        const currentIndex = state.items.findIndex((current) =>
          current.character.slug === item.character.slug && current.path === item.path);
        if (currentIndex !== -1) openViewer(state.items, currentIndex);
      });
      state.cards.set(key, button);
      return button;
    });
    // Move existing cards instead of recreating and decoding their images.
    const visible = new Set(nodes);
    [...container.children].forEach((node) => {
      if (!visible.has(node)) node.remove();
    });
    nodes.forEach((node, index) => {
      if (container.children[index] !== node) {
        container.insertBefore(node, container.children[index] ?? null);
      }
    });
  };

  const filters = [...document.querySelectorAll(".group-filter")];
  const sortSelect = document.querySelector(".sort-select");
  site.sorting.options.forEach(({ value, label }) => sortSelect.append(new Option(label, value)));
  sortSelect.value = selectedSort;
  sortSelect.addEventListener("change", () => {
    selectedSort = sortSelect.value;
    renderRoute(false);
  });
  const groups = [...new Set(characters.flatMap((character) => character.groups ?? []))];
  filters.forEach((select) => {
    select.append(new Option(site.gallery.allGroupsLabel, ""));
    groups.forEach((group) => select.append(new Option(group, group)));
    select.addEventListener("change", () => {
      selectedGroup = select.value;
      filters.forEach((filter) => { filter.value = selectedGroup; });
      renderRoute(false);
    });
  });

  const showGallery = () => {
    profileView.hidden = true;
    assetArchive.hidden = true;
    galleryView.hidden = false;
    document.querySelector(".card-count").textContent = fill(site.gallery.countTemplate, { count: characters.length });
    document.title = site.meta.title;
    setPage("home");
  };
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
    setPage("profile", character.name);
  };


  const renderAssetArchive = (typeId) => {
    const type = assetTypeById.get(typeId);
    if (!type) return false;
    sortSelect.closest("label").hidden = typeId !== "reference_card";
    document.querySelector(".sorting-note").hidden = typeId !== "reference_card" || selectedSort !== "marketCap";
    const items = makeItems(typeId);
    assetArchiveTitle.textContent = type.archiveTitle;
    assetArchiveCount.textContent = fill(site.assetArchive.countTemplate, { count: items.length });
    renderGrid(assetList, items);
    galleryView.hidden = true;
    profileView.hidden = true;
    assetArchive.hidden = false;
    document.title = fill(site.meta.archiveTitleTemplate, { title: type.archiveTitle });
    setPage("archive", type.archiveTitle);
    return true;
  };

  const controls = [...document.querySelectorAll(".carousel-control")];
  // Endless carousel ----------------------------------------------------------
  track.addEventListener("click", (event) => {
    if (didDrag) { event.preventDefault(); event.stopPropagation(); didDrag = false; }
  });
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
    if (previousTime && !document.hidden && !galleryView.hidden) {
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

  const renderRoute = (resetScroll = true) => {
    if (viewer.open) viewer.close();
    const match = location.hash.match(/^#character\/([a-z0-9-]+)$/);
    const assetMatch = location.hash.match(/^#assets\/([a-z_]+)$/);
    if (match) renderProfile(match[1]);
    else if (!assetMatch || !renderAssetArchive(assetMatch[1])) showGallery();
    if (resetScroll) scrollToTop();
  };
  document.querySelector(".profile-back").addEventListener("click", () => { location.hash = "characters"; });
  window.addEventListener("hashchange", () => renderRoute());
  document.querySelectorAll('.brand, .logo-home').forEach((link) => {
    link.addEventListener("click", () => {
      if (!selectedGroup) return;
      selectedGroup = "";
      filters.forEach((filter) => { filter.value = ""; });
      if (location.hash === "#characters") renderRoute();
    });
  });
  renderRoute();
})();
