class Order:
    def __init__(self):
        self.qty = 0
        self.asset = ""
        self.order_types = ['limit', 'market']
        self.order_type = ""
        self.sell = False
        self.buy = False