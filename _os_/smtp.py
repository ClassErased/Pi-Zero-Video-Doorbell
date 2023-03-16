import smtplib
import os
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from time import sleep

sender = ""
password = ""
receiver = ""

dir = "./doorbell/"  #I don't like this, this is just a placeholder for another way. I plan to store the videos locally anyway so
#This will certainly change 
prefix = "video"

def capture_img():
    if not os.path.exists(dir):
        os.makedirs(dir)
