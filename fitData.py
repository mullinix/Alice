#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def findNorth(data):
	udegs=np.unique(data['degs'])
	ndegs=len(udegs)
	counts_per_second = np.zeros(ndegs)
	
	for i in xrange(ndegs):
		ix=np.where(data['degs']==udegs[i])
		times=data['time'][ix]
		times=times-min(times)
#		dt=np.diff(times)
#		dt=np.insert(dt,0,dt[0])
                dt=times[len(times)-1]
		volts=data['volts'][ix]
		dvolts=np.diff(volts)
                dvolts=sum(dvolts)
		voltsdt=volts
#                voltspertime=volts/times
		counts_per_second[i]=np.median(voltsdt)
	
	macks=np.median(counts_per_second)*2
	fitrads=np.linspace(0,2*np.pi,num=100)
	urads=udegs*np.pi/180.0
	A=np.ones((ndegs,3))
	A[:,1]=np.cos(urads)
	A[:,2]=np.sin(urads)
	fit = np.linalg.lstsq(A,counts_per_second)[0]
	alfa=fit[1]
	betta=fit[2]
	B=fit[0]
	a=np.sqrt(alfa**2+betta**2)
	phase_shift = np.arctan2(betta,alfa)
	phase_shift = np.pi/2.0-phase_shift
	faze = phase_shift*180/np.pi
	root = np.mod((180.0-np.arcsin(-B/a)*180.0/np.pi-faze), 360.0)
	print "North is located at: %.2f degrees relative." % root

	A=np.ones((100,3))
	A[:,1]=np.cos(fitrads)
	A[:,2]=np.sin(fitrads)

#	plt.close('all')
	plt.clf()
	
	plt.plot(udegs,counts_per_second,'k.',label='Data',markersize=10)
	plt.plot(fitrads*180.0/np.pi,np.dot(A,fit.T),'b-',label='Fit')
	plt.plot(root,0,'ro',label=('North: %.1f' % root),markersize=8)
	plt.legend()
	plt.show(block=False)
	plt.pause(1)

	return root
