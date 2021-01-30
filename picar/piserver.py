import servoReal as servo
import DC_Hbridge as dc
import led
from socket import *
import _thread
import time

servo.setup()
dc.setup()
led.setup()

ctrCmd = ['L','R','F','B','C']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

def newClient(tcpCliSock,addr):
        file = open("safeMove.txt", "r")
        state = file.readline()
        if state == "True":
                try:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE).decode()
                        if data == ctrCmd[0]:
                                servo.left()
                                print('left')
                        if data == ctrCmd[1]:
                                servo.right()
                                print('right')
                        if data == ctrCmd[2]:
                                dc.stepsFor()
                                print('forr')
                        if data == ctrCmd[3]:
                                dc.stepsBack()
                                print('bkk')
                        if data == ctrCmd[4]:
                                servo.cent()
                                print('centre')
                except KeyboardInterrupt:
                        tcpSerSock.close()
                time.sleep(0.5)
        elif state == "False":
                led.ledOn(37)
        tcpCliSock.close()
        file.close()


print ('Waiting for connection')
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        tcpCliSock,addr = tcpSerSock.accept()
        _thread.start_new_thread(newClient,(tcpCliSock,addr))
        print('heer')
tcpSerSock.close()
