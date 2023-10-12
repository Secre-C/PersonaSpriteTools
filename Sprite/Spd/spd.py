from Sprite.Spd.spd_header import spd_header
from Sprite.Spd.spd_texture_entry import spd_texture_entry
from Sprite.Spd.spd_sprite_entry import spd_sprite_entry
from collections import OrderedDict

class spd:
    header: spd_header = {}
    texture_dict: OrderedDict = {}
    sprite_dict: OrderedDict = {}
    texture_data_dict: OrderedDict = {}

    @classmethod
    def read_spd_file(cls, file_path: str):
        # Open Spd file and read the header
        spd_file = open(file_path, 'rb')
        cls.header = spd_header.read_from_buffer(spd_file)

        # Initialize dictionaries
        cls.texture_dict = {}
        cls.sprite_dict = {}
        cls.texture_data_dict = {}

        # Populate texture entry dictionary
        for i in range(0, cls.header.texture_entry_count):
            texture_entry = spd_texture_entry.read_from_buffer(spd_file)
            cls.texture_dict[texture_entry.texture_id] = texture_entry
        
        # Populate sprite entry dictionary
        for i in range(0, cls.header.sprite_entry_count):
            sprite_entry = spd_sprite_entry.read_from_buffer(spd_file)
            cls.sprite_dict[sprite_entry.sprite_id] = sprite_entry

        # Populate texture data dictionary
        for key, value in cls.texture_dict.items():
            spd_file.seek(value.texture_data_offset)
            texture_data_bytes = spd_file.read()
            cls.texture_data_dict[key] = texture_data_bytes

        return cls

    def build(self, output_path):
        # constants
        HEADER_SIZE = 0x20
        TEXTURE_ENTRY_SIZE = 0x30
        SPRITE_ENTRY_SIZE = 0xa0
        
        # Create a new file
        file = open(output_path, 'wb')

        # Build the header
        header = spd_header()
        header.texture_entry_count = len(self.texture_dict)
        header.sprite_entry_count = len(self.sprite_dict)
        header.texture_entry_start_offset = HEADER_SIZE 
        header.sprite_entry_start_offset = HEADER_SIZE + (TEXTURE_ENTRY_SIZE * header.texture_entry_count) 
        texture_data_start_offset = header.sprite_entry_start_offset + (SPRITE_ENTRY_SIZE * header.sprite_entry_count)

        # Write header to file
        header.write(file)

        # Write texture entries
        for value in self.texture_dict.values():
            value.texture_data_offset = texture_data_start_offset
            texture_data_start_offset = texture_data_start_offset + value.texture_data_size
            value.write(file)

        # Write sprite entries
        for value in self.sprite_dict.values():
            value.write(file)

        # Write texture data
        for value in self.texture_data_dict.values():
            file.write(value) 
        
        file.close()
