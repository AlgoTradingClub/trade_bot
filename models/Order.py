class Order:
    def __init__(self):
        self.qty = 0
        self.asset = ""
        self.order_types = ['limit', 'market']
        self.order_type = ""
        self.sell = False
        self.buy = False

    def send_to_alpaca(self, paper=True):
        """
        Puts the order in the correct format for alpaca, then sends the order
        """