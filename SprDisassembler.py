import os
import sys
from Sprite.Spr.spr import spr
import multiprocessing 
import Sprite.utils as utils

def disassemble_spr_file(input_spr, output_folder, multiplier):
    # Set maximum processes. Change to 4 if you experience crashing
    MAX_PROCESSES = 1
    
    # Parse spr
    spr_data = spr.read_spr_file(input_spr)

    # Check if output path exists. Create it if it doesn't
    if not os.path.exists(output_folder):
        os.mkdir(output_folder, True)

    # write textures to output path
    for i in range(0, spr_data.header.texture_entry_count):
        write_tmx_to_file(spr_data.texture_data[i], f'{output_folder}\\tex_{i}.tmx')
        utils.convert_tmx_to_png(f'{output_folder}\\tex_{i}.tmx', f'{output_folder}\\tex_{i}.png')

    for i in range(0, spr_data.header.sprite_entry_count):
        export_sprite(i, spr_data.sprite_list[i], output_folder, multiplier)

def export_sprite(key, value, output_folder, multiplier = 1):
    print(f"Exporting sprite id {key}")

    # Prepare information to cut sprite from texture
    texture_path = f'{output_folder}\\tex_{value.texture_index}.png'
    texture_output = f'{output_folder}\\spr_{key}.png'

    # Cut sprite from texture
    utils.cut_from_image(texture_path, value.sprite_x_position * multiplier, value.sprite_y_position * multiplier, 
                         value.sprite_x_length * multiplier - value.sprite_x_position * multiplier,
                         value.sprite_y_length * multiplier - value.sprite_y_position * multiplier, 
                         texture_output)

    # Zero out sprite x and y
    value.sprite_x_length -= value.sprite_x_position
    value.sprite_y_length -= value.sprite_y_position
    value.sprite_x_position = 0
    value.sprite_y_position = 0

    # Write .sprt to file
    write_spr_to_file(value, f'{output_folder}\\spr_{key}.sprt')

def write_tmx_to_file(tmx, output_file):
    file = open(output_file, 'wb')
    tmx.write(file)
    file.close()

def write_spr_to_file(unpacked_spr, output_file):
    file = open(output_file, 'wb')
    unpacked_spr.write(file)
    file.close()

args = sys.argv

if args == 1:
    print("Usage: <input spr path> <output folder>\nYou may also drag a file on to the .py")
    exit() 

input_spr = args[1]

if len(args) > 2:
    output_folder = args[2]
else:
    output_folder = f'{os.path.splitext(input_spr)[0]}'

disassemble_spr_file(input_spr, output_folder, int(input("Enter the image scale multiplier (2 for p4gpc, 4 for p3ppc, 1 for psp/vita games): ")))
