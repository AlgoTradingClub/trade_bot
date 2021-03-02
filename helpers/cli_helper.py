from .trading_manager import run_strategies


def hello_world(name):
    return f"hello, {name}"


def trade(paper: bool = True):
    run_strategies(paper)

