from Sprite.Spd.spd import spd
from Sprite.Spd.spd_texture_entry import spd_texture_entry
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry

from Sprite.Spr.spr import spr
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry

import os
import sys
import glob
from collections import OrderedDict
from pathlib import Path

def assemble_sprite(path, file_type):
    texture_ids = get_ids_from_filenames(path, 'tex', '*.dds')
    sprite_ids = get_ids_from_filenames(path, 'spr', '*.spdspr')

    sprite_file = spd()
    
    for id in texture_ids:
        texture_path = path + '\\' + f'tex_{id}.dds'
        sprite_file.texture_dict[id] = spd_texture_entry.create(id, f'texture{id}', texture_path)
        sprite_file.texture_data_dict[id] = open(texture_path, 'rb').read()

    for id in sprite_ids:
        sprite_path = path + '\\' + f'spr_{id}.spdspr'
        sprite_texture_path = path + '\\' + f'spr_{id}.dds'

        sprite_file.sprite_dict[id] = spd_sprite_entry.read_from_file(sprite_path)

        if os.path.isfile(sprite_texture_path):
            new_texture_id = max(sprite_file.texture_dict.keys()) + 1
            sprite_file.texture_dict[new_texture_id] = spd_texture_entry.create(new_texture_id, f'sprite_{id}', sprite_texture_path)
            sprite_file.sprite_dict[id].sprite_texture_id = new_texture_id
            sprite_file.texture_data_dict[new_texture_id] = open(sprite_texture_path, 'rb').read()
        
    sprite_file.build(path + '_out.spd')

def get_ids_from_filenames(path, prefix, extension):
    # Path to files with texture extension
    file_path = path + '\\*' + extension
    
    files = glob.glob(file_path)
    
    file_path: list = []

    for file in files:
        if not Path(file).stem.startswith(prefix):
            continue

        id = int(Path(file).stem.split('_')[1]) 
        file_path.append(id) 

    file_path.sort()
    return file_path 

assemble_sprite("E:\ModsnStuff\P5R Modding real\steam files\EN.CPK_unpacked\FONT\CHAT\CHAT", 'spd')
