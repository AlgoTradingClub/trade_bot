from utils.Alpaca_Account import AlpacaAccount


class Context:
    def __init__(self, paper=False):
        self.aa = AlpacaAccount(paper)

    def getCurrentPorfolio(self):
        ...

    def getBuyingPower(self):
        ...

    def __str__(self):
        return f"Context Object: "
