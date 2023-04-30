from flask import Blueprint, jsonify, request

from app import db
from .models import User, History
from .auth import token_required
from .helper import history_to_dict, day_of_curr_month, curr_month_len, curr_month_name

home = Blueprint('home', __name__)


@home.route('/history')
@token_required
def history(current_user: User):
    user_history = History.query.filter_by(user_id=current_user.id)
    user_history_json = []

    for item in user_history:
        user_history_json.append(history_to_dict(item))
    
    return jsonify({'status': 'success', 'history': user_history_json})


categories = ["food", "transport", "rent", "health"]
@home.route('/add', methods=['POST'])
@token_required
def add_to_history(current_user: User):
    data = request.get_json()
    if (not data or not data['amount'] or not data['category'] or not data['description']):
        return jsonify({'status': 'fail', 'message': 'invalid form'})

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
def get_category(current_user: User):
    return jsonify({'categories': categories})


@home.route('/getuser', methods=['GET'])
@token_required
def get_user(current_user: User):
    return jsonify({'user': {'username': current_user.username, 'public_id': current_user.public_id}})


@home.route('/bargraph')
@token_required
def bargraph(current_user: User):
    data = History.query.filter_by(user_id=current_user.id)
    chart_data = [0] * curr_month_len()
    total = 0
    for item in data:
        month = day_of_curr_month(item.date_time)
        if (month):
            chart_data[month - 1] += item.amount
            total += item.amount

    return jsonify({'chartData': chart_data, 'monthName': curr_month_name(), 'total': total})


@home.route('/piechart')
@token_required
def piechart(current_user: User):
    data = History.query.filter_by(user_id=current_user.id)
    chart_data = dict()
    total = 0
    for item in data:
        total += item.amount
        if item.category in chart_data:
            chart_data[item.category] += item.amount
        else:
            chart_data[item.category] = item.amount
    
    return jsonify({'chartData': chart_data, 'total': total})