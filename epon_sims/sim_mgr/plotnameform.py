# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotnameform.ui'
#
# Created: Sat Jan 13 14:36:37 2018
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = [
"15 15 2 1",
"# c #000000",
". c #ffffff",
"...............",
"......##.......",
"......##.......",
"......##.......",
"......##.......",
"......##.......",
".############..",
".############..",
"......##.......",
"......##.......",
"......##.......",
"......##.......",
"......##.......",
"...............",
"..............."
]
image1_data = [
"18 18 2 1",
"# c #000000",
". c #ffffff",
"..................",
".#............#...",
".##..........##...",
"..##........##....",
"...##......##.....",
"....##....##......",
".....##..##.......",
"......####........",
".......##.........",
"......####........",
".....##..##.......",
"....##....##......",
"...##......##.....",
"..##........##....",
".##..........##...",
"##............##..",
"..................",
".................."
]
image2_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
".##...##...#...",
"..##..##..##...",
"...##.##.##....",
"....######.....",
"..##########...",
"..##########...",
".....####......",
"....######.....",
"...##.##.##....",
"..##..##..##...",
".##...##...#...",
"..............."
]
image3_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
"...............",
"..#########....",
"..#.......#....",
"..#.......#....",
"..#.......#....",
"..#...#...#....",
"..#.......#....",
"..#.......#....",
"..#.......#....",
"..#########....",
"...............",
"..............."
]
image4_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
"...............",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"..#########....",
"...............",
"..............."
]
image5_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
"......#........",
"....##.##......",
"...#.....#.....",
"...#.....#.....",
"..#.......#....",
"..#...#...#....",
"..#.......#....",
"...#.....#.....",
"...#.....#.....",
"....##.##......",
"......#........",
"..............."
]
image6_data = [
"14 12 9 1",
"e c #000000",
"g c #070707",
"b c #0a0a0a",
"d c #0d0d0d",
"a c #242424",
"f c #252525",
"# c #a3a3a3",
"c c #b1b1b1",
". c #ffffff",
"..............",
"..............",
"....#aba#.....",
"...cdeeedc....",
"...feeeeef....",
"...geeeeee....",
"...feeeeef....",
"...cdeeedc....",
"....#aba#.....",
"..............",
"..............",
".............."
]
image7_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
".....###.......",
".....#..#......",
"....#...#......",
"....#....#.....",
"...#.....#.....",
"...#......#....",
"..#...#...#....",
"..#........#...",
".#.........#...",
".###########...",
"...............",
"...............",
"..............."
]
image8_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
".....###.......",
".....####......",
"....#####......",
"....######.....",
"...#######.....",
"...########....",
"..#########....",
"..##########...",
".###########...",
".###########...",
"...............",
"...............",
"..............."
]
image9_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
"...............",
"...............",
"...###########.",
"...#.........#.",
"...#........#..",
"....#...#...#..",
"....#......#...",
".....#.....#...",
".....#....#....",
"......#...#....",
"......#..#.....",
".......###....."
]
image10_data = [
"15 13 2 1",
"# c #000000",
". c #ffffff",
"...............",
"...............",
"...............",
"...###########.",
"...###########.",
"...##########..",
"....#########..",
"....########...",
".....#######...",
".....######....",
"......#####....",
"......####.....",
".......###....."
]

class plotNameForm(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        self.image0 = QPixmap(image0_data)
        self.image1 = QPixmap(image1_data)
        self.image2 = QPixmap(image2_data)
        self.image3 = QPixmap(image3_data)
        self.image4 = QPixmap(image4_data)
        self.image5 = QPixmap(image5_data)
        self.image6 = QPixmap(image6_data)
        self.image7 = QPixmap(image7_data)
        self.image8 = QPixmap(image8_data)
        self.image9 = QPixmap(image9_data)
        self.image10 = QPixmap(image10_data)

        if not name:
            self.setName("plotNameForm")



        self.file1Lbl = QLabel(self,"file1Lbl")
        self.file1Lbl.setGeometry(QRect(10,50,290,20))
        file1Lbl_font = QFont(self.file1Lbl.font())
        self.file1Lbl.setFont(file1Lbl_font)

        self.PlotLegendLbl = QLabel(self,"PlotLegendLbl")
        self.PlotLegendLbl.setGeometry(QRect(370,20,70,20))
        PlotLegendLbl_font = QFont(self.PlotLegendLbl.font())
        self.PlotLegendLbl.setFont(PlotLegendLbl_font)

        self.lineColorCBox1 = QComboBox(0,self,"lineColorCBox1")
        self.lineColorCBox1.setGeometry(QRect(740,50,90,20))

        self.file7Lbl = QLabel(self,"file7Lbl")
        self.file7Lbl.setGeometry(QRect(10,350,290,20))
        file7Lbl_font = QFont(self.file7Lbl.font())
        self.file7Lbl.setFont(file7Lbl_font)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(470,20,60,20))
        textLabel1_font = QFont(self.textLabel1.font())
        self.textLabel1.setFont(textLabel1_font)

        self.LineWidthLbl_2_2 = QLabel(self,"LineWidthLbl_2_2")
        self.LineWidthLbl_2_2.setGeometry(QRect(750,20,60,20))
        LineWidthLbl_2_2_font = QFont(self.LineWidthLbl_2_2.font())
        self.LineWidthLbl_2_2.setFont(LineWidthLbl_2_2_font)

        self.file5Lbl = QLabel(self,"file5Lbl")
        self.file5Lbl.setGeometry(QRect(10,250,290,20))
        file5Lbl_font = QFont(self.file5Lbl.font())
        self.file5Lbl.setFont(file5Lbl_font)

        self.lineColorCBox6 = QComboBox(0,self,"lineColorCBox6")
        self.lineColorCBox6.setGeometry(QRect(740,300,90,20))

        self.lineColorCBox3 = QComboBox(0,self,"lineColorCBox3")
        self.lineColorCBox3.setGeometry(QRect(740,150,90,20))

        self.lineColorCBox2 = QComboBox(0,self,"lineColorCBox2")
        self.lineColorCBox2.setGeometry(QRect(740,100,90,20))

        self.PointSizeLbl = QLabel(self,"PointSizeLbl")
        self.PointSizeLbl.setGeometry(QRect(650,10,40,30))
        PointSizeLbl_font = QFont(self.PointSizeLbl.font())
        self.PointSizeLbl.setFont(PointSizeLbl_font)

        self.lineColorCBox7 = QComboBox(0,self,"lineColorCBox7")
        self.lineColorCBox7.setGeometry(QRect(740,350,90,20))

        self.lineColorCBox5 = QComboBox(0,self,"lineColorCBox5")
        self.lineColorCBox5.setGeometry(QRect(740,250,90,20))

        self.file6Lbl = QLabel(self,"file6Lbl")
        self.file6Lbl.setGeometry(QRect(10,300,290,20))
        file6Lbl_font = QFont(self.file6Lbl.font())
        self.file6Lbl.setFont(file6Lbl_font)

        self.LineWidthLbl_2 = QLabel(self,"LineWidthLbl_2")
        self.LineWidthLbl_2.setGeometry(QRect(700,10,38,40))
        LineWidthLbl_2_font = QFont(self.LineWidthLbl_2.font())
        self.LineWidthLbl_2.setFont(LineWidthLbl_2_font)

        self.PointsLbl = QLabel(self,"PointsLbl")
        self.PointsLbl.setGeometry(QRect(550,20,65,20))
        PointsLbl_font = QFont(self.PointsLbl.font())
        self.PointsLbl.setFont(PointsLbl_font)

        self.lineColorCBox4 = QComboBox(0,self,"lineColorCBox4")
        self.lineColorCBox4.setGeometry(QRect(740,200,90,20))

        self.plotOrder6 = QLineEdit(self,"plotOrder6")
        self.plotOrder6.setGeometry(QRect(480,300,20,22))
        plotOrder6_font = QFont(self.plotOrder6.font())
        self.plotOrder6.setFont(plotOrder6_font)

        self.plotOrder7 = QLineEdit(self,"plotOrder7")
        self.plotOrder7.setGeometry(QRect(480,350,20,22))
        plotOrder7_font = QFont(self.plotOrder7.font())
        self.plotOrder7.setFont(plotOrder7_font)

        self.pointsCBox3 = QComboBox(0,self,"pointsCBox3")
        self.pointsCBox3.setGeometry(QRect(510,150,120,20))

        self.pointsCBox4 = QComboBox(0,self,"pointsCBox4")
        self.pointsCBox4.setGeometry(QRect(510,200,120,20))

        self.pointsCBox5 = QComboBox(0,self,"pointsCBox5")
        self.pointsCBox5.setGeometry(QRect(510,250,120,20))

        self.pointsCBox6 = QComboBox(0,self,"pointsCBox6")
        self.pointsCBox6.setGeometry(QRect(510,300,120,20))

        self.file8Lbl = QLabel(self,"file8Lbl")
        self.file8Lbl.setGeometry(QRect(10,400,290,20))
        file8Lbl_font = QFont(self.file8Lbl.font())
        self.file8Lbl.setFont(file8Lbl_font)

        self.file3Lbl = QLabel(self,"file3Lbl")
        self.file3Lbl.setGeometry(QRect(10,150,290,20))
        file3Lbl_font = QFont(self.file3Lbl.font())
        self.file3Lbl.setFont(file3Lbl_font)

        self.plotOrder1 = QLineEdit(self,"plotOrder1")
        self.plotOrder1.setGeometry(QRect(480,50,20,22))
        plotOrder1_font = QFont(self.plotOrder1.font())
        self.plotOrder1.setFont(plotOrder1_font)

        self.plotOrder2 = QLineEdit(self,"plotOrder2")
        self.plotOrder2.setGeometry(QRect(480,100,20,22))
        plotOrder2_font = QFont(self.plotOrder2.font())
        self.plotOrder2.setFont(plotOrder2_font)

        self.plotOrder3 = QLineEdit(self,"plotOrder3")
        self.plotOrder3.setGeometry(QRect(480,150,20,22))
        plotOrder3_font = QFont(self.plotOrder3.font())
        self.plotOrder3.setFont(plotOrder3_font)

        self.plotOrder4 = QLineEdit(self,"plotOrder4")
        self.plotOrder4.setGeometry(QRect(480,200,20,22))
        plotOrder4_font = QFont(self.plotOrder4.font())
        self.plotOrder4.setFont(plotOrder4_font)

        self.plotOrder5 = QLineEdit(self,"plotOrder5")
        self.plotOrder5.setGeometry(QRect(480,250,20,22))
        plotOrder5_font = QFont(self.plotOrder5.font())
        self.plotOrder5.setFont(plotOrder5_font)

        self.pointSizeCBox1 = QComboBox(0,self,"pointSizeCBox1")
        self.pointSizeCBox1.setGeometry(QRect(640,50,50,20))

        self.pointSizeCBox2 = QComboBox(0,self,"pointSizeCBox2")
        self.pointSizeCBox2.setGeometry(QRect(640,100,50,20))

        self.pointSizeCBox3 = QComboBox(0,self,"pointSizeCBox3")
        self.pointSizeCBox3.setGeometry(QRect(640,150,50,20))

        self.pointSizeCBox4 = QComboBox(0,self,"pointSizeCBox4")
        self.pointSizeCBox4.setGeometry(QRect(640,200,50,20))

        self.pointSizeCBox5 = QComboBox(0,self,"pointSizeCBox5")
        self.pointSizeCBox5.setGeometry(QRect(640,250,50,20))

        self.pointSizeCBox6 = QComboBox(0,self,"pointSizeCBox6")
        self.pointSizeCBox6.setGeometry(QRect(640,300,50,20))

        self.pointSizeCBox7 = QComboBox(0,self,"pointSizeCBox7")
        self.pointSizeCBox7.setGeometry(QRect(640,350,50,20))

        self.lineWidthCBox1 = QComboBox(0,self,"lineWidthCBox1")
        self.lineWidthCBox1.setGeometry(QRect(700,50,30,20))

        self.lineWidthCBox2 = QComboBox(0,self,"lineWidthCBox2")
        self.lineWidthCBox2.setGeometry(QRect(700,100,30,20))

        self.lineWidthCBox3 = QComboBox(0,self,"lineWidthCBox3")
        self.lineWidthCBox3.setGeometry(QRect(700,150,30,20))

        self.lineWidthCBox4 = QComboBox(0,self,"lineWidthCBox4")
        self.lineWidthCBox4.setGeometry(QRect(700,200,30,20))

        self.lineWidthCBox5 = QComboBox(0,self,"lineWidthCBox5")
        self.lineWidthCBox5.setGeometry(QRect(700,250,30,20))

        self.lineWidthCBox6 = QComboBox(0,self,"lineWidthCBox6")
        self.lineWidthCBox6.setGeometry(QRect(700,300,30,20))

        self.lineWidthCBox7 = QComboBox(0,self,"lineWidthCBox7")
        self.lineWidthCBox7.setGeometry(QRect(700,350,30,20))

        self.file4Lbl = QLabel(self,"file4Lbl")
        self.file4Lbl.setGeometry(QRect(10,200,290,20))
        file4Lbl_font = QFont(self.file4Lbl.font())
        self.file4Lbl.setFont(file4Lbl_font)

        self.file3Edit = QLineEdit(self,"file3Edit")
        self.file3Edit.setGeometry(QRect(310,150,160,23))
        file3Edit_font = QFont(self.file3Edit.font())
        self.file3Edit.setFont(file3Edit_font)

        self.file4Edit = QLineEdit(self,"file4Edit")
        self.file4Edit.setGeometry(QRect(310,200,160,23))
        file4Edit_font = QFont(self.file4Edit.font())
        self.file4Edit.setFont(file4Edit_font)

        self.file5Edit = QLineEdit(self,"file5Edit")
        self.file5Edit.setGeometry(QRect(310,250,160,23))
        file5Edit_font = QFont(self.file5Edit.font())
        self.file5Edit.setFont(file5Edit_font)

        self.file6Edit = QLineEdit(self,"file6Edit")
        self.file6Edit.setGeometry(QRect(310,300,160,23))
        file6Edit_font = QFont(self.file6Edit.font())
        self.file6Edit.setFont(file6Edit_font)

        self.file2Lbl = QLabel(self,"file2Lbl")
        self.file2Lbl.setGeometry(QRect(10,100,290,20))
        file2Lbl_font = QFont(self.file2Lbl.font())
        self.file2Lbl.setFont(file2Lbl_font)

        self.file2Edit = QLineEdit(self,"file2Edit")
        self.file2Edit.setGeometry(QRect(310,100,160,23))
        file2Edit_font = QFont(self.file2Edit.font())
        self.file2Edit.setFont(file2Edit_font)

        self.pointsCBox7 = QComboBox(0,self,"pointsCBox7")
        self.pointsCBox7.setGeometry(QRect(510,350,120,20))

        self.file7Edit = QLineEdit(self,"file7Edit")
        self.file7Edit.setGeometry(QRect(310,350,160,23))
        file7Edit_font = QFont(self.file7Edit.font())
        self.file7Edit.setFont(file7Edit_font)

        self.file1Edit = QLineEdit(self,"file1Edit")
        self.file1Edit.setGeometry(QRect(310,50,160,23))
        file1Edit_font = QFont(self.file1Edit.font())
        self.file1Edit.setFont(file1Edit_font)

        self.plotOrder8 = QLineEdit(self,"plotOrder8")
        self.plotOrder8.setGeometry(QRect(480,400,20,22))
        plotOrder8_font = QFont(self.plotOrder8.font())
        self.plotOrder8.setFont(plotOrder8_font)

        self.pointsCBox8 = QComboBox(0,self,"pointsCBox8")
        self.pointsCBox8.setGeometry(QRect(510,400,120,20))

        self.pointSizeCBox8 = QComboBox(0,self,"pointSizeCBox8")
        self.pointSizeCBox8.setGeometry(QRect(640,400,50,20))

        self.lineWidthCBox8 = QComboBox(0,self,"lineWidthCBox8")
        self.lineWidthCBox8.setGeometry(QRect(700,400,30,20))

        self.lineColorCBox8 = QComboBox(0,self,"lineColorCBox8")
        self.lineColorCBox8.setGeometry(QRect(740,400,90,20))

        self.file8Edit = QLineEdit(self,"file8Edit")
        self.file8Edit.setGeometry(QRect(310,400,160,23))
        file8Edit_font = QFont(self.file8Edit.font())
        self.file8Edit.setFont(file8Edit_font)

        self.pointsCBox1 = QComboBox(0,self,"pointsCBox1")
        self.pointsCBox1.setGeometry(QRect(510,50,120,20))

        self.pointsCBox2 = QComboBox(0,self,"pointsCBox2")
        self.pointsCBox2.setGeometry(QRect(510,100,120,20))

        self.lineWidthCBoxChangeAll = QComboBox(0,self,"lineWidthCBoxChangeAll")
        self.lineWidthCBoxChangeAll.setGeometry(QRect(700,460,30,20))

        self.lineColorCBoxChangeAll = QComboBox(0,self,"lineColorCBoxChangeAll")
        self.lineColorCBoxChangeAll.setGeometry(QRect(740,460,90,20))

        self.y_axisPositionLbl = QLabel(self,"y_axisPositionLbl")
        self.y_axisPositionLbl.setEnabled(0)
        self.y_axisPositionLbl.setGeometry(QRect(630,510,90,20))
        y_axisPositionLbl_font = QFont(self.y_axisPositionLbl.font())
        self.y_axisPositionLbl.setFont(y_axisPositionLbl_font)

        self.pointSizeCBoxChangeAll = QComboBox(0,self,"pointSizeCBoxChangeAll")
        self.pointSizeCBoxChangeAll.setGeometry(QRect(640,460,50,20))

        self.pointsCBoxChangeAll = QComboBox(0,self,"pointsCBoxChangeAll")
        self.pointsCBoxChangeAll.setGeometry(QRect(510,460,120,20))

        self.cancelBtn = QPushButton(self,"cancelBtn")
        self.cancelBtn.setGeometry(QRect(540,560,87,30))

        self.legendCBox = QComboBox(0,self,"legendCBox")
        self.legendCBox.setGeometry(QRect(280,510,140,20))

        self.LegendPositioningLbl = QLabel(self,"LegendPositioningLbl")
        self.LegendPositioningLbl.setGeometry(QRect(150,510,120,20))
        LegendPositioningLbl_font = QFont(self.LegendPositioningLbl.font())
        self.LegendPositioningLbl.setFont(LegendPositioningLbl_font)

        self.x_axisEdit = QLineEdit(self,"x_axisEdit")
        self.x_axisEdit.setEnabled(0)
        self.x_axisEdit.setGeometry(QRect(540,510,70,23))
        x_axisEdit_font = QFont(self.x_axisEdit.font())
        self.x_axisEdit.setFont(x_axisEdit_font)

        self.y_axisEdit = QLineEdit(self,"y_axisEdit")
        self.y_axisEdit.setEnabled(0)
        self.y_axisEdit.setGeometry(QRect(720,510,70,23))
        y_axisEdit_font = QFont(self.y_axisEdit.font())
        self.y_axisEdit.setFont(y_axisEdit_font)

        self.x_axisPositionLbl = QLabel(self,"x_axisPositionLbl")
        self.x_axisPositionLbl.setEnabled(0)
        self.x_axisPositionLbl.setGeometry(QRect(450,510,90,20))
        x_axisPositionLbl_font = QFont(self.x_axisPositionLbl.font())
        self.x_axisPositionLbl.setFont(x_axisPositionLbl_font)

        self.doneBtn = QPushButton(self,"doneBtn")
        self.doneBtn.setGeometry(QRect(190,560,87,30))

        self.saveSettingsLbl = QLabel(self,"saveSettingsLbl")
        self.saveSettingsLbl.setEnabled(1)
        self.saveSettingsLbl.setGeometry(QRect(280,440,137,20))
        saveSettingsLbl_font = QFont(self.saveSettingsLbl.font())
        self.saveSettingsLbl.setFont(saveSettingsLbl_font)

        self.SaveTimeButton = QPushButton(self,"SaveTimeButton")
        self.SaveTimeButton.setGeometry(QRect(40,460,71,31))

        self.saveSettingsBtn = QPushButton(self,"saveSettingsBtn")
        self.saveSettingsBtn.setGeometry(QRect(290,460,50,30))

        self.restoreSettingsBtn = QPushButton(self,"restoreSettingsBtn")
        self.restoreSettingsBtn.setGeometry(QRect(350,460,60,31))

        self.languageChange()

        self.resize(QSize(840,614).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.doneBtn,SIGNAL("pressed()"),self.doneBtn_pressed)
        self.connect(self.cancelBtn,SIGNAL("pressed()"),self.cancelBtn_pressed)
        self.connect(self.legendCBox,SIGNAL("activated(int)"),self.LegendPosition_selected)
        self.connect(self.SaveTimeButton,SIGNAL("pressed()"),self.SaveTimeButton_pressed)
        self.connect(self.pointsCBoxChangeAll,SIGNAL("activated(int)"),self.pointsCBoxChangeAll_activated)
        self.connect(self.pointSizeCBoxChangeAll,SIGNAL("activated(int)"),self.pointSizeCBoxChangeAll_activated)
        self.connect(self.lineWidthCBoxChangeAll,SIGNAL("activated(int)"),self.lineWidthCBoxChangeAll_activated)
        self.connect(self.lineColorCBoxChangeAll,SIGNAL("activated(int)"),self.lineColorCBoxChangeAll_activated)
        self.connect(self.saveSettingsBtn,SIGNAL("pressed()"),self.saveSettingsBtn_pressed)
        self.connect(self.restoreSettingsBtn,SIGNAL("pressed()"),self.restoreSettingsBtn_pressed)

        self.setTabOrder(self.file1Edit,self.file2Edit)
        self.setTabOrder(self.file2Edit,self.file3Edit)
        self.setTabOrder(self.file3Edit,self.file4Edit)
        self.setTabOrder(self.file4Edit,self.file5Edit)
        self.setTabOrder(self.file5Edit,self.file6Edit)
        self.setTabOrder(self.file6Edit,self.file7Edit)
        self.setTabOrder(self.file7Edit,self.doneBtn)
        self.setTabOrder(self.doneBtn,self.cancelBtn)


    def languageChange(self):
        self.setCaption(self.__tr("Plot Naming"))
        self.file1Lbl.setText(self.__tr("file1"))
        self.PlotLegendLbl.setText(self.__tr("Plot Legend"))
        self.lineColorCBox1.clear()
        self.lineColorCBox1.insertItem(self.__tr("black"))
        self.lineColorCBox1.insertItem(self.__tr("red"))
        self.lineColorCBox1.insertItem(self.__tr("green"))
        self.lineColorCBox1.insertItem(self.__tr("blue"))
        self.lineColorCBox1.insertItem(self.__tr("purple"))
        self.lineColorCBox1.insertItem(self.__tr("aqua"))
        self.lineColorCBox1.insertItem(self.__tr("brown"))
        self.lineColorCBox1.insertItem(self.__tr("orange"))
        self.lineColorCBox1.insertItem(self.__tr("Light Brown"))
        self.file7Lbl.setText(self.__tr("file7"))
        self.textLabel1.setText(self.__tr("Plot Order"))
        self.LineWidthLbl_2_2.setText(self.__tr("Line Color"))
        self.file5Lbl.setText(self.__tr("file5"))
        self.lineColorCBox6.clear()
        self.lineColorCBox6.insertItem(self.__tr("black"))
        self.lineColorCBox6.insertItem(self.__tr("red"))
        self.lineColorCBox6.insertItem(self.__tr("green"))
        self.lineColorCBox6.insertItem(self.__tr("blue"))
        self.lineColorCBox6.insertItem(self.__tr("purple"))
        self.lineColorCBox6.insertItem(self.__tr("aqua"))
        self.lineColorCBox6.insertItem(self.__tr("brown"))
        self.lineColorCBox6.insertItem(self.__tr("orange"))
        self.lineColorCBox6.insertItem(self.__tr("Light Brown"))
        self.lineColorCBox3.clear()
        self.lineColorCBox3.insertItem(self.__tr("black"))
        self.lineColorCBox3.insertItem(self.__tr("red"))
        self.lineColorCBox3.insertItem(self.__tr("green"))
        self.lineColorCBox3.insertItem(self.__tr("blue"))
        self.lineColorCBox3.insertItem(self.__tr("purple"))
        self.lineColorCBox3.insertItem(self.__tr("aqua"))
        self.lineColorCBox3.insertItem(self.__tr("brown"))
        self.lineColorCBox3.insertItem(self.__tr("orange"))
        self.lineColorCBox3.insertItem(self.__tr("Light Brown"))
        self.lineColorCBox2.clear()
        self.lineColorCBox2.insertItem(self.__tr("black"))
        self.lineColorCBox2.insertItem(self.__tr("red"))
        self.lineColorCBox2.insertItem(self.__tr("green"))
        self.lineColorCBox2.insertItem(self.__tr("blue"))
        self.lineColorCBox2.insertItem(self.__tr("purple"))
        self.lineColorCBox2.insertItem(self.__tr("aqua"))
        self.lineColorCBox2.insertItem(self.__tr("brown"))
        self.lineColorCBox2.insertItem(self.__tr("orange"))
        self.lineColorCBox2.insertItem(self.__tr("Light Brown"))
        self.PointSizeLbl.setText(self.__tr("<p align=\"center\">Point \n"
"Size</p>"))
        self.lineColorCBox7.clear()
        self.lineColorCBox7.insertItem(self.__tr("black"))
        self.lineColorCBox7.insertItem(self.__tr("red"))
        self.lineColorCBox7.insertItem(self.__tr("green"))
        self.lineColorCBox7.insertItem(self.__tr("blue"))
        self.lineColorCBox7.insertItem(self.__tr("purple"))
        self.lineColorCBox7.insertItem(self.__tr("aqua"))
        self.lineColorCBox7.insertItem(self.__tr("brown"))
        self.lineColorCBox7.insertItem(self.__tr("orange"))
        self.lineColorCBox7.insertItem(self.__tr("Light Brown"))
        self.lineColorCBox5.clear()
        self.lineColorCBox5.insertItem(self.__tr("black"))
        self.lineColorCBox5.insertItem(self.__tr("red"))
        self.lineColorCBox5.insertItem(self.__tr("green"))
        self.lineColorCBox5.insertItem(self.__tr("blue"))
        self.lineColorCBox5.insertItem(self.__tr("purple"))
        self.lineColorCBox5.insertItem(self.__tr("aqua"))
        self.lineColorCBox5.insertItem(self.__tr("brown"))
        self.lineColorCBox5.insertItem(self.__tr("orange"))
        self.lineColorCBox5.insertItem(self.__tr("Light Brown"))
        self.file6Lbl.setText(self.__tr("file6"))
        self.LineWidthLbl_2.setText(self.__tr("<p align=\"center\">Line \n"
"Width</p>"))
        self.PointsLbl.setText(self.__tr("Point Type"))
        self.lineColorCBox4.clear()
        self.lineColorCBox4.insertItem(self.__tr("black"))
        self.lineColorCBox4.insertItem(self.__tr("red"))
        self.lineColorCBox4.insertItem(self.__tr("green"))
        self.lineColorCBox4.insertItem(self.__tr("blue"))
        self.lineColorCBox4.insertItem(self.__tr("purple"))
        self.lineColorCBox4.insertItem(self.__tr("aqua"))
        self.lineColorCBox4.insertItem(self.__tr("brown"))
        self.lineColorCBox4.insertItem(self.__tr("orange"))
        self.lineColorCBox4.insertItem(self.__tr("Light Brown"))
        self.plotOrder6.setText(self.__tr("6"))
        self.plotOrder7.setText(self.__tr("7"))
        self.pointsCBox3.clear()
        self.pointsCBox3.insertItem(self.__tr("No Points"))
        self.pointsCBox3.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox3.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox3.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox3.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox3.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox3.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox3.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox3.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox3.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox3.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox3.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.pointsCBox4.clear()
        self.pointsCBox4.insertItem(self.__tr("No Points"))
        self.pointsCBox4.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox4.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox4.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox4.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox4.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox4.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox4.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox4.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox4.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox4.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox4.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.pointsCBox5.clear()
        self.pointsCBox5.insertItem(self.__tr("No Points"))
        self.pointsCBox5.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox5.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox5.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox5.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox5.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox5.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox5.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox5.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox5.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox5.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox5.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.pointsCBox6.clear()
        self.pointsCBox6.insertItem(self.__tr("No Points"))
        self.pointsCBox6.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox6.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox6.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox6.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox6.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox6.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox6.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox6.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox6.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox6.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox6.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.file8Lbl.setText(self.__tr("file8"))
        self.file3Lbl.setText(self.__tr("file3"))
        self.plotOrder1.setText(self.__tr("1"))
        self.plotOrder2.setText(self.__tr("2"))
        self.plotOrder3.setText(self.__tr("3"))
        self.plotOrder4.setText(self.__tr("4"))
        self.plotOrder5.setText(self.__tr("5"))
        self.pointSizeCBox1.clear()
        self.pointSizeCBox1.insertItem(self.__tr("0"))
        self.pointSizeCBox1.insertItem(self.__tr("1"))
        self.pointSizeCBox1.insertItem(self.__tr("1.25"))
        self.pointSizeCBox1.insertItem(self.__tr("1.5"))
        self.pointSizeCBox1.insertItem(self.__tr("1.75"))
        self.pointSizeCBox1.insertItem(self.__tr("2"))
        self.pointSizeCBox1.insertItem(self.__tr("2.25"))
        self.pointSizeCBox1.insertItem(self.__tr("2.5"))
        self.pointSizeCBox1.insertItem(self.__tr("3"))
        self.pointSizeCBox2.clear()
        self.pointSizeCBox2.insertItem(self.__tr("0"))
        self.pointSizeCBox2.insertItem(self.__tr("1"))
        self.pointSizeCBox2.insertItem(self.__tr("1.25"))
        self.pointSizeCBox2.insertItem(self.__tr("1.5"))
        self.pointSizeCBox2.insertItem(self.__tr("1.75"))
        self.pointSizeCBox2.insertItem(self.__tr("2"))
        self.pointSizeCBox2.insertItem(self.__tr("2.25"))
        self.pointSizeCBox2.insertItem(self.__tr("2.5"))
        self.pointSizeCBox2.insertItem(self.__tr("3"))
        self.pointSizeCBox3.clear()
        self.pointSizeCBox3.insertItem(self.__tr("0"))
        self.pointSizeCBox3.insertItem(self.__tr("1"))
        self.pointSizeCBox3.insertItem(self.__tr("1.25"))
        self.pointSizeCBox3.insertItem(self.__tr("1.5"))
        self.pointSizeCBox3.insertItem(self.__tr("1.75"))
        self.pointSizeCBox3.insertItem(self.__tr("2"))
        self.pointSizeCBox3.insertItem(self.__tr("2.25"))
        self.pointSizeCBox3.insertItem(self.__tr("2.5"))
        self.pointSizeCBox3.insertItem(self.__tr("3"))
        self.pointSizeCBox4.clear()
        self.pointSizeCBox4.insertItem(self.__tr("0"))
        self.pointSizeCBox4.insertItem(self.__tr("1"))
        self.pointSizeCBox4.insertItem(self.__tr("1.25"))
        self.pointSizeCBox4.insertItem(self.__tr("1.5"))
        self.pointSizeCBox4.insertItem(self.__tr("1.75"))
        self.pointSizeCBox4.insertItem(self.__tr("2"))
        self.pointSizeCBox4.insertItem(self.__tr("2.25"))
        self.pointSizeCBox4.insertItem(self.__tr("2.5"))
        self.pointSizeCBox4.insertItem(self.__tr("3"))
        self.pointSizeCBox5.clear()
        self.pointSizeCBox5.insertItem(self.__tr("0"))
        self.pointSizeCBox5.insertItem(self.__tr("1"))
        self.pointSizeCBox5.insertItem(self.__tr("1.25"))
        self.pointSizeCBox5.insertItem(self.__tr("1.5"))
        self.pointSizeCBox5.insertItem(self.__tr("1.75"))
        self.pointSizeCBox5.insertItem(self.__tr("2"))
        self.pointSizeCBox5.insertItem(self.__tr("2.25"))
        self.pointSizeCBox5.insertItem(self.__tr("2.5"))
        self.pointSizeCBox5.insertItem(self.__tr("3"))
        self.pointSizeCBox6.clear()
        self.pointSizeCBox6.insertItem(self.__tr("0"))
        self.pointSizeCBox6.insertItem(self.__tr("1"))
        self.pointSizeCBox6.insertItem(self.__tr("1.25"))
        self.pointSizeCBox6.insertItem(self.__tr("1.5"))
        self.pointSizeCBox6.insertItem(self.__tr("1.75"))
        self.pointSizeCBox6.insertItem(self.__tr("2"))
        self.pointSizeCBox6.insertItem(self.__tr("2.25"))
        self.pointSizeCBox6.insertItem(self.__tr("2.5"))
        self.pointSizeCBox6.insertItem(self.__tr("3"))
        self.pointSizeCBox7.clear()
        self.pointSizeCBox7.insertItem(self.__tr("0"))
        self.pointSizeCBox7.insertItem(self.__tr("1"))
        self.pointSizeCBox7.insertItem(self.__tr("1.25"))
        self.pointSizeCBox7.insertItem(self.__tr("1.5"))
        self.pointSizeCBox7.insertItem(self.__tr("1.75"))
        self.pointSizeCBox7.insertItem(self.__tr("2"))
        self.pointSizeCBox7.insertItem(self.__tr("2.25"))
        self.pointSizeCBox7.insertItem(self.__tr("2.5"))
        self.pointSizeCBox7.insertItem(self.__tr("3"))
        self.lineWidthCBox1.clear()
        self.lineWidthCBox1.insertItem(self.__tr("1"))
        self.lineWidthCBox1.insertItem(self.__tr("2"))
        self.lineWidthCBox1.insertItem(self.__tr("3"))
        self.lineWidthCBox1.insertItem(self.__tr("4"))
        self.lineWidthCBox1.insertItem(self.__tr("5"))
        self.lineWidthCBox1.insertItem(self.__tr("6"))
        self.lineWidthCBox2.clear()
        self.lineWidthCBox2.insertItem(self.__tr("1"))
        self.lineWidthCBox2.insertItem(self.__tr("2"))
        self.lineWidthCBox2.insertItem(self.__tr("3"))
        self.lineWidthCBox2.insertItem(self.__tr("4"))
        self.lineWidthCBox2.insertItem(self.__tr("5"))
        self.lineWidthCBox2.insertItem(self.__tr("6"))
        self.lineWidthCBox3.clear()
        self.lineWidthCBox3.insertItem(self.__tr("1"))
        self.lineWidthCBox3.insertItem(self.__tr("2"))
        self.lineWidthCBox3.insertItem(self.__tr("3"))
        self.lineWidthCBox3.insertItem(self.__tr("4"))
        self.lineWidthCBox3.insertItem(self.__tr("5"))
        self.lineWidthCBox3.insertItem(self.__tr("6"))
        self.lineWidthCBox4.clear()
        self.lineWidthCBox4.insertItem(self.__tr("1"))
        self.lineWidthCBox4.insertItem(self.__tr("2"))
        self.lineWidthCBox4.insertItem(self.__tr("3"))
        self.lineWidthCBox4.insertItem(self.__tr("4"))
        self.lineWidthCBox4.insertItem(self.__tr("5"))
        self.lineWidthCBox4.insertItem(self.__tr("6"))
        self.lineWidthCBox5.clear()
        self.lineWidthCBox5.insertItem(self.__tr("1"))
        self.lineWidthCBox5.insertItem(self.__tr("2"))
        self.lineWidthCBox5.insertItem(self.__tr("3"))
        self.lineWidthCBox5.insertItem(self.__tr("4"))
        self.lineWidthCBox5.insertItem(self.__tr("5"))
        self.lineWidthCBox5.insertItem(self.__tr("6"))
        self.lineWidthCBox6.clear()
        self.lineWidthCBox6.insertItem(self.__tr("1"))
        self.lineWidthCBox6.insertItem(self.__tr("2"))
        self.lineWidthCBox6.insertItem(self.__tr("3"))
        self.lineWidthCBox6.insertItem(self.__tr("4"))
        self.lineWidthCBox6.insertItem(self.__tr("5"))
        self.lineWidthCBox6.insertItem(self.__tr("6"))
        self.lineWidthCBox7.clear()
        self.lineWidthCBox7.insertItem(self.__tr("1"))
        self.lineWidthCBox7.insertItem(self.__tr("2"))
        self.lineWidthCBox7.insertItem(self.__tr("3"))
        self.lineWidthCBox7.insertItem(self.__tr("4"))
        self.lineWidthCBox7.insertItem(self.__tr("5"))
        self.lineWidthCBox7.insertItem(self.__tr("6"))
        self.file4Lbl.setText(self.__tr("file4"))
        self.file2Lbl.setText(self.__tr("file2"))
        self.pointsCBox7.clear()
        self.pointsCBox7.insertItem(self.__tr("No Points"))
        self.pointsCBox7.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox7.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox7.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox7.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox7.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox7.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox7.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox7.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox7.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox7.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox7.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.file1Edit.setText(QString.null)
        self.plotOrder8.setText(self.__tr("8"))
        self.pointsCBox8.clear()
        self.pointsCBox8.insertItem(self.__tr("No Points"))
        self.pointsCBox8.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox8.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox8.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox8.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox8.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox8.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox8.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox8.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox8.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox8.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox8.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.pointSizeCBox8.clear()
        self.pointSizeCBox8.insertItem(self.__tr("0"))
        self.pointSizeCBox8.insertItem(self.__tr("1"))
        self.pointSizeCBox8.insertItem(self.__tr("1.25"))
        self.pointSizeCBox8.insertItem(self.__tr("1.5"))
        self.pointSizeCBox8.insertItem(self.__tr("1.75"))
        self.pointSizeCBox8.insertItem(self.__tr("2"))
        self.pointSizeCBox8.insertItem(self.__tr("2.25"))
        self.pointSizeCBox8.insertItem(self.__tr("2.5"))
        self.pointSizeCBox8.insertItem(self.__tr("3"))
        self.lineWidthCBox8.clear()
        self.lineWidthCBox8.insertItem(self.__tr("1"))
        self.lineWidthCBox8.insertItem(self.__tr("2"))
        self.lineWidthCBox8.insertItem(self.__tr("3"))
        self.lineWidthCBox8.insertItem(self.__tr("4"))
        self.lineWidthCBox8.insertItem(self.__tr("5"))
        self.lineWidthCBox8.insertItem(self.__tr("6"))
        self.lineColorCBox8.clear()
        self.lineColorCBox8.insertItem(self.__tr("black"))
        self.lineColorCBox8.insertItem(self.__tr("red"))
        self.lineColorCBox8.insertItem(self.__tr("green"))
        self.lineColorCBox8.insertItem(self.__tr("blue"))
        self.lineColorCBox8.insertItem(self.__tr("purple"))
        self.lineColorCBox8.insertItem(self.__tr("aqua"))
        self.lineColorCBox8.insertItem(self.__tr("brown"))
        self.lineColorCBox8.insertItem(self.__tr("orange"))
        self.lineColorCBox8.insertItem(self.__tr("Light Brown"))
        self.pointsCBox1.clear()
        self.pointsCBox1.insertItem(self.__tr("No Points"))
        self.pointsCBox1.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox1.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox1.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox1.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox1.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox1.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox1.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox1.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox1.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox1.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox1.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.pointsCBox2.clear()
        self.pointsCBox2.insertItem(self.__tr("No Points"))
        self.pointsCBox2.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBox2.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBox2.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBox2.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBox2.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBox2.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBox2.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBox2.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBox2.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBox2.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBox2.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.lineWidthCBoxChangeAll.clear()
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("1"))
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("2"))
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("3"))
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("4"))
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("5"))
        self.lineWidthCBoxChangeAll.insertItem(self.__tr("6"))
        self.lineColorCBoxChangeAll.clear()
        self.lineColorCBoxChangeAll.insertItem(self.__tr("black"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("red"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("green"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("blue"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("purple"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("aqua"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("brown"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("orange"))
        self.lineColorCBoxChangeAll.insertItem(self.__tr("Light Brown"))
        self.y_axisPositionLbl.setText(self.__tr("y-axis Position:"))
        self.pointSizeCBoxChangeAll.clear()
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("0"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("1"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("1.25"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("1.5"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("1.75"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("2"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("2.25"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("2.5"))
        self.pointSizeCBoxChangeAll.insertItem(self.__tr("3"))
        self.pointsCBoxChangeAll.clear()
        self.pointsCBoxChangeAll.insertItem(self.__tr("No Points"))
        self.pointsCBoxChangeAll.insertItem(self.image0,self.__tr("Plus"))
        self.pointsCBoxChangeAll.insertItem(self.image1,self.__tr("Multiply"))
        self.pointsCBoxChangeAll.insertItem(self.image2,self.__tr("Star"))
        self.pointsCBoxChangeAll.insertItem(self.image3,self.__tr("Dotted Square"))
        self.pointsCBoxChangeAll.insertItem(self.image4,self.__tr("Solid Square"))
        self.pointsCBoxChangeAll.insertItem(self.image5,self.__tr("Dotted Circle"))
        self.pointsCBoxChangeAll.insertItem(self.image6,self.__tr("Solid Circle"))
        self.pointsCBoxChangeAll.insertItem(self.image7,self.__tr("Dotted Triangle"))
        self.pointsCBoxChangeAll.insertItem(self.image8,self.__tr("Solid Trangle"))
        self.pointsCBoxChangeAll.insertItem(self.image9,self.__tr("UsD Dotted Tri."))
        self.pointsCBoxChangeAll.insertItem(self.image10,self.__tr("UsD Solid Tri."))
        self.cancelBtn.setText(self.__tr("Cancel"))
        self.legendCBox.clear()
        self.legendCBox.insertItem(self.__tr("Default Position"))
        self.legendCBox.insertItem(self.__tr("Customized Position"))
        self.legendCBox.insertItem(self.__tr("Remove Legend"))
        self.LegendPositioningLbl.setText(self.__tr("Plot Legend Position:"))
        self.x_axisPositionLbl.setText(self.__tr("x-axis Position:"))
        self.doneBtn.setText(self.__tr("Done"))
        self.saveSettingsLbl.setText(self.__tr("Settings Management"))
        self.SaveTimeButton.setText(self.__tr("Save Time"))
        self.saveSettingsBtn.setText(self.__tr("Save"))
        self.restoreSettingsBtn.setText(self.__tr("Restore"))


    def doneBtn_pressed(self):
        print "plotNameForm.doneBtn_pressed(): Not implemented yet"

    def cancelBtn_pressed(self):
        print "plotNameForm.cancelBtn_pressed(): Not implemented yet"

    def LegendPosition_selected(self):
        print "plotNameForm.LegendPosition_selected(): Not implemented yet"

    def SaveTimeButton_pressed(self):
        print "plotNameForm.SaveTimeButton_pressed(): Not implemented yet"

    def pointsCBoxChangeAll_activated(self,a0):
        print "plotNameForm.pointsCBoxChangeAll_activated(int): Not implemented yet"

    def pointSizeCBoxChangeAll_activated(self,a0):
        print "plotNameForm.pointSizeCBoxChangeAll_activated(int): Not implemented yet"

    def lineWidthCBoxChangeAll_activated(self,a0):
        print "plotNameForm.lineWidthCBoxChangeAll_activated(int): Not implemented yet"

    def lineColorCBoxChangeAll_activated(self,a0):
        print "plotNameForm.lineColorCBoxChangeAll_activated(int): Not implemented yet"

    def saveSettingsBtn_pressed(self):
        print "plotNameForm.saveSettingsBtn_pressed(): Not implemented yet"

    def restoreSettingsBtn_pressed(self):
        print "plotNameForm.restoreSettingsBtn_pressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("plotNameForm",s,c)
