#!/usr/bin/python

import os
from qgis.core import *
from qgis.gui import *
from qgis.core.contextmanagers import qgisapp
from PyQt4.QtCore import *

def do_conversion(database, table, display):
   # Open a Spatialite vector layer
   uri = QgsDataSourceURI()
   uri.setDatabase(database)
   schema = ''
   geom_column = 'Geometry'
   uri.setDataSource(schema, table, geom_column)

   layer = QgsVectorLayer(uri.uri(), display, 'spatialite')
   if not layer.isValid():
      print("Layer '" + display + "' failed to load")
      exit(1)

   print("Layer '" + display + "' is loaded")
   for field in layer.pendingFields():
      print(field.name(), field.typeName())
      print

   layer.startEditing()

   if not layer.isEditable():
      print ("Layer '" + display + "' is not editable")
      exit(1)

   iter = layer.getFeatures()
   for feature in iter:
      # Retrieve every feature with its geometry and attributes
      geom = feature.geometry()
      fid = feature.id()
      print("Feature ID %d: " % fid)

      # Show some information about the feature
      attrs = feature.attributes()
      print(attrs)
      if geom.type() == QGis.Point:
         pt = geom.asPoint()
         print("Point was: " + str(pt))

         # CHANGE THE GEOMETRY: put a 4 in front of the easting, and a 1 in front of the northing
         newX = pt.x() + 400000
         newY = pt.y() + 100000

         print("Point is now: " + str(newX) + ", " + str(newY))

         newgeom = QgsGeometry.fromPoint(QgsPoint(newX, newY))
         layer.changeGeometry(fid, newgeom)
         print()

      elif geom.type() == QGis.Line:
         lin = geom.asPolyline()
         newlin = []
         print("Line: %d points" % len(lin))
         for n in range(len(lin)):
            # CHANGE THE GEOMETRY: put a 4 in front of the easting, and a 1 in front of the northing
            newX = lin[n].x() + 400000
            newY = lin[n].y() + 100000

            print("Polyline point is now: " + str(newX) + ", " + str(newY))

            newlin.append(QgsPoint(newX, newY))

         newgeom = QgsGeometry.fromPolyline(newlin)
         layer.changeGeometry(fid, newgeom)
         print()


      elif geom.type() == QGis.Polygon:
         plin = geom.asPolygon()
         newplin = []
         numPts = 0
         for ring in plin:
            numPts += len(ring)
         print("Polygon: %d rings with %d points" % (len(plin), numPts))

         for nring in range(len(plin)):
            lin = plin[nring]
            newlin = []
            for n in range(len(lin)):
               # CHANGE THE GEOMETRY: put a 4 in front of the easting, and a 1 in front of the northing
               newX = lin[n].x() + 400000
               newY = lin[n].y() + 100000

               print("Polygon point is now: " + str(newX) + ", " + str(newY))

               newlin.append(QgsPoint(newX, newY))

            newplin.append(newlin)

         newgeom = QgsGeometry.fromPolygon(newplin)
         layer.changeGeometry(fid, newgeom)
         print()

      else:
         print("Unknown")

      crs = QgsCoordinateReferenceSystem("OSGB 1936")

      tmp = database.split(".")
      outfile = tmp[0] + ".shp"
      error = QgsVectorFileWriter.writeAsVectorFormat(layer, outfile, "utf-8", crs, "ESRI Shapefile")
      if error != QgsVectorFileWriter.NoError:
         print("Error writing '" + outfile + "'")
      else:
         print("'" + outfile + "' written")
      print()


with qgisapp():
   project = QgsProject.instance()
   canvas = QgsMapCanvas(None)
   bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)

   database = ['field_centroids.sqlite', 'farms.sqlite', 'field_centroids_google.sqlite', 'river.sqlite', 'towns.sqlite', 'villages.sqlite']
   table = ['field_centroids', 'farms', 'field_centroids', 'river', 'towns', 'villages']
   display = ['Field centroids original', 'Farms', 'Field centroids Google', 'River', 'Towns', 'Villages']

   for thisdata in range(len(database)):
      print("Converting '" + database[thisdata] + "'")
      do_conversion(database[thisdata], table[thisdata], display[thisdata])

   print("End of run")
   exit(0)

