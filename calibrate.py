import time



def calibrateTouch(light, touchPin):
    light.changeColor(127,127,127, delay_ms=0)
    untouchedReading = getMedianReading(touchPin)
    light.changeColor(225,225,0, delay_ms=0)
    threshold = getThreshold(touchPin, untouchedReading)
    light.changeColor(127,127,127, delay_ms=0)
    return threshold



def getMedianReading(touchPin, time_sec=5):
    readings = []
    secondsToRead = time.time() + time_sec
    while time.time() < secondsToRead:
        time.sleep(0.1)
        readings.append(touchPin.read())
    # find median integer
    s = sorted(readings)
    n = len(readings)
    index = (n - 1) // 2
    if (n % 2): # odd numbered list
        return s[index]
    else:
        return (s[index] + s[index + 1])/2


def getThreshold(touchPin, untouchedReading):
    
    untouchedTolerance = untouchedReading*.90 
    while touchPin.read() >= untouchedTolerance:
        time.sleep(0.1)

    threshold = getMedianReading(touchPin, 3)
    thresholdWithTolerance = threshold+untouchedReading/2
    
    return thresholdWithTolerance



if __name__ == "__main__":
    from light import Light
    from constants import *
    from machine import TouchPad, Pin

    light = Light(LED_PIN, NUM_LEDS)
    touchPin = TouchPad(Pin(TOUCH_PIN))

    threshold = calibrateTouch(light, touchPin)
    print("Threshold: "+ str(threshold))