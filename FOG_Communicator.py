import serial
import time
import re

class FOG_Communicator:
        def __init__(self,PortIn='COM7', BaudIn=115200, TOIn=5):
		self.ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		self.ser.write('Z')
	
	def read_emcore(self):
		self.ser.write('G')
                time.sleep(0.5)
                self.ser.flushOutput()
                self.ser.flushInput()
                for i in xrange(5):
                    self.ser.readline()
                strout=self.ser.readline()
                cleanstr=strout.strip()
                numre=re.compile('[-]?\d+')
                numlist=numre.findall(cleanstr)
                valout=float(numlist[0])
                self.ser.write('X')
                return valout
	
	def test_emcore(self):
		for i in xrange(10):
                        print self.read_emcore()
			time.sleep(0.5)
                self.ser.close()

		
