#!/usr/bin/python3

try:
   from osgeo import gdal
   gdal.TermProgress = gdal.TermProgress_nocb
except ImportError:
   import gdal

import sys
import matplotlib.pyplot as plt


# =============================================================================
def Usage():
   print("Usage is: GIS_histo <input file> <output file>")
   sys.exit(1)

# =============================================================================


# =============================================================================
def Main():
   # Say who we are and what we do
   print("This Python scruipt creates a histogram from a GIS input file using GDAL and Matplotlib")

   # Do some initialization
   indemfile = None
   outfile = None

   # Parse command line arguments
   i = 1
   while i < len(sys.argv):
      arg = sys.argv[i]

      if i == 1:
         indemfile = arg
      elif i == 2:
         outfile = arg
      i += 1

   # Do some initialization
   nbins = 100
   grid = True
   xlabel = "Elevation"
   ylabel = 'Frequency'
   verbose = True

   # Do we have both filenames?
   if indemfile is None or outfile is None:
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

   # Now create a 1D array to store the data
   data_list = [0] * (indata.RasterXSize * indata.RasterYSize)

   # And read the data into the array
   n = 0
   for i in range(band.YSize - 1, -1, -1):
      scanline = band.ReadAsArray(0, i, band.XSize, 1, band.XSize, 1)
      j = 0
      while j < band.XSize:
         data_list[n] = scanline[0, j]
         j += 1
         n += 1

         if verbose:
            gdal.TermProgress(float(band.YSize - i) / band.YSize)

   n, bins, patches = plt.hist(data_list, nbins, normed = False, cumulative = False, histtype = 'bar', log = False, facecolor = 'green', alpha = 0.75)
   plt.xlabel(xlabel)                      # label the x axis
   plt.ylabel(ylabel)                      # label the y axis
   plt.grid(grid)                               # put a grid on it
   plt.show()                                   # plot the graph

   # Open the output file TODO check that this opens correctly at runtime
   fp_out = open(outfile, "w")
   for i in range(len(data_list)):
      fp_out.write("%7.6f" % data_list[i])
      fp_out.write("\n")

   fp_out.close()

   if verbose:
      print("DEM graphed, end of run")

# =============================================================================


Main()

