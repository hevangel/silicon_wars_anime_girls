"""Build a self-contained Silicon Wars gallery."""
import argparse
from pathlib import Path
from shutil import copyfile

ROOT = Path(__file__).resolve().parents[1]
CHARACTERS = ("intel", "amd", "nvidia")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New directory for the gallery")
    args = parser.parse_args()

    sources = {
        "index.html": ROOT / "site/index.html",
        "assets/storyboard.svg": ROOT / "chapters/pilot-001/storyboard.svg",
        "assets/pilot-001.png": ROOT / "chapters/pilot-001/pages/page-001/final/page-001.png",
    }
    for character in CHARACTERS:
        sources[f"assets/{character}.jpg"] = (
            ROOT / "characters" / character / "reference_card.jpg"
        )

    for source in sources.values():
        if not source.is_file():
            parser.error(f"Missing source file: {source}")

    output = args.output.resolve()
    try:
        output.mkdir(parents=True)
    except FileExistsError:
        parser.error(f"Choose a new output directory: {output}")
    (output / "assets").mkdir()
    for name, source in sources.items():
        copyfile(source, output / name)
    print(output / "index.html")


if __name__ == "__main__":
    main()
