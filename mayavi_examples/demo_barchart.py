#!/usr/bin/python

import numpy as np
from mayavi.mlab import *

def test_barchart():
    """ Demo the bar chart plot with a 2D array.
    """
    s = np.abs(np.random.random((3, 3)))
    return barchart(s)

# View it
from mayavi import mlab
c = test_barchart()
mlab.show()
