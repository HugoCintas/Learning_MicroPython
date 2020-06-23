# main.py the main file of the project

# import
import pyb
from time import sleep


# create a variable called led on the pin number 1
# by default the pin is an input to create an output use : Pin.OUT
led_green = pyb.Pin('LED_GREEN', pyb.Pin.OUT)

# Three differents ways to control a pin

# ONE
led_green.on() # turn the pin on
led_green.off() # turn the pin off

# TWO
# led.value() zero is off and one is on and empty read the pin status
led_green.value() # -->

# shortcut
led_green(0) # turn the pin off
led_green(1) # turn the pin on


# programm
while True:
	led_green.on()
	sleep(1)
	led_green.off()
	sleep(1)