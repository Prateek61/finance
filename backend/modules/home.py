from flask import Blueprint, jsonify, request

from app import db
from .models import User, History
from .auth import token_required
from .helper import history_to_dict

home = Blueprint('home', __name__)

@home.route('/history')
@token_required
def history(current_user):
    user_history = History.query.filter_by(user_id=current_user.id)
    user_history_json = []

    for item in user_history:
        user_history_json.append(history_to_dict(item))
    
    return jsonify({'status': 'success', 'history': user_history_json})


categories = ["food", "transport", "rent", "health"]
@home.route('/add', methods=['POST'])
@token_required
def add_to_history(current_user):
    data = request.get_json()

    try:
        amount = int(data['amount'])
    except:
        return jsonify({'status': 'fail', 'message': 'invalid amount'})
    else:
        if (amount < 0):
            return jsonify({'status': 'fail', 'message': 'invalid amount'})
        if (data['category'] not in categories):
            return jsonify({'status': 'fail', 'message': 'invalid category'})

    new_item = History(category=data['category'], amount=amount, description=data['description'], user_id = current_user.id)

    try:
        db.session.add(new_item)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'status': 'fail', 'message': 'could not add to database'})
    
    return jsonify({'status': 'success', 'message': 'added'})


@home.route('/getcategories')
@token_required
def get_catrgory(current_user):
    return jsonify(categories)

@home.route('/getuser', methods=['GET'])
@token_required
def get_user(current_user):
    return jsonify({'user': {'username': current_user.username, 'public_id': current_user.public_id}})