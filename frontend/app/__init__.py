import os
from dotenv import load_dotenv

from flask import Flask
#from flask_wtf.csrf import CsrfProtect
#from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET")

#login_manager = LoginManager(app)

from app import routes

#csrf = CsrfProtect(app)
#csrf.init_app(app)
