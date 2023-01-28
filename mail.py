import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "crudespace@gmail.com"
receiver_email = "vedantfar@gmail.com,varospaxo@gmail.com"
password = "qngnwmlokpwxtoka"
cc = ""

message = MIMEMultipart("alternative")
message["Subject"] = "Email Test"
message["From"] = sender_email
message["To"] = receiver_email
message["Cc"] = cc

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       ISS will pass over you soon<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        message["From"], message["To"].split(",") + message["Cc"].split(","), message.as_string()
    )