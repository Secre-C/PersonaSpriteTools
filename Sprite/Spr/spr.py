from Sprite.Spr.spr_header import spr_header
from Sprite.Spr.spr_sprite_entry import spr_sprite_entry
from Sprite.Spr.spr_pointer_table import spr_pointer_table
from Sprite.Spr.tmx import tmx
from collections import OrderedDict

class spr:
    header: spr_header
    texture_pointers: list = []
    sprite_pointers: list = []
    texture_list: list = []
    sprite_list: list = [] 
    texture_data: list = [] 

    @classmethod
    def read_spr_file(cls, file_path: str):
        # Open spr file and read the header
        spr_file = open(file_path, 'rb')
        cls.header = spr_header.read_from_buffer(spr_file)

        # read texture entry pointers 
        spr_file.seek(cls.header.texture_entry_start_offset)
        for i in range(0, cls.header.texture_entry_count):
            cls.texture_pointers.append(spr_pointer_table.read_from_buffer(spr_file))
        
        # read sprite entry pointers 
        spr_file.seek(cls.header.sprite_entry_start_offset)
        for i in range(0, cls.header.sprite_entry_count):
            cls.sprite_pointers.append(spr_pointer_table.read_from_buffer(spr_file))

        # Populate sprite entry list 
        for i in range(0, cls.header.sprite_entry_count):
            spr_file.seek(cls.sprite_pointers[i].offset)
            cls.sprite_list.append(spr_sprite_entry.read_from_buffer(spr_file))

        # Populate texture data 
        for i in range(0, cls.header.texture_entry_count):
            spr_file.seek(cls.texture_pointers[i].offset)
            cls.texture_data.append(tmx.read_from_buffer(spr_file))

        return cls

    def build(self, output_path):
        # constants
        HEADER_SIZE = 0x20
        SPRITE_ENTRY_SIZE = 0x80
        
        # Create a new file
        # Build the header
        header = spr_header()
        header.texture_entry_count = len(self.texture_list)
        header.sprite_entry_count = len(self.sprite_list)
        header.texture_entry_start_offset = HEADER_SIZE 
        header.sprite_entry_start_offset = HEADER_SIZE + (TEXTURE_ENTRY_SIZE * header.texture_entry_count) 
        texture_data_start_offset = header.sprite_entry_start_offset + (SPRITE_ENTRY_SIZE * header.sprite_entry_count)

        # Write header to file
        header.write(file)

        # Write texture entries
        for key, value in self.texture_list.items():
            value.texture_data_offset = texture_data_start_offset
            texture_data_start_offset = texture_data_start_offset + value.texture_data_size
            value.write(file)

        # Write sprite entries
        for key, value in self.sprite_list.items():
            value.write(file)

        # Write texture data
        for key, value in self.texture_data_dict.items():
            file.write(value) 
 