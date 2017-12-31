import requests
import json
import os

from utils import print_json


def get_address():
    return os.environ.get("ADDRESS_BITCOIN")

def get_url(address, action):
    url = "https://blockchain.info/q/{}/{}".format(action,address)
    print(url)
    return url

def call_api(action="addressbalance"):
    url = get_url(get_address(),action)
    r = requests.get(url)
    return r

def get_wallet_balance():
    balance = call_api().text
    return float(balance)*pow(10,-8) # balance is in satoshi units

if __name__=="__main__":
    print(call_api().text)
    print(get_wallet_balance())