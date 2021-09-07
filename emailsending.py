import smtplib
host="smtp.gmail.com"
port=587

body="""\
Subject: ImportantEmail

Hey this is vinay"""
session=smtplib.SMTP(host,port)
session.starttls()

session.login("coursep41@gmail.com","YANIVias")
session.sendmail("coursep41@gmail.com","vpkrkmd@gmail.com",body)
session.quit()
