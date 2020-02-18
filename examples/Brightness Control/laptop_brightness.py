from arbd import Arbd1
import wmi as wmi # pywin32 package is also required
import time
board=Arbd1('COM3')
board.ldr_delay=1
time.sleep(5)
while 1:

    x=100-board.ldr()*100
    print(x)
    if(x<20):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(10, 0)
    if (20 < x < 50):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(30, 0)
    if (50 <x< 65) :
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(50, 0)
    if (65 <x  < 80):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(70, 0)
    if (80 < x < 100):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(90, 0)

