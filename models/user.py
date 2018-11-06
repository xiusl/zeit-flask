# coding=utf-8
# author:xsl

from mongoengine import Document, StringField, IntField, DateTimeField
from bson import ObjectId
import datetime


class User(Document):
    meta = {
       "db_alias": "heroku_rnz54xf1",
    }

    id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField()
    email = StringField()
    phone = StringField()
    password = StringField()
    avatar = StringField()
    desc = StringField()
    type = IntField()
    level = IntField()
    created_at = DateTimeField(default=datetime.datetime.now)
