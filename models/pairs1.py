from Algo import Algorithm
from Order import Order


print("Running Pairs Trading Strategy 1 ...")


class Pairs(Algorithm):
    def before_trading(self) -> None:
        ...

    def trade(self) -> Order:
        ...

    def after_trading(self) -> None:
        ...


