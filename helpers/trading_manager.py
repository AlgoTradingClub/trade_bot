import datetime
from models.mac1 import mac
from models.pairs1 import Pairs
from models.Order import Order


def run_strategies(paper=True):
    strategies = [
        mac(),
        Pairs()
    ]

    for strat in strategies:

        strat.before_trading()
        order = strat.trade()
        print("Doing something with the order. Checking with the portfolio checker to see if this is legit")
        print("Submitting Order")
        strat.after_trading()

    print("Finished Running Strategies")


def run_backtest(start: str = "2020-01-01"
                 , end: str = datetime.date.today().isoformat()):
    ...

