import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "Enter sender email address"
receiver_email = "Enter receiver email address"
password = "Password of sender email"
message = """\
Subject: Message from Python script

Hi there!

This message is sent from Python script.
You can see more code in github.com/chrisrm86.

Bye!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)