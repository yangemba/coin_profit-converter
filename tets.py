from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import argparse
import logging


def historical_value(data, index):
    return round(float(data[index]['priceUsd']), 1)


def count(money, date):
    url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
    response = requests.get(url=url)
    # print(response.text)
    data = json.loads(response.text)
    days = int(date) * 30
    historical_index = len(data['data']) - days
    price = float(data['data'][-1]['priceUsd'])
    today_price = round(price, 1)
    #print(data['data'][historical_index]['priceUsd'])
    bitcoin_purchaise = [money / historical_value(data['data'], x) for x in range(len(data['data']), len(data['data']) - days)]
    btc_qnt = 0
    for i in bitcoin_purchaise:
        print(i)
    historical_price = historical_value(data['data'], historical_index)
    final_money = btc_qnt * today_price
    return btc_qnt, final_money


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--salary", help="Use this option to specify the domain or IP to scan.")
    parser.add_argument("-m", "--month", help="Use this option to specify the domain or IP to scan.")
    args = parser.parse_args()

    money = args.salary
    date = args.month
    logging.warning(f"Your profit would be {count(money, date)[0]} BTC and {count(money, date)[1]} USD")
