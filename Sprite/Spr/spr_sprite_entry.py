from struct import Struct
from Sprite.Spr.spr_pointer_table import spr_pointer_table

class spr_sprite_entry:
    unk0x00: int = 0
    comment: str = b'spr_sprite' 
    texture_index: int = 0
    unk0x18: int = 4   # some sort of id?
    unk0x1C: int = 0
    unk0x20: int = 0
    unk0x24: int = 0
    unk0x28: int = 0
    unk0x2C: int = 0
    unk0x30: int = 0
    unk0x34: int = 0
    unk0x38: int = 0
    unk0x3C: int = 0
    unk0x40: int = 0   # set in 'center' frames?
    offset_x: int = 0
    offset_y: int = 0
    unk0x4C: int = 0
    unk0x50: int = 0
    sprite_x_position: int = 0
    sprite_y_position: int = 0
    sprite_x_length: int = 0
    sprite_y_length: int = 0
    unk0x64: int = 0x80808080   # argb color
    unk0x68: int = 0x80808080   # argb color
    unk0x6C: int = 0x80808080   # argb color
    unk0x70: int = 0x80808080   # argb color
    unk0x74: int = 0   # possibly padding
    unk0x78: int = 0   # possibly padding
    unk0x7C: int = 0   # possibly padding

    sprite_entry_struct = Struct('<i16s27I')

    @classmethod
    def read_from_buffer(cls, file):
        unpacked_sprite_entry = cls.sprite_entry_struct.unpack(file.read(0x80))

        this = cls()

        cls.populateMembers(this, unpacked_sprite_entry)
        
        return this

    @classmethod
    def read_from_file(cls, path):
        unpacked_sprite_entry = cls.sprite_entry_struct.unpack(open(path, 'rb').read())

        this = cls()
        cls.populateMembers(this, unpacked_sprite_entry)
        return this
                
    def write(self, file):
        entry_bytes = self.sprite_entry_struct.pack(
            self.unk0x00,
            self.comment,
            self.texture_index,
            self.unk0x18,
            self.unk0x1C,
            self.unk0x20,
            self.unk0x24,
            self.unk0x28,
            self.unk0x2C,
            self.unk0x30,
            self.unk0x34,
            self.unk0x38,
            self.unk0x3C,
            self.unk0x40,
            self.offset_x,
            self.offset_y,
            self.unk0x4C,
            self.unk0x50,
            self.sprite_x_position,
            self.sprite_y_position,
            self.sprite_x_length,
            self.sprite_y_length,
            self.unk0x64,
            self.unk0x68,
            self.unk0x6C,
            self.unk0x70,
            self.unk0x74,
            self.unk0x78,
            self.unk0x7C
        )

        file.write(entry_bytes)

    def populateMembers(cls, unpacked_sprite_entry):
        cls.unk0x00 = unpacked_sprite_entry[0]
        cls.comment = unpacked_sprite_entry[1]
        cls.texture_index = unpacked_sprite_entry[2]
        cls.unk0x18 = unpacked_sprite_entry[3]
        cls.unk0x1C = unpacked_sprite_entry[4]
        cls.unk0x20 = unpacked_sprite_entry[5]
        cls.unk0x24 = unpacked_sprite_entry[6]
        cls.unk0x28 = unpacked_sprite_entry[7]
        cls.unk0x2C = unpacked_sprite_entry[8]
        cls.unk0x30 = unpacked_sprite_entry[9]
        cls.unk0x34 = unpacked_sprite_entry[10]
        cls.unk0x38 = unpacked_sprite_entry[11]
        cls.unk0x3C = unpacked_sprite_entry[12]
        cls.unk0x40 = unpacked_sprite_entry[13]
        cls.offset_x = unpacked_sprite_entry[14]
        cls.offset_y = unpacked_sprite_entry[15]
        cls.unk0x4C = unpacked_sprite_entry[16]
        cls.unk0x50 = unpacked_sprite_entry[17]
        cls.sprite_x_position = unpacked_sprite_entry[18]
        cls.sprite_y_position = unpacked_sprite_entry[19]
        cls.sprite_x_length = unpacked_sprite_entry[20]
        cls.sprite_y_length = unpacked_sprite_entry[21]
        cls.unk0x64 = unpacked_sprite_entry[22]
        cls.unk0x68 = unpacked_sprite_entry[23]
        cls.unk0x6C = unpacked_sprite_entry[24]
        cls.unk0x70 = unpacked_sprite_entry[25]
        cls.unk0x74 = unpacked_sprite_entry[26]
        cls.unk0x78 = unpacked_sprite_entry[27]
        cls.unk0x7C = unpacked_sprite_entry[28]
