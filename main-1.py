from microwifimanager.manager import *
from machine import TouchPad, Pin, reset
from constants import *
from light import Light
from senko import Senko
import time, api


try:

    light = Light(LED_PIN, NUM_LEDS)
    touchPin = TouchPad(Pin(TOUCH_PIN))
    OTA = Senko(user="graham768", repo="Familamps", files = UPDATE_FILES)

    wlan = WifiManager(ssid="Familamp").get_connection()

    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            # fade red on/off until rebooted
            light.changeColor(127, 0, 0, delay_ms=5)
            light.changeColor(0, 0, 0, delay_ms=5)

    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        reset()

    time.sleep(1) # allow glowBlue thread to recognize wifi connection
    light.changeColor(*api.getColor())


    lastRequest = 0
    failCount = 0
    while True:
        time.sleep(1)
        try:
            # Check for an update every 10 seconds
            if (time.time() - lastRequest) > 10:
                # TODO WDT
                lastRequest = time.time()
                light.changeColor(*api.getColor())


            if touchPin.read() < TOUCH_THRESHOLD:
                print("I'm touched!")
                light.blinkWhite()
                light.changeColor(*COLOR)
                resp = api.putColor(*COLOR)
                    
        except Exception:
            light.blinkError()
            failCount += 1
            if failCount >= 5:
                raise
            
except Exception:
    # TODO Error logging
    # reset()
    raise