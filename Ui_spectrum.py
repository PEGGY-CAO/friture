# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrum.ui'
#
# Created: Fri Mar 26 17:15:29 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Spectrum_Widget(object):
    def setupUi(self, Spectrum_Widget):
        Spectrum_Widget.setObjectName("Spectrum_Widget")
        Spectrum_Widget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Spectrum_Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.PlotZoneSpect = SpectPlot(Spectrum_Widget)
        self.PlotZoneSpect.setObjectName("PlotZoneSpect")
        self.gridLayout.addWidget(self.PlotZoneSpect, 1, 0, 1, 1)
        self.pushButtonSettings = QtGui.QPushButton(Spectrum_Widget)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.gridLayout.addWidget(self.pushButtonSettings, 0, 0, 1, 1)

        self.retranslateUi(Spectrum_Widget)
        QtCore.QMetaObject.connectSlotsByName(Spectrum_Widget)

    def retranslateUi(self, Spectrum_Widget):
        Spectrum_Widget.setWindowTitle(QtGui.QApplication.translate("Spectrum_Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSettings.setText(QtGui.QApplication.translate("Spectrum_Widget", "Settings", None, QtGui.QApplication.UnicodeUTF8))

from spectplot import SpectPlot
