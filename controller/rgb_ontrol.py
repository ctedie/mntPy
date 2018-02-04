# -*- coding:utf-8 -*-

from ctypes import *
import socket
from .param import *
from .frame import FrameHeader


class RGBControlFrame(Structure):
    _pack_ = 1
    _fields_ = [
        ("header", FrameHeader),
        ("red", c_uint16),
        ("green", c_uint16),
        ("blue", c_uint16),
        ("luminosity", c_uint16)
    ]


class RGBControl(object):
    """

    """
    def __init__(self):
        self._frame = RGBControlFrame()
        # data = s.recv(BUFFER_SIZE)
        # ret = cast(data, LedControlFrame)
        # self._s.close()
        self._frame.header.dest_address = CONTROLLER_ADDRESS
        self._frame.header.source_address = SOURCE_ADDRESS
        self._frame.header.frame_param = (0, 0, 0)
        self._frame.header.command = RGB_CONTROL
        pass

    def _send(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.connect((CONNECTION_ADDRESS, CONNECTION_PORT))
        self._s.send(self._frame)
        self._s.close()
        pass

    def set_rgb(self, red, green, blue):
        """
        Set the RGB color
        :param red: The red color intensity
        :param green: The green color intensity
        :param blue: The blue color intensity
        :return:
        """
        self._frame.red = red
        self._frame.green = green
        self._frame.blue = blue

        self._frame.header.data_size = sizeof(RGBControlFrame) - sizeof(FrameHeader)
        self._send()
        pass
