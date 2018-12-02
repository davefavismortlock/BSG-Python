#!/usr/bin/python

import numpy as np
from mayavi.mlab import *

def test_flow():
    x, y, z = np.mgrid[-4:4:40j, -4:4:40j, 0:4:20j]
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2 + 0.1)
    u = y * np.sin(r) / r
    v = -x * np.sin(r) / r
    w = np.ones_like(z)*0.05
    obj = flow(u, v, w)
    return obj

# View it
from mayavi import mlab
c = test_flow()
mlab.show()
