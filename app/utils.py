# coding=utf-8
# author:xsl

import smtplib
from email.mime.text import MIMEText
from app import config
from flask import jsonify, current_app
from functools import wraps

def send_email(to, subject, content):
    msg = MIMEText(content.encode('utf8'), 'html', 'utf8')
    msg['From'] = config.EMAIL_FROM
    msg['To'] = to
    msg['Subject'] = subject

    try:
        smtp = smtplin.SMTP_SSL(config.EMAIL_SMTP, config.EMAIL_SMTP_PORT)
        smtp.ehlo()
        smtp.login(config.EMAIL_FROM, config.EMAIL_FROM_PWD)
        smtp.sendmail(config.EMAIL_FROM, to, msg.as_string())
        smtp.close()
    except Exception as e:
        return False
    return True

def send_email_code(to, code):
    subject = '验证码'
    content = '验证码 %s' % code
    return send_email(to, subject, content)

class InvalidAPIUsage(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def login_required(fn):
    @wraps(fn)
    def wrapped_func(*args, **kwargs):
        u = current_app.user
        if not u:
            raise InvalidAPIUsage('No Auth', 403)
        return fn(*args, **kwargs)
    return wrapped_func
