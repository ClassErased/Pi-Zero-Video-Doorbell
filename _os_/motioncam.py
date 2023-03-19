#import libcamera
from gpiozero import Button, MotionSensor, LED
import gpiozero as GPIO 
#import requests 
import time 
#from time import gmtime, strftime 
#from pygame import mixer
#from threading import Thread

#cam - PiCamera() Don't think this needs to be defined
sens = MotionSensor(17)
doorbell = Button(22)
led = LED(27)

#initialize the pi board and set pins to input
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sens, GPIO.IN)
GPIO.setup(doorbell, GPIO.IN)
#variables that will change with pyhsical interaction
activity = False
button = False

def motion_scanning() -> bool:
    try:
        while True:
            time.sleep(0.3) #code will look for input every 300ms
            activity = GPIO.input(sens)
            if activity == 1:
                print(f"GPIO pin ",sens,"is ",activity) #debug
                led.on() #if activity is found then turn led on for 1000ms
                time.sleep(1)
                led.off()

    except KeyboardInterrupt:
        pass

#hey so you're gonna need to thread these ;) AND the code to handle communication
#but if a piezo or other sound method is added it can be added to each function
#but if you have lots of functions just define sound and call it
def button_press() -> bool:
    try:
        while True:
            time.sleep(0.1) # look for input every 100ms
            button = GPIO.input(doorbell)
            if button == 1:
                print(f"GPIO pin ",doorbell,"is ",button) #debug
                led.on() #if the button is pressed turn led on for 1000ms
                time.sleep(1)
                led.off()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    print()
    #GPIO.cleanup()