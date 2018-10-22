# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siminitform.ui'
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

class Ui_SimInitForm(object):
    def setupUi(self, SimInitForm):
        SimInitForm.setObjectName(_fromUtf8("SimInitForm"))
        SimInitForm.resize(860, 887)
        self.simIdLbl = QtGui.QLabel(SimInitForm)
        self.simIdLbl.setGeometry(QtCore.QRect(20, 40, 90, 20))
        font = QtGui.QFont()
        self.simIdLbl.setFont(font)
        self.simIdLbl.setWordWrap(False)
        self.simIdLbl.setObjectName(_fromUtf8("simIdLbl"))
        self.usernameEdit = QtGui.QLineEdit(SimInitForm)
        self.usernameEdit.setGeometry(QtCore.QRect(120, 10, 200, 21))
        self.usernameEdit.setObjectName(_fromUtf8("usernameEdit"))
        self.passwordLbl = QtGui.QLabel(SimInitForm)
        self.passwordLbl.setGeometry(QtCore.QRect(340, 10, 70, 20))
        font = QtGui.QFont()
        self.passwordLbl.setFont(font)
        self.passwordLbl.setWordWrap(False)
        self.passwordLbl.setObjectName(_fromUtf8("passwordLbl"))
        self.hostEdit = QtGui.QLineEdit(SimInitForm)
        self.hostEdit.setGeometry(QtCore.QRect(410, 40, 230, 23))
        self.hostEdit.setObjectName(_fromUtf8("hostEdit"))
        self.loginBtn = QtGui.QPushButton(SimInitForm)
        self.loginBtn.setGeometry(QtCore.QRect(650, 10, 70, 28))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.logoutBtn = QtGui.QPushButton(SimInitForm)
        self.logoutBtn.setEnabled(False)
        self.logoutBtn.setGeometry(QtCore.QRect(730, 10, 90, 28))
        self.logoutBtn.setObjectName(_fromUtf8("logoutBtn"))
        self.passwordEdit = QtGui.QLineEdit(SimInitForm)
        self.passwordEdit.setGeometry(QtCore.QRect(410, 10, 230, 22))
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.usernameLbl = QtGui.QLabel(SimInitForm)
        self.usernameLbl.setGeometry(QtCore.QRect(30, 10, 70, 20))
        font = QtGui.QFont()
        self.usernameLbl.setFont(font)
        self.usernameLbl.setWordWrap(False)
        self.usernameLbl.setObjectName(_fromUtf8("usernameLbl"))
        self.simIdEdit = QtGui.QLineEdit(SimInitForm)
        self.simIdEdit.setGeometry(QtCore.QRect(120, 40, 200, 21))
        self.simIdEdit.setObjectName(_fromUtf8("simIdEdit"))
        self.hostLbl = QtGui.QLabel(SimInitForm)
        self.hostLbl.setGeometry(QtCore.QRect(350, 40, 50, 20))
        font = QtGui.QFont()
        self.hostLbl.setFont(font)
        self.hostLbl.setWordWrap(False)
        self.hostLbl.setObjectName(_fromUtf8("hostLbl"))
