from datetime import datetime
from calendar import day_name, monthrange
from .models import History

def history_to_dict(history: History) -> dict:
    result = dict()
    result['id'] = history.id
    result['category'] = history.category
    result['amount'] = history.amount
    result['description'] = history.description
    result['datetime'] = datetime.fromisoformat(history.date_time).strftime('%Y/%m/%d %H:%M:%S')
    return result

def curr_month_name() -> str:
    return datetime.now().strftime('%B')

def day_of_curr_month(time: str) -> int:
    now = datetime.now()
    date = datetime.fromisoformat(time)
    if now.month == date.month and now.year == date.year:
        return date.day
    else:
        return None

def curr_month_len() -> int:
    now = datetime.now()
    range = monthrange(now.year, now.month)
    return range[1]