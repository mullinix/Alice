import serial
import time

class RT_Communicator:
#	def __init__(self):
#		print "DMM Object Initialized\n"

	def turn_galil(self,ser,AC=25600,DC=25600,SP=151200000,theta=0)
		ser.write('AC='+AC+'\n')
		ser.write('DC='+DC+'\n')
		ser.write('SP='+SP+'\n')
		ser.write('PRA='+theta+'\n')
		ser.write('BGA\n')
		#return ser.readline()
	
	def init_galil(self,PortIn='COM1', BaudIn=19200, TOIn=1):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('SHA\n')
		return ser
	
	def test_galil(self):
		ser=self.init_galil()
		for i in xrange(10):
			print self.turn_galil(ser=ser,theta=10*(i+1))
			time.sleep(2)

		
