from nanpy import (ArduinoApi, SerialManager)
from time import sleep

ledPin = 7
btnPin = 8
ledStat = False
btnstat = 0

try:
    connection = serialManager()
    a = ArduinoApi (connection = connection)
except:
    print("fail to connect to ardinno")

# Setup t
a.pinMode(ledPin,a.OUTPUT)
a.pinMode(btnPin,a.INPUT)

try:
    while True:
        btnStat - a.digitalRead(btnPin)
        print("btn state is : {}".format(btnStat))
        if btnStat:
            if ledStat:
                a.digitalWrite(ledPin, a.LOW)
                ledstat = False
                print("leeed offff")
                sleep(1)
            else:
                a.digitalWrite(ledPin, a.HIGH)
                ledState = True
                print("leeed onnnn")
                sleep(1)
except:
    a.digitalWrite(ledPin, a.LOW)
    
