from models.Algo import Algorithm
from models.Order import Order


print("Running Moving Average Crossover Strategy 1...")


class mac(Algorithm):
    def before_trading(self) -> None:
        ...

    def trade(self) -> Order:
        ...

    def after_trading(self) -> None:
        ...


