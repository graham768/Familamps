from machine import Pin
from neopixel import NeoPixel
import time, _thread, network

class Light:

  def __init__(self, pinNum, numLeds, api_key) -> None:
    self.pin = Pin(pinNum, Pin.OUT)   # set pin to output to drive NeoPixels
    self.numLeds = numLeds
    self.leds = NeoPixel(pinNum, numLeds)
    self.api_key = api_key
    self.changeColor(127,127,127)
    _thread.start_new_thread(self.glowBlue)

  def changeColor(self, red, green, blue, delay_ms=3):
    if delay_ms:
      r_now, g_now, b_now = self.leds[0]
      while r_now != red and g_now != green and b_now != blue:
        for x in range(0, self.numLeds):
          r_now, g_now, b_now = self.leds[x]
          self.leds[x] = (seek(r_now, red), seek(g_now, green), seek(b_now, blue))
        time.sleep(delay_ms/1000)
        self.leds.write()
    else:
      for x in range(0, self.numLeds):
        self.leds[x] = (red, green, blue)
      self.leds.write()


  def blinkWhite(self, times=1, delay_ms=150):
    r_now, g_now, b_now = self.leds[0]

    for time in range(0, times):
      self.changeColor(255, 255, 255, delay_ms=0)
      time.sleep(delay_ms)
      self.changeColor(r_now, g_now, b_now, delay_ms=0)


  def blinkError(self):
    r_now, g_now, b_now = self.leds[0]

    for time in range(0, 2):
      self.changeColor(255, 0, 0, delay_ms=0)
      time.sleep(75)
      self.changeColor(255, 128, 0, delay_ms=0)
      time.sleep(75)

    self.changeColor(r_now, g_now, b_now, delay_ms=0)


  def glowBlue(self):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while not wlan.isconnected():
      self.changeColor(0, 0, 255, delay_ms=5)
      self.changeColor(0, 0, 60, delay_ms=5)


  def getColor(self):
    pass


  def postColor(self):
    pass

def seek(num, goal):
  if(num < goal):
    return num+1
  elif(num > goal):
    return num-1
  else:
    return num