#!/usr/bin/python3

try:
   from osgeo import gdal
   gdal.TermProgress = gdal.TermProgress_nocb
except ImportError:
   import gdal

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource


# =============================================================================
def Usage():
   print("Usage is: GIS_display <input file>")
   sys.exit(1)

# =============================================================================


# =============================================================================
def Main():
   # Say who we are and what we do
   print("This python script displays a single GIS layer using GDAL")

   # Do some initialization
   indemfile = None

   # Parse command line arguments
   i = 1
   while i < len(sys.argv):
      arg = sys.argv[i]

      if i == 1:
         indemfile = arg
      i += 1

   # initialize
   verbose = True

   # Got an input filename?
   if indemfile is None:
      Usage()

   # OK, open the input DEM file using GDAL
   indata = gdal.Open(indemfile)
   if indemfile == None:
      # Error, give up
      print("Cannot open", indemfile)
      sys.exit(2)

   # Now read in some information using GDAL
   geotransform = indata.GetGeoTransform()
   nBand = 1                                    # Assume that there is only one band of data
   band = indata.GetRasterBand(nBand)
   if band == None:
      # Error, give up
      print("Cannot load band", nBand, "from", indemfile)
      sys.exit(2)

   if verbose:
      # Display some information about the DEM
      print("Reading from", indemfile)
      print("   Size is", indata.RasterXSize, "x", indata.RasterYSize, "x", indata.RasterCount)
      print("   Projection is", indata.GetProjection())
      print("   Origin = (", geotransform[0], ",", geotransform[3], ")")
      print("   Pixel size = (", geotransform[1], ",", geotransform[5], ")")
      print("   Overall size =", indata.RasterXSize * geotransform[1], ",", indata.RasterYSize * geotransform[5])
      datatype = gdal.GetDataTypeName(band.DataType)
      print("   Reading band number", nBand, "with type", datatype)

      min = band.GetMinimum()
      max = band.GetMaximum()
      if min is None or max is None:
         (min, max) = band.ComputeRasterMinMax(nBand)
      print("   Min = %.3f, Max = %.3f" % (min, max))

      if band.GetOverviewCount() > 0:
         print("   Band has", band.GetOverviewCount(), "overviews")

      if not band.GetRasterColorTable() is None:
         print("   Band has a color table with", band.GetRasterColorTable().GetCount(), "entries")

      print("Storing data from", indemfile)

   # Now create a 2D array to store the data
   data = np.zeros((indata.RasterYSize, indata.RasterXSize))

   # And read the data into the array. NOTE: NumPy uses matrix (i.e. row-column) notation rather than array (x-y) notation
   for i in range(band.YSize - 1, -1, -1):
      scanline = band.ReadAsArray(0, i, band.XSize, 1, band.XSize, 1)
      j = 0
      while j < band.XSize:
         data[i, j] = scanline[0, j]
         j += 1

         if verbose:
            gdal.TermProgress(float(band.YSize - i) / band.YSize)

   # Create a light source object
   ls = LightSource(azdeg=0, altdeg=-35)

   # Shade data, creating an RGB array
   rgb = ls.shade(data, plt.cm.copper)

   plt.imshow(rgb)
   plt.title(indemfile)

   plt.show()

   if verbose:
      print("DEM displayed, end of run")

# =============================================================================


Main()

