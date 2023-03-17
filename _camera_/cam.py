import libcamera
from gpiozero import Button, MotionSensor 
import requests 
import time 
from time import gmtime, strftime 
from pygame import mixer

#cam - PiCamera() Don't think this needs to be defined with libcamera
sens = MotionSensor()
doorbell = Button()

activity = False

def motion_scanning(sens):
    #if motion_found:
        #activity = True #note to self: handle this properly otherwise there's many potential issues.
    print()

#def motion_detect(activity):
    #if not activity == False:
        #print("motion detected")
    #else:
        #pass 