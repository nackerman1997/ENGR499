#I am testing to see if this work
#this is my second test to see if it works
rpm = 1000             #rotations per minutes
pul = 1600          #pulses per revoltuion
spr = 200           #steps per revolution
dps = (0.393701/spr)             #in inches
dis = 9              #distnace desired (inches)
pps = int(pul/spr)    #pulses per step 
sl = ((60/rpm)/pul)/2     #sleep delay

import RPi.GPIO as GPIO       
from time import sleep                          

def step():
    for i in range(pps):
        GPIO.output(20, GPIO.HIGH)
        sleep(sl)
        GPIO.output(20, GPIO.LOW)
        sleep(sl)
        
def distance_T():
    for i in range(int(dis/dps)):
        step()

def cleanGPIO():
    GPIO.cleanup()

def main():
    GPIO.setwarnings(False)                   #do not show any warnings
    GPIO.setmode(GPIO.BCM)                     #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
    GPIO.setup(20,GPIO.OUT)                     # initialize GPIO19 as an output.
    GPIO.setup(21,GPIO.OUT)                     #dirction pin initilized

    GPIO.output(20,GPIO.LOW)
    GPIO.setup(21,GPIO.LOW) 

    print("start of program")
    distance_T()

    sleep(5)#sleep for 5 seconds 
    print("backstep")#return back to set distance 
    GPIO.output(21, GPIO.HIGH)
    distance_T()
    GPIO.output(21, GPIO.LOW)
    
    print("end of program")
    cleanGPIO()

main()
