Coinwatch
=========

Overview
--------

This is a personal project I put together to view my current crypto coin balances for my mining pools and wallets.

The structure is a simple python Flask web site that displays HTML tables for each cryptocurrency I am mining or owning.

I currently host this for my personal use on heroku. Others could easily follow suit. Since the wallet addresses are configuration values stored in environment variables, this project could easily be reused by anyone with cryptocurrency.

APIs Used
--------

|    API                  |    Purpose                                          |   |
|-------------------------|-----------------------------------------------------|---|
|    Blockchain.info      |    Bitcoin   wallet balance                         |   |
|    Etherscan.io         |    Ehter   wallet balance                           |   |
|    Coinmarketcap.com    |    Coin   prices                                    |   |
|    Miningpoolhub.com    |    Mining   hash speeds and pool wallet balances    |   |
|    Colindesk.com        |    Bitcoin   prices                                 |   |
