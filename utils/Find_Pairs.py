from utils.Alpaca_Data import AlpacaData
from utils.Alpaca_Account import AlpacaAccount
from datetime import datetime
import pathlib as p


def find_pairs(timespan: int = 365):
    data_dir = p.Path(__file__).parent.parent.joinpath("data")
    pairs_data = data_dir.joinpath("pairs_data.txt")
    account = AlpacaAccount()
    api = AlpacaData()
    assets = account.list_assets(shortable=True, fractionable=True)

    print(f"Calculation completed. Data saved in {data_dir}")
