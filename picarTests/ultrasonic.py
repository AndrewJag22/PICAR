from gpiozero import DistanceSensor
import time

ultrasonic = DistanceSensor(echo=18,trigger=24)

ultrasonic.distance

while True:
    print(ultrasonic.distance)
    time.sleep(1)
