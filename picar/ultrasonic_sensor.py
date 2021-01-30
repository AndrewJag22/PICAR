import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
trigg = 8

gpio.setmode(gpio.BOARD)

def setup():
        gpio.setup(trigg, gpio.OUT)
        gpio.setup(10, gpio.IN)
        gpio.setup(12, gpio.IN)

def dist(echo):
        startt = time.time()
        stopt = time.time()
        timeouts = 0
        gpio.output(trigg, True)
        time.sleep(0.00001)
        gpio.output(trigg,False)
        
        while gpio.input(echo) == 0:
                startt = time.time()
                timeouts += 1
                if timeouts > 5000:
                        break
        while gpio.input(echo) == 1:
                stopt = time.time()
                if timeouts > 5000:
                        break
                
        timetaken = stopt - startt
        distance = (timetaken * 34300) / 2
        return distance
