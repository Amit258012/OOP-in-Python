"""
Dependency :- One class depends on another class.

A customer depends on the order class to place orders. This is a temporary relationship.

[customer] - - - - > [order] // Customer places orders
"""


class Order:
    def __init__(self, order_id):
        self.order_id = order_id


class Customer:
    def __init__(self, name):
        self.name = name

    def place_order(self, order):
        return f"oder {order.order_id} placed by {self.name}"


customer = Customer("Amit")
order = Order(1234)
print(customer.place_order(order))  # Output: oder 1234 placed by Amit
