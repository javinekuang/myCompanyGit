# -*- coding: utf-8 -*-
__author__ = 'Administrator'



from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr(u'匡宇的Python程序 <%s>' % from_addr)
msg['To'] = _format_addr(u'小芳芳 <%s>' % to_addr)
msg['Subject'] = Header(u'来自Python的问候', 'utf-8').encode()

msg.attach(MIMEText('hello, this mail is sent by Python...\n Q me when you received this', 'plain', 'utf-8'))

with open('blur.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='blur.png')
    mime.add_header('Content-Disposition', 'attachment', filename='blur.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')

    mime.set_payload(f.read())

    encoders.encode_base64(mime)

    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



