# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:58:52 2019

@author: tabarez
"""
import serial
from serial.tools import list_ports
import pickle
import time

class RxTx_Object:
    def __init__(self,name):
        self.Name=name
        self.System=True #if False system is offline
        self.year=0
        self.month=0
        self.day=0
        self.hour=0
        self.minute=0
        self.second=0
        self.Freq1=float('NaN')
        self.Freq2=float('NaN')
        #Panel 1
        self.VDC1_R=float('NaN') #DC Voltage on roof
        self.IDC1_R=float('NaN') #DC Current on roof
        self.TA1=float('NaN')    #Temp under panel
        self.TP1=float('NaN')    #Temp of panel
        self.VDC1_L=float('NaN') #DC Voltage in lab
        self.IDC1_L=float('NaN') #DC Current in lab
        self.VAC1=float('NaN')   #AC Voltage in lab
        self.IAC1=float('NaN')   #AC Current in lab
        self.kW1=float('NaN')    
        self.kVar1=float('NaN')
        self.kVA1=float('NaN')
        self.PF1=float('NaN')
        #Panel 2
        self.VDC2_R=float('NaN') #DC Voltage on roof
        self.IDC2_R=float('NaN') #Dc Current on roof
        self.TA2=float('NaN')    #Temp under panel
        self.TP2=float('NaN')    #Temp of panel
        self.VDC2_L=float('NaN') #DC Voltage in lab
        self.IDC2_L=float('NaN') #DC Current in lab
        self.VAC2=float('NaN')   #AC Voltage in lab
        self.IAC2=float('NaN')   #AC Current in lab
        self.kW2=float('NaN')    
        self.kVar2=float('NaN')
        self.kVA2=float('NaN')
        self.PF2=float('NaN')
        #Panel 3
        self.VDC3_R=float('NaN') #DC Voltage on roof
        self.IDC3_R=float('NaN') #Dc Current on roof
        self.TA3=float('NaN')    #Temp under panel
        self.TP3=float('NaN')    #Temp of panel
        self.VDC3_L=float('NaN') #DC Voltage in lab
        self.IDC3_L=float('NaN') #DC Current in lab
        self.VAC3=float('NaN')   #AC Voltage in lab
        self.IAC3=float('NaN')   #AC Current in lab
        self.kW3=float('NaN')    
        self.kVar3=float('NaN')
        self.kVA3=float('NaN')
        self.PF3=float('NaN')
        #Panel 4
        self.VDC4_R=float('NaN') #DC Voltage on roof
        self.IDC4_R=float('NaN') #Dc Current on roof
        self.TA4=float('NaN')    #Temp under panel
        self.TP4=float('NaN')    #Temp of panel
        self.VDC4_L=float('NaN') #DC Voltage in lab
        self.IDC4_L=float('NaN') #DC Current in lab
        self.VAC4=float('NaN')   #AC Voltage in lab
        self.IAC4=float('NaN')   #AC Current in lab
        self.kW4=float('NaN')    
        self.kVar4=float('NaN')
        self.kVA4=float('NaN')
        self.PF4=float('NaN')
        
class Comm_Serial:
    def __init__(self):
        self.Error=False
        self.ErrorType='Init Data'
        self.COM=''
    def Setup_Serial(self):
        ports=list_ports.comports()
        for port in ports:
            if port.vid==1027 and port.pid==24597:
                 self.COM=port.device
    def Get_Data(self):
        attemp=0
        try:
            SerPort=serial.Serial(self.COM,115200,timeout=1)
            SerPort.flush()
            time.sleep(.1)
            SerPort.write("Send Data")
            while attemp<3:
                try:
                    msg=SerPort.read(10000) 
                    RxObj=pickle.loads(msg)
                    self.__dict__.update(RxObj.__dict__)
                    self.Error=False
                    self.ErrorType=''
                    attemp=10
                    SerPort.flushInput()
                    SerPort.close()
                except:
                    attemp+=1
                    #SerPort.write("Send Data")
                    self.Error=True
                    self.ErrorType='Failed to Receive Data'
        except:
            self.Error=True
            self.ErrorType="Failed to Connect"
        try:
            SerPort.flush()
            SerPort.close()
        except:
            pass
        

        
