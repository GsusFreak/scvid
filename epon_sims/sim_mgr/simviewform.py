# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simviewform.ui'
#
# Created: Sat Jan 13 14:36:37 2018
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class SimViewForm(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("SimViewForm")



        self.maxXEdit = QLineEdit(self,"maxXEdit")
        self.maxXEdit.setGeometry(QRect(100,150,70,23))
        maxXEdit_font = QFont(self.maxXEdit.font())
        self.maxXEdit.setFont(maxXEdit_font)

        self.minXEdit = QLineEdit(self,"minXEdit")
        self.minXEdit.setGeometry(QRect(100,120,70,23))
        minXEdit_font = QFont(self.minXEdit.font())
        self.minXEdit.setFont(minXEdit_font)

        self.maxXLbl = QLabel(self,"maxXLbl")
        self.maxXLbl.setGeometry(QRect(20,150,80,20))
        maxXLbl_font = QFont(self.maxXLbl.font())
        self.maxXLbl.setFont(maxXLbl_font)

        self.hostEdit = QLineEdit(self,"hostEdit")
        self.hostEdit.setGeometry(QRect(60,50,125,23))

        self.plotCaptionEdit = QLineEdit(self,"plotCaptionEdit")
        self.plotCaptionEdit.setGeometry(QRect(290,50,290,21))

        self.maxYLbl = QLabel(self,"maxYLbl")
        self.maxYLbl.setGeometry(QRect(20,210,80,20))
        maxYLbl_font = QFont(self.maxYLbl.font())
        self.maxYLbl.setFont(maxYLbl_font)

        self.maxYEdit = QLineEdit(self,"maxYEdit")
        self.maxYEdit.setGeometry(QRect(100,210,70,23))
        maxYEdit_font = QFont(self.maxYEdit.font())
        self.maxYEdit.setFont(maxYEdit_font)

        self.minYEdit = QLineEdit(self,"minYEdit")
        self.minYEdit.setGeometry(QRect(100,180,70,23))
        minYEdit_font = QFont(self.minYEdit.font())
        self.minYEdit.setFont(minYEdit_font)

        self.minYLbl = QLabel(self,"minYLbl")
        self.minYLbl.setGeometry(QRect(20,180,80,20))
        minYLbl_font = QFont(self.minYLbl.font())
        self.minYLbl.setFont(minYLbl_font)

        self.exportOutputBtn = QPushButton(self,"exportOutputBtn")
        self.exportOutputBtn.setGeometry(QRect(180,600,150,30))
        exportOutputBtn_font = QFont(self.exportOutputBtn.font())
        self.exportOutputBtn.setFont(exportOutputBtn_font)

        self.viewParamsBtn = QPushButton(self,"viewParamsBtn")
        self.viewParamsBtn.setGeometry(QRect(350,600,110,30))
        viewParamsBtn_font = QFont(self.viewParamsBtn.font())
        self.viewParamsBtn.setFont(viewParamsBtn_font)

        self.exitBtn = QPushButton(self,"exitBtn")
        self.exitBtn.setGeometry(QRect(590,600,87,30))
        exitBtn_font = QFont(self.exitBtn.font())
        self.exitBtn.setFont(exitBtn_font)

        self.viewOutputBtn = QPushButton(self,"viewOutputBtn")
        self.viewOutputBtn.setGeometry(QRect(20,600,140,30))
        viewOutputBtn_font = QFont(self.viewOutputBtn.font())
        self.viewOutputBtn.setFont(viewOutputBtn_font)

        self.stopSimBtn = QPushButton(self,"stopSimBtn")
        self.stopSimBtn.setGeometry(QRect(480,600,93,29))
        stopSimBtn_font = QFont(self.stopSimBtn.font())
        self.stopSimBtn.setFont(stopSimBtn_font)

        self.confIntvlChkBox = QCheckBox(self,"confIntvlChkBox")
        self.confIntvlChkBox.setGeometry(QRect(20,240,160,21))
        confIntvlChkBox_font = QFont(self.confIntvlChkBox.font())
        self.confIntvlChkBox.setFont(confIntvlChkBox_font)

        self.minXLbl = QLabel(self,"minXLbl")
        self.minXLbl.setGeometry(QRect(20,120,80,20))
        minXLbl_font = QFont(self.minXLbl.font())
        self.minXLbl.setFont(minXLbl_font)

        self.plotRefreshChkBox = QCheckBox(self,"plotRefreshChkBox")
        self.plotRefreshChkBox.setGeometry(QRect(20,270,150,22))
        plotRefreshChkBox_font = QFont(self.plotRefreshChkBox.font())
        self.plotRefreshChkBox.setFont(plotRefreshChkBox_font)

        self.simOutputLbl = QLabel(self,"simOutputLbl")
        self.simOutputLbl.setGeometry(QRect(30,300,170,27))
        simOutputLbl_font = QFont(self.simOutputLbl.font())
        simOutputLbl_font.setBold(1)
        self.simOutputLbl.setFont(simOutputLbl_font)

        self.simIDLbl = QLabel(self,"simIDLbl")
        self.simIDLbl.setGeometry(QRect(10,10,90,20))
        simIDLbl_font = QFont(self.simIDLbl.font())
        self.simIDLbl.setFont(simIDLbl_font)
        self.simIDLbl.setFrameShape(QLabel.NoFrame)
        self.simIDLbl.setFrameShadow(QLabel.Plain)

        self.simIDEdit = QLineEdit(self,"simIDEdit")
        self.simIDEdit.setGeometry(QRect(110,10,125,23))

        self.plotNameLbl = QLabel(self,"plotNameLbl")
        self.plotNameLbl.setGeometry(QRect(270,10,70,20))
        plotNameLbl_font = QFont(self.plotNameLbl.font())
        self.plotNameLbl.setFont(plotNameLbl_font)

        self.hostLbl = QLabel(self,"hostLbl")
        self.hostLbl.setGeometry(QRect(10,50,40,20))
        hostLbl_font = QFont(self.hostLbl.font())
        self.hostLbl.setFont(hostLbl_font)

        self.plotCaptionLbl = QLabel(self,"plotCaptionLbl")
        self.plotCaptionLbl.setGeometry(QRect(200,50,80,20))
        plotCaptionLbl_font = QFont(self.plotCaptionLbl.font())
        self.plotCaptionLbl.setFont(plotCaptionLbl_font)

        self.simStatusLbl = QLabel(self,"simStatusLbl")
        self.simStatusLbl.setGeometry(QRect(160,90,110,20))
        simStatusLbl_font = QFont(self.simStatusLbl.font())
        self.simStatusLbl.setFont(simStatusLbl_font)

        self.simStatusTitleLbl = QLabel(self,"simStatusTitleLbl")
        self.simStatusTitleLbl.setGeometry(QRect(10,90,130,20))
        simStatusTitleLbl_font = QFont(self.simStatusTitleLbl.font())
        self.simStatusTitleLbl.setFont(simStatusTitleLbl_font)

        self.simOutputListBox = QListBox(self,"simOutputListBox")
        self.simOutputListBox.setGeometry(QRect(30,330,650,260))
        simOutputListBox_font = QFont(self.simOutputListBox.font())
        self.simOutputListBox.setFont(simOutputListBox_font)
        self.simOutputListBox.setSelectionMode(QListBox.Extended)

        self.plotTypeBtnGrp = QButtonGroup(self,"plotTypeBtnGrp")
        self.plotTypeBtnGrp.setGeometry(QRect(210,110,480,210))
        plotTypeBtnGrp_font = QFont(self.plotTypeBtnGrp.font())
        self.plotTypeBtnGrp.setFont(plotTypeBtnGrp_font)

        self.utilVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"utilVsLoadBtn")
        self.utilVsLoadBtn.setGeometry(QRect(10,60,140,20))

        self.cyclelenVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"cyclelenVsLoadBtn")
        self.cyclelenVsLoadBtn.setGeometry(QRect(10,90,150,20))

        self.histBtn = QRadioButton(self.plotTypeBtnGrp,"histBtn")
        self.histBtn.setGeometry(QRect(320,30,105,21))

        self.delayVsONUBtn = QRadioButton(self.plotTypeBtnGrp,"delayVsONUBtn")
        self.delayVsONUBtn.setGeometry(QRect(320,120,120,20))

        self.granttimeVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"granttimeVsLoadBtn")
        self.granttimeVsLoadBtn.setGeometry(QRect(160,30,150,20))

        self.byteHistBtn = QRadioButton(self.plotTypeBtnGrp,"byteHistBtn")
        self.byteHistBtn.setGeometry(QRect(320,90,130,21))

        self.timeHistBtn = QRadioButton(self.plotTypeBtnGrp,"timeHistBtn")
        self.timeHistBtn.setGeometry(QRect(320,60,140,21))

        self.nzrVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"nzrVsLoadBtn")
        self.nzrVsLoadBtn.setGeometry(QRect(160,60,120,20))

        self.tputVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"tputVsLoadBtn")
        self.tputVsLoadBtn.setGeometry(QRect(160,90,160,20))

        self.nosVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"nosVsLoadBtn")
        self.nosVsLoadBtn.setGeometry(QRect(160,120,160,20))

        self.delayVsTimeBtn = QRadioButton(self.plotTypeBtnGrp,"delayVsTimeBtn")
        self.delayVsTimeBtn.setGeometry(QRect(160,150,130,22))

        self.cyclelenVsONUBtn = QRadioButton(self.plotTypeBtnGrp,"cyclelenVsONUBtn")
        self.cyclelenVsONUBtn.setGeometry(QRect(320,150,150,20))

        self.grantsizePVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"grantsizePVsLoadBtn")
        self.grantsizePVsLoadBtn.setGeometry(QRect(10,150,150,20))

        self.grantsizeVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"grantsizeVsLoadBtn")
        self.grantsizeVsLoadBtn.setGeometry(QRect(10,120,150,20))

        self.reportsizeVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"reportsizeVsLoadBtn")
        self.reportsizeVsLoadBtn.setGeometry(QRect(10,180,150,20))

        self.delayVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"delayVsLoadBtn")
        self.delayVsLoadBtn.setGeometry(QRect(10,30,120,20))

        self.jitterVsLoadBtn = QRadioButton(self.plotTypeBtnGrp,"jitterVsLoadBtn")
        self.jitterVsLoadBtn.setGeometry(QRect(160,180,120,20))

        self.plotNameEdit = QLineEdit(self,"plotNameEdit")
        self.plotNameEdit.setGeometry(QRect(360,10,125,23))

        self.pushButtonAutoName = QPushButton(self,"pushButtonAutoName")
        self.pushButtonAutoName.setGeometry(QRect(500,10,21,21))

        self.languageChange()

        self.resize(QSize(708,639).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.viewOutputBtn,SIGNAL("pressed()"),self.viewOutputBtn_pressed)
        self.connect(self.exportOutputBtn,SIGNAL("pressed()"),self.exportOutputBtn_pressed)
        self.connect(self.viewParamsBtn,SIGNAL("pressed()"),self.viewParamsBtn_pressed)
        self.connect(self.exitBtn,SIGNAL("pressed()"),self.exitBtn_pressed)
        self.connect(self.stopSimBtn,SIGNAL("pressed()"),self.stopSimBtn_pressed)
        self.connect(self.pushButtonAutoName,SIGNAL("pressed()"),self.pushButtonAutoName_pressed)

        self.setTabOrder(self.plotNameEdit,self.plotCaptionEdit)
        self.setTabOrder(self.plotCaptionEdit,self.minXEdit)
        self.setTabOrder(self.minXEdit,self.maxXEdit)
        self.setTabOrder(self.maxXEdit,self.minYEdit)
        self.setTabOrder(self.minYEdit,self.maxYEdit)
        self.setTabOrder(self.maxYEdit,self.confIntvlChkBox)
        self.setTabOrder(self.confIntvlChkBox,self.delayVsLoadBtn)
        self.setTabOrder(self.delayVsLoadBtn,self.utilVsLoadBtn)
        self.setTabOrder(self.utilVsLoadBtn,self.cyclelenVsLoadBtn)
        self.setTabOrder(self.cyclelenVsLoadBtn,self.grantsizeVsLoadBtn)
        self.setTabOrder(self.grantsizeVsLoadBtn,self.grantsizePVsLoadBtn)
        self.setTabOrder(self.grantsizePVsLoadBtn,self.granttimeVsLoadBtn)
        self.setTabOrder(self.granttimeVsLoadBtn,self.nzrVsLoadBtn)
        self.setTabOrder(self.nzrVsLoadBtn,self.tputVsLoadBtn)
        self.setTabOrder(self.tputVsLoadBtn,self.nosVsLoadBtn)
        self.setTabOrder(self.nosVsLoadBtn,self.histBtn)
        self.setTabOrder(self.histBtn,self.timeHistBtn)
        self.setTabOrder(self.timeHistBtn,self.byteHistBtn)
        self.setTabOrder(self.byteHistBtn,self.delayVsONUBtn)
        self.setTabOrder(self.delayVsONUBtn,self.cyclelenVsONUBtn)
        self.setTabOrder(self.cyclelenVsONUBtn,self.viewOutputBtn)
        self.setTabOrder(self.viewOutputBtn,self.exportOutputBtn)
        self.setTabOrder(self.exportOutputBtn,self.viewParamsBtn)
        self.setTabOrder(self.viewParamsBtn,self.exitBtn)
        self.setTabOrder(self.exitBtn,self.simIDEdit)
        self.setTabOrder(self.simIDEdit,self.hostEdit)
        self.setTabOrder(self.hostEdit,self.simOutputListBox)


    def languageChange(self):
        self.setCaption(self.__tr("Simulation View"))
        self.maxXLbl.setText(self.__tr("Max X value"))
        self.maxYLbl.setText(self.__tr("Max Y value"))
        self.minYLbl.setText(self.__tr("Min Y value"))
        self.exportOutputBtn.setText(self.__tr("Export Selected Output"))
        self.viewParamsBtn.setText(self.__tr("View Sim Params"))
        self.exitBtn.setText(self.__tr("Exit"))
        self.viewOutputBtn.setText(self.__tr("View Selected Output"))
        self.stopSimBtn.setText(self.__tr("Stop Sim"))
        self.confIntvlChkBox.setText(self.__tr("Confidence Intervals"))
        self.minXLbl.setText(self.__tr("Min X value"))
        self.plotRefreshChkBox.setText(self.__tr("Plot Refresh"))
        self.simOutputLbl.setText(self.__tr("Simulation Output"))
        self.simIDLbl.setText(self.__tr("Simulation ID"))
        self.plotNameLbl.setText(self.__tr("Plot Name"))
        self.hostLbl.setText(self.__tr("Host"))
        self.plotCaptionLbl.setText(self.__tr("Plot Caption"))
        self.simStatusLbl.setText(self.__tr("Status"))
        self.simStatusTitleLbl.setText(self.__tr("Simulation Status:"))
        self.simOutputListBox.clear()
        self.simOutputListBox.insertItem(self.__tr("New Item"))
        self.plotTypeBtnGrp.setTitle(self.__tr("Plot Type"))
        self.utilVsLoadBtn.setText(self.__tr("Utilization vs. Load"))
        self.cyclelenVsLoadBtn.setText(self.__tr("Cycle Len vs. Load"))
        self.histBtn.setText(self.__tr("Histogram"))
        self.delayVsONUBtn.setText(self.__tr("Delay vs. ONU"))
        self.granttimeVsLoadBtn.setText(self.__tr("Grant Time vs. Load"))
        self.byteHistBtn.setText(self.__tr("Byte Histogram"))
        self.timeHistBtn.setText(self.__tr("Time Histogram"))
        self.nzrVsLoadBtn.setText(self.__tr("NZR vs. Load"))
        self.tputVsLoadBtn.setText(self.__tr("Throughput vs. Load"))
        self.nosVsLoadBtn.setText(self.__tr("ONU Sched vs. Load"))
        self.delayVsTimeBtn.setText(self.__tr("Delay vs. Time"))
        self.cyclelenVsONUBtn.setText(self.__tr("Cycle Len vs. ONU"))
        self.grantsizePVsLoadBtn.setText(self.__tr("Grnt Sz Pkt vs. Ld"))
        self.grantsizeVsLoadBtn.setText(self.__tr("Grant Size vs. Load"))
        self.reportsizeVsLoadBtn.setText(self.__tr("Report Size vs. Load"))
        self.delayVsLoadBtn.setText(self.__tr("Delay vs. Load"))
        self.jitterVsLoadBtn.setText(self.__tr("Jitter vs. Load"))
        self.pushButtonAutoName.setText(QString.null)


    def viewOutputBtn_pressed(self):
        print "SimViewForm.viewOutputBtn_pressed(): Not implemented yet"

    def exportOutputBtn_pressed(self):
        print "SimViewForm.exportOutputBtn_pressed(): Not implemented yet"

    def viewParamsBtn_pressed(self):
        print "SimViewForm.viewParamsBtn_pressed(): Not implemented yet"

    def exitBtn_pressed(self):
        print "SimViewForm.exitBtn_pressed(): Not implemented yet"

    def stopSimBtn_pressed(self):
        print "SimViewForm.stopSimBtn_pressed(): Not implemented yet"

    def pushButtonAutoName_pressed(self):
        print "SimViewForm.pushButtonAutoName_pressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("SimViewForm",s,c)
