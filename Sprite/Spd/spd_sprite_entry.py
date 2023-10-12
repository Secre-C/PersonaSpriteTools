from struct import Struct

class spd_sprite_entry:
    sprite_id: int = 0
    sprite_texture_id: int = 0
    unk08: int = 0
    unk0c: int = 0
    unk10: int = 0
    unk14: int = 0
    unk18: int = 0
    unk1c: int = 0
    sprite_x_position: int = 0
    sprite_y_position: int = 0
    sprite_x_length: int = 0
    sprite_y_length: int = 0
    unk30: int = 0
    unk34: int = 0
    sprite_x_scale: int = 0
    sprite_y_scale: int = 0
    unk40: int = 0
    unk44: int = 0
    unk48: int = 0
    unk4c: int = 0
    unk50: int = 0xffffffff
    unk54: int = 0xffffffff
    unk58: int = 0xffffffff
    unk5c: int = 0xffffffff
    unk60: int = 0
    unk64: int = 0
    unk68: int = 0
    unk6c: int = 0
    sprite_name: str = b'spd_sprite'  
    sprite_entry_struct = Struct('<28I48s')

    @classmethod
    def read_from_buffer(cls, file):
        sprite_entry_bytes = file.read(0xa0)
        unpacked_sprite_entry = cls.sprite_entry_struct.unpack(sprite_entry_bytes)

        # create new class instance
        new_cls = cls()

        # initialize properties
        cls.populate_members(new_cls, unpacked_sprite_entry)  
        return new_cls

    @classmethod
    def read_from_file(cls, path):
        unpacked_sprite = cls.sprite_entry_struct.unpack(open(path, 'rb').read())
        new_cls = cls()

        cls.populate_members(new_cls, unpacked_sprite)
        return new_cls

    def write(self, file):
        packed_entry = self.sprite_entry_struct.pack(
                self.sprite_id,
                self.sprite_texture_id,
                self.unk08,
                self.unk0c,
                self.unk10,
                self.unk14,
                self.unk18,
                self.unk1c,
                self.sprite_x_position,
                self.sprite_y_position,
                self.sprite_x_length,
                self.sprite_y_length,
                self.unk30,
                self.unk34,
                self.sprite_x_scale,
                self.sprite_y_scale,
                self.unk40,
                self.unk44,
                self.unk48,
                self.unk4c,
                self.unk50,
                self.unk54,
                self.unk58,
                self.unk5c,
                self.unk60,
                self.unk64,
                self.unk68,
                self.unk6c,
                self.sprite_name
        )

        file.write(packed_entry)

    def populate_members(cls, unpacked_sprite_entry):
        cls.sprite_id = unpacked_sprite_entry[0]
        cls.sprite_texture_id = unpacked_sprite_entry[1]
        cls.unk08 = unpacked_sprite_entry[2]
        cls.unk0c = unpacked_sprite_entry[3]
        cls.unk10 = unpacked_sprite_entry[4]
        cls.unk14 = unpacked_sprite_entry[5]
        cls.unk18 = unpacked_sprite_entry[6]
        cls.unk1c = unpacked_sprite_entry[7]
        cls.sprite_x_position = unpacked_sprite_entry[8]
        cls.sprite_y_position = unpacked_sprite_entry[9]
        cls.sprite_x_length = unpacked_sprite_entry[10]
        cls.sprite_y_length = unpacked_sprite_entry[11]
        cls.unk30 = unpacked_sprite_entry[12]
        cls.unk34 = unpacked_sprite_entry[13]
        cls.sprite_x_scale = unpacked_sprite_entry[14]
        cls.sprite_y_scale = unpacked_sprite_entry[15]
        cls.unk40 = unpacked_sprite_entry[16]
        cls.unk44 = unpacked_sprite_entry[17]
        cls.unk48 = unpacked_sprite_entry[18]
        cls.unk4c = unpacked_sprite_entry[19]
        cls.unk50 = unpacked_sprite_entry[20]
        cls.unk54 = unpacked_sprite_entry[21]
        cls.unk58 = unpacked_sprite_entry[22]
        cls.unk5c = unpacked_sprite_entry[23]
        cls.unk60 = unpacked_sprite_entry[24]
        cls.unk64 = unpacked_sprite_entry[25]
        cls.unk68 = unpacked_sprite_entry[26]
        cls.unk6c = unpacked_sprite_entry[27]
        cls.sprite_name = unpacked_sprite_entry[28]
