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

dir = "./doorbell/"  #I don't like this, this is just a placeholder for another way. I plan to store the videos locally anyway so
#This will certainly change 
prefix = "video"

def capture_img():
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    files = sorted(glob.glob(os.path.join(dir, prefix + '[0-9][0-9][0-9].jpg'))) # Returns a list of files that matches the path & prefix specified in the function argument
    
    count = 0
    if len(files) > 0:
        count = int(files[-1][-7:-4])+1 # Use the last filename to initialize the count

if __name__ == '__main__':
    print("hi my name is, my name is, ricka rucka slim shady")
    #if motion_detected:
        #capture_img()
