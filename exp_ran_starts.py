#!/usr/bin/env python
import numpy as np
import os

randegs = np.random.rand()*360.0

print "Shifting to random starting position of %.2f degrees." % randegs

os.system("moveRT.py %.2f" % randegs)

print "Finding North..."

os.system("run_exp.py 10 15 dataout.csv")
