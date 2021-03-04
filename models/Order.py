from alpaca_trade_api import REST
from trade_bot.models.settings import Settings
from os import environ


class Order:
    def __init__(self, side: str, asset: str, qty: float = 0.0, o_type: str = "market", notional: float = 0.0,
                 time_in_force: str = 'day', limit_price: float = 0.0, stop_price: float = 0.0,
                 trail_price: float = 0.0, trail_percent: float = 0.0, extended_hours: bool = False):
        self.qty = qty
        self.asset = asset.upper()
        self.notional = notional  # the dollar amount you want to trade
        order_types = ['limit', 'market', 'stop', 'stop_limit', 'trailing_stop']
        force_types = ['day', 'gtc', 'opg', 'cls', 'ioc', 'fok']
        self.time_in_force = time_in_force
        self.order_type = o_type
        self.side = side
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.trail_price = trail_price
        self.trail_percent = trail_percent
        self.extended_hours = extended_hours
        assert isinstance(self.qty, float) or isinstance(self.qty, int)
        assert self.side == 'buy' or self.side == 'sell'
        assert (self.notional > 0 and self.order_type == 'market') or (self.notional == 0 and self.qty > 0)
        assert self.notional == 0 or self.qty == 0
        assert self.order_type in order_types
        assert self.time_in_force in force_types
        if self.order_type in ["limit", 'stop_limit']:
            assert self.limit_price > 0
        if self.order_type in ['stop', 'stop_limit']:
            assert self.stop_price > 0

        # convert to str for alpaca
        self.notional = str(self.notional)
        self.limit_price = str(self.limit_price)
        self.stop_price = str(self.stop_price)
        self.trail_price = str(self.trail_price)
        self.trail_percent = str(self.trail_percent)

    def send_to_alpaca(self, paper=True):
        """
        Puts the order in the correct format for alpaca, then sends the order
        """
        key_names = Settings.keys_names
        if paper:
            key_id = key_names["Alpaca Paper Key ID"]
            secret_key = key_names["Alpaca Paper Secret Key"]
            base_url = "https://paper-api.alpaca.markets/v2"
        else:
            key_id = key_names["Alpaca Live Key ID"]
            secret_key = key_names["Alpaca Live Secret Key"]
            base_url = "https://api.alpaca.markets/v2"

        key_id = environ[key_id]
        secret_key = environ[secret_key]
        api = REST(key_id, secret_key, base_url)

        if self.order_type == "trailing_stop":
            api.submit_order(
                symbol=self.asset,
                qty=self.qty,
                side=self.side,
                type=self.order_type,
                time_in_force=self.time_in_force,
                trail_price=self.trail_price,
                trail_percent=self.trail_percent,
            )
        elif self.order_type == "stop_limit":
            api.submit_order(
                symbol=self.asset,
                qty=self.qty,
                side=self.side,
                type=self.order_type,
                time_in_force=self.time_in_force,
                stop_price=self.stop_price,
                limit_price=self.limit_price,
            )
        elif self.order_type == "limit":
            api.submit_order(
                symbol=self.asset,
                qty=self.qty,
                side=self.side,
                type=self.order_type,
                time_in_force=self.time_in_force,
                limit_price=self.limit_price,
            )
        elif self.order_type == "stop":
            api.submit_order(
                symbol=self.asset,
                qty=self.qty,
                side=self.side,
                type=self.order_type,
                time_in_force=self.time_in_force,
                stop_price=self.stop_price,
            )
        else:
            api.submit_order(
                symbol=self.asset,
                qty=self.qty,
                side=self.side,
                type=self.order_type,
                time_in_force=self.time_in_force,
            )
