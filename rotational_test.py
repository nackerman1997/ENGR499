rpm = 4             #rotations per minutes
pul = 1600          #pulses per revoltuion
spr = 200           #steps per revolution
revs = 10           #revolutions desired
pps = int(pul/spr)    #pulses per step 
sl = ((60/rpm)/pul)/2     #sleep delay

import RPi.GPIO as GPIO                   #calling header file which helps us use GPIO’s of PI
from time import sleep                           #calling time to provide delays in program

def step():
    for i in range(pps):
        GPIO.output(12, GPIO.HIGH)
        sleep(sl)
        GPIO.output(12, GPIO.LOW)
        sleep(sl)

def revolution():
    for i in range(spr*revs):
        step()

def cleanGPIO():
		GPIO.cleanup()

def main():
    GPIO.setwarnings(False)                   #do not show any warnings
    GPIO.setmode(GPIO.BCM)                     #we are programming the GPIO by BCM pin numbers. 

    GPIO.setup(12,GPIO.OUT)     #Pulse Rotational Motor
    GPIO.setup(16, GPIO.OUT)    #direction Rotational Motor
    GPIO.output(12,GPIO.LOW)
    GPIO.setup(16,GPIO.LOW) 
    
    print("Starting revolutions")
    revolution()
    print("end of program")

    cleanGPIO()
main()