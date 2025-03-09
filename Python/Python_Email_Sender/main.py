import smtplib

sender = "19409@uktc-bg.com"
receiver = "gogo.rex20052@gmail.com"
password = "adelina20"
subject = "Python email test"
body = "I wrote an email"

message = f""" From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")

    server.sendmail(sender, receiver, message)
    print("Email sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")

