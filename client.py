#!/usr/bin/env python

import socket
from ctypes import *


class MntFrame(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("source_address", c_uint8),
        ("dest_address", c_uint8),
        ("frame_param", c_uint32),
        ("command", c_uint8),
        ("data_size", c_uint16),
        ("data", c_char_p)
    ]

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
mess = create_string_buffer(0x30, 1024)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))
# s.send(MESSAGE)
# data = s.recv(BUFFER_SIZE)
# s.close()

frame = MntFrame(0, 0, 0, 0, 0, 0)

frame.data = addressof(mess)
print("taille de MntFrame : " + str(sizeof(MntFrame)))
print("taille de c_char_p : " + str(sizeof(c_char_p)))
print("Valeur de c_char_p : " + str(frame.data))


