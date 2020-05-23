'''
STATUS:
current configuration - 1.8 deg per step

'''

import RPi.GPIO as GPIO
from time import sleep

DIR = 19   # Direction GPIO Pin
STEP = 26  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)

def rotate(degrees):
    step_count = degrees//(360/SPR)
    delay = 0.005 # 1/SPR

    for _ in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
