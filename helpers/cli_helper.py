from helpers.trading_manager import run_strategies, run_backtest
from utils.Alpaca_Data import AlpacaData
from datetime import datetime, date



def run_trade(paper: bool = True):
    run_strategies(paper)


def current_stock_price(symbol: str):
    d = AlpacaData()
    today = date.today()
    r = d.get_bars_data([symbol], timeframe='day', from_year=today.year, from_month=today.month, from_day=today.day,
                        to_year=today.year, to_month=today.month, to_day=today.day, limit=1)

    if r.empty:
        return f"No data found for symbol '{symbol}'"

    date = datetime.strptime(r['time'][0], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
    o = r['open'][0]
    close = r['close'][0]
    high = r['high'][0]
    low = r['low'][0]
    vol = r['volume'][0]
    ans = f"The day's aggregates of {date} for '{symbol}' are:\n\n" \
          f"\tHigh:   ${high}\n\tLow:    ${low}\n\tOpen:   ${o}\n\tClose:  ${close}\n\tVolume: {vol}"

    return ans


def start_backtest(start, end):
    # making sure the dates are in the right format
    s = datetime.strptime(start, "%Y-%m-%d").strftime("%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d").strftime("%Y-%m-%d")
    run_backtest(start=s, end=e)
