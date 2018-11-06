# coding=utf-8
# author:xsl

from . import main

@main.route('/')
def index():
    return "Hello Now!"
