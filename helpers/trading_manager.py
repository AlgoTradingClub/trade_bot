import datetime
from models.algos.mac1 import MAC as mac1
from models.algos.pairs1 import Pairs as pairs1
from models.algos.mac2_btc import MAC2
from datetime import datetime, timedelta
from helpers.order_reconciler import OrderReconciler
from models.PortfolioSim import Portfolio
from models.Algo import Algorithm
from models.Context import Context
import logging
logger = logging.getLogger(__name__)


strategies = [
        mac1,
        pairs1,
        MAC2
    ]


# TODO implement an option to only run one or some of the strategies
def run_strategies(paper=True):
    """
    This runs all the strategies to get their calculated orders
    It compiles all the order in a list and hand this off to the order reconciler
    The order reconciler will remove redundancies and check that the order can be made
    """
    print("Running...")

    all_orders = []
    first_trading_day = last_trading_day = datetime.today()
    context = Context()
    for obj in strategies:
        strat = obj()
        try:
            assert isinstance(strat, Algorithm)
        except AssertionError:
            logger.error(f"The strat, {strat.__class__.__name__}, is not a child instance of Algorithm")
            exit(1)
        strat.before_trading(first_trading_day, last_trading_day)
        orders = strat.trade(datetime.today(), context)
        assert isinstance(orders, list)
        all_orders += orders
        strat.after_trading()

    print("Submitting Orders...")
    o_r = OrderReconciler(paper)
    o_r.place_order(all_orders)
    logger.info(f"Date: {datetime.today().isoformat()}")
    for o in all_orders:
        logger.warning(f"Order Made. Type={'PAPER' if paper else 'LIVE'} {str(o)}")
    print("Finished Running Strategies")


# TODO implement an option to only run one or some of the strategies
def run_backtest(start: str = "2020-01-01"
                 , end: str = datetime.today().strftime("%Y-%m-%d")
                 , cash: float = 10000.00):

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    try:
        assert start <= end
    except AssertionError:
        print(f"The start date {start.strftime('%Y-%m-%d')} is after the end date{end.strftime('%Y-%m-%d')}")
        return

    diff = end - start

    results = []
    portfolio = Portfolio(cash)
    o_r = OrderReconciler()
    context = Context()
    my_objs = [obj() for obj in strategies]

    for i in range(diff.days + 1):
        day = start + timedelta(i)
        orders = []
        for strat in my_objs:
            try:
                assert isinstance(strat, Algorithm)
            except AssertionError:
                logger.error(f"The strat, {strat.__class__.__name__}, is not a child instance of Algorithm")
                exit(1)
            strat.before_trading(start, end)
            print(f"running strat {strat.__class__.__name__} for day {day.strftime('%Y-%m-%d')}")
            orders += strat.trade(day, context=context)
            strat.after_trading()

        my_orders = o_r.backtest_orders(orders)
        portfolio.place_backtest_order(my_orders)

    return portfolio.results()


