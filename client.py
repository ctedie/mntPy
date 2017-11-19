#!/usr/bin/env python

import socket
from ctypes import *


class MntFrameHeader(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("dest_address", c_uint8),
        ("source_address", c_uint8),
        ("frame_param", c_uint32),
        ("command", c_uint8),
        ("data_size", c_uint16),
    ]


class MntFrame(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("header", MntFrameHeader),
        ("data", c_uint8 * (1000 - sizeof(MntFrameHeader))),
    ]


TCP_IP = '192.168.0.12'
TCP_PORT = 1000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
mess = create_string_buffer(0x30, 1024)

test = c_uint16 * 5

frame = MntFrame()
ptData = pointer(frame.data)

print("taille de MntFrame : " + str(sizeof(MntFrame)))
print("taille de c_char_p : " + str(sizeof(c_char_p)))
print("Valeur de ptData : " + str(ptData))
print("adresse de ptData : " + hex(addressof(ptData)))
print("adresse de frame : " + hex(addressof(frame)))
print("adresse de frame.data : " + hex(addressof(frame.data)))

frame.header.dest_address = 2
frame.header.source_address = 170
frame.data[0] = 0x0C
frame.data[1] = 0xED
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(frame)
data = s.recv(BUFFER_SIZE)
s.close()


pass
