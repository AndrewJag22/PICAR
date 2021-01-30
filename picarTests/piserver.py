import servoReal as servo
import DC_Hbridge as dc
from socket import *
import _thread
from time import ctime
import RPi.GPIO as GPIO

servo.setup()
dc.stepup()

ctrCmd = ['Up','Down','For','Back']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)



def newClient(tcpCliSock,addr):
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if data.decode() == ctrCmd[0]:
                                servo.left()
                                print("lefy")
                        if data.decode() == ctrCmd[1]:
                                servo.right()
                                print("right")
                        if data.decode() == ctrCmd[2]:
                                dc.stepsFor()
                                print("dor")
                        if data.decode() == ctrCmd[3]:
                                dc.stepsBack()
                                print("bCK")
                tcpCliSock.close()
        except KeyboardInterrupt:
                Servomotor.close()
                GPIO.cleanup()

print ('Waiting for connection')
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        tcpCliSock,addr = tcpSerSock.accept()
        _thread.start_new_thread(newClient,(tcpCliSock,addr))
        
tcpSerSock.close();
