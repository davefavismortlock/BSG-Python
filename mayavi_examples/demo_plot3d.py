#!/usr/bin/python

import numpy as np
from mayavi.mlab import *

def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
    mu = phi * n_mer
    x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    z = np.sin(n_long * mu / n_mer) * 0.5

    l = plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
    return l

# View it
from mayavi import mlab
c = test_plot3d()
mlab.show()
