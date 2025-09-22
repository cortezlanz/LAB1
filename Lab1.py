class Product:
    inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = str(product_id)
        self.name = str(name)
        self.category = str(category)
        self.quantity = int(quantity)
        self.price = int(price)
        self.supplier = str(supplier)

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        """Updates the details of an existing product."""
        for product in cls.inventory:
            if product.product_id == str(product_id):
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        """Deletes a product from the inventory based on its ID."""
        product_to_delete = None
        for product in cls.inventory:
            if product.product_id == str(product_id):
                product_to_delete = product
                break
        if product_to_delete:
            cls.inventory.remove(product_to_delete)
            return "Product deleted successfully"
        else:
            return "Product not found"

class Order:
    """Represents a customer order."""
    def __init__(self, order_id, product_id, quantity, customer_info=None):
        self.order_id = order_id
        self.product_id = str(product_id)
        self.quantity = quantity
        self.customer_info = customer_info

    def place_order(self):
        """Processes an order, checking stock and updating the inventory."""
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return f"Order placed successfully. Order ID: {self.order_id}"
                else:
                    return f"Insufficient stock to place the order. Available: {product.quantity}"
        return "Product not found"

print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B"))
print(Product.update_product(1, quantity=45, price=950))
print(Product.delete_product(2))
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())