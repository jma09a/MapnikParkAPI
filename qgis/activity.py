from qgis.core import *
from qgis.gui import *
import sys

class Activity
	def __init__(self, owner, sdate, edate, points, color, opacity):
		self.owner = owner
		self.startDate = sdate
		self.endDate = edate
		self.points = points
		self.color = color
		self.opacity = opacity

	
