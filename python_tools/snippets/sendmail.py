"""
Send an email from your G-mail account.
ref: https://realpython.com/python-send-email/#sending-your-plain-text-email
"""

import smtplib
import ssl
from password import mail_password_alalaki as mail_password  # Import your password
from email.mime.text import MIMEText


def sendmail(from_email="alalaki.koyomi@gmail.com",  # Enter your address
             to_email="harlan.zhu@gmail.com",  # Enter receiver address, can be a list
             subject="Test Test",
             body="""
Hi,

This message is sent from Python.
"""):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = mail_password
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = ", ".join(to_email) if isinstance(to_email, list) else to_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())


if __name__ == "__main__":
    sendmail()
