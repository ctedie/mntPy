# -*- coding:utf-8 -*-

from ctypes import *
import socket
from .param import *
from .frame import FrameHeader


class TestFrame(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("header", FrameHeader),
        ("data", c_uint8)
    ]


class Test(object):
    """

    """
    def __init__(self):
        self._frame = TestFrame()
        # data = s.recv(BUFFER_SIZE)
        # ret = cast(data, LedControlFrame)
        # self._s.close()
        self._frame.header.dest_address = CONTROLLER_ADDRESS
        self._frame.header.source_address = SOURCE_ADDRESS
        self._frame.header.frame_param = (0, 0, 0)
        self._frame.header.command = COMMAND_TEST
        pass

    def _send(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect((CONNECTION_ADDRESS, CONNECTION_PORT))
        self._s.send(self._frame)
        self._s.close()
        pass

    def send(self, data):
        self._frame.data = data
        self._frame.header.data_size = sizeof(TestFrame) - sizeof(FrameHeader)
        self._send()
