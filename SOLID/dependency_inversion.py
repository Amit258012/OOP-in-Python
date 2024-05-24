""" Dependency Inversion Principle """

# The dependency inversion principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. In other words, the principle states that classes should depend on abstractions, not on concrete implementations.

# The dependency inversion principle is about decoupling high-level modules from low-level modules so that changes in one module do not affect the other module.

# Abstractions should not depend on details. Details should depend on abstractions.

# The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.


# class FXConverter:
#     def convert(self, from_cur, to_cur, amount):
#         print(f"{amount} {from_cur} = {amount * 1.3} {to_cur}")
#         return amount * 1.3


# class App:
#     def start(self):
#         converter = FXConverter()
#         converter.convert("USD", "EUR", 100)


# if __name__ == "__main__":
#     app = App()
#     app.start()

"""
Problem :- 
    The App class depends on the FXConverter class. 
    If the FXConverter class changes, the App class needs to change. 
    If the App class changes, the FXConverter class needs to change.

    It doesn't follow the dependency inversion principle because the App class depends on the FXConverter class.

"""
"""
Solution:- 
    We can create an interface for the FXConverter class. 
    The App class will depend on the interface, not on the FXConverter class. 
    This way, if the implementation of the FXConverter class changes, the App class will not be affected.
    In case we changed api of FXConverter, we can create new class and implement the interface in it.
"""

from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    def convert(self, from_cur, to_cur, amount):
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_cur, to_cur, amount):
        print("Converting currency usin FXConverter")
        print(f"{amount} {from_cur} = {amount * 1.3} {to_cur}")
        return amount * 1.3


class AlphConverter(CurrencyConverter):
    def convert(self, from_cur, to_cur, amount):
        print("Converting currency usin AlphConverter")
        print(f"{amount} {from_cur} = {amount * 1.3} {to_cur}")
        return amount * 1.3


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("USD", "EUR", 100)


if __name__ == "__main__":
    converter = FXConverter()
    converter2 = AlphConverter()
    app = App(converter)
    app.start()

    app2 = App(converter2)
    app2.start()
