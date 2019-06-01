import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

try:
    I = 1
    while I < 9:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.25)
        I += 1
    
    GPIO.cleanup()





