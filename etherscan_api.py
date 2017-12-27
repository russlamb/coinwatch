import requests
import json
import os

from utils import print_json

def get_api_key():
    return os.environ.get("APIKEY_ETHERSCAN")

def get_address():
    return os.environ.get("ADDRESS_ETHEREUM")

def get_url(address, action):
    url = "https://api.etherscan.io/api?module=account&action={}&address={}&tag=latest&apikey={}".format(action,
        address, get_api_key()
    )
    print(url)
    return url


def call_api(action="balance"):
    url = get_url(get_address(),action)
    r = requests.get(url)
    return r

def get_wallet_balance():
    walletdict = json.loads(call_api().text)
    return float(walletdict["result"])/pow(10,18)

if __name__=="__main__":
    print_json(call_api().text)
    print(get_wallet_balance())