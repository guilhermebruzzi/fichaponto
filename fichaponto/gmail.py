#!/usr/bin/env python
#-*- coding:utf-8 -*-

import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

USER = os.environ['USER_GMAIL'] if 'USER_GMAIL' in os.environ.keys() else 'ficha.ponto.contato'
PASSWD = os.environ['PASSWD_GMAIL'] if 'PASSWD_GMAIL' in os.environ.keys() else 'ficha.ponto.contato@ejcm'

def send_email(to, subject, body, file_path):
    user_gmail = "%s@gmail.com" % USER
    passwd_gmail = PASSWD

    msg = MIMEMultipart()
    msg['From'] = user_gmail
    msg['To'] = ', '.join(to)
    msg['Subject'] = subject

    msgText = MIMEText('<p>%s</p>' % body, 'html')
    msg.attach(msgText)   # Added, and edited the previous line

    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(file_path,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_path))
    msg.attach(part)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user_gmail, passwd_gmail)
    mailServer.sendmail(user_gmail, to, msg.as_string())
    mailServer.close()
