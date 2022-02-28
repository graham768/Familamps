from microwifimanager.manager import *
from machine import TouchPad, Pin
from constants import *
from light import Light
import time

# TODO Turn on neopixel
light = Light(LED_PIN, NUM_LEDS, env_dict['api_key'])


wlan = WifiManager(ssid="Familamp").get_connection()

if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D



touchPin = TouchPad(Pin(TOUCH_PIN))
lastRequest = 0
while True:
    # Check for an update every 10 seconds
    if(time.time() - lastRequest > 10):
        lastRequest = time.time()
        light.changeColor(*light.getColor())


    # TODO Capacitive touch reading
    if(touchPin.read() > TOUCH_THRESHOLD):
        light.blinkWhite()
        try:
            light.postColor(*light.leds[0])
        except:
            light.blinkError()
            # TODO Error logging

