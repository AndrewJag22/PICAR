import sys
import time
import RPi.GPIO as gpio

stepFor = 16
stepBack = 18
def stepup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(stepFor, gpio.OUT)
    gpio.setup(stepBack, gpio.OUT)

def stepsFor():
    gpio.output(stepFor, gpio.HIGH)
    time.sleep(1)
    gpio.output(stepFor, gpio.LOW)

def stepsBack():
    gpio.output(stepBack, gpio.HIGH)
    time.sleep(1)
    gpio.output(stepBack, gpio.LOW)

gpio.cleanup()
