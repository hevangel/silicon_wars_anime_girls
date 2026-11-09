"""Build a self-contained Silicon Wars gallery from website/ and its character art."""
import argparse
import json
from pathlib import Path
from shutil import copyfile

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New directory for the gallery")
    args = parser.parse_args()

    site = json.loads((WEBSITE / "data" / "site.json").read_text(encoding="utf-8"))
    characters_file = WEBSITE / site["paths"]["characters"]
    characters = json.loads(characters_file.read_text(encoding="utf-8"))["characters"]

    # Site files keep their layout; art is copied beside them, so assetBase becomes "".
    site["paths"]["assetBase"] = ""
    generated = {"data/site.json": json.dumps(site, indent=2, ensure_ascii=False) + "\n"}
    sources = {
        path.relative_to(WEBSITE).as_posix(): path
        for path in WEBSITE.rglob("*")
        if path.is_file() and path.relative_to(WEBSITE).as_posix() not in generated
    }
    for character in characters:
        for relative in [character["referenceCard"], *character["artwork"].values()]:
            sources[relative] = ROOT / relative

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
    for name, text in generated.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
    print(output / "index.html")


if __name__ == "__main__":
    main()
