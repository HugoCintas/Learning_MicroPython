# main.py the main file of the project

from time import sleep
import pyb


## Pins
# create a variable called led_green on the pin number LED_GREEN
# by default the pin is an input to create an output use : Pin.OUT
led_green = pyb.Pin('LED_GREEN', pyb.Pin.OUT)
led_blue = machine.Pin('PD15') # another way to create a pin

# create a timer using timer 4 with a freq of 1000 Hz
timer = pyb.Timer(4, freq=1000)
# t4_ch1 is the timer 4 channel 1 using as a pwm on the pin of the green led with a duty cycle initial of 50 % and because the timer 4 channel 1 is on the pin led_green
t4_ch1 = timer.channel(1, mode = pyb.Timer.PWM, pin=led_green, pulse_width_percent=50)


## Functions
def set_duty_cycle(timer_channel, duty_cycle):
	timer_channel.pulse_width_percent(duty_cycle)

def toggle_led(led):
	if led.value() == 1:
		led.off() # led.value(0) # OFF
	else:
		led.on() # led.value(1) # ON


## Variable
positive = 1
value_light = 50
blue_timer = 0


## Init & Test of the system before the Loop
led_blue.on()
sleep(1)
led_blue.off()
sleep(1)


## Infinite Loop
while True:

	# the positive direction the incrementation of the duty_cycle 
	if positive == 1:
		value_light += 1
		if value_light >= 100:
			positive = 0
	# NOT the positive direction (negative direction) the decrementation of the duty_cycle 
	else:
		value_light -= 1
		if value_light <= 0:
			positive = 1
	# set the value of the duty cycle
	set_duty_cycle(t4_ch1,value_light)

	# toggle the blue led every 10 loop
	if blue_timer < 10:
		blue_timer += 1
	else:
		blue_timer = 0
		toggle_led(led_blue)

	sleep(0.05) # ~the period of the loop