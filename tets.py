from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
parameters = {
  'start': '1',
  'limit': '1',
  'convert': 'USD,BTC',
  'date': '2019-01-29',

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '9d0051fa-6435-44ab-8e28-15be0a598018',
}

investments = input("Input your money ")

month = input("Input your month ")

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)