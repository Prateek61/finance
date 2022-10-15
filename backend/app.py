from flask import Flask
from os import path
from flask_cors import CORS

from modules.models import  db
from modules.auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = "notsosecretafterall"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'database.db')
app.register_blueprint(auth, url_prefix='/auth')

db.init_app(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)