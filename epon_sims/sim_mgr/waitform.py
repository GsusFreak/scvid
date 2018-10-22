# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waitform.ui'
#
# Created: Sat Jan 13 14:36:37 2018
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class WaitForm(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("WaitForm")



        self.waitLbl = QLabel(self,"waitLbl")
        self.waitLbl.setGeometry(QRect(50,20,90,20))

        self.waitProgressBar = QProgressBar(self,"waitProgressBar")
        self.waitProgressBar.setGeometry(QRect(20,50,170,24))

        self.languageChange()

        self.resize(QSize(204,121).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Wait"))
        self.waitLbl.setText(self.__tr("Please Wait"))


    def __tr(self,s,c = None):
        return qApp.translate("WaitForm",s,c)
