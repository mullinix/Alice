import serial
import time

class DMM_Communicator:
	def __init__(self,PortIn='COM2', BaudIn=9600, TOIn=1):
		self.ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		self.ser.write('SYST:REM\n')
		self.ser.write('MEAS:VOLT:DC? 1E-2,1E-4\n')
		self.ser.write('INIT\n')
                # here we read the first line (it comes out wonky, so let's waste it)
                self.ser.write('READ?\n')
                self.ser.readline()
                # flush serial, prepare for reading
                self.ser.flushOutput()
                self.ser.flushInput()
	
	def read_agilent(self):
		self.ser.write('READ?\n')
                strout=self.ser.readline()
                cleanstr=strout.strip()
                valout=float(cleanstr)
		return valout
	
	def test_agilent(self):
		for i in xrange(10):
			print self.read_agilent()

	def disconnect(self):
		self.ser.close()	
