import psutil

def get_battery_percent():
    battery = psutil.sensors_battery()
    if battery is None:
        return 100
    return int(battery.percent)

def is_charging():
    battery = psutil.sensors_battery()
    if battery is None:
        return False
    return battery.power_plugged

