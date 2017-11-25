import serial
import time

class RT_Communicator:
#	def __init__(self):
#		print "DMM Object Initialized\n"

	def read_galil(self,ser):
		ser.write('READ?\n')
		return ser.readline()
	
	def init_galil(self,PortIn='COM1', BaudIn=19200, TOIn=1):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('SHA\n')
		return ser
	
	def test_galil(self):
		ser=self.init_galil()
		for i in xrange(10):
			print self.read_galil(ser)
			time.sleep(2)

		
