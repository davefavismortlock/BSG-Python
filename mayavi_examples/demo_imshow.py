#!/usr/bin/python

import numpy as np
from mayavi.mlab import *

def test_imshow():
    """ Use imshow to visualize a 2D 10x10 random array.
    """
    s = np.random.random((10, 10))
    return imshow(s, colormap='gist_earth')

# View it
from mayavi import mlab
c = test_imshow()
mlab.show()
