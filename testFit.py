#!/usr/bin/env python
from fitData import findNorth
import numpy as np

fullData = np.genfromtxt('res_45deg.csv',delimiter=',',dtype=[('degs','float'),('volts','float'),('fogs','float'),('time','float')])
udegs=np.unique(fullData['degs'])
ndegs=len(udegs)
for i in xrange(ndegs):
	idx=np.where(fullData['degs']<=udegs[i])
	findNorth(data=fullData[idx])
