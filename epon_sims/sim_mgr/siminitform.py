# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siminitform.ui'
#
# Created: Sat Jan 13 14:36:37 2018
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class SimInitForm(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("SimInitForm")



        self.simIdLbl = QLabel(self,"simIdLbl")
        self.simIdLbl.setGeometry(QRect(20,40,90,20))
        simIdLbl_font = QFont(self.simIdLbl.font())
        self.simIdLbl.setFont(simIdLbl_font)

        self.usernameEdit = QLineEdit(self,"usernameEdit")
        self.usernameEdit.setGeometry(QRect(120,10,200,21))

        self.passwordLbl = QLabel(self,"passwordLbl")
        self.passwordLbl.setGeometry(QRect(340,10,70,20))
        passwordLbl_font = QFont(self.passwordLbl.font())
        self.passwordLbl.setFont(passwordLbl_font)

        self.hostEdit = QLineEdit(self,"hostEdit")
        self.hostEdit.setGeometry(QRect(410,40,230,23))

        self.loginBtn = QPushButton(self,"loginBtn")
        self.loginBtn.setGeometry(QRect(650,10,70,28))

        self.logoutBtn = QPushButton(self,"logoutBtn")
        self.logoutBtn.setEnabled(0)
        self.logoutBtn.setGeometry(QRect(730,10,90,28))

        self.passwordEdit = QLineEdit(self,"passwordEdit")
        self.passwordEdit.setGeometry(QRect(410,10,230,22))
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.usernameLbl = QLabel(self,"usernameLbl")
        self.usernameLbl.setGeometry(QRect(30,10,70,20))
        usernameLbl_font = QFont(self.usernameLbl.font())
        self.usernameLbl.setFont(usernameLbl_font)

        self.simIdEdit = QLineEdit(self,"simIdEdit")
        self.simIdEdit.setGeometry(QRect(120,40,200,21))

        self.hostLbl = QLabel(self,"hostLbl")
        self.hostLbl.setGeometry(QRect(350,40,50,20))
        hostLbl_font = QFont(self.hostLbl.font())
        self.hostLbl.setFont(hostLbl_font)

        self.dbaParamsBox = QGroupBox(self,"dbaParamsBox")
        self.dbaParamsBox.setGeometry(QRect(570,190,260,90))
        dbaParamsBox_font = QFont(self.dbaParamsBox.font())
        self.dbaParamsBox.setFont(dbaParamsBox_font)

        self.fixedGrantSizeLbl = QLabel(self.dbaParamsBox,"fixedGrantSizeLbl")
        self.fixedGrantSizeLbl.setGeometry(QRect(10,20,150,20))
        fixedGrantSizeLbl_font = QFont(self.fixedGrantSizeLbl.font())
        self.fixedGrantSizeLbl.setFont(fixedGrantSizeLbl_font)

        self.maxGrantSizeLbl = QLabel(self.dbaParamsBox,"maxGrantSizeLbl")
        self.maxGrantSizeLbl.setGeometry(QRect(10,50,150,20))
        maxGrantSizeLbl_font = QFont(self.maxGrantSizeLbl.font())
        self.maxGrantSizeLbl.setFont(maxGrantSizeLbl_font)

        self.fixedGrantSizeEdit = QLineEdit(self.dbaParamsBox,"fixedGrantSizeEdit")
        self.fixedGrantSizeEdit.setGeometry(QRect(150,20,90,22))

        self.maxGrantSizeEdit = QLineEdit(self.dbaParamsBox,"maxGrantSizeEdit")
        self.maxGrantSizeEdit.setGeometry(QRect(150,50,90,22))

        self.schedulerParamsBox = QGroupBox(self,"schedulerParamsBox")
        self.schedulerParamsBox.setGeometry(QRect(10,290,480,110))
        schedulerParamsBox_font = QFont(self.schedulerParamsBox.font())
        self.schedulerParamsBox.setFont(schedulerParamsBox_font)

        self.starveThreshLbl = QLabel(self.schedulerParamsBox,"starveThreshLbl")
        self.starveThreshLbl.setGeometry(QRect(10,20,130,20))
        starveThreshLbl_font = QFont(self.starveThreshLbl.font())
        self.starveThreshLbl.setFont(starveThreshLbl_font)

        self.acwLbl = QLabel(self.schedulerParamsBox,"acwLbl")
        self.acwLbl.setGeometry(QRect(10,50,150,20))
        acwLbl_font = QFont(self.acwLbl.font())
        self.acwLbl.setFont(acwLbl_font)

        self.schedulerMaxWinChkBox = QCheckBox(self.schedulerParamsBox,"schedulerMaxWinChkBox")
        self.schedulerMaxWinChkBox.setGeometry(QRect(280,20,180,21))
        schedulerMaxWinChkBox_font = QFont(self.schedulerMaxWinChkBox.font())
        self.schedulerMaxWinChkBox.setFont(schedulerMaxWinChkBox_font)

        self.npoLbl = QLabel(self.schedulerParamsBox,"npoLbl")
        self.npoLbl.setGeometry(QRect(10,80,170,20))
        npoLbl_font = QFont(self.npoLbl.font())
        self.npoLbl.setFont(npoLbl_font)

        self.npoEdit = QLineEdit(self.schedulerParamsBox,"npoEdit")
        self.npoEdit.setGeometry(QRect(180,80,80,24))

        self.acwEdit = QLineEdit(self.schedulerParamsBox,"acwEdit")
        self.acwEdit.setGeometry(QRect(180,50,80,24))

        self.starveThreshEdit = QLineEdit(self.schedulerParamsBox,"starveThreshEdit")
        self.starveThreshEdit.setGeometry(QRect(180,20,80,24))

        self.schedulerNumSlotLbl = QLabel(self.schedulerParamsBox,"schedulerNumSlotLbl")
        self.schedulerNumSlotLbl.setGeometry(QRect(270,50,180,20))
        schedulerNumSlotLbl_font = QFont(self.schedulerNumSlotLbl.font())
        self.schedulerNumSlotLbl.setFont(schedulerNumSlotLbl_font)

        self.schedulerSlotSizeLbl = QLabel(self.schedulerParamsBox,"schedulerSlotSizeLbl")
        self.schedulerSlotSizeLbl.setGeometry(QRect(270,80,180,20))

        self.schedulerSlotSizeEdit = QLineEdit(self.schedulerParamsBox,"schedulerSlotSizeEdit")
        self.schedulerSlotSizeEdit.setGeometry(QRect(440,80,30,23))

        self.schedulerNumSlotEdit = QLineEdit(self.schedulerParamsBox,"schedulerNumSlotEdit")
        self.schedulerNumSlotEdit.setGeometry(QRect(440,50,30,23))

        self.lambdaParamsBox = QGroupBox(self,"lambdaParamsBox")
        self.lambdaParamsBox.setGeometry(QRect(500,640,170,80))
        lambdaParamsBox_font = QFont(self.lambdaParamsBox.font())
        self.lambdaParamsBox.setFont(lambdaParamsBox_font)

        self.startLambdaLbl = QLabel(self.lambdaParamsBox,"startLambdaLbl")
        self.startLambdaLbl.setGeometry(QRect(10,20,120,20))

        self.endLambdaLbl = QLabel(self.lambdaParamsBox,"endLambdaLbl")
        self.endLambdaLbl.setGeometry(QRect(10,50,110,20))

        self.startLambdaEdit = QLineEdit(self.lambdaParamsBox,"startLambdaEdit")
        self.startLambdaEdit.setGeometry(QRect(120,20,40,21))

        self.endLambdaEdit = QLineEdit(self.lambdaParamsBox,"endLambdaEdit")
        self.endLambdaEdit.setGeometry(QRect(120,50,40,21))

        self.ssParamsBox = QGroupBox(self,"ssParamsBox")
        self.ssParamsBox.setGeometry(QRect(500,450,170,80))
        ssParamsBox_font = QFont(self.ssParamsBox.font())
        self.ssParamsBox.setFont(ssParamsBox_font)

        self.numStrmsLbl = QLabel(self.ssParamsBox,"numStrmsLbl")
        self.numStrmsLbl.setGeometry(QRect(10,50,94,20))

        self.hurstParamLbl = QLabel(self.ssParamsBox,"hurstParamLbl")
        self.hurstParamLbl.setGeometry(QRect(10,20,93,20))

        self.hurstParamEdit = QLineEdit(self.ssParamsBox,"hurstParamEdit")
        self.hurstParamEdit.setGeometry(QRect(110,20,50,22))

        self.numStrmsEdit = QLineEdit(self.ssParamsBox,"numStrmsEdit")
        self.numStrmsEdit.setGeometry(QRect(110,50,50,22))

        self.loadParamsBox = QGroupBox(self,"loadParamsBox")
        self.loadParamsBox.setGeometry(QRect(500,530,170,110))
        loadParamsBox_font = QFont(self.loadParamsBox.font())
        self.loadParamsBox.setFont(loadParamsBox_font)

        self.startLoadLbl = QLabel(self.loadParamsBox,"startLoadLbl")
        self.startLoadLbl.setGeometry(QRect(10,20,80,20))

        self.endLoadLbl = QLabel(self.loadParamsBox,"endLoadLbl")
        self.endLoadLbl.setGeometry(QRect(10,50,70,20))

        self.loadIncrLbl = QLabel(self.loadParamsBox,"loadIncrLbl")
        self.loadIncrLbl.setGeometry(QRect(10,80,80,20))

        self.endLoadEdit = QLineEdit(self.loadParamsBox,"endLoadEdit")
        self.endLoadEdit.setGeometry(QRect(100,50,60,22))

        self.loadIncrEdit = QLineEdit(self.loadParamsBox,"loadIncrEdit")
        self.loadIncrEdit.setGeometry(QRect(100,80,60,22))

        self.startLoadEdit = QLineEdit(self.loadParamsBox,"startLoadEdit")
        self.startLoadEdit.setGeometry(QRect(100,20,60,22))

        self.FRateLbl = QLabel(self,"FRateLbl")
        self.FRateLbl.setEnabled(0)
        self.FRateLbl.setGeometry(QRect(780,290,70,20))
        FRateLbl_font = QFont(self.FRateLbl.font())
        self.FRateLbl.setFont(FRateLbl_font)

        self.videoStartBox = QButtonGroup(self,"videoStartBox")
        self.videoStartBox.setEnabled(0)
        self.videoStartBox.setGeometry(QRect(500,290,270,50))

        self.timeShiftLbl = QLabel(self.videoStartBox,"timeShiftLbl")
        self.timeShiftLbl.setEnabled(0)
        self.timeShiftLbl.setGeometry(QRect(120,20,101,20))
        timeShiftLbl_font = QFont(self.timeShiftLbl.font())
        self.timeShiftLbl.setFont(timeShiftLbl_font)

        self.vsOffBtn = QRadioButton(self.videoStartBox,"vsOffBtn")
        self.vsOffBtn.setGeometry(QRect(10,20,50,22))
        self.vsOffBtn.setChecked(1)

        self.vsOnBtn = QRadioButton(self.videoStartBox,"vsOnBtn")
        self.vsOnBtn.setGeometry(QRect(70,20,40,22))

        self.timeShiftEdit = QLineEdit(self.videoStartBox,"timeShiftEdit")
        self.timeShiftEdit.setEnabled(0)
        self.timeShiftEdit.setGeometry(QRect(220,20,40,22))

        self.videoTraceFileLbl = QLabel(self,"videoTraceFileLbl")
        self.videoTraceFileLbl.setGeometry(QRect(500,390,100,20))
        videoTraceFileLbl_font = QFont(self.videoTraceFileLbl.font())
        self.videoTraceFileLbl.setFont(videoTraceFileLbl_font)

        self.changeTraceBtn = QPushButton(self,"changeTraceBtn")
        self.changeTraceBtn.setEnabled(0)
        self.changeTraceBtn.setGeometry(QRect(760,380,90,30))

        self.videoTraceEdit = QLineEdit(self,"videoTraceEdit")
        self.videoTraceEdit.setEnabled(0)
        self.videoTraceEdit.setGeometry(QRect(500,410,350,22))
        self.videoTraceEdit.setReadOnly(1)

        self.buttonGroup4_2 = QButtonGroup(self,"buttonGroup4_2")
        self.buttonGroup4_2.setGeometry(QRect(700,670,130,50))
        buttonGroup4_2_font = QFont(self.buttonGroup4_2.font())
        self.buttonGroup4_2.setFont(buttonGroup4_2_font)

        self.gtOffBtn = QRadioButton(self.buttonGroup4_2,"gtOffBtn")
        self.gtOffBtn.setGeometry(QRect(10,20,50,20))

        self.gtOnBtn = QRadioButton(self.buttonGroup4_2,"gtOnBtn")
        self.gtOnBtn.setGeometry(QRect(70,20,40,20))

        self.buttonGroup7 = QButtonGroup(self,"buttonGroup7")
        self.buttonGroup7.setGeometry(QRect(700,620,130,50))
        buttonGroup7_font = QFont(self.buttonGroup7.font())
        self.buttonGroup7.setFont(buttonGroup7_font)

        self.grtOffBtn = QRadioButton(self.buttonGroup7,"grtOffBtn")
        self.grtOffBtn.setGeometry(QRect(10,20,60,22))

        self.grtOnBtn = QRadioButton(self.buttonGroup7,"grtOnBtn")
        self.grtOnBtn.setGeometry(QRect(70,20,40,22))

        self.VideoDBABtnGroup = QButtonGroup(self,"VideoDBABtnGroup")
        self.VideoDBABtnGroup.setEnabled(0)
        self.VideoDBABtnGroup.setGeometry(QRect(710,70,140,110))
        VideoDBABtnGroup_font = QFont(self.VideoDBABtnGroup.font())
        self.VideoDBABtnGroup.setFont(VideoDBABtnGroup_font)

        self.dbaFixedVideoBtn = QRadioButton(self.VideoDBABtnGroup,"dbaFixedVideoBtn")
        self.dbaFixedVideoBtn.setEnabled(0)
        self.dbaFixedVideoBtn.setGeometry(QRect(20,40,70,22))

        self.dbaGatedVideoBtn = QRadioButton(self.VideoDBABtnGroup,"dbaGatedVideoBtn")
        self.dbaGatedVideoBtn.setEnabled(0)
        self.dbaGatedVideoBtn.setGeometry(QRect(20,20,70,22))
        self.dbaGatedVideoBtn.setChecked(0)

        self.dbaLimitedVideoBtn = QRadioButton(self.VideoDBABtnGroup,"dbaLimitedVideoBtn")
        self.dbaLimitedVideoBtn.setEnabled(0)
        self.dbaLimitedVideoBtn.setGeometry(QRect(20,60,80,22))
        self.dbaLimitedVideoBtn.setChecked(1)

        self.buttonGroup6 = QButtonGroup(self,"buttonGroup6")
        self.buttonGroup6.setGeometry(QRect(570,70,130,110))
        buttonGroup6_font = QFont(self.buttonGroup6.font())
        self.buttonGroup6.setFont(buttonGroup6_font)

        self.dbaExcessBtn = QRadioButton(self.buttonGroup6,"dbaExcessBtn")
        self.dbaExcessBtn.setGeometry(QRect(20,80,90,21))

        self.dbaGatedBtn = QRadioButton(self.buttonGroup6,"dbaGatedBtn")
        self.dbaGatedBtn.setGeometry(QRect(20,20,80,22))

        self.dbaFixedBtn = QRadioButton(self.buttonGroup6,"dbaFixedBtn")
        self.dbaFixedBtn.setGeometry(QRect(20,40,70,22))

        self.dbaLimitedBtn = QRadioButton(self.buttonGroup6,"dbaLimitedBtn")
        self.dbaLimitedBtn.setGeometry(QRect(20,60,90,22))
        self.dbaLimitedBtn.setChecked(1)

        self.buttonGroup5 = QButtonGroup(self,"buttonGroup5")
        self.buttonGroup5.setGeometry(QRect(700,570,130,50))
        buttonGroup5_font = QFont(self.buttonGroup5.font())
        self.buttonGroup5.setFont(buttonGroup5_font)

        self.ttOffBtn = QRadioButton(self.buttonGroup5,"ttOffBtn")
        self.ttOffBtn.setGeometry(QRect(10,20,50,20))

        self.ttOnBtn = QRadioButton(self.buttonGroup5,"ttOnBtn")
        self.ttOnBtn.setGeometry(QRect(70,20,40,20))

        self.dataTrafficTypeBox = QButtonGroup(self,"dataTrafficTypeBox")
        self.dataTrafficTypeBox.setGeometry(QRect(700,500,130,70))
        dataTrafficTypeBox_font = QFont(self.dataTrafficTypeBox.font())
        self.dataTrafficTypeBox.setFont(dataTrafficTypeBox_font)

        self.ssBtn = QRadioButton(self.dataTrafficTypeBox,"ssBtn")
        self.ssBtn.setGeometry(QRect(10,40,100,21))

        self.pnBtn = QRadioButton(self.dataTrafficTypeBox,"pnBtn")
        self.pnBtn.setGeometry(QRect(10,20,80,21))
        self.pnBtn.setChecked(1)

        self.predictTrafficBox = QButtonGroup(self,"predictTrafficBox")
        self.predictTrafficBox.setEnabled(0)
        self.predictTrafficBox.setGeometry(QRect(500,340,250,50))

        self.PredTypeLbl = QLabel(self.predictTrafficBox,"PredTypeLbl")
        self.PredTypeLbl.setEnabled(0)
        self.PredTypeLbl.setGeometry(QRect(130,20,70,20))
        PredTypeLbl_font = QFont(self.PredTypeLbl.font())
        self.PredTypeLbl.setFont(PredTypeLbl_font)

        self.pvtOffBtn = QRadioButton(self.predictTrafficBox,"pvtOffBtn")
        self.pvtOffBtn.setGeometry(QRect(10,20,50,22))
        self.pvtOffBtn.setChecked(1)

        self.PredTypeEdit = QLineEdit(self.predictTrafficBox,"PredTypeEdit")
        self.PredTypeEdit.setEnabled(0)
        self.PredTypeEdit.setGeometry(QRect(200,20,40,22))

        self.pvtOnBtn = QRadioButton(self.predictTrafficBox,"pvtOnBtn")
        self.pvtOnBtn.setGeometry(QRect(70,20,40,22))

        self.videoTrafficBox = QButtonGroup(self,"videoTrafficBox")
        self.videoTrafficBox.setGeometry(QRect(700,450,130,50))

        self.vtOffBtn = QRadioButton(self.videoTrafficBox,"vtOffBtn")
        self.vtOffBtn.setGeometry(QRect(10,20,50,22))
        self.vtOffBtn.setChecked(1)

        self.vtOnBtn = QRadioButton(self.videoTrafficBox,"vtOnBtn")
        self.vtOnBtn.setGeometry(QRect(70,20,40,22))

        self.launchBtn = QPushButton(self,"launchBtn")
        self.launchBtn.setEnabled(0)
        self.launchBtn.setGeometry(QRect(50,760,86,28))

        self.cancelBtn = QPushButton(self,"cancelBtn")
        self.cancelBtn.setGeometry(QRect(210,760,86,28))

        self.saveTimeButton = QPushButton(self,"saveTimeButton")
        self.saveTimeButton.setGeometry(QRect(790,350,40,20))

        self.groupBox6 = QGroupBox(self,"groupBox6")
        self.groupBox6.setGeometry(QRect(10,410,480,310))
        groupBox6_font = QFont(self.groupBox6.font())
        self.groupBox6.setFont(groupBox6_font)

        self.fpdValueLbl = QLabel(self.groupBox6,"fpdValueLbl")
        self.fpdValueLbl.setGeometry(QRect(250,250,150,20))

        self.runsEdit = QLineEdit(self.groupBox6,"runsEdit")
        self.runsEdit.setGeometry(QRect(140,30,100,25))

        self.tuningTimeEdit = QLineEdit(self.groupBox6,"tuningTimeEdit")
        self.tuningTimeEdit.setGeometry(QRect(140,130,100,23))

        self.grdTimeEdit = QLineEdit(self.groupBox6,"grdTimeEdit")
        self.grdTimeEdit.setGeometry(QRect(140,160,100,23))

        self.numONUEdit = QLineEdit(self.groupBox6,"numONUEdit")
        self.numONUEdit.setGeometry(QRect(140,190,70,21))

        self.numHvyONULbl = QLabel(self.groupBox6,"numHvyONULbl")
        self.numHvyONULbl.setGeometry(QRect(10,220,130,20))

        self.numHvyONUEdit = QLineEdit(self.groupBox6,"numHvyONUEdit")
        self.numHvyONUEdit.setGeometry(QRect(140,220,70,21))

        self.heavyLoadEdit = QLineEdit(self.groupBox6,"heavyLoadEdit")
        self.heavyLoadEdit.setGeometry(QRect(140,250,70,21))

        self.tuningTimeLbl = QLabel(self.groupBox6,"tuningTimeLbl")
        self.tuningTimeLbl.setGeometry(QRect(40,130,82,20))

        self.grdTimeLbl = QLabel(self.groupBox6,"grdTimeLbl")
        self.grdTimeLbl.setGeometry(QRect(40,160,80,20))

        self.numONULbl = QLabel(self.groupBox6,"numONULbl")
        self.numONULbl.setGeometry(QRect(50,190,63,20))

        self.runsLbl = QLabel(self.groupBox6,"runsLbl")
        self.runsLbl.setGeometry(QRect(40,30,80,20))

        self.heavyLoadLbl = QLabel(self.groupBox6,"heavyLoadLbl")
        self.heavyLoadLbl.setGeometry(QRect(40,250,100,20))

        self.numWdmONULbl = QLabel(self.groupBox6,"numWdmONULbl")
        self.numWdmONULbl.setGeometry(QRect(260,90,120,20))

        self.numUhWdmONULbl = QLabel(self.groupBox6,"numUhWdmONULbl")
        self.numUhWdmONULbl.setGeometry(QRect(260,120,150,20))

        self.numLhWdmONULbl = QLabel(self.groupBox6,"numLhWdmONULbl")
        self.numLhWdmONULbl.setGeometry(QRect(260,150,150,20))

        self.wdmTypeBtnGrp = QButtonGroup(self.groupBox6,"wdmTypeBtnGrp")
        self.wdmTypeBtnGrp.setGeometry(QRect(260,20,200,60))

        self.fixedBtn = QRadioButton(self.wdmTypeBtnGrp,"fixedBtn")
        self.fixedBtn.setGeometry(QRect(10,30,100,20))

        self.tunableBtn = QRadioButton(self.wdmTypeBtnGrp,"tunableBtn")
        self.tunableBtn.setGeometry(QRect(110,30,80,20))

        self.buttonGroup8 = QButtonGroup(self.groupBox6,"buttonGroup8")
        self.buttonGroup8.setGeometry(QRect(260,190,180,50))

        self.fpdOnBtn = QRadioButton(self.buttonGroup8,"fpdOnBtn")
        self.fpdOnBtn.setGeometry(QRect(110,20,60,22))

        self.fpdOffBtn = QRadioButton(self.buttonGroup8,"fpdOffBtn")
        self.fpdOffBtn.setGeometry(QRect(20,20,60,22))

        self.numLhWdmONUEdit = QLineEdit(self.groupBox6,"numLhWdmONUEdit")
        self.numLhWdmONUEdit.setGeometry(QRect(400,150,70,22))

        self.numUhWdmONUEdit = QLineEdit(self.groupBox6,"numUhWdmONUEdit")
        self.numUhWdmONUEdit.setGeometry(QRect(400,120,70,22))

        self.numWdmONUEdit = QLineEdit(self.groupBox6,"numWdmONUEdit")
        self.numWdmONUEdit.setGeometry(QRect(400,90,70,21))

        self.fpdValueEdit = QLineEdit(self.groupBox6,"fpdValueEdit")
        self.fpdValueEdit.setGeometry(QRect(390,250,80,22))

        self.maxPropDelayEdit = QLineEdit(self.groupBox6,"maxPropDelayEdit")
        self.maxPropDelayEdit.setGeometry(QRect(390,280,80,21))

        self.maxPropDelayLbl = QLabel(self.groupBox6,"maxPropDelayLbl")
        self.maxPropDelayLbl.setGeometry(QRect(250,280,140,20))

        self.linkSpdLbl = QLabel(self.groupBox6,"linkSpdLbl")
        self.linkSpdLbl.setGeometry(QRect(40,100,80,20))

        self.linkSpdEdit = QLineEdit(self.groupBox6,"linkSpdEdit")
        self.linkSpdEdit.setGeometry(QRect(140,100,100,21))

        self.simTimeLbl = QLabel(self.groupBox6,"simTimeLbl")
        self.simTimeLbl.setGeometry(QRect(50,60,70,20))

        self.simTimeEdit = QLineEdit(self.groupBox6,"simTimeEdit")
        self.simTimeEdit.setGeometry(QRect(140,60,100,23))

        self.indexMaxIncreaseButton = QPushButton(self,"indexMaxIncreaseButton")
        self.indexMaxIncreaseButton.setGeometry(QRect(450,730,30,20))

        self.indexMaxDecreaseButton = QPushButton(self,"indexMaxDecreaseButton")
        self.indexMaxDecreaseButton.setGeometry(QRect(410,730,30,20))

        self.indexDecreaseButton = QPushButton(self,"indexDecreaseButton")
        self.indexDecreaseButton.setGeometry(QRect(350,760,30,30))

        self.queueIndexSlotEdit = QLineEdit(self,"queueIndexSlotEdit")
        self.queueIndexSlotEdit.setGeometry(QRect(390,760,30,30))
        self.queueIndexSlotEdit.setReadOnly(1)

        self.frameRateEdit = QLineEdit(self,"frameRateEdit")
        self.frameRateEdit.setEnabled(0)
        self.frameRateEdit.setGeometry(QRect(790,310,40,22))

        self.indexIncreaseButton = QPushButton(self,"indexIncreaseButton")
        self.indexIncreaseButton.setGeometry(QRect(430,760,30,30))

        self.parallelSimsEdit = QLineEdit(self,"parallelSimsEdit")
        self.parallelSimsEdit.setGeometry(QRect(790,780,40,23))

        self.parallelSimsLbl = QLabel(self,"parallelSimsLbl")
        self.parallelSimsLbl.setGeometry(QRect(700,780,80,20))

        self.svButtonGroup = QButtonGroup(self,"svButtonGroup")
        self.svButtonGroup.setEnabled(0)
        self.svButtonGroup.setGeometry(QRect(500,720,170,160))
        svButtonGroup_font = QFont(self.svButtonGroup.font())
        self.svButtonGroup.setFont(svButtonGroup_font)

        self.svDropSensitivity = QLineEdit(self.svButtonGroup,"svDropSensitivity")
        self.svDropSensitivity.setEnabled(0)
        self.svDropSensitivity.setGeometry(QRect(120,62,40,21))
        self.svDropSensitivity.setAlignment(QLineEdit.AlignRight)

        self.svDropThresholdEdit = QLineEdit(self.svButtonGroup,"svDropThresholdEdit")
        self.svDropThresholdEdit.setEnabled(0)
        self.svDropThresholdEdit.setGeometry(QRect(120,40,40,21))
        self.svDropThresholdEdit.setAlignment(QLineEdit.AlignRight)

        self.svDropStepMinBound = QLineEdit(self.svButtonGroup,"svDropStepMinBound")
        self.svDropStepMinBound.setEnabled(0)
        self.svDropStepMinBound.setGeometry(QRect(80,106,80,21))
        self.svDropStepMinBound.setAlignment(QLineEdit.AlignRight)

        self.svDropStep_NumMAValues = QLineEdit(self.svButtonGroup,"svDropStep_NumMAValues")
        self.svDropStep_NumMAValues.setEnabled(0)
        self.svDropStep_NumMAValues.setGeometry(QRect(120,84,40,21))
        self.svDropStep_NumMAValues.setAlignment(QLineEdit.AlignRight)

        self.svDropMinBoundLabel = QLabel(self.svButtonGroup,"svDropMinBoundLabel")
        self.svDropMinBoundLabel.setGeometry(QRect(4,107,68,20))

        self.svDropNone = QRadioButton(self.svButtonGroup,"svDropNone")
        self.svDropNone.setGeometry(QRect(20,20,90,22))
        self.svDropNone.setChecked(1)

        self.svDropThreshold = QRadioButton(self.svButtonGroup,"svDropThreshold")
        self.svDropThreshold.setGeometry(QRect(20,40,90,22))

        self.svDropDynamic = QRadioButton(self.svButtonGroup,"svDropDynamic")
        self.svDropDynamic.setGeometry(QRect(20,60,90,22))
        self.svDropDynamic.setChecked(0)

        self.svDropStepThreshold = QRadioButton(self.svButtonGroup,"svDropStepThreshold")
        self.svDropStepThreshold.setGeometry(QRect(20,80,90,22))
        self.svDropStepThreshold.setChecked(0)

        self.svDropMaxBoundLabel = QLabel(self.svButtonGroup,"svDropMaxBoundLabel")
        self.svDropMaxBoundLabel.setEnabled(0)
        self.svDropMaxBoundLabel.setGeometry(QRect(4,130,71,20))

        self.svDropStepMaxBound = QLineEdit(self.svButtonGroup,"svDropStepMaxBound")
        self.svDropStepMaxBound.setEnabled(0)
        self.svDropStepMaxBound.setGeometry(QRect(80,129,80,21))
        self.svDropStepMaxBound.setFrameShape(QLineEdit.LineEditPanel)
        self.svDropStepMaxBound.setAlignment(QLineEdit.AlignRight)

        self.oltTypeBtnGrp = QButtonGroup(self,"oltTypeBtnGrp")
        self.oltTypeBtnGrp.setGeometry(QRect(10,70,550,210))
        oltTypeBtnGrp_font = QFont(self.oltTypeBtnGrp.font())
        self.oltTypeBtnGrp.setFont(oltTypeBtnGrp_font)

        self.lfjlnfBtn = QRadioButton(self.oltTypeBtnGrp,"lfjlnfBtn")
        self.lfjlnfBtn.setGeometry(QRect(20,80,80,21))

        self.lfjsptBtn = QRadioButton(self.oltTypeBtnGrp,"lfjsptBtn")
        self.lfjsptBtn.setGeometry(QRect(20,60,80,20))

        self.intvlLfjlnfBtn = QRadioButton(self.oltTypeBtnGrp,"intvlLfjlnfBtn")
        self.intvlLfjlnfBtn.setGeometry(QRect(140,80,130,20))

        self.intvlLfjsptBtn = QRadioButton(self.oltTypeBtnGrp,"intvlLfjsptBtn")
        self.intvlLfjsptBtn.setGeometry(QRect(140,60,140,20))

        self.intvlLfjlptBtn = QRadioButton(self.oltTypeBtnGrp,"intvlLfjlptBtn")
        self.intvlLfjlptBtn.setGeometry(QRect(140,40,130,20))

        self.jitLfjsptBtn = QRadioButton(self.oltTypeBtnGrp,"jitLfjsptBtn")
        self.jitLfjsptBtn.setGeometry(QRect(290,60,112,21))

        self.jitLfjlptBtn = QRadioButton(self.oltTypeBtnGrp,"jitLfjlptBtn")
        self.jitLfjlptBtn.setGeometry(QRect(290,40,112,21))

        self.apsBtn = QRadioButton(self.oltTypeBtnGrp,"apsBtn")
        self.apsBtn.setGeometry(QRect(420,140,60,21))

        self.lfjBtn = QRadioButton(self.oltTypeBtnGrp,"lfjBtn")
        self.lfjBtn.setGeometry(QRect(420,120,50,21))

        self.leastAssignedBtn = QRadioButton(self.oltTypeBtnGrp,"leastAssignedBtn")
        self.leastAssignedBtn.setGeometry(QRect(420,100,120,21))

        self.jitTestBtn = QRadioButton(self.oltTypeBtnGrp,"jitTestBtn")
        self.jitTestBtn.setGeometry(QRect(420,60,90,21))

        self.textLabel4 = QLabel(self.oltTypeBtnGrp,"textLabel4")
        self.textLabel4.setGeometry(QRect(300,20,70,20))

        self.textLabel5 = QLabel(self.oltTypeBtnGrp,"textLabel5")
        self.textLabel5.setGeometry(QRect(430,20,40,20))

        self.textLabel2 = QLabel(self.oltTypeBtnGrp,"textLabel2")
        self.textLabel2.setGeometry(QRect(30,20,61,20))

        self.lfjlptBtn = QRadioButton(self.oltTypeBtnGrp,"lfjlptBtn")
        self.lfjlptBtn.setGeometry(QRect(20,40,80,21))

        self.lpdBtn = QRadioButton(self.oltTypeBtnGrp,"lpdBtn")
        self.lpdBtn.setGeometry(QRect(20,120,112,23))

        self.eafBtn = QRadioButton(self.oltTypeBtnGrp,"eafBtn")
        self.eafBtn.setGeometry(QRect(20,140,70,21))

        self.eaafBtn = QRadioButton(self.oltTypeBtnGrp,"eaafBtn")
        self.eaafBtn.setGeometry(QRect(20,160,80,21))

        self.spdBtn = QRadioButton(self.oltTypeBtnGrp,"spdBtn")
        self.spdBtn.setGeometry(QRect(20,100,112,23))

        self.spdLptBtn = QRadioButton(self.oltTypeBtnGrp,"spdLptBtn")
        self.spdLptBtn.setGeometry(QRect(20,180,100,22))

        self.jitLfjlnfBtn = QRadioButton(self.oltTypeBtnGrp,"jitLfjlnfBtn")
        self.jitLfjlnfBtn.setGeometry(QRect(290,80,112,21))

        self.jitSpdBtn = QRadioButton(self.oltTypeBtnGrp,"jitSpdBtn")
        self.jitSpdBtn.setGeometry(QRect(290,100,111,22))

        self.jitEafBtn = QRadioButton(self.oltTypeBtnGrp,"jitEafBtn")
        self.jitEafBtn.setGeometry(QRect(290,140,121,22))

        self.intvlEaafBtn = QRadioButton(self.oltTypeBtnGrp,"intvlEaafBtn")
        self.intvlEaafBtn.setGeometry(QRect(140,160,121,22))

        self.textLabel3 = QLabel(self.oltTypeBtnGrp,"textLabel3")
        self.textLabel3.setGeometry(QRect(150,20,100,20))

        self.nascBtn = QRadioButton(self.oltTypeBtnGrp,"nascBtn")
        self.nascBtn.setGeometry(QRect(420,40,60,21))

        self.ipactBtn = QRadioButton(self.oltTypeBtnGrp,"ipactBtn")
        self.ipactBtn.setGeometry(QRect(420,80,70,21))

        self.jitEaafBtn = QRadioButton(self.oltTypeBtnGrp,"jitEaafBtn")
        self.jitEaafBtn.setGeometry(QRect(290,160,121,22))

        self.intvlEafBtn = QRadioButton(self.oltTypeBtnGrp,"intvlEafBtn")
        self.intvlEafBtn.setGeometry(QRect(140,140,121,22))

        self.jitLpdBtn = QRadioButton(self.oltTypeBtnGrp,"jitLpdBtn")
        self.jitLpdBtn.setGeometry(QRect(290,120,111,22))

        self.ipactpsfBtn = QRadioButton(self.oltTypeBtnGrp,"ipactpsfBtn")
        self.ipactpsfBtn.setEnabled(0)
        self.ipactpsfBtn.setGeometry(QRect(420,180,100,21))
        self.ipactpsfBtn.setChecked(1)

        self.scalableVideoBox = QButtonGroup(self,"scalableVideoBox")
        self.scalableVideoBox.setEnabled(0)
        self.scalableVideoBox.setGeometry(QRect(700,720,130,50))
        self.scalableVideoBox.setMargin(0)

        self.svOffBtn = QRadioButton(self.scalableVideoBox,"svOffBtn")
        self.svOffBtn.setGeometry(QRect(10,20,50,22))
        self.svOffBtn.setChecked(1)

        self.svOnBtn = QRadioButton(self.scalableVideoBox,"svOnBtn")
        self.svOnBtn.setGeometry(QRect(70,20,40,22))

        self.AuxLabel1 = QLabel(self,"AuxLabel1")
        self.AuxLabel1.setEnabled(1)
        self.AuxLabel1.setGeometry(QRect(50,800,340,63))

        self.languageChange()

        self.resize(QSize(860,887).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.cancelBtn,SIGNAL("pressed()"),self.cancelBtn_pressed)
        self.connect(self.launchBtn,SIGNAL("pressed()"),self.launchBtn_pressed)
        self.connect(self.loginBtn,SIGNAL("pressed()"),self.loginBtn_pressed)
        self.connect(self.logoutBtn,SIGNAL("pressed()"),self.logoutBtn_pressed)
        self.connect(self.vtOnBtn,SIGNAL("clicked()"),self.vtOnBtn_checked)
        self.connect(self.vtOffBtn,SIGNAL("clicked()"),self.vtOffBtn_checked)
        self.connect(self.changeTraceBtn,SIGNAL("pressed()"),self.changeTraceBtn_pressed)
        self.connect(self.vsOffBtn,SIGNAL("clicked()"),self.vsOffBtn_checked)
        self.connect(self.vsOnBtn,SIGNAL("clicked()"),self.vsOnBtn_checked)
        self.connect(self.pvtOffBtn,SIGNAL("clicked()"),self.pvtOffBtn_checked)
        self.connect(self.pvtOnBtn,SIGNAL("clicked()"),self.pvtOnBtn_checked)
        self.connect(self.saveTimeButton,SIGNAL("released()"),self.dbaLimitedBtn.toggle)
        self.connect(self.saveTimeButton,SIGNAL("released()"),self.ipactpsfBtn.toggle)
        self.connect(self.saveTimeButton,SIGNAL("released()"),self.dbaLimitedVideoBtn.toggle)
        self.connect(self.saveTimeButton,SIGNAL("released()"),self.pnBtn.toggle)
        self.connect(self.svOffBtn,SIGNAL("clicked()"),self.svOffBtn_checked)
        self.connect(self.svOnBtn,SIGNAL("clicked()"),self.svOnBtn_checked)
        self.connect(self.indexMaxIncreaseButton,SIGNAL("pressed()"),self.indexMaxIncreaseButton_pressed)
        self.connect(self.indexMaxDecreaseButton,SIGNAL("pressed()"),self.indexMaxDecreaseButton_pressed)
        self.connect(self.indexIncreaseButton,SIGNAL("pressed()"),self.indexIncreaseButton_pressed)
        self.connect(self.indexDecreaseButton,SIGNAL("pressed()"),self.indexDecreaseButton_pressed)

        self.setTabOrder(self.passwordEdit,self.loginBtn)
        self.setTabOrder(self.loginBtn,self.simIdEdit)
        self.setTabOrder(self.simIdEdit,self.hostEdit)
        self.setTabOrder(self.hostEdit,self.lfjlptBtn)
        self.setTabOrder(self.lfjlptBtn,self.lfjsptBtn)
        self.setTabOrder(self.lfjsptBtn,self.lfjlnfBtn)
        self.setTabOrder(self.lfjlnfBtn,self.eafBtn)
        self.setTabOrder(self.eafBtn,self.eaafBtn)
        self.setTabOrder(self.eaafBtn,self.intvlLfjlptBtn)
        self.setTabOrder(self.intvlLfjlptBtn,self.intvlLfjsptBtn)
        self.setTabOrder(self.intvlLfjsptBtn,self.intvlLfjlnfBtn)
        self.setTabOrder(self.intvlLfjlnfBtn,self.intvlEafBtn)
        self.setTabOrder(self.intvlEafBtn,self.intvlEaafBtn)
        self.setTabOrder(self.intvlEaafBtn,self.jitLfjlptBtn)
        self.setTabOrder(self.jitLfjlptBtn,self.jitLfjsptBtn)
        self.setTabOrder(self.jitLfjsptBtn,self.jitLfjlnfBtn)
        self.setTabOrder(self.jitLfjlnfBtn,self.jitEafBtn)
        self.setTabOrder(self.jitEafBtn,self.jitEaafBtn)
        self.setTabOrder(self.jitEaafBtn,self.nascBtn)
        self.setTabOrder(self.nascBtn,self.jitTestBtn)
        self.setTabOrder(self.jitTestBtn,self.ipactBtn)
        self.setTabOrder(self.ipactBtn,self.leastAssignedBtn)
        self.setTabOrder(self.leastAssignedBtn,self.lfjBtn)
        self.setTabOrder(self.lfjBtn,self.apsBtn)
        self.setTabOrder(self.apsBtn,self.starveThreshEdit)
        self.setTabOrder(self.starveThreshEdit,self.acwEdit)
        self.setTabOrder(self.acwEdit,self.npoEdit)
        self.setTabOrder(self.npoEdit,self.schedulerMaxWinChkBox)
        self.setTabOrder(self.schedulerMaxWinChkBox,self.schedulerNumSlotEdit)
        self.setTabOrder(self.schedulerNumSlotEdit,self.schedulerSlotSizeEdit)
        self.setTabOrder(self.schedulerSlotSizeEdit,self.dbaGatedBtn)
        self.setTabOrder(self.dbaGatedBtn,self.dbaLimitedBtn)
        self.setTabOrder(self.dbaLimitedBtn,self.dbaFixedBtn)
        self.setTabOrder(self.dbaFixedBtn,self.dbaExcessBtn)
        self.setTabOrder(self.dbaExcessBtn,self.fixedGrantSizeEdit)
        self.setTabOrder(self.fixedGrantSizeEdit,self.maxGrantSizeEdit)
        self.setTabOrder(self.maxGrantSizeEdit,self.linkSpdEdit)
        self.setTabOrder(self.linkSpdEdit,self.simTimeEdit)
        self.setTabOrder(self.simTimeEdit,self.tuningTimeEdit)
        self.setTabOrder(self.tuningTimeEdit,self.grdTimeEdit)
        self.setTabOrder(self.grdTimeEdit,self.numONUEdit)
        self.setTabOrder(self.numONUEdit,self.numHvyONUEdit)
        self.setTabOrder(self.numHvyONUEdit,self.numWdmONUEdit)
        self.setTabOrder(self.numWdmONUEdit,self.numUhWdmONUEdit)
        self.setTabOrder(self.numUhWdmONUEdit,self.numLhWdmONUEdit)
        self.setTabOrder(self.numLhWdmONUEdit,self.fixedBtn)
        self.setTabOrder(self.fixedBtn,self.tunableBtn)
        self.setTabOrder(self.tunableBtn,self.fpdOffBtn)
        self.setTabOrder(self.fpdOffBtn,self.fpdOnBtn)
        self.setTabOrder(self.fpdOnBtn,self.fpdValueEdit)
        self.setTabOrder(self.fpdValueEdit,self.maxPropDelayEdit)
        self.setTabOrder(self.maxPropDelayEdit,self.pnBtn)
        self.setTabOrder(self.pnBtn,self.ssBtn)
        self.setTabOrder(self.ssBtn,self.hurstParamEdit)
        self.setTabOrder(self.hurstParamEdit,self.numStrmsEdit)
        self.setTabOrder(self.numStrmsEdit,self.startLoadEdit)
        self.setTabOrder(self.startLoadEdit,self.endLoadEdit)
        self.setTabOrder(self.endLoadEdit,self.loadIncrEdit)
        self.setTabOrder(self.loadIncrEdit,self.startLambdaEdit)
        self.setTabOrder(self.startLambdaEdit,self.endLambdaEdit)
        self.setTabOrder(self.endLambdaEdit,self.ttOffBtn)
        self.setTabOrder(self.ttOffBtn,self.ttOnBtn)
        self.setTabOrder(self.ttOnBtn,self.grtOffBtn)
        self.setTabOrder(self.grtOffBtn,self.grtOnBtn)
        self.setTabOrder(self.grtOnBtn,self.gtOffBtn)
        self.setTabOrder(self.gtOffBtn,self.gtOnBtn)
        self.setTabOrder(self.gtOnBtn,self.launchBtn)
        self.setTabOrder(self.launchBtn,self.cancelBtn)
        self.setTabOrder(self.cancelBtn,self.usernameEdit)
        self.setTabOrder(self.usernameEdit,self.lpdBtn)
        self.setTabOrder(self.lpdBtn,self.spdBtn)
        self.setTabOrder(self.spdBtn,self.spdLptBtn)
        self.setTabOrder(self.spdLptBtn,self.jitSpdBtn)
        self.setTabOrder(self.jitSpdBtn,self.jitLpdBtn)
        self.setTabOrder(self.jitLpdBtn,self.heavyLoadEdit)
        self.setTabOrder(self.heavyLoadEdit,self.runsEdit)
        self.setTabOrder(self.runsEdit,self.logoutBtn)


    def languageChange(self):
        self.setCaption(self.__tr("Simulation Initialization"))
        self.simIdLbl.setText(self.__tr("Simulation ID"))
        self.passwordLbl.setText(self.__tr("Password"))
        self.loginBtn.setText(self.__tr("Login"))
        self.logoutBtn.setText(self.__tr("Logout"))
        self.usernameLbl.setText(self.__tr("Username"))
        self.hostLbl.setText(self.__tr("HOST"))
        self.dbaParamsBox.setTitle(self.__tr("Grant Sizing Parameters"))
        self.fixedGrantSizeLbl.setText(self.__tr("FIXED_GRANT_SIZE"))
        self.maxGrantSizeLbl.setText(self.__tr("MAX_GRANT_SIZE"))
        self.schedulerParamsBox.setTitle(self.__tr("Grant Scheduling Parameters"))
        self.starveThreshLbl.setText(self.__tr("STARVE_THRESH"))
        self.acwLbl.setText(self.__tr("AVAIL_COST_WEIGHT"))
        self.schedulerMaxWinChkBox.setText(self.__tr("SCHEDULER_MAX_WIN"))
        self.npoLbl.setText(self.__tr("NUM_PREFERRED_ONU"))
        self.schedulerNumSlotLbl.setText(self.__tr("SCHEDULER_NUM_SLOT"))
        self.schedulerSlotSizeLbl.setText(self.__tr("SCHEDULER_SLOT_SIZE"))
        self.lambdaParamsBox.setTitle(self.__tr("Lambda Parameters"))
        self.startLambdaLbl.setText(self.__tr("START_LAMBDA"))
        self.endLambdaLbl.setText(self.__tr("END_LAMBDA"))
        self.ssParamsBox.setTitle(self.__tr("Self-Similar Parameters"))
        self.numStrmsLbl.setText(self.__tr("NUM_STREAMS"))
        self.hurstParamLbl.setText(self.__tr("HURST_PARAM"))
        self.loadParamsBox.setTitle(self.__tr("Load Parameters"))
        self.startLoadLbl.setText(self.__tr("START_LOAD"))
        self.endLoadLbl.setText(self.__tr("END_LOAD"))
        self.loadIncrLbl.setText(self.__tr("LOAD_INCR"))
        self.FRateLbl.setText(self.__tr("Frame Rate"))
        self.videoStartBox.setTitle(self.__tr("Random Video Start"))
        self.timeShiftLbl.setText(self.__tr("Time Shift (ms):"))
        self.vsOffBtn.setText(self.__tr("OFF"))
        self.vsOnBtn.setText(self.__tr("ON"))
        self.timeShiftEdit.setText(self.__tr("0.0"))
        self.videoTraceFileLbl.setText(self.__tr("Video Trace File"))
        self.changeTraceBtn.setText(self.__tr("Change Trace"))
        self.buttonGroup4_2.setTitle(self.__tr("GET_TAIL"))
        self.gtOffBtn.setText(self.__tr("OFF"))
        self.gtOnBtn.setText(self.__tr("ON"))
        self.buttonGroup7.setTitle(self.__tr("GRANT_TRACE"))
        self.grtOffBtn.setText(self.__tr("OFF"))
        self.grtOnBtn.setText(self.__tr("ON"))
        self.VideoDBABtnGroup.setTitle(self.__tr("Grant Sizing (Video)"))
        self.dbaFixedVideoBtn.setText(self.__tr("FIXED"))
        self.dbaGatedVideoBtn.setText(self.__tr("GATED"))
        self.dbaLimitedVideoBtn.setText(self.__tr("LIMITED"))
        self.buttonGroup6.setTitle(self.__tr("Grant Sizing (Data)"))
        self.dbaExcessBtn.setText(self.__tr("EXCESS"))
        self.dbaGatedBtn.setText(self.__tr("GATED"))
        self.dbaFixedBtn.setText(self.__tr("FIXED"))
        self.dbaLimitedBtn.setText(self.__tr("LIMITED"))
        self.buttonGroup5.setTitle(self.__tr("TIME_TRACE"))
        self.ttOffBtn.setText(self.__tr("OFF"))
        self.ttOnBtn.setText(self.__tr("ON"))
        self.dataTrafficTypeBox.setTitle(self.__tr("Data Traffic Type"))
        self.ssBtn.setText(self.__tr("Self-Similar"))
        self.pnBtn.setText(self.__tr("Poisson"))
        self.predictTrafficBox.setTitle(self.__tr("Predict Video Traffic"))
        self.PredTypeLbl.setText(self.__tr("Pred. Type:"))
        self.pvtOffBtn.setText(self.__tr("OFF"))
        self.PredTypeEdit.setText(self.__tr("FFBI"))
        self.pvtOnBtn.setText(self.__tr("ON"))
        self.videoTrafficBox.setTitle(self.__tr("Video Traffic"))
        self.vtOffBtn.setText(self.__tr("OFF"))
        self.vtOnBtn.setText(self.__tr("ON"))
        self.launchBtn.setText(self.__tr("LAUNCH"))
        self.cancelBtn.setText(self.__tr("CANCEL"))
        self.saveTimeButton.setText(QString.null)
        self.groupBox6.setTitle(self.__tr("Network Parameters"))
        self.fpdValueLbl.setText(self.__tr("PROP_DELAY_VALUE"))
        self.numHvyONULbl.setText(self.__tr("NUM_HEAVY_ONU"))
        self.tuningTimeLbl.setText(self.__tr("TUNING_TIME"))
        self.grdTimeLbl.setText(self.__tr("GUARD_TIME"))
        self.numONULbl.setText(self.__tr("NUM_ONU"))
        self.runsLbl.setText(self.__tr("NUM_RUNS"))
        self.heavyLoadLbl.setText(self.__tr("HEAVY_LOAD"))
        self.numWdmONULbl.setText(self.__tr("NUM_WDM_ONU"))
        self.numUhWdmONULbl.setText(self.__tr("NUM_UH_WDM_ONU"))
        self.numLhWdmONULbl.setText(self.__tr("NUM_LH_WDM_ONU"))
        self.wdmTypeBtnGrp.setTitle(self.__tr("WDM Type"))
        self.fixedBtn.setText(self.__tr("Fixed Array"))
        self.tunableBtn.setText(self.__tr("Tunable"))
        self.buttonGroup8.setTitle(self.__tr("FIXED_PROP_DELAY"))
        self.fpdOnBtn.setText(self.__tr("ON"))
        self.fpdOffBtn.setText(self.__tr("OFF"))
        self.maxPropDelayLbl.setText(self.__tr("MAX_PROP_DELAY"))
        self.linkSpdLbl.setText(self.__tr("LINK_SPEED"))
        self.simTimeLbl.setText(self.__tr("SIM_TIME"))
        self.indexMaxIncreaseButton.setText(self.__tr("+"))
        self.indexMaxDecreaseButton.setText(self.__tr("--"))
        self.indexDecreaseButton.setText(self.__tr("<-"))
        self.queueIndexSlotEdit.setText(self.__tr("1"))
        self.frameRateEdit.setText(self.__tr("24.0"))
        self.indexIncreaseButton.setText(self.__tr("->"))
        self.parallelSimsEdit.setText(self.__tr("1"))
        self.parallelSimsLbl.setText(self.__tr("Parallel Sims"))
        self.svButtonGroup.setTitle(self.__tr("SV Packet Dropping"))
        self.svDropSensitivity.setText(self.__tr("1.0"))
        self.svDropThresholdEdit.setText(self.__tr("4"))
        self.svDropStepMinBound.setText(self.__tr("0.0005"))
        self.svDropStep_NumMAValues.setText(self.__tr("5"))
        self.svDropMinBoundLabel.setText(self.__tr("Min Bound"))
        self.svDropNone.setText(self.__tr("None"))
        self.svDropThreshold.setText(self.__tr("Drop if >"))
        self.svDropDynamic.setText(self.__tr("Dynamic"))
        self.svDropStepThreshold.setText(self.__tr("Step"))
        self.svDropMaxBoundLabel.setText(self.__tr("Max Bound"))
        self.svDropStepMaxBound.setText(self.__tr("0.005"))
        self.oltTypeBtnGrp.setTitle(self.__tr("Grant Scheduling"))
        self.lfjlnfBtn.setText(self.__tr("LFJ-LNF"))
        self.lfjsptBtn.setText(self.__tr("LFJ-SPT"))
        self.intvlLfjlnfBtn.setText(self.__tr("INTVL LFJ-LNF"))
        self.intvlLfjsptBtn.setText(self.__tr("INTVL LFJ-SPT"))
        self.intvlLfjlptBtn.setText(self.__tr("INTVL LFJ-LPT"))
        self.jitLfjsptBtn.setText(self.__tr("JIT LFJ-SPT"))
        self.jitLfjlptBtn.setText(self.__tr("JIT LFJ-LPT"))
        self.apsBtn.setText(self.__tr("APS"))
        self.lfjBtn.setText(self.__tr("LFJ"))
        self.leastAssignedBtn.setText(self.__tr("Least Assigned"))
        self.jitTestBtn.setText(self.__tr("JIT TEST"))
        self.textLabel4.setText(self.__tr("Online JIT"))
        self.textLabel5.setText(self.__tr("Misc"))
        self.textLabel2.setText(self.__tr("Offline"))
        self.lfjlptBtn.setText(self.__tr("LFJ-LPT"))
        self.lpdBtn.setText(self.__tr("LPD"))
        self.eafBtn.setText(self.__tr("EAF"))
        self.eaafBtn.setText(self.__tr("EAAF"))
        self.spdBtn.setText(self.__tr("SPD"))
        self.spdLptBtn.setText(self.__tr("SPD-LPT"))
        self.jitLfjlnfBtn.setText(self.__tr("JIT LFJ-LNF"))
        self.jitSpdBtn.setText(self.__tr("JIT SPD"))
        self.jitEafBtn.setText(self.__tr("JIT EAF"))
        self.intvlEaafBtn.setText(self.__tr("INTVL EAAF"))
        self.textLabel3.setText(self.__tr("Online Interval"))
        self.nascBtn.setText(self.__tr("NASC"))
        self.ipactBtn.setText(self.__tr("IPACT"))
        self.jitEaafBtn.setText(self.__tr("JIT EAAF"))
        self.intvlEafBtn.setText(self.__tr("INTVL EAF"))
        self.jitLpdBtn.setText(self.__tr("JIT LPD"))
        self.ipactpsfBtn.setText(self.__tr("IPACT-PSF"))
        self.scalableVideoBox.setTitle(self.__tr("Scalable Video"))
        self.svOffBtn.setText(self.__tr("OFF"))
        self.svOnBtn.setText(self.__tr("ON"))
        self.AuxLabel1.setText(self.__tr("Please note:\n"
"The \"Drop if >\" option for scalable video assumes\n"
"that the base layer is layer 1. Thus, if you \"Drop if > 1\",\n"
"you're dropping everything except the base layer."))


    def cancelBtn_pressed(self):
        print "SimInitForm.cancelBtn_pressed(): Not implemented yet"

    def launchBtn_pressed(self):
        print "SimInitForm.launchBtn_pressed(): Not implemented yet"

    def loginBtn_pressed(self):
        print "SimInitForm.loginBtn_pressed(): Not implemented yet"

    def logoutBtn_pressed(self):
        print "SimInitForm.logoutBtn_pressed(): Not implemented yet"

    def vtOnBtn_checked(self):
        print "SimInitForm.vtOnBtn_checked(): Not implemented yet"

    def vtOffBtn_checked(self):
        print "SimInitForm.vtOffBtn_checked(): Not implemented yet"

    def changeTraceBtn_pressed(self):
        print "SimInitForm.changeTraceBtn_pressed(): Not implemented yet"

    def vsOffBtn_checked(self):
        print "SimInitForm.vsOffBtn_checked(): Not implemented yet"

    def vsOnBtn_checked(self):
        print "SimInitForm.vsOnBtn_checked(): Not implemented yet"

    def pvtOffBtn_checked(self):
        print "SimInitForm.pvtOffBtn_checked(): Not implemented yet"

    def pvtOnBtn_checked(self):
        print "SimInitForm.pvtOnBtn_checked(): Not implemented yet"

    def svOnBtn_checked(self):
        print "SimInitForm.svOnBtn_checked(): Not implemented yet"

    def svOffBtn_checked(self):
        print "SimInitForm.svOffBtn_checked(): Not implemented yet"

    def indexMaxIncreaseButton_pressed(self):
        print "SimInitForm.indexMaxIncreaseButton_pressed(): Not implemented yet"

    def indexMaxDecreaseButton_pressed(self):
        print "SimInitForm.indexMaxDecreaseButton_pressed(): Not implemented yet"

    def indexIncreaseButton_pressed(self):
        print "SimInitForm.indexIncreaseButton_pressed(): Not implemented yet"

    def indexDecreaseButton_pressed(self):
        print "SimInitForm.indexDecreaseButton_pressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("SimInitForm",s,c)
