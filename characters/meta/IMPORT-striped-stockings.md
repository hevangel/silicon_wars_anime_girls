# Import the regenerated Meta outfit assets

Three separate binary assets were generated using the existing repository layout conventions:

| Path | Purpose | Dimensions | SHA-256 |
|---|---|---|---|
| `characters/meta/character_sheet.png` | Character turnaround | 1536×1024 | `fdfbd7c90987803afb8ef8cd149ad65a28f5d1ae591d5e07060db638c099f071` |
| `characters/meta/expressions.png` | 12-expression reference sheet | 1536×1024 | `3af41170f40708fb68754df1ba80bd84e9c590b1eb48426ad55800c88d19b83b` |
| `characters/meta/reference_card.jpg` | Portrait reference card | 1024×1536 | `4503255153512307aec9e5859299553a5cd6071c1291429e18fae5f59bce0fda` |

**Status:** These binary images are **not yet uploaded** to this branch. Their source bytes are in the ChatGPT download package `meta_striped_stockings_import.zip`.

Extract that ZIP **outside** your local repository and run `bash /path/to/meta_striped_stockings_import/push_meta.sh` from the repository root. The script checks the origin repository, fetches `art/meta-social-worldbuilder`, copies the three files, creates a commit and pushes it to PR #11's existing branch.

**Visual continuity:** Blue-violet hair, Meta-logo VR headset, oversized black hoodie, purple holographic cape, purple-and-black **opaque horizontal striped stockings that entirely cover her thighs**, black boots.
