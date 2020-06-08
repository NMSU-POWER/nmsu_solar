import datetime 
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
    def Update(self,Objects):
        timeMark=datetime.datetime.now()
        self.year=timeMark.hour
        self.month=timeMark.month
        self.day=timeMark.day
        self.hour=timeMark.hour
        self.minute=timeMark.minute
        self.second=timeMark.second
        for i in range(len(Objects)):
            if Objects[i].Name=='SP-1':
                self.IDC1_R=Objects[i].I
            elif Objects[i].Name=='SP-2':
                self.IDC2_R=Objects[i].I
            elif Objects[i].Name=='SP-3':
                self.IDC3_R=Objects[i].I
            elif Objects[i].Name=='SP-4':
                self.IDC4_R=Objects[i].I 
            elif Objects[i].Name=='MI-1':
                self.IDC1_L=Objects[i].I
            elif Objects[i].Name=='MI-2':
                self.IDC2_L=Objects[i].I
            elif Objects[i].Name=='MI-3':
                self.IDC3_L=Objects[i].I
            elif Objects[i].Name=='MI-4':
                self.IDC4_L=Objects[i].I    
            elif Objects[i].Name=='DCMeter-1':
                self.VDC1_R=Objects[i].V1
                self.VDC2_R=Objects[i].V2
                self.VDC3_R=Objects[i].V3
                self.VDC4_R=Objects[i].V4
            elif Objects[i].Name=='DCMeter-2':
                self.VDC1_L=Objects[i].V1
                self.VDC2_L=Objects[i].V2
                self.VDC3_L=Objects[i].V3
                self.VDC4_L=Objects[i].V4
            elif Objects[i].Name=='ACMeter-1':
                self.VAC1=Objects[i].Va
                self.IAC1=Objects[i].Ia
                self.kW1=Objects[i].kWa   
                self.kVar1=Objects[i].kVara
                self.kVA1=Objects[i].kVAa
                self.PF1=Objects[i].PFa
                self.VAC2=Objects[i].Vb
                self.IAC2=Objects[i].Ib
                self.kW2=Objects[i].kWb   
                self.kVar2=Objects[i].kVarb
                self.kVA2=Objects[i].kVAb
                self.PF2=Objects[i].PFb
                self.VAC3=Objects[i].Vc
                self.IAC3=Objects[i].Ic
                self.kW3=Objects[i].kWc  
                self.kVar3=Objects[i].kVarc
                self.kVA3=Objects[i].kVAc
                self.PF3=Objects[i].PFc
                self.Freq1=Objects[i].Freq
            elif Objects[i].Name=='ACMeter-2':
                self.VAC4=Objects[i].Va
                self.IAC4=Objects[i].Ia
                self.kW4=Objects[i].kWa   
                self.kVar4=Objects[i].kVara
                self.kVA4=Objects[i].kVAa
                self.PF4=Objects[i].PFa
                self.Freq2=Objects[i].Freq    
