'''
Here we could make a cli interface file that works similar to 'manage.py' from django.
Meaning, that since this is in the top level directory, it can run any function, unittest,
and would make a centralized point of entry for any of the programs.

Does anyone have objection for this?

This file could use the package pyCLI to automate the command line interface making process.
maybe using 'click' or 'fire'. They seem a bit more friendly than 'argparse'
'''
import click
import os
import sys
from helpers.cli_helper import run_trade, current_stock_price, start_backtest, environ_checker, \
    tests, current_coin_price, list_alpaca_assets, find_and_save_pairs, download_bars_data
from pathlib import Path
import logging
from logging.config import fileConfig


#  See https://zetcode.com/python/click/ for a good guide to working with click


@click.group()
def cli():
    pass


@cli.command(name="trade")
@click.argument('paper', default='Paper')
def trade(paper: str):
    """
    Runs the strategies and submits the order.
    Can be paper trading or live.

    $ cli.py trade [Paper]  ==> Paper Trading
    $ cli.py trade Live   ==> Live Trading
    """
    if paper.lower() == "paper":
        logger.info(f"Running paper trade")
        run_trade(True)
    elif paper.lower() == "live":
        click.echo("Do you want to confirm paper trading (y/N)?")
        if input("--> ") == "y":
            ...
            logger.info(f"Running live trade")
            run_trade(False)
        else:
            click.echo("Aborting Live Trade")
            logger.warning(f"Live Trade aborted by user")

    else:
        click.echo("Unknown command.")
        logger.error(f"Unknown command {paper.lower()} in trade function")


@cli.command(name='backtest')
@click.option('-s', '-start', 'start', default='2020-06-01', type=str, show_default=True)
@click.option('-e', '-end', 'end', default='2021-03-22', type=str, show_default=True)
@click.option('-c', '-cach', 'cash', default=1000.00, type=float, show_default=True)
def backtest(start, end, cash):
    """
    Runs a back test using historical data with the algorithms in `trading_manager.py`
    """
    logger.info("Starting a backtest")
    click.echo(start_backtest(start, end, cash))


# @cli.command(name='wel')
# @click.argument('name', default='guest')
# @click.option('-n', default=1, type=int, show_default=True)
# def welcome(name, n):


@cli.command(name="check_environ")
def check_environment():
    """
    Check to see if the necessary environment variables are present
    """
    logger.info("Checking environment")
    click.echo(environ_checker())


@cli.command(name="stock")
@click.argument("symbol", default='A', type=str)
def get_stock_price(symbol):
    """
    Get the last price of `symbol`
    """
    print("Retrieving Data")
    logger.info(f"Retrieving data for symbol {symbol.upper()}")
    p = current_stock_price(symbol.upper())
    click.echo(p)

@cli.command(name="coin")
@click.argument('coin', type=str)
@click.option('-c', '-curr', 'currency', default='usd', type=str, show_default=True)
def get_coin_price(coin, currency):
    """
    Get the last price of 'coin'
    :param coin: The name of the cryptocurrency
    :param currency: The name of the comparative currency, i.e. usd, yen, eur, btc, etc...
    :return: str
    """
    print("Retrieving Data")
    logger.info(f"Retrieving data for symbol {coin.lower()} vs {currency.lower()}")
    p = current_coin_price(coin.lower(), currency.lower())
    click.echo(p)


@cli.command(name="test")
def run_test():
    """
    Runs automated test
    """
    print("Interpreter Location: ", sys.executable)
    logger.info("Running tests")
    tests()

@cli.command(name="list_stocks")
@click.option('--s', '--shortable', 'shortable', is_flag=True, default=False, type=bool, show_default=True)
@click.option('--f', '--fractionable', 'fractionable', is_flag=True, default=False, type=bool, show_default=True)
@click.option('--n', '--names', 'show_names', is_flag=True, default=False, type=bool, show_default=True)
def list_stocks(shortable: bool, fractionable: bool, show_names: bool):
    """
    Lists Alpaca Assets. Can be filtered in a variety of ways. '--s' shows all the shortable assets.
    '--f' shows all assets which can be bought in fractions (not whole shares).
    '--n' shows assets symbols with the name of the company.
    """
    logger.info("Getting lists of stocks")
    click.echo(f"  List of Alpaca Assets"
               f"{' that are' if shortable or fractionable else ''} "
               f"{'shortable' if shortable else ''}"
               f"{'fractionable' if fractionable and not shortable else ''}"
               f"{' and fractionable:' if fractionable and shortable else ':'}\n")
    resp = list_alpaca_assets(shortable=shortable, fractionable=fractionable, show_names=show_names)
    click.echo(f"{resp}\n\n   ++ Total: {len(resp)} ++")


@cli.command(name="calc_pairs")
def calc_pairs():
    click.echo("Starting up Pairs finding algorithm. This may take a while")  # TODO make this a estimated time
    find_and_save_pairs()


@cli.command(name="download_data")
@click.option('-t', '-timespan', 'timespan', default=180, type=int, show_default=True)
@click.option('-s', '-syms', 'symbols', default=None, type=str, show_default=True) # TODO remove default
@click.option('-r', '-replace', 'replace_old_data', default=False, type=bool, show_default=True)
def download_asset_data(timespan: int, symbols, replace_old_data):
    click.echo("Starting Download into trade_bot/data/bars/ . This will take a while.")  # TODO make this a estimated time
    if isinstance(symbols, str):
        symbols = [symbols.upper()]
    elif symbols is None:
        click.echo("Do you want to download all tradable stock from alpaca? There are about 1800 Stocks.")
        ans = input("(y/N) -->")
        if ans != 'y':
            exit()
    else:
        exit()

    download_bars_data(timespan=timespan, symbols=symbols, replace_old_data=replace_old_data)


'''
TODO commands to make:
- pull data: gets the most recent data for the last N days for previously defined stocks and stores them in csv files
- run: pulls data (if necessary), runs some strategy, then asks for confirmation before submitting trades.
'''

if __name__ == '__main__':
    log_format = (
        '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

    currDir = Path(__file__).parent.absolute()
    
    if 'logs' not in [file for file in os.listdir(currDir) if os.path.isdir(file)]:
        os.mkdir('logs')
    config_file_path = currDir / 'logs' / 'tradeBot.log'

    logging.basicConfig(
        level=logging.WARNING,
        format=log_format,
        filename=config_file_path,
    )
    logger = logging.getLogger(__name__)

    cli()

    with open(config_file_path, 'r') as f:
        lines = f.readlines()
        if len(lines) > 1000:
            click.echo(f"The length of the log file {config_file_path} is longer than 1000 lines. "
                       f"Consider purging the file.")
