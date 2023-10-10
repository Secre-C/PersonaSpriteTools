from struct import Struct

class tmx:
    unk00: int
    unk02: int
    file_size: int
    magic: int
    unk0c: int
    unk10: int
    width: int
    height: int
    unk16: int
    unk18: int
    unk1c: int
    tmx_data = None
    tmx_header_struct = Struct('<2h3i4h2i')

    @classmethod
    def read_from_buffer(cls, file):
        unpacked_header = cls.tmx_header_struct.unpack(file.read(0x20))

        this = cls()

        this.unk00 = unpacked_header[0]
        this.unk02 = unpacked_header[1]
        this.file_size = unpacked_header[2]
        this.magic = unpacked_header[3]
        this.unk0c = unpacked_header[4]
        this.unk10 = unpacked_header[5]
        this.width = unpacked_header[6]
        this.height = unpacked_header[7]
        this.unk16 = unpacked_header[8]
        this.unk18 = unpacked_header[9]
        this.unk1c = unpacked_header[10]

        this.tmx_data = file.read(this.file_size - 0x20)

        return this

    def write(self, file):
        header_bytes = self.tmx_header_struct.pack(
            self.unk00,
            self.unk02,
            self.file_size,
            self.magic,
            self.unk0c,
            self.unk10,
            self.width,
            self.height,
            self.unk16,
            self.unk18,
            self.unk1c
        )

        file.write(header_bytes)
        file.write(self.tmx_data)
