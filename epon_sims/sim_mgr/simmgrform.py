# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simmgrform.ui'
#
# Created: Sat Jan 13 14:36:37 2018
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class SimMgr(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("SimMgr")



        self.viewSimButton = QPushButton(self,"viewSimButton")
        self.viewSimButton.setGeometry(QRect(130,430,86,28))
        viewSimButton_font = QFont(self.viewSimButton.font())
        viewSimButton_font.setPointSize(10)
        self.viewSimButton.setFont(viewSimButton_font)

        self.newSimButton = QPushButton(self,"newSimButton")
        self.newSimButton.setGeometry(QRect(20,430,86,28))
        newSimButton_font = QFont(self.newSimButton.font())
        newSimButton_font.setPointSize(10)
        self.newSimButton.setFont(newSimButton_font)

        self.consolidateBtn = QPushButton(self,"consolidateBtn")
        self.consolidateBtn.setGeometry(QRect(240,430,87,30))
        consolidateBtn_font = QFont(self.consolidateBtn.font())
        consolidateBtn_font.setPointSize(10)
        self.consolidateBtn.setFont(consolidateBtn_font)

        self.addSimButton = QPushButton(self,"addSimButton")
        self.addSimButton.setGeometry(QRect(350,430,94,30))
        addSimButton_font = QFont(self.addSimButton.font())
        addSimButton_font.setPointSize(10)
        self.addSimButton.setFont(addSimButton_font)

        self.consolidateNameEdit = QLineEdit(self,"consolidateNameEdit")
        self.consolidateNameEdit.setGeometry(QRect(460,20,108,20))

        self.quitButton = QPushButton(self,"quitButton")
        self.quitButton.setGeometry(QRect(590,430,86,28))
        quitButton_font = QFont(self.quitButton.font())
        quitButton_font.setPointSize(10)
        self.quitButton.setFont(quitButton_font)

        self.removeDirCheckBox = QCheckBox(self,"removeDirCheckBox")
        self.removeDirCheckBox.setGeometry(QRect(300,400,140,21))
        removeDirCheckBox_font = QFont(self.removeDirCheckBox.font())
        removeDirCheckBox_font.setPointSize(10)
        self.removeDirCheckBox.setFont(removeDirCheckBox_font)

        self.haltButton = QPushButton(self,"haltButton")
        self.haltButton.setGeometry(QRect(590,390,86,28))
        haltButton_font = QFont(self.haltButton.font())
        haltButton_font.setPointSize(10)
        self.haltButton.setFont(haltButton_font)

        self.removeSimButton = QPushButton(self,"removeSimButton")
        self.removeSimButton.setGeometry(QRect(470,430,94,30))
        removeSimButton_font = QFont(self.removeSimButton.font())
        removeSimButton_font.setPointSize(10)
        self.removeSimButton.setFont(removeSimButton_font)

        self.openSimButton = QPushButton(self,"openSimButton")
        self.openSimButton.setGeometry(QRect(470,390,94,30))
        openSimButton_font = QFont(self.openSimButton.font())
        openSimButton_font.setPointSize(10)
        self.openSimButton.setFont(openSimButton_font)

        self.titleLabel = QLabel(self,"titleLabel")
        self.titleLabel.setGeometry(QRect(70,10,200,24))
        titleLabel_font = QFont(self.titleLabel.font())
        titleLabel_font.setPointSize(14)
        self.titleLabel.setFont(titleLabel_font)
        self.titleLabel.setFrameShape(QLabel.NoFrame)
        self.titleLabel.setFrameShadow(QLabel.Plain)

        self.consolidateNameLbl = QLabel(self,"consolidateNameLbl")
        self.consolidateNameLbl.setGeometry(QRect(320,20,136,20))
        consolidateNameLbl_font = QFont(self.consolidateNameLbl.font())
        consolidateNameLbl_font.setPointSize(10)
        self.consolidateNameLbl.setFont(consolidateNameLbl_font)

        self.simListBox = QListBox(self,"simListBox")
        self.simListBox.setGeometry(QRect(20,70,310,310))
        simListBox_font = QFont(self.simListBox.font())
        simListBox_font.setPointSize(10)
        self.simListBox.setFont(simListBox_font)
        self.simListBox.setSelectionMode(QListBox.Extended)

        self.startedNameLbl = QLabel(self,"startedNameLbl")
        self.startedNameLbl.setGeometry(QRect(360,230,136,20))
        startedNameLbl_font = QFont(self.startedNameLbl.font())
        startedNameLbl_font.setPointSize(10)
        self.startedNameLbl.setFont(startedNameLbl_font)

        self.notStartedNameLbl = QLabel(self,"notStartedNameLbl")
        self.notStartedNameLbl.setGeometry(QRect(360,50,136,20))
        notStartedNameLbl_font = QFont(self.notStartedNameLbl.font())
        notStartedNameLbl_font.setPointSize(10)
        self.notStartedNameLbl.setFont(notStartedNameLbl_font)

        self.notStartedListBox = QListBox(self,"notStartedListBox")
        self.notStartedListBox.setGeometry(QRect(360,70,310,130))
        notStartedListBox_font = QFont(self.notStartedListBox.font())
        notStartedListBox_font.setPointSize(10)
        self.notStartedListBox.setFont(notStartedListBox_font)
        self.notStartedListBox.setSelectionMode(QListBox.Extended)

        self.startedListBox = QListBox(self,"startedListBox")
        self.startedListBox.setGeometry(QRect(360,250,310,130))
        startedListBox_font = QFont(self.startedListBox.font())
        startedListBox_font.setPointSize(10)
        self.startedListBox.setFont(startedListBox_font)
        self.startedListBox.setSelectionMode(QListBox.Extended)

        self.completedNameLbl = QLabel(self,"completedNameLbl")
        self.completedNameLbl.setGeometry(QRect(20,50,136,20))
        completedNameLbl_font = QFont(self.completedNameLbl.font())
        completedNameLbl_font.setPointSize(10)
        self.completedNameLbl.setFont(completedNameLbl_font)

        self.languageChange()

        self.resize(QSize(694,482).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.quitButton,SIGNAL("pressed()"),self.quitButton_pressed)
        self.connect(self.newSimButton,SIGNAL("pressed()"),self.newSimButton_pressed)
        self.connect(self.viewSimButton,SIGNAL("pressed()"),self.viewSimButton_pressed)
        self.connect(self.simListBox,SIGNAL("doubleClicked(QListBoxItem*)"),self.simListBox_doubleClicked)
        self.connect(self.removeSimButton,SIGNAL("pressed()"),self.removeSimButton_pressed)
        self.connect(self.consolidateBtn,SIGNAL("pressed()"),self.consolidateBtn_pressed)
        self.connect(self.addSimButton,SIGNAL("pressed()"),self.addSimButton_pressed)
        self.connect(self.haltButton,SIGNAL("pressed()"),self.haltSimBtn_pressed)
        self.connect(self.openSimButton,SIGNAL("pressed()"),self.openSimButton_pressed)

        self.setTabOrder(self.consolidateNameEdit,self.removeDirCheckBox)
        self.setTabOrder(self.removeDirCheckBox,self.newSimButton)
        self.setTabOrder(self.newSimButton,self.viewSimButton)
        self.setTabOrder(self.viewSimButton,self.consolidateBtn)
        self.setTabOrder(self.consolidateBtn,self.removeSimButton)
        self.setTabOrder(self.removeSimButton,self.quitButton)
        self.setTabOrder(self.quitButton,self.simListBox)


    def languageChange(self):
        self.setCaption(self.__tr("Simulation Manager"))
        self.viewSimButton.setText(self.__tr("View"))
        self.newSimButton.setText(self.__tr("New"))
        self.consolidateBtn.setText(self.__tr("Consolidate"))
        self.addSimButton.setText(self.__tr("Add"))
        self.quitButton.setText(self.__tr("QUIT"))
        self.removeDirCheckBox.setText(self.__tr("Remove Directory"))
        self.haltButton.setText(self.__tr("Halt"))
        self.removeSimButton.setText(self.__tr("Remove"))
        self.openSimButton.setText(self.__tr("Open"))
        self.titleLabel.setText(self.__tr("Running Simulations"))
        self.consolidateNameLbl.setText(self.__tr("Consolidation Name"))
        self.simListBox.clear()
        self.simListBox.insertItem(self.__tr("New Item"))
        self.startedNameLbl.setText(self.__tr("Running"))
        self.notStartedNameLbl.setText(self.__tr("Waiting to Run"))
        self.notStartedListBox.clear()
        self.notStartedListBox.insertItem(self.__tr("New Item"))
        self.startedListBox.clear()
        self.startedListBox.insertItem(self.__tr("New Item"))
        self.completedNameLbl.setText(self.__tr("Finished"))


    def quitButton_pressed(self):
        print "SimMgr.quitButton_pressed(): Not implemented yet"

    def newSimButton_pressed(self):
        print "SimMgr.newSimButton_pressed(): Not implemented yet"

    def viewSimButton_pressed(self):
        print "SimMgr.viewSimButton_pressed(): Not implemented yet"

    def simListBox_doubleClicked(self,a0):
        print "SimMgr.simListBox_doubleClicked(QListBoxItem*): Not implemented yet"

    def removeSimButton_pressed(self):
        print "SimMgr.removeSimButton_pressed(): Not implemented yet"

    def consolidateBtn_pressed(self):
        print "SimMgr.consolidateBtn_pressed(): Not implemented yet"

    def addSimButton_pressed(self):
        print "SimMgr.addSimButton_pressed(): Not implemented yet"

    def haltSimBtn_pressed(self):
        print "SimMgr.haltSimBtn_pressed(): Not implemented yet"

    def openSimButton_pressed(self):
        print "SimMgr.openSimButton_pressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("SimMgr",s,c)
