import json

import os
import requests

from utils import print_json, value_search


def get_api_key():
    return os.environ["APIKEY_MININGPOOLHUB"]


def call_api(action, coin_name=None, id=None):
    url = get_url(action, coin_name, id)
    r = requests.get(url)
    return r


def get_url(action, coin_name=None, i=None):
    id_url = "" if (i is None or "" == i) else "&id={}".format(i)
    coin_name_url = "" if coin_name is None else "{}.".format(coin_name)
    api_key = get_api_key()
    url = r"https://{}miningpoolhub.com/index.php?page=api&action={}&api_key={}{}".format(
        coin_name_url, action, api_key, id_url)
    return url


def get_hashrate(coin="monacoin"):
    dashdict = json.loads(call_api("getdashboarddata", coin).text)
    return dashdict["getdashboarddata"]["data"]["raw"]["personal"]["hashrate"]


def get_transactions(coin):
    paydict = json.loads(call_api("getusertransactions", coin, os.environ.get("USERID_MININGPOOLHUB")).text)
    return paydict["getusertransactions"]["data"]["transactions"]


def print_transaction():
    print_json(call_api("getusertransactions", "ethereum", os.environ.get("USERID_MININGPOOLHUB")).text)


def get_debits(coin):
    trans = [i for i in get_transactions(coin) if not i["type"].startswith("Credit")]
    return trans


def print_dashboard_json():
    print_json(call_api("getdashboarddata", "monacoin").text)


def print_bitcion_json():
    print_json(call_api("getdashboarddata", "bitcoin").text)


def print_transaction_json():
    print_json(call_api("getusertransactions", "ethereum").text)


def print_balance_json():
    print_json(call_api("getuserallbalances").text)


def get_coin_balance(coin_name="bitcoin"):
    dashdict = json.loads(call_api("getuserallbalances").text)
    coin_balances = dashdict["getuserallbalances"]["data"]
    for i in coin_balances:
        if i["coin"] == coin_name:
            return i["confirmed"]

    return None
