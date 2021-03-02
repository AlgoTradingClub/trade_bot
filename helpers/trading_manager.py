import datetime
from models.mac1 import mac
from models.pairs1 import Pairs
from models.Order import Order
from datetime import date, datetime, timedelta
from helpers.order_reconciler import place_order

strategies = [
        mac,
        Pairs
    ]


# TODO implement an option to only run one or some of the strategies
def run_strategies(paper=True):
    """
    This runs all the strategies to get their calculated orders
    It compiles all the order in a list and hand this off to the order reconciler
    The order reconciler will remove redundancies and check that the order can be made
    """
    print("running")

    all_orders = []
    for obj in strategies:
        strat = obj()
        strat.before_trading()
        orders = strat.trade(date.today())
        all_orders.append(orders)
        strat.after_trading()

    print("Submitting Orders")
    place_order(all_orders, paper)
    print("Finished Running Strategies")


# TODO implement an option to only run one or some of the strategies
def run_backtest(start: str = "2020-01-01"
                 , end: str = date.today().strftime("%Y-%m-%d")):
    # TODO is there a way to consolidate this and the list above?

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    try:
        assert start <= end
    except AssertionError:
        print(f"The start date {start.strftime('%Y-%m-%d')} is after the end date{end.strftime('%Y-%m-%d')}")
        return

    diff = end - start

    results = []
    for obj in strategies:
        strat = obj()
        strat.before_trading()
        for i in range(diff.days + 1):
            day = start + timedelta(i)
            print(f"running strat {strat.__class__.__name__} for day {day.strftime('%Y-%m-%d')}")
            orders = strat.trade(day)
            # TODO do something with the order
        strat.after_trading()


