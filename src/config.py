"""Configuration module for Pymath calculator."""

import os

# Directory paths
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOUNDS_DIR = os.path.join(CURRENT_DIR, "sounds")
IMAGES_DIR = os.path.join(CURRENT_DIR, "images")

# Sound file paths
MUSIC_PATH = os.path.join(SOUNDS_DIR, "background_music..wav")
CLICK_SOUND_PATH = os.path.join(SOUNDS_DIR, "click.wav")
DEVIL_SOUND_PATH = os.path.join(SOUNDS_DIR, "devil.wav")
SOUNDTRACK_PATH = os.path.join(SOUNDS_DIR, "soundtrack.mp3")

# Icon path
ICON_PATH = os.path.join(IMAGES_DIR, "pyculator.png")

# UI Colors
COLORS = {
    'background': '#49769e',
    'button_primary': '#4B8BBE',
    'button_secondary': '#ffe483',
    'entry_bg': '#ffe483',
    'entry_fg': '#306998',
    'label_bg': '#306998',
    'label_fg': 'white',
    'red': 'red',
    'red_button': '#ff4444',
    'red_entry': '#ffcccc',
    'red_label': '#cc0000',
    'pink': '#ff69b4'
}

# Button configuration
BUTTON_STYLE = {
    'font': ('Consolas', 14, 'bold'),
    'width': 10,
    'height': 3,
    'relief': 'flat',
    'bd': 0,
    'padx': 10,
    'pady': 5,
    'cursor': 'hand2'
}

# Calculator button layout
BUTTON_LAYOUT = [
    ('C', 2, 0), ('/', 2, 1), ('*', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('=', 4, 3),
    ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('0', 5, 3)
]

# Special buttons that use secondary color
SPECIAL_BUTTONS = {'C', '/', '*', '-', '+', '=', '0'}

# Icon sizes for multi-resolution support
ICON_SIZES = [(32, 32), (48, 48), (64, 64), (128, 128), (256, 256), (512, 512)]

# Easter egg expressions
EASTER_EGGS = {
    "666+666": {
        'message': "YOU ARE NOW FATED TO ETERNAL DAMNATION",
        'warning': "YOU HAVE SUMMONED THE DARK FORCES!",
        'color': 'red'
    },
    "1+1": {
        'message': "Never gonna give you up!",
        'url': "https://youtu.be/dQw4w9WgXcQ?si=7SmsRcslz8fYpWkZ",
        'color': '#ff69b4'
    }
}