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
from helpers.cli_helper import run_trade, current_stock_price, start_backtest, environ_checker, tests

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
    $ cli.py trade [Paper]  > Paper Trading
    $ cli.py trade Live   > Live Trading
    """
    if paper.lower() == "paper":
        run_trade(True)
    elif paper.lower() == "live":
        run_trade(False)


@cli.command(name='backtest')
@click.option('-s', '-start', 'start', default='2020-06-01', type=str, show_default=True)
@click.option('-e', '-end', 'end', default='2021-03-02', type=str, show_default=True)
def backtest(start, end):
    """
    Runs a back test using historical data with the algorithms in `trading_manager.py`
    """
    start_backtest(start, end)


# @cli.command(name='wel')
# @click.argument('name', default='guest')
# @click.option('-n', default=1, type=int, show_default=True)
# def welcome(name, n):


@cli.command(name="check_environ")
def check_environment():
    """
    Check to see if the necessary environment variables are present
    """
    click.echo(environ_checker())


@cli.command(name="stock")
@click.argument("symbol", default='A', type=str)
def get_stock_price(symbol):
    """
    Get the last price of `symbol`
    """
    print("Retrieving Data")
    p = current_stock_price(symbol.upper())
    click.echo(p)


@cli.command(name="test")
def run_test():
    """
    Runs automated test
    """
    tests()


'''
TODO commands to make:
- pull data: gets the most recent data for the last N days for previously defined stocks and stores them in csv files
- run: pulls data (if necessary), runs some strategy, then asks for confirmation before submitting trades.
'''

if __name__ == '__main__':
    cli()
