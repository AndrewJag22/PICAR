import Servomotor
import DC_Hbridge as dc
import ultrasonic_sensor as us
from socket import *
import _thread
from time import ctime
import RPi.GPIO as GPIO

Servomotor.setup()
dc.stepup()
us.setup()

HOST = ''
PORT = 21678
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)

def newClient(tcpCliSock,addr):
        print ('...connected from :', addr)
        try:
                data = ''
                data = tcpCliSock.recv(BUFSIZE)
                print (data.decode())

                msg = str(us.distance())
                msgg = str.encode(msg, 'utf-8')
                
                tcpCliSock.sendall(msgg)
                tcpCliSock.close()
        except KeyboardInterrupt:
                Servomotor.close()
                GPIO.cleanup()

print ('Waiting for connection')
tcpSerSock.bind(ADDR)
tcpSerSock.listen(2)

while True:
        tcpCliSock,addr = tcpSerSock.accept()
        _thread.start_new_thread(newClient,(tcpCliSock,addr))
        
tcpSerSock.close();
