# MinecraftShapes To Schematic

A little tool I made to convert an SVG file obtained from [MinecraftShapes](https://minecraftshapes.com/) to a schematic file for use with [Litematica](https://github.com/maruohon/litematica).

## Usage

To use the tool, simply run the `to_schematic.py` file according to the following usage:

```
usage: to_schematic.py [-h] [--brush BRUSH] [--version VERSION] svg schematic

positional arguments:
  svg                The path to the SVG file
  schematic          The path at which to save the schematic

options:
  -h, --help         show this help message and exit
  --brush BRUSH      The block to use for the schematic. By default 'minecraft:gold_block'
  --version VERSION  The version for which the schematic is for. By default 'JE_1_12_2'
```
