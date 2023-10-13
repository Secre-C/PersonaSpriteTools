import os
import sys
import glob
from pathlib import Path

from Sprite.Spd.spd import spd
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry
from Sprite.Spd.spd_texture_entry import spd_texture_entry

from Sprite.Spr.spr import spr
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry
from Sprite.Spr.tmx import tmx

def PatchSpriteFile(original_sprite_path, new_sprites):
    ext = os.path.splitext(original_sprite_path) 

    patched_sprite_file = None

    if ext[1].lower().endswith('spr'):
        patched_sprite_file = PatchSprFile(original_sprite_path, new_sprites)
    elif ext[1].lower().endswith('spd'):
        patched_sprite_file = PatchSpdFile(original_sprite_path, new_sprites)
    else:
        print("Invalid file type")
        return

    patched_sprite_file.build(patched_sprite_file, ext[0] + f'_out{ext[1]}')

def PatchSpdFile(original_spd_path, new_sprites):
    original_sprite = spd.read_file(original_spd_path) 
    
    sprite_entry_ids = get_ids_from_filenames(new_sprites, 'spr', 'spdspr')
    sprite_texture_ids = get_ids_from_filenames(new_sprites, 'spr', 'dds')
    texture_ids = get_ids_from_filenames(new_sprites, 'tex', 'dds')

    for id_set in texture_ids.values():
        id = id_set[0]
        print(f'Replacing texture id {id}')
        texture_path = new_sprites + f'\\tex_{id}.dds' 
        original_sprite.texture_dict[id] = spd_texture_entry.create(id, f'texture_{id}', texture_path)
        original_sprite.texture_data_dict[id] = open(texture_path, 'rb').read()

    for id_set in sprite_entry_ids.values(): 
        id = id_set[0]
        sprite_path = new_sprites + f'\\spr_{id}.spdspr'
        sprite_entry = spd_sprite_entry.read_from_file(sprite_path)
        id = sprite_entry.sprite_id
        print(f'Injecting sprite id {id}')
        original_sprite.sprite_dict[id] = sprite_entry 
        
    for file, id in sprite_texture_ids.items():
        next_id = max(original_sprite.texture_dict.keys()) + 1
        print(f"Injecting texture id {next_id}")
        texture_path = file
        original_sprite.texture_dict[next_id] = spd_texture_entry.create(next_id, f'spr_{id[0]}', texture_path)
        original_sprite.texture_data_dict[next_id] = open(texture_path, 'rb').read()
        for i in id:
            original_sprite.sprite_dict[i].sprite_texture_id = next_id

    return original_sprite

def PatchSprFile(original_spr_path, new_sprites):
    original_sprite = spr.read_file(original_spr_path) 
    
    sprite_entries = get_ids_from_filenames(new_sprites, 'spr', 'sprt')
    sprite_textures = get_ids_from_filenames(new_sprites, 'spr', 'tmx')
    textures = get_ids_from_filenames(new_sprites, 'tex', 'tmx')

    for id_set in textures.values():
        id = id_set[0]
        texture_path = new_sprites + f'\\tex_{id}.tmx'

        if id >= len(original_sprite.texture_data):
            Print("Invalid Id, cannot append sprites using the 'tex_' prefix. Skipping...")
            continue

        print(f'Replacing texture index {id}')
        original_sprite.texture_data[id] = tmx.read_from_buffer(open(texture_path, 'rb'))

    for id_set in sprite_entries.values(): 
        id = id_set[0]
        if id >= len(original_sprite.sprite_list):
            for i in range(id, len(original_sprite.sprite_list)):
                original_sprite.sprite_list.append(spr_sprite_entry())

        print(f'Injecting sprite index {id}')
        sprite_path = new_sprites + f'\\spr_{id}.sprt'
        original_sprite.sprite_list[id] = spr_sprite_entry.read_from_file(sprite_path)
        
    print(len(sprite_textures))
    for file, id in sprite_textures.items():
        next_id = len(original_sprite.texture_data)

        print(f'Injecting texture index {next_id}')
        texture_path = file
        original_sprite.texture_data.append(tmx.read_from_buffer(open(texture_path, 'rb')))
        for i in id:
            if i >= len(original_sprite.sprite_list):
                Print(f"Tried to patch nonexisted sprite id {i}. Skipping...")
                continue
            original_sprite.sprite_list[i].texture_index = next_id

    return original_sprite

def get_ids_from_filenames(path, prefix, extension):
    # Path to files with texture extension
    file_path = path + '\\*.' + extension
    
    files = glob.glob(file_path)
    
    file_path = dict()

    for file in files:
        if not Path(file).stem.startswith(prefix):
            continue

        file_path[file] = []
        for ids in Path(file).stem[4:].split('_'): 
            if '-' in ids:
                id_range = ids.split('-')
                for i in range(int(id_range[0]), int(id_range[1]) + 1):
                    file_path[file].append(i)
            else:
                file_path[file].append(int(ids)) 

    return file_path

PatchSpriteFile(sys.argv[1], sys.argv[2])
