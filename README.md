# PersonaSpriteTools
Deconstructs an Spd or Spr file, separating each sprite it's own texture and sprite entry. Best used to easily make custom spds to be used with the Spd Emulator

![image](https://github.com/Secre-C/SpdDisassembler/assets/89033534/1baa7f36-ce60-4638-aed3-102aa6d6d545)

## Prerequisites
[ImageMagick](https://imagemagick.org/script/download.php)

[.NET 7.0](https://dotnet.microsoft.com/en-us/download/dotnet/7.0) (for spr disassembly)

whatever the latest version of [Python](https://www.python.org/downloads/) is

## Usage
Usage is as follows `SpdDisassembler.py <spd file path> <output folder>`

You may also drag an spd file onto `SpdDisassembler.py`. If you do, the output folder will be `<spd file path>`.

In the output folder, the script will make a `.dds` texture file for each sprite, scaled down to the lowest possible size possible with each dimension being either 2<sup>n</sup> or (2<sup>n</sup> + 2<sup>n-1</sup>) (necessary to prevent crashing).

the script will also create a `.spdspr` file for each sprite entry, with the sprite coordinates zeroed out, making the `.spdspr` and `.dds` files ready to be used with the SpdEmulator releasing soon:tm:

To use with the spd emulator, simply copy your edited sprite and the accompanying `.spdspr` file to the spds path, as you normally would when using the spd emulator.

Usage for `.Spr` files are the same, but the program will output `.sprt` for sprite entries and `.png` files for the images. `.png` files will need to be reconverted to `.tmx` files before using in-game

### WARNING
do NOT use this when replacing sprites that have button prompts next to them. Those need to be in the full sized texture otherwise the button next to them won't show.
