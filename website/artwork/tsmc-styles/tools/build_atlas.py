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
ondisk = {d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d)) and d not in ("contact-sheets", "expansion", "classify")}
assert ondisk == set(STYLES), f"disk/content mismatch: {ondisk ^ set(STYLES)}"
print(f"curriculum OK: {len(LESSONS)} lessons, {len(STYLES)} styles")

# --- classification metadata (Visual Literacy Series supplement) ---
# Every style is multi-tagged across the series' 11 classification categories
# and carries a one-line grammar note plus tendency links into Parts II/III.
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "classifications.json")) as fh:
    CLASSIFICATIONS = json.load(fh)
assert set(CLASSIFICATIONS) == set(STYLES), \
    f"classification mismatch: {set(CLASSIFICATIONS) ^ set(STYLES)}"
CATEGORIES = ["Medium", "Technique", "Artistic movement", "Cultural tradition",
              "Historical period", "Artistic school", "Aesthetic", "Genre",
              "Design system", "Production technology", "Functional application"]
for slug, entry in CLASSIFICATIONS.items():
    assert set(entry["classes"]) <= set(CATEGORIES), f"bad category on {slug}"
print(f"classifications OK: {len(CLASSIFICATIONS)} styles, {len(CATEGORIES)} categories")

os.makedirs(ART, exist_ok=True)


def save_variant(src_path, dst_path, maxdim, quality):
    im = Image.open(src_path).convert("RGB")
    im.thumbnail((maxdim, maxdim), Image.LANCZOS)
    im.save(dst_path, "WEBP", quality=quality)
    return im.size


# --- face-aware square thumbnails ---
# The page shows thumbs in square tiles (object-fit: cover), so a plain
# center crop cuts the character's face whenever she sits off-center.
# faces.json (built by facecrop/detect_all.py in the study dir) records the
# detected face box per source image; the thumb is a square crop positioned
# so the face sits at (50%, 38%) of the tile. No detection -> upper-region
# prior (the café pose keeps her face in the top half).
FACES = {}
_faces_path = os.path.join(SRC, "faces.json")
if os.path.exists(_faces_path):
    with open(_faces_path) as fh:
        FACES = json.load(fh)


def save_thumb(src_path, dst_path, size=440, quality=75):
    im = Image.open(src_path).convert("RGB")
    W, H = im.size
    S = min(W, H)
    rel = os.path.relpath(src_path, SRC)
    face = FACES.get(rel)
    if face:
        cx = face["x"] + face["w"] / 2
        cy = face["y"] + face["h"] / 2
        left = cx - 0.50 * S
        top = cy - 0.38 * S
    elif H > W:  # portrait: face lives in the upper part
        left, top = (W - S) / 2, H * 0.28 - S / 2
    else:  # landscape café pose: figure left of center, face upper area
        left, top = W * 0.38 - S / 2, H * 0.34 - S / 2
    left = int(min(max(left, 0), W - S))
    top = int(min(max(top, 0), H - S))
    im.crop((left, top, left + S, top + S)).resize((size, size), Image.LANCZOS).save(
        dst_path, "WEBP", quality=quality)


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
            save_thumb(f, thumb)
            images.append({"src": f"art/{slug}/{i}.webp", "thumb": f"art/{slug}/t{i}.webp",
                           "w": w, "h": h, "label": f"Variant {i}" if len(files) > 1 else "Study"})
        total_images += len(images)
        cls = CLASSIFICATIONS[slug]
        styles_out.append({"slug": slug, "name": name, "tag": tag, "blurb": blurb,
                           "look": look, "wiki": f"https://en.wikipedia.org/wiki/{wiki}",
                           "classes": cls["classes"], "grammar": cls["grammar"],
                           "links": cls["links"],
                           "images": images})
    lessons_out.append({"id": lesson["id"], "title": lesson["title"],
                        "bigIdea": lesson["bigIdea"], "intro": lesson["intro"],
                        "exercise": lesson["exercise"], "styles": styles_out})

data = {
    "meta": {
        "title": "The TSMC Style Course",
        "subtitle": f"One model. One café. {len(STYLES)} ways to make a picture — all images generated by Muse.",
        "model": "TSMC — 'The Quiet Queenmaker' of Silicon Wars — drawn from her character sheet in every picture.",
        "totalStyles": len(STYLES),
        "totalImages": total_images,
        "totalLessons": len(LESSONS),
        "categories": CATEGORIES,
        "series": "TSMC Visual Literacy Series — Part I: Visual Languages and Dialects",
    },
    "lessons": lessons_out,
}
with open(os.path.join(DST, "artwork.json"), "w") as fh:
    json.dump(data, fh, indent=1, ensure_ascii=False)
print(f"wrote artwork.json: {total_images} images")
