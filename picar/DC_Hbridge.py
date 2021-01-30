import sys
import time
import pigpio

pi = pigpio.pi()

def setup():
    pi.set_mode(23, pigpio.OUTPUT)
    pi.set_mode(24, pigpio.OUTPUT)

def stepsFor():
    pi.set_PWM_dutycycle(23,255)
    time.sleep(1)
    pi.write(23,0)

def stepsBack():
    pi.set_PWM_dutycycle(24,255)
    time.sleep(1)
    pi.write(24,0)

def stop():
    pi.stop()
