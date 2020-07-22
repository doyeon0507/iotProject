#!/usr/bin/python

import sys, serial, time

comm = '/dev/ttyAMA0'
baudrate = 38400

device = serial.Serial(comm, baudrate, timeout = 5)
print(device)

while True :
	try:
		rcvBuf = bytearray()
		device.reset_input_buffer()
		rcvBuf = device.read_until(size=12)
		print rcvBuf
		temp = rcvBuf.find('p')
		a = rcvBuf[2:temp]
		b = int(a)
		print b
	except Exception as e:
		print("Exception read") + str(e)

	time.sleep(5)
