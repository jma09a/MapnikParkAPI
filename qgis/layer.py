from qgis.core import *
from qgis.gui import *
import sys

class Layer
 	def __init__(self, desc, numOccupants, t, active, owner):
		self.description = desc
		self.numOccupants = numOccupants
		self.active = active
		self.type = t
		self.owner = owner
		self.startDate
		self.endDate
		self.points
		self.color
		self.opacity
		self.filename

	def setDescription(desc)
		self.description = desc

	def getDescription()
		return self.description

	def setNumOccupants(x)
		self.numOccupants = x

	def getNumOccupants()
		return self.numOccupants

	def setOwner(x)
		self.owner = x

	def getOwner()
		return self.owner

	def setStartDate(x)
		self.startDate = x

	def getStartDate()
		return self.startDate

	def setEndDate(x)
		self.endDate = x

	def getEndDate()
		return self.endDate

	def setPoints(points)
		self.points = points

	def getPoints()
		return self.points

	def setColor(color)
		self.color = color

	def getColor()
		return self.color

	def setOpacity(opacity)
		self.opacity = opacity

	def getOpacity()
		return self.opacity
