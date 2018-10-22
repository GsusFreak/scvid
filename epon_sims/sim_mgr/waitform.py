# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waitform.ui'
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

class Ui_WaitForm(object):
    def setupUi(self, WaitForm):
        WaitForm.setObjectName(_fromUtf8("WaitForm"))
        WaitForm.resize(204, 121)
        self.waitLbl = QtGui.QLabel(WaitForm)
        self.waitLbl.setGeometry(QtCore.QRect(50, 20, 90, 20))
        self.waitLbl.setWordWrap(False)
        self.waitLbl.setObjectName(_fromUtf8("waitLbl"))
