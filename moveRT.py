#!/usr/bin/env python
import sys
from RT_Communicator import RT_Communicator

nargin = len(sys.argv)

if(nargin<2):
    sys.exit("Usage: $ %s <degrees_to_rotate>" % sys.argv[0])

rt = RT_Communicator()
rt.turn_galil(theta=float(sys.argv[1]))
