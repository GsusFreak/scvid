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
        SimMgr.resize(701, 482)
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
        self.startedNameLbl = QtGui.QLabel(SimMgr)
        self.startedNameLbl.setGeometry(QtCore.QRect(360, 219, 136, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startedNameLbl.setFont(font)
        self.startedNameLbl.setWordWrap(False)
        self.startedNameLbl.setObjectName(_fromUtf8("startedNameLbl"))
        self.notStartedNameLbl = QtGui.QLabel(SimMgr)
        self.notStartedNameLbl.setGeometry(QtCore.QRect(360, 50, 136, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.notStartedNameLbl.setFont(font)
        self.notStartedNameLbl.setWordWrap(False)
        self.notStartedNameLbl.setObjectName(_fromUtf8("notStartedNameLbl"))
        self.completedNameLbl = QtGui.QLabel(SimMgr)
        self.completedNameLbl.setGeometry(QtCore.QRect(21, 50, 136, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.completedNameLbl.setFont(font)
        self.completedNameLbl.setWordWrap(False)
        self.completedNameLbl.setObjectName(_fromUtf8("completedNameLbl"))
        self.simListBox = QtGui.QListWidget(SimMgr)
        self.simListBox.setGeometry(QtCore.QRect(20, 70, 301, 311))
        self.simListBox.setObjectName(_fromUtf8("simListBox"))
        self.notStartedListBox = QtGui.QListWidget(SimMgr)
        self.notStartedListBox.setGeometry(QtCore.QRect(360, 70, 320, 141))
        self.notStartedListBox.setObjectName(_fromUtf8("notStartedListBox"))
        self.startedListBox_2 = QtGui.QListWidget(SimMgr)
        self.startedListBox_2.setGeometry(QtCore.QRect(360, 240, 320, 141))
        self.startedListBox_2.setObjectName(_fromUtf8("startedListBox_2"))

        self.retranslateUi(SimMgr)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.quitButton_pressed)
        QtCore.QObject.connect(self.newSimButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.newSimButton_pressed)
        QtCore.QObject.connect(self.viewSimButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.viewSimButton_pressed)
        QtCore.QObject.connect(self.removeSimButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.removeSimButton_pressed)
        QtCore.QObject.connect(self.consolidateBtn, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.consolidateBtn_pressed)
        QtCore.QObject.connect(self.addSimButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.addSimButton_pressed)
        QtCore.QObject.connect(self.haltButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.haltSimBtn_pressed)
        QtCore.QObject.connect(self.openSimButton, QtCore.SIGNAL(_fromUtf8("pressed()")), SimMgr.openSimButton_pressed)
        QtCore.QMetaObject.connectSlotsByName(SimMgr)
        SimMgr.setTabOrder(self.consolidateNameEdit, self.removeDirCheckBox)
        SimMgr.setTabOrder(self.removeDirCheckBox, self.newSimButton)
        SimMgr.setTabOrder(self.newSimButton, self.viewSimButton)
        SimMgr.setTabOrder(self.viewSimButton, self.consolidateBtn)
        SimMgr.setTabOrder(self.consolidateBtn, self.removeSimButton)
        SimMgr.setTabOrder(self.removeSimButton, self.quitButton)

    def retranslateUi(self, SimMgr):
        SimMgr.setWindowTitle(_translate("SimMgr", "Simulation Manager", None))
        self.viewSimButton.setText(_translate("SimMgr", "View", None))
        self.newSimButton.setText(_translate("SimMgr", "New", None))
        self.consolidateBtn.setText(_translate("SimMgr", "Consolidate", None))
        self.addSimButton.setText(_translate("SimMgr", "Add", None))
        self.quitButton.setText(_translate("SimMgr", "QUIT", None))
        self.removeDirCheckBox.setText(_translate("SimMgr", "Remove Directory", None))
        self.haltButton.setText(_translate("SimMgr", "Halt", None))
        self.removeSimButton.setText(_translate("SimMgr", "Remove", None))
        self.openSimButton.setText(_translate("SimMgr", "Open", None))
        self.titleLabel.setText(_translate("SimMgr", "Running Simulations", None))
        self.consolidateNameLbl.setText(_translate("SimMgr", "Consolidation Name", None))
        self.startedNameLbl.setText(_translate("SimMgr", "Running", None))
        self.notStartedNameLbl.setText(_translate("SimMgr", "Waiting to Run", None))
        self.completedNameLbl.setText(_translate("SimMgr", "Finished", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SimMgr = QtGui.QWidget()
    ui = Ui_SimMgr()
    ui.setupUi(SimMgr)
    SimMgr.show()
    sys.exit(app.exec_())

