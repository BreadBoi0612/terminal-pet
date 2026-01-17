import curses
import time

from pet.system import get_battery_percent, is_charging
from pet.moods import battery_to_mood, apply_time_modifier
from pet.animations import FRAMES, SPEED
from pet.timeofday import get_time_modifier
from pet.dialogue import get_dialogue


def run():
    curses.wrapper(main)


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    frame = 0

    while True:
        stdscr.clear()

        battery = get_battery_percent()
        charging = is_charging()

        base_mood = battery_to_mood(battery, charging)
        time_mod = get_time_modifier()
        mood = apply_time_modifier(base_mood, time_mod)

        frames = FRAMES[mood]
        speed = SPEED[mood]

        pet = frames[frame % len(frames)]
        line = get_dialogue(mood)

        stdscr.addstr(2, 4, pet)
        stdscr.addstr(4, 4, f"💬 {line}")
        stdscr.addstr(6, 4, f"Battery: {battery}%")
        stdscr.addstr(7, 4, f"Mood: {mood}")
        stdscr.addstr(8, 4, f"Time: {time_mod}")
        stdscr.addstr(10, 4, "Press Q to quit")

        stdscr.refresh()
        frame += 1

        time.sleep(speed)

        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            break


if __name__ == "__main__":
    run()

