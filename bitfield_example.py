import ctypes


c_uint8 = ctypes.c_uint8

class Flags_bits(ctypes.LittleEndianStructure):
    _fields_ = [
            ("logout", c_uint8, 1),
            ("userswitch", c_uint8, 1),
            ("suspend", c_uint8, 1),
            ("idle", c_uint8, 1),
        ]

class Flags(ctypes.Union):
    _fields_ = [("b", Flags_bits),
                ("asbyte", c_uint8)]

flags = Flags()
flags.asbyte = 0x1

print("logout : " + str(flags.b.logout))
print("userswitch : " + str(flags.b.userswitch))
print("suspend : " + str(flags.b.suspend))
print("idle : " + str(flags.b.idle))
print('==> All : ' + hex(flags.asbyte))
