# 🐾 Terminal Pet

A Linux-only terminal pet that reacts to:
- 🔋 Battery level
- 🕒 Time of day
- ⚡ Charging state
- 💬 Random dialogue

## Features
- ASCII animations
- Time-of-day behavior
- Random dialogue
- Linux-native, no GUI
- Works on all major distros

---

## Installation & Run

### Option 1: Run via launcher script (no pip needed)

Clone the repo:
`git clone https://github.com/BreadBoi0612/terminal-pet.git`

Copy the launcher to your PATH:
`mkdir -p ~/.local/bin
cp terminal-pet/scripts/pet ~/.local/bin/pet
chmod +x ~/.local/bin/pet`

Run the pet from anywhere:
`pet`

### Option 2: Install via pip (recommended)

Clone the repo:

`git clone https://github.com/BreadBoi0612/terminal-pet.git
cd terminal-pet`


Install the package:

`pip install --user -e`


Run from anywhere:

`pet`

---

### Controls

Q — Quit

---

## Requirements

-Python 3.8+

-Linux (no Windows/macOS)

-pip3 (optional; auto-installable via launcher script)
