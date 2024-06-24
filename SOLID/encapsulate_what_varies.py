"""
Identify the aspects of your application that vary and separate them from what stays the same

ex:- You are developing eCommerce website, there is getOrderTotal (including Tax), tax can chage any time, modifying getOrderTotal all the time can create the bugs and make the funtion code lengthy.
"""

#  Tax is mixed with order

# class Order:
#     def getOrderTotal(self, order):
#         total = 0
#         for item in order:
#             total += item.price * item.quantity

#         if order.country == "INDIA":
#             total = total * 0.18
#         elif order.country == "US":
#             total = total * 0.10
#         return total


# solution:- (Isolate Tax)
#  Tax is separated from order (Refactored code)

# class Order:
#     def getOrderTotal(self, order):
#         total = 0
#         for item in order:
#             total += item.price * item.quantity
#         total += total * self.getTaxRate(order.country)
#         return total

#     def getTaxRate(self, country):
#         if country == "INDIA":
#             return 0.18
#         elif country == "US":
#             return 0.10
#         else:
#             return 0


"""
At class Level:

Over time you might add more responsibilities to class.
These behaviours often come with their own helper fiels and methods, it blurs the main responsibility.
Extracting things to new class can make things simple and clear

Create new class for Tax and write methods related to tax there.
"""


class Order:
    def __init__(self, orders):
        self.orders = orders

    def getOrderTotal(self, tax):
        total = 0
        for item in self.orders:
            print(item)
            total += item["price"] * item["quantity"]
        total += total * tax.getTaxRate(self.orders[0]["country"])
        return total


class Tax:
    def getTaxRate(self, country):
        if country == "INDIA":
            return 0.18
        elif country == "US":
            return 0.10
        else:
            return 0


order1 = Order([{"price": 30, "quantity": 2, "country": "INDIA"}])
tax = Tax()
tot = order1.getOrderTotal(tax)
print(tot)
