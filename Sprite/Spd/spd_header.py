from struct import Struct

class spd_header:
    magic: int = 0x30525053
    unk04: int = 2
    file_size: int = 0
    unk0c: int = 0
    unk10: int = 0
    texture_entry_count: int = 0
    sprite_entry_count: int = 0
    texture_entry_start_offset: int = 0
    sprite_entry_start_offset: int = 0
    header_struct = Struct('<5i2h2i')

    @classmethod
    def read_from_buffer(cls, file):
        header_bytes = file.read(0x20)
        unpacked_header = cls.header_struct.unpack(header_bytes)

        # Create a new instance of spd_header
        new_cls = cls()

        # initialize class properties
        new_cls.magic = unpacked_header[0]
        new_cls.unk04 = unpacked_header[1]
        new_cls.file_size = unpacked_header[2]
        new_cls.unk0c = unpacked_header[3]
        new_cls.unk10 = unpacked_header[4]
        new_cls.texture_entry_count = unpacked_header[5]
        new_cls.sprite_entry_count = unpacked_header[6]
        new_cls.texture_entry_start_offset = unpacked_header[7]
        new_cls.sprite_entry_start_offset = unpacked_header[8]

        return new_cls 

    def write(self, file):
        packed_header = self.header_struct.pack(
                self.magic,
                self.unk04,
                self.file_size,
                self.unk0c,
                self.unk10,
                self.texture_entry_count,
                self.sprite_entry_count,
                self.texture_entry_start_offset,
                self.sprite_entry_start_offset
        ) 

        file.write(packed_header)
