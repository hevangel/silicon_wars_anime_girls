(() => {
  const form = document.querySelector(".catalog-search");
  const query = document.querySelector("#catalog-query");
  const status = document.querySelector("#catalog-results");
  const results = document.querySelector("#catalog-matches");
  const normalize = value => value.normalize("NFD").replace(/\p{Mark}/gu, "").toLowerCase()
    .replace(/[’']/g, "").replace(/[^\p{Letter}\p{Number}]+/gu, " ").trim();

  const studies = [...document.querySelectorAll(".catalog-home .style-family")].map(study => {
    const title = document.getElementById(study.getAttribute("aria-labelledby")).textContent.trim();
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
