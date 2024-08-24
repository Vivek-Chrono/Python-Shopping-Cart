# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        self.cart_items.append(CartItem(product, quantity))

    def remove_from_cart(self, product_id):
        self.cart_items = [item for item in self.cart_items if item.get_product().get_id() != product_id]

    def update_quantity(self, product_id, quantity):
        for item in self.cart_items:
            if item.get_product().get_id() == product_id:
                item.set_quantity(quantity)

    def view_cart(self):
        return [(item.get_product().get_name(), item.get_quantity(), item.get_product().get_price()) for item in self.cart_items]

    def checkout(self):
        total = sum(item.get_product().get_price() * item.get_quantity() for item in self.cart_items)
        self.cart_items.clear()
        return total
