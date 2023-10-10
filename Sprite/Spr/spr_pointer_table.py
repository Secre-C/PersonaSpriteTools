from struct import Struct

class spr_pointer_table:
    unk00: int = 0
    offset: int = 0

    spr_pointer_table_struct = Struct('<2i')

    @classmethod
    def read_from_buffer(cls, file):
        pointer_entry = cls.spr_pointer_table_struct.unpack(file.read(8))

        this = cls()

        this.unk00 = pointer_entry[0]
        this.offset = pointer_entry[1]

        return this 

    def write(self, file):
        pointer_bytes = self.spr_pointer_table_struct.pack(self.unk00, self.offset)
        file.write(pointer_bytes)
