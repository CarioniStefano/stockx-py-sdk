class StockxItem(object):
    def __init__(self, item_json):
        self.item_type = item_json.get('text')
        self.item_price = item_json.get('amount')
        self.item_id = item_json.get('chainId')
