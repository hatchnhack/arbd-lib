import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from arbd import Arbd1
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Control volume
# volume.SetMasterVolumeLevel(-0.0, None) #max
#volume.SetMasterVolumeLevel(-50, None) #72%
board=Arbd1('COM3')
time.sleep(5)
while 1:
    k=board.potentiometer()
    j=(k*100)/2 -50
    volume.SetMasterVolumeLevel(j, None)  # 51%