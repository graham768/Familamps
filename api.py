import urequests
from constants import ENV_DICT


def getColor():
  url = f"https://familamps-api.azurewebsites.net/api/GetColor?code={ENV_DICT['api_key']}"
  return urequests.get(url)


def putColor(red, green, blue):
  url = f"https://familamps-api.azurewebsites.net/api/PutColor?code={ENV_DICT['api_key']}&red={red}&green={green}&blue={blue}"
  headers = {
    "Content-Length": 0
  }
  return urequests.put(url, headers=headers)