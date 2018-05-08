import RPi.GPIO as GPIO
import subprocess
import platform

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
if platform.system=="Windows":
    subprocess.call(["set", "FLASK_APP=webserver.py"])
else:
    subprocess.call(["export", "FLASK_APP=webserver.py"])
subprocess.call(["flask", "run"])
subprocess.call(["python", "demo.py", "One.pmdl"])
