import Servomotor
import DC_Hbridge as dc
import ultrasonic_sensor as us
from socket import *
import _thread
import time
from time import ctime
import RPi.GPIO as GPIO

Servomotor.setup()
dc.stepup()
us.setup()

server = ''
port = 21678
BUFSIZE = 1024

server_addr = (server,port)

while True:
        tcpSock = socket(AF_INET,SOCK_STREAM)
        try:
                tcpSock.connect(server_addr)
                msg = str(us.distance())
                msgg = str.encode(msg, 'utf-8')
                tcpSock.sendall(msgg)
                data = ''
                data = tcpSock.recv(BUFSIZE)
                print (data.decode())
        except KeyboardInterrupt:
                print("ending")
        tcpSock.close()
        time.sleep(2)
        

