from pool_api import get_hashrate, get_coin_balance
from price_api import get_bitcoin_price_index



def main():

    print("moncoin hashrate: {}".format(get_hashrate()))
    print("bitcoin balance: {}".format(get_coin_balance("bitcoin")))
    print("bitcoin price: {}".format(get_bitcoin_price_index()))
    print("USD equivalent: {}".format(get_bitcoin_price_index()*get_coin_balance("bitcoin")))

if __name__ == "__main__":
    main()
