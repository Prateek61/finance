from flask import Blueprint, request, jsonify, make_response
import jwt
import uuid
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from sqlalchemy.exc import IntegrityError

from app import db
from .models import User


auth = Blueprint('auth', __name__)
secret_key = 'notsosecretafterall'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'no token'}), 401
        
        try:
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        else:
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            if not current_user:
                return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    
    return decorated


@auth.route('/users')
def users():
    users = User.query.all()

    output = list()
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        output.append(user_data)
    return jsonify({'users': output})


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already taken', 'register_status': 'fail'})
    return jsonify({'message': 'user created', 'register_status': 'success'})


@auth.route('/login')
def login():
    auth = request.authorization
    error = {'login_status': 'fail', 'message': 'incorrect username or password'}

    if not auth or not auth.username or not auth.password:
        return  make_response({'message': 'khate credentials ramrari han', 'login_status': 'fail'}, 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})

    user = User.query.filter_by(username=auth.username).first()
    if not user:
        return jsonify(error)

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=30)}, secret_key, algorithm='HS256')

        return jsonify({'token': token, 'user': {'username': user.username, 'public_id': user.public_id}, 'login_status': 'success'})
    
    return jsonify(error)