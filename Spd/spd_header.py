from struct import Struct

class spd_header:
    magic: int
    unk04: int = 2
    file_size: int
    unk0c: int = 0
    unk10: int = 0
    texture_entry_count: int
    sprite_entry_count: int
    texture_entry_start_offset: int
    sprite_entry_start_offset: int

    def __init__(self, file):
        header_struct = Struct('<5i2h2i')
        header_bytes = file.read(0x20)
        unpacked_header = header_struct.unpack(header_bytes)

        # initialize class properties
        self.magic = unpacked_header[0]
        self.unk04 = unpacked_header[1]
        self.file_size = unpacked_header[2]
        self.unk0c = unpacked_header[3]
        self.unk10 = unpacked_header[4]
        self.texture_entry_count = unpacked_header[5]
        self.sprite_entry_count = unpacked_header[6]
        self.texture_entry_start_offset = unpacked_header[7]
        self.texture_entry_start_offset = unpacked_header[8]