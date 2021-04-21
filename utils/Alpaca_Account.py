from models.settings import Settings
from os import environ
from alpaca_trade_api import REST


class AlpacaAccount:
    def __init__(self, paper=True):
        key_names = Settings.keys_names
        if paper:
            key_id = key_names["Alpaca Paper Key ID"]
            secret_key = key_names["Alpaca Paper Secret Key"]
            base_url = "https://paper-api.alpaca.markets"
        else:
            key_id = key_names["Alpaca Live Key ID"]
            secret_key = key_names["Alpaca Live Secret Key"]
            base_url = "https://api.alpaca.markets"

        key_id = environ[key_id]
        secret_key = environ[secret_key]
        self.api = REST(key_id, secret_key, base_url)
        del key_id, secret_key

    def get_api(self):
        return self.api

    def list_assets(self, shortable=False, fractionable=False, show_names=False):
        active_assets = self.api.list_assets(status='active')
        myfilter = []
        if shortable and fractionable:
            for asset in active_assets:
                if asset.easy_to_borrow and asset.marginable and asset.fractionable:
                    myfilter.append(asset)

        elif shortable:
            for asset in active_assets:
                if asset.easy_to_borrow and asset.marginable:
                    myfilter.append(asset)

        elif fractionable:
            for asset in active_assets:
                if asset.fractionable:
                    myfilter.append(asset)

        else:
            myfilter = active_assets

        if show_names:
            return [f"{i.name} :: '{i.symbol}'" for i in myfilter]
        else:
            return [i.symbol for i in myfilter]
