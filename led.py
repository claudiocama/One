import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

def led_sec(sec):
    GPIO.output(33, True) 
    GPIO.output(37, True)
    sleep(sec)
    GPIO.output(33, False)
    GPIO.output(37, False)

def blink_sec(sec):
    x=0
    while True:
        GPIO.output(33, True) 
       	GPIO.output(37, True)
        sleep(0.5)
        GPIO.output(33, False)
        GPIO.output(37, False)
        sleep(0.5)
        x+=1
        if x==sec:
            break
