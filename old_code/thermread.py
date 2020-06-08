import socket
from RS485 import *
from DeviceAddress import *
from Serial_TX import *

CommPort = Find_Port()
A=Therm('Therm-1','0E',CommPort[0],'Roof')
A.Read()
print(A.IN0)
print(A.IN1)
print(A.IN2)
print(A.IN3)
print(A.IN4)
print(A.IN5)
print(A.IN6)
print(A.IN7)