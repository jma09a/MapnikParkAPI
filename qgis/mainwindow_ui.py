# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May  4 21:28:32 2007
#      by: PyQt4 UI code generator 4-snapshot-20070228
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,1000,800).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.frameMap = QtGui.QFrame(self.centralwidget)
        self.frameMap.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMap.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMap.setObjectName("frameMap")
        self.gridlayout.addWidget(self.frameMap,0,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

	self.rbLabel = QtGui.QLabel(self.centralwidget)
        self.rbLabel.setObjectName("rbLabel")
        self.gridlayout.addWidget(self.rbLabel,1,1,1,1)

	self.showRubberBand = QtGui.QToolButton(self.centralwidget)
        self.showRubberBand.setObjectName("showRubberBand")
        self.gridlayout.addWidget(self.showRubberBand,1,2,1,1)

        self.hideRubberBand = QtGui.QToolButton(self.centralwidget)
        self.hideRubberBand.setObjectName("hideRubberBand")
        self.gridlayout.addWidget(self.hideRubberBand,1,3,1,1)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,579,22))
        self.menubar.setObjectName("menubar")

        self.menuMap = QtGui.QMenu(self.menubar)
        self.menuMap.setObjectName("menuMap")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mpActionZoomIn = QtGui.QAction(MainWindow)
        self.mpActionZoomIn.setIcon(QtGui.QIcon(":/mActionZoomIn.png"))
        self.mpActionZoomIn.setObjectName("mpActionZoomIn")

        self.mpActionZoomOut = QtGui.QAction(MainWindow)
        self.mpActionZoomOut.setIcon(QtGui.QIcon(":/mActionZoomOut.png"))
        self.mpActionZoomOut.setObjectName("mpActionZoomOut")

        self.mpActionPan = QtGui.QAction(MainWindow)
        self.mpActionPan.setIcon(QtGui.QIcon(":/mActionPan.png"))
        self.mpActionPan.setObjectName("mpActionPan")

        self.actionAddLayerShape = QtGui.QAction(MainWindow)
        self.actionAddLayerShape.setIcon(QtGui.QIcon(":/mActionAddLayer.png"))
        self.actionAddLayerShape.setObjectName("actionAddLayerShape")

        self.actionAddLayerRaster = QtGui.QAction(MainWindow)
        self.actionAddLayerRaster.setIcon(QtGui.QIcon(":/mActionAddLayer.png"))
        self.actionAddLayerRaster.setObjectName("actionAddLayerRaster")

        self.actionAddRubberBand = QtGui.QAction(MainWindow)
        self.actionAddRubberBand.setIcon(QtGui.QIcon(":/mActionAddLayer.png"))
        self.actionAddRubberBand.setObjectName("actionAddRubberBand")

        self.menuMap.addAction(self.mpActionZoomIn)
        self.menuMap.addAction(self.mpActionZoomOut)
        self.menuMap.addAction(self.mpActionPan)
        self.menuMap.addAction(self.actionAddLayerShape)
	self.menuMap.addAction(self.actionAddLayerRaster)
	self.menuMap.addAction(self.actionAddRubberBand)
        self.menubar.addAction(self.menuMap.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
	self.menuMap.setTitle(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
	self.rbLabel.setText(QtGui.QApplication.translate("MainWindow", "Rubber Band Visibility:", None, QtGui.QApplication.UnicodeUTF8))
        self.showRubberBand.setText(QtGui.QApplication.translate("MainWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.hideRubberBand.setText(QtGui.QApplication.translate("MainWindow", "Hide", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLayerShape.setText(QtGui.QApplication.translate("MainWindow", "Add Shape Layer", None, QtGui.QApplication.UnicodeUTF8))
	self.actionAddLayerRaster.setText(QtGui.QApplication.translate("MainWindow", "Add Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
	self.actionAddRubberBand.setText(QtGui.QApplication.translate("MainWindow", "Add Rubber Band", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
