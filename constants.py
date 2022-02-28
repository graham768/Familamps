import json

# There are ten capacitive touch-enabled pins that can be used on the ESP32: 0, 2, 4, 12, 13 14, 15, 27, 32, 33
TOUCH_PIN = 14
TOUCH_THRESHOLD = 500 # TODO test thresholds
NUM_LEDS = 12
LED_PIN = 0
f = open('env.json', mode="r+", encoding="utf-8")
env_dict = json.load(f)