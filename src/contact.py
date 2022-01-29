import os
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from dotenv import load_dotenv
from ftplib import FTP_TLS



load_dotenv()



smtp_server = "smtp.gmail.com"
Port = 587  # For starttls

# Create a secure SSL context
context = ssl.create_default_context()
client = Client(os.getenv('API_SID_TWILIO'), os.getenv('API_KEY_TWILIO'))


def reportcapture(ImgFileName):
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, Port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(os.getenv('SENDER_EMAIL'), os.getenv('SENDER_MAIL_PASS'))

        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = 'Security Capture'
        msg['From'] = 'OCV Security'
        msg['To'] = os.getenv('RECEIVER_EMAIL')

        msg2 = MIMEMultipart()
        msg2['Subject'] = 'Security Capture'
        msg2['From'] = 'OCV Security'
        msg2['To'] = os.getenv('RECEIVER_EMAIL_TWO')

        text = MIMEText("Figure Detected")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

        server.sendmail(os.getenv('SENDER_EMAIL'), os.getenv('RECEIVER_EMAIL'), msg.as_string())
        client.messages.create(body=f"Figure Detected \n Time: {time.asctime(time.localtime(time.time()))}", from_=os.getenv('SENDER_NUMBER'), to=os.getenv('RECEIVER_NUMBER'))
        server.quit()

    except Exception as e:
        # Print any error messages to stdout
        print(e)


def write():
    ftp = FTP_TLS("webdevgroupcu.org")
    ftp.login(os.getenv('SERVER_LOGIN'), os.getenv('SERVER_PASS'))
    ftp.getwelcome()
    print('Server connected.')


