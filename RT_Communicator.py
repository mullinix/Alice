import serial
import time

class RT_Communicator:
	def __init__(self,PortIn='COM1', BaudIn=19200, TOIn=5):
		self.ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
                self.ser.write('EO 0\r\n') # the code is written ignoring echo
		self.ser.write('SH A\r\n') # this starts code on A
                self.ser.flushOutput()
	
        def turn_galil(self,AC=256000,DC=256000,SP=15120,theta=0):
                self.ser.flushOutput()
                self.ser.flushInput()
                writestr='ACA='+str(AC)+\
                        ';DCA='+str(DC)+\
                        ';SPA='+str(SP)+\
                        ';PRA='+str(theta*2100)+\
                        ';BG A;\r\n'

                self.ser.write(writestr)
                self.ser.flushOutput()
                self.ser.flushInput()
		return 0 
	
	def test_galil(self):
		for i in xrange(3):
                        if(self.turn_galil(ser=ser,theta=10*(i+1))==0):
                            print "Rotated %d degrees." % (10*(i+1))
                self.ser.close()


	def disconnect(self):
		self.ser.close()		
