class StockxOrder(object):
    def __init__(self, order_type, order_json):
        self.product_uuid = order_json.get('skuUuid')
        self.order_type = order_type
        self.order_price = order_json.get('amount')
        self.shoe_size = order_json.get('shoeSize')
        self.num_orders = order_json.get('frequency')
