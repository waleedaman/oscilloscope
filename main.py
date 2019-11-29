import time
import matplotlib.pyplot as plt
from drawnow import *
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

Val = [ ]
cnt = 0

plt.ion()

adc.start_adc(0, gain=GAIN)

 plt.ylim(-5000,5000)
 plt.title('Osciloscope')
 plt.grid(True)
 plt.ylabel('ADC outputs')
 plt.plot(val, 'ro-', label='lux')
 plt.legend(loc='lower right')

 value = adc.get_last_result()

print('Channel 0: {0}'.format(value))
time.sleep(0.5)
val.append(int(value))

drawnow(makeFig)

cnt = cnt+1
if(cnt>50):
val.pop(0)


