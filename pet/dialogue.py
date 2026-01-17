import random
import time

DIALOGUE = {
    "sleepy": [
        "five more minutes...",
        "zzz...",
        "why am i awake",
    ],
    "very_tired": [
        "i need coffee",
        "this is rough",
    ],
    "low": [
        "kinda tired tbh",
        "running on fumes",
    ],
    "neutral": [
        "just vibing",
        "hello :)",
    ],
    "energetic": [
        "i feel great!",
        "let's do stuff!",
    ],
    "hyper": [
        "GO GO GO",
        "ENERGY!!!",
    ],
    "unstoppable": [
        "I AM POWER",
        "NOTHING CAN STOP ME",
    ],
    "charging": [
        "charging up...",
        "juice acquired",
    ],
}

_last_change = 0
_current_line = ""

def get_dialogue(mood, interval=5):
    """Return a line of dialogue for the current mood, updated every `interval` seconds"""
    global _last_change, _current_line
    now = time.time()

    if now - _last_change > interval or not _current_line:
        _current_line = random.choice(DIALOGUE.get(mood, ["..."]))
        _last_change = now

    return _current_line

