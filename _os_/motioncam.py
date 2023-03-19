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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sens, GPIO.IN)
GPIO.setup(doorbell, GPIO.IN)
activity = False
button = False

def motion_scanning() -> bool:
    try:
        while True:
            time.sleep(0.3)
            activity = GPIO.input(sens)
            if activity == 1:
                print(f"GPIO pin ",sens,"is ",activity)
                led.on()
                time.sleep(1)
                led.off()

    except KeyboardInterrupt:
        pass

#hey so you're gonna need to thread these ;)
def button_press() -> bool:
    try:
        while True:
            time.sleep(0.2)
            button = GPIO.input(doorbell)
            if button == 1:
                print(f"GPIO pin ",doorbell,"is ",button)
                led.on()
                time.sleep(1)
                led.off()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    print()
    #GPIO.cleanup()