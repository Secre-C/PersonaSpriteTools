from Spd.spd_header import spd_header
from Spd.spd_texture_entry import spd_texture_entry
from Spd.spd_sprite_entry import spd_sprite_entry
from collections import OrderedDict

class spd:
    header: spd_header
    texture_dict: OrderedDict
    sprite_dict: OrderedDict
    texture_data_dict: OrderedDict

    def __init__(self, file_path: str):
        # Open Spd file and read the header
        spd_file = open(file_path, 'rb')
        self.header = spd_header(spd_file)

        # Initialize dictionaries
        self.texture_dict = {}
        self.sprite_dict = {}
        self.texture_data_dict = {}

        # Populate texture entry dictionary
        for i in range(0, self.header.texture_entry_count):
            texture_entry = spd_texture_entry(spd_file)
            self.texture_dict[texture_entry.texture_id] = texture_entry
        
        # Populate sprite entry dictionary
        for i in range(0, self.header.sprite_entry_count):
            sprite_entry = spd_sprite_entry(spd_file)
            self.sprite_dict[sprite_entry.sprite_id] = sprite_entry

        # Populate texture data dictionary
        for key, value in self.texture_dict.items():
            spd_file.seek(value.texture_data_offset)
            texture_data_bytes = spd_file.read(value.texture_data_size)
            self.texture_data_dict[key] = texture_data_bytes