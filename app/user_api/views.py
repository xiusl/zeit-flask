# coding=utf-8
# author:xsl

from __future__ import absolute_import
from models import User
from . import user_api
from flask import request, abort, current_app, jsonify
from bson import ObjectId


@user_api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']
    u = User.objects(email=email).first()
    if u:
        return jsonify({"msg": "User Exist"}), 400
    u = User(email=email, password=password)
    u.save()
    return jsonify({"data": u.to_json()}), 200
