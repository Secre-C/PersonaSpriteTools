import os
import sys
from Spd.spd import spd

def disassemble_spd_file(input_spd, output_folder):
    # Parse Spd
    spd_data = spd(input_spd)

    # Check if output path exists. Create it if it doesn't
    if not os.path.exists(output_folder):
        os.mkdir(output_folder, True)

    # write textures to output path
    for key, value in spd_data.texture_data_dict.items():
        write_dds_to_file(value, f'{output_folder}\\tex_{key}.dds')

    # Write spdsprs to output path, and cut sprites from dds files
    for key, value in spd_data.sprite_dict.items():
        print(f"Exporting sprite id {value.sprite_id}")

        # prepare information to cut sprite from texture 
        texture_path = f'{output_folder}\\tex_{value.sprite_texture_id}.dds'
        texture_output = f'{output_folder}\\spr_{value.sprite_id}.dds'

        # cut sprite from texture
        cut_image(texture_path, value.sprite_x_position, value.sprite_y_position, value.sprite_x_length, value.sprite_y_length, texture_output)

        # zero out sprite x and y 
        value.sprite_x_position = 0
        value.sprite_y_position = 0

        # write spdspr to file
        write_spr_to_file(value, f'{output_folder}\\spr_{key}.spdspr') 

def write_dds_to_file(dds_bytes, output_file):
    file = open(output_file, 'wb')
    file.write(dds_bytes)
    file.close()

def write_spr_to_file(unpacked_spr, output_file):
    file = open(output_file, 'wb')
    unpacked_spr.write(file)
    file.close()

# Recursive (cuz I like suffering) function that rounds up an integer to a number that won't crash p5r
def round_up(length, starting_num = 1):
    # compare the length to 2^n
    if length > starting_num: 
        # if it's larger, compare the length to 2^n plus 2^(n-1)
        if length > (starting_num | starting_num >> 1):
            # if it's still larger, increase the starting exponent and recurse
            return round_up(length, starting_num << 1)
        # return 2^n + 2^(n-1)
        return (starting_num | starting_num >> 1)
    # return 2^n
    return starting_num

def cut_image(image_path, x, y, width, height, output_path):
    # Cut the sprite out of the original texture and add padding 
    magick_command = f'magick "{image_path}" -crop {width}x{height}+{x}+{y} -background transparent -extent {round_up(width)}x{round_up(height)} "{output_path}"'
    os.system(magick_command)

args = sys.argv

if args == 1:
    print("Usage: <input spd path> <output folder>\nYou may also drag a file on to the .py file, but output will be the filepath + '_out'")
    exit() 

input_spd = args[1]

if len(args) > 2:
    output_folder = args[2]
else:
    output_folder = f'{input_spd}_out'

disassemble_spd_file(input_spd, output_folder)
    
