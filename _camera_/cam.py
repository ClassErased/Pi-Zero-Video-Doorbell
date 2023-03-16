import libcamera
from gpiozero import Button, MotionSensor

#do I import this into PIR.py or vice-versa? Or just merge them? I don't know but ill work it out later.
#cam - PiCamera() Don't think this needs to be defined with libcamera
sens = MotionSensor()
doorbell = Button()