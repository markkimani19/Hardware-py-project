class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  # list of tuples (Product, quantity)

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items)

