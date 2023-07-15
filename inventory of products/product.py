class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return "Product ID: {}, Price: {}, Quantity: {}".format(self.id, self.price, self.quantity)

    def buy(self, n):
        try:
            if n <= self.quantity:
                self.quantity = self.quantity - n
            else:
                raise ValueError("Insufficient quantity product")
        except ValueError:
            return ("Insufficient quantity product")








