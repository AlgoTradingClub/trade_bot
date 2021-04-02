from helpers.trading_manager import run_strategies, run_backtest
from utils.Alpaca_Data import AlpacaData
from utils.Alpaca_Account import AlpacaAccount
from datetime import datetime, date
from models.settings import Settings
from typing import List
import numpy as np
import subprocess
from os import listdir, environ, path
from os.path import isfile, join
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
    r = d.get_bars_data([symbol], timeframe='day', from_year=today.year, from_month=today.month, from_day=today.day,
                        to_year=today.year, to_month=today.month, to_day=today.day, limit=1)

    if r[symbol].empty:
        account = AlpacaAccount()
        symbols = [i.symbol for i in account.list_assets()]
        suggestion = min_edit_dist(symbol, symbols)
        return f"No data found for symbol '{symbol}'\n\n Did you mean '{suggestion}'?"

    date = str(r[symbol]['time'][0])
    o = r[symbol]['open'][0]
    close = r[symbol]['close'][0]
    high = r[symbol]['high'][0]
    low = r[symbol]['low'][0]
    vol = r[symbol]['volume'][0]
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
    s = "API Keys Check:\n" + "-"*80 + "\n"
    for key in key_names:
        if key_names[key] in environ:
            line = f"{key} Passed:".rjust(32, " ") + f" '{key_names[key]}' found in $PATH.\n"
        else:
            line = f"{key} Failed:".rjust(32, " ") + f" Add '{key_names[key]}' in $PATH variable. " \
                 f"See README.md ('Sign up for an alpaca account') for how to add variable to path. \n"
        s += line
    return s


def tests():
    testdir = pathlib.Path(__file__).resolve().parent.parent / 'tests'
    subprocess.run(['python', '-m', 'unittest', 'discover', testdir])
