from datetime import datetime
from calendar import day_name
from .models import History

def history_to_dict(history: History) -> dict:
    result = dict()
    result['id'] = history.id
    result['category'] = history.category
    result['amount'] = history.amount
    result['description'] = history.description
    result['datetime'] = datetime.fromisoformat(history.date_time).strftime('%Y/%m/%d %H:%M:%S')
    return result

def get_week(time: str) -> str:
    return day_name[datetime.fromisoformat(time).weekday()]