#!/usr/bin/env python3
"""Generate one style-study plate through the AutoGLM Seedream API.

Reads the plate's prompt verbatim from art/style-study/plates.json, posts it
together with the character-sheet reference URL, and prints the image URL.
Retries up to 4 attempts with ~20s spacing on transport / HTTP 500 failures.

Usage: python scratchpad/seedream_plate.py <plate-id> <reference-url>
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

APP_ID = "100003"
APP_KEY = "38d2391985e2369a5fb8227d8e6cd5e5"
URL = "https://autoglm-api.autoglm.ai/agentdr/v1/assistant/skills/generate-image-seedream"
TOKEN_URL = "http://127.0.0.1:18432/get_token"
ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "art" / "style-study" / "plates.json"


def get_token() -> str:
    with urllib.request.urlopen(TOKEN_URL, timeout=30) as resp:
        token = resp.read().decode("utf-8").strip()
    if not token:
        raise RuntimeError("empty token")
    if not token.lower().startswith("bearer "):
        token = f"Bearer {token}"
    return token


def headers(token: str) -> dict:
    ts = str(int(time.time()))
    sign = hashlib.md5(f"{APP_ID}&{ts}&{APP_KEY}".encode("utf-8")).hexdigest()
    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "X-Auth-Appid": APP_ID,
        "X-Auth-TimeStamp": ts,
        "X-Auth-Sign": sign,
    }


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    pid, image_url = sys.argv[1], sys.argv[2]

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    plate = next((p for p in data["plates"] if p["id"] == pid), None)
    if plate is None:
        print(f"RESULT unknown plate id: {pid}")
        return 1

    body = json.dumps({"query": plate["prompt"], "image": image_url}).encode("utf-8")

    last = ""
    for attempt in range(1, 5):
        try:
            req = urllib.request.Request(
                URL, data=body, headers=headers(get_token()), method="POST"
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            url = (result.get("data") or {}).get("image_url") or ""
            if result.get("code") == 0 and url:
                print(f"RESULT ok attempt={attempt} url={url}")
                return 0
            last = f"code={result.get('code')} msg={result.get('msg')}"
        except urllib.error.HTTPError as exc:
            last = f"http_{exc.code} {exc.read().decode('utf-8', 'replace')[:300]}"
        except Exception as exc:  # noqa: BLE001 - transport failures are retried
            last = f"{type(exc).__name__}: {exc}"
        print(f"ATTEMPT {attempt} failed: {last}", flush=True)
        if attempt < 4:
            time.sleep(20)

    print(f"RESULT failed {last}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
