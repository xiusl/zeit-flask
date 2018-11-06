from flask import Flask, request, jsonify, current_app 
from models import User

def create_app():
    app = Flask(__name__)

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

    return app

