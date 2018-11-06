# coding=utf-8
# author:xsl

from mongoengine import Document, ObjectIdField, StringField, IntField, DateTimeField
from bson import ObjectId
import datetime, time
from werkzeug.security import generate_password_hash, check_password_hash
import hmac, hashlib, base64

def hmac_sha256(key, message):
    key = key.encode('utf8')
    message = message.encode('utf8')
    sign = hmac.new(key, message, digestmod=hashlib.sha256).digest()
    sign = ''.join([('%02x' % b) for b in sign])
    return sign


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

    def save(self, *args, **kwargs):
        if self.password and \
            (self.password.count('$') < 2 or len(self.password) < 50):
            self.password = generate_password_hash(self.password)
        if not self.avatar:
            self.avatar = 'https://image.sleen.top/default.jpg'
        return super(User, self).save(*args, **kwargs)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    
    def get_token(self, timestamp=None, expired_at=None):
        timestamp = timestamp or int(time.time())
        expired_at = expired_at or (timestamp + 86400 * 30)
        message = '%s:%s:%s' % (self.id, timestamp, expired_at)
        sign = hmac_sha256(self.password, message)
        signed_message = '%s$%s' % (message, sign)
        token = base64.b64encode(signed_message.encode('utf8'))
        return token.decode('utf8')


    @classmethod
    def get_by_token(cls, token):
        try:
            token = base64.b64decode(token).decode('utf8')
            message, sign = token.split('$')
            user_id, ts, expired_at = message.split(':')
        except:
            return None
        if int(time.time()) > int(expired_at):
            return None

        user = cls.objects(id=user_id).first()
        if not user:
            return None

        if sign != hmac_sha256(user.password, message):
            return None

        return user


    def to_json(self, with_token=False):
        user_json = {
            "id": str(self.id),
            "name": self.name,
            "desc": self.desc,
            "avatar": self.avatar,
        }
        if with_token:
            user_json["token"] = self.get_token()
        return user_json

    def edit(self, data):
        allow_edit = ['name', 'desc', 'avatar']
        for k, v in data.items():
            if allow_edit.__contains__(k):
                setattr(self, k, v)
            print(k)
        self.save()
