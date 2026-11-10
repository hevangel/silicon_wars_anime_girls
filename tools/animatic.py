#!/usr/bin/env python3
"""Frame-accurate storyboard-to-animatic builder for Silicon Wars pilot 001.

Uses existing approved/review-draft panel PNGs; never generates replacement art.
Requires Pillow and PyYAML; MP4 mode additionally requires ffmpeg+libx264.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TIMELINE = ROOT / "chapters/pilot-001/video/animatic/timeline.json"
VERSION = "1.0.0"


class AnimaticError(ValueError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_repo_path(root: Path, rel: str) -> Path:
    if not isinstance(rel, str) or not rel:
        raise AnimaticError("Expected a repository-relative path")
    path = (root / rel).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise AnimaticError("Missing or unsafe source: " + rel)
    return path


def load(timeline_path: Path, root: Path = ROOT, verify_art: bool = True):
    root = root.resolve()
    data = json.loads(timeline_path.read_text(encoding="utf-8"))
    if data.get("schema") != 1 or data.get("technique") != "animatic":
        raise AnimaticError("Expected schema 1 and technique animatic")
    if data.get("art_style") != "default_manga" or data.get("reading_direction") != "rtl":
        raise AnimaticError("Pilot source art style and RTL reading direction must be explicit")
    if type(data.get("fps")) is not int or not 1 <= data["fps"] <= 120:
        raise AnimaticError("FPS must be a positive integer up to 120")
    if (not isinstance(data.get("resolution"), list)
            or len(data["resolution"]) != 2
            or any(type(v) is not int or v <= 0 or v % 2 for v in data["resolution"])):
        raise AnimaticError("Resolution must be positive even dimensions")
    if type(data.get("frames")) is not int or data["frames"] <= 0:
        raise AnimaticError("Total frames must be positive")
    storyboard = yaml.safe_load(resolve_repo_path(root, data["source_storyboard"]).read_text(encoding="utf-8"))
    lettering = yaml.safe_load(resolve_repo_path(root, data["source_lettering"]).read_text(encoding="utf-8"))
    manifest = yaml.safe_load(resolve_repo_path(root, data["source_manifest"]).read_text(encoding="utf-8"))
    story_ids = [p["id"] for p in storyboard["panels"]]
    lettering_map = {p["id"]: p for p in lettering["items"]}
    generated = {p["id"]: p for p in manifest["panels"]}
    shots = data.get("shots")
    if not isinstance(shots, list) or not shots:
        raise AnimaticError("At least one shot required")
    ids = set()
    next_frame = 0
    details = []
    for shot in shots:
        sid = shot.get("id")
        if not isinstance(sid, str) or not sid or sid in ids:
            raise AnimaticError("Unique stable shot IDs are required")
        ids.add(sid)
        start, end = shot.get("start_frame"), shot.get("end_frame")
        if (type(start) is not int or type(end) is not int
                or start != next_frame or end <= start):
            raise AnimaticError(sid + ": shots must have contiguous integer [start,end) ranges")
        next_frame = end
        panel = shot.get("panel_id")
        if panel not in story_ids or story_ids.index(panel) != len(details):
            raise AnimaticError(sid + ": source panel order must match RTL storyboard")
        if generated[panel]["output"] != shot.get("art"):
            raise AnimaticError(sid + ": source does not match published page manifest")
        if generated[panel]["image_sha256"] != shot.get("art_sha256"):
            raise AnimaticError(sid + ": expected art hash does not match the source manifest")
        path = resolve_repo_path(root, shot["art"])
        if verify_art and sha256(path) != shot["art_sha256"]:
            raise AnimaticError(sid + ": source panel SHA-256 changed; re-review before rebuilding")
        if not isinstance(shot.get("characters"), list):
            raise AnimaticError(sid + ": characters must be an explicit list")
        camera = shot.get("camera", {})
        center = camera.get("center")
        if (not isinstance(center, list) or len(center) != 2
                or any(type(v) not in (int, float) or not 0 <= v <= 1 for v in center)):
            raise AnimaticError(sid + ": camera center must be normalized coordinates")
        for key in ("zoom_from", "zoom_to"):
            zoom = camera.get(key)
            if type(zoom) not in (int, float) or not 1 <= zoom <= 1.5:
                raise AnimaticError(sid + ": invalid " + key)
        seen_cues = set()
        for cue in shot.get("cues", []):
            cid = cue.get("id")
            if cid in seen_cues or cid not in lettering_map:
                raise AnimaticError(sid + ": missing or duplicate lettering ID")
            seen_cues.add(cid)
            source = lettering_map[cid]
            if source["panel"] != panel or cue.get("text") != source["text"]:
                raise AnimaticError(sid + ": cue text/panel differs from editable lettering")
            offset, duration = cue.get("offset_frames"), cue.get("duration_frames")
            if (type(offset) is not int or type(duration) is not int
                    or offset < 0 or duration <= 0 or offset + duration > end - start):
                raise AnimaticError(sid + ": cue outside shot timing")
        for cid in shot.get("screen_overlays", []):
            if cid not in lettering_map or lettering_map[cid]["panel"] != panel or lettering_map[cid]["kind"] != "screen":
                raise AnimaticError(sid + ": unknown screen overlay")
        details.append({"id": sid, "art_path": path, "start": start, "end": end, "source_sha256": shot["art_sha256"]})
    if next_frame != data["frames"]:
        raise AnimaticError("Last frame must equal frames field")
    return data, details, lettering_map


def timecode(frames, fps):
    millis = (frames * 1000 + fps // 2) // fps
    hours, remain = divmod(millis, 3600000)
    minutes, remain = divmod(remain, 60000)
    seconds, milliseconds = divmod(remain, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def build_edit_metadata(data, out: Path, lettering):
    fps = data["fps"]
    with (out / "edit-decision-list.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["shot_id", "panel_id", "start_frame", "end_frame_exclusive", "fps",
                         "start_s", "duration_s", "art", "sha256", "cue_ids"])
        for shot in data["shots"]:
            writer.writerow([shot["id"], shot["panel_id"], shot["start_frame"],
                             shot["end_frame"], fps, shot["start_frame"]/fps,
                             (shot["end_frame"]-shot["start_frame"])/fps,
                             shot["art"], shot["art_sha256"],
                             "|".join(c["id"] for c in shot.get("cues", []))])
    events = []
    for shot in data["shots"]:
        for cue in shot.get("cues", []):
            source = lettering[cue["id"]]
            if source["kind"] == "screen":
                continue
            start = shot["start_frame"] + cue["offset_frames"]
            end = start + cue["duration_frames"]
            events.append((start, end, cue["text"]))
    events.sort()
    srt = []
    for index, (start, end, text) in enumerate(events, start=1):
        srt.extend([str(index), f"{timecode(start, fps)} --> {timecode(end, fps)}", text, ""])
    (out / "subtitles.srt").write_text("\n".join(srt), encoding="utf-8")


def fit_panel(image: Image.Image, size, center):
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS,
                        centering=(float(center[0]), float(center[1])))


def build_stills(data, details, lettering, out: Path, size):
    temp = out / "stills"
    temp.mkdir(parents=True, exist_ok=True)
    thumbs = []
    for shot, detail in zip(data["shots"], details):
        with Image.open(detail["art_path"]) as image:
            still = fit_panel(image, size, shot["camera"]["center"])
        for cue_id in shot.get("screen_overlays", []):
            text = lettering[cue_id]["text"]
            draw = ImageDraw.Draw(still)
            rect = [int(size[0]*.20), int(size[1]*.87),
                    int(size[0]*.80), int(size[1]*.97)]
            draw.rounded_rectangle(rect, radius=max(4, size[1]//95),
                                   fill=(15, 27, 40), outline=(115, 165, 215), width=2)
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                                      max(10, size[1]//30)) if Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf").is_file() else ImageFont.load_default()
            draw.text((size[0]*.50, size[1]*.92), text,
                      anchor="mm", fill=(225, 238, 250), font=font)
        target = temp / (shot["id"] + ".png")
        still.save(target)
        thumb = ImageOps.contain(still, (480, 270))
        tile = Image.new("RGB", (480, 292), (18, 25, 36))
        tile.paste(thumb, ((480-thumb.width)//2, 0))
        dr = ImageDraw.Draw(tile)
        dr.text((8, 272), f'{shot["id"]}: {shot["panel_id"]}  '
                 f'{shot["start_frame"]}-{shot["end_frame"]} @ {data["fps"]} fps',
                 fill=(235, 239, 245))
        thumbs.append(tile)
    contact = Image.new("RGB", (480*3, 292*math.ceil(len(thumbs)/3)), (0, 0, 0))
    for i, thumb in enumerate(thumbs):
        contact.paste(thumb, ((i%3)*480, (i//3)*292))
    contact.save(out / "contact-sheet.jpg", quality=87)
    return temp


def synth_placeholder_audio(data, lettering, out: Path):
    """Generate only *silence and synthetic mechanical clicks*, never fake dialogue."""
    rate = 48000
    samples = [0] * (data["frames"] * rate // data["fps"])
    # Sound-effect cues from source lettering, no AI speech or real-person voice.
    for shot in data["shots"]:
        for cue in shot.get("cues", []):
            if lettering[cue["id"]]["kind"] != "sfx":
                continue
            start_frame = shot["start_frame"] + cue["offset_frames"]
            for click in (0, 7):  # mechanical dual click
                start = (start_frame + click) * rate // data["fps"]
                for i in range(int(rate * .11)):
                    pos = start + i
                    if pos >= len(samples):
                        break
                    envelope = math.exp(-i / (rate * .02))
                    val = int(6500 * envelope * math.sin(2 * math.pi * 940 * i / rate))
                    samples[pos] = max(-32768, min(32767, samples[pos] + val))
    with wave.open(str(out / "placeholder-audio.wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(struct.pack("<" + "h" * len(samples), *samples))


def command(args):
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def render_mp4(data, out: Path, stills: Path, size):
    if not shutil.which("ffmpeg"):
        raise AnimaticError("ffmpeg executable required for MP4; use --no-video for metadata and contact sheet")
    fps = data["fps"]
    clips = out / "clips"
    clips.mkdir(exist_ok=True)
    outputs = []
    for shot in data["shots"]:
        n = shot["end_frame"] - shot["start_frame"]
        cam = shot["camera"]
        z0, z1 = cam["zoom_from"], cam["zoom_to"]
        cx, cy = cam["center"]
        # Each static storyboard becomes n original 24-fps frames via zoompan.
        z = f"{z0:.6f}+({z1-z0:.7f})*on/{max(1,n-1)}"
        xp = f"max(0,min(iw-iw/zoom,iw*{cx:.6f}-iw/(2*zoom)))"
        yp = f"max(0,min(ih-ih/zoom,ih*{cy:.6f}-ih/(2*zoom)))"
        vf = f"zoompan=z='{z}':x='{xp}':y='{yp}':d={n}:fps={fps}:s={size[0]}x{size[1]},format=yuv420p"
        clip = clips / (shot["id"] + ".mp4")
        command(["ffmpeg", "-y", "-loglevel", "error",
                 "-i", str(stills / (shot["id"] + ".png")),
                 "-vf", vf, "-frames:v", str(n), "-r", str(fps),
                 "-an", "-c:v", "libx264", "-preset", "ultrafast",
                 "-crf", "31", "-pix_fmt", "yuv420p", str(clip)])
        outputs.append(clip)
    concat_file = out / "clips.txt"
    concat_file.write_text("".join("file '" + p.resolve().as_posix() + "'\n" for p in outputs),
                           encoding="utf-8")
    joined = out / "joined-no-audio.mp4"
    command(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(concat_file), "-c", "copy", str(joined)])
    command(["ffmpeg", "-y", "-loglevel", "error",
             "-i", str(joined), "-i", str(out/"placeholder-audio.wav"),
             "-i", str(out/"subtitles.srt"),
             "-map", "0:v:0", "-map", "1:a:0", "-map", "2:s:0",
             "-c:v", "copy", "-c:a", "aac", "-b:a", "96k", "-c:s", "mov_text",
             "-disposition:s:0", "default",
             "-t", str(data["frames"]/fps), "-movflags", "+faststart",
             str(out/"animatic.mp4")])


def build(timeline: Path, out: Path, root: Path = ROOT,
          video: bool = True, size_override=None):
    data, details, lettering = load(timeline, root=root)
    out.mkdir(parents=True, exist_ok=True)
    size = tuple(size_override or data["resolution"])
    if any(type(x) is not int or x <= 0 or x % 2 for x in size) or size[0]*9 != size[1]*16:
        raise AnimaticError("Preview/export resolution must have even 16:9 dimensions")
    build_edit_metadata(data, out, lettering)
    stills = build_stills(data, details, lettering, out, size)
    synth_placeholder_audio(data, lettering, out)
    if video:
        render_mp4(data, out, stills, size)
    result = {
        "schema": 1, "technique": "animatic",
        "review_status": "timing_draft_not_human_approved",
        "fps": data["fps"], "frames": data["frames"],
        "duration_seconds": data["frames"]/data["fps"], "resolution": list(size),
        "tool_version": VERSION, "python": sys.version.split()[0],
        "ffmpeg_version": (subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True).stdout.splitlines()[0]
                           if video else "not_run"),
        "audio": "synthetic mechanical clicks and silence; NO generated voices",
        "subtitles": "selectable mov_text in MP4; source synced to editable lettering YAML",
        "source_images": {d["id"]: {"path": d["art_path"].relative_to(root).as_posix(),
                                    "sha256": d["source_sha256"]} for d in details},
        "outputs": {p.name: sha256(p) for p in sorted(out.glob("*"))
                    if p.is_file() and p.name not in ("build-manifest.json", "joined-no-audio.mp4")},
    }
    (out/"build-manifest.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--timeline", type=Path, default=DEFAULT_TIMELINE)
    p.add_argument("--out", type=Path, default=Path("/tmp/silicon-wars-animatic"))
    p.add_argument("--check", action="store_true", help="Validate all sources/hashes and timeline without rendering")
    p.add_argument("--no-video", action="store_true", help="Make metadata, WAV and contact sheet without ffmpeg")
    p.add_argument("--size", default=None, help="Test export size, e.g. 640x360; defaults to 1920x1080")
    args = p.parse_args()
    try:
        if args.check:
            data, details, _ = load(args.timeline)
            print("VALID", len(details), "shots", data["frames"], "frames", data["fps"], "fps")
            return
        size = list(map(int, args.size.lower().split("x"))) if args.size else None
        result = build(args.timeline, args.out, video=not args.no_video, size_override=size)
        print("BUILT", result["duration_seconds"], "seconds",
              result["resolution"], "video=", not args.no_video,
              "at", args.out)
    except (AnimaticError, OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        p.exit(1, "animatic: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
