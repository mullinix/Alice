from DMM_Communicator import DMM_Communicator
from FOG_Communicator import FOG_Communicator
from RT_Communicator import RT_Communicator
from fitData import findNorth
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

nargin = len(sys.argv)

if(nargin<4):
	sys.exit( "Usage: $ %s <number_of_samples_per_step> <number_of_degrees_per_step> <output_file_name>" % sys.argv[0])

num_samples = int(sys.argv[1])
shift_degs = int(sys.argv[2])
fname = str(sys.argv[3])

num_shifts = 360/shift_degs+1 # add one to include 180 degrees

def difftime(start,end):
    return float(end-start)

data=np.zeros((num_samples*num_shifts,4))
data.view(dtype=[('degs', 'float'),('volts','float'),('fogs','float'),('time','float')]).reshape(len(data))

north=np.zeros(num_shifts)

dmm = DMM_Communicator()
rt = RT_Communicator()
fog = FOG_Communicator()

starttime=time.time()
degs=0
for shift in xrange(num_shifts):
    print "Shift %d" % shift
    for sample in xrange(num_samples):
        idx = shift*num_samples+sample
        volts = dmm.read_agilent()
        counts = fog.read_emcore()
        thyme = difftime(starttime,time.time())
        data[idx,]=[degs,volts,counts,thyme]
        print "Progress: %.2f%%" % (float(idx+1)/(num_shifts*num_samples)*100)
        print data[idx,]
    rt.turn_galil(theta=shift_degs)
    degs+=shift_degs
    time.sleep(4)
    north[shift] = findNorth(data[1:idx,])

np.savetxt(fname,data,delimiter=",")

udegs=np.unique(data[:,1])

plt.plot(udegs,north,'k.-',label='Convergence to North')
plt.legend()
plt.show()
