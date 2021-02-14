from flask import Flask
from flask_wtf.csrf import CsrfProtect
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "JZINICR0N-S3RV3R"
#login_manager = LoginManager(app)
from app import routes
csrf = CsrfProtect(app)
csrf.init_app(app)
