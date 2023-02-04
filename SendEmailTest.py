from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

HOST = 'smtp.gmail.com'
PORT = 465

USERNAME = 'ken.stephani@gmail.com'
PASSWORD = 'Nicholas044!'

SENDER = 'ken.stephani@gmail.com'
RECIPIENT = 'ken.stephani@gmail.com'

text_subtype = 'plain'

with open('textfile', 'rb') as f:
    msg = MIMEText(f.read(), text_subtype)


msg['Subject'] = 'Python Script'
msg['From'] = SENDER
msg['To'] = RECIPIENT

try:
    connection = SMTP(HOST, PORT)
    connection.login(USERNAME, PASSWORD)
    connection.sendmail(SENDER, RECIPIENT, msg.as_string())
except  e:
    print("At 28: ", e)
