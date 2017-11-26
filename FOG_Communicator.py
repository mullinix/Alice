import serial
import time

class FOG_Communicator:
#	def __init__(self):
#		print "FOG Object Initialized\n"

	def read_crossbow(self,ser):
		ser.write('G')
                time.sleep(0.5)
                ser.flushOutput()
                ser.flushInput()
                for i in xrange(5):
                    ser.readline()
#		return ser.readline()
	
        def stop_crossbow_read(self,ser):
                ser.write('X')


        def init_crossbow(self,PortIn='COM7', BaudIn=115200, TOIn=5):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('Z')
		return ser
	
	def test_crossbow(self):
		ser=self.init_crossbow()
                self.read_crossbow(ser)
		for i in xrange(10):
			print ser.readline()
			time.sleep(0.5)
                self.stop_crossbow_read(ser)
                ser.close()

		
