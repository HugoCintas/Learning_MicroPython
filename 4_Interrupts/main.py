# main.py the main file of the project

import pyb
from time import sleep



## Pins

# create a variable called led_green on the pin number LED_GREEN
# by default the pin is an input to create an output use : Pin.OUT
led_green = pyb.Pin('LED_GREEN', pyb.Pin.OUT)
# create a variable called led_red on the pin number LED_GREEN
led_red = pyb.Pin('LED_RED', pyb.Pin.OUT)

# create a variable called btn on the pin number PA0
btn = pyb.Pin('PA0',pyb.Pin.IN)


## constants
delay = 0.001
rebund_effect = 0.3
red_period = 0.500



## functions

def Change_State(pin):
	if led_green.value() == 1: # active high -> pressed
		led_green.off()
	else:
		led_green.on()
	sleep(rebund_effect)




## Interrupt

# Interrupt Request Query : irq
btn.irq(Change_State) #, Pin.IRQ_RISING) # rising edge not working


while True:
	led_red.on()
	sleep(red_period)
	led_red.off()
	sleep(red_period)