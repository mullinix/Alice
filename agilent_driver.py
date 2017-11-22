import serial
import time

def read_agilent(ser):
	ser.write('READ?\n')
	return ser.readline()

def init_agilent(PortIn='COM2', BaudIn=9600, TOIn=1):
	ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
	ser.write('SYST:REM\n')
	ser.write('MEAS:VOLT:DC?\n')
	ser.write('INIT\n')
	return ser

def test_agilent():
	ser=init_agilent()
	for i in xrange(10):
		print read_agilent(ser)
		time.sleep(2)

test_agilent()
		
