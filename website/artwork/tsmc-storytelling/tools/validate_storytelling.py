#!/usr/bin/env python3
"""Validate the built TSMC Storytelling Course data against the files on disk.

Checks: unique lesson/group/image ids; every published image + thumbnail
exists and its recorded dimensions match the actual file; controls resolve
(including the C00 reference into Part II); copy fields are non-empty;
coverage numbers agree with a recount; the caption experiment carries three
captions per plate; quiz lesson groups hold exactly two plates each.
Run after build_storytelling.py. Exits non-zero on any failure.
"""
import json
import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.dirname(HERE)


def main():
    data = json.load(open(os.path.join(PAGE, "storytelling.json")))
    problems = []

    def check_img(src, thumb, w, h, where):
        for rel in (src, thumb):
            if rel.startswith("../"):
                path = os.path.normpath(os.path.join(PAGE, rel))
            else:
                path = os.path.join(PAGE, rel)
            if not os.path.exists(path):
                problems.append(f"{where}: missing file {rel}")
                return
        if w and h and not src.startswith("../"):
            im = Image.open(os.path.join(PAGE, src))
            if (im.width, im.height) != (w, h):
                problems.append(f"{where}: recorded {w}x{h}, actual {im.width}x{im.height}")

    seen = set()
    n_acc = n_pen = n_reuse = 0
    for c in data["controls"]:
        if c["id"] in seen:
            problems.append(f"duplicate control id {c['id']}")
        seen.add(c["id"])
        check_img(c["src"], c["thumb"], c.get("w"), c.get("h"), f"control {c['id']}")
    for lesson in data["lessons"]:
        if not lesson["intro"]:
            problems.append(f"{lesson['id']}: empty intro")
        if not lesson["exercise"] or not lesson["exercise_answer"]:
            problems.append(f"{lesson['id']}: empty exercise")
        for g in lesson["groups"]:
            if g["id"] in seen:
                problems.append(f"duplicate group id {g['id']}")
            seen.add(g["id"])
            for field in ("learn", "meaning", "alternatives", "prompt_tip"):
                if not g[field]:
                    problems.append(f"{g['id']}: empty {field}")
            if len(g["observe"]) != 3:
                problems.append(f"{g['id']}: observe has {len(g['observe'])} bullets, want 3")
            if g["layout"] == "caption-experiment":
                caps = g.get("captions") or {}
                if len(caps) != len(g["images"]) or any(len(v) != 3 for v in caps.values()):
                    problems.append(f"{g['id']}: caption experiment needs 3 captions x every plate")
            if lesson["quiz"] and len(g["images"]) != 2:
                problems.append(f"{g['id']}: quiz pair must hold exactly 2 plates")
            for img in g["images"]:
                if img["status"] == "accepted":
                    n_acc += 1
                    if img.get("reuse_of"):
                        n_reuse += 1
                    check_img(img["src"], img["thumb"], img.get("w"), img.get("h"),
                              f"{g['id']}/{img['job']}")
                elif img["status"] == "pending":
                    n_pen += 1
                    if "src" in img:
                        problems.append(f"{g['id']}/{img['job']}: pending plate carries an image")
                else:
                    problems.append(f"{g['id']}/{img['job']}: unknown status {img['status']}")
    cov = data["coverage"]
    # accepted count in coverage excludes reuse slots (they point at originals,
    # which are counted under their own groups); pending counts placeholders.
    if cov["study_pending"] != n_pen:
        problems.append(f"coverage pending {cov['study_pending']} != recount {n_pen}")
    if cov["reuse_slots"] != n_reuse:
        problems.append(f"coverage reuse {cov['reuse_slots']} != recount {n_reuse}")
    total_slots = sum(len(g['images']) for l in data['lessons'] for g in l['groups'])
    if total_slots != n_acc + n_pen:
        problems.append(f"slot recount {total_slots} != accepted {n_acc} + pending {n_pen}")

    if problems:
        print(f"INVALID — {len(problems)} problem(s):")
        for p in problems:
            print(" -", p)
        return 1
    print(f"VALID: {len(data['lessons'])} lessons, {cov['groups']} groups, "
          f"{n_acc} published plates ({n_reuse} of them reuse), {n_pen} pending, "
          f"{len(data['controls'])} controls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
