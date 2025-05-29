class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False


# store.add_product(Product(1, "Cement", 700, 100))
# store.add_product(Product(2, "Nails (1kg)", 120, 200))