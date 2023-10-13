from Sprite.Spd.spd import spd
from Sprite.Spd.spd_texture_entry import spd_texture_entry
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry

from Sprite.Spr.spr import spr
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry
from Sprite.Spr.tmx import tmx

import os
import sys
import glob
from collections import OrderedDict
from pathlib import Path

def assemble_spd(path):
    sprite_extension = 'spdspr'
    texture_extension = 'dds'

    # initialize spd
    sprite_file = spd()

    # get texture and sprite id list
    texture_ids = get_ids_from_filenames(path, 'tex', f'*.{texture_extension}')
    sprite_ids = get_ids_from_filenames(path, 'spr', f'*.{sprite_extension}')
    
    for id in texture_ids:
        texture_path = path + '\\' + f'tex_{id}.{texture_extension}'
        sprite_file.texture_dict[id] = spd_texture_entry.create(id, f'texture{id}', texture_path)
        sprite_file.texture_data_dict[id] = open(texture_path, 'rb').read()

    for id in sprite_ids:
        sprite_path = path + '\\' + f'spr_{id}.{sprite_extension}'
        sprite_texture_path = path + '\\' + f'spr_{id}.{texture_extension}'

        sprite_file.sprite_dict[id] = spd_sprite_entry.read_from_file(sprite_path)

        if os.path.isfile(sprite_texture_path):
            new_texture_id = 0

            if len(sprite_file.texture_dict) != 0:
                new_texture_id = max(sprite_file.texture_dict.keys()) + 1

            sprite_file.texture_dict[new_texture_id] = spd_texture_entry.create(new_texture_id, f'sprite_{id}', sprite_texture_path)
            sprite_file.sprite_dict[id].sprite_texture_id = new_texture_id
            sprite_file.texture_data_dict[new_texture_id] = open(sprite_texture_path, 'rb').read()
            
    return sprite_file

def assemble_spr(path):
    sprite_extension = 'sprt'
    texture_extension = 'tmx'

    # inititialize spr
    sprite_file = spr()

    # get texture and sprite id list
    texture_ids = get_ids_from_filenames(path, 'tex', f'*.{texture_extension}')
    sprite_ids = get_ids_from_filenames(path, 'spr', f'*.{sprite_extension}')
    
    for id in texture_ids:
        texture_path = path + '\\' + f'tex_{id}.{texture_extension}'
        sprite_file.texture_data.append(tmx.read_from_buffer(open(texture_path, 'rb')))

    last_id = 0
    for id in sprite_ids:
        if id != last_id + 1:
            for i in range(0, id - last_id):
                sprite_file.sprite_list.append(spr_sprite_entry())
        last_id = id
                
        sprite_path = path + '\\' + f'spr_{id}.{sprite_extension}'
        sprite_texture_path = path + '\\' + f'spr_{id}.{texture_extension}'

        sprite_file.sprite_list.append(spr_sprite_entry.read_from_file(sprite_path))

        if os.path.isfile(sprite_texture_path):
            new_texture_id = len(sprite_file.texture_data)
            sprite_file.texture_data.append(tmx.read_from_buffer(open(sprite_texture_path, 'rb')))
            sprite_file.sprite_list[id].texture_index = new_texture_id
        
    return sprite_file
 
def assemble_sprite(path, file_type):
    sprite_file = None

    if file_type == 'spr':
        sprite_file = assemble_spr(path)
    elif file_type == 'spd':
        sprite_file = assemble_spd(path)
    else: 
        print("Invalid sprite archive file")
        return
   
    sprite_file.build(path + f'_out.{file_type}')

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

file_type: str

if len(sys.argv) == 1:
    print("missing spr path")
    exit()
elif len(sys.argv) == 2:
    file_type = input("input sprite file type (spd or spr): ")
else:
    file_type = sys.argv[2]

assemble_sprite(sys.argv[1], file_type)
