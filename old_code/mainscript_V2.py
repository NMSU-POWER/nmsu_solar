# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_Plot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys
import time
import random 
import numpy as np
import socket 
from RS485 import *
from DeviceAddress import *
from Serial_TX import *
import datetime
import pickle
import serial


[RS485Port,UARTPort]=Find_Port()
Obj=[]
for name in DCCURRENT.keys():
    Obj.append(DCCurrent(name,DCCURRENT[name][0],RS485Port,DCCURRENT[name][1]))
for name in DCVOLTAGE.keys():
    Obj.append(DCVoltage(name,DCVOLTAGE[name][0],RS485Port,DCVOLTAGE[name][1]))
for name in ACMETER.keys():
    Obj.append(ACMeter(name,ACMETER[name][0],RS485Port,ACMETER[name][1]))
for name in THERM.keys():
    Obj.append(Therm(name,THERM[name][0],RS485Port,THERM[name][1]))    
SerialObj=RxTx_Object('NMSU Measurments')
Obj=Read_Meters(Obj)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.PlotData1=[]
        self.PlotData2=[]
        self.SelectPlot=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.widget_12 = QtWidgets.QWidget(self.centralwidget)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_3 = QtWidgets.QWidget(self.widget_12)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.PlotSelectLabel = QtWidgets.QLabel(self.widget_10)
        self.PlotSelectLabel.setObjectName("PlotSelectLabel")
        self.horizontalLayout_9.addWidget(self.PlotSelectLabel)
        self.verticalLayout_3.addWidget(self.widget_10)
        self.PLotHolder = PlotWidget(self.widget_9)
        self.PLotHolder.setObjectName("PLotHolder")
        self.curve=self.PLotHolder.plot(self.PlotData1,pen='r')
        self.curve2=self.PLotHolder.plot(self.PlotData2,pen='b')
        self.verticalLayout_3.addWidget(self.PLotHolder)
        self.widget_11 = QtWidgets.QWidget(self.widget_9)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.PlotSelectFixed = QtWidgets.QLabel(self.widget_11)
        self.PlotSelectFixed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PlotSelectFixed.setObjectName("PlotSelectFixed")
        self.horizontalLayout_8.addWidget(self.PlotSelectFixed)
        self.comboBox = QtWidgets.QComboBox(self.widget_11)
        self.comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(1, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("DC Currents")
        self.comboBox.addItem("DC Voltages")
        self.comboBox.addItem("AC Current")
        self.comboBox.addItem("AC Voltage")
        self.comboBox.addItem("AC Powers")
        self.comboBox.addItem("Temperatures")
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SP_Current = QtWidgets.QLabel(self.widget_2)
        self.SP_Current.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SP_Current.setObjectName("SP_Current")
        self.horizontalLayout_2.addWidget(self.SP_Current)
        self.Panel_DC_Current_lcd = QtWidgets.QLCDNumber(self.widget_2)
        self.Panel_DC_Current_lcd.setObjectName("Panel_DC_Current_lcd")
        self.Panel_DC_Current_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Panel_DC_Current_lcd.setStyleSheet("background-color: black")
        palette=self.Panel_DC_Current_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        self.Panel_DC_Current_lcd.setPalette(palette)
        self.horizontalLayout_2.addWidget(self.Panel_DC_Current_lcd)
        self.MI_Current = QtWidgets.QLabel(self.widget_2)
        self.MI_Current.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MI_Current.setObjectName("MI_Current")
        self.horizontalLayout_2.addWidget(self.MI_Current)
        self.Inverter_DC_Current_lcd = QtWidgets.QLCDNumber(self.widget_2)
        self.Inverter_DC_Current_lcd.setObjectName("Inverter_DC_Current_lcd")
        self.Inverter_DC_Current_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Inverter_DC_Current_lcd.setStyleSheet("background-color: black")
        palette=self.Inverter_DC_Current_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 0, 255))
        self.Inverter_DC_Current_lcd.setPalette(palette)
        self.horizontalLayout_2.addWidget(self.Inverter_DC_Current_lcd)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.DCMeter_1 = QtWidgets.QLabel(self.widget_5)
        self.DCMeter_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DCMeter_1.setObjectName("DCMeter_1")
        self.horizontalLayout_3.addWidget(self.DCMeter_1)
        self.Panel_DC_Voltage_lcd = QtWidgets.QLCDNumber(self.widget_5)
        self.Panel_DC_Voltage_lcd.setObjectName("Panel_DC_Voltage_lcd")
        self.Panel_DC_Voltage_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Panel_DC_Voltage_lcd.setStyleSheet("background-color: black")
        palette=self.Panel_DC_Voltage_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        self.Panel_DC_Voltage_lcd.setPalette(palette)
        self.horizontalLayout_3.addWidget(self.Panel_DC_Voltage_lcd)
        self.DCMeter_2 = QtWidgets.QLabel(self.widget_5)
        self.DCMeter_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DCMeter_2.setObjectName("DCMeter_2")
        self.horizontalLayout_3.addWidget(self.DCMeter_2)
        self.Inverter_DC_Current_lcd_2 = QtWidgets.QLCDNumber(self.widget_5)
        self.Inverter_DC_Current_lcd_2.setObjectName("Inverter_DC_Current_lcd_2")
        self.Inverter_DC_Current_lcd_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Inverter_DC_Current_lcd_2.setStyleSheet("background-color: black")
        palette=self.Inverter_DC_Current_lcd_2.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 0, 255))
        self.Inverter_DC_Current_lcd_2.setPalette(palette)
        self.horizontalLayout_3.addWidget(self.Inverter_DC_Current_lcd_2)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ACCurrent = QtWidgets.QLabel(self.widget_6)
        self.ACCurrent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACCurrent.setObjectName("ACCurrent")
        self.horizontalLayout_4.addWidget(self.ACCurrent)
        self.AC_Inverter_Current_lcd = QtWidgets.QLCDNumber(self.widget_6)
        self.AC_Inverter_Current_lcd.setObjectName("AC_Inverter_Current_lcd")
        self.AC_Inverter_Current_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.AC_Inverter_Current_lcd.setStyleSheet("background-color: black")
        palette=self.AC_Inverter_Current_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(85, 255, 255))
        self.AC_Inverter_Current_lcd.setPalette(palette)
        self.horizontalLayout_4.addWidget(self.AC_Inverter_Current_lcd)
        self.ACVoltage = QtWidgets.QLabel(self.widget_6)
        self.ACVoltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACVoltage.setObjectName("ACVoltage")
        self.horizontalLayout_4.addWidget(self.ACVoltage)
        self.AC_Inverter_Voltage_lcd = QtWidgets.QLCDNumber(self.widget_6)
        self.AC_Inverter_Voltage_lcd.setObjectName("AC_Inverter_Voltage_lcd")
        self.AC_Inverter_Voltage_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.AC_Inverter_Voltage_lcd.setStyleSheet("background-color: black")
        palette=self.AC_Inverter_Voltage_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(85, 255, 255))
        self.AC_Inverter_Voltage_lcd.setPalette(palette)
        self.horizontalLayout_4.addWidget(self.AC_Inverter_Voltage_lcd)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ACPower = QtWidgets.QLabel(self.widget_7)
        self.ACPower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACPower.setObjectName("ACPower")
        self.horizontalLayout_5.addWidget(self.ACPower)
        self.AC_Inverter_Power_lcd = QtWidgets.QLCDNumber(self.widget_7)
        self.AC_Inverter_Power_lcd.setObjectName("AC_Inverter_Power_lcd")
        self.AC_Inverter_Power_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.AC_Inverter_Power_lcd.setStyleSheet("background-color: black")
        palette=self.AC_Inverter_Power_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        self.AC_Inverter_Power_lcd.setPalette(palette)
        self.horizontalLayout_5.addWidget(self.AC_Inverter_Power_lcd)
        self.ACBuildingPower = QtWidgets.QLabel(self.widget_7)
        self.ACBuildingPower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ACBuildingPower.setObjectName("ACBuildingPower")
        self.horizontalLayout_5.addWidget(self.ACBuildingPower)
        self.Building_Phase_Load_lcd = QtWidgets.QLCDNumber(self.widget_7)
        self.Building_Phase_Load_lcd.setObjectName("Building_Phase_Load_lcd")
        self.Building_Phase_Load_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Building_Phase_Load_lcd.setStyleSheet("background-color: black")
        palette=self.Building_Phase_Load_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 0, 255))
        self.Building_Phase_Load_lcd.setPalette(palette)
        self.horizontalLayout_5.addWidget(self.Building_Phase_Load_lcd)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ABTemp = QtWidgets.QLabel(self.widget_8)
        self.ABTemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ABTemp.setObjectName("ABTemp")
        self.horizontalLayout_6.addWidget(self.ABTemp)
        self.Ambient_Panel_Temp_lcd = QtWidgets.QLCDNumber(self.widget_8)
        self.Ambient_Panel_Temp_lcd.setObjectName("Ambient_Panel_Temp_lcd")
        self.Ambient_Panel_Temp_lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.Ambient_Panel_Temp_lcd.setStyleSheet("background-color: black")
        palette=self.Ambient_Panel_Temp_lcd.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        self.Ambient_Panel_Temp_lcd.setPalette(palette)
        self.horizontalLayout_6.addWidget(self.Ambient_Panel_Temp_lcd)
        self.STemp = QtWidgets.QLabel(self.widget_8)
        self.STemp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.STemp.setObjectName("STemp")
        self.horizontalLayout_6.addWidget(self.STemp)
        self.S = QtWidgets.QLCDNumber(self.widget_8)
        self.S.setObjectName("S")
        self.S.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.S.setStyleSheet("background-color: black")
        palette=self.S.palette()
        palette.setColor(palette.WindowText, QtGui.QColor(0, 0, 255))
        self.S.setPalette(palette)
        self.horizontalLayout_6.addWidget(self.S)
        self.verticalLayout.addWidget(self.widget_8)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TimeUpdate = QtWidgets.QLabel(self.widget_4)
        self.TimeUpdate.setObjectName("TimeUpdate")
        self.horizontalLayout.addWidget(self.TimeUpdate)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_8.addWidget(self.widget_3)
        self.horizontalLayout_18.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.centralwidget)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_18.addWidget(self.widget_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.Data_Thread=DataThread()  
        self.Data_Thread.signal.connect(self.GuiUpdate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: DC Currents"))
        self.PlotSelectFixed.setText(_translate("MainWindow", "Plot "))
        self.SP_Current.setText(_translate("MainWindow", "Panel DC Current"))
        self.MI_Current.setText(_translate("MainWindow", "Inverter DC Current"))
        self.DCMeter_1.setText(_translate("MainWindow", "Panel DC Voltage "))
        self.DCMeter_2.setText(_translate("MainWindow", "Inverter DC Voltage "))
        self.ACCurrent.setText(_translate("MainWindow", "AC Inverter Current"))
        self.ACVoltage.setText(_translate("MainWindow", "AC Inverter Voltage"))
        self.ACPower.setText(_translate("MainWindow", "AC Inverter Power"))
        self.ACBuildingPower.setText(_translate("MainWindow", "Building Phase Load"))
        self.ABTemp.setText(_translate("MainWindow", "Ambient Panel Temp"))
        self.STemp.setText(_translate("MainWindow", "Surface Panel Temp"))
        self.TimeUpdate.setText(_translate("MainWindow", "Last Udpate: "))
    def selectionchange(self,i):
        global PlotData1
        _translate = QtCore.QCoreApplication.translate
        self.SelectPlot=i
        if self.SelectPlot==0:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: DC Currents"))
        elif self.SelectPlot==1:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: DC Voltages"))
        elif self.SelectPlot==2:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: AC Current"))
        elif self.SelectPlot==3:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: AC Voltage"))
        elif self.SelectPlot==4:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: AC Powers"))
        elif self.SelectPlot==5:
            self.PlotSelectLabel.setText(_translate("MainWindow", "Plotting: Temperatures"))
        self.PlotData1=self.Data[self.SelectPlot][0]
        if len(self.Data[self.SelectPlot])==2:
            self.PlotData2=self.Data[self.SelectPlot][1] 
        else:
            self.PlotData2=[]
        self.PLotHolder.plot(clear=True)
        self.curve=self.PLotHolder.plot(self.PlotData1,pen='r')
        self.curve2=self.PLotHolder.plot(self.PlotData2,pen='b')
    def CallGuiUpdate(self):
        self.Data_Thread.start()
    def GuiUpdate(self,result):
        self.Data=result
        self.Panel_DC_Current_lcd.display(result[0][0][len(result[0][0])-1])
        self.Inverter_DC_Current_lcd.display(result[0][1][len(result[0][1])-1])
        self.Panel_DC_Voltage_lcd.display(result[1][0][len(result[1][0])-1])
        self.Inverter_DC_Current_lcd_2.display(result[1][1][len(result[1][1])-1])
        self.AC_Inverter_Current_lcd.display(result[2][0][len(result[2][0])-1])
        self.AC_Inverter_Voltage_lcd.display(result[3][0][len(result[3][0])-1])
        self.AC_Inverter_Power_lcd.display(result[4][0][len(result[4][0])-1])
        self.Ambient_Panel_Temp_lcd.display(result[5][0][len(result[5][0])-1])
        self.S.display(result[5][1][len(result[5][1])-1])
        self.PlotData1=result[self.SelectPlot][0]
        if len(result[self.SelectPlot])==2:
            self.PlotData2=result[self.SelectPlot][1] 
        else:
            self.PlotData2=[]
        self.curve.setData(self.PlotData1)
        self.curve2.setData(self.PlotData2)
        

        # self.curve.setData(result[0])
        # self.curve2.setData(result[1])


class DataThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self):
        QThread.__init__(self)
        self.MIData=[]
        self.SPData=[]
        self.DC1Data=[]
        self.DC2Data=[]
        self.ACIData=[]
        self.ACVData=[]
        self.ACPData=[]
        self.ATData=[]
        self.STData=[]
        self.Blank=[]
    def run(self):
        global Obj
        while True:
            timestamp=datetime.datetime.now()
            if timestamp.second%5==0 and Marker==True:
                Obj=Read_Meters(Obj)
                SerialObj.Update(Obj)
                f=open(FileName,'a')
                TMark=datetime.datetime.now()
                print TMark
                f.write('Time: '+str(TMark.hour)+':'+str(TMark.minute)+':'+str(TMark.second)+'\n')
                for i in range(len(Obj)):
                    if 'MI' in Obj[i].Name:
                        print Obj[i].Name+' Current='+str(Obj[i].I)+'A'
                        f.write(Obj[i].Name+' Current='+str(Obj[i].I)+'A\n')
                        if Obj[i].Name=='MI-1':
                            self.MIData.append(Obj[i].I)
                    if 'DCMeter' in Obj[i].Name:
                        print Obj[i].Name+' Voltages: '+str(Obj[i].V1*6)+' '+str(Obj[i].V2*6)+' '+str(Obj[i].V3*6)+' '+str(Obj[i].V4*6)
                        f.write(Obj[i].Name+' Voltages: '+str(Obj[i].V1)+' '+str(Obj[i].V2)+' '+str(Obj[i].V3)+' '+str(Obj[i].V4)+'\n')
                        if Obj[i].Name=='DCMeter-1':
                            self.DC1Data.append(Obj[i].V1*6)
                        else:
                            self.DC2Data.append(Obj[i].V1*6)
                    if 'ACMeter-1' in Obj[i].Name:
                        print Obj[i].Name+' Volatges: '+str(Obj[i].Va)+' '+str(Obj[i].Vb)+' '+str(Obj[i].Vc)
                        print Obj[i].Name+' Currents: '+str(Obj[i].Ia)+' '+str(Obj[i].Ib)+' '+str(Obj[i].Ic)
                        print Obj[i].Name+' Power: '+str(Obj[i].kWa)+' '+str(Obj[i].kWb)+' '+str(Obj[i].kWc)
                        f.write(Obj[i].Name+' Volatges: '+str(Obj[i].Va)+' '+str(Obj[i].Vb)+' '+str(Obj[i].Vc)+'\n')
                        f.write(Obj[i].Name+' Currents: '+str(Obj[i].Ia)+' '+str(Obj[i].Ib)+' '+str(Obj[i].Ic)+'\n')
                        f.write(Obj[i].Name+' Power: '+str(Obj[i].kWa)+' '+str(Obj[i].kWb)+' '+str(Obj[i].kWc)+'\n')    
                        self.ACIData.append(Obj[i].Ia)
                        self.ACVData.append(Obj[i].Va)
                        self.ACPData.append(Obj[i].kWa)
                    if 'SP' in Obj[i].Name:
                        print Obj[i].Name+' Current='+str(Obj[i].I)+'A'
                        f.write(Obj[i].Name+' Current='+str(Obj[i].I)+'A\n')
                        if Obj[i].Name=='SP-1':
                            self.SPData.append(Obj[i].I)
                    if 'Therm'in Obj[i].Name:
                        print Obj[i].Name+' Ambient Temp: '+str(Obj[i].IN0)+' '+str(Obj[i].IN1)+' '+str(Obj[i].IN2)+' '+str(Obj[i].IN3)
                        print Obj[i].Name+' Panel Temp: '+str(Obj[i].IN4)+' '+str(Obj[i].IN5)+' '+str(Obj[i].IN6)+' '+str(Obj[i].IN7)
                        f.write(Obj[i].Name+' Ambient Temp: '+str(Obj[i].IN0)+' '+str(Obj[i].IN1)+' '+str(Obj[i].IN2)+' '+str(Obj[i].IN3)+'\n')
                        f.write(Obj[i].Name+' Panel Temp: '+str(Obj[i].IN4)+' '+str(Obj[i].IN5)+' '+str(Obj[i].IN6)+' '+str(Obj[i].IN7)+'\n')
                        self.ATData.append(Obj[i].IN0)
                        self.STData.append(Obj[i].IN4)
                print '#####################################################################'
                f.close()        
                Marker=False              
                self.Blank.append(np.nan)
                data=[[self.MIData,self.SPData],[self.DC1Data,self.DC2Data],[self.ACIData],[self.ACVData],[self.ACPData],[self.ATData,self.STData],[self.Blank]]
                self.signal.emit(data)
            if timestamp.second%5!=0: 
                Marker=True
            
        

if __name__ == "__main__":
    SerPort=serial.Serial(UARTPort,115200,timeout=.1)        
    Marker=True
    TimeMark=datetime.datetime.now()
    FileName='Solar_'+str(TimeMark.month)+'_'+str(TimeMark.day)+'.txt'
    f=open(FileName,'w+')
    f.write('Start Time: '+str(TimeMark.hour)+':'+str(TimeMark.minute)+':'+str(TimeMark.second)+'\n')
    f.close()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(lambda: ui.CallGuiUpdate())
    timer.start()
    MainWindow.show()
    sys.exit(app.exec_())

