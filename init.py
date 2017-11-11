import serial
import io
import time

def read_agilent(sio):
	sio.write(unicode('READ?\n'))
	sio.flush()
	return sio.readline()

ser = serial.Serial(port='COM1', baudrate=9600, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))

while(1):
	print read_agilent(sio)
	time.sleep(2)



