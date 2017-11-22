# -*- coding:utf-8 -*-

from ctypes import *
import socket
from .param import *
from .frame import FrameHeader


class NormalControl(LittleEndianStructure):
	_pack_ = 1
	_fields_ = [
		("state", c_uint8)
	]


class PWMControl(LittleEndianStructure):
	_pack_ = 1
	_fields_ = [
		("frequency", c_uint16),
		("dutyCycle", c_uint8)
	]


class LedControlType(Union):
	_pack_ = 1
	_fields_ = [
		("normal", NormalControl),
		("pwm", PWMControl)
	]


class LedControlFrame(LittleEndianStructure):
	_pack_ = 1
	_fields_ = [
		("header", FrameHeader),
		("ledNumber", c_uint8),
		("ledControlType", c_uint8),
		("type", LedControlType)
	]


class LedControl(object):
	"""

	"""
	def __init__(self):
		self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._s.connect((CONNECTION_ADDRESS, CONNECTION_PORT))
		self._frame = LedControlFrame()
		self._s.send(self._frame)
		#data = s.recv(BUFFER_SIZE)
		# ret = cast(data, LedControlFrame)
		#s.close()

		pass

	def set_led(self, led_number, state):
		# type: (int, bool) -> int
		"""
		Set the led to a defined state
		:param led_number: The led number
		:param state: the state
		:return: The error code
		"""
		pass
