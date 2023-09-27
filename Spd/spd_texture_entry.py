from struct import Struct

class spd_texture_entry:
    texture_id: int
    unk04: int = 0
    texture_data_offset: int
    texture_data_size: int
    texture_width: int
    texture_height: int
    unk18: int
    unk1c: int
    description: str
    texture_entry_struct = Struct('<8i16s')

    def __init__(self, file):
        texture_entry_bytes = file.read(0x30)
        unpacked_texture_entry = self.texture_entry_struct.unpack(texture_entry_bytes)

        # initialize class properties
        self.texture_id = unpacked_texture_entry[0]
        self.unk04 = unpacked_texture_entry[1]
        self.texture_data_offset = unpacked_texture_entry[2]
        self.texture_data_size = unpacked_texture_entry[3]
        self.texture_width = unpacked_texture_entry[4]
        self.texture_height = unpacked_texture_entry[5]
        self.unk18 = unpacked_texture_entry[6]
        self.unk1c = unpacked_texture_entry[7]
        self.description = unpacked_texture_entry[8]

    def write(self, file):
        packed_entry = self.texture_entry_struct.pack(
            self.texture_id,
            self.unk04,
            self.texture_data_offset,
            self.texture_data_size,
            self.texture_width,
            self.texture_height,
            self.unk18,
            self.unk1c,
            self.description
        )
