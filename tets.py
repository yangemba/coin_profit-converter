from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests

url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
response = requests.get(url=url)
# print(response.text)
data = json.loads(response.text)
# money = input("please input your money:")
# correct = False
#
# while True:
#   try:
#     date = int(input("please input qnt of mouth(Integer, 0 < 24): "))
#   except Exception as e:
#     print(f"{e}")
#     continue
#   if int(date) <= 24:
#     break
money = 5000
date = 4

days = int(date) * 30
historical_index = len(data['data']) - days
price = float(data['data'][-1]['priceUsd'])
today_price = round(price, 0)
print(data['data'][historical_index]['priceUsd'])

historical_price = round(float(data['data'][historical_index]['priceUsd']), 0)
final_money = (int(money) * today_price) / historical_price
print(final_money)


















