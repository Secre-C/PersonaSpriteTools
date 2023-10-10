import utils, os, glob

input_path = ".\\input"
output_path = ".\\unpacked"
for x in os.listdir(input_path):
    full_input_path = os.path.join(input_path, x)
    full_output_path = os.path.join(output_path, x)
    output, err = utils.unpack_bin_to_folder(full_input_path, full_output_path)
    output = output.decode().split("\n")
    pak_version = output[0]
    pak_version = pak_version[pak_version.index(": ") + 2:].strip()
    os.rename(full_output_path, "%s_%s" % (full_output_path, pak_version))

for x in glob.glob(os.path.join(output_path, "**/*.tmx")):
    output_dir = x.replace(".tmx", ".png")
    utils.convert_tmx_to_png(x, output_dir)
    os.remove(x)