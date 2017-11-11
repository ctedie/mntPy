#!/usr/bin/env python

import socket

# class MntFrame(Structure):
#     source_address = c_uint8()
#     dest_address = c_uint8()
#     frame_param = c_uint32()
#     command = c_uint8()
#     data_size = c_uint16()
#     data = c_uint8(1024)


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)

