# coding=utf-8
# author:xsl

import os, sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(PROJECT_DIR, os.pardir)

sys.path.append(PARENT_DIR)
sys.path.append(PROJECT_DIR)

EMAIL_FROM = 'help@xiusl.com'
EMAIL_FROM_PASS = 'He0108.'
EMAIL_SMTP = 'smtp.exmail.qq.com'
EMAIL_SMTP_PORT = 465

