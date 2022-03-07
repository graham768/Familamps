import urequests, json
from constants import ENV_DICT

baseUrl= f"{ENV_DICT['api_url']}?code={ENV_DICT['api_key']}"

def getColor():
  response = urequests.get(baseUrl)
  if response.status_code != 200:
    raise Exception("api get error")
  return json.loads(response.content)


def putColor(red, green, blue):
  url = f"{baseUrl}&red={red}&green={green}&blue={blue}"
  headers = {
    b'Content-Length': b'0'
  }
  response = urequests.put(url, headers=headers)
  if response.status_code != 200:
    raise Exception("api put error")
  return json.loads(response.content)


if __name__ == "__main__":
    response = getColor()
    print(response)