# Run on first time install
import time, network, upip
from constants import env_dict

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(env_dict['ssid'], env_dict['password'])

# To let connection finish
time.sleep(3)

upip.install('micro-wifi-manager')
