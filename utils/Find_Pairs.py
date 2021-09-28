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

    possible_pairs = []
    for i in range(len(assets)):
        for j in range(i + 1, len(assets)):
            possible_pairs.append(f"doing analysis on {assets[i]} and {assets[j]}")

    print(f"pairs calculated: {len(possible_pairs)}")

    print(f"Calculation completed. Data saved in {pairs_data}")
