import csv, smtplib, ssl

message =  """Subject: This is a test email from a Python script

Hi {NAME}, Your favorite sport is {SPORT}\n
It's a great sport.\n
\n
Greetings.
"""

sender_email = "Enter your email sender address"
password = "Password of email sender address"


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	server.login(sender_email, password)

	with open("emails.csv") as file:
		reader = csv.reader(file)
		next(reader)
		for NAME, EMAIL, SPORT in reader:
			server.sendmail(
				sender_email,
				EMAIL,
				message.format(NAME=NAME, SPORT=SPORT),
			)