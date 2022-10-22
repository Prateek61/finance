from .models import History

def history_to_dict(history):
    result = {}
    result['id'] = history.id
    result['category'] = history.category
    result['amount'] = history.amount
    result['description'] = history.description
    return result