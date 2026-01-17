def battery_to_mood(percent, charging=False):
    """Determine base mood from battery percent and charging state"""
    if charging and percent < 100:
        return "charging"

    if percent <= 10:
        return "sleepy"
    elif percent <= 20:
        return "very_tired"
    elif percent <= 40:
        return "low"
    elif percent <= 60:
        return "neutral"
    elif percent <= 80:
        return "energetic"
    elif percent < 100:
        return "hyper"
    else:
        return "unstoppable"


def apply_time_modifier(mood, time_modifier):
    """Adjust mood based on local time of day"""
    if time_modifier in ("night", "late"):
        if mood in ("energetic", "hyper"):
            return "neutral"
        if mood == "neutral":
            return "low"

    if time_modifier == "morning":
        if mood in ("sleepy", "very_tired"):
            return "low"

    return mood

