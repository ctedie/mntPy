# -*- coding:utf-8 -*-

from ctypes import *


class FrameParam(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("isParted", c_uint32, 2),
        ("partNumber", c_uint32, 15),
        ("totalPart", c_uint32, 15)
    ]


class FrameHeader(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("dest_address", c_uint8),
        ("source_address", c_uint8),
        ("frame_param", FrameParam),
        ("command", c_uint8),
        ("data_size", c_uint16),
    ]

