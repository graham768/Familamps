import json

# There are ten capacitive touch-enabled pins that can be used on the ESP32: 0, 2, 4, 12, 13 14, 15, 27, 32, 33
TOUCH_PIN = 4
TOUCH_THRESHOLD = 200
NUM_LEDS = 12
LED_PIN = 2
COLOR = [120, 0, 165]
UPDATE_FILES = ['main.py', 'light.py', 'api.py', 'configure.py', 'constants.py', 'calibrate.py']
f = open('env.json', mode="r+", encoding="utf-8")
ENV_DICT = json.load(f)
