from struct import Struct

class spr_header:
    flags: int = 1 #00
    user_id: int = 0 #02
    reserved1: int = 0 # 04
    magic: int = 0x30525053 # 08
    header_size: int = 0 # 0c 
    file_size: int = 0 # 10
    texture_entry_count: int = 0 # 14
    sprite_entry_count: int = 0 # 16
    texture_entry_start_offset: int = 0 # 18
    sprite_entry_start_offset: int = 0 # 1c
    header_struct = Struct('<2h4i2h2i')

    @classmethod
    def read_from_buffer(cls, file):
        header_bytes = file.read(0x20)
        unpacked_header = cls.header_struct.unpack(header_bytes)

        # Create a new instance of spr_header
        this = cls()

        # initialize class properties
        this.flags = unpacked_header[0]
        this.user_id = unpacked_header[1]
        this.reserved1 = unpacked_header[2]
        this.magic = unpacked_header[3]
        this.header_size = unpacked_header[4]
        this.file_size = unpacked_header[5]
        this.texture_entry_count = unpacked_header[6]
        this.sprite_entry_count = unpacked_header[7]
        this.texture_entry_start_offset = unpacked_header[8]
        this.sprite_entry_start_offset = unpacked_header[9]

        return this 

    def write(self, file):
        packed_header = self.header_struct.pack(
                self.flags,
                self.user_id,
                self.reserved1,
                self.magic,
                self.header_size,
                self.file_size,
                self.texture_entry_count,
                self.sprite_entry_count,
                self.texture_entry_start_offset,
                self.sprite_entry_start_offset   
) 

        file.write(packed_header)
