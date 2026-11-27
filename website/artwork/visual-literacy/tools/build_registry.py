#!/usr/bin/env python3
"""Build the Visual Literacy Series concept registry (concepts.json).

Harvests the structured cross-references the three courses already carry:
- Part I (tsmc-styles/tools/classifications.json): each style's tendency
  links — the decisions it commonly uses and the meanings it can carry.
- Part II (tsmc-seeing/seeing.json): the decision cards themselves; a
  concept earns a Part II reference when a card's name/subtitle matches it.
- Part III (tsmc-storytelling/storytelling.json): each group's concept
  list — plain names are concepts taught in that group; "Part I — X" /
  "Part II — X" strings are cross-references that also register X.

Relationships are tendencies, never universals ("red means anger" is the
misconception Part III exists to correct), and the page phrases them that
way. A concept enters the registry when at least two references support it.
Stack layers follow the series' Visual Language Stack.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.dirname(HERE)
ARTWORK = os.path.dirname(PAGE)
sys.path.insert(0, os.path.join(ARTWORK, "tsmc-styles", "tools"))
from content import LESSONS as STYLE_LESSONS  # noqa: E402

LAYER_KEYWORDS = [
    (7, "Pragmatics", ["audience", "caption", "context", "satire", "persuasion",
                       "advertising", "editorial", "intended", "perceived"]),
    (5, "Narrative syntax", ["sequence", "panel", "ellipsis", "narrative", "genre",
                             "story", "montage", "flashback"]),
    (6, "Semantics", ["symbol", "metaphor", "mood", "atmosphere", "emotion", "meaning",
                      "irony", "allegory", "drama", "nostalgia", "suspense", "loneliness",
                      "authority", "hope", "grief", "joy", "fear", "intimacy", "reverence"]),
    (4, "Spatial syntax", ["composition", "framing", "balance", "thirds", "camera",
                           "angle", "viewpoint", "distance", "proxemics", "depth",
                           "placement", "scale", "cropping"]),
    (3, "Representation", ["perspective", "proportion", "realism", "stylization",
                           "anatomy", "foreshortening", "modeling", "rendering"]),
    (2, "Visual primitives", ["line", "value", "color", "colour", "light", "shadow",
                              "shape", "texture", "contrast", "palette", "tone"]),
]
MEANING_WORDS = {
    "drama", "authority", "nostalgia", "suspense", "loneliness", "hope", "satire",
    "unease", "reverence", "formality", "transience", "tranquility", "alienation",
    "spectacle", "intimacy", "grief", "joy", "fear", "playfulness", "optimism",
    "protection", "ancestry", "mystery", "confidence", "arrogance", "calmness",
    "vulnerability", "weakness", "professionalism", "coldness", "confusion",
    "intimidation", "indifference", "sadness",
}


# Near-duplicate phrasings harvested from three independently written data
# sets are merged onto one canonical concept.
ALIASES = {
    "dramatic directional lighting": "directional lighting",
    "directional light": "directional lighting",
    "light direction": "directional lighting",
    "dramatic light": "directional lighting",
    "strong value contrast": "value contrast",
    "value and contrast": "value contrast",
    "light side and shadow side": "light and shadow",
    "atmosphere and light": "atmosphere",
    "atmosphere and emotional context": "atmosphere",
    "light and time of day": "time of day",
    "soft diffused lighting": "soft light",
    "soft lighting": "soft light",
    "flat color": "flat colour",
    "limited palette": "limited palette",
    "props and set dressing": "props",
    "basic emotional expressions": "emotional expressions",
    "emotional intensity": "intensity",
}


def norm(text):
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower()).strip()


def layer_for(name):
    n = norm(name)
    for layer, title, words in LAYER_KEYWORDS:
        if any(w in n for w in words):
            return layer, title
    if any(w in n for w in MEANING_WORDS):
        return 6, "Semantics"
    return 6, "Semantics"


def slugify(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


def main():
    concepts = {}

    def add(name, ref):
        name = name.strip()
        if not name:
            return
        name = ALIASES.get(norm(name), name)
        key = norm(name)
        c = concepts.setdefault(key, {"id": slugify(name), "name": name, "refs": []})
        if ref not in c["refs"]:
            c["refs"].append(ref)

    # ---- Part I tendencies -------------------------------------------------
    cls = json.load(open(os.path.join(ARTWORK, "tsmc-styles", "tools", "classifications.json")))
    styles_data = json.load(open(os.path.join(ARTWORK, "tsmc-styles", "artwork.json")))
    style_name = {s["slug"]: s["name"] for l in styles_data["lessons"] for s in l["styles"]}
    lesson_of = {s: l["id"] for l in STYLE_LESSONS for s in l["styles"]}
    for slug, entry in cls.items():
        for link in entry["links"]:
            add(link, {"course": "Part I", "kind": "tendency",
                       "label": style_name[slug],
                       "href": f"../tsmc-styles/#lesson-{lesson_of[slug]}"})

    # ---- Part III group concepts -------------------------------------------
    story = json.load(open(os.path.join(ARTWORK, "tsmc-storytelling", "storytelling.json")))
    for lesson in story["lessons"]:
        for g in lesson["groups"]:
            for raw in g["concepts"]:
                m = re.match(r"^Part (I|II|III)\s*[—–-]\s*(.+)$", raw)
                name = m.group(2) if m else raw
                add(name, {"course": "Part III", "kind": "taught",
                           "label": f"{lesson['title'].split('—')[0].strip()} · {g['title']}",
                           "href": f"../tsmc-storytelling/#group-{g['id']}"})

    # ---- Part II card matching ----------------------------------------------
    seeing = json.load(open(os.path.join(ARTWORK, "tsmc-seeing", "seeing.json")))
    cards = []
    for les in seeing["lessons"]:
        for cd in les["cards"]:
            cards.append((norm(cd["name"] + " " + cd["subtitle"] + " " + cd["explanation"]),
                          les, cd))
    for c in concepts.values():
        tokens = [t for t in norm(c["name"]).split() if len(t) > 2]
        if not tokens:
            continue
        best, best_score = None, 0
        for text, les, cd in cards:
            score = sum(1 for t in tokens if t in text) / len(tokens)
            if score > best_score:
                best, best_score = (les, cd), score
        if best and best_score >= 0.5:
            les, cd = best
            add(c["name"], {"course": "Part II", "kind": "decision",
                            "label": f"Lesson {les['n']} · {cd['name']}",
                            "href": f"../tsmc-seeing/#lesson-{les['id']}"})

    out = []
    for c in concepts.values():
        courses = {r["course"] for r in c["refs"]}
        if len(courses) < 2 and len(c["refs"]) < 4:
            continue
        layer, layer_title = layer_for(c["name"])
        ctype = ("language" if layer == 1 else "decision" if layer <= 4
                 else "narrative" if layer == 5 else "meaning" if layer == 6 else "context")
        out.append({"id": c["id"], "name": c["name"], "type": ctype,
                    "layer": layer, "layer_title": layer_title, "refs": c["refs"]})
    out.sort(key=lambda c: (c["layer"], c["name"].lower()))
    data = {
        "series": "TSMC Visual Literacy Series",
        "stack": [
            {"layer": 1, "title": "Artistic languages", "parts": "Part I"},
            {"layer": 2, "title": "Visual primitives", "parts": "Part II"},
            {"layer": 3, "title": "Representation", "parts": "Part II"},
            {"layer": 4, "title": "Spatial syntax", "parts": "Part II"},
            {"layer": 5, "title": "Narrative syntax", "parts": "Part III"},
            {"layer": 6, "title": "Semantics", "parts": "Part III"},
            {"layer": 7, "title": "Pragmatics", "parts": "Part III"},
        ],
        "concepts": out,
    }
    with open(os.path.join(PAGE, "concepts.json"), "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"registry: {len(out)} concepts "
          f"({sum(1 for c in out if len({r['course'] for r in c['refs']}) >= 2)} cross-course)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
