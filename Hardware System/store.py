class HardwareStore:
    def __init__(self):
        self.products = {}  # product_id -> Product
        self.customers = {}  # customer_id -> Customer

    def add_product(self, product):
        self.products[product.product_id] = product

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def sell(self, customer_id, product_id, quantity):
        customer = self.customers.get(customer_id)
        product = self.products.get(product_id)
        
        if not customer or not product:
            print("Customer or product not found.")
            return
        
        if product.reduce_stock(quantity):
            order = Order(customer)
            order.add_item(product, quantity)
            total = order.calculate_total()
            print(f"Sold {quantity} {product.name} to {customer.name} for KES {total}")
        else:
            print(f"Not enough stock for {product.name}.")
