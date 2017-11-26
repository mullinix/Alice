import serial
import time

class RT_Communicator:
#	def __init__(self):
#		print "DMM Object Initialized\r\n"

        def turn_galil(self,ser,AC=256000,DC=256000,SP=15120,theta=0):
                ser.flushOutput()
                ser.flushInput()
                ser.write('TPA\r\n')
                time.sleep(0.5)
                loc=ser.readline() # first line out is text
                loc=ser.readline() # this line is the number
                start=int(loc)
                writestr='ACA='+str(AC)+\
                        ';DCA='+str(DC)+\
                        ';SPA='+str(SP)+\
                        ';PRA='+str(theta*2100)+\
                        ';BG A;\r\n'

                ser.write(writestr)
                time.sleep(0.5)
                ser.flushOutput()
                ser.flushInput()
                ser.write('TPA\r\n')
                time.sleep(0.5)
                loc=ser.readline() # first line out is text
                loc=ser.readline() # this line is the number
                loc=int(loc)
#                print("The position, currently, is %d" % loc)
# NOTE: We may have to adjust the following test to allow overflow of int!
                while(loc<start+theta*2100):
                    ser.write('TPA\r\n')
                    time.sleep(0.5)
                    loc=ser.readline() # first line out is text
                    loc=ser.readline() # this line is the number
                    loc=int(loc)
#                    print("The position, currently, is %d" % loc)

                ser.write('TC0\r\n') # uncomment this line for error code return
                time.sleep(0.5)
                ser.readline() # ignore the command echo
		return int(ser.readline())
	
	def init_galil(self,PortIn='COM1', BaudIn=19200, TOIn=5):
		ser=serial.Serial(port=PortIn,baudrate=BaudIn, timeout=TOIn)
                ser.write('EO 1\r\n') # the code is written expecting echo
                time.sleep(0.5)
		ser.write('SH A\r\n') # this starts code on A
                time.sleep(0.5)
                ser.flushOutput()
#                print ser # uncomment for troubleshooting serial object
		return ser
	
	def test_galil(self):
		ser=self.init_galil()
		for i in xrange(3):
                        if(self.turn_galil(ser=ser,theta=10*(i+1))==0):
                            print "Rotated %d degrees." % (10*(i+1))
			time.sleep(2)

                ser.close()

		
