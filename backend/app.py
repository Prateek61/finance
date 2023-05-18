from flask import Flask, jsonify
from os import path, environ
from flask_cors import CORS

from modules.models import  db
from modules.auth import auth, token_required
from modules.home import home

# Get environment variable for database URI
DATABASE_URI = environ.get('DATABASE_URI')
SECRET_KEY = environ.get('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = "notsosecretafterall"
if SECRET_KEY:
    app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'database.db')
if DATABASE_URI:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(home)

db.init_app(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=False)

