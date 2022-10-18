from flask import Flask, jsonify
from os import path
from flask_cors import CORS

from modules.models import  db
from modules.auth import auth, token_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "notsosecretafterall"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'database.db')
app.register_blueprint(auth, url_prefix='/auth')

db.init_app(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/getuser', methods=['GET'])
@token_required
def get_user(current_user):
    return jsonify({'user': {'username': current_user.username, 'public_id': current_user.public_id}})