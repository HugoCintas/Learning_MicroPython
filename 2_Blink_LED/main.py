# main.py the main file of the project

# import
import pyb
from time import sleep


# create a variable called led_green on the pin number LED_GREEN
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


# to play
led_blue = pyb.Pin('LED_BLUE', pyb.Pin.OUT)

blue_counter = 0
blue_period = 500
green_counter = 0
green_period = 1000
counter = 0

# programm
while True:
	# led_green.on()
	# sleep(1)
	# led_green.off()
	# sleep(1)

	# check the status of the blue led
	if counter >= blue_counter:
		# check the value of the led
		if led_blue.value() == 0:
			led_blue.on()
		else:
			led_blue.off()
		blue_counter = counter + blue_period # fix new time to make change

	# check the status of the green led
	if counter >= green_counter:
		# check the value of the led
		if led_green.value() == 0:
			led_green.on()
		else:
			led_green.off()
		green_counter = counter + green_period # fix new time to make change

	sleep(0.001)
	counter += 1