from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .user_api import user_api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')

    return app

