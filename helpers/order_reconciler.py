from models.Order import Order
from models.settings import Settings
from typing import List
import os


def place_order(order: List[Order], paper=True, backtest=False):
    """
    Only for the trade function and not the backtester
    """
    # TODO order reconciler
    """
    - check to see for any redundancies
        i.e. if one order wants to sell BTC and another order wants to buy BTC, condense that down into one
        break if theres any issues with the order type (limit. market)
        
    - check to see if we have the cash to buy or the assets to sell
    
    - execute the orders in alpaca
    """
    key_names = Settings.keys_names
    if paper:
        key_id = key_names["Alpaca Paper Key ID"]
        secret_key = key_names["Alpaca Paper Secret Key"]
    else:
        key_id = key_names["Alpaca Live Key ID"]
        secret_key = key_names["Alpaca Live Secret Key"]

    key_id = os.environ[key_id]
    secret_key = os.environ[secret_key]

    # TODO check redundancies

    # TODO check account

    # TODO convert Order to alpaca format

    # TODO place order