# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:43:16 2019

@author: tabar
"""
import datetime
from Serial_RX import *
NMSU=Comm_Serial()
NMSU.__init__()
NMSU.Setup_Serial()
print NMSU


#Call for data 
it=0
Mraker=True
while it<300:
    timestamp=datetime.datetime.now()
    if timestamp.second%5==0 and Marker==True:
        it+=1
        try:
            NMSU.Get_Data()
            if NMSU.Error:
                print NMSU.ErrorType
            else:
                print 'Recieved at '+str(NMSU.minute)+':'+str(NMSU.second)
        except:
            print('Call Failed')
        Marker=False
    elif timestamp.second%5!=0:
        Marker=True

