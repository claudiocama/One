#import RPi.GPIO as GPIO
import subprocess
import platform
import os, _thread

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(33, GPIO.OUT)
#GPIO.setup(37, GPIO.OUT)
if platform.system()=="Windows":
    subprocess.call(["set", "FLASK_APP=webserver.py"])
else:
    os.putenv("FLASK_APP","webserver.py")
def webserver():
    subprocess.call(["flask", "run"])
_thread.start_new_thread(webserver,())
subprocess.call(["python", "detect.py", "One.pmdl"])
