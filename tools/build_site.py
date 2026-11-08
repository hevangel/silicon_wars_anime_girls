"""Build a self-contained Silicon Wars gallery."""
import argparse
import re
from pathlib import Path
from shutil import copyfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New directory for the gallery")
    args = parser.parse_args()

    homepage = ROOT / "index.html"
    card_paths = re.findall(
        r'src="(characters/[^"]+/reference_card\.jpg)"',
        homepage.read_text(encoding="utf-8"),
    )
    sources = {"index.html": homepage}
    sources.update({path: ROOT / path for path in card_paths})

    for source in sources.values():
        if not source.is_file():
            parser.error(f"Missing source file: {source}")

    output = args.output.resolve()
    try:
        output.mkdir(parents=True)
    except FileExistsError:
        parser.error(f"Choose a new output directory: {output}")
    for name, source in sources.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        copyfile(source, destination)
    print(output / "index.html")


if __name__ == "__main__":
    main()
