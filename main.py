from constants import *
from light import Light
import time, api, network, socket, re


light = Light(LED_PIN, NUM_LEDS)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ENV_DICT['ssid'], ENV_DICT['password'])
    while not wlan.isconnected():
        pass
print('network config: ', wlan.ifconfig())

time.sleep(3) # allow glowBlue thread to recognize wifi connection
light.changeColor(255,0,0)


port = 80
addr = socket.getaddrinfo('', port)[0][-1]
website = socket.socket()
website.bind(addr)
website.listen(1)


def send_color_picker(hexColor):
  client.sendall("HTTP/1.0 200 OK\r\n")
  client.sendall("Content-Type: text/html\r\n")
  client.sendall("\r\n")
  client.sendall(f"""\
    <form action="/" method="post">
      <input type="color" name="color" value="#{hexColor}" style="width:100%; height:50vh">
      <input type="submit" style="width:100%; display:block; text-align:center; height:30vh; font-size: 60px;">
    </form>
      """)


hexColor = 'ff0000'
while True:
  client, addr = website.accept()
  print('client connected from', addr)
  try:
    client.settimeout(5.0)

    request = b""
    try:
      while "\r\n\r\n" not in request:
          request += client.recv(512)
    except OSError:
      pass

    print("Request is: {}".format(request))
    if "HTTP" not in request:  # skip invalid requests
      continue

    match = re.search("color=([^&]*)", request)
    if match:
      hexColor = match.group(1).decode("utf-8").lstrip('%23')
      light.changeColorHex(hexColor)

    send_color_picker(hexColor)

  finally:
      client.close()