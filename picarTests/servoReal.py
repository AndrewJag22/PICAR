import time
import pigpio

serv = 4
pi = pigpio.pi()
def setup():
    pi.set_mode(serv, pigpio.OUTPUT)

def left():
    pi.set_servo_pulsewidth(serv,1000)

def right():
    pi.set_servo_pulsewidth(serv,2500)

def stop():
    pi.stop()

    
