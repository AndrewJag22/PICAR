import RPi.GPIO as gpio
import time

trigg = 12
echo = 18

startt = time.time()
stopt = time.time()

gpio.setmode(gpio.BOARD)

def setup():
        gpio.setup(trigg, gpio.OUT)
        gpio.setup(echo, gpio.IN)

def distance():
	gpio.output(trigg, True)
	time.sleep(0.00001)
	gpio.output(trigg,False)

	while gpio.input(echo) == 0:
		startt = time.time()

	while gpio.input(echo) == 1:
		stopt = time.time()

	timetaken = stopt - startt
	distance = (timetaken * 34300) / 2
	return distance
