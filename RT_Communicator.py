import serial
import time

class RT_Communicator:
	def __init__(self,PortIn='COM1', BaudIn=19200, TOIn=5):
		self.ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
                self.ser.write('EO 1\r\n') # the code is written expecting echo
#                time.sleep(0.5)
		self.ser.write('SH A\r\n') # this starts code on A
#                time.sleep(0.5)
                self.ser.flushOutput()
	
        def turn_galil(self,AC=256000,DC=256000,SP=15120,theta=0):
                self.ser.flushOutput()
                self.ser.flushInput()
                self.ser.write('TPA\r\n')
#                time.sleep(0.5)
                loc=self.ser.readline() # first line out is text
                loc=self.ser.readline() # this line is the number
                start=int(loc)
                writestr='ACA='+str(AC)+\
                        ';DCA='+str(DC)+\
                        ';SPA='+str(SP)+\
                        ';PRA='+str(theta*2100)+\
                        ';BG A;\r\n'

                self.ser.write(writestr)
#                time.sleep(0.5)
                self.ser.flushOutput()
                self.ser.flushInput()
                self.ser.write('TPA\r\n')
                time.sleep(0.2)
                loc=self.ser.readline() # first line out is text
                loc=self.ser.readline() # this line is the number
                loc=int(loc)
                # NOTE: We may have to adjust the following test to allow overflow of int!
#                while(loc<start+theta*2100):
#                    self.ser.write('TPA\r\n')
#                    time.sleep(0.5)
#                    loc=self.ser.readline() # first line out is text
#                    loc=self.ser.readline() # this line is the number
#                    loc=self.ser.readline() # this line is the number
#                    loc=int(loc)
#                self.ser.write('TC0\r\n') # uncomment this line for error code return
##                time.sleep(0.5)
#                self.ser.readline() # ignore the command echo
		return int(self.ser.readline())
	
	def test_galil(self):
		for i in xrange(3):
                        if(self.turn_galil(ser=ser,theta=10*(i+1))==0):
                            print "Rotated %d degrees." % (10*(i+1))
#			time.sleep(2)
                self.ser.close()


	def disconnect(self):
		self.ser.close()		
