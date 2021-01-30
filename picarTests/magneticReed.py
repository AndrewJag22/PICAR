import RPi.GPIO as gpio
import time
import smtplib

try:
    need_clean = False
    msg = 'door waws '
    door_msg = {True:'opened', False:'closed'}

    print('seetting up')

    pin = 12
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    next_state = True
    need_clean = True
    print('readu')

    while True:
        
        if gpio.input(pin) == next_state:
            print('detected!!!: ')
            next_state = not next_state
        time.sleep(0.3)
except KeyboardInterrupt:
    gpio.cleanup()
    cleaned = False
if need_clean:
    gpio.cleanup()
print('endd')
