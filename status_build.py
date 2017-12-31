from market_cap_api import get_coin_price
from pool_api import get_coin_balance, get_hashrate
from etherscan_api import get_wallet_balance
from blockchain_api import get_wallet_balance as btc_balance
from utils import print_json
import json

def usd_value(coin):
    balance = get_coin_balance(coin)
    price = get_coin_price(coin)
    if isinstance(balance, (int, float)) and isinstance(price, (int, float)):
        return round(balance * price, 2)
    else:
        return None


def build_status():
    status = []
    coins = ["ethereum", "bitcoin", "monacoin"]
    functions = {
        "balance": get_coin_balance,
        "hashrate": get_hashrate,
        "price": get_coin_price,
        "USD value": usd_value
    }

    for c in coins:
        coin_status = []
        for f in functions:
            coin_status.append(get_status("{}".format(f), functions[f](c)))

        #call specific one off functions by coin
        if c=="ethereum":
            wallet_balance=get_wallet_balance()
            coin_status.append(get_status("wallet balance", wallet_balance ))
            coin_status.append(get_status("wallet USD", round(wallet_balance*get_coin_price(c),2)))

        if c=="bitcoin":
            wallet_balance = btc_balance()
            coin_status.append(get_status("wallet balance", wallet_balance))
            coin_status.append(get_status("wallet USD", round(wallet_balance * get_coin_price(c), 2)))
        status.append({
            "coin":c,
            "state":coin_status
        })
    return status


def get_status(status, status_value):
    return {
        "status": status,
        "status_value": status_value
    }


if __name__ == "__main__":
    for i in build_status():
        print_json(json.dumps(i))
