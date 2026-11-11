const reader = document.querySelector(".reader");
const title = document.querySelector("#comic-title");
const picker = document.querySelector("#comic-picker");
const previous = document.querySelector("#previous");
const next = document.querySelector("#next");
const fullSize = document.querySelector("#full-size");
const comicImage = document.querySelector("#comic-image");
const caption = document.querySelector("#variant-caption");
const gallery = document.querySelector("#variant-list");
const referencePanel = document.querySelector(".reference-panel");
const references = document.querySelector("#reference-list");
const noReferences = document.querySelector("#no-references");

function route(comic, variant = comic.defaultVariant) {
  return `#${encodeURIComponent(comic.id)}/${encodeURIComponent(variant)}`;
}

function comicLink(link, comic) {
  if (comic) {
    link.href = route(comic);
    link.removeAttribute("aria-disabled");
  } else {
    link.removeAttribute("href");
    link.setAttribute("aria-disabled", "true");
  }
}

function artworkLink({ href, image, label, alt = "", className, detail }) {
  const item = document.createElement("li");
  const link = document.createElement("a");
  const preview = document.createElement("img");
  const name = document.createElement("span");
  link.href = href;
  link.className = className;
  preview.src = image;
  preview.alt = alt;
  preview.loading = "lazy";
  name.textContent = label;
  link.append(preview, name);
  if (detail) {
    const text = document.createElement("small");
    text.textContent = detail;
    link.append(text);
  }
  item.append(link);
  return item;
}

function initialize({ meta, paths, copy, defaultComic, models, comics }) {
  const comicRoutes = new Map(comics.map((comic, index) => [route(comic).split("/")[0], index]));
  const defaultIndex = comics.findIndex((comic) => comic.id === defaultComic);
  let activeComic;
  document.documentElement.lang = meta.lang;
  document.querySelector('meta[name="theme-color"]').content = meta.themeColor;
  document.querySelector('meta[name="description"]').content = meta.description;
  document.querySelectorAll("[data-copy]").forEach((node) => {
    node.textContent = copy[node.dataset.copy];
  });
  document.querySelector("#comics-home").href = route(comics[defaultIndex]);
  document.querySelector("#character-archive").href = paths.characterArchive;
  document.querySelector("#comic-navigation").setAttribute("aria-label", copy.navigation);

  for (const comic of comics) {
    picker.add(new Option(comic.title, route(comic)));
  }
  picker.addEventListener("change", () => { location.hash = picker.value; });

  function render() {
    const [comicHash] = location.hash.split("/");
    const index = comicRoutes.get(comicHash) ?? defaultIndex;
    const comic = comics[index];
    const variant = comic.variants.find((entry) => route(comic, entry.id) === location.hash)
      ?? comic.variants.find((entry) => entry.id === comic.defaultVariant);
    const comicChanged = activeComic !== comic;
    const focusedVariant = gallery.contains(document.activeElement);
    activeComic = comic;

    document.title = meta.titleTemplate.replace("{comic}", comic.title);
    title.textContent = comic.title;
    picker.value = route(comic);
    comicLink(previous, comics[index - 1]);
    comicLink(next, comics[index + 1]);
    const imagePath = paths.art + variant.image;
    fullSize.href = imagePath;
    fullSize.setAttribute("aria-label", copy.fullSize.replace("{comic}", comic.title));
    comicImage.width = variant.width;
    comicImage.height = variant.height;
    comicImage.alt = variant.alt;
    comicImage.src = imagePath;
    caption.textContent = copy.caption
      .replace("{model}", models[variant.model])
      .replace("{version}", variant.label);

    gallery.replaceChildren(...comic.variants.map((entry) => {
      const item = artworkLink({
        href: route(comic, entry.id),
        image: paths.art + (entry.thumbnail ?? entry.image),
        label: entry.label,
        detail: models[entry.model],
        className: "variant-card"
      });
      if (entry === variant) item.firstElementChild.setAttribute("aria-current", "true");
      return item;
    }));

    if (comicChanged) referencePanel.open = false;
    references.replaceChildren(...variant.references.map((reference) => artworkLink({
      href: paths.references + reference.path,
      image: paths.references + reference.path,
      label: reference.label,
      className: "reference-card"
    })));
    noReferences.hidden = variant.references.length > 0;

    reader.hidden = false;
    if (focusedVariant) gallery.querySelector('[aria-current="true"]').focus({ preventScroll: true });
  }

  render();
  window.addEventListener("hashchange", render);
  document.querySelector("#comic-navigation").addEventListener("click", (event) => {
    if (event.target.matches("a[href]") && !event.ctrlKey && !event.metaKey && !event.shiftKey && !event.altKey) {
      title.focus({ preventScroll: true });
    }
  });
}

async function start() {
  try {
    const response = await fetch("comics.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    initialize(await response.json());
  } catch (error) {
    console.error("Could not initialize the comics reader", error);
    document.querySelector(".load-error").hidden = false;
  }
}

start();
