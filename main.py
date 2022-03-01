from microwifimanager.manager import *
from machine import TouchPad, Pin
from constants import *
from light import Light
import time, api


light = Light(LED_PIN, NUM_LEDS)

wlan = WifiManager(ssid="Familamp").get_connection()

if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        # fade red on/off until rebooted
        light.changeColor(127, 0, 0, delay_ms=5)
        light.changeColor(0, 0, 0, delay_ms=5)

time.sleep(2) # allow glowBlue thread to recognize connection
light.changeColor(0,0,0)


touchPin = TouchPad(Pin(TOUCH_PIN))
lastRequest = 0
while True:
    # Check for an update every 10 seconds
    if (time.time() - lastRequest) > 10:
        lastRequest = time.time()
        light.changeColor(*light.getColor())


    # TODO Capacitive touch reading
    if touchPin.read() > TOUCH_THRESHOLD:
        light.blinkWhite()
        try:
            resp = light.postColor(*light.leds[0])
            if resp.status_code != "200":
                light.blinkError()
                # TODO error logging
        except:
            light.blinkError()
            # TODO Error logging

