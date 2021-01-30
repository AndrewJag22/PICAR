#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)
 
# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [7,11,13,15]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, 0)
 
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
        
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise
# Initialise variables
StepCounter = 0
 
# Start main loop
while True:
 
  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      GPIO.output(xpin, 1)
    else:
      GPIO.output(xpin, 0)
 
  StepCounter += StepDir
 
  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
 
  # Wait before moving on
  time.sleep(0.001)
