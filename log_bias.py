from DMM_Communicator import DMM_Communicator
from FOG_Communicator import FOG_Communicator
from RT_Communicator import RT_Communicator
import numpy as np
import time

def difftime(start,end):
    return float(end-start)


num_samples = 100
shift_degs = 211.75
num_shifts = 1 # 360/shift_degs+1 # add one to include 180 degrees

data=np.zeros((num_samples*num_shifts,4))

dmm = DMM_Communicator()
dmmser = dmm.init_agilent()

rt = RT_Communicator()
rtser = rt.init_galil()

fog = FOG_Communicator()
fogser = fog.init_emcore()
starttime=time.time()
degs=0
for shift in xrange(num_shifts):
    print "Shift %d" % shift
    rt.turn_galil(ser=rtser,theta=shift_degs)
    degs+=shift_degs
    time.sleep(5)
    for sample in xrange(num_samples):
        idx = shift*num_samples+sample
        volts = dmm.read_agilent(dmmser)
        counts = fog.read_emcore(fogser)
        thyme = difftime(starttime,time.time())
        data[idx,]=[degs,volts,counts,thyme]
        print "Progress: %.2f%%" % (float(idx+1)/(num_shifts*num_samples)*100)
        print data[idx,]

np.savetxt("bias.csv",data,delimiter=",")
