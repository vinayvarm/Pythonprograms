import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


host="smtp.gmail.com"
port=587


file=open("detailsemail.txt","r")
data=file.readlines()
print(data)

body="""\
Subject: ImportantEmail

Hey siva how are u"""
session=smtplib.SMTP(host,port)
session.starttls()

session.login("coursep41@gmail.com","YANIVias")
for i in data:
    new=i.split(",")
    session.sendmail("coursep41@gmail.com", i, body)
session.quit()




