import pandas as pd
import smtplib

#import socket
#socket.getaddrinfo('localhost', 25)

s = smtplib.SMTP('userfortest0123456789@gmail.com', )

s.starttls()

s.login("userfortest0123456789@gmail.com", "ThisIsThePassword0123456789")

message = "This is a text message"

s.sendmail("userfortest0123456789@gmail.com","christianrmoran86@gmail.com", message)
print("Successfully send mail!")

s.quit()

