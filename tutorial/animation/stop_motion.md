# Digital stop-motion paper puppets (#83)

**Demonstrated:** Eight original SVG pose frames and printable paper parts, with deliberate 8fps cadence.

## Run

```sh
python -m unittest tools.test_animation_stop_motion -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/stop_motion/preview.html
```

The [review board](../../chapters/pilot-001/video/stop_motion/reference-board.svg) and technique-specific SVG artwork are original. The canonical character reference cards in `characters/intel` and `characters/amd` remain untouched.

Play the 8fps stepped paper-cutout simulation, inspect its frame-by-frame SVG sources, and print `printable-puppets.svg` with paper fasteners. A real physical stop-motion test would require a locked camera, even lighting, permissions and 8–12 unique photographic frames per second.

**Release gate:** This is simulated digital stop-motion, not photographs of physically moved puppets. Review the motion/interaction on a phone and desktop, verify source licenses and hashes, and obtain human approval before merging as complete.
