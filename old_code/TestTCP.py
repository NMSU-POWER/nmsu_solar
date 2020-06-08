from TCP import *
import threading

count = 0
def Run():
    f = open("/Users/joshuatellez/Desktop/Test"+str(count)+".txt", "w+")
    
    global count
    count += 1

    a=TBMeter('','')
    a.Read()
    
    f.write(str(a.month)+'/'+str(a.day)+'/'+str(a.year)+', '+str(a.hour)+':'+str(a.minute)+':'+str(a.second))
    f.write("\n\n")
    f.write("- VOLTAGE DATA -")
    f.write("\n")
    f.write('Voltage A-B: '+str(a.Vab)+' V')
    f.write("\n")
    f.write('Phase A-B: '+str(a.phVab)+' deg')
    f.write("\n")
    f.write('Voltage A-N: '+str(a.Van)+' V')
    f.write("\n")
    f.write('Voltage B-C: '+str(a.Vbc)+' V')
    f.write("\n")
    f.write('Phase B-C: '+str(a.phVbc)+' deg')
    f.write("\n")
    f.write('Voltage B-N: '+str(a.Vbn)+' V')
    f.write("\n")
    f.write('Voltage C-A: '+str(a.Vca)+' V')
    f.write("\n")
    f.write('Phase C-A: '+str(a.phVca)+' deg')
    f.write("\n")
    f.write('Voltage C-N: '+str(a.Vcn)+' V')
    f.write("\n\n")
    f.write("- CURRENT DATA -")
    f.write("\n")
    f.write('Current A: '+str(a.Ia)+' A')
    f.write("\n")
    f.write('Phase Ia: ' +str(a.phIa)+' deg')
    f.write("\n")
    f.write('Current B: '+str(a.Ib)+' A')
    f.write("\n")
    f.write('Phase Ib: ' +str(a.phIb)+' deg')
    f.write("\n")
    f.write('Current C: '+str(a.Ic)+' A')
    f.write("\n")
    f.write('Phase Ic: ' +str(a.phIc)+' deg')
    f.write("\n")
    f.write('Current N: '+str(a.In)+' A')
    f.write("\n\n")
    f.write("- POWER DATA -")
    f.write("\n")
    f.write('Wattage Phase A: '+str(a.WphA)+' W')
    f.write("\n")
    f.write('Wattage Phase B: '+str(a.WphB)+' W')
    f.write("\n")
    f.write('Wattage Phase C: '+str(a.WphC)+' W')
    f.write("\n")
    f.write('VARs Phase A: '+str(a.VARphA)+' VAR')
    f.write("\n")
    f.write('VARs Phase B: '+str(a.VARphB)+' VAR')
    f.write("\n")
    f.write('VARs Phase C: '+str(a.VARphC)+' VAR')
    f.write("\n\n")
    f.write("- PERFORMANCE DATA -")
    f.write("\n")
    f.write('Phase A THD V:'+str(a.VanTHD)+'% \tI:'+str(a.IaTHD)+'%')
    f.write("\n")
    f.write('Phase B THD V:'+str(a.VbnTHD)+'% \tI:'+str(a.IbTHD)+'%')
    f.write("\n")
    f.write('Phase C THD V:'+str(a.VcnTHD)+'% \tI:'+str(a.IcTHD)+'%')
    f.write("\n")
    f.close()

    if count < 5:
        timer=threading.Timer(1.0,Run)
        timer.start()

timer=threading.Timer(1.0,Run)
timer.start()