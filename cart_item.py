# cart_item.py
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
