"""
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

When to Use:
- When you want to construct complex objects that require multiple steps to complete.
- When you need to create different representations of a complex object.
- When the creation process needs to be independent of the parts that make up the object.

Components:
- Builder Interface: Declares the steps to create different parts of the product.
- Concrete Builder: Implements the Builder interface and provides specific implementations for building the parts of the product. It also keeps track of the product under construction.
- Product: The complex object that is being built.
- Director: Constructs an object using the Builder interface. It controls the construction process.

Benefits:
- Allows you to construct complex objects step by step.
- Provides a clear separation between the construction and representation of an object.
- Makes the construction process more flexible and reusable.
"""


class Car:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None

    def __str__(self):
        return f"Car with {self.wheels}, {self.engine}, and {self.body}."


# Builder Interface
class CarBuilder:
    def set_wheels(self, wheels):
        pass

    def set_engine(self, engine):
        pass

    def set_body(self, body):
        pass

    def get_car(self):
        pass


# Concrete Builder
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, wheels):
        self.car.wheels = wheels

    def set_engine(self, engine):
        self.car.engine = engine

    def set_body(self, body):
        self.car.body = body

    def get_car(self):
        return self.car


# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_wheels("Sports Wheels")
        self.builder.set_engine("V8 Engine")
        self.builder.set_body("Sporty body")


# Client code
builder = SportsCarBuilder()
director = Director(builder)
director.construct_car()
car = builder.get_car()
print(car)  # Car with Sports Wheels, V8 Engine, and Sporty body.
