# main.py the main file of the project

import pyb
from time import sleep

# create a variable called led on the pin number LED_GREEN
# by default the pin is an input to create an output use : Pin.OUT
led_green = pyb.Pin('LED_GREEN', pyb.Pin.OUT)

# create a variable called led on the pin number PA0
btn = pyb.Pin('PA0',pyb.Pin.IN)

led_green.on()

delay = 0.001
rebund_effect = 0.3
while True:

	if btn.value()==1:
		if led_green.value() == 1: # == led on
			led_green.off()
		else:
			led_green.on()
		sleep(rebund_effect) # protect again the rebund effect of the button
	sleep(delay)