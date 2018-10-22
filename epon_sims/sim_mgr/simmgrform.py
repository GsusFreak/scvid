# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simmgrform.ui'
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

class Ui_SimMgr(object):
    def setupUi(self, SimMgr):
        SimMgr.setObjectName(_fromUtf8("SimMgr"))
        SimMgr.resize(694, 482)
        self.viewSimButton = QtGui.QPushButton(SimMgr)
        self.viewSimButton.setGeometry(QtCore.QRect(130, 430, 86, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.viewSimButton.setFont(font)
        self.viewSimButton.setObjectName(_fromUtf8("viewSimButton"))
        self.newSimButton = QtGui.QPushButton(SimMgr)
        self.newSimButton.setGeometry(QtCore.QRect(20, 430, 86, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newSimButton.setFont(font)
        self.newSimButton.setObjectName(_fromUtf8("newSimButton"))
        self.consolidateBtn = QtGui.QPushButton(SimMgr)
        self.consolidateBtn.setGeometry(QtCore.QRect(240, 430, 87, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.consolidateBtn.setFont(font)
        self.consolidateBtn.setObjectName(_fromUtf8("consolidateBtn"))
        self.addSimButton = QtGui.QPushButton(SimMgr)
        self.addSimButton.setGeometry(QtCore.QRect(350, 430, 94, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addSimButton.setFont(font)
        self.addSimButton.setObjectName(_fromUtf8("addSimButton"))
        self.consolidateNameEdit = QtGui.QLineEdit(SimMgr)
        self.consolidateNameEdit.setGeometry(QtCore.QRect(460, 20, 108, 20))
        self.consolidateNameEdit.setObjectName(_fromUtf8("consolidateNameEdit"))
        self.quitButton = QtGui.QPushButton(SimMgr)
        self.quitButton.setGeometry(QtCore.QRect(590, 430, 86, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.removeDirCheckBox = QtGui.QCheckBox(SimMgr)
        self.removeDirCheckBox.setGeometry(QtCore.QRect(300, 400, 140, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removeDirCheckBox.setFont(font)
        self.removeDirCheckBox.setObjectName(_fromUtf8("removeDirCheckBox"))
        self.haltButton = QtGui.QPushButton(SimMgr)
        self.haltButton.setGeometry(QtCore.QRect(590, 390, 86, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.haltButton.setFont(font)
        self.haltButton.setObjectName(_fromUtf8("haltButton"))
        self.removeSimButton = QtGui.QPushButton(SimMgr)
        self.removeSimButton.setGeometry(QtCore.QRect(470, 430, 94, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.removeSimButton.setFont(font)
        self.removeSimButton.setObjectName(_fromUtf8("removeSimButton"))
        self.openSimButton = QtGui.QPushButton(SimMgr)
        self.openSimButton.setGeometry(QtCore.QRect(470, 390, 94, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openSimButton.setFont(font)
        self.openSimButton.setObjectName(_fromUtf8("openSimButton"))
        self.titleLabel = QtGui.QLabel(SimMgr)
        self.titleLabel.setGeometry(QtCore.QRect(70, 10, 200, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titleLabel.setFont(font)
        self.titleLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.titleLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.titleLabel.setWordWrap(False)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.consolidateNameLbl = QtGui.QLabel(SimMgr)
        self.consolidateNameLbl.setGeometry(QtCore.QRect(320, 20, 136, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.consolidateNameLbl.setFont(font)
        self.consolidateNameLbl.setWordWrap(False)
        self.consolidateNameLbl.setObjectName(_fromUtf8("consolidateNameLbl"))
