from struct import Struct
import os
import sys
from Sprite.Spr.tmx import tmx

# returns a tuple with the dds filesize, width, and height
def read_dds_metadata(image_path):
    dds_header = Struct("<5i")

    # Open dds file
    dds_file = open(image_path, 'rb')

    # Get the filesize of the dds
    filesize = len(dds_file.read())
    dds_file.seek(0)

    # Get width and height from the dds header
    unpacked_dds_header = dds_header.unpack(dds_file.read(0x14))
    width = unpacked_dds_header[4]
    height = unpacked_dds_header[3]

    return (filesize, width, height)

def read_tmx_metadata(image_path):
    with open(image_path, 'rb') as tmx_file:
        tmx_data = tmx.read_from_buffer(tmx_file)
        
        file_size = tmx_data.file_size
        width = tmx_data.width
        height = tmx_data.height

        return (file_size, width, height)

def convert_tmx_to_png(image_path, output_path):
    current_path = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\';
    tmx_converter = current_path + r"TmxToPng\TmxToPng.exe"

    print(tmx_converter)
    command = f'{tmx_converter} "{image_path}"'
    os.system(command)

def cut_from_image(image_path, x, y, width, height, output_path):
    # Cut the sprite out of the original texture and add padding 
    magick_command = f'magick "{image_path}" -crop {width}x{height}+{x}+{y} -background transparent -extent {round_up(width)}x{round_up(height)} "{output_path}"'
    os.system(magick_command)

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
