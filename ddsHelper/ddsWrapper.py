import os

def cut_image(image_path, x, y, width, height, output_path):
    # Cut the sprite out of the original texture and add padding 
    magick_command = f'magick {image_path} -crop {width}x{height}+{x}+{y} -background transparent -extent {round(width)}x{round(height)} {output_path}'
    os.system(magick_command)
