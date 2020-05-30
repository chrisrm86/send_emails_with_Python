"""
import smtplib, ssl

port = 465
password = "ThisIsThePassword0123456789"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login("userfortest0123456789@gmail.com", password)

#SMTP_SSL


port = 465
smtp_server = "smtp.gmail.com"

sender_email = "userfortest0123456789@gmail.com"
receiver_email = "christianrmoran86@gmail.com"
message = "ESto es un correo electronico mandado desde Python" 
"""

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "userfortest0123456789@gmail.com"  # Enter your address
receiver_email = "christianrmoran86@gmail.com"  # Enter receiver address
password = "ThisIsThePassword0123456789"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
