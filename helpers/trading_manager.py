import datetime
from models.mac1 import mac
from models.pairs1 import Pairs
from models.Order import Order
from datetime import date, datetime, timedelta


# TODO implement an option to only run one or some of the strategies
def run_strategies(paper=True):
    print("running")
    strategies = [
        mac(),
        Pairs()
    ]

    for strat in strategies:

        strat.before_trading()
        order = strat.trade(date.today())
        print("Doing something with the order. Checking with the portfolio checker to see if this is legit")
        print("Submitting Order")
        strat.after_trading()

    print("Finished Running Strategies")


# TODO implement an option to only run one or some of the strategies
def run_backtest(start: str = "2020-01-01"
                 , end: str = date.today().strftime("%Y-%m-%d")):
    # TODO is there a way to consolidate this and the list above?
    strategies = [
        mac(),
        Pairs()
    ]

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    try:
        assert start <= end
    except AssertionError:
        print(f"The start date {start.strftime('%Y-%m-%d')} is after the end date{end.strftime('%Y-%m-%d')}")
        return

    diff = end - start

    results = []
    for strat in strategies:
        for i in range(diff.days + 1):
            day = start + timedelta(i)
            print(f"running strat {strat.__class__.__name__} for day {day}")


