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
import pathlib
import logging
logger = logging.getLogger(__name__)


def run_trade(paper: bool = True):
    run_strategies(paper)


def levenshtein(source, target):
    """
    Vectorized version of min edit distance of strings
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    """
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]


def min_edit_dist(str1: str, strings: List[str]) -> str:
    best = 10
    suggestion = ""
    for s in strings:
        result = levenshtein(str1, s)
        if result < best:
            best = result
            suggestion = s
    return suggestion


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
