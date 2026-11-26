(() => {
  const form = document.querySelector(".catalog-search");
  const query = document.querySelector("#catalog-query");
  const status = document.querySelector("#catalog-results");
  const results = document.querySelector("#catalog-matches");
  const normalize = value => value.normalize("NFD").replace(/\p{Mark}/gu, "").toLowerCase()
    .replace(/[’']/g, "").replace(/[^\p{Letter}\p{Number}]+/gu, " ").trim();

  const studies = [...document.querySelectorAll(".catalog-home .style-family:not(.atlas-board)")].map(study => {
    const title = document.getElementById(study.getAttribute("aria-labelledby")).firstChild.textContent.trim();
    const home = study.closest(".catalog-home");
    const guide = styleGuide[study.id];
    return {
      id: study.id,
      title,
      home: home.querySelector("h3").textContent,
      titleKey: normalize(title),
      searchText: normalize([study.id, study.textContent, study.dataset.tags, guide?.period,
        guide?.history, guide?.effect, guide?.use, home.querySelector("h3").textContent].join(" ")),
    };
  });

  for (const entry of document.querySelectorAll("[data-atlas-entry], [data-search-alias]")) {
    const title = entry.dataset.atlasEntry || entry.dataset.searchAlias;
    const board = entry.closest(".style-family");
    const home = document.getElementById(board.getAttribute("aria-labelledby")).firstChild.textContent.trim();
    studies.push({
      id: entry.id,
      title,
      home,
      titleKey: normalize(title),
      searchText: normalize([title, home, entry.dataset.tags, entry.textContent].join(" ")),
    });
  }

  function revealStudy() {
    const target = document.getElementById(location.hash.slice(1));
    const collection = target?.closest("details.atlas-collection");
    if (collection && !collection.open) {
      collection.open = true;
      target.scrollIntoView();
    }
  }

  window.addEventListener("hashchange", revealStudy);
  revealStudy();

  form.hidden = false;
  query.addEventListener("input", () => {
    const value = normalize(query.value);
    results.replaceChildren();
    if (!value) {
      status.textContent = "";
      return;
    }

    const terms = value.split(" ");
    const matches = studies.filter(study => terms.every(term => study.searchText.includes(term)))
      .sort((a, b) => Number(b.titleKey.includes(value)) - Number(a.titleKey.includes(value)));
    status.textContent = matches.length ? `${matches.length} matching ${matches.length === 1 ? "study" : "studies"}.`
      : "No matching studies.";
    for (const study of matches) {
      const row = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#${study.id}`;
      link.textContent = study.title;
      row.append(link, ` · ${study.home}`);
      results.append(row);
    }
  });
})();
