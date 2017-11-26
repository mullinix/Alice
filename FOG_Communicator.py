import serial
import time

class FOG_Communicator:
#	def __init__(self):
#		print "FOG Object Initialized\n"

	def read_crossbow(self,ser):
		ser.write('READ?\n')
		return ser.readline()
	
	def init_crossbow(self,PortIn='COM7', BaudIn=115200, TOIn=5):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('SYST:REM\n')
		ser.write('MEAS:VOLT:DC?\n')
		ser.write('INIT\n')
		return ser
	
	def test_crossbow(self):
		ser=self.init_crossbow()
		for i in xrange(10):
			print self.read_crossbow(ser)
			time.sleep(2)

		
