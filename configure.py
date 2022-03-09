# Run on first time install
import time, network, upip
from constants import ENV_DICT

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ENV_DICT['ssid'], ENV_DICT['password'])
time.sleep(3)

# Install Dependencies
upip.install('micro-wifi-manager')
upip.install('urequests')
upip.install('micropython-senko')