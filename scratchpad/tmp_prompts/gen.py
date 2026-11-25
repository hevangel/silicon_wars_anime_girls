"""Call the AutoGLM Seedream endpoint with a plate prompt read verbatim from plates.json."""
from __future__ import annotations

import json
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILL = pathlib.Path(
    r"C:\Users\hevan\AppData\Roaming\AutoClaw-oversea-official\accounts"
    r"\c4bb4efa970685b36dd0f4ee4d0916c0dfa372a29abb3aac1a23ac5e48750d9d"
    r"\runtime\pi-resources\revisions\30347b2447b96ab5"
    r"\skills\autoglm-generate-image-seedream"
)


def load_module(name: str, filename: str):
    import importlib.util

    spec = importlib.util.spec_from_file_location(name, SKILL / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # noqa: SLF001 - script modules guard main()
    return mod


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gen.py <plate-id>")
        return 2
    pid = sys.argv[1]
    plates = json.loads((ROOT / "art/style-study/plates.json").read_text(encoding="utf-8"))
    plate = next((p for p in plates["plates"] if p["id"] == pid), None)
    if plate is None:
        print(f"unknown plate: {pid}")
        return 1

    skill = load_module("seedream_mod", "generate-image-seedream.py")

    # fresh public URL for the character sheet each attempt (upload signatures decay)
    import mimetypes, uuid  # noqa: E401

    sheet = ROOT / "characters/arm/character_sheet.png"
    filename = sheet.name
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    data = sheet.read_bytes()
    token = skill.get_token()
    ts = str(int(__import__("time").time()))
    sign = __import__("hashlib").md5(
        f"100003&{ts}&38d2391985e2369a5fb8227d8e6cd5e5".encode()
    ).hexdigest()
    boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:16]}"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="files"; filename="{filename}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode() + data + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        "https://autoglm-api.autoglm.ai/agentdr/v1/assistant/upload-mix",
        data=body,
        headers={
            "Authorization": token,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "X-Auth-Appid": "100003",
            "X-Auth-TimeStamp": ts,
            "X-Auth-Sign": sign,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        up = json.loads(resp.read().decode())
    image_url = up["data"]["oss_info"][0]["oss_url"]

    token = skill.get_token()
    headers = skill.build_headers(token)
    payload = json.dumps({"query": plate["prompt"], "image": image_url}).encode()
    req = urllib.request.Request(
        skill.URL, data=payload, headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        print(f"HTTP_ERROR {exc.code}")
        print(exc.read().decode("utf-8", errors="replace")[:800])
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"TRANSPORT_ERROR {exc}")
        return 1

    url = (result.get("data") or {}).get("image_url", "")
    print(f"CODE {result.get('code')} MSG {result.get('msg')}")
    print(f"IMAGE_URL {url}")
    return 0 if url else 1


if __name__ == "__main__":
    raise SystemExit(main())
