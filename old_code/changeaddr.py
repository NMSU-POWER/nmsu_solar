import socket
from RS485 import *
from DeviceAddress import *
from Serial_TX import *

CommPort = Find_Port()
print(CommPort)
A=DCVoltage('DCMeter-1','0A',CommPort[0],'Lab')
A.Read()
print(A.V4)

B=DCCurrent('MI-4','05',CommPort[0],'Lab')
B.Read()
print(B.I)
B=DCCurrent('MI-3','07',CommPort[0],'Lab')
B.Read()
print(B.I)
B=DCCurrent('MI-41','08',CommPort[0],'Lab')
B.Read()
print(B.I)
B=DCCurrent('MI-46','09',CommPort[0],'Lab')
B.Read()
print(B.I)
##
##A=Set_Addr('0A',CommPort[0],'01')
##print(A)
##B=Test_Address('08',CommPort)
##print(B)