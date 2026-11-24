#!/usr/bin/env python3
"""Build the TSMC Style Course site data + images into website/artwork/tsmc-styles/."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import LESSONS, STYLES
from PIL import Image

SRC = os.environ.get("TSMC_STUDY_DIR", os.path.expanduser("~/workspace/tsmc_style_study"))
DST = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(DST, "art")

# --- validate the curriculum covers every style exactly once ---
assigned = [s for lesson in LESSONS for s in lesson["styles"]]
assert len(assigned) == len(set(assigned)), "duplicate style in lessons"
missing = [s for s in assigned if s not in STYLES]
assert not missing, f"lesson styles without content: {missing}"
unassigned = [s for s in STYLES if s not in assigned]
assert not unassigned, f"styles not in any lesson: {unassigned}"
ondisk = {d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d)) and d != "contact-sheets"}
assert ondisk == set(STYLES), f"disk/content mismatch: {ondisk ^ set(STYLES)}"
print(f"curriculum OK: {len(LESSONS)} lessons, {len(STYLES)} styles")

os.makedirs(ART, exist_ok=True)


def save_variant(src_path, dst_path, maxdim, quality):
    im = Image.open(src_path).convert("RGB")
    im.thumbnail((maxdim, maxdim), Image.LANCZOS)
    im.save(dst_path, "WEBP", quality=quality)
    return im.size


lessons_out = []
total_images = 0
for lesson in LESSONS:
    styles_out = []
    for slug in lesson["styles"]:
        name, tag, blurb, look, wiki = STYLES[slug]
        src_dir = os.path.join(SRC, slug)
        files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if f.endswith(".webp")]
        files.sort(key=os.path.getmtime)
        assert files, f"no images for {slug}"
        dst_dir = os.path.join(ART, slug)
        os.makedirs(dst_dir, exist_ok=True)
        images = []
        for i, f in enumerate(files, 1):
            full = os.path.join(dst_dir, f"{i}.webp")
            thumb = os.path.join(dst_dir, f"t{i}.webp")
            w, h = save_variant(f, full, 1100, 80)
            save_variant(f, thumb, 440, 75)
            images.append({"src": f"art/{slug}/{i}.webp", "thumb": f"art/{slug}/t{i}.webp",
                           "w": w, "h": h, "label": f"Variant {i}" if len(files) > 1 else "Study"})
        total_images += len(images)
        styles_out.append({"slug": slug, "name": name, "tag": tag, "blurb": blurb,
                           "look": look, "wiki": f"https://en.wikipedia.org/wiki/{wiki}",
                           "images": images})
    lessons_out.append({"id": lesson["id"], "title": lesson["title"],
                        "bigIdea": lesson["bigIdea"], "intro": lesson["intro"],
                        "exercise": lesson["exercise"], "styles": styles_out})

data = {
    "meta": {
        "title": "The TSMC Style Course",
        "subtitle": "One model. One café. 105 ways to make a picture.",
        "model": "TSMC — 'The Quiet Queenmaker' of Silicon Wars — drawn from her character sheet in every picture.",
        "totalStyles": len(STYLES),
        "totalImages": total_images,
        "totalLessons": len(LESSONS),
    },
    "lessons": lessons_out,
}
with open(os.path.join(DST, "artwork.json"), "w") as fh:
    json.dump(data, fh, indent=1, ensure_ascii=False)
print(f"wrote artwork.json: {total_images} images")
