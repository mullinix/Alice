import serial
import time
import re

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
                strout=ser.readline()
                cleanstr=strout.strip()
                numre=re.compile('\d+')
                numlist=numre.findall(cleanstr)
                valout=float(numlist[0])
                ser.write('X')
                return valout
	
        def init_crossbow(self,PortIn='COM7', BaudIn=115200, TOIn=5):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('Z')
		return ser
	
	def test_crossbow(self):
		ser=self.init_crossbow()
		for i in xrange(10):
                        print self.read_crossbow(ser)
			time.sleep(0.5)
                ser.close()

		
