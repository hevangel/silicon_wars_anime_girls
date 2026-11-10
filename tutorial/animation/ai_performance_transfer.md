# AI performance transfer (#80)

This is an implementation milestone: **Consent-gated driver pose to AMD**. It has an original [visual board](../../chapters/pilot-001/video/ai_performance_transfer/reference-board.svg), a runnable browser concept preview, a three-beat scene JSON, pipeline YAML and smoke tests.

```sh
python -m unittest tools.test_animation_ai_performance_transfer -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/ai_performance_transfer/preview.html
```

The synthetic driver / target pose mapping contains no real actor footage. Real recordings must be accompanied by explicit source rights and consent in a ledger before any external performance-transfer model is used.

Edit `scene.json` for timing and review the original storyboard before creating final export.

Technical validation does not certify video quality or artistic approval.

**Not complete:** No rights-cleared actor recording or inference provider result; demonstration uses procedurally authored driver motions.. Record source hashes, precise tool versions, rights and generated binary provenance, render and visually approve the result, then replace the draft status.
