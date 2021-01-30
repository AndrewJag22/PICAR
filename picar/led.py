import time
import sys
import RPi.GPIO as gpio

gpio.setwarnings(False)

led1 = 37
led2 = 35
led3 = 33
led4 = 31
led5 = 29

def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(37, gpio.OUT)
    gpio.setup(35, gpio.OUT)
    gpio.setup(33, gpio.OUT)
    gpio.setup(31, gpio.OUT)
    gpio.setup(29, gpio.OUT)

def ledOn(pin):
    gpio.output(37, gpio.LOW)
    gpio.output(35, gpio.LOW)
    gpio.output(33, gpio.LOW)
    gpio.output(31, gpio.LOW)
    gpio.output(29, gpio.LOW)
    gpio.output(pin, gpio.HIGH)
    
gpio.cleanup()
