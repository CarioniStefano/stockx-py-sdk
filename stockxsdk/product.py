class StockxProduct(object):
    def __init__(self, product_json):
        product = product_json.get('Product')
        self.product_id = product.get('id')
        self.title = product.get('title')
        self.retail_price = product.get('retailPrice')
        self.style_id = product.get('styleId')
        self.brand = product.get('brand')
        self.image = product['media']['imageUrl']
        children = [product['children'][child] for child in product['children']]
        self.sizes = {child['shoeSize']: child['id'] for child in children}
