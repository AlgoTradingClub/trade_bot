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
        to_remove = set()
        for i in range(len(orders) - 1):
            for j in range(i + 1, len(orders)):
                if j in to_remove:
                    continue
                elif (orders[i].asset == orders[j].asset) and (orders[i].order_type == orders[j].order_type) \
                        and orders[i].notional == '0.0' and orders[j].notional == '0.0':
                    # condense
                    i_sign = -1 if orders[i].side == 'sell' else 1
                    j_sign = -1 if orders[j].side == 'sell' else 1
                    i_qty = i_sign * orders[i].qty
                    j_qty = j_sign * orders[j].qty
                    total_qty = i_qty + j_qty
                    orders[i].side = 'sell' if total_qty < 0 else 'buy'
                    orders[i].qty = abs(total_qty)
                    to_remove.add(j)

        k = 0
        while k < len(orders):
            if k in to_remove:
                orders.pop(k)
            else:
                k += 1

        # TODO check account

        # TODO convert Order to alpaca format

        return orders

    def backtest_orders(self, orders: List[Order]) -> List[Order]:
        return self.__check_orders(orders)

    def place_order(self, orders: List[Order]):
        """
        Only for the trade function and not the backtester
        """
        orders = self.__check_orders(orders)

        for o in orders:
            o.send_to_alpaca(paper=self.paper)