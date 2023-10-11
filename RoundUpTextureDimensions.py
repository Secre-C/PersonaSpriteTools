import Sprite.utils as utils
import sys

def round_up_dds_dimensions(dds_path):
    dimensions = utils.read_dds_metadata(dds_path)
    utils.cut_from_image(dds_path, 0, 0, dimensions[1], dimensions[2], dds_path)

args = sys.argv

for i in range(1, len(args)):
    round_up_dds_dimensions(args[i])
