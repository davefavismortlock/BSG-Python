#!/usr/bin/python2

from qgis.core import QgsProject
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from qgis.core.contextmanagers import qgisapp
from PyQt4.QtCore import QFileInfo

with qgisapp():
   # note that this must be an absolute path 
   project_path = '/home/davefm/Documents/Teaching/Postgrad/BSG Windsor/Python_for_Managing_Your_Data/examples/QGIS_examples/TEST.qgs'

   canvas = QgsMapCanvas(None)  # will reparent it to widget via layout

   # load the  project
   bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)
   QgsProject.instance().read(QFileInfo(project_path))

   # and show the canvas
   canvas.show()

