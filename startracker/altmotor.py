'''
STATUS:
current configuration - 1.8 deg per step

'''

import RPi.GPIO as GPIO
from time import sleep

DIREC = 20   # direction GPIO Pin
step = 21  # Step GPIO Pin
cw = 1     # Clockwise Rotation
ccw = 0    # Counterclockwise Rotation
spr = 200   # Steps per Revolution (360 / 1.8)

GPIO.setup(DIREC, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.output(DIREC, cw)

def rotate(degrees):
    step_count = int(degrees//(360/spr))
    delay = 0.005 # 1/SPR

    for _ in range(step_count):
        GPIO.output(step, GPIO.HIGH)
        sleep(delay)
        GPIO.output(step, GPIO.LOW)
        sleep(delay)
