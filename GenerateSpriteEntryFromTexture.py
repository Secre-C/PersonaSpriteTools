import Sprite.utils as utils
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry
from Sprite.Spr.tmx import tmx
import os
import sys

def GenerateSpdSprite(dds_path, sprite_id, scale_multiplier):
    sprite = spd_sprite_entry()

    metadata = utils.read_dds_metadata(dds_path)

    sprite.sprite_id = sprite_id
    sprite.sprite_x_position = 0   
    sprite.sprite_y_position = 0   
    sprite.sprite_x_length = metadata[1]
    sprite.sprite_y_length = metadata[2]
    sprite.sprite_x_scale = int(metadata[1] / scale_multiplier)
    sprite.sprite_y_scale = int(metadata[2] / scale_multiplier)

    spd = open(os.path.splitext(dds_path)[0] + '.spdspr', 'wb')
    sprite.write(spd)
    spd.close()

def GenerateSprSprite(tmx_path, scale_multiplier):
    sprite = spr_sprite_entry()
    
    tmx_metadata = utils.read_tmx_metadata(tmx_path) 

    sprite.sprite_x_position = 0   
    sprite.sprite_y_position = 0   
    sprite.sprite_x_length = int(tmx_metadata[1] / scale_multiplier)
    sprite.sprite_y_length = int(tmx_metadata[2] / scale_multiplier)

    spr = open(os.path.splitext(tmx_path)[0] + '.sprt', 'wb')
    sprite.write(spr)
    
args = sys.argv
del args[0]

for arg in args:
    if os.path.splitext(arg)[1].lower() == '.dds':
        GenerateSpdSprite(arg, int(input(f'input the id of the generated sprite: ')),
                          int(input(f'input the sprite scale mulitplier (2 for p5rpc, 1 for every other version of p5/r): ')))
    elif os.path.splitext(arg)[1] == '.tmx':
        GenerateSprSprite(arg, int(input('input the sprite scale divisor (2 for p4gpc, 4 for p3ppc, 1 for psp/vita): '))) 
