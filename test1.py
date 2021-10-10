import RPi.GPIO as GPIO
import time

PIN18 = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(PIN18, True)
    time.sleep(1)
    GPIO.output(PIN18, False)
    time.sleep(1)
