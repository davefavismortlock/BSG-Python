#!/usr/bin/python

import numpy as np
from mayavi.mlab import *

def test_points3d():
    t = np.linspace(0, 4 * np.pi, 20)

    x = np.sin(2 * t)
    y = np.cos(t)
    z = np.cos(2 * t)
    s = 2 + np.sin(t)

    return points3d(x, y, z, s, colormap="copper", scale_factor=.25)

# View it
from mayavi import mlab
c = test_points3d()
mlab.show()
