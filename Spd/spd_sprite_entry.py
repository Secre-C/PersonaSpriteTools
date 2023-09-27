from struct import Struct

class spd_sprite_entry:
    sprite_id: int
    sprite_texture_id: int
    unk08: int
    unk0c: int
    unk10: int
    unk14: int
    unk18: int
    unk1c: int
    sprite_x_position: int
    sprite_y_position: int
    sprite_x_length: int
    sprite_y_length: int
    unk30: int
    unk34: int
    sprite_x_scale: int
    sprite_y_scale: int
    unk40: int
    unk44: int
    unk48: int
    unk4c: int
    unk50: int
    unk54: int
    unk58: int
    unk5c: int
    unk60: int
    unk64: int
    unk68: int
    unk6c: int
    sprite_name: str  
    sprite_entry_struct = Struct('<28i48s')

    def __init__(self, file):
        sprite_entry_bytes = file.read(0xa0)
        unpacked_sprite_entry = self.sprite_entry_struct.unpack(sprite_entry_bytes)

        # initialize properties
        self.sprite_id = unpacked_sprite_entry[0]
        self.sprite_texture_id = unpacked_sprite_entry[1]
        self.unk08 = unpacked_sprite_entry[2]
        self.unk0c = unpacked_sprite_entry[3]
        self.unk10 = unpacked_sprite_entry[4]
        self.unk14 = unpacked_sprite_entry[5]
        self.unk18 = unpacked_sprite_entry[6]
        self.unk1c = unpacked_sprite_entry[7]
        self.sprite_x_position = unpacked_sprite_entry[8]
        self.sprite_y_position = unpacked_sprite_entry[9]
        self.sprite_x_length = unpacked_sprite_entry[10]
        self.sprite_y_length = unpacked_sprite_entry[11]
        self.unk30 = unpacked_sprite_entry[12]
        self.unk34 = unpacked_sprite_entry[13]
        self.sprite_x_scale = unpacked_sprite_entry[14]
        self.sprite_y_scale = unpacked_sprite_entry[15]
        self.unk40 = unpacked_sprite_entry[16]
        self.unk44 = unpacked_sprite_entry[17]
        self.unk48 = unpacked_sprite_entry[18]
        self.unk4c = unpacked_sprite_entry[19]
        self.unk50 = unpacked_sprite_entry[20]
        self.unk54 = unpacked_sprite_entry[21]
        self.unk58 = unpacked_sprite_entry[22]
        self.unk5c = unpacked_sprite_entry[23]
        self.unk60 = unpacked_sprite_entry[24]
        self.unk64 = unpacked_sprite_entry[25]
        self.unk68 = unpacked_sprite_entry[26]
        self.unk6c = unpacked_sprite_entry[27]
        self.sprite_name = unpacked_sprite_entry[28]

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
