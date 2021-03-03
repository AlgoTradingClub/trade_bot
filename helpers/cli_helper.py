from trade_bot.helpers.trading_manager import run_strategies, run_backtest
from trade_bot.utils.Alpaca_Data import AlpacaData
from datetime import datetime, date
from trade_bot.models.settings import Settings
from typing import List
import numpy as np
import subprocess
from os import listdir, environ, path
from os.path import isfile, join


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
    d = AlpacaData()
    today = datetime.today()
    r = d.get_bars_data([symbol], timeframe='day', from_year=today.year, from_month=today.month, from_day=today.day,
                        to_year=today.year, to_month=today.month, to_day=today.day, limit=1)

    if r.empty:
        symbols = [i.symbol for i in d.list_assets()]
        suggestion = min_edit_dist(symbol, symbols)
        return f"No data found for symbol '{symbol}'\n\n Did you mean '{suggestion}'?"

    date = datetime.strptime(r['time'][0], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
    o = r['open'][0]
    close = r['close'][0]
    high = r['high'][0]
    low = r['low'][0]
    vol = r['volume'][0]
    ans = f"The day's aggregates of {date} for '{symbol}' are:\n\n" \
          f"\t   High: ${high}\n\t    Low: ${low}\n\t   Open: ${o}\n\t  Close: ${close}\n\t Volume: {vol}"

    return ans


def start_backtest(start, end, cash):
    # making sure the dates are in the right format
    s = datetime.strptime(start, "%Y-%m-%d").strftime("%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d").strftime("%Y-%m-%d")
    return run_backtest(start=s, end=e)


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
    testdir = join('..', 'trade_bot', 'tests')
    CURR_DIR = path.dirname(path.realpath(__file__))
    onlyfiles = [f for f in listdir(testdir) if isfile(join(testdir, f))]
    for f in onlyfiles:
        if f != "__init__.py":
            print(f)
            p = path.abspath(join(testdir, f))
            subprocess.run(["python", f"{p}"])
