from flask import Flask, request, jsonify, current_app 
from models import User
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .user_api import user_api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')


    @app.before_request
    def before_request():
        if request.method != "GET":
            try:
                ct = request.headers["Content-Type"]
            except:
                ct = "a"
            if ct and ct != "application/json":
                return jsonify({"msg": "json ok?"}), 400
        try:
            token = request.headers["X-Token"]
        except:
            token = ""
        
        u = User.get_by_token(token)
        current_app.user = u

    @app.after_request
    def after_request(resp):
        resp = make_response(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return resp


    return app

