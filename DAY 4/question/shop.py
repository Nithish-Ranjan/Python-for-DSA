class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.product_id} - {self.name} - ₹{self.price:.2f}"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        for item in self.items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                return

        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_id):
        for item in self.items:
            if item["product"].product_id == product_id:
                self.items.remove(item)
                return True
        return False

    def update_quantity(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        for item in self.items:
            if item["product"].product_id == product_id:
                item["quantity"] = quantity
                return True
        return False

    def get_total(self):
        total = 0.0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def apply_discount(self, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100.")
        return self.get_total() - (self.get_total() * discount_percent / 100)

    def __str__(self):
        if not self.items:
            return "Cart is empty."

        result = []
        for item in self.items:
            result.append(
                f"{item['product'].name} x {item['quantity']} = ₹{item['product'].price * item['quantity']:.2f}"
            )
        return "\n".join(result)


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)

    def remove_from_cart(self, product_id):
        self.cart.remove_item(product_id)

    def checkout(self):
        order = Order(self, self.cart.items.copy())
        self.cart.items.clear()
        return order


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        total = 0.0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self):
        return f"Order for {self.customer.name}: Total ₹{self.total_amount:.2f}"


def main():
    p1 = Product(101, "Laptop", 45000)
    p2 = Product(102, "Phone", 25000)
    p3 = Product(103, "Headphones", 3000)

    customer = Customer(1, "Alice")

    customer.add_to_cart(p1, 1)
    customer.add_to_cart(p2, 2)
    customer.add_to_cart(p3, 1)

    print("Cart Items:")
    print(customer.cart)
    print(f"Total before discount: ₹{customer.cart.get_total():.2f}")
    print(f"Discounted total: ₹{customer.cart.apply_discount(10):.2f}")

    customer.cart.update_quantity(102, 3)
    print("\nUpdated Cart:")
    print(customer.cart)

    order = customer.checkout()
    print("\n" + str(order))
    print("\nCart after checkout:")
    print(customer.cart)


if __name__ == "__main__":
    main()
