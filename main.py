import time
import matplotlib.pyplot as plot
from drawnow import *
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

val = [ ]
cnt = 0

plot.ion()

adc.start_adc(0, gain=GAIN)
def makePlt():
    plot.ylim(-5000,5000)
    plot.title('Osciloscope')
    plot.grid(True)
    plot.ylabel('ADC outputs')
    plot.plot(val, 'ro-', label='lux')
    plot.legend(loc='lower right')
    
while (0):
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    time.sleep(0.5)
    val.append(int(value))

    drawnow(makePlt)

    cnt = cnt+1
    if(cnt>50):
        val.pop(0)


