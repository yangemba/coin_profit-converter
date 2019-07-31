import json
import requests
import argparse
import logging


def historical_value(data, index):
    return round(float(data['data'][index].get('priceUsd')), 1)


def count(money, date):
    url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'
    response = requests.get(url=url)
    data = json.loads(response.text)
    days = int(date) * 30
    # historical_index = len(data['data']) - days
    price = float(data['data'][-1]['priceUsd'])
    today_price = round(price, 1)
    bitcoin_purchase = [(float(money) / historical_value(data, x)) for x in
                        range((len(data['data']) - days),  len(data['data']), 30)]
    btc_qnt = 0
    # print([x for x in range((len(data['data']) - days),  len(data['data']), 30)])
    for i in bitcoin_purchase:
        btc_qnt = btc_qnt + i

    final_money = btc_qnt * today_price
    return round(btc_qnt, 3), round(final_money, 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--salary", help="Use this option to specify your salary.")
    parser.add_argument("-m", "--month", help="Use this option to specify amount of month less than 24 included.")
    args = parser.parse_args()

    money = args.salary
    date = args.month
    if int(date) > 24:
        raise ValueError("24 month is maximum!")
    logging.warning(f"Your profit would be {count(money, date)[0]} BTC and {count(money, date)[1]} USD")
