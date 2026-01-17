from datetime import datetime

def get_time_modifier():
    """Return time-of-day category based on local hour"""
    hour = datetime.now().hour

    if 0 <= hour <= 5:
        return "night"
    elif 6 <= hour <= 9:
        return "morning"
    elif 10 <= hour <= 17:
        return "day"
    elif 18 <= hour <= 21:
        return "evening"
    else:
        return "late"

