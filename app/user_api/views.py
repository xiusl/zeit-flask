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

@user_api.route('/<id>', methods=['GET'])
def get_by_id(id):
    u = User.objects(id=ObjectId(id)).first()
    if not u:
        return jsonify({"msg": "User not Found"}), 404
    return jsonify({"data": u.to_json()}), 200

@user_api.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    email = data['email']
    password = data['password']
    u = User.objects(email=email).first()
    if not u:
        return jsonify({"msg": "User not Found"}), 404
    if not u.check_password(password):
        return jsonify({"msg": "Password error"}), 400
    return jsonify({"data": u.to_json(with_token=True)}), 200

