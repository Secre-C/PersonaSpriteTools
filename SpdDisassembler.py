import os
import sys
from Sprite.Spd.spd import spd
import multiprocessing 
import Sprite.utils as utils


def disassemble_spd_file(input_spd, output_folder):
    # Set maximum processes. Change to 4 if you experience crashing
    MAX_PROCESSES = 8
    
    # Parse Spd
    spd_data = spd.read_spd_file(input_spd)

    # Check if output path exists. Create it if it doesn't
    if not os.path.exists(output_folder):
        os.mkdir(output_folder, True)

    # write textures to output path
    for key, value in spd_data.texture_data_dict.items():
        write_dds_to_file(value, f'{output_folder}\\tex_{key}.dds')
    
    # le epic chat gpt copy paste
    if __name__ == "__main__":
        # Write spdsprs to output path, and cut sprites from dds files
        with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
            # Use the map method to process each sprite in parallel
            results = []
            for key, value in spd_data.sprite_dict.items():
                result = pool.apply_async(export_sprite, (key, value, output_folder))
                results.append(result)

            # Wait for all processes to complete
            pool.close()
            pool.join()

            # Get any potesntial sexceptions raised by the processes
            for result in results:
                result.get()

def export_sprite(key, value, output_folder):
    print(f"Exporting sprite id {value.sprite_id}")

    # Prepare information to cut sprite from texture
    texture_path = f'{output_folder}\\tex_{value.sprite_texture_id}.dds'
    texture_output = f'{output_folder}\\spr_{value.sprite_id}.dds'

    # Cut sprite from texture
    utils.cut_from_image(texture_path, value.sprite_x_position, value.sprite_y_position, value.sprite_x_length, value.sprite_y_length, texture_output)

    # Zero out sprite x and y
    value.sprite_x_position = 0
    value.sprite_y_position = 0

    # Write spdspr to file
    write_spr_to_file(value, f'{output_folder}\\spr_{key}.spdspr')

def write_dds_to_file(dds_bytes, output_file):
    file = open(output_file, 'wb')
    file.write(dds_bytes)
    file.close()

def write_spr_to_file(unpacked_spr, output_file):
    file = open(output_file, 'wb')
    unpacked_spr.write(file)
    file.close()

args = sys.argv

if args == 1:
    print("Usage: <input spd path> <output folder>\nYou may also drag a file on to the .py file, but output will be the filepath + '_out'")
    exit() 

input_spd = args[1]

if len(args) > 2:
    output_folder = args[2]
else:
    output_folder = f'{os.path.splitext(input_spd)[0]}'

disassemble_spd_file(input_spd, output_folder)
