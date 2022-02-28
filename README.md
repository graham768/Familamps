# Familamps

# Installation

- This library expects MicroPython installed on your microcontroller. For a guide for ESP32 boards, see [Getting started with MicroPython on the ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
- Rename `env.json.example` to `env.json` and include your local WiFi details for the initial library configuration. If you have your database's api key, you can add it here now as well.
- Update all of the constants in `constants.py` to reflect your GPIO pins, number of leds, and capacitive touch threshold (see below for this value)
- Upload the repository to each of your microcontrollers and run `configure.py` to install [MicroWifiManager](https://github.com/graham768/MicroWiFiManager) for fast, intuitive WiFi configuration on deployed boards (from here, your WiFi credentials are no longer needed if you want to remove them from the board).
- In MicroPython, `main.py` runs automatically when the microcontroller is power on. The light will look for an update every 10 seconds by default and if the capacitive touch threshold is passed, will post an updated.



# Capacitive Touch Threshold

Your capacitive touch values will vary based on a number of factors, so it's best to measure these yourself. To do this, you can run the following script while touching and untouching your capacitive area and monitoring the output:

```python
from machine import TouchPad, Pin

touchPin = TouchPad(Pin(<your-GPIO-pin>))

while True:
  print(touchPin.read())
```
