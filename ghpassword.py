'''
Password generator 
'''
import random
import math
from email.message import EmailMessage
import ssl
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
import os

symbols = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*"]

length = input("How long do you want your password to be? (16 would be safe) ")

password =  ""

for i in range(int(length)):
    x = random.choice(symbols)
    password += x


from_addr = "example@gmail.com"
email_password = '''Your gmail or other SMTP service password'''
to_addr = "example@gmail.com"
subject = 'Your Password' 
content = "Here is your super secret password: " + "\n" + password 

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(from_addr, email_password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())

print("Check your email!")



