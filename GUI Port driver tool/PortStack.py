################################################################################
## AVR PORT STAK TOOL
## this tool genrate (Port.c Port.h Port_confg.h Port_prv.h)
## Port_confg.h -> with your configration
## The defult configration is Output_LOW (in case the user miss to choose)
## 
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

PinCfgList=[]
for i in range(0,32):
  PinCfgList.append(2)
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(967, 847)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 941, 771))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(100, 500))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -821, 918, 3022))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(100, 3000))
        self.PIN0 = QGroupBox(self.groupBox)
        self.PIN0.setObjectName(u"PIN0")
        self.PIN0.setGeometry(QRect(20, 40, 800, 70))
        self.IP0 = QRadioButton(self.PIN0)
        self.IP0.setObjectName(u"IP0")
        self.IP0.setGeometry(QRect(80, 30, 95, 20))
        self.IH0 = QRadioButton(self.PIN0)
        self.IH0.setObjectName(u"IH0")
        self.IH0.setGeometry(QRect(260, 30, 161, 20))
        self.OL0 = QRadioButton(self.PIN0)
        self.OL0.setObjectName(u"OL0")
        self.OL0.setGeometry(QRect(500, 30, 95, 20))
        self.OH0 = QRadioButton(self.PIN0)
        self.OH0.setObjectName(u"OH0")
        self.OH0.setGeometry(QRect(700, 30, 95, 20))
        self.PIN1 = QGroupBox(self.groupBox)
        self.PIN1.setObjectName(u"PIN1")
        self.PIN1.setGeometry(QRect(20, 120, 800, 70))
        self.IP1 = QRadioButton(self.PIN1)
        self.IP1.setObjectName(u"IP1")
        self.IP1.setGeometry(QRect(80, 30, 95, 20))
        self.IH1 = QRadioButton(self.PIN1)
        self.IH1.setObjectName(u"IH1")
        self.IH1.setGeometry(QRect(260, 30, 161, 20))
        self.OL1 = QRadioButton(self.PIN1)
        self.OL1.setObjectName(u"OL1")
        self.OL1.setGeometry(QRect(500, 30, 95, 20))
        self.OH1 = QRadioButton(self.PIN1)
        self.OH1.setObjectName(u"OH1")
        self.OH1.setGeometry(QRect(700, 30, 95, 20))
        self.PIN2 = QGroupBox(self.groupBox)
        self.PIN2.setObjectName(u"PIN2")
        self.PIN2.setGeometry(QRect(20, 200, 800, 70))
        self.IP2 = QRadioButton(self.PIN2)
        self.IP2.setObjectName(u"IP2")
        self.IP2.setGeometry(QRect(80, 30, 95, 20))
        self.IH2 = QRadioButton(self.PIN2)
        self.IH2.setObjectName(u"IH2")
        self.IH2.setGeometry(QRect(260, 30, 161, 20))
        self.OL2 = QRadioButton(self.PIN2)
        self.OL2.setObjectName(u"OL2")
        self.OL2.setGeometry(QRect(500, 30, 95, 20))
        self.OH2 = QRadioButton(self.PIN2)
        self.OH2.setObjectName(u"OH2")
        self.OH2.setGeometry(QRect(700, 30, 95, 20))
        self.PIN3 = QGroupBox(self.groupBox)
        self.PIN3.setObjectName(u"PIN3")
        self.PIN3.setGeometry(QRect(20, 280, 801, 71))
        self.IP3 = QRadioButton(self.PIN3)
        self.IP3.setObjectName(u"IP3")
        self.IP3.setGeometry(QRect(80, 30, 95, 20))
        self.IH3 = QRadioButton(self.PIN3)
        self.IH3.setObjectName(u"IH3")
        self.IH3.setGeometry(QRect(260, 30, 161, 20))
        self.OL3 = QRadioButton(self.PIN3)
        self.OL3.setObjectName(u"OL3")
        self.OL3.setGeometry(QRect(500, 30, 95, 20))
        self.OH3 = QRadioButton(self.PIN3)
        self.OH3.setObjectName(u"OH3")
        self.OH3.setGeometry(QRect(700, 30, 95, 20))
        self.PIN4 = QGroupBox(self.groupBox)
        self.PIN4.setObjectName(u"PIN4")
        self.PIN4.setGeometry(QRect(20, 350, 801, 71))
        self.IP4 = QRadioButton(self.PIN4)
        self.IP4.setObjectName(u"IP4")
        self.IP4.setGeometry(QRect(80, 30, 95, 20))
        self.IH4 = QRadioButton(self.PIN4)
        self.IH4.setObjectName(u"IH4")
        self.IH4.setGeometry(QRect(260, 30, 161, 20))
        self.OL4 = QRadioButton(self.PIN4)
        self.OL4.setObjectName(u"OL4")
        self.OL4.setGeometry(QRect(500, 30, 95, 20))
        self.OH4 = QRadioButton(self.PIN4)
        self.OH4.setObjectName(u"OH4")
        self.OH4.setGeometry(QRect(700, 30, 95, 20))
        self.PIN5 = QGroupBox(self.groupBox)
        self.PIN5.setObjectName(u"PIN5")
        self.PIN5.setGeometry(QRect(20, 420, 801, 70))
        self.IP5 = QRadioButton(self.PIN5)
        self.IP5.setObjectName(u"IP5")
        self.IP5.setGeometry(QRect(80, 30, 95, 20))
        self.IH5 = QRadioButton(self.PIN5)
        self.IH5.setObjectName(u"IH5")
        self.IH5.setGeometry(QRect(260, 30, 161, 20))
        self.OL5 = QRadioButton(self.PIN5)
        self.OL5.setObjectName(u"OL5")
        self.OL5.setGeometry(QRect(500, 30, 95, 20))
        self.OH5 = QRadioButton(self.PIN5)
        self.OH5.setObjectName(u"OH5")
        self.OH5.setGeometry(QRect(700, 30, 95, 20))
        self.PIN6 = QGroupBox(self.groupBox)
        self.PIN6.setObjectName(u"PIN6")
        self.PIN6.setGeometry(QRect(20, 500, 801, 70))
        self.IP6 = QRadioButton(self.PIN6)
        self.IP6.setObjectName(u"IP6")
        self.IP6.setGeometry(QRect(80, 30, 95, 20))
        self.IH6 = QRadioButton(self.PIN6)
        self.IH6.setObjectName(u"IH6")
        self.IH6.setGeometry(QRect(260, 30, 161, 20))
        self.OL6 = QRadioButton(self.PIN6)
        self.OL6.setObjectName(u"OL6")
        self.OL6.setGeometry(QRect(500, 30, 95, 20))
        self.OH6 = QRadioButton(self.PIN6)
        self.OH6.setObjectName(u"OH6")
        self.OH6.setGeometry(QRect(700, 30, 95, 20))
        self.PIN7 = QGroupBox(self.groupBox)
        self.PIN7.setObjectName(u"PIN7")
        self.PIN7.setGeometry(QRect(20, 580, 801, 70))
        self.IP7 = QRadioButton(self.PIN7)
        self.IP7.setObjectName(u"IP7")
        self.IP7.setGeometry(QRect(80, 30, 95, 20))
        self.IH7 = QRadioButton(self.PIN7)
        self.IH7.setObjectName(u"IH7")
        self.IH7.setGeometry(QRect(260, 30, 161, 20))
        self.OL7 = QRadioButton(self.PIN7)
        self.OL7.setObjectName(u"OL7")
        self.OL7.setGeometry(QRect(500, 30, 95, 20))
        self.OH7 = QRadioButton(self.PIN7)
        self.OH7.setObjectName(u"OH7")
        self.OH7.setGeometry(QRect(700, 30, 95, 20))
        self.PIN8 = QGroupBox(self.groupBox)
        self.PIN8.setObjectName(u"PIN8")
        self.PIN8.setGeometry(QRect(20, 660, 801, 70))
        self.IP8 = QRadioButton(self.PIN8)
        self.IP8.setObjectName(u"IP8")
        self.IP8.setGeometry(QRect(80, 30, 95, 20))
        self.IH8 = QRadioButton(self.PIN8)
        self.IH8.setObjectName(u"IH8")
        self.IH8.setGeometry(QRect(260, 30, 161, 20))
        self.OL8 = QRadioButton(self.PIN8)
        self.OL8.setObjectName(u"OL8")
        self.OL8.setGeometry(QRect(500, 30, 95, 20))
        self.OH8 = QRadioButton(self.PIN8)
        self.OH8.setObjectName(u"OH8")
        self.OH8.setGeometry(QRect(700, 30, 95, 20))
        self.PIN9 = QGroupBox(self.groupBox)
        self.PIN9.setObjectName(u"PIN9")
        self.PIN9.setGeometry(QRect(20, 750, 801, 70))
        self.IP9 = QRadioButton(self.PIN9)
        self.IP9.setObjectName(u"IP9")
        self.IP9.setGeometry(QRect(80, 30, 95, 20))
        self.IH9 = QRadioButton(self.PIN9)
        self.IH9.setObjectName(u"IH9")
        self.IH9.setGeometry(QRect(260, 30, 161, 20))
        self.OL9 = QRadioButton(self.PIN9)
        self.OL9.setObjectName(u"OL9")
        self.OL9.setGeometry(QRect(500, 30, 95, 20))
        self.OH9 = QRadioButton(self.PIN9)
        self.OH9.setObjectName(u"OH9")
        self.OH9.setGeometry(QRect(700, 30, 95, 20))
        self.PIN10 = QGroupBox(self.groupBox)
        self.PIN10.setObjectName(u"PIN10")
        self.PIN10.setGeometry(QRect(20, 840, 801, 70))
        self.IP10 = QRadioButton(self.PIN10)
        self.IP10.setObjectName(u"IP10")
        self.IP10.setGeometry(QRect(80, 30, 95, 20))
        self.IH10 = QRadioButton(self.PIN10)
        self.IH10.setObjectName(u"IH10")
        self.IH10.setGeometry(QRect(260, 30, 161, 20))
        self.OL10 = QRadioButton(self.PIN10)
        self.OL10.setObjectName(u"OL10")
        self.OL10.setGeometry(QRect(500, 30, 95, 20))
        self.OH10 = QRadioButton(self.PIN10)
        self.OH10.setObjectName(u"OH10")
        self.OH10.setGeometry(QRect(700, 30, 95, 20))
        self.PIN11 = QGroupBox(self.groupBox)
        self.PIN11.setObjectName(u"PIN11")
        self.PIN11.setGeometry(QRect(20, 930, 801, 70))
        self.IP11 = QRadioButton(self.PIN11)
        self.IP11.setObjectName(u"IP11")
        self.IP11.setGeometry(QRect(80, 30, 95, 20))
        self.IH11 = QRadioButton(self.PIN11)
        self.IH11.setObjectName(u"IH11")
        self.IH11.setGeometry(QRect(260, 30, 161, 20))
        self.OL11 = QRadioButton(self.PIN11)
        self.OL11.setObjectName(u"OL11")
        self.OL11.setGeometry(QRect(500, 30, 95, 20))
        self.OH11 = QRadioButton(self.PIN11)
        self.OH11.setObjectName(u"OH11")
        self.OH11.setGeometry(QRect(700, 30, 95, 20))
        self.PIN12 = QGroupBox(self.groupBox)
        self.PIN12.setObjectName(u"PIN12")
        self.PIN12.setGeometry(QRect(20, 1020, 801, 70))
        self.IP12 = QRadioButton(self.PIN12)
        self.IP12.setObjectName(u"IP12")
        self.IP12.setGeometry(QRect(80, 30, 95, 20))
        self.IH12 = QRadioButton(self.PIN12)
        self.IH12.setObjectName(u"IH12")
        self.IH12.setGeometry(QRect(260, 30, 161, 20))
        self.OL12 = QRadioButton(self.PIN12)
        self.OL12.setObjectName(u"OL12")
        self.OL12.setGeometry(QRect(500, 30, 95, 20))
        self.OH12 = QRadioButton(self.PIN12)
        self.OH12.setObjectName(u"OH12")
        self.OH12.setGeometry(QRect(700, 30, 95, 20))
        self.PIN14 = QGroupBox(self.groupBox)
        self.PIN14.setObjectName(u"PIN14")
        self.PIN14.setGeometry(QRect(20, 1170, 801, 70))
        self.IP14 = QRadioButton(self.PIN14)
        self.IP14.setObjectName(u"IP14")
        self.IP14.setGeometry(QRect(80, 30, 95, 20))
        self.IH14 = QRadioButton(self.PIN14)
        self.IH14.setObjectName(u"IH14")
        self.IH14.setGeometry(QRect(260, 30, 161, 20))
        self.OL14 = QRadioButton(self.PIN14)
        self.OL14.setObjectName(u"OL14")
        self.OL14.setGeometry(QRect(500, 30, 95, 20))
        self.OH14 = QRadioButton(self.PIN14)
        self.OH14.setObjectName(u"OH14")
        self.OH14.setGeometry(QRect(700, 30, 95, 20))
        self.PIN15 = QGroupBox(self.groupBox)
        self.PIN15.setObjectName(u"PIN15")
        self.PIN15.setGeometry(QRect(20, 1250, 801, 70))
        self.IP15 = QRadioButton(self.PIN15)
        self.IP15.setObjectName(u"IP15")
        self.IP15.setGeometry(QRect(80, 30, 95, 20))
        self.IH15 = QRadioButton(self.PIN15)
        self.IH15.setObjectName(u"IH15")
        self.IH15.setGeometry(QRect(260, 30, 161, 20))
        self.OL15 = QRadioButton(self.PIN15)
        self.OL15.setObjectName(u"OL15")
        self.OL15.setGeometry(QRect(500, 30, 95, 20))
        self.OH15 = QRadioButton(self.PIN15)
        self.OH15.setObjectName(u"OH15")
        self.OH15.setGeometry(QRect(700, 30, 95, 20))
        self.PIN16 = QGroupBox(self.groupBox)
        self.PIN16.setObjectName(u"PIN16")
        self.PIN16.setGeometry(QRect(20, 1340, 801, 70))
        self.IP16 = QRadioButton(self.PIN16)
        self.IP16.setObjectName(u"IP16")
        self.IP16.setGeometry(QRect(80, 30, 95, 20))
        self.IH16 = QRadioButton(self.PIN16)
        self.IH16.setObjectName(u"IH16")
        self.IH16.setGeometry(QRect(260, 30, 161, 20))
        self.OL16 = QRadioButton(self.PIN16)
        self.OL16.setObjectName(u"OL16")
        self.OL16.setGeometry(QRect(500, 30, 95, 20))
        self.OH16 = QRadioButton(self.PIN16)
        self.OH16.setObjectName(u"OH16")
        self.OH16.setGeometry(QRect(700, 30, 95, 20))
        self.PIN17 = QGroupBox(self.groupBox)
        self.PIN17.setObjectName(u"PIN17")
        self.PIN17.setGeometry(QRect(20, 1430, 801, 70))
        self.IP17 = QRadioButton(self.PIN17)
        self.IP17.setObjectName(u"IP17")
        self.IP17.setGeometry(QRect(80, 30, 95, 20))
        self.IH17 = QRadioButton(self.PIN17)
        self.IH17.setObjectName(u"IH17")
        self.IH17.setGeometry(QRect(260, 30, 161, 20))
        self.OL17 = QRadioButton(self.PIN17)
        self.OL17.setObjectName(u"OL17")
        self.OL17.setGeometry(QRect(500, 30, 95, 20))
        self.OH17 = QRadioButton(self.PIN17)
        self.OH17.setObjectName(u"OH17")
        self.OH17.setGeometry(QRect(700, 30, 95, 20))
        self.PIN18 = QGroupBox(self.groupBox)
        self.PIN18.setObjectName(u"PIN18")
        self.PIN18.setGeometry(QRect(20, 1510, 801, 70))
        self.IP18 = QRadioButton(self.PIN18)
        self.IP18.setObjectName(u"IP18")
        self.IP18.setGeometry(QRect(80, 30, 95, 20))
        self.IH18 = QRadioButton(self.PIN18)
        self.IH18.setObjectName(u"IH18")
        self.IH18.setGeometry(QRect(260, 30, 161, 20))
        self.OL18 = QRadioButton(self.PIN18)
        self.OL18.setObjectName(u"OL18")
        self.OL18.setGeometry(QRect(500, 30, 95, 20))
        self.OH18 = QRadioButton(self.PIN18)
        self.OH18.setObjectName(u"OH18")
        self.OH18.setGeometry(QRect(700, 30, 95, 20))
        self.PIN19 = QGroupBox(self.groupBox)
        self.PIN19.setObjectName(u"PIN19")
        self.PIN19.setGeometry(QRect(10, 1610, 801, 70))
        self.IP19 = QRadioButton(self.PIN19)
        self.IP19.setObjectName(u"IP19")
        self.IP19.setGeometry(QRect(80, 30, 95, 20))
        self.IH19 = QRadioButton(self.PIN19)
        self.IH19.setObjectName(u"IH19")
        self.IH19.setGeometry(QRect(260, 30, 161, 20))
        self.OL19 = QRadioButton(self.PIN19)
        self.OL19.setObjectName(u"OL19")
        self.OL19.setGeometry(QRect(500, 30, 95, 20))
        self.OH19 = QRadioButton(self.PIN19)
        self.OH19.setObjectName(u"OH19")
        self.OH19.setGeometry(QRect(700, 30, 95, 20))
        self.PIN20 = QGroupBox(self.groupBox)
        self.PIN20.setObjectName(u"PIN20")
        self.PIN20.setGeometry(QRect(10, 1700, 801, 70))
        self.IP20 = QRadioButton(self.PIN20)
        self.IP20.setObjectName(u"IP20")
        self.IP20.setGeometry(QRect(80, 30, 95, 20))
        self.IH20 = QRadioButton(self.PIN20)
        self.IH20.setObjectName(u"IH20")
        self.IH20.setGeometry(QRect(260, 30, 161, 20))
        self.OL20 = QRadioButton(self.PIN20)
        self.OL20.setObjectName(u"OL20")
        self.OL20.setGeometry(QRect(500, 30, 95, 20))
        self.OH20 = QRadioButton(self.PIN20)
        self.OH20.setObjectName(u"OH20")
        self.OH20.setGeometry(QRect(700, 30, 95, 20))
        self.PIN21 = QGroupBox(self.groupBox)
        self.PIN21.setObjectName(u"PIN21")
        self.PIN21.setGeometry(QRect(10, 1790, 801, 70))
        self.IP21 = QRadioButton(self.PIN21)
        self.IP21.setObjectName(u"IP21")
        self.IP21.setGeometry(QRect(80, 30, 95, 20))
        self.IH21 = QRadioButton(self.PIN21)
        self.IH21.setObjectName(u"IH21")
        self.IH21.setGeometry(QRect(260, 30, 161, 20))
        self.OL21 = QRadioButton(self.PIN21)
        self.OL21.setObjectName(u"OL21")
        self.OL21.setGeometry(QRect(500, 30, 95, 20))
        self.OH21 = QRadioButton(self.PIN21)
        self.OH21.setObjectName(u"OH21")
        self.OH21.setGeometry(QRect(700, 30, 95, 20))
        self.PIN22 = QGroupBox(self.groupBox)
        self.PIN22.setObjectName(u"PIN22")
        self.PIN22.setGeometry(QRect(10, 1870, 801, 70))
        self.IP22 = QRadioButton(self.PIN22)
        self.IP22.setObjectName(u"IP22")
        self.IP22.setGeometry(QRect(80, 30, 95, 20))
        self.IH22 = QRadioButton(self.PIN22)
        self.IH22.setObjectName(u"IH22")
        self.IH22.setGeometry(QRect(260, 30, 161, 20))
        self.OL22 = QRadioButton(self.PIN22)
        self.OL22.setObjectName(u"OL22")
        self.OL22.setGeometry(QRect(500, 30, 95, 20))
        self.OH22 = QRadioButton(self.PIN22)
        self.OH22.setObjectName(u"OH22")
        self.OH22.setGeometry(QRect(700, 30, 95, 20))
        self.PIN23 = QGroupBox(self.groupBox)
        self.PIN23.setObjectName(u"PIN23")
        self.PIN23.setGeometry(QRect(10, 1960, 801, 70))
        self.IP23 = QRadioButton(self.PIN23)
        self.IP23.setObjectName(u"IP23")
        self.IP23.setGeometry(QRect(80, 30, 95, 20))
        self.IH23 = QRadioButton(self.PIN23)
        self.IH23.setObjectName(u"IH23")
        self.IH23.setGeometry(QRect(260, 30, 161, 20))
        self.OL23 = QRadioButton(self.PIN23)
        self.OL23.setObjectName(u"OL23")
        self.OL23.setGeometry(QRect(500, 30, 95, 20))
        self.OH23 = QRadioButton(self.PIN23)
        self.OH23.setObjectName(u"OH23")
        self.OH23.setGeometry(QRect(700, 30, 95, 20))
        self.PIN24 = QGroupBox(self.groupBox)
        self.PIN24.setObjectName(u"PIN24")
        self.PIN24.setGeometry(QRect(10, 2050, 801, 70))
        self.IP24 = QRadioButton(self.PIN24)
        self.IP24.setObjectName(u"IP24")
        self.IP24.setGeometry(QRect(80, 30, 95, 20))
        self.IH24 = QRadioButton(self.PIN24)
        self.IH24.setObjectName(u"IH24")
        self.IH24.setGeometry(QRect(260, 30, 161, 20))
        self.OL24 = QRadioButton(self.PIN24)
        self.OL24.setObjectName(u"OL24")
        self.OL24.setGeometry(QRect(500, 30, 95, 20))
        self.OH24 = QRadioButton(self.PIN24)
        self.OH24.setObjectName(u"OH24")
        self.OH24.setGeometry(QRect(700, 30, 95, 20))
        self.PIN25 = QGroupBox(self.groupBox)
        self.PIN25.setObjectName(u"PIN25")
        self.PIN25.setGeometry(QRect(10, 2140, 801, 70))
        self.IP25 = QRadioButton(self.PIN25)
        self.IP25.setObjectName(u"IP25")
        self.IP25.setGeometry(QRect(80, 30, 95, 20))
        self.IH25 = QRadioButton(self.PIN25)
        self.IH25.setObjectName(u"IH25")
        self.IH25.setGeometry(QRect(260, 30, 161, 20))
        self.OL25 = QRadioButton(self.PIN25)
        self.OL25.setObjectName(u"OL25")
        self.OL25.setGeometry(QRect(500, 30, 95, 20))
        self.OH25 = QRadioButton(self.PIN25)
        self.OH25.setObjectName(u"OH25")
        self.OH25.setGeometry(QRect(700, 30, 95, 20))
        self.PIN26 = QGroupBox(self.groupBox)
        self.PIN26.setObjectName(u"PIN26")
        self.PIN26.setGeometry(QRect(10, 2230, 801, 70))
        self.IP26 = QRadioButton(self.PIN26)
        self.IP26.setObjectName(u"IP26")
        self.IP26.setGeometry(QRect(80, 30, 95, 20))
        self.IH26 = QRadioButton(self.PIN26)
        self.IH26.setObjectName(u"IH26")
        self.IH26.setGeometry(QRect(260, 30, 161, 20))
        self.OL26 = QRadioButton(self.PIN26)
        self.OL26.setObjectName(u"OL26")
        self.OL26.setGeometry(QRect(500, 30, 95, 20))
        self.OH26 = QRadioButton(self.PIN26)
        self.OH26.setObjectName(u"OH26")
        self.OH26.setGeometry(QRect(700, 30, 95, 20))
        self.PIN27 = QGroupBox(self.groupBox)
        self.PIN27.setObjectName(u"PIN27")
        self.PIN27.setGeometry(QRect(10, 2320, 801, 70))
        self.IP27 = QRadioButton(self.PIN27)
        self.IP27.setObjectName(u"IP27")
        self.IP27.setGeometry(QRect(80, 30, 95, 20))
        self.IH27 = QRadioButton(self.PIN27)
        self.IH27.setObjectName(u"IH27")
        self.IH27.setGeometry(QRect(260, 30, 161, 20))
        self.OL27 = QRadioButton(self.PIN27)
        self.OL27.setObjectName(u"OL27")
        self.OL27.setGeometry(QRect(500, 30, 95, 20))
        self.OH27 = QRadioButton(self.PIN27)
        self.OH27.setObjectName(u"OH27")
        self.OH27.setGeometry(QRect(700, 30, 95, 20))
        self.PIN28 = QGroupBox(self.groupBox)
        self.PIN28.setObjectName(u"PIN28")
        self.PIN28.setGeometry(QRect(10, 2400, 801, 70))
        self.IP28 = QRadioButton(self.PIN28)
        self.IP28.setObjectName(u"IP28")
        self.IP28.setGeometry(QRect(80, 30, 95, 20))
        self.IH28 = QRadioButton(self.PIN28)
        self.IH28.setObjectName(u"IH28")
        self.IH28.setGeometry(QRect(260, 30, 161, 20))
        self.OL28 = QRadioButton(self.PIN28)
        self.OL28.setObjectName(u"OL28")
        self.OL28.setGeometry(QRect(500, 30, 95, 20))
        self.OH28 = QRadioButton(self.PIN28)
        self.OH28.setObjectName(u"OH28")
        self.OH28.setGeometry(QRect(700, 30, 95, 20))
        self.PIN29 = QGroupBox(self.groupBox)
        self.PIN29.setObjectName(u"PIN29")
        self.PIN29.setGeometry(QRect(10, 2480, 801, 70))
        self.IP29 = QRadioButton(self.PIN29)
        self.IP29.setObjectName(u"IP29")
        self.IP29.setGeometry(QRect(80, 30, 95, 20))
        self.IH29 = QRadioButton(self.PIN29)
        self.IH29.setObjectName(u"IH29")
        self.IH29.setGeometry(QRect(260, 30, 161, 20))
        self.OL29 = QRadioButton(self.PIN29)
        self.OL29.setObjectName(u"OL29")
        self.OL29.setGeometry(QRect(500, 30, 95, 20))
        self.OH29 = QRadioButton(self.PIN29)
        self.OH29.setObjectName(u"OH29")
        self.OH29.setGeometry(QRect(700, 30, 95, 20))
        self.PIN30 = QGroupBox(self.groupBox)
        self.PIN30.setObjectName(u"PIN30")
        self.PIN30.setGeometry(QRect(10, 2570, 801, 70))
        self.IP30 = QRadioButton(self.PIN30)
        self.IP30.setObjectName(u"IP30")
        self.IP30.setGeometry(QRect(80, 30, 95, 20))
        self.IH30 = QRadioButton(self.PIN30)
        self.IH30.setObjectName(u"IH30")
        self.IH30.setGeometry(QRect(260, 30, 161, 20))
        self.OL30 = QRadioButton(self.PIN30)
        self.OL30.setObjectName(u"OL30")
        self.OL30.setGeometry(QRect(500, 30, 95, 20))
        self.OH30 = QRadioButton(self.PIN30)
        self.OH30.setObjectName(u"OH30")
        self.OH30.setGeometry(QRect(700, 30, 95, 20))
        self.PIN31 = QGroupBox(self.groupBox)
        self.PIN31.setObjectName(u"PIN31")
        self.PIN31.setGeometry(QRect(10, 2670, 801, 70))
        self.IP31 = QRadioButton(self.PIN31)
        self.IP31.setObjectName(u"IP31")
        self.IP31.setGeometry(QRect(80, 30, 95, 20))
        self.IH31 = QRadioButton(self.PIN31)
        self.IH31.setObjectName(u"IH31")
        self.IH31.setGeometry(QRect(260, 30, 161, 20))
        self.OL31 = QRadioButton(self.PIN31)
        self.OL31.setObjectName(u"OL31")
        self.OL31.setGeometry(QRect(500, 30, 95, 20))
        self.OH31 = QRadioButton(self.PIN31)
        self.OH31.setObjectName(u"OH31")
        self.OH31.setGeometry(QRect(700, 30, 95, 20))
        self.PIN13 = QGroupBox(self.groupBox)
        self.PIN13.setObjectName(u"PIN13")
        self.PIN13.setGeometry(QRect(20, 1090, 801, 70))
        self.IP13 = QRadioButton(self.PIN13)
        self.IP13.setObjectName(u"IP13")
        self.IP13.setGeometry(QRect(80, 30, 95, 20))
        self.IH13 = QRadioButton(self.PIN13)
        self.IH13.setObjectName(u"IH13")
        self.IH13.setGeometry(QRect(260, 30, 161, 20))
        self.OL13 = QRadioButton(self.PIN13)
        self.OL13.setObjectName(u"OL13")
        self.OL13.setGeometry(QRect(500, 30, 95, 20))
        self.OH13 = QRadioButton(self.PIN13)
        self.OH13.setObjectName(u"OH13")
        self.OH13.setGeometry(QRect(700, 30, 95, 20))

        self.verticalLayout.addWidget(self.groupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Gen = QPushButton(Form)
        self.Gen.setObjectName(u"Gen")
        self.Gen.setGeometry(QRect(810, 790, 141, 41))
        self.save = QPushButton(Form)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(650, 790, 131, 41))
        self.load = QPushButton(Form)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(490, 790, 121, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.Gen.clicked.connect(self.GenerateBtnClked)
        QObject.connect(self.IP0,SIGNAL("clicked(bool)"), self.Input_FloatingClcked0)
        QObject.connect(self.IH0,SIGNAL("clicked(bool)"), self.InputPulLUpClcked0)
        QObject.connect(self.OL0,SIGNAL("clicked(bool)"), self.OutputLowClcked0)
        QObject.connect(self.OH0,SIGNAL("clicked(bool)"), self.OutputHighClcked0)
        
        QObject.connect(self.IP1,SIGNAL("clicked(bool)"), self.Input_FloatingClcked1)
        QObject.connect(self.IH1,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked1)
        QObject.connect(self.OL1,SIGNAL("clicked(bool)"),      self.OutputLowClcked1)
        QObject.connect(self.OH1,SIGNAL("clicked(bool)"),     self.OutputHighClcked1)
        
        QObject.connect(self.IP2,SIGNAL("clicked(bool)"), self.Input_FloatingClcked2)
        QObject.connect(self.IH2,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked2)
        QObject.connect(self.OL2,SIGNAL("clicked(bool)"),      self.OutputLowClcked2)
        QObject.connect(self.OH2,SIGNAL("clicked(bool)"),     self.OutputHighClcked2)  
        
        QObject.connect(self.IP3,SIGNAL("clicked(bool)"), self.Input_FloatingClcked3)
        QObject.connect(self.IH3,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked3)
        QObject.connect(self.OL3,SIGNAL("clicked(bool)"),      self.OutputLowClcked3)
        QObject.connect(self.OH3,SIGNAL("clicked(bool)"),     self.OutputHighClcked3) 

        QObject.connect(self.IP4,SIGNAL("clicked(bool)"), self.Input_FloatingClcked4)
        QObject.connect(self.IH4,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked4)
        QObject.connect(self.OL4,SIGNAL("clicked(bool)"),      self.OutputLowClcked4)
        QObject.connect(self.OH4,SIGNAL("clicked(bool)"),     self.OutputHighClcked4)

        QObject.connect(self.IP5,SIGNAL("clicked(bool)"), self.Input_FloatingClcked5)
        QObject.connect(self.IH5,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked5)
        QObject.connect(self.OL5,SIGNAL("clicked(bool)"),      self.OutputLowClcked5)
        QObject.connect(self.OH5,SIGNAL("clicked(bool)"),     self.OutputHighClcked5)

        QObject.connect(self.IP6,SIGNAL("clicked(bool)"), self.Input_FloatingClcked6)
        QObject.connect(self.IH6,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked6)
        QObject.connect(self.OL6,SIGNAL("clicked(bool)"),      self.OutputLowClcked6)
        QObject.connect(self.OH6,SIGNAL("clicked(bool)"),     self.OutputHighClcked6)

        QObject.connect(self.IP7,SIGNAL("clicked(bool)"), self.Input_FloatingClcked7)
        QObject.connect(self.IH7,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked7)
        QObject.connect(self.OL7,SIGNAL("clicked(bool)"),      self.OutputLowClcked7)
        QObject.connect(self.OH7,SIGNAL("clicked(bool)"),     self.OutputHighClcked7)

        QObject.connect(self.IP8,SIGNAL("clicked(bool)"), self.Input_FloatingClcked8)
        QObject.connect(self.IH8,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked8)
        QObject.connect(self.OL8,SIGNAL("clicked(bool)"),      self.OutputLowClcked8)
        QObject.connect(self.OH8,SIGNAL("clicked(bool)"),     self.OutputHighClcked8)

        QObject.connect(self.IP9,SIGNAL("clicked(bool)"), self.Input_FloatingClcked9)
        QObject.connect(self.IH9,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked9)
        QObject.connect(self.OL9,SIGNAL("clicked(bool)"),      self.OutputLowClcked9)
        QObject.connect(self.OH9,SIGNAL("clicked(bool)"),     self.OutputHighClcked9)

        QObject.connect(self.IP10,SIGNAL("clicked(bool)"), self.Input_FloatingClcked10)
        QObject.connect(self.IH10,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked10)
        QObject.connect(self.OL10,SIGNAL("clicked(bool)"),      self.OutputLowClcked10)
        QObject.connect(self.OH10,SIGNAL("clicked(bool)"),     self.OutputHighClcked10)

        QObject.connect(self.IP11,SIGNAL("clicked(bool)"), self.Input_FloatingClcked11)
        QObject.connect(self.IH11,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked11)
        QObject.connect(self.OL11,SIGNAL("clicked(bool)"),      self.OutputLowClcked11)
        QObject.connect(self.OH11,SIGNAL("clicked(bool)"),     self.OutputHighClcked11)

        QObject.connect(self.IP12,SIGNAL("clicked(bool)"), self.Input_FloatingClcked12)
        QObject.connect(self.IH12,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked12)
        QObject.connect(self.OL12,SIGNAL("clicked(bool)"),      self.OutputLowClcked12)
        QObject.connect(self.OH12,SIGNAL("clicked(bool)"),     self.OutputHighClcked12)

        QObject.connect(self.IP13,SIGNAL("clicked(bool)"), self.Input_FloatingClcked13)
        QObject.connect(self.IH13,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked13)
        QObject.connect(self.OL13,SIGNAL("clicked(bool)"),      self.OutputLowClcked13)
        QObject.connect(self.OH13,SIGNAL("clicked(bool)"),     self.OutputHighClcked13)

        QObject.connect(self.IP14,SIGNAL("clicked(bool)"), self.Input_FloatingClcked14)
        QObject.connect(self.IH14,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked14)
        QObject.connect(self.OL14,SIGNAL("clicked(bool)"),      self.OutputLowClcked14)
        QObject.connect(self.OH14,SIGNAL("clicked(bool)"),     self.OutputHighClcked14)

        QObject.connect(self.IP15,SIGNAL("clicked(bool)"), self.Input_FloatingClcked15)
        QObject.connect(self.IH15,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked15)
        QObject.connect(self.OL15,SIGNAL("clicked(bool)"),      self.OutputLowClcked15)
        QObject.connect(self.OH15,SIGNAL("clicked(bool)"),     self.OutputHighClcked15)

        QObject.connect(self.IP16,SIGNAL("clicked(bool)"), self.Input_FloatingClcked16)
        QObject.connect(self.IH16,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked16)
        QObject.connect(self.OL16,SIGNAL("clicked(bool)"),      self.OutputLowClcked16)
        QObject.connect(self.OH16,SIGNAL("clicked(bool)"),     self.OutputHighClcked16)

        QObject.connect(self.IP17,SIGNAL("clicked(bool)"), self.Input_FloatingClcked17)
        QObject.connect(self.IH17,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked17)
        QObject.connect(self.OL17,SIGNAL("clicked(bool)"),      self.OutputLowClcked17)
        QObject.connect(self.OH17,SIGNAL("clicked(bool)"),     self.OutputHighClcked17)

        QObject.connect(self.IP18,SIGNAL("clicked(bool)"), self.Input_FloatingClcked18)
        QObject.connect(self.IH18,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked18)
        QObject.connect(self.OL18,SIGNAL("clicked(bool)"),      self.OutputLowClcked18)
        QObject.connect(self.OH18,SIGNAL("clicked(bool)"),     self.OutputHighClcked18)

        QObject.connect(self.IP19,SIGNAL("clicked(bool)"), self.Input_FloatingClcked19)
        QObject.connect(self.IH19,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked19)
        QObject.connect(self.OL19,SIGNAL("clicked(bool)"),      self.OutputLowClcked19)
        QObject.connect(self.OH19,SIGNAL("clicked(bool)"),     self.OutputHighClcked19)
        
        QObject.connect(self.IP20,SIGNAL("clicked(bool)"), self.Input_FloatingClcked20)
        QObject.connect(self.IH20,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked20)
        QObject.connect(self.OL20,SIGNAL("clicked(bool)"),      self.OutputLowClcked20)
        QObject.connect(self.OH20,SIGNAL("clicked(bool)"),     self.OutputHighClcked20)

        QObject.connect(self.IP21,SIGNAL("clicked(bool)"), self.Input_FloatingClcked21)
        QObject.connect(self.IH21,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked21)
        QObject.connect(self.OL21,SIGNAL("clicked(bool)"),      self.OutputLowClcked21)
        QObject.connect(self.OH21,SIGNAL("clicked(bool)"),     self.OutputHighClcked21)  
                
        QObject.connect(self.IP22,SIGNAL("clicked(bool)"), self.Input_FloatingClcked22)
        QObject.connect(self.IH22,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked22)
        QObject.connect(self.OL22,SIGNAL("clicked(bool)"),      self.OutputLowClcked22)
        QObject.connect(self.OH22,SIGNAL("clicked(bool)"),     self.OutputHighClcked22)  

        QObject.connect(self.IP23,SIGNAL("clicked(bool)"), self.Input_FloatingClcked23)
        QObject.connect(self.IH23,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked23)
        QObject.connect(self.OL23,SIGNAL("clicked(bool)"),      self.OutputLowClcked23)
        QObject.connect(self.OH23,SIGNAL("clicked(bool)"),     self.OutputHighClcked23)  

        QObject.connect(self.IP24,SIGNAL("clicked(bool)"), self.Input_FloatingClcked24)
        QObject.connect(self.IH24,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked24)
        QObject.connect(self.OL24,SIGNAL("clicked(bool)"),      self.OutputLowClcked24)
        QObject.connect(self.OH24,SIGNAL("clicked(bool)"),     self.OutputHighClcked24)  

        QObject.connect(self.IP25,SIGNAL("clicked(bool)"), self.Input_FloatingClcked25)
        QObject.connect(self.IH25,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked25)
        QObject.connect(self.OL25,SIGNAL("clicked(bool)"),      self.OutputLowClcked25)
        QObject.connect(self.OH25,SIGNAL("clicked(bool)"),     self.OutputHighClcked25)  

        QObject.connect(self.IP26,SIGNAL("clicked(bool)"), self.Input_FloatingClcked26)
        QObject.connect(self.IH26,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked26)
        QObject.connect(self.OL26,SIGNAL("clicked(bool)"),      self.OutputLowClcked26)
        QObject.connect(self.OH26,SIGNAL("clicked(bool)"),     self.OutputHighClcked26)  

        QObject.connect(self.IP27,SIGNAL("clicked(bool)"), self.Input_FloatingClcked27)
        QObject.connect(self.IH27,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked27)
        QObject.connect(self.OL27,SIGNAL("clicked(bool)"),      self.OutputLowClcked27)
        QObject.connect(self.OH27,SIGNAL("clicked(bool)"),     self.OutputHighClcked27)  

        QObject.connect(self.IP28,SIGNAL("clicked(bool)"), self.Input_FloatingClcked28)
        QObject.connect(self.IH28,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked28)
        QObject.connect(self.OL28,SIGNAL("clicked(bool)"),      self.OutputLowClcked28)
        QObject.connect(self.OH28,SIGNAL("clicked(bool)"),     self.OutputHighClcked28)  
 
        QObject.connect(self.IP29,SIGNAL("clicked(bool)"), self.Input_FloatingClcked29)
        QObject.connect(self.IH29,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked29)
        QObject.connect(self.OL29,SIGNAL("clicked(bool)"),      self.OutputLowClcked29)
        QObject.connect(self.OH29,SIGNAL("clicked(bool)"),     self.OutputHighClcked29)  

        QObject.connect(self.IP30,SIGNAL("clicked(bool)"), self.Input_FloatingClcked30)
        QObject.connect(self.IH30,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked30)
        QObject.connect(self.OL30,SIGNAL("clicked(bool)"),      self.OutputLowClcked30)
        QObject.connect(self.OH30,SIGNAL("clicked(bool)"),     self.OutputHighClcked30)  

        QObject.connect(self.IP31,SIGNAL("clicked(bool)"), self.Input_FloatingClcked31)
        QObject.connect(self.IH31,SIGNAL("clicked(bool)"),    self.InputPulLUpClcked31)
        QObject.connect(self.OL31,SIGNAL("clicked(bool)"),      self.OutputLowClcked31)
        QObject.connect(self.OH31,SIGNAL("clicked(bool)"),     self.OutputHighClcked31)         
    # setupUi
    def GenerateBtnClked(self):
        with open('Port_confg.h','w') as f:
          f.write('#ifndef PORT_CFG_H_\n')
          f.write('#define PORT_CFG_H_\n\n\n\n\n')
          for i in range(0,32):
            if PinCfgList[i] == 0:
              f.write('#define PORT_U8_MODE_PIN'+str(i)+'             ' + 'PORT_U8_MODE_INPUT_PULLUP\n')
            elif PinCfgList[i] == 1:            
              f.write('#define PORT_U8_MODE_PIN'+str(i)+'             ' + 'PORT_U8_MODE_INPUT_HIGHIMP\n')
            elif PinCfgList[i] == 2:            
              f.write('#define PORT_U8_MODE_PIN'+str(i)+'             ' + 'PORT_U8_MODE_OUTPUT_LOW\n')
            elif PinCfgList[i] == 3:            
              f.write('#define PORT_U8_MODE_PIN'+str(i)+'             ' + 'PORT_U8_MODE_OUTPUT_HIGH\n')
          f.write('\n\n\n\n#endif')
        with open('Port_prv.h','w') as f:
          f.write('#ifndef PORT_PRV_H_\n\
#define PORT_PRV_H_\n\
\n\
#define PORT_U8_PORTA                           0\n\
#define PORT_U8_PORTB                           1\n\
#define PORT_U8_PORTC                           2\n\
#define PORT_U8_PORTD                           3\n\
\n\
\n\
#define PORT_U8_DIR_OUTPUT                      1\n\
#define PORT_U8_DIR_INPUT                       0\n\
\n\
#define PORT_U8_MODE_OUTPUT_LOW         0\n\
#define PORT_U8_MODE_OUTPUT_HIGH        1\n\
\n\
#define PORT_U8_MODE_INPUT_HIGHIMP      2\n\
#define PORT_U8_MODE_INPUT_PULLUP       3\n\
\n\
\n\
\n\
\n\
\n\
\n\
/*for direction*/\n\
\n\
#if   PORT_U8_MODE_PIN0 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN0 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN0_DIR    1\n\
#else\n\
#define PORTA_U8_PIN0_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN1 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN1 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN1_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN1_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN2 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN2 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN2_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN2_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN3 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN3 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN3_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN3_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN4 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN4 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN4_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN4_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN5 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN5 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN5_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN5_DIR    0\n\
#endif\n\
\n\
#if   PORT_U8_MODE_PIN6 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN6 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN6_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN6_DIR    0\n\
#endif\n\
#if   PORT_U8_MODE_PIN7 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN7 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN7_DIR    1\n\
#else               \n\
#define PORTA_U8_PIN7_DIR    0\n\
#endif\n\
\n\
#if   PORT_U8_MODE_PIN8 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN8 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN0_DIR    1\n\
#else       \n\
#define PORTB_U8_PIN0_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN9 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN9 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN1_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN1_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN10 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN10 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN2_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN2_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN11 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN11 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN3_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN3_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN12 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN12 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN4_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN4_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN13 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN13 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN5_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN5_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN14 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN14 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN6_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN6_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN15 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN15 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN7_DIR    1\n\
#else              \n\
#define PORTB_U8_PIN7_DIR    0\n\
#endif\n\
\n\
#if   PORT_U8_MODE_PIN16 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN16== PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN0_DIR    1\n\
#else       \n\
#define PORTC_U8_PIN0_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN17 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN17 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN1_DIR    1\n\
#else             \n\
#define PORTC_U8_PIN1_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN18 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN18 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN2_DIR    1\n\
#else              \n\
#define PORTC_U8_PIN2_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN19 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN19 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN3_DIR    1\n\
#else              \n\
#define PORTC_U8_PIN3_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN20 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN20 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN4_DIR    1\n\
#else              \n\
#define PORTC_U8_PIN4_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN21 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN21 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN5_DIR    1\n\
#else             \n\
#define PORTC_U8_PIN5_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN22 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN22 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN6_DIR    1\n\
#else              \n\
#define PORTC_U8_PIN6_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN23 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN23 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN7_DIR    1\n\
#else              \n\
#define PORTC_U8_PIN7_DIR    0\n\
#endif\n\
\n\
#if   PORT_U8_MODE_PIN24 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN24== PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN0_DIR    1\n\
#else       \n\
#define PORTD_U8_PIN0_DIR    0\n\
#endif      \n\
#if   PORT_U8_MODE_PIN25 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN25 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN1_DIR    1\n\
#else             \n\
#define PORTD_U8_PIN1_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN26 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN26 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN2_DIR    1\n\
#else              \n\
#define PORTD_U8_PIN2_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN27 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN27 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN3_DIR    1\n\
#else              \n\
#define PORTD_U8_PIN3_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN28 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN28 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN4_DIR    1\n\
#else              \n\
#define PORTD_U8_PIN4_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN29 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN29 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN5_DIR    1\n\
#else             \n\
#define PORTD_U8_PIN5_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN30 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN30 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN6_DIR    1\n\
#else              \n\
#define PORTD_U8_PIN6_DIR    0\n\
#endif       \n\
#if   PORT_U8_MODE_PIN31 ==   PORT_U8_MODE_OUTPUT_LOW ||  PORT_U8_MODE_PIN31 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN7_DIR    1\n\
#else              \n\
#define PORTD_U8_PIN7_DIR    0\n\
#endif\n\
\n\
//----------------------------------------------------------------------------------------------------------------------------------\n\
//----------------------------------------------------------------------------------------------------------------------------------\n\
/*Choos port */\n\
#if PORT_U8_MODE_PIN0 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN0 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN0_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN0_INTIAL_VALUE    0\n\
#endif               \n\
#if  PORT_U8_MODE_PIN1 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN1 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN1_INTIAL_VALUE    1\n\
#else                   \n\
#define PORTA_U8_PIN1_INTIAL_VALUE    0\n\
#endif                      \n\
#if  PORT_U8_MODE_PIN2 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN2 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN2_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN2_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN3 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN3 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN3_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN3_INTIAL_VALUE    0\n\
#endif              \n\
#if  PORT_U8_MODE_PIN4 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN4 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN4_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN4_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN5 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN5 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN5_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN5_INTIAL_VALUE    0\n\
#endif                \n\
\n\
#if  PORT_U8_MODE_PIN6 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN6 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN6_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN6_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN7 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN7 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTA_U8_PIN7_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTA_U8_PIN7_INTIAL_VALUE    0\n\
#endif                \n\
\n\
#if  PORT_U8_MODE_PIN8 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN8 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN0_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN0_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN9 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN9 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN1_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN1_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN10 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN10 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN2_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN2_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN11 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN11 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN3_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN3_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN12 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN12 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN4_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN4_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN13 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN13 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN5_INTIAL_VALUE    1\n\
#else                   \n\
#define PORTB_U8_PIN5_INTIAL_VALUE    0\n\
#endif                  \n\
#if  PORT_U8_MODE_PIN14 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN14 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN6_INTIAL_VALUE    1\n\
#else                   \n\
#define PORTB_U8_PIN6_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN15 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN15 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTB_U8_PIN7_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTB_U8_PIN7_INTIAL_VALUE    0\n\
#endif                            \n\
\n\
#if  PORT_U8_MODE_PIN16 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN16== PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN0_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN0_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN17 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN17 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN1_INTIAL_VALUE    1\n\
#else                \n\
#define PORTC_U8_PIN1_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN18 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN18 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN2_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN2_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN19 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN19 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN3_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN3_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN20 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN20 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN4_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN4_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN21 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN21 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN5_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN5_INTIAL_VALUE    0\n\
#endif                \n\
#if             PORT_U8_MODE_PIN22 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN22 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN6_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN6_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN23 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN23 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTC_U8_PIN7_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTC_U8_PIN7_INTIAL_VALUE    0\n\
#endif                            \n\
\n\
#if  PORT_U8_MODE_PIN24 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN24== PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN0_INTIAL_VALUE    1\n\
#else               \n\
#define PORTD_U8_PIN0_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN25 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN25 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN1_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN1_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN26 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN26 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN2_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN2_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN27 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN27 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN3_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN3_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN28 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN28 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN4_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN4_INTIAL_VALUE    0\n\
#endif                            \n\
#if  PORT_U8_MODE_PIN29 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN29 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN5_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN5_INTIAL_VALUE    0\n\
#endif               \n\
#if  PORT_U8_MODE_PIN30 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN30 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN6_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN6_INTIAL_VALUE    0\n\
#endif                \n\
#if  PORT_U8_MODE_PIN31 ==   PORT_U8_MODE_INPUT_PULLUP ||  PORT_U8_MODE_PIN31 == PORT_U8_MODE_OUTPUT_HIGH\n\
#define PORTD_U8_PIN7_INTIAL_VALUE    1\n\
#else                 \n\
#define PORTD_U8_PIN7_INTIAL_VALUE    0\n\
#endif\n\
\n\
#define conc(b7,b6,b5,b4,b3,b2,b1,b0)            conc_HLPER(b7,b6,b5,b4,b3,b2,b1,b0)\n\
#define conc_HLPER(b7,b6,b5,b4,b3,b2,b1,b0)      0b##b7##b6##b5##b4##b3##b2##b1##b0\n\
\n\
#define PORTA_U8_DIR   conc(PORTA_U8_PIN7_DIR,PORTA_U8_PIN6_DIR,PORTA_U8_PIN5_DIR,PORTA_U8_PIN4_DIR,PORTA_U8_PIN3_DIR,PORTA_U8_PIN2_DIR,PORTA_U8_PIN1_DIR,PORTA_U8_PIN0_DIR)\n\
#define PORTB_U8_DIR   conc(PORTB_U8_PIN7_DIR,PORTB_U8_PIN6_DIR,PORTB_U8_PIN5_DIR,PORTB_U8_PIN4_DIR,PORTB_U8_PIN3_DIR,PORTB_U8_PIN2_DIR,PORTB_U8_PIN1_DIR,PORTB_U8_PIN0_DIR)\n\
#define PORTC_U8_DIR   conc(PORTC_U8_PIN7_DIR,PORTC_U8_PIN6_DIR,PORTC_U8_PIN5_DIR,PORTC_U8_PIN4_DIR,PORTC_U8_PIN3_DIR,PORTC_U8_PIN2_DIR,PORTC_U8_PIN1_DIR,PORTC_U8_PIN0_DIR)\n\
#define PORTD_U8_DIR   conc(PORTD_U8_PIN7_DIR,PORTD_U8_PIN6_DIR,PORTD_U8_PIN5_DIR,PORTD_U8_PIN4_DIR,PORTD_U8_PIN3_DIR,PORTD_U8_PIN2_DIR,PORTD_U8_PIN1_DIR,PORTD_U8_PIN0_DIR)\n\
\n\
#define PORTA_U8_INTIAL_VALUE   conc(PORTA_U8_PIN7_INTIAL_VALUE,PORTA_U8_PIN6_INTIAL_VALUE,PORTA_U8_PIN5_INTIAL_VALUE,PORTA_U8_PIN4_INTIAL_VALUE,PORTA_U8_PIN3_INTIAL_VALUE,PORTA_U8_PIN2_INTIAL_VALUE,PORTA_U8_PIN1_INTIAL_VALUE,PORTA_U8_PIN0_INTIAL_VALUE)\n\
#define PORTB_U8_INTIAL_VALUE   conc(PORTB_U8_PIN7_INTIAL_VALUE,PORTB_U8_PIN6_INTIAL_VALUE,PORTB_U8_PIN5_INTIAL_VALUE,PORTB_U8_PIN4_INTIAL_VALUE,PORTB_U8_PIN3_INTIAL_VALUE,PORTB_U8_PIN2_INTIAL_VALUE,PORTB_U8_PIN1_INTIAL_VALUE,PORTB_U8_PIN0_INTIAL_VALUE)\n\
#define PORTC_U8_INTIAL_VALUE   conc(PORTC_U8_PIN7_INTIAL_VALUE,PORTC_U8_PIN6_INTIAL_VALUE,PORTC_U8_PIN5_INTIAL_VALUE,PORTC_U8_PIN4_INTIAL_VALUE,PORTC_U8_PIN3_INTIAL_VALUE,PORTC_U8_PIN2_INTIAL_VALUE,PORTC_U8_PIN1_INTIAL_VALUE,PORTC_U8_PIN0_INTIAL_VALUE)\n\
#define PORTD_U8_INTIAL_VALUE   conc(PORTD_U8_PIN7_INTIAL_VALUE,PORTD_U8_PIN6_INTIAL_VALUE,PORTD_U8_PIN5_INTIAL_VALUE,PORTD_U8_PIN4_INTIAL_VALUE,PORTD_U8_PIN3_INTIAL_VALUE,PORTD_U8_PIN2_INTIAL_VALUE,PORTD_U8_PIN1_INTIAL_VALUE,PORTD_U8_PIN0_INTIAL_VALUE)\n\
\n\
#endif')
        
        with open('Port.h','w') as f:
          f.write('#ifndef PORT_H_\n\
#define PORT_H_\n\
\n\
\n\
typedef enum\n\
{\n\
    Port_enumPinError,\n\
    Port_enumDirectionError,\n\
    Port_enumModeError,\n\
    Port_enumOK\n\
}Port_tenumErrorStatus;\n\
\n\
\n\
#define PORT_U8_PORTA                           0\n\
#define PORT_U8_PORTB                           1\n\
#define PORT_U8_PORTC                           2\n\
#define PORT_U8_PORTD                           3\n\
\n\
\n\
void Port_vidInit();\n\
Port_tenumErrorStatus Port_enuSetPinDirection(u8 Copy_u8PinNum,u8 Copy_u8Direction);\n\
Port_tenumErrorStatus Port_enuSerPinMode(u8 Copy_u8PinNum,u8 Copy_u8Mode);\n\
\n\
\n\
#endif')

        with open('Port.c','w') as f:
          f.write('#include <avr/io.h>\n\
#include "STD_Types.h"\n\
#include "BIT_UTL.h"\n\
\n\
\n\
\n\
\n\
#include "Port.h"\n\
#include "Port_confg.h"\n\
#include "Port_prv.h"\n\
\n\
\n\
\n\
\n\
\n\
\n\
void Port_vidInit()\n\
{\n\
        DDRA = PORTA_U8_DIR;\n\
        DDRB = PORTB_U8_DIR;\n\
        DDRC = PORTC_U8_DIR;\n\
        DDRD = PORTD_U8_DIR;\n\
\n\
        PORTA = PORTA_U8_INTIAL_VALUE;\n\
        PORTB = PORTB_U8_INTIAL_VALUE;\n\
        PORTC = PORTC_U8_INTIAL_VALUE;\n\
        PORTD = PORTD_U8_INTIAL_VALUE;\n\
\n\
}\n\
Port_tenumErrorStatus Port_enuSetPinDirection(u8 Copy_u8PinNum,u8 Copy_u8Direction)\n\
{\n\
        Port_tenumErrorStatus Loc_enuReturnStatus = Port_enumOK;\n\
        u8 Loc_u8Port;\n\
        u8 Loc_u8Pin;\n\
        if(Copy_u8PinNum>31)\n\
        {\n\
                Loc_enuReturnStatus = Port_enumPinError;\n\
        }\n\
        else if(Copy_u8Direction>1)\n\
        {\n\
                Loc_enuReturnStatus = Port_enumDirectionError;\n\
        }\n\
        else\n\
        {\n\
                Loc_u8Port = Copy_u8PinNum / 8;\n\
                Loc_u8Pin = Copy_u8PinNum % 8;\n\
                switch(Loc_u8Port)\n\
                {\n\
                        case PORT_U8_PORTA:\n\
                                        if(Copy_u8Direction==PORT_U8_DIR_OUTPUT)\n\
                                        {\n\
                                                SET_BIT(DDRA,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRA,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
                        case PORT_U8_PORTB:\n\
                                        if(Copy_u8Direction==PORT_U8_DIR_OUTPUT)\n\
                                        {\n\
                                                SET_BIT(DDRB,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRB,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
                        case PORT_U8_PORTC:\n\
                                        if(Copy_u8Direction==PORT_U8_DIR_OUTPUT)\n\
                                        {\n\
                                                SET_BIT(DDRC,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRC,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
                        case PORT_U8_PORTD:\n\
                                        if(Copy_u8Direction==PORT_U8_DIR_OUTPUT)\n\
                                        {\n\
                                                SET_BIT(DDRD,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRD,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
                }\n\
        }\n\
\n\
        return Loc_enuReturnStatus;\n\
}\n\
Port_tenumErrorStatus Port_enuSerPinMode(u8 Copy_u8PinNum,u8 Copy_u8Mode)\n\
{\n\
        Port_tenumErrorStatus Loc_enuReturnStatus = Port_enumOK;\n\
        u8 Loc_u8Port;\n\
        u8 Loc_u8Pin;\n\
        if(Copy_u8PinNum>31)\n\
        {\n\
                Loc_enuReturnStatus = Port_enumPinError;\n\
        }\n\
        else if(Copy_u8Mode>3)\n\
        {\n\
                Loc_enuReturnStatus = Port_enumDirectionError;\n\
        }\n\
        else\n\
        {\n\
                Loc_u8Port = Copy_u8PinNum / 8;\n\
                Loc_u8Pin = Copy_u8PinNum % 8;\n\
                switch(Loc_u8Port)\n\
                {\n\
                        case PORT_U8_PORTA:\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH || Copy_u8Mode == PORT_U8_MODE_OUTPUT_LOW)\n\
                                        {\n\
                                                SET_BIT(DDRA,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRA,Loc_u8Pin);\n\
                                        }\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_INPUT_HIGHIMP || Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH)\n\
                                        {\n\
                                                SET_BIT(PORTA,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(PORTA,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
\n\
                        case PORT_U8_PORTB:\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH || Copy_u8Mode == PORT_U8_MODE_OUTPUT_LOW)\n\
                                        {\n\
                                                SET_BIT(DDRB,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(DDRB,Loc_u8Pin);\n\
                                        }\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_INPUT_HIGHIMP || Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH)\n\
                                        {\n\
                                                SET_BIT(PORTB,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                                CLR_BIT(PORTB,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
                        case PORT_U8_PORTC:\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH || Copy_u8Mode == PORT_U8_MODE_OUTPUT_LOW)\n\
                                        {\n\
                                        SET_BIT(DDRC,Loc_u8Pin);\n\
                                        }\n\
                                        else\n\
                                        {\n\
                                        CLR_BIT(DDRC,Loc_u8Pin);\n\
                                        }\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_INPUT_HIGHIMP || Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH)\n\
                    {\n\
                                        SET_BIT(PORTC,Loc_u8Pin);\n\
                                    }\n\
                                    else\n\
                                    {\n\
                                        CLR_BIT(PORTC,Loc_u8Pin);\n\
                                    }\n\
                                    break;\n\
\n\
\n\
\n\
                        case PORT_U8_PORTD:\n\
                                        if(Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH || Copy_u8Mode == PORT_U8_MODE_OUTPUT_LOW)\n\
                                    {\n\
                                        SET_BIT(DDRD,Loc_u8Pin);\n\
                                    }\n\
                                    else\n\
                                    {\n\
                                        CLR_BIT(DDRD,Loc_u8Pin);\n\
                                    }\n\
                                    if(Copy_u8Mode == PORT_U8_MODE_INPUT_HIGHIMP || Copy_u8Mode == PORT_U8_MODE_OUTPUT_HIGH)\n\
                                    {\n\
                                        SET_BIT(PORTD,Loc_u8Pin);\n\
                                    }\n\
                                        else\n\
                                    {\n\
                                                CLR_BIT(PORTD,Loc_u8Pin);\n\
                                        }\n\
                                        break;\n\
\n\
                }\n\
        }\n\
        return Loc_enuReturnStatus;\n\
}')
        
    def Input_FloatingClcked0(self):
        global PinCfgList
        PinCfgList[0] = 0
    
    def InputPulLUpClcked0(self):
        global PinCfgList
        PinCfgList[0] = 1
    
    def OutputLowClcked0(self):
        global PinCfgList
        PinCfgList[0] = 2
    
    def OutputHighClcked0(self):
        global PinCfgList
        PinCfgList[0] = 3
        self.retranslateUi(MainWindow)
        
    def Input_FloatingClcked1(self):
        global PinCfgList
        PinCfgList[1] = 0
    
    def InputPulLUpClcked1(self):
        global PinCfgList
        PinCfgList[1] = 1
    
    def OutputLowClcked1(self):
        global PinCfgList
        PinCfgList[1] = 2
    
    def OutputHighClcked1(self):
        global PinCfgList
        PinCfgList[1] = 3
        self.retranslateUi(MainWindow)
        
    def Input_FloatingClcked2(self):
        global PinCfgList
        PinCfgList[2] = 0
    
    def InputPulLUpClcked2(self):
        global PinCfgList
        PinCfgList[2] = 1
    
    def OutputLowClcked2(self):
        global PinCfgList
        PinCfgList[2] = 2
    
    def OutputHighClcked2(self):
        global PinCfgList
        PinCfgList[2] = 3
###########################
    def Input_FloatingClcked3(self):
        global PinCfgList
        PinCfgList[3] = 0
    
    def InputPulLUpClcked3(self):
        global PinCfgList
        PinCfgList[3] = 1
    
    def OutputLowClcked3(self):
        global PinCfgList
        PinCfgList[3] = 2
    
    def OutputHighClcked3(self):
        global PinCfgList
        PinCfgList[3] = 3
###########################
    def Input_FloatingClcked4(self):
        global PinCfgList
        PinCfgList[4] = 0
    
    def InputPulLUpClcked4(self):
        global PinCfgList
        PinCfgList[4] = 1
    
    def OutputLowClcked4(self):
        global PinCfgList
        PinCfgList[4] = 2
    
    def OutputHighClcked4(self):
        global PinCfgList
        PinCfgList[4] = 3
###########################
    def Input_FloatingClcked5(self):
        global PinCfgList
        PinCfgList[5] = 0
    
    def InputPulLUpClcked5(self):
        global PinCfgList
        PinCfgList[5] = 1
    
    def OutputLowClcked5(self):
        global PinCfgList
        PinCfgList[5] = 2
    
    def OutputHighClcked5(self):
        global PinCfgList
        PinCfgList[5] = 3
###########################
    def Input_FloatingClcked6(self):
        global PinCfgList
        PinCfgList[6] = 0
    
    def InputPulLUpClcked6(self):
        global PinCfgList
        PinCfgList[6] = 1
    
    def OutputLowClcked6(self):
        global PinCfgList
        PinCfgList[6] = 2
    
    def OutputHighClcked6(self):
        global PinCfgList
        PinCfgList[6] = 3
###########################
    def Input_FloatingClcked7(self):
        global PinCfgList
        PinCfgList[7] = 0
    
    def InputPulLUpClcked7(self):
        global PinCfgList
        PinCfgList[7] = 1
    
    def OutputLowClcked7(self):
        global PinCfgList
        PinCfgList[7] = 2
    
    def OutputHighClcked7(self):
        global PinCfgList
        PinCfgList[7] = 3
###########################
    def Input_FloatingClcked8(self):
        global PinCfgList
        PinCfgList[8] = 0
    
    def InputPulLUpClcked8(self):
        global PinCfgList
        PinCfgList[8] = 1
    
    def OutputLowClcked8(self):
        global PinCfgList
        PinCfgList[8] = 2
    
    def OutputHighClcked8(self):
        global PinCfgList
        PinCfgList[8] = 3
###########################
    def Input_FloatingClcked9(self):
        global PinCfgList
        PinCfgList[9] = 0
    
    def InputPulLUpClcked9(self):
        global PinCfgList
        PinCfgList[9] = 1
    
    def OutputLowClcked9(self):
        global PinCfgList
        PinCfgList[9] = 2
    
    def OutputHighClcked9(self):
        global PinCfgList
        PinCfgList[9] = 3
###########################
    def Input_FloatingClcked10(self):
        global PinCfgList
        PinCfgList[10] = 0
    
    def InputPulLUpClcked10(self):
        global PinCfgList
        PinCfgList[10] = 1
    
    def OutputLowClcked10(self):
        global PinCfgList
        PinCfgList[10] = 2
    
    def OutputHighClcked10(self):
        global PinCfgList
        PinCfgList[10] = 3
###########################
    def Input_FloatingClcked11(self):
        global PinCfgList
        PinCfgList[11] = 0
    
    def InputPulLUpClcked11(self):
        global PinCfgList
        PinCfgList[11] = 1
    
    def OutputLowClcked11(self):
        global PinCfgList
        PinCfgList[11] = 2
    
    def OutputHighClcked11(self):
        global PinCfgList
        PinCfgList[11] = 3
###########################
    def Input_FloatingClcked12(self):
        global PinCfgList
        PinCfgList[12] = 0
    
    def InputPulLUpClcked12(self):
        global PinCfgList
        PinCfgList[12] = 1
    
    def OutputLowClcked12(self):
        global PinCfgList
        PinCfgList[12] = 2
    
    def OutputHighClcked12(self):
        global PinCfgList
        PinCfgList[12] = 3
###########################
    def Input_FloatingClcked13(self):
        global PinCfgList
        PinCfgList[13] = 0
    
    def InputPulLUpClcked13(self):
        global PinCfgList
        PinCfgList[13] = 1
    
    def OutputLowClcked13(self):
        global PinCfgList
        PinCfgList[13] = 2
    
    def OutputHighClcked13(self):
        global PinCfgList
        PinCfgList[13] = 3
###########################
    def Input_FloatingClcked14(self):
        global PinCfgList
        PinCfgList[14] = 0
    
    def InputPulLUpClcked14(self):
        global PinCfgList
        PinCfgList[14] = 1
    
    def OutputLowClcked14(self):
        global PinCfgList
        PinCfgList[14] = 2
    
    def OutputHighClcked14(self):
        global PinCfgList
        PinCfgList[14] = 3
###########################
    def Input_FloatingClcked15(self):
        global PinCfgList
        PinCfgList[15] = 0
    
    def InputPulLUpClcked15(self):
        global PinCfgList
        PinCfgList[15] = 1
    
    def OutputLowClcked15(self):
        global PinCfgList
        PinCfgList[15] = 2
    
    def OutputHighClcked15(self):
        global PinCfgList
        PinCfgList[15] = 3
###########################
    def Input_FloatingClcked16(self):
        global PinCfgList
        PinCfgList[16] = 0
    
    def InputPulLUpClcked16(self):
        global PinCfgList
        PinCfgList[16] = 1
    
    def OutputLowClcked16(self):
        global PinCfgList
        PinCfgList[16] = 2
    
    def OutputHighClcked16(self):
        global PinCfgList
        PinCfgList[16] = 3
###########################
    def Input_FloatingClcked17(self):
        global PinCfgList
        PinCfgList[17] = 0
    
    def InputPulLUpClcked17(self):
        global PinCfgList
        PinCfgList[17] = 1
    
    def OutputLowClcked17(self):
        global PinCfgList
        PinCfgList[17] = 2
    
    def OutputHighClcked17(self):
        global PinCfgList
        PinCfgList[17] = 3
###########################
    def Input_FloatingClcked18(self):
        global PinCfgList
        PinCfgList[18] = 0
    
    def InputPulLUpClcked18(self):
        global PinCfgList
        PinCfgList[18] = 1
    
    def OutputLowClcked18(self):
        global PinCfgList
        PinCfgList[18] = 2
    
    def OutputHighClcked18(self):
        global PinCfgList
        PinCfgList[18] = 3
###########################
    def Input_FloatingClcked19(self):
        global PinCfgList
        PinCfgList[19] = 0
    
    def InputPulLUpClcked19(self):
        global PinCfgList
        PinCfgList[19] = 1
    
    def OutputLowClcked19(self):
        global PinCfgList
        PinCfgList[19] = 2
    
    def OutputHighClcked19(self):
        global PinCfgList
        PinCfgList[19] = 3
###########################
    def Input_FloatingClcked20(self):
        global PinCfgList
        PinCfgList[20] = 0
    
    def InputPulLUpClcked20(self):
        global PinCfgList
        PinCfgList[20] = 1
    
    def OutputLowClcked20(self):
        global PinCfgList
        PinCfgList[20] = 2
    
    def OutputHighClcked20(self):
        global PinCfgList
        PinCfgList[20] = 3
###########################
    def Input_FloatingClcked21(self):
        global PinCfgList
        PinCfgList[21] = 0
    
    def InputPulLUpClcked21(self):
        global PinCfgList
        PinCfgList[21] = 1
    
    def OutputLowClcked21(self):
        global PinCfgList
        PinCfgList[21] = 2
    
    def OutputHighClcked21(self):
        global PinCfgList
        PinCfgList[21] = 3
###########################
    def Input_FloatingClcked21(self):
        global PinCfgList
        PinCfgList[21] = 0
    
    def InputPulLUpClcked21(self):
        global PinCfgList
        PinCfgList[21] = 1
    
    def OutputLowClcked21(self):
        global PinCfgList
        PinCfgList[21] = 2
    
    def OutputHighClcked21(self):
        global PinCfgList
        PinCfgList[21] = 3
###########################
    def Input_FloatingClcked22(self):
        global PinCfgList
        PinCfgList[22] = 0
    
    def InputPulLUpClcked22(self):
        global PinCfgList
        PinCfgList[22] = 1
    
    def OutputLowClcked22(self):
        global PinCfgList
        PinCfgList[22] = 2
    
    def OutputHighClcked22(self):
        global PinCfgList
        PinCfgList[22] = 3
###########################
    def Input_FloatingClcked23(self):
        global PinCfgList
        PinCfgList[23] = 0
    
    def InputPulLUpClcked23(self):
        global PinCfgList
        PinCfgList[23] = 1
    
    def OutputLowClcked23(self):
        global PinCfgList
        PinCfgList[23] = 2
    
    def OutputHighClcked23(self):
        global PinCfgList
        PinCfgList[23] = 3
###########################
    def Input_FloatingClcked24(self):
        global PinCfgList
        PinCfgList[24] = 0
    
    def InputPulLUpClcked24(self):
        global PinCfgList
        PinCfgList[24] = 1
    
    def OutputLowClcked24(self):
        global PinCfgList
        PinCfgList[24] = 2
    
    def OutputHighClcked24(self):
        global PinCfgList
        PinCfgList[24] = 3
###########################
    def Input_FloatingClcked25(self):
        global PinCfgList
        PinCfgList[25] = 0
    
    def InputPulLUpClcked25(self):
        global PinCfgList
        PinCfgList[25] = 1
    
    def OutputLowClcked25(self):
        global PinCfgList
        PinCfgList[25] = 2
    
    def OutputHighClcked25(self):
        global PinCfgList
        PinCfgList[25] = 3
###########################
    def Input_FloatingClcked26(self):
        global PinCfgList
        PinCfgList[26] = 0
    
    def InputPulLUpClcked26(self):
        global PinCfgList
        PinCfgList[26] = 1
    
    def OutputLowClcked26(self):
        global PinCfgList
        PinCfgList[26] = 2
    
    def OutputHighClcked26(self):
        global PinCfgList
        PinCfgList[26] = 3
###########################
    def Input_FloatingClcked27(self):
        global PinCfgList
        PinCfgList[27] = 0
    
    def InputPulLUpClcked27(self):
        global PinCfgList
        PinCfgList[27] = 1
    
    def OutputLowClcked27(self):
        global PinCfgList
        PinCfgList[27] = 2
    
    def OutputHighClcked27(self):
        global PinCfgList
        PinCfgList[27] = 3
###########################
    def Input_FloatingClcked28(self):
        global PinCfgList
        PinCfgList[28] = 0
    
    def InputPulLUpClcked28(self):
        global PinCfgList
        PinCfgList[28] = 1
    
    def OutputLowClcked28(self):
        global PinCfgList
        PinCfgList[28] = 2
    
    def OutputHighClcked28(self):
        global PinCfgList
        PinCfgList[28] = 3
###########################
    def Input_FloatingClcked29(self):
        global PinCfgList
        PinCfgList[29] = 0
    
    def InputPulLUpClcked29(self):
        global PinCfgList
        PinCfgList[29] = 1
    
    def OutputLowClcked29(self):
        global PinCfgList
        PinCfgList[29] = 2
    
    def OutputHighClcked29(self):
        global PinCfgList
        PinCfgList[29] = 3
###########################
    def Input_FloatingClcked30(self):
        global PinCfgList
        PinCfgList[30] = 0
    
    def InputPulLUpClcked30(self):
        global PinCfgList
        PinCfgList[30] = 1
    
    def OutputLowClcked30(self):
        global PinCfgList
        PinCfgList[30] = 2
    
    def OutputHighClcked30(self):
        global PinCfgList
        PinCfgList[30] = 3
###########################
    def Input_FloatingClcked31(self):
        global PinCfgList
        PinCfgList[31] = 0
    
    def InputPulLUpClcked31(self):
        global PinCfgList
        PinCfgList[31] = 1
    
    def OutputLowClcked31(self):
        global PinCfgList
        PinCfgList[31] = 2
    
    def OutputHighClcked31(self):
        global PinCfgList
        PinCfgList[31] = 3
###########################
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Avr Pin Configuration ", None))
        self.PIN0.setTitle(QCoreApplication.translate("Form", u"Pin0", None))
        self.IP0.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH0.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL0.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH0.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN1.setTitle(QCoreApplication.translate("Form", u"Pin1", None))
        self.IP1.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH1.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL1.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH1.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN2.setTitle(QCoreApplication.translate("Form", u"Pin2", None))
        self.IP2.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH2.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL2.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH2.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN3.setTitle(QCoreApplication.translate("Form", u"Pin3", None))
        self.IP3.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH3.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL3.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH3.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN4.setTitle(QCoreApplication.translate("Form", u"Pin4", None))
        self.IP4.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH4.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL4.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH4.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN5.setTitle(QCoreApplication.translate("Form", u"Pin5", None))
        self.IP5.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH5.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL5.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH5.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN6.setTitle(QCoreApplication.translate("Form", u"Pin6", None))
        self.IP6.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH6.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL6.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH6.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN7.setTitle(QCoreApplication.translate("Form", u"Pin7", None))
        self.IP7.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH7.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL7.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH7.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN8.setTitle(QCoreApplication.translate("Form", u"Pin8", None))
        self.IP8.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH8.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL8.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH8.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN9.setTitle(QCoreApplication.translate("Form", u"Pin9", None))
        self.IP9.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH9.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL9.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH9.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN10.setTitle(QCoreApplication.translate("Form", u"Pin10", None))
        self.IP10.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH10.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL10.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH10.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN11.setTitle(QCoreApplication.translate("Form", u"Pin11", None))
        self.IP11.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH11.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL11.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH11.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN12.setTitle(QCoreApplication.translate("Form", u"Pin12", None))
        self.IP12.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH12.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL12.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH12.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN14.setTitle(QCoreApplication.translate("Form", u"Pin14", None))
        self.IP14.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH14.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL14.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH14.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN15.setTitle(QCoreApplication.translate("Form", u"Pin15", None))
        self.IP15.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH15.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL15.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH15.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN16.setTitle(QCoreApplication.translate("Form", u"Pin16", None))
        self.IP16.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH16.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL16.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH16.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN17.setTitle(QCoreApplication.translate("Form", u"Pin17", None))
        self.IP17.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH17.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL17.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH17.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN18.setTitle(QCoreApplication.translate("Form", u"Pin18", None))
        self.IP18.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH18.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL18.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH18.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN19.setTitle(QCoreApplication.translate("Form", u"Pin19", None))
        self.IP19.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH19.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL19.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH19.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN20.setTitle(QCoreApplication.translate("Form", u"Pin20", None))
        self.IP20.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH20.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL20.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH20.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN21.setTitle(QCoreApplication.translate("Form", u"Pin21", None))
        self.IP21.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH21.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL21.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH21.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN22.setTitle(QCoreApplication.translate("Form", u"Pin22", None))
        self.IP22.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH22.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL22.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH22.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN23.setTitle(QCoreApplication.translate("Form", u"Pin23", None))
        self.IP23.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH23.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL23.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH23.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN24.setTitle(QCoreApplication.translate("Form", u"Pin24", None))
        self.IP24.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH24.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL24.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH24.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN25.setTitle(QCoreApplication.translate("Form", u"Pin25", None))
        self.IP25.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH25.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL25.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH25.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN26.setTitle(QCoreApplication.translate("Form", u"Pin26", None))
        self.IP26.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH26.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL26.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH26.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN27.setTitle(QCoreApplication.translate("Form", u"Pin27", None))
        self.IP27.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH27.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL27.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH27.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN28.setTitle(QCoreApplication.translate("Form", u"Pin28", None))
        self.IP28.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH28.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL28.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH28.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN29.setTitle(QCoreApplication.translate("Form", u"Pin29", None))
        self.IP29.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH29.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL29.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH29.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN30.setTitle(QCoreApplication.translate("Form", u"Pin30", None))
        self.IP30.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH30.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL30.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH30.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN31.setTitle(QCoreApplication.translate("Form", u"Pin31", None))
        self.IP31.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH31.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL31.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH31.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.PIN13.setTitle(QCoreApplication.translate("Form", u"Pin13", None))
        self.IP13.setText(QCoreApplication.translate("Form", u"input pullup", None))
        self.IH13.setText(QCoreApplication.translate("Form", u"input high impedunce", None))
        self.OL13.setText(QCoreApplication.translate("Form", u"Output Llow", None))
        self.OH13.setText(QCoreApplication.translate("Form", u"Output High", None))
        self.Gen.setText(QCoreApplication.translate("Form", u"Genrate Port Stack", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.load.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
