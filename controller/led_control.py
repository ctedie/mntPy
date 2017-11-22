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
		self._frame = LedControlFrame()
		# data = s.recv(BUFFER_SIZE)
		# ret = cast(data, LedControlFrame)
		# self._s.close()
		self._frame.header.dest_address = CONTROLLER_ADDRESS
		self._frame.header.source_address = SOURCE_ADDRESS
		self._frame.header.frame_param = (0, 0, 0)
		self._frame.header.command = COMMAND_LED_CONTROL
		pass

	def _send(self):
		self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._s.connect((CONNECTION_ADDRESS, CONNECTION_PORT))
		self._s.send(self._frame)
		self._s.close()
		pass

	def set_led(self, led_number, state):
		# type: (int, bool) -> int
		"""
		Set the led to a defined state
		:param led_number: The led number
		:param state: the state
		:return: The error code
		"""
		self._frame.ledNumber = led_number
		self._frame.ledControlType = 0
		self._frame.type.normal.state = state
		self._frame.header.data_size = sizeof(LedControlFrame) - sizeof(FrameHeader)
		self._send()
		pass
