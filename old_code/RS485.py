import serial
from serial.tools import list_ports
import time
import struct
import datetime
import numpy as np

##############################################################################
#################### CRC Generator Function by Javier. Hdez. A. ##############
##############################################################################

def CRCGen(cadena):
    mensaje = bytearray.fromhex(cadena)
    CRC = int('FFFF',16)
    POLY = int('A001',16)
    bit_mask = int('00000001', 2)

    for y in range(len(mensaje)):
        CRC = CRC ^ mensaje[y]
        for i in range(8):
            if (CRC & bit_mask)==1:
                CRC = CRC >> 1
                CRC = CRC ^ POLY
            else:
                CRC = CRC >> 1

    tipo = hex(CRC)  #string with the CRC
    if len(tipo)<6:
        if len(tipo)<5:
            Pad='00'
        else:
            Pad='0'
        tipo=tipo[0:2]+Pad+tipo[2:len(tipo)]
    tipo2 = tipo[4]+tipo[5]+tipo[2]+tipo[3] #concatenate the CRC string in the right order for transmission
    return(tipo2) # a webo que tiene que jalar =)

##############################################################################
##############################################################################
##############################################################################

def Find_Port():
    ports=list_ports.comports()
    RS485Port=False
    UARTPort=False
    for port in ports:
        if port.vid == 6790:
            RS485Port=port.device
        # if port.vid==1027 and port.pid==24597:
        #     UARTPort=port.device
    return [RS485Port,UARTPort]

def Set_Addr(addr,port,Address):
    try:
        sport=serial.Serial(port,38400,timeout=1)
        Function='06'
        Data=Address+Function+'0006'+'00'+addr
        CRC=CRCGen(Data)
        mensaje=bytearray.fromhex(Data+CRC)
        sport.write(mensaje)
        lectura=sport.read(32)
        Data=hex(int(lectura.encode('hex'),16))
        print(Data)
        sport.close()
        return True
    except:
        return False

def Test_Address(addr,port):
    try:
        sport=serial.Serial(port,38400,timeout=1)
        Function='03'
        Data=addr+Function+'0006'+'0001'
        CRC=CRCGen(Data)
        mensaje=bytearray.fromhex(Data+CRC)
        sport.write(mensaje)
        lectura=sport.read(32)
        Data=hex(int(lectura.encode('hex'),16))
        print(Data)
        sport.close()
        return True
    except:
        return False

def Enable_Inputs(addr,port):
    try:
        sport=serial.Serial(port,38400,timeout=1)
        Function='06'
        Data=addr+Function+'000B'+'00FF'
        CRC=CRCGen(Data)
        mensaje=bytearray.fromhex(Data+CRC)
        sport.write(mensaje)
        lectura=sport.read(32)
        Data=hex(int(lectura.encode('hex'),16))
        print(Data)
        sport.close()
        return True
    except:
        return False

def Test_Enable(addr,port):
    try:
        sport=serial.Serial(port,38400,timeout=1)
        Function='03'
        Data=addr+Function+'000B'+'0001'
        CRC=CRCGen(Data)
        mensaje=bytearray.fromhex(Data+CRC)
        sport.write(mensaje)
        lectura=sport.read(32)
        Data=hex(int(lectura.encode('hex'),16))
        print(Data)
        sport.close()
        return True
    except:
        return False

def Read_Meters(Obj):
    for i in range(len(Obj)):
        Obj[i].Read()
        #print('Object: '+Obj[i].Name+' Error: '+str(Obj[i].Error)+' Type: '+Obj[i].ErrorType)
    return Obj

##############################################################################
##############################################################################
##############################################################################

class Meter:
    def __init__(self,name,addr,port,local):
        self.Name=name
        self.Address=addr
        self.CommPort=port
        self.Location=local
        self.Error=True
        self.ErrorType="Init"
        self.year=0
        self.month=0
        self.day=0
        self.hour=0
        self.minute=0
        self.second=0

class ACMeter(Meter):
    def __init__(self,name,addr,port,local):
        Meter.__init__(self,name,addr,port,local)
        self.Va=float(np.nan)
        self.Vb=float(np.nan)
        self.Vc=float(np.nan)
        self.Ia=float(np.nan)
        self.Ib=float(np.nan)
        self.Ic=float(np.nan)
        self.kWa=float(np.nan)
        self.kWb=float(np.nan)
        self.kWc=float(np.nan)
        self.kVara=float(np.nan)
        self.kVarb=float(np.nan)
        self.kVarc=float(np.nan)
        self.kVAa=float(np.nan)
        self.kVAb=float(np.nan)
        self.kVAc=float(np.nan)
        self.PFa=float(np.nan)
        self.PFb=float(np.nan)
        self.PFc=float(np.nan)
        self.TPF=float(np.nan)
        self.TkW=float(np.nan)
        self.TkVar=float(np.nan)
        self.TkVA=float(np.nan)
        self.In=float(np.nan)
        self.Freq=float(np.nan) 
    def Read(self):
        self.Reset()
        self.Error=True
        try:
            sport=serial.Serial(self.CommPort,38400,timeout=.1)
            Function='03'
            Address=self.Address
            Reg=hex(256)
            Num=hex(24)
            Data=Address+Function+'0'+Reg[2:len(Reg)]+'00'+Num[2:len(Num)]
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            RecCRC=Data[len(Data)-5:len(Data)-1]
            RecData='0'+Data[2:len(Data)-5]
            CRC=CRCGen(RecData)
            if CRC==RecCRC:
                self.Error=False
                self.ErrorType=''
                timeMark=datetime.datetime.now()
                self.year=timeMark.hour
                self.month=timeMark.month
                self.day=timeMark.day
                self.hour=timeMark.hour
                self.minute=timeMark.minute
                self.second=timeMark.second
                self.Va=float(int(RecData[6:10],16))/9999*144
                self.Vb=float(int(RecData[10:14],16))/9999*144
                self.Vc=float(int(RecData[14:18],16))/9999*144
                self.Ia=float(int(RecData[18:22],16))/9999*2*5
                self.Ib=float(int(RecData[22:26],16))/9999*2*5
                self.Ic=float(int(RecData[26:30],16))/9999*2*5
                PMax=144*2*5*3
                self.kWa=float(int(RecData[30:34],16))/9999*(2*PMax)-PMax
                self.kWb=float(int(RecData[34:38],16))/9999*(2*PMax)-PMax
                self.kWc=float(int(RecData[38:42],16))/9999*(2*PMax)-PMax
                self.kVara=float(int(RecData[42:46],16))/9999*(2*PMax)-PMax
                self.kVarb=float(int(RecData[46:50],16))/9999*(2*PMax)-PMax
                self.kVarc=float(int(RecData[50:54],16))/9999*(2*PMax)-PMax
                self.kVAa=float(int(RecData[54:58],16))/9999*(2*PMax)-PMax
                self.kVAb=float(int(RecData[58:62],16))/9999*(2*PMax)-PMax
                self.kVAc=float(int(RecData[62:66],16))/9999*(2*PMax)-PMax
                self.PFa=float(int(RecData[66:70],16))/9999*(2)-1
                self.PFb=float(int(RecData[70:74],16))/9999*(2)-1
                self.PFc=float(int(RecData[74:78],16))/9999*(2)-1
                self.TPF=float(int(RecData[78:82],16))/9999*(2)-1
                self.TkW=float(int(RecData[82:86],16))/9999*(2*PMax)-PMax
                self.TkVar=float(int(RecData[86:90],16))/9999*(2*PMax)-PMax
                self.TkVA=float(int(RecData[90:94],16))/9999*(2*PMax)-PMax
                self.In=float(int(RecData[94:98],16))/9999*1.2*5
                self.Freq=float(int(RecData[98:102],16))/9999*(65-45)+45
            else:
                self.Error=True
                self.ErrorType='CRC Error'
        except:
            self.Error=True
            self.ErrorType='Connection Error'
    def Reset(self):
        self.Va=float(np.nan)
        self.Vb=float(np.nan)
        self.Vc=float(np.nan)
        self.Ia=float(np.nan)
        self.Ib=float(np.nan)
        self.Ic=float(np.nan)
        self.kWa=float(np.nan)
        self.kWb=float(np.nan)
        self.kWc=float(np.nan)
        self.kVara=float(np.nan)
        self.kVarb=float(np.nan)
        self.kVarc=float(np.nan)
        self.kVAa=float(np.nan)
        self.kVAb=float(np.nan)
        self.kVAc=float(np.nan)
        self.PFa=float(np.nan)
        self.PFb=float(np.nan)
        self.PFc=float(np.nan)
        self.TPF=float(np.nan)
        self.TkW=float(np.nan)
        self.TkVar=float(np.nan)
        self.TkVA=float(np.nan)
        self.In=float(np.nan)
        self.Freq=float(np.nan) 
class DCCurrent(Meter):
    def __init__(self,name,addr,port,local):
        Meter.__init__(self,name,addr,port,local)
        self.I=float(np.nan)
    def Read(self):
        self.Reset()
        self.Error=True
        try:
            sport=serial.Serial(self.CommPort,38400,timeout=.1)
            Address=self.Address
            Data=Address+'03'+'00240002'
            #Data=Address+'03'+'002F0001'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            RecCRC=Data[len(Data)-5:len(Data)-1]
            RecData='0'+Data[2:len(Data)-5]
            CRC=CRCGen(RecData)
            if CRC==RecCRC:
                self.Error=False
                self.ErrorType=''
                timeMark=datetime.datetime.now()
                self.year=timeMark.hour
                self.month=timeMark.month
                self.day=timeMark.day
                self.hour=timeMark.hour
                self.minute=timeMark.minute
                self.second=timeMark.second
                Val=RecData[10:14]+RecData[6:10]
                self.I=struct.unpack('!f',Val.decode('hex'))[0]
            else:
                self.Error=True
                self.ErrorType='CRC Error'
                sport.close()
        except:
            self.Error=True
            self.ErrorType='Connection Error'
    def Reset(self):
        self.I=float(np.nan)

class DCVoltage(Meter):
    def __init__(self,name,addr,port,local):
        Meter.__init__(self,name,addr,port,local)
        self.V1=float(np.nan)
        self.V2=float(np.nan)
        self.V3=float(np.nan)
        self.V4=float(np.nan)
    def Read(self):
        self.Reset()
        self.Error=True
        try:
            sport=serial.Serial(self.CommPort,38400,timeout=.1)
            Address=self.Address
            Function='03'
            Data=Address+Function+'000E0004'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            RecCRC=Data[len(Data)-5:len(Data)-1]
            RecData='0'+Data[2:len(Data)-5]
            CRC=CRCGen(RecData)
            if CRC==RecCRC:
                self.Error=False
                self.ErrorType=''
                timeMark=datetime.datetime.now()
                self.year=timeMark.hour
                self.month=timeMark.month
                self.day=timeMark.day
                self.hour=timeMark.hour
                self.minute=timeMark.minute
                self.second=timeMark.second
                Val=RecData[6:10]
                self.V1=float(self.twos_complement(Val))/1000
                Val=RecData[10:14]
                self.V2=float(self.twos_complement(Val))/1000
                Val=RecData[14:18]
                self.V3=float(self.twos_complement(Val))/1000
                Val=RecData[18:22]
                self.V4=float(self.twos_complement(Val))/1000
            else:
                self.Error=True
                self.ErrorType='CRC Error'
            sport.close()
        except:
            self.Error=True
            self.ErrorType='Connection Error'
    def Reset(self):
        self.V1=float(np.nan)
        self.V2=float(np.nan)
        self.V3=float(np.nan)
        self.V4=float(np.nan)
    def twos_complement(self,hexstr):
        value=int(hexstr,16)
        if value&(1 << (15)):
            value-=1<<16
        return value

class Therm(Meter):
    def __init__(self,name,addr,port,local):
        Meter.__init__(self,name,addr,port,local)
        self.IN0=float(np.nan)
        self.IN1=float(np.nan)
        self.IN2=float(np.nan)
        self.IN3=float(np.nan)
        self.IN4=float(np.nan)
        self.IN5=float(np.nan)
        self.IN6=float(np.nan)
        self.IN7=float(np.nan)
        sport=serial.Serial(self.CommPort,38400,timeout=.1)
        Address=self.Address
        Function='06'
        try:
            Data=Address+Function+'000AAAAA'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            Data=Address+Function+'000BAAAA'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            Function='03'
            Data=Address+Function+'000A0002'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
        except:
            self.Error=True
            self.ErrorType='Connection Error'
    def Read(self):
        self.Reset()
        self.Error=True
        try:
            sport=serial.Serial(self.CommPort,38400,timeout=.1)
            sport.flush()
            Address=self.Address
            Function='03'
            Data=Address+Function+'000E0008'
            CRC=CRCGen(Data)
            mensaje=bytearray.fromhex(Data+CRC)
            sport.write(mensaje)
            lectura=sport.read(120)
            Data=hex(int(lectura.encode('hex'),16))
            RecCRC=Data[len(Data)-5:len(Data)-1]
            RecData='0'+Data[2:len(Data)-5]
            CRC=CRCGen(RecData)
            if CRC==RecCRC:
                self.Error=False
                self.ErrorType=''
                timeMark=datetime.datetime.now()
                self.year=timeMark.hour
                self.month=timeMark.month
                self.day=timeMark.day
                self.hour=timeMark.hour
                self.minute=timeMark.minute
                self.second=timeMark.second
                Val=RecData[6:10]
                self.IN0=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[10:14]
                self.IN1=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[14:18]
                self.IN2=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[18:22]
                self.IN3=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[22:26]
                self.IN4=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[26:30]
                self.IN5=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[30:34]
                self.IN6=float(self.twos_complement(Val))/9.475-1.7414
                Val=RecData[34:38]
                self.IN7=float(self.twos_complement(Val))/9.475-1.7414
            else:
                self.Error=True
                self.ErrorType='CRC Error'
            sport.close()
        except:
            self.Error=True
            self.ErrorType='Connection Error'
    def Reset(self):
        self.IN0=float(np.nan)
        self.IN1=float(np.nan)
        self.IN2=float(np.nan)
        self.IN3=float(np.nan)
        self.IN4=float(np.nan)
        self.IN5=float(np.nan)
        self.IN6=float(np.nan)
        self.IN7=float(np.nan)
    def twos_complement(self,hexstr):
        value=int(hexstr,16)
        if value&(1 << (15)):
            value-=1<<16
        return value