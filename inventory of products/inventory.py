from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    def __repr__(self):
        return "\n".join([str(product) for product in self.products])

    def add_product(self, product):
        self.products.append(product)

    def get_product_prices(self):
        return ["ID-{}: Price-{}".format(product.id, product.price) for product in self.products]


inventory = Inventory()

product1 = Product(150, 1, 13)
product2 = Product(550, 2, 9)
product3 = Product(180, 3, 5)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

print(inventory)
print(inventory.get_product_prices())
