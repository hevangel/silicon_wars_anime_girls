# Silicon Wars · Pose & Costume

Local dashboard adapted from the Open Pose & Costume React GUI. Select a pose,
costume and one of the **32 Silicon Wars characters**, then generate using the
installed **Codex CLI**. Character uploads are disabled; costume uploads and
costume extraction remain available.

```powershell
cd B:\silicon_wars_anime_girls\pose-costume
npm install
npm run dev
```

Open **http://127.0.0.1:5200**. For a production build, run `npm run build` then
`npm start`. Both modes need the Node server; opening `dist/index.html` directly
does not provide the catalog or generation backend. `PORT` overrides 5200.
The server binds only to loopback and fails if the port is occupied.

## Codex setup

Install Codex CLI and sign in with `codex login`. The server launches the `codex`
executable on PATH. If needed, set `CODEX_BIN` to the absolute executable path
before starting the dashboard:

```powershell
$env:CODEX_BIN = 'C:\path\to\codex.exe'
npm run dev
```

The CLI must expose an image generation tool in noninteractive `codex exec`
sessions. The settings dialog checks CLI availability, **not image tool access**.
If a session lacks the tool, the job fails with an explanation and log; the
backend never substitutes a drawing or calls Atomflow/OpenWego. No image API key
is requested by this dashboard. Codex retains its own authentication, provider,
network and approval configuration. The process is local; image generation still
uses the service configured for Codex.

Generation invokes `codex exec --ephemeral --sandbox workspace-write -C <job-dir>`
with separate `--image <path>` arguments and the full prompt over stdin. No shell
or approval bypass flags are used. Only one job runs at a time. Cancel stops its
process tree; jobs time out after 15 minutes of CLI execution. Jobs already
running are cancelled when the server exits. Restarting the server clears job
handles; saved output files and browser history remain.

## References and outputs

The top-right index example uses the AMD snow render from job
`fef3c556-d379-4122-a167-a6c4c8b242bc`, with its actual depth-pose reference,
WIN-0026 costume and AMD model sheet. The featured render, prompt and metadata
are committed as an explicit exception to ignored job output. Pose and costume
assets remain at their existing sources; the example depth pose loads from its
original gallery URL.

- The pose/costume catalog is read directly from
  `../external/open-pose-costume/public/data/catalog.json` on server startup.
- Images under the upstream `pose/`, `costume/` and `public/custom/` directories
  are served in place. Nothing is copied into this app. Gallery URLs remain as
  fallbacks for references absent from the checkout; these require internet.
  A selected missing original is downloaded into that job directory for Codex.
- Character selection reads `../characters/roster.json` and uses each canonical
  `character_sheet.png` (or reference card if a sheet is absent). Generation adds
  the current character profile and series bible. Restart after roster changes.
- All generated images are saved to
  `pose-costume/output/<job-id>/output.png`. Alongside them are
  `generation.prompt.md`, `generation.json` (separate identity, scene and
  lettering fields, reference IDs and hashes), `codex.log`, and `status.json`.
  Existing approved art is never overwritten.
- Costume-only extraction jobs use the same `pose-costume/output/<job-id>/`
  structure. The output directory is ignored by Git. Existing files in the
  former character/extraction locations remain accessible at their original URLs.
- Size and quality are instructions to the Codex image tool; exact dimensions
  depend on that tool. Costume changes retain identity and company marks, and
  prompts require age-appropriate treatment for the younger cast.
- Favorites, selection and history use separate `swpc-` browser storage keys.

## Validation and attribution

`npm test` checks catalog replacement, reference validation, CLI arguments,
provenance, cancellation, concurrency and missing-output failures with a fake
Codex process. `npm run build` typechecks and builds the retained React GUI.
These tests do not demonstrate live image tool access.

UI source adapted from `external/open-pose-costume` at upstream revision
`578461c575987ef1a4223fdac3144692d1c123e6`. No submodule pin was changed. See
[UPSTREAM-LICENSE](UPSTREAM-LICENSE). Reference image rights are governed by the
upstream [SOURCES.md](../external/open-pose-costume/SOURCES.md),
[THIRD_PARTY_NOTICES.md](../external/open-pose-costume/THIRD_PARTY_NOTICES.md), and
[custom asset terms](../external/open-pose-costume/public/custom/LICENSE.txt).
