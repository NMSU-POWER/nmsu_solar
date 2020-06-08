from pyModbusTCP.client import ModbusClient
from serial.tools import list_ports
from ctypes import *
import datetime
import struct
import serial
import time

#Register addresses for power meter readings
vabaddr     = 4002
vbcaddr     = 4004
vcaaddr     = 4006
vanaddr     = 4010
vbnaddr     = 4012
vcnaddr     = 4014
phvabaddr   = 4497
phvbcaddr   = 4499
phvcaaddr   = 4501
iaaddr      = 5002
ibaddr      = 5004
icaddr      = 5006
inaddr      = 5010
phiaaddr    = 5338
phibaddr    = 5340
phicaddr    = 5342
wphaaddr    = 6000
wphbaddr    = 6002
wphcaddr    = 6004
varaaddr    = 6128
varbaddr    = 6130
varcaddr    = 6132
vanthdaddr  = 8154
vbnthdaddr  = 8156
vcnthdaddr  = 8158
iathdaddr   = 9436
ibthdaddr   = 9438
icthdaddr   = 9440

ip = "10.123.130.208"
port = 502

#Function pulls in a register address and returns a converted
#integer-to-float value stored in referenced address
def convert(c,s):
    regs = c.read_holding_registers(s, 2)
    Val= (regs[0]<<16)+(regs[1])
    Val = hex(Val)
    if 'L' in Val:
        Val=Val[0:len(Val)-1]
    Val=Val[2:len(Val)]
    floatVal=struct.unpack('!f',Val.decode('hex'))[0]
    return floatVal 

#Initializes and defines meter parameters
class Meter:
    def __init__(self,name,local):
        self.Name=name
        self.Address="10.123.130.208"
        self.CommPort=502
        self.Location=local
        self.Error=True
        self.ErrorType="Init"
        self.year=0
        self.month=0
        self.day=0
        self.hour=0
        self.minute=0
        self.second=0

#Continues initialization and defines meter values
class TBMeter(Meter):
    def __init__(self,name,local):
        Meter.__init__(self,name,local)
        self.Vab=   float('NaN')
        self.Vbc=   float('NaN')
        self.Vca=   float('NaN')
        self.Van=   float('NaN')
        self.Vbn=   float('NaN')
        self.Vcn=   float('NaN')
        self.phVab= float('NaN')
        self.phVbc= float('NaN')
        self.phVca= float('NaN')
        self.Ia=    float('NaN')
        self.Ib=    float('NaN')
        self.Ic=    float('NaN')
        self.In=    float('NaN')
        self.phIa=  float('NaN')
        self.phIb=  float('NaN')
        self.phIc=  float('NaN')
        self.WphA=  float('NaN')
        self.WphB=  float('NaN')
        self.WphC=  float('NaN')
        self.VARphA=float('NaN')
        self.VARphB=float('NaN')
        self.VARphC=float('NaN')
        self.VanTHD=float('NaN')
        self.VbnTHD=float('NaN')
        self.VcnTHD=float('NaN')
        self.IaTHD= float('NaN')
        self.IbTHD= float('NaN')
        self.IcTHD= float('NaN')
    
    def Read(self):
        self.Reset()
        self.Error=True
        try:
            # Initializing connection to Eaton power meter via TCP
            c = ModbusClient()
            c.host(ip)
            c.port(port)
            c.open()
            #All time-stamp values
            timeMark=datetime.datetime.now()
            self.Error=False
            self.ErrorType=''
            self.year=timeMark.year
            self.month=timeMark.month
            self.day=timeMark.day
            self.hour=timeMark.hour
            self.minute=timeMark.minute
            self.second=timeMark.second
            #All meter values
            self.Vab=   convert(c, vabaddr)
            self.Vbc=   convert(c, vbcaddr)
            self.Vca=   convert(c, vcaaddr)
            self.Van=   convert(c, vanaddr)
            self.Vbn=   convert(c, vbnaddr)
            self.Vcn=   convert(c, vcnaddr)
            self.phVab= convert(c, phvabaddr)
            self.phVbc= convert(c, phvbcaddr)
            self.phVca= convert(c, phvcaaddr)
            self.Ia=    convert(c, iaaddr)
            self.Ib=    convert(c, ibaddr)
            self.Ic=    convert(c, icaddr)
            self.In=    convert(c, inaddr)
            self.phIa=  convert(c, phiaaddr)
            self.phIb=  convert(c, phibaddr)
            self.phIc=  convert(c, phicaddr)
            self.WphA=  convert(c, wphaaddr)
            self.WphB=  convert(c, wphbaddr)
            self.WphC=  convert(c, wphcaddr)
            self.VARphA=convert(c, varaaddr)
            self.VARphB=convert(c, varbaddr)
            self.VARphC=convert(c, varcaddr)
            self.VanTHD=convert(c, vanaddr)
            self.VbnTHD=convert(c, vbnaddr)
            self.VcnTHD=convert(c, vcnaddr)
            self.IaTHD= convert(c, iathdaddr)
            self.IbTHD= convert(c, ibthdaddr)
            self.IcTHD= convert(c, icthdaddr)
            c.close()
        except:
            try:
                c.close()
            except:
                pass
            self.Error=True
            self.ErrorType='Connection Error'
    
    def Reset(self):
        self.Vab=   float('NaN')
        self.Vbc=   float('NaN')
        self.Vca=   float('NaN')
        self.Van=   float('NaN')
        self.Vbn=   float('NaN')
        self.Vcn=   float('NaN')
        self.phVab= float('NaN')
        self.phVbc= float('NaN')
        self.phVca= float('NaN')
        self.Ia=    float('NaN')
        self.Ib=    float('NaN')
        self.Ic=    float('NaN')
        self.In=    float('NaN')
        self.phIa=  float('NaN')
        self.phIb=  float('NaN')
        self.phIc=  float('NaN')
        self.WphA=  float('NaN')
        self.WphB=  float('NaN')
        self.WphC=  float('NaN')
        self.VARphA=float('NaN')
        self.VARphB=float('NaN')
        self.VARphC=float('NaN')
        self.VanTHD=float('NaN')
        self.VbnTHD=float('NaN')
        self.VcnTHD=float('NaN')
        self.IaTHD= float('NaN')
        self.IbTHD= float('NaN')
        self.IcTHD= float('NaN')