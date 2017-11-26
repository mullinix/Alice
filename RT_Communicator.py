import serial
import time

class RT_Communicator:
#	def __init__(self):
#		print "DMM Object Initialized\r\n"

        def turn_galil(self,ser,AC=256000,DC=256000,SP=15120,theta=0):
                writestr='ACA='+str(AC)+\
                        ';DCA='+str(DC)+\
                        ';SPA='+str(SP)+\
                        ';PRA='+str(theta)+\
                        ';BG A\r\n'
                ser.write(writestr)
#                ser.write('TC1\r\n')
                ser.flush()
		return ser.readline()
	
	def init_galil(self,PortIn='COM1', BaudIn=19200, TOIn=5):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
		ser.write('SH A\r\n')
                ser.flush()
                print ser
		return ser
	
	def test_galil(self):
		ser=self.init_galil()
		for i in xrange(10):
			print self.turn_galil(ser=ser,theta=1000*(i+1))
			time.sleep(2)

                ser.close()

		
