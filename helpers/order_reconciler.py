from trade_bot.models.Order import Order
from trade_bot.models.settings import Settings
from typing import List
import os


class OrderReconciler:
    def __init__(self, paper=True):
        self.paper = paper

    def __check_orders(self, orders: List[Order]) -> List[Order]:
        """
                - check to see for any redundancies
                    i.e. if one order wants to sell BTC and another order wants to buy BTC, condense that down into one
                    break if theres any issues with the order type (limit. market)

                - check to see if we have the cash to buy or the assets to sell

                - execute the orders in alpaca
                """
        # TODO check redundancies

        # TODO check account

        # TODO convert Order to alpaca format

        return []

    def backtest_orders(self, orders: List[Order]) -> List[Order]:
        return self.__check_orders(orders)

    def place_order(self, orders: List[Order]):
        """
        Only for the trade function and not the backtester
        """
        orders = self.__check_orders(orders)

        for o in orders:
            o.send_to_alpaca(paper=self.paper)