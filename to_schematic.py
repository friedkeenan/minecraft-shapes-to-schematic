#!/usr/bin/env python3

import mcschematic

from pathlib     import Path
from svgelements import SVG, Rect

def convert(svg_path, schematic_path, brush, version):
    schematic_path = Path(schematic_path)

    if schematic_path.suffix != ".schem":
        raise ValueError("Schematic path must end with the '.schem' extension")

    svg    = SVG.parse(svg_path)
    blocks = list(svg.elements(lambda elem: isinstance(elem, Rect) and elem.fill == "#008000"))

    min_x = min(blocks, key=lambda elem: elem.x).x
    min_y = min(blocks, key=lambda elem: elem.y).y

    next_min_y = min((block for block in blocks if block.y > min_y), key=lambda elem: elem.y).y
    scale      = next_min_y - min_y

    schematic = mcschematic.MCSchematic()
    for block in blocks:
        # NOTE: This probably won't fly for everything,
        # but it worked for me and that's good enough.
        x = int((block.x - min_x) // scale)
        y = int((block.y - min_y) // scale)

        schematic.setBlock((x, 0, y), brush)

    schematic_path.parent.mkdir(parents=True, exist_ok=True)
    schematic.save(str(schematic_path.parent), schematic_path.stem, version)

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()

    parser.add_argument("svg",       type=Path, help="The path to the SVG file")
    parser.add_argument("schematic", type=Path, help="The path at which to save the schematic")

    parser.add_argument("--brush",   default="minecraft:gold_block", help="The block to use for the schematic. By default 'minecraft:gold_block'")
    parser.add_argument("--version", default="JE_1_12_2",            help="The version for which the schematic is for. By default 'JE_1_12_2'")

    args = parser.parse_args()

    version = getattr(mcschematic.Version, args.version, None)
    if version is None:
        print(f"Invalid version: '{args.version}'")

        sys.exit(1)

    convert(args.svg, args.schematic, args.brush, version)
