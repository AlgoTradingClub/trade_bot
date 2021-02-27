'''
Here we could make a cli interface file that works similar to 'manage.py' from django. Meaning, that since this is in the top level directory, it can run any function, unittest, and would make a centralized point of entry for any of the programs.

Does anyone have objection for this?

This file could use the package pyCLI to automate the command line interface making process.
maybe using 'click' or 'fire'. They seem a bit more friendly than 'argparse'
'''
import click
import os
from helpers.cli_helper import *

#  See https://zetcode.com/python/click/ for a good guide to working with click


@click.group()
def cli():
  pass


@cli.command(name='gen')
def generic():
    """
    Prints a generic hello message
    """
    click.echo('Hello there')


@cli.command(name='wel')
@click.argument('name', default='guest')
@click.option('-n', default=1, type=int, show_default=True)
def welcome(name, n):
    """
    Sends a warm welcome!
    """
    click.echo(hello_world(name) * n)


@cli.command(name="check_environ")
def check_environment():
    """
    Check to see if the necessary environment variables are present
    """
    live_key = 'polygon_api_key'
    if live_key in os.environ:
        click.echo("Passed: Alpaca Live Key is in the environment variables")
    else:
        click.echo(f"Failed: '{live_key}' is not found in $PATH\n Add 'polygon_api_key' to $PATH.")

@cli.command(name='poly')
@click.option('-v', nargs=1, default='', type=str, help="Shows the last aggregate data point from the given stock ticker")
@click.option('--u', is_flag=True, help="updates the CSV files with current data based on saved tickers in ... .txt")
def polygon_cli(v, u):
    if v:
        click.echo(v)
    if u:
        click.echo(u)

'''
TODO commands to make:
- pull data: gets the most recent data for the last N days for previously defined stocks and stores them in csv files
- run: pulls data (if necessary), runs some strategy, then asks for confirmation before submitting trades.
'''

if __name__ == '__main__':
    cli()
