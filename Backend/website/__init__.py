from flask import Flask
from flask_cors import CORS
from os import path 
from flask_login import LoginManager
import mysql.connector


def create_app():
    app = Flask(__name__)
    CORS(app)

    db_config = {
        
    }
    conn = mysql.connect()
    cursor =conn.cursor()

    

    from .main_page import main_page
    from .auth import auth

    app.register_blueprint(main_page, url_prefix="/home")
    app.register_blueprint(auth, url_prefix="/")

    
    return app