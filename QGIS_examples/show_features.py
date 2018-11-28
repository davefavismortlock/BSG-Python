#!/usr/bin/python

import os
from qgis.core import *
from qgis.gui import *
from qgis.core.contextmanagers import qgisapp
from PyQt4.QtCore import *

with qgisapp():
   project = QgsProject.instance()
   canvas = QgsMapCanvas(None)
   bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)

   project.read(QFileInfo('/home/davefm/Documents/Research/0 To Do/JB_West_Sussex_GIS/JB_West_Sussex.qgs'))

   # Spatialite vector layer
   uri = QgsDataSourceURI()
   uri.setDatabase('field_centroids.sqlite')
   schema = ''
   table = 'field_centroids'
   geom_column = 'Geometry'
   uri.setDataSource(schema, table, geom_column)

   display_name = 'Field Centroids Original'
   layer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
   if not layer.isValid():
      print "Layer failed to load!"

   for field in layer.pendingFields():
      print field.name(), field.typeName()

   iter = layer.getFeatures()
   for feature in iter:
      # retrieve every feature with its geometry and attributes
      # fetch geometry
      geom = feature.geometry()
      print "Feature ID %d: " % feature.id()

      # show some information about the feature
      if geom.type() == QGis.Point:
         x = geom.asPoint()
         print "Point: " + str(x)
      elif geom.type() == QGis.Line:
         x = geom.asPolyline()
         print "Line: %d points" % len(x)
      elif geom.type() == QGis.Polygon:
         x = geom.asPolygon()
         numPts = 0
         for ring in x:
            numPts += len(ring)
         print "Polygon: %d rings with %d points" % (len(x), numPts)
      else:
         print "Unknown"

      # fetch attributes
      attrs = feature.attributes()

      # attrs is a list. It contains all the attribute values of this feature
      print attrs   

   exit(0)
