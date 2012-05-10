# Original sources Copyright (c) 2006 by Tim Sutton
#
# ported to Python by Martin Dobias
#
# licensed under the terms of GNU GPL 2

from PyQt4 import QtCore, QtGui
from mainwindow_ui import Ui_MainWindow
from qgis.core import *
from qgis.gui import *
import sys

qgis_prefix = "/usr"

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

  def __init__(self):
    QtGui.QMainWindow.__init__(self)

    # required by Qt4 to initialize the UI
    self.setupUi(self)

    # create map canvas
    self.canvas = QgsMapCanvas()
    self.canvas.setCanvasColor(QtGui.QColor(255,255,255))
    self.canvas.enableAntiAliasing(True)
    self.canvas.show()

    # lay our widgets out in the main window
    self.layout = QtGui.QVBoxLayout(self.frameMap)
    self.layout.addWidget(self.canvas)

    # create the actions behaviours
    self.connect(self.actionAddRubberBand, QtCore.SIGNAL("triggered()"), self.addRubberBand)
    self.connect(self.actionAddLayerShape, QtCore.SIGNAL("triggered()"), self.addLayerShape)
    self.connect(self.actionAddLayerRaster, QtCore.SIGNAL("triggered()"), self.addLayerRaster)
    self.connect(self.mpActionZoomIn, QtCore.SIGNAL("triggered()"), self.zoomIn)
    self.connect(self.mpActionZoomOut, QtCore.SIGNAL("triggered()"), self.zoomOut)
    self.connect(self.mpActionPan, QtCore.SIGNAL("triggered()"), self.pan)

    # create a little toolbar
    self.toolbar = self.addToolBar("File");
    self.toolbar.addAction(self.actionAddRubberBand);
    self.toolbar.addAction(self.actionAddLayerShape);
    self.toolbar.addAction(self.actionAddLayerRaster);
    self.toolbar.addAction(self.mpActionZoomIn);
    self.toolbar.addAction(self.mpActionZoomOut);
    self.toolbar.addAction(self.mpActionPan);

    # create the map tools
    self.toolPan = QgsMapToolPan(self.canvas)
    self.toolPan.setAction(self.mpActionPan)
    self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
    self.toolZoomIn.setAction(self.mpActionZoomIn)
    self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
    self.toolZoomOut.setAction(self.mpActionZoomOut)

    self.polygon = True
    self.rubberband = QgsRubberBand(self.canvas, self.polygon)

    self.rubberbands = []
    self.layers = []

  def zoomIn(self):
    self.canvas.setMapTool(self.toolZoomIn)

  def zoomOut(self):
    self.canvas.setMapTool(self.toolZoomOut)

  def pan(self):
    self.canvas.setMapTool(self.toolPan)

  def addLayerRaster(self):
    filename = unicode(QtGui.QFileDialog.getOpenFileName(self, 'Select Vector Layer', '.', ("Raster (*.tif)")))

    rasterFile = QtCore.QFileInfo(filename)
    # create layer
    layer = QgsRasterLayer(rasterFile.filePath(), rasterFile.completeBaseName())
    if not layer.isValid():
      return
    layer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
    layer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
    layer.setContrastEnhancementAlgorithm(QgsContrastEnhancement.StretchToMinimumMaximum, False)
    # add layer to the registry
    QgsMapLayerRegistry.instance().addMapLayer(layer);
    
    # set extent to the extent of our layer
    self.canvas.setExtent(layer.extent())

    # set the map canvas layer set
    self.layers.insert(0, QgsMapCanvasLayer(layer))
    self.canvas.setLayerSet(self.layers)

  def addLayerShape(self):
    """add a (hardcoded) layer and zoom to its extent"""
    filename = unicode(QtGui.QFileDialog.getOpenFileName(self, 'Select Vector Layer', '.', ("Shapes (*.shp)")))

    layerPath = filename
    layerName = "test"
    layerProvider = "ogr"

    # create layer
    layer = QgsVectorLayer(layerPath, layerName, layerProvider)

    if not layer.isValid():
      return

    # add layer to the registry
    QgsMapLayerRegistry.instance().addMapLayer(layer);
    
    # set extent to the extent of our layer
    self.canvas.setExtent(layer.extent())

    # set the map canvas layer set
    self.layers.insert(0, QgsMapCanvasLayer(layer))
    self.canvas.setLayerSet(self.layers)

  def transform(self, x, y):
    return QgsPoint(self.canvas.getCoordinateTransform().toMapCoordinates(x,y))

  def addRubberBand(self):
    rb = QgsRubberBand(self.canvas, True)
    points = [[self.transform(100,100), self.transform(150,100), self.transform(200,200), 		self.transform(100,200)]]
    rb.setToGeometry(QgsGeometry.fromPolygon(points), None)
    self.rubberbands.insert(0, rb)

  def on_showRubberBand_clicked(self):
    self.rubberbands[0].show()

  def on_hideRubberBand_clicked(self):
    self.rubberbands[0].hide()

def main(app):

  # initialize qgis libraries
  QgsApplication.setPrefixPath(qgis_prefix, True)
  QgsApplication.initQgis()

  # create main window
  wnd = MainWindow()
  wnd.show()

  # run!
  retval = app.exec_()

  # exit
  QgsApplication.exitQgis()
  sys.exit(retval)


if __name__ == "__main__":
  
  # create Qt application
  app = QtGui.QApplication(sys.argv)

  main(app)

