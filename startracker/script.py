import RPi.GPIO as GPIO
import argparse
import azmotor
import altmotor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alt", type=float, help="Altitude of destination")
    parser.add_argument("az", type=float, help="Azimuth of destination")
    args = parser.parse_args()
    altAngle, azAngle = args.alt, args.az

    GPIO.setmode(GPIO.BCM)
    altmotor.setup()
    azmotor.setup()
    altmotor.rotate(altAngle)
    azmotor.rotate(azAngle)    
