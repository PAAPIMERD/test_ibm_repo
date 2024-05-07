import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while True:
  time.sleep(60)
  sender_email = "rishavi080720002@gmail.com"
  sender_password = "vbgi mtxh gnfw fzoq"
  receiver_email = "avinash9588@gmail.com"
  subject = "TRADE SETUP SUCESSFULL BUDDY,ALL SET TO GOT"
  body = "Hello ,now we are all set to trade !!,algo will start trade whenever its feels like to go into a trade now sit back and relax,and just make sure the hardware the your network remains stable ,else algo might get interuppted in between and will spoil your experienrnce"
  send_email(sender_email, sender_password, receiver_email, subject, body)

