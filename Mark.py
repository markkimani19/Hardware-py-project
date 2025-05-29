
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price= price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False










class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items)

    def print_receipt(self):
        print(f"\n Receipt for {self.customer.name}")
        for product, qty in self.items:
            print(f"{product.name} x{qty} @ {product.price} KES each")
        print(f"Total: {self.calculate_total()} KES\n")











class HardwareStore:
    def __init__(self):
        self.products = {}   
        self.customers = {} 



    def add_product(self, product):
        self.products[product.product_id] = product



    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer



    def sell(self, customer_id, product_id, quantity):
        customer = self.customers.get(customer_id)
        product = self.products.get(product_id)

        if not customer:
            print("Customer not found.")
            return
        if not product:
            print("Product not found.")
            return

        if product.reduce_stock(quantity):
            order = Order(customer)
            order.add_item(product, quantity)
            order.print_receipt()
        else:
            print(f"Not enough stock for {product.name}. Only {product.stock} left.")




if __name__ == "__main__":
    store = HardwareStore()


    store.add_product(Product(1, "Cement", 700, 100))
    store.add_product(Product(2, "Nails (1kg)", 120, 200))
    store.add_product(Product(3, "Timber (per piece)", 450, 50))

    
    store.add_customer(Customer(101, "Mark"))


    store.sell(101, 1, 5)   
    store.sell(101, 2, 10)  
    store.sell(101, 3, 2)   
