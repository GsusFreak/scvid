# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simviewform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SimViewForm(object):
    def setupUi(self, SimViewForm):
        SimViewForm.setObjectName(_fromUtf8("SimViewForm"))
        SimViewForm.resize(708, 639)
        self.maxXEdit = QtGui.QLineEdit(SimViewForm)
        self.maxXEdit.setGeometry(QtCore.QRect(100, 150, 70, 23))
        font = QtGui.QFont()
        self.maxXEdit.setFont(font)
        self.maxXEdit.setObjectName(_fromUtf8("maxXEdit"))
        self.minXEdit = QtGui.QLineEdit(SimViewForm)
        self.minXEdit.setGeometry(QtCore.QRect(100, 120, 70, 23))
        font = QtGui.QFont()
        self.minXEdit.setFont(font)
        self.minXEdit.setObjectName(_fromUtf8("minXEdit"))
        self.maxXLbl = QtGui.QLabel(SimViewForm)
        self.maxXLbl.setGeometry(QtCore.QRect(20, 150, 80, 20))
        font = QtGui.QFont()
        self.maxXLbl.setFont(font)
        self.maxXLbl.setWordWrap(False)
        self.maxXLbl.setObjectName(_fromUtf8("maxXLbl"))
        self.hostEdit = QtGui.QLineEdit(SimViewForm)
        self.hostEdit.setGeometry(QtCore.QRect(60, 50, 125, 23))
        self.hostEdit.setObjectName(_fromUtf8("hostEdit"))
        self.plotCaptionEdit = QtGui.QLineEdit(SimViewForm)
        self.plotCaptionEdit.setGeometry(QtCore.QRect(290, 50, 290, 21))
        self.plotCaptionEdit.setObjectName(_fromUtf8("plotCaptionEdit"))
        self.maxYLbl = QtGui.QLabel(SimViewForm)
        self.maxYLbl.setGeometry(QtCore.QRect(20, 210, 80, 20))
        font = QtGui.QFont()
        self.maxYLbl.setFont(font)
        self.maxYLbl.setWordWrap(False)
        self.maxYLbl.setObjectName(_fromUtf8("maxYLbl"))
        self.maxYEdit = QtGui.QLineEdit(SimViewForm)
        self.maxYEdit.setGeometry(QtCore.QRect(100, 210, 70, 23))
        font = QtGui.QFont()
        self.maxYEdit.setFont(font)
        self.maxYEdit.setObjectName(_fromUtf8("maxYEdit"))
        self.minYEdit = QtGui.QLineEdit(SimViewForm)
        self.minYEdit.setGeometry(QtCore.QRect(100, 180, 70, 23))
        font = QtGui.QFont()
        self.minYEdit.setFont(font)
        self.minYEdit.setObjectName(_fromUtf8("minYEdit"))
        self.minYLbl = QtGui.QLabel(SimViewForm)
        self.minYLbl.setGeometry(QtCore.QRect(20, 180, 80, 20))
        font = QtGui.QFont()
        self.minYLbl.setFont(font)
        self.minYLbl.setWordWrap(False)
        self.minYLbl.setObjectName(_fromUtf8("minYLbl"))
        self.exportOutputBtn = QtGui.QPushButton(SimViewForm)
        self.exportOutputBtn.setGeometry(QtCore.QRect(180, 600, 150, 30))
        font = QtGui.QFont()
        self.exportOutputBtn.setFont(font)
        self.exportOutputBtn.setObjectName(_fromUtf8("exportOutputBtn"))
        self.viewParamsBtn = QtGui.QPushButton(SimViewForm)
        self.viewParamsBtn.setGeometry(QtCore.QRect(350, 600, 110, 30))
        font = QtGui.QFont()
        self.viewParamsBtn.setFont(font)
        self.viewParamsBtn.setObjectName(_fromUtf8("viewParamsBtn"))
        self.exitBtn = QtGui.QPushButton(SimViewForm)
        self.exitBtn.setGeometry(QtCore.QRect(590, 600, 87, 30))
        font = QtGui.QFont()
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.viewOutputBtn = QtGui.QPushButton(SimViewForm)
        self.viewOutputBtn.setGeometry(QtCore.QRect(20, 600, 140, 30))
        font = QtGui.QFont()
        self.viewOutputBtn.setFont(font)
        self.viewOutputBtn.setObjectName(_fromUtf8("viewOutputBtn"))
        self.stopSimBtn = QtGui.QPushButton(SimViewForm)
        self.stopSimBtn.setGeometry(QtCore.QRect(480, 600, 93, 29))
        font = QtGui.QFont()
        self.stopSimBtn.setFont(font)
        self.stopSimBtn.setObjectName(_fromUtf8("stopSimBtn"))
        self.confIntvlChkBox = QtGui.QCheckBox(SimViewForm)
        self.confIntvlChkBox.setGeometry(QtCore.QRect(20, 240, 160, 21))
        font = QtGui.QFont()
        self.confIntvlChkBox.setFont(font)
        self.confIntvlChkBox.setObjectName(_fromUtf8("confIntvlChkBox"))
        self.minXLbl = QtGui.QLabel(SimViewForm)
        self.minXLbl.setGeometry(QtCore.QRect(20, 120, 80, 20))
        font = QtGui.QFont()
        self.minXLbl.setFont(font)
        self.minXLbl.setWordWrap(False)
        self.minXLbl.setObjectName(_fromUtf8("minXLbl"))
        self.plotRefreshChkBox = QtGui.QCheckBox(SimViewForm)
        self.plotRefreshChkBox.setGeometry(QtCore.QRect(20, 270, 150, 22))
        font = QtGui.QFont()
        self.plotRefreshChkBox.setFont(font)
        self.plotRefreshChkBox.setObjectName(_fromUtf8("plotRefreshChkBox"))
        self.simOutputLbl = QtGui.QLabel(SimViewForm)
        self.simOutputLbl.setGeometry(QtCore.QRect(30, 300, 170, 27))
        font = QtGui.QFont()
        font.setBold(True)
        self.simOutputLbl.setFont(font)
        self.simOutputLbl.setWordWrap(False)
        self.simOutputLbl.setObjectName(_fromUtf8("simOutputLbl"))
        self.simIDLbl = QtGui.QLabel(SimViewForm)
        self.simIDLbl.setGeometry(QtCore.QRect(10, 10, 90, 20))
        font = QtGui.QFont()
        self.simIDLbl.setFont(font)
        self.simIDLbl.setFrameShape(QtGui.QFrame.NoFrame)
        self.simIDLbl.setFrameShadow(QtGui.QFrame.Plain)
        self.simIDLbl.setWordWrap(False)
        self.simIDLbl.setObjectName(_fromUtf8("simIDLbl"))
        self.simIDEdit = QtGui.QLineEdit(SimViewForm)
        self.simIDEdit.setGeometry(QtCore.QRect(110, 10, 125, 23))
        self.simIDEdit.setObjectName(_fromUtf8("simIDEdit"))
        self.plotNameLbl = QtGui.QLabel(SimViewForm)
        self.plotNameLbl.setGeometry(QtCore.QRect(270, 10, 70, 20))
        font = QtGui.QFont()
        self.plotNameLbl.setFont(font)
        self.plotNameLbl.setWordWrap(False)
        self.plotNameLbl.setObjectName(_fromUtf8("plotNameLbl"))
        self.hostLbl = QtGui.QLabel(SimViewForm)
        self.hostLbl.setGeometry(QtCore.QRect(10, 50, 40, 20))
        font = QtGui.QFont()
        self.hostLbl.setFont(font)
        self.hostLbl.setWordWrap(False)
        self.hostLbl.setObjectName(_fromUtf8("hostLbl"))
        self.plotCaptionLbl = QtGui.QLabel(SimViewForm)
        self.plotCaptionLbl.setGeometry(QtCore.QRect(200, 50, 80, 20))
        font = QtGui.QFont()
        self.plotCaptionLbl.setFont(font)
        self.plotCaptionLbl.setWordWrap(False)
        self.plotCaptionLbl.setObjectName(_fromUtf8("plotCaptionLbl"))
        self.simStatusLbl = QtGui.QLabel(SimViewForm)
        self.simStatusLbl.setGeometry(QtCore.QRect(160, 90, 110, 20))
        font = QtGui.QFont()
        self.simStatusLbl.setFont(font)
        self.simStatusLbl.setWordWrap(False)
        self.simStatusLbl.setObjectName(_fromUtf8("simStatusLbl"))
        self.simStatusTitleLbl = QtGui.QLabel(SimViewForm)
        self.simStatusTitleLbl.setGeometry(QtCore.QRect(10, 90, 130, 20))
        font = QtGui.QFont()
        self.simStatusTitleLbl.setFont(font)
        self.simStatusTitleLbl.setWordWrap(False)
        self.simStatusTitleLbl.setObjectName(_fromUtf8("simStatusTitleLbl"))
