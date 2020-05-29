import RPi.GPIO as GPIO
from time import sleep
import argparse

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
RESOLUTION = 32  # 1/32
SPR = 200 * RESOLUTION   # Steps per Revolution (360 / 1.8)
MODE = (14, 15, 18)  # Microstep resolution pins

alt_dir = 19   # Altitude motor
az_dir = 20    # azimuth motor
alt_step = 26  # Alt
az_step = 21   # Az

GPIO.setmode(GPIO.BCM)
GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE, (1, 0, 1))
GPIO.setup(alt_dir, GPIO.OUT)
GPIO.setup(az_dir, GPIO.OUT)
GPIO.setup(alt_step, GPIO.OUT)
GPIO.setup(az_step, GPIO.OUT)


def rotate(step, dir_pin, DIR, degrees):
    step_count = round(degrees/(360/SPR))
    delay = 0.005/RESOLUTION  # 1/SPR
    GPIO.output(dir_pin, DIR)
    for _ in range(step_count):
        GPIO.output(step, GPIO.HIGH)
        sleep(delay)
        GPIO.output(step, GPIO.LOW)
        sleep(delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alt", type=float, help="Altitude of destination")
    parser.add_argument("az", type=float, help="Azimuth of destination")
    args = parser.parse_args()
    altAngle, azAngle = args.alt, args.az

    if altAngle >= 0:
        rotate(alt_step, alt_dir, CW, altAngle)
    else:
        rotate(alt_step, alt_dir, CCW, altAngle)

    if azAngle >= 0:
        rotate(az_step, az_dir, CW, azAngle)
    else:
        rotate(az_step, az_dir, CCW, azAngle)
    GPIO.cleanup()
