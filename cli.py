'''
Here we could make a cli interface file that works similar to 'manage.py' from django. Meaning, that since this is in the top level directory, it can run any function, unittest, and would make a centralized point of entry for any of the programs.

Does anyone have objection for this?

This file could use the package pyCLI to automate the command line interface making process.
maybe using 'click' or 'fire'. They seem a bit more friendly than 'argparse'
'''
import click

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
def welcome(name):
    """
    Sends a warm welcome!
    """
    click.echo(f'Welcome, {name}')

'''
TODO commands to make:
- pull data: gets the most recent data for the last N days for previously defined stocks and stores them in csv files
- run: pulls data (if necessary), runs some strategy, then asks for confirmation before submitting trades.
'''

if __name__ == '__main__':
    cli()
