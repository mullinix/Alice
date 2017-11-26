from DMM_Communicator import DMM_Communicator
from FOG_Communicator import FOG_Communicator
from RT_Communicator import RT_Communicator
import numpy as np
import time

num_samples = 30
shift_degs = 15
num_shifts = 180/shift_degs+1 # add one to include 180 degrees

data=np.zeros((num_samples*num_shifts,3))

dmm = DMM_Communicator()
dmmser = dmm.init_agilent()

rt = RT_Communicator()
rtser = rt.init_galil()

fog = FOG_Communicator()
fogser = fog.init_crossbow()

degs=0
for shift in xrange(num_shifts):
    for sample in xrange(num_samples):
        idx = shift*num_samples+sample
        volts = dmm.read_agilent(dmmser)
        counts = fog.read_crossbow(fogser)
        data[idx,]=[degs,volts,counts]
        print data[idx,]
    rt.turn_galil(ser=rtser,theta=shift_degs)
    degs+=shift_degs
    time.sleep(5)

np.savetxt("results.csv",data,delimeter=",")
