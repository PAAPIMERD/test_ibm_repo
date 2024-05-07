import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add message body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your gmail account
    server.login(sender_email, sender_password)

    # Send Email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()

while True:
  time.sleep(1)
  sender_email = "rishavi08072002@gmail.com"
  sender_password = "vbgi mtxh gnfw fzoq"
  receiver_email = "avinash9588@gmail.com"
  subject = "TRADE SETUP SUCESSFULL BUDDY,ALL SET TO GOT"
  body = "Hello ,now we are all set to trade !!,algo will start trade whenever its feels like to go into a trade now sit back and relax,and just make sure the hardware the your network remains stable ,else algo might get interuppted in between and will spoil your experienrnce"
  send_email(sender_email, sender_password, receiver_email, subject, body)

