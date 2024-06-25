"""
 Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
"""

"""
code without factory design

class PaymentType(Enum):
    CREDIT_CARD = "creditcard"
    PAYPAL = "paypal"
    BANK_TRANSFER = "banktransfer"


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card."


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using PayPal."


class BankTransferPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Bank Transfer."


if __name__ == "__main__":
    method_input = input(
        "Enter the payment method (creditcard/paypal/banktransfer): "
    ).lower()
    amount = float(input("Enter the amount to pay: "))

    try:
        if method_input == "creditcard":
            payment_method = CreditCardPayment()
        elif method_input == "paypal":
            payment_method = PayPalPayment()
        elif method_input == "banktransfer":
            payment_method = BankTransferPayment()
        else:
            raise ValueError("Unknown payment method type")

        print(payment_method.pay(amount))
    except ValueError as e:
        print(e)
"""

"""
Problem without using factory design pattern

Duplicated Logic:- The logic for selecting the payment method is duplicated and scattered in the client code.

Hard to Maintain:- Adding a new payment method requires modifying the client code, which can lead to errors and is not scalable.

Violation of Open/Closed Principle:- The client code needs to be modified for each new payment method, violating the principle that classes should be open for extension but closed for modification.
"""


"""
When to Use:- If you see the similar behavior, if you can imagine the factoy creating object. "If you class has class types like shown in examples"

list of real world example:-

-Vehicle Manufacturing:
    Different types of vehicles (cars, trucks, motorcycles) can be created using a factory. The factory determines the type of vehicle to create based on input parameters.

-Document Creation:
    Different types of documents (Word, PDF, Excel) can be created by a factory based on the required format.
    
-Shape Drawing Applications:(circle, rectangle, square)

-UI Elements in Software Development: (buttons, text fields, labels)

-Game Development: (enemies, power-ups, obstacles)

-Notification Systems: (email, SMS, push notification)

-Database Connection Management: (MySQL, PostgreSQL, MongoDB) 

-Credit Card Verification Systems: (Visa, MasterCard, UPI)

-Logistics and Delivery Systems:(air, sea, land)

-Cloud Service Providers: (compute, storage, database)

-Financial Trading Systems:(stocks, bonds, options)

-Payment Gateways: (credit card, PayPal, bank transfer)
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Union


# Enum for payment methods
class PaymentType(Enum):
    CREDIT_CARD = "creditcard"
    PAYPAL = "paypal"
    BANK_TRANSFER = "banktransfer"


# Abstract product
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# Concrete products
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card."


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using PayPal."


class BankTransferPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Bank Transfer."


# Factory
class PaymentFactory:
    @staticmethod
    def create_payment_method(
        method_type: PaymentType,
    ) -> Union[CreditCardPayment, PayPalPayment, BankTransferPayment]:
        if method_type == PaymentType.CREDIT_CARD:
            return CreditCardPayment()
        elif method_type == PaymentType.PAYPAL:
            return PayPalPayment()
        elif method_type == PaymentType.BANK_TRANSFER:
            return BankTransferPayment()
        else:
            raise ValueError("Unknown payment method type")


# Client code
if __name__ == "__main__":
    # Input method and amount
    method_input = input(
        "Enter the payment method (creditcard/paypal/banktransfer): "
    ).lower()
    amount = float(input("Enter the amount to pay: "))

    try:
        method_type = PaymentType(method_input)
        payment_method = PaymentFactory.create_payment_method(method_type)
        print(payment_method.pay(amount))
    except ValueError as e:
        print(e)
