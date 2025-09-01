from flask import Flask
from flask_cors import CORS
from os import path 
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
    app.config ['SECRET_KEY'] = "studyspacereview"
    # db = SQLAlchemy(app)
    CORS(app)

    from .main_page import main_page
    from .auth import auth

    app.register_blueprint(main_page, url_prefix="/home")
    app.register_blueprint(auth, url_prefix="/")

    
    return app