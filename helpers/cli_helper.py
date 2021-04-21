from helpers.trading_manager import run_strategies, run_backtest
from utils.Alpaca_Data import AlpacaData
from utils.Alpaca_Account import AlpacaAccount
from utils.CoinGeckoData import CoinGecko
from datetime import datetime
from models.settings import Settings
import subprocess
from os import environ
import sys
from utils.Min_Edit_Distance import levenshtein, min_edit_dist
import pathlib
import logging
logger = logging.getLogger(__name__)


def run_trade(paper: bool = True):
    run_strategies(paper)


def current_stock_price(symbol: str):
    logger.debug("Getting price info")
    d = AlpacaData()
    today = datetime.today()
    r = d.get_bars_data([symbol], timeframe='minute', start=today, end=today, limit=5)

    if r[symbol].empty:
        account = AlpacaAccount()
        symbols = [i.symbol for i in account.list_assets()]
        suggestion = min_edit_dist(symbol, symbols)
        return f"No data found for symbol '{symbol}'\n\n Did you mean '{suggestion}'?"

    idx = 0
    length = len(r[symbol]['time'])
    if r[symbol]['time'][0] < r[symbol]['time'][length - 1]:
        idx = length - 1

    date = str(r[symbol]['time'][idx])
    o = r[symbol]['open'][idx]
    close = r[symbol]['close'][idx]
    high = r[symbol]['high'][idx]
    low = r[symbol]['low'][idx]
    vol = r[symbol]['volume'][idx]
    ans = f"The day's aggregates of {date} for '{symbol}' are:\n\n" \
          f"\t   High: ${high}\n\t    Low: ${low}\n\t   Open: ${o}\n\t  Close: ${close}\n\t Volume: {vol}"

    return ans


def start_backtest(start, end, cash=1000):
    # making sure the dates are in the right format
    s = datetime.strptime(start, "%Y-%m-%d").strftime("%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d").strftime("%Y-%m-%d")
    run_backtest(start=s, end=e, cash=cash)


def environ_checker() -> str:
    key_names = Settings.keys_names
    failed = 0
    s = "API Keys Check:\n" + "-"*80 + "\n"
    for key in key_names:
        if key_names[key] in environ:
            line = f"{key} Passed:".rjust(32, " ") + f" '{key_names[key]}' found in $PATH.\n"
        else:
            failed += 1
            line = f"{key} Failed:".rjust(32, " ") + f" Add '{key_names[key]}' in $PATH variable. " \
                 f"See README.md ('Sign up for an alpaca account') for how to add variable to path. \n"
        s += line

    s += "\nModule Check\n"

    req_modules = ['pycoingecko', 'polygon-api-client', 'polygon-api-client',
                   'requests', 'pandas', 'click', 'alpaca-trade-api']
    for mod in req_modules:
        try:
            __import__(mod)
        except ImportError:
            s += f"Failed: Module {mod} not found in virtual env \n"
            failed += 1
        else:
            s += f"Passed: Module {mod} not found in virtual env \n"

    s += "API Keys Check:\n" + "-" * 80

    return s


def tests():
    # having sys.executable run instead of a basic 'python' command ensures that the pytest still runs underneath of
    # the virtualenv
    testdir = pathlib.Path(__file__).resolve().parent.parent / 'tests'
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', testdir])


def current_coin_price(coin, currency):
    logger.debug(f"Getting {coin} price info")
    cg = CoinGecko()
    return cg.get_current_coin_price([coin], currency)


def list_alpaca_assets(shortable=False, fractionable=False, show_names=False):
    aa = AlpacaAccount()
    return aa.list_assets(shortable=shortable, fractionable=fractionable, show_names=show_names)

