import smtplib, ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
import re
import os
import shutil

mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

mycursor = mydb.cursor()

mycursor.execute("SELECT email FROM users;")

myresult = mycursor.fetchall()

for x in myresult:
  #print(x)
  file = open("hehe.txt", "a")
  file.write(str(x))
  file.close()
path_current="./hehe_current.txt"
shutil.move("./hehe.txt", path_current)
with open("./hehe_current.txt") as f:
    body = f.read()
    #print (body)
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", body)
    # print (emails)

sender_email = "crudespace@gmail.com"
receiver_email = "vedantfar@gmail.com"
password = ""
cc = ""
bcc = emails

message = MIMEMultipart("alternative")
message["Subject"] = "Next 10 Days ISS Visible Passes (Beta)"
message["From"] = sender_email
message["To"] = receiver_email
message["Cc"] = cc
message["Bcc"] = ", ".join(bcc)
# print (message["Bcc"])

# string to store the body of the mail
with open('iss_passes_current.txt') as f:
    body = f.read()

# attach the body with the msg instance
message.attach(MIMEText(body, 'plain'))
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        message["From"], message["To"].split(",") + message["Cc"].split(",") + message["Bcc"].split(","), message.as_string()
    )
