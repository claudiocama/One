import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
subprocess.call(["python", "demo.py", "One.pmdl"])
