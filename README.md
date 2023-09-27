# SpdDisassembler
Deconstructs an Spd file, separating each sprite it's own texture and sprite entry. Best used to easily make custom spds to be used with the Spd Emulator

## Prerequisites
[ImageMagick](https://imagemagick.org/script/download.php)

whatever the latest version of [Python](https://www.python.org/downloads/) is

## Usage
Usage is as follows `SpdDisassembler.py <spd file path> <output folder>`

You may also drag an spd file onto `SpdDisassembler.py`. If you do, the output folder will be `<spd file path>_out`.

In the output folder, the script will make a `.dds` texture file for each sprite, scaled down to the lowest possible size possible with each dimension being either 2<sup>n</sup> or (2<sup>n</sup> + 2<sup>n-1</sup>) (necessary to prevent crashing).

the script will also create a `.spdspr` file for each sprite entry, with the sprite coordinates zeroed out, making the `.spdspr` and `.dds` files ready to be used with the SpdEmulator releasing soon:tm:

Also do NOT use this when replacing sprites that have button prompts next to them. Those need to be in the full sized texture otherwise the button next to them won't show.
