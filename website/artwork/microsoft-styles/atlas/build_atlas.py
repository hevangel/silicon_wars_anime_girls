"""Rebuild the static comparison galleries in the adjacent index.html."""

import json
import re
from collections import defaultdict
from html import escape
from pathlib import Path
from urllib.parse import urlsplit


ATLAS = Path(__file__).resolve().parent
INDEX = ATLAS.parent / "index.html"
POSITIONS = {
    1: ["Study"],
    2: ["Left", "Right"],
    3: ["Left", "Center", "Right"],
    4: ["Top left", "Top right", "Bottom left", "Bottom right"],
}


def read_record(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def render_example(entry_id, position, requested, variant):
    name = escape(variant["name"])
    source = variant["source"]
    period = f'<p>{escape(variant["period"])}</p>' if variant.get("period") else ""
    if urlsplit(source["href"]).scheme not in ("http", "https"):
        raise ValueError(f"Invalid historical source for {name}")
    return f"""<div id="{entry_id}" data-atlas-entry="{name}" data-tags="{escape(requested)}">
  <dt>{position}: {name}</dt>
  <dd>{escape(variant["look"])}</dd>
  <dd><details><summary>History and use</summary>
    <div class="atlas-context">
      <section><h3>Art history connection</h3>{period}<p>{escape(variant["history"])}</p>
        <p><a href="{escape(source["href"])}">{escape(source["label"])}</a></p></section>
      <section><h3>When to use it</h3><p>{escape(variant["when"])}</p></section>
      <section><h3>Why use it</h3><p>{escape(variant["why"])}</p></section>
    </div>
  </details></dd>
</div>"""


def render_board(plan):
    board_id = plan["id"]
    board = read_record(ATLAS / f"{board_id}.json")
    entries = board["variants"]
    positions = board.get("positions", POSITIONS[len(entries)])
    image = board["image"]
    if Path(image).name != image or not (ATLAS / image).is_file():
        raise ValueError(f"Missing board image for {board_id}: {image}")
    notes = "\n".join(
        render_example(f"atlas-study-{number}", escape(position), term, variant)
        for number, position, term, variant in zip(
            plan["indices"], positions, plan["terms"], entries, strict=True
        )
    )
    title = escape(plan["title"])
    layout = {1: " atlas-single", 3: " atlas-three"}.get(len(entries), "")
    return f"""<section class="style-family atlas-board{layout}" id="{board_id}" aria-labelledby="{board_id}-title">
  <h4 id="{board_id}-title">{title}</h4>
  <p class="style-intro">{escape(board["intro"])}</p>
  <figure class="style-board">
    <a href="atlas/{escape(image)}" aria-label="Open full-size comparison: {title}">
      <img class="piece-image" src="atlas/{escape(image)}" width="{int(board["width"])}" height="{int(board["height"])}" loading="lazy" decoding="async" alt="{escape(board["alt"])}">
    </a>
  </figure>
  <dl class="style-board-notes">{notes}</dl>
</section>"""


def render_collection(anchor, label, boards):
    links = "\n".join(f'<li><a href="#{b["id"]}">{escape(b["title"])}</a></li>' for b in boards)
    count = sum(len(b["terms"]) for b in boards)
    content = "\n".join(render_board(b) for b in boards)
    return f"""<details class="atlas-collection" id="{anchor}"><summary>{escape(label)} · {count} examples</summary>
<ul class="atlas-contents">{links}</ul>
{content}
</details>"""


def main():
    groups = defaultdict(list)
    for board in read_record(ATLAS / "plan.json"):
        groups[board["home"]].append(board)
    page = INDEX.read_text(encoding="utf-8")
    directory = []
    for home in sorted(groups, key=lambda topic: page.index(f'id="{topic}"')):
        boards = groups[home]
        start = f"<!-- atlas:{home} -->"
        end = f"<!-- /atlas:{home} -->"
        if page.count(start) != 1 or page.count(end) != 1:
            raise ValueError(f"Expected one gallery location for {home}")
        galleries = defaultdict(list)
        for board in boards:
            galleries[board.get("gallery", "Explore related studies")].append(board)
        collections = []
        for index, (label, group) in enumerate(galleries.items(), 1):
            anchor = f"gallery-{home}-{index}"
            collections.append(render_collection(anchor, label, group))
            if len(galleries) == 1:
                label = re.search(fr'<h3 id="{home}-title">([^<]+)</h3>', page)[1]
            directory.append(f'<li><a href="#{anchor}">{escape(label)}</a></li>')
        gallery = "\n".join(collections)
        page = re.sub(f"{start}.*?{end}", lambda _: f"{start}\n{gallery}\n{end}", page, flags=re.S)
    listing = "\n".join(directory)
    page = re.sub("<!-- atlas-directory -->.*?<!-- /atlas-directory -->", lambda _:
        f'<!-- atlas-directory -->\n<details class="atlas-directory"><summary>Browse comparison galleries</summary>'
        f'\n<ul class="atlas-contents">{listing}</ul></details>\n<!-- /atlas-directory -->', page, flags=re.S)
    INDEX.write_text(page, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
