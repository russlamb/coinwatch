import requests
import json

from utils import print_json


def get_url(limit=None):
    url = "https://api.coinmarketcap.com/v1/ticker/{}".format("?limit={}".format(limit)
                                                              if isinstance(limit, int) and limit > 0 else "")
    return url


def call_api(limit=None):
    url = get_url(limit)
    r = requests.get(url)
    return r


def print_cap_json():
    print_json(call_api(10).text)


def get_coin_property(coin, property):
    coinlist = json.loads(call_api().text)
    coin_state = [item for item in coinlist if item["id"] == coin or item["symbol"] == coin]
    return coin_state[0][property]


def get_coin_price(coin):
    return float(get_coin_property(coin, "price_usd"))


if __name__ == "__main__":
    print(get_coin_price("bitcoin"))
    print(get_coin_price("ethereum"))
    print_cap_json()
