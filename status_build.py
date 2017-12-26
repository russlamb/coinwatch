from market_cap_api import get_coin_price
from pool_api import get_coin_balance, get_hashrate


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
        for f in functions:
            status.append(get_status("{} {}".format(c, f), functions[f](c)))
    return status


def get_status(status, status_value):
    return {
        "status": status,
        "status_value": status_value
    }


if __name__ == "__main__":
    print(build_status())
