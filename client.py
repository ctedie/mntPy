# -*- coding:utf-8 -*-
# #!/usr/bin/env python

import socket
from ctypes import *


# class MntFrameParam(LittleEndianStructure):
#     _pack_ = 1
#     _fields_ = [
#         ("isParted", c_uint32, 2),
#         ("partNumber", c_uint32, 15),
#         ("totalPart", c_uint32, 15)
#     ]
#
#
# class MntFrameHeader(LittleEndianStructure):
#     _pack_ = 1
#     _fields_ = [
#         ("dest_address", c_uint8),
#         ("source_address", c_uint8),
#         ("frame_param", MntFrameParam),
#         ("command", c_uint8),
#         ("data_size", c_uint16),
#     ]
#
#
# class MntFrame(LittleEndianStructure):
#     _pack_ = 1
#     _fields_ = [
#         ("header", MntFrameHeader),
#         ("data", c_uint8 * 8),
#     ]
#

# class PWMControl(LittleEndianStructure):
#     _pack_ = 1
#     _fields_ = [
#         ("frequency", c_uint16),
#         ("dutyCycle", c_uint8)
#     ]
#
#
# class LedControlType(Union):
#     _pack_ = 1
#     _fields_ = [
#         ("normal", c_uint8),
#         ("pwm", PWMControl)
#     ]
#
#
# class LedControlFrame(LittleEndianStructure):
#     _pack_ = 1
#     _fields_ = [
#         ("header", MntFrameHeader),
#         ("ledNumber", c_uint8),
#         ("ledControlType", c_uint8),
#         ("type", LedControlType)
#     ]

TCP_IP = '127.0.0.1'
# TCP_IP = '192.168.0.12'
TCP_PORT = 49452
BUFFER_SIZE = 1024
MESSAGE = 'Hello, World!'
mess = create_string_buffer(0x30, 1024)

test = c_uint16 * 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
# ret = cast(data, LedControlFrame)
#s.close()

s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
data = s.recv(BUFFER_SIZE)
# ret = cast(data, LedControlFrame)
s.close()


pass
