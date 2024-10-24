#import libraries
import RPi.GPIO as GPIO # type: ignore
import time

#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
# Data pin for the led
led = 4
#Initialize your pin
GPIO.setup(led,GPIO.OUT)

#Turn on the LED
print("LED on")
GPIO.output(led,1)

#Wait 5s
time.sleep(5)

#Turn off the LED
print("LED off")
GPIO.output(led,0)