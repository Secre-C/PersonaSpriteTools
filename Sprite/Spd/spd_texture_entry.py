from struct import Struct
import Sprite.utils 

class spd_texture_entry:
    texture_id: int
    unk04: int = 0
    texture_data_offset: int = 0
    texture_data_size: int = 0
    texture_width: int = 0
    texture_height: int = 0
    unk18: int = 0
    unk1c: int = 0
    description: str
    texture_entry_struct = Struct('<8i16s')

    @classmethod
    def read_from_buffer(cls, file):
        texture_entry_bytes = file.read(0x30)
        unpacked_texture_entry = cls.texture_entry_struct.unpack(texture_entry_bytes)

        # create a new class instance
        new_cls = cls()

        # initialize class properties
        new_cls.texture_id = unpacked_texture_entry[0]
        new_cls.unk04 = unpacked_texture_entry[1]
        new_cls.texture_data_offset = unpacked_texture_entry[2]
        new_cls.texture_data_size = unpacked_texture_entry[3]
        new_cls.texture_width = unpacked_texture_entry[4]
        new_cls.texture_height = unpacked_texture_entry[5]
        new_cls.unk18 = unpacked_texture_entry[6]
        new_cls.unk1c = unpacked_texture_entry[7]
        new_cls.description = unpacked_texture_entry[8]
        return new_cls

    @classmethod
    def create(cls, id, description: str, image_path: str):
        # create a new class instance
        new_cls = cls()

        new_cls.texture_id = id
        new_cls.description = description.ljust(0x10)
        (filesize, width, height) = utils.read_dds_metadata(image_path)
        new_cls.texture_data_size = filesize
        new_cls.texture_width = width
        new_cls.texture_height = height
        return new_cls

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

        file.write(packed_entry)
