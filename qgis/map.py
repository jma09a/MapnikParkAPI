from qgis.core import *
from qgis.gui import *
import sys

class Map()
	def __init__(self):
		self.layers = []

	def addLayer(layer)
		self.layers.append(layer)

	def getLayers()
		return self.layers

	def getActiveLayers()
		activeLayers = []
		for layer in self.layers:
			if(layer.active == True):
				activeLayers.append(layer)
		return activeLayers

	def render(canvas)
		layers = self.getActiveLayers()
		toBeRendered = []

		for x in layers:
			if(layer.type == "raster"):
			    rasterFile = QtCore.QFileInfo(layer.filename)
			    # create layer
			    newLayer = QgsRasterLayer(rasterFile.filePath(), rasterFile.completeBaseName())
			    if not newLayer.isValid():
			      return
			    newLayer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
			    newLayer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
			    newLayer.setContrastEnhancementAlgorithm(QgsContrastEnhancement.StretchToMinimumMaximum, False)
			    # add layer to the registry
			    QgsMapLayerRegistry.instance().addMapLayer(newLayer);
			    
			    # set extent to the extent of our layer
			    canvas.setExtent(newLayer.extent())

			    # set the map canvas layer set
			    toBeRendered.insert(0, QgsMapCanvasLayer(newLayer))

			elif(layer.type == "shape"):
				layerPath = layer.filename
				layerName = "test"
				layerProvider = "ogr"

				# create layer
				newLayer = QgsVectorLayer(layerPath, layerName, layerProvider)

				if not newLayer.isValid():
				return

				# add layer to the registry
				QgsMapLayerRegistry.instance().addMapLayer(newLayer);

				# set extent to the extent of our layer
				self.canvas.setExtent(newLayer.extent())

				# set the map canvas layer set
				toBeRendered.insert(0, QgsMapCanvasLayer(newLayer))

			elif(layer.type == "rubberband"):
			    rb = QgsRubberBand(canvas, True)
    			    points = [[]]
			    for point in layer.points:
				points.append(self.transform(point))
			    rb.setToGeometry(QgsGeometry.fromPolygon(points), None)

		canvas.setLayerSet(toBeRendered)
				
