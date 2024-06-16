def format_date(date):
    return date.strftime('%Y-%m-%d')

def get_current_time():
    from datetime import datetime
    return datetime.utcnow()