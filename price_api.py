import requests
import json

from utils import print_json
from datetime import datetime
from collections import OrderedDict


def get_url(currency="USD"):
    url = "https://api.coindesk.com/v1/bpi/currentprice/{}.json".format(currency)
    return url


def get_url_history(start, end, currency="USD"):
    start_string = start.strftime('%Y-%m-%d')
    end_string = end.strftime('%Y-%m-%d')
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}&currency={}".format(
        start_string, end_string, currency)
    print(url)
    return url


def call_api(currency):
    url = get_url(currency)
    r = requests.get(url)
    return r


def call_api_history(start, end):
    url = get_url_history(start, end)
    r = requests.get(url)
    return r


def get_bitcoin_price_index():
    d = json.loads(call_api("USD").text)
    return d["bpi"]["USD"]["rate_float"]


def get_bitcoin_price_history(start, end):
    d = json.loads(call_api_history(start, end).text)
    return d["bpi"]


def print_bitcoin_json():
    print_json(call_api("USD").text)


def print_history_json():
    print_json(
        call_api_history(datetime.strptime("2017-09-01", "%Y-%m-%d"), datetime.strptime("2017-12-22", "%Y-%m-%d")).text)


if __name__ == "__main__":
    print_history_json()
    print(get_bitcoin_price_index())
    print(get_bitcoin_price_history(datetime.strptime("2017-09-01", "%Y-%m-%d"),
                                    datetime.strptime("2017-12-22", "%Y-%m-%d")))
