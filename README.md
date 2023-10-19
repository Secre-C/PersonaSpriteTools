# PersonaSpriteTools
Deconstructs an Spd or Spr file, separating each sprite it's own texture and sprite entry. Best used to easily make custom spds to be used with the Spd Emulator

![image](https://github.com/Secre-C/SpdDisassembler/assets/89033534/1baa7f36-ce60-4638-aed3-102aa6d6d545)

## Prerequisites
[ImageMagick](https://imagemagick.org/script/download.php)

[.NET 7.0](https://dotnet.microsoft.com/en-us/download/dotnet/7.0) (for spr disassembly, used by the TmxToPng program)

whatever the latest version of [Python](https://www.python.org/downloads/) is

# Scripts
## SpdDisassembler.py/SprDisassembler.py 
Exports each sprite entry into individual files, and cuts those portions from the texture to export into individual textures

Usage: `SpdDisassembler.py <spd file path> <output folder>`

You may also drag an spd file onto `SpdDisassembler.py`. If you do, the output folder will be `<spd file path>`.

In the output folder, the script will make a `.dds` texture file for each sprite, scaled down to the lowest possible size possible with each dimension being either 2<sup>n</sup> or (2<sup>n</sup> + 2<sup>n-1</sup>) (necessary to prevent crashing).

the script will also create a `.spdspr` file for each sprite entry, with the sprite coordinates zeroed out, making the `.spdspr` and `.dds` files ready to be used with the SpdEmulator releasing soon:tm:

To use with the spd emulator, simply copy your edited sprite and the accompanying `.spdspr` file to the spds path, as you normally would when using the spd emulator.

Usage for `.Spr` files are the same, but the program will output `.sprt` for sprite entries and `.png` files for the images. `.png` files will need to be reconverted to `.tmx` files before using in-game

### WARNING
do NOT use this when replacing sprites that have button prompts next to them. They need to be in a full sized texture otherwise the button next to them won't be in the right place.

## ExtractSprite.py
Exports unmodified sprite textures and sprite entries. Texture names will include the ids of all the sprites that point to them, unless the filename is too long where it will instead use the texture id.

Usage: `ExtractSprite.py <path to .spd or .spr>`

## AssembleSprite.py
Builds a sprite file using texture and sprite entry files from a folder. sprite entry files (`.sprt/.spdspr`) should be named `spr_xx` where `xx` is the id of the sprite. Textures can be named either `tex_xx` or `spr_xx`. `spr` textures will only be included if there's an accompanying sprite entry file with the same name.

Usage: `AssembleSprite.py <path to sprite component folder> <type of sprite file to build (spd or spr)>`

## PatchSprite.py
Patches an existing sprite archive, replacing or appending sprites and textures

Usage: `PatchSprite.py <path to sprite archive> <path to directory containing sprite entries and textures to patch>`

## RoundUpTextureDimensions.py
(For DDS and PNG) rounds up a texture's dimensions to the next 2<sup>n</sup> or (2<sup>n</sup> + 2<sup>n-1</sup>), and fills added pixels with transparent pixels.

Usage: `RoundUpTextureDimensions.py <path to texture>`

## GenerateSpriteEntryFromTexture.py
(For DDS and TMX) Creates a sprite entry file (`.sprt` or `.spdspr`) using the dimensions from a provided texture.

Usage: `GenerateSpriteEntryFromTexture.py <path to texture>`

