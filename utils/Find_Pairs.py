from utils.Alpaca_Data import AlpacaData
from utils.Alpaca_Account import AlpacaAccount
from datetime import datetime
import pathlib as p


def find_pairs(timespan: int = 365):
    today = str(datetime.now().date())
    data_dir = p.Path(__file__).parent.parent.joinpath("data").joinpath("pairs_calculations")
    pairs_data = data_dir.joinpath(f"{today}_pairs_data.txt")
    account = AlpacaAccount()
    api = AlpacaData()
    assets = account.list_assets(shortable=True, fractionable=True)

    print(f"Calculation completed. Data saved in {pairs_data}")
