import socket 
from RS485 import *
from DeviceAddress import *
from Serial_TX import *
from threading import Lock, Thread
from Queue import Queue
import datetime
import pickle
import time
import serial

lock=Lock()
threadQueue=Queue()
[RS485Port,UARTPort]=Find_Port()
print UARTPort
print RS485Port
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
MasterStop=False
#something
def Measurements(threadQueue):
    global Obj
    global SerialObj
    global MasterStop
    it=0
    Marker=True
    while it<100:
        timestamp=datetime.datetime.now()
        if timestamp.second%5==0 and Marker==True:
            lock.acquire(1)
            Obj=Read_Meters(Obj)
            SerialObj.Update(Obj)
            lock.release()
            print("Done With Measurement@:"+str(timestamp.second))
            it+=1
            Marker=False
        if timestamp.second%5!=0: 
            Marker=True
    MasterStop=True
def SerialCheck(threadQueue):
    try:
        SerPort=serial.Serial(UARTPort,115200,timeout=.1)
        SerPort.flush()
        while not MasterStop:
            try:
                bytes_rec=SerPort.read(16)
                if 'Send Data' in bytes_rec:
                    lock.acquire(1)
                    print 'Lock'
                    timestamp = datetime.datetime.now()
                    print 'Request Recieved @:'#+timestamp
                    print('sending data...')
                    bytes_xmt=pickle.dumps(SerialObj)
                    SerPort.write(bytes_xmt)
                    print 'unlock'
                    SerPort.flush()
                    lock.release()
                    SerPort.close()
                    time.sleep(.1)
                    SerPort=serial.Serial(UARTPort,115200,timeout=.1)
            except:
                SerPort.close()
                time.sleep(.1)
                SerPort=serial.Serial(UARTPort,115200,timeout=.1)
        SerPort.close()
    except:
        print('serial connection error')
    
def UpdateGUI(threadQueue):
    while MasterStop:
        lock.acquire()
        Copy_Obj=Obj
        lock.release()
##        for Copy_Obj in Obj:
##            print Copy_Obj.Name
SerPort=serial.Serial(UARTPort,115200,timeout=.1)        
Marker=True
TimeMark=datetime.datetime.now()
FileName='Solar_'+str(TimeMark.month)+'_'+str(TimeMark.day)+'.txt'
f=open(FileName,'w+')
f.write('Start Time: '+str(TimeMark.hour)+':'+str(TimeMark.minute)+':'+str(TimeMark.second)+'\n')
f.close()
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
            if 'DCMeter' in Obj[i].Name:
                print Obj[i].Name+' Voltages: '+str(Obj[i].V1*6)+' '+str(Obj[i].V2*6)+' '+str(Obj[i].V3*6)+' '+str(Obj[i].V4*6)
                f.write(Obj[i].Name+' Voltages: '+str(Obj[i].V1)+' '+str(Obj[i].V2)+' '+str(Obj[i].V3)+' '+str(Obj[i].V4)+'\n')
            if 'ACMeter-1' in Obj[i].Name:
                print Obj[i].Name+' Volatges: '+str(Obj[i].Va)+' '+str(Obj[i].Vb)+' '+str(Obj[i].Vc)
                print Obj[i].Name+' Currents: '+str(Obj[i].Ia)+' '+str(Obj[i].Ib)+' '+str(Obj[i].Ic)
                print Obj[i].Name+' Power: '+str(Obj[i].kWa)+' '+str(Obj[i].kWb)+' '+str(Obj[i].kWc)
                f.write(Obj[i].Name+' Volatges: '+str(Obj[i].Va)+' '+str(Obj[i].Vb)+' '+str(Obj[i].Vc)+'\n')
                f.write(Obj[i].Name+' Currents: '+str(Obj[i].Ia)+' '+str(Obj[i].Ib)+' '+str(Obj[i].Ic)+'\n')
                f.write(Obj[i].Name+' Power: '+str(Obj[i].kWa)+' '+str(Obj[i].kWb)+' '+str(Obj[i].kWc)+'\n')    
            if 'SP' in Obj[i].Name:
                print Obj[i].Name+' Current='+str(Obj[i].I)+'A'
                f.write(Obj[i].Name+' Current='+str(Obj[i].I)+'A\n')
            if 'Therm'in Obj[i].Name:
                print Obj[i].Name+' Ambient Temp: '+str(Obj[i].IN0)+' '+str(Obj[i].IN1)+' '+str(Obj[i].IN2)+' '+str(Obj[i].IN3)
                print Obj[i].Name+' Panel Temp: '+str(Obj[i].IN4)+' '+str(Obj[i].IN5)+' '+str(Obj[i].IN6)+' '+str(Obj[i].IN7)
                f.write(Obj[i].Name+' Ambient Temp: '+str(Obj[i].IN0)+' '+str(Obj[i].IN1)+' '+str(Obj[i].IN2)+' '+str(Obj[i].IN3)+'\n')
                f.write(Obj[i].Name+' Panel Temp: '+str(Obj[i].IN4)+' '+str(Obj[i].IN5)+' '+str(Obj[i].IN6)+' '+str(Obj[i].IN7)+'\n')
        print '#####################################################################'
        f.close()        
        Marker=False
    if timestamp.second%5!=0: 
        Marker=True
    try:
        bytes_rec=SerPort.read(16)
        if 'Send Data' in bytes_rec:
            bytes_xmt=pickle.dumps(SerialObj)
            SerPort.write(bytes_xmt)
        SerPort.flush()
    except:
        pass
SerPort.close()
SerPort=serial.Serial(UARTPort,115200,timeout=.1)
            
    
##threads=[]
##try:
##    t=Thread(target=Measurements,args=(threadQueue,))
##    t.setDaemon(True)
##    threads.append(t)
##    t.start()
##    t=Thread(target=UpdateGUI,args=(threadQueue,))
##    t.setDaemon(True)
##    threads.append(t)
##    t.start()
##    t=Thread(target=SerialCheck,args=(threadQueue,))
##    t.setDaemon(True)
##    threads.append(t)
##    t.start()
##except:
##    print 'Error: unable to start thread'
##for n in threads:
##     n.join()
##while not threadQueue.empty():
##    holdData=threadQueue.get()
##    print holdData

################################Test####################################################
# A=DCVoltage('DCMeter-1','0A',CommPort,'Roof')
# A.Read()
# A=ACMeter('ACMeter-1','0C',CommPort,'Lab')
# A.Read(Obj)

# Use to Set Address OLNY!!!! Password 0201
# a=Set_Addr('0A',CommPort)
# print(a)
# b=Test_Address('0A',CommPort)
# print(b)
# Use to Enable Inputs OLNY!!!! Password 0201
# a=Enable_Inputs('0A',CommPort)
# print(a)
# b=Test_Enable('0A',CommPort)
# print(b)

