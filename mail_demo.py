import smtplib
import os
from email.message import EmailMessage

email_address=os.environ.get('EMAIL_ADDRESS')   # to hide private information
email_password=os.environ.get('EMAIL_PASSWORD')  # by storing it in environment variables
msg=EmailMessage()

msg['Subject']='just a demo by MUSKAN!!'
msg['From']=email_address
msg['To']='abc123@gmail.com'
msg.set_content('this is just for testing ,spamming,entertaining purposes')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_address,email_password)    # to login to the sender's gmail account

    for i in range(1,51):  # for sending multiple mails by applying loop

         smtp.send_message(msg)