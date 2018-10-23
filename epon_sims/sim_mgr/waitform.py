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
        self.waitLbl.setGeometry(QtCore.QRect(53, 30, 100, 20))
        self.waitLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.waitLbl.setWordWrap(False)
        self.waitLbl.setObjectName(_fromUtf8("waitLbl"))
        self.waitProgressBar_2 = QtGui.QProgressBar(WaitForm)
        self.waitProgressBar_2.setGeometry(QtCore.QRect(43, 50, 118, 23))
        self.waitProgressBar_2.setProperty("value", 24)
        self.waitProgressBar_2.setObjectName(_fromUtf8("waitProgressBar_2"))

        self.retranslateUi(WaitForm)
        QtCore.QMetaObject.connectSlotsByName(WaitForm)

    def retranslateUi(self, WaitForm):
        WaitForm.setWindowTitle(_translate("WaitForm", "Wait", None))
        self.waitLbl.setText(_translate("WaitForm", "Please Wait", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WaitForm = QtGui.QWidget()
    ui = Ui_WaitForm()
    ui.setupUi(WaitForm)
    WaitForm.show()
    sys.exit(app.exec_())

