import ultrasonic_sensor as us
from socket import *
import _thread
import time
import RPi.GPIO as GPIO
import led
import pigpio

GPIO.setwarnings(False)
us.setup()
led.setup()

eFront = 10
eBack = 12
pi = pigpio.pi()

server = '192.168.1.115'
port = 21678
BUFSIZE = 1024

server_addr = (server,port)
tcpSock = socket(AF_INET,SOCK_STREAM)
tcpSock.connect(server_addr)

def calcc(front,back,ofront,oback):
        file = open("safeMove.txt", "w+")
        pi.set_mode(17, pigpio.OUTPUT)
     
        if (front <= 30) or (back <= 30):
                print('less than 30')
                if (ofront <= 30) or (oback <= 30):
                        file.write("False")
                        file.flush()
                        led.ledOn(37)
                        pi.write(17, 1)
                        time.sleep(1)
                        pi.write(17, 0)
                elif (ofront > 30) and (oback > 30):
                        file.write("False")
                        file.flush()
                        led.ledOn(35)
                else:
                        file.write("False")
                        file.flush()
                        led.ledOn(29)
        elif (front > 30) and (back > 30):
                if (ofront <= 30) or (oback <= 30):
                        file.write("True")
                        file.flush()
                        led.ledOn(33)
                        pi.write(17, 1)
                        time.sleep(1)
                        pi.write(17, 0)
                elif (ofront > 30) and (oback > 30):
                        file.write("True")
                        file.flush()
                        led.ledOn(31)
                else:
                        file.write("True")
                        file.flush()
                        led.ledOn(29)
        else:
                print('skipped')
                file.write("True")
                file.flush()
                led.ledOn(29)
        file.close()

while True:
        try:
                file = open("safeMove.txt")
                frontt = str(int(us.dist(eFront)))
                backt = str(int(us.dist(eBack)))
                msg = frontt + ';' + backt
                
                tcpSock.sendall(msg.encode())
                front = int(frontt)
                back = int(backt)
                
                data = ''
                data = tcpSock.recv(BUFSIZE).decode()
                num = data.split(';')
                ofront = int(num[0])
                oback = int(num[1])
                calcc(front,back,ofront,oback)
                print(file.read())
        except KeyboardInterrupt:
                print("ending")
                file.close()
                #tcpSock.close()
        time.sleep(1)
