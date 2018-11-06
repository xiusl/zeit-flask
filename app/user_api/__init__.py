# coding=utf-8
# author:xsl

from flask import Blueprint
user_api = Blueprint('user_api', __name__)
from . import views

