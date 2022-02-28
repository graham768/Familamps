# Run on first time install
import upip
import network
import json
import time

f = open('env.json', mode="r+", encoding="utf-8")
env_dict = json.load(f)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(env_dict['ssid'], env_dict['password'])

time.sleep(3)

upip.install('micro-wifi-manager')

