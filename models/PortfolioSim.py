from typing import List


class Transaction:
    def __init__(self, symbol, price, buy_or_sell, o_type):
        assert isinstance(symbol, str)
        self.symbol = symbol
        assert isinstance(price, float)
        self.price = round(price, 2)
        assert buy_or_sell in {"buy", "sell", "short"}
        self.buy_or_sell = buy_or_sell.upper()
        assert o_type in {"market", "limit"}
        self.o_type = o_type

    def __str__(self):
        return f"T: {self.buy_or_sell}({self.o_type}) of {self.symbol} @ ${self.price}"


class Asset:
    def __init__(self, symbol, bought_at, shares):
        assert isinstance(symbol, str)
        assert isinstance(bought_at, float)
        assert isinstance(shares, float)

        self.symbol = symbol
        self.bought_at = bought_at
        self.shares = shares

    def average(self, shares, bought_price):
        self.bought_at = ((self.bought_at * self.shares) + (shares * bought_price)) / (shares + self.shares)
        self.shares += shares

    def partial_sell(self, shares):
        assert shares < self.shares
        self.shares -= shares

    def __str__(self):
        return f"{self.shares} of {self.symbol}. Average Cost: {self.bought_at}"


class Portfolio:
    """
    Keeps track of the information of my portfolio during a backtest.
    Does its best to mimic the restrictions present during paper/ live trading
    """
    def __init__(self, cash=10000.00):
        self.starting_cash = cash
        self.cash = float(cash)
        self.current_day = ""
        self.assets = []
        """
        List<Asset>
        """
        self.transactions = {}
        '''
        '2020-01-01': List<Transaction>
        '''
        self.day_trades = 0

    def place_backtest_order(self, order: List) -> bool:
        ...

    def get_current_portfolio_price(self) -> float:
        return self.cash

    def results(self) -> str:
        s = "*"*20 + "Results for Backtest" + "*"*20 + "\n"
        s += f"Starting Cash: {self.starting_cash};  Ending Cash: {self.cash}\n"
        curr = self.get_current_portfolio_price()
        change = (curr + self.cash) * 100 / self.starting_cash
        s += f"Current Portfolio Price (not including cash): {curr};  Total % Change: {change}\n"
        s += "*"*20 + "Current Assets:" + "*"*20 + "\n"
        for asset in self.assets:
            s += f"\t-{str(asset)}\n"

        s += "*"*20 + "All Transaction: " + "*"*20 + "\n"
        for trans in self.transactions:
            s += f"\t-{str(trans)}\n"

        s += "*"*50
        return s
