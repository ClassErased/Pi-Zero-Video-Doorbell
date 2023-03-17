from _camera_ import cam
import smtplib
import os
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from time import sleep
import glob

sender = ""
password = ""
receiver = ""

dir = "./doorbell/"  #Note to self: change this, by no means how this will be done but good enough for now. #Securing this folder is important, but dont use hardcoded passwords... obiviously.
prefix = "video"

motion_detected = False

def motion_detect(activity):
    if not activity == False:
        print("motion detected")
    else:
        pass 

def capture_img():
    if not os.path.exists(dir):
        os.makedirs(dir) #I trust you not to execute this somewhere dumb. #Note to self: maybe make it an input?
        print(f'\n directory ', dir, ' not found',  '\ncreating ', dir, ' in current path\n') # added this to let user know the path has been created.
    
    files = sorted(glob.glob(os.path.join(dir, prefix + '[0-9][0-9][0-9].jpg'))) # Returns a list of files that matches the path & prefix specified in the function argument
    
    count = 0
    if len(files) > 0:
        count = int(files[-1][-7:-4])+1 # Use the last filename to initialize the count

if __name__ == '__main__':
    print("hi my name is, my name is, ricka rucka slim shady")
    #if motion_detected:
        #capture_img()
