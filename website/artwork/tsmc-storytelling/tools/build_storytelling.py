#!/usr/bin/env python3
"""Build the TSMC Storytelling Course data + art from the storytelling study.

Reads  $TSMC_STORYTELLING_DIR/manifest.json  (v2.0-supplement: lessons/groups/jobs)
       $TSMC_STORYTELLING_DIR/ledger.json    (the acceptance record)
       $TSMC_STORYTELLING_DIR/copy/copy-*.json (lesson intros, group copy, exercises)
       $TSMC_STORYTELLING_DIR/images/<job-id>.webp  (accepted renders)
       $TSMC_STORYTELLING_DIR/controls/c01..c05.webp (approved controls)
Writes website/artwork/tsmc-storytelling/storytelling.json,
       generation-manifest.json (canonical copy of the study manifest),
       art/controls/c01..c05.webp and art/l<NN>/<group>/<i>.webp + t<i>.webp
       (web copies: full <=1200px wide, thumbs <=480px wide, native aspect).

Acceptance comes from the ledger, never from the manifest alone: a job is
published only when the ledger marks it "accepted". Jobs the ledger marks
"generated" (rendered but not yet accepted) are published as descriptive
pending placeholders with no image, per the production spec. Reuse jobs
point at the original plate's art files instead of duplicating them.
C00 is referenced from Part II (../tsmc-seeing/art/control.webp).
"""
import glob
import json
import os
import shutil
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.dirname(HERE)
SRC = os.environ.get("TSMC_STORYTELLING_DIR",
                     os.path.expanduser("~/workspace/tsmc_storytelling_study"))

MODULES = [
    ("m1", "The face", ["l01", "l02", "l03", "l04", "l05"]),
    ("m2", "The body", ["l06", "l07", "l08"]),
    ("m3", "People together", ["l09", "l10", "l11"]),
    ("m4", "Signs, scenes and symbols", ["l12", "l13", "l14", "l15", "l16"]),
    ("m5", "Stories", ["l17", "l18", "l19", "l20"]),
    ("m6", "Semantic experiments", ["l21", "l22", "l23", "l24", "l25"]),
]
MODULE_OF = {lid: (mid, mtitle) for mid, mtitle, lids in MODULES for lid in lids}

CONTROL_ALT = {
    "C00": "The original café control (Part II): TSMC seated in side profile in a café, "
           "raising a ceramic cup on its saucer, legs crossed, soft daylight from a window on the left.",
    "C01": "Control C01, neutral facial portrait: TSMC front-facing, head and shoulders, "
           "neutral expression, round silver glasses, wafer-die hairpin with wine-red tassel.",
    "C02": "Control C02, neutral standing pose: TSMC full body on a warm-gray studio backdrop, "
           "arms relaxed, pearl ankle boots visible.",
    "C03": "Control C03, two-character café scene: TSMC seated screen-left and ASML seated "
           "screen-right at a café table with cups and a wafer.",
    "C04": "Control C04, narrative staging: TSMC standing left of a café table holding a sealed "
           "cream envelope, cup and protective case on the table, closed door at frame right.",
    "C05": "Control C05, conceptual stage: TSMC standing centered on a plain warm-gray studio "
           "stage, hands relaxed, empty space around her for symbolic objects.",
}


def web_copy(src_path, dst_full, dst_thumb):
    im = Image.open(src_path).convert("RGB")
    dims = {}
    for dst, maxw in ((dst_full, 1200), (dst_thumb, 480)):
        out = im
        if im.width > maxw:
            out = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        out.save(dst, "WEBP", quality=82)
        if dst == dst_full:
            dims = {"w": out.width, "h": out.height}
    return dims


def main():
    man = json.load(open(os.path.join(SRC, "manifest.json")))
    led = json.load(open(os.path.join(SRC, "ledger.json")))
    copy = {"lessons": {}, "groups": {}, "exercises": {}}
    for path in sorted(glob.glob(os.path.join(SRC, "copy", "copy-*.json"))):
        chunk = json.load(open(path))
        for key in copy:
            copy[key].update(chunk.get(key, {}))
    jobs = {j["id"]: j for j in man["jobs"]}
    status = {jid: v["status"] for jid, v in led["jobs"].items()}

    errors = []

    # ---- controls ------------------------------------------------------
    controls = {}
    for c in man["controls"]:
        cid = c["id"]
        if cid == "C00":
            controls[cid] = {"id": cid, "title": c["title"],
                             "src": "../tsmc-seeing/art/control.webp",
                             "thumb": "../tsmc-seeing/art/control.webp",
                             "alt": CONTROL_ALT[cid], "reused_from_part2": True}
            continue
        src_file = os.path.join(SRC, "controls", cid.lower() + ".webp")
        rel = f"art/controls/{cid.lower()}.webp"
        rel_t = f"art/controls/t{cid.lower()}.webp"
        dims = web_copy(src_file, os.path.join(PAGE, rel), os.path.join(PAGE, rel_t))
        controls[cid] = {"id": cid, "title": c["title"], "src": rel, "thumb": rel_t,
                         "alt": CONTROL_ALT[cid], **dims}

    # ---- art paths ------------------------------------------------------
    def art_rel(job):
        """(full, thumb) page-relative paths for a job's own render."""
        lesson = job["lesson"]
        idx = group_images[job["group"]].index(job["id"]) + 1
        return (f"art/{lesson}/{job['group']}/{idx}.webp",
                f"art/{lesson}/{job['group']}/t{idx}.webp")

    group_images = {g["id"]: list(g["images"]) for l in man["lessons"] for g in l["groups"]}

    # ---- lessons / groups ----------------------------------------------
    lessons_out = []
    accepted_jobs = set()
    n_pending = n_reuse_slots = 0
    for lesson in man["lessons"]:
        lid = lesson["id"]
        if lid not in copy["lessons"]:
            errors.append(f"missing lesson intro copy: {lid}")
        groups_out = []
        for g in lesson["groups"]:
            gid = g["id"]
            if gid not in copy["groups"]:
                errors.append(f"missing group copy: {gid}")
                gcopy = {}
            else:
                gcopy = copy["groups"][gid]
            images_out = []
            for jid in g["images"]:
                if jid in controls and g["layout"] == "caption-experiment":
                    # Experiment C plates may be controls themselves (C00, C04)
                    c = controls[jid]
                    images_out.append({
                        "job": jid, "label": c["title"], "cue": "Reused plate — the picture never changes.",
                        "src": c["src"], "thumb": c["thumb"], "alt": c["alt"],
                        "status": "accepted", "control_ref": jid})
                    continue
                job = jobs[jid]
                st = status.get(jid, job["status"])
                entry = {"job": jid, "label": job["label"], "cue": job["visual_cue"],
                         "control": job["control"]}
                if job.get("sequence_order"):
                    entry["sequence_order"] = job["sequence_order"]
                if job.get("page_dialogue"):
                    entry["dialogue"] = job["page_dialogue"]
                note = led["jobs"].get(jid, {}).get("note", "")
                if job["status"] == "reuse" or st == "reuse":
                    orig = jobs[job["reuse_of"]]
                    full, thumb = art_rel(orig)
                    entry.update({"src": full, "thumb": thumb, "status": "accepted",
                                  "reuse_of": job["reuse_of"],
                                  "alt": f"TSMC — {job['label']}: {job['visual_cue']} "
                                         f"(same plate as {orig['label']} in {orig['group']})"})
                    n_reuse_slots += 1
                elif st == "accepted":
                    full, thumb = art_rel(job)
                    dims = web_copy(os.path.join(SRC, "images", jid + ".webp"),
                                    os.path.join(PAGE, full), os.path.join(PAGE, thumb))
                    entry.update({"src": full, "thumb": thumb, "status": "accepted",
                                  "alt": f"TSMC — {job['label']}: {job['visual_cue']}",
                                  "prompt": job["prompt"], **dims})
                    if note.startswith("Accepted with deviation"):
                        entry["note"] = note
                    accepted_jobs.add(jid)
                else:
                    entry.update({"status": "pending",
                                  "alt": f"Pending plate — TSMC, {job['label']}: {job['visual_cue']}"})
                    n_pending += 1
                images_out.append(entry)
            groups_out.append({
                "id": gid, "title": g["title"], "control": g["control"],
                "layout": g["layout"], "fixed": g["invariants"],
                "learn": gcopy.get("learn", ""), "observe": gcopy.get("observe", []),
                "meaning": gcopy.get("meaning", ""), "alternatives": gcopy.get("alternatives", ""),
                "concepts": gcopy.get("concepts", []), "prompt_tip": gcopy.get("prompt_tip", ""),
                "captions": g.get("captions"),
                "images": images_out})
        mid, mtitle = MODULE_OF[lid]
        ex = copy["exercises"].get(lid, {})
        if not ex:
            errors.append(f"missing exercise copy: {lid}")
        lessons_out.append({
            "id": lid, "title": lesson["title"], "objective": lesson["objective"],
            "source_note": lesson["source_note"], "module": mid, "module_title": mtitle,
            "intro": copy["lessons"].get(lid, {}).get("intro", ""),
            "exercise": ex.get("exercise", ""), "exercise_answer": ex.get("answer", ""),
            "quiz": lid == "l25",
            "groups": groups_out})

    data = {
        "title": "The TSMC Storytelling Course",
        "subtitle": "One character. Many meanings.",
        "series": "TSMC Visual Literacy Series — Part III: Visual Semantics and Pragmatics",
        "controls": [controls[c["id"]] for c in man["controls"]],
        "modules": [{"id": mid, "title": t, "lessons": lids} for mid, t, lids in MODULES],
        "lessons": lessons_out,
        "coverage": {
            "study_accepted": len(accepted_jobs), "study_pending": n_pending,
            "reuse_slots": n_reuse_slots,
            "study_total": len([j for j in man["jobs"]]),
            "groups": sum(len(l["groups"]) for l in man["lessons"]),
            "lessons": len(man["lessons"]),
            "controls": len(man["controls"]),
        },
    }
    with open(os.path.join(PAGE, "storytelling.json"), "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    shutil.copy(os.path.join(SRC, "manifest.json"),
                os.path.join(PAGE, "generation-manifest.json"))
    print(f"coverage: {len(accepted_jobs)} accepted, {n_pending} pending, "
          f"{n_reuse_slots} reuse slots, {data['coverage']['groups']} groups, "
          f"{data['coverage']['lessons']} lessons")
    if errors:
        print("COPY GAPS:")
        for e in errors:
            print(" -", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
