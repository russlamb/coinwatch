#!/usr/bin/env python
"""
Monitor coin mining activity using miningpoolhub API
"""

from pool_api import get_hashrate, get_coin_balance, get_debits
from price_api import get_bitcoin_price_index

def main():
    print(get_debits("ethereum"))
    print("ethereum balance: {}".format(get_coin_balance("ethereum")))
    print("moncoin hashrate: {}".format(get_hashrate()))
    print("ethereum hashrate: {}".format(get_hashrate("ethereum")))
    print("bitcoin balance: {}".format(get_coin_balance("bitcoin")))
    print("bitcoin price: {}".format(get_bitcoin_price_index()))
    print("USD equivalent: {}".format(get_bitcoin_price_index()*get_coin_balance("bitcoin")))

if __name__ == "__main__":
    main()
