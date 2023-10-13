from Sprite.Spd.spd import spd
from Sprite.Spd.spd_texture_entry import spd_texture_entry
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry

from Sprite.Spr.spr import spr
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry
from Sprite.Spr.tmx import tmx

import os
import sys
from pathlib import Path

def extract_sprite(path):
    file_type: str = os.path.splitext(path)[1].lower()

    if file_type.endswith('spr'):
        extract_spr(path) 
    elif file_type.endswith('spd'):
        extract_spd(path) 
    else:
        print("Invalid File Type")
        return

def extract_spd(path):
    sprite_file = spd.read_file(path)
    sprite_path = os.path.dirname(path) + '\\' + Path(path).stem + '\\'

    if not os.path.isdir(sprite_path):
        os.mkdir(sprite_path)
    
    for key, value in sprite_file.texture_data_dict.items():
        with open(sprite_path + f'tex_{key}.dds', 'wb') as texture:
            print(len(value))
            texture.write(value)

    for key, value in sprite_file.sprite_dict.items():
        with open(sprite_path + f'spr_{key}.spdspr', 'wb') as sprite:
            value.write(sprite)

def extract_spr(path):
    sprite_file = spr.read_file(path)
    sprite_path = os.path.dirname(path) + '\\' + Path(path).stem + '\\'

    if not os.path.isdir(sprite_path):
        os.mkdir(sprite_path)
 
    for i, texture in enumerate(sprite_file.texture_data):
        with open(sprite_path + f'tex_{i}.tmx', 'wb') as texture_file:
            texture.write(texture_file)

    for i, sprite in enumerate(sprite_file.sprite_list):
        with open(sprite_path + f'spr_{i}.sprt', 'wb') as sprite_file:
            sprite.write(sprite_file)

extract_sprite(sys.argv[1])
