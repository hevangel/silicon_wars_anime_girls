(() => {
  const dialog = document.querySelector("#style-dialog");
  if (typeof dialog?.showModal !== "function") return;

  const title = dialog.querySelector("#style-dialog-title");
  const content = dialog.querySelector(".style-dialog-content");

  function appendSection(heading, explanation) {
    const section = document.createElement("section");
    const subtitle = document.createElement("h3");
    subtitle.textContent = heading;
    const text = document.createElement("p");
    text.textContent = explanation;
    section.append(subtitle, text);
    content.append(section);
    return section;
  }

  function appendHistory(period, examples, connection) {
    const section = appendSection("Art history connection", period);
    if (connection) {
      const comparison = document.createElement("p");
      comparison.textContent = connection;
      section.append(comparison);
    }

    const links = document.createElement("ul");
    links.className = "style-dialog-sources";
    for (const { label, href } of examples) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      item.append(link);
      links.append(item);
    }
    section.append(links);
  }

  function addDialogButton(label, accessibleTitle, renderContent) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "style-info-button";
    button.setAttribute("aria-label", `About ${accessibleTitle}`);
    button.setAttribute("aria-haspopup", "dialog");
    button.setAttribute("aria-controls", dialog.id);

    const icon = document.createElement("span");
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = "i";
    button.append(icon);
    label.append(button);

    button.addEventListener("click", () => {
      title.textContent = accessibleTitle;
      content.replaceChildren();

      renderContent();

      dialog.showModal();
      dialog.scrollTop = 0;
      dialog.addEventListener("close", () => button.focus({ preventScroll: true }), { once: true });
    });
  }

  function addInfoButton(label, accessibleTitle, sections, history) {
    addDialogButton(label, accessibleTitle, () => {
      for (const [heading, explanation] of sections) appendSection(heading, explanation);
      appendHistory(history.period, history.examples, history.connection);
    });
  }

  for (const entry of document.querySelectorAll("[data-atlas-entry]")) {
    const label = entry.querySelector("dt");
    const details = entry.querySelector("details");
    addDialogButton(label, entry.dataset.atlasEntry, () => {
      content.append(details.querySelector(".atlas-context").cloneNode(true));
    });
    details.hidden = true;
  }

  for (const family of document.querySelectorAll(".style-family")) {
    const guide = styleGuide[family.id];
    if (!guide) continue;

    const heading = document.getElementById(family.getAttribute("aria-labelledby"));
    const styleName = heading.textContent.trim();
    addInfoButton(heading, styleName, [
      ["Background", guide.history],
      ["What makes it distinctive", guide.effect],
      ["When to use it", guide.use],
      ["Why use it", guide.why],
    ], guide);

    const labels = family.querySelectorAll(".style-board-notes dt");
    for (const [index, label] of labels.entries()) {
      const name = label.textContent.split(": ").slice(1).join(": ");
      const variant = guide.variants[index];

      addInfoButton(label, `${name} · ${styleName}`, [
        ["What to look for", variant.detail],
        ["When to use it", variant.when],
        ["Why use it", variant.why],
      ], {
        period: guide.period,
        examples: [guide.examples[variant.example]],
        connection: variant.connection,
      });
    }
  }
})();
