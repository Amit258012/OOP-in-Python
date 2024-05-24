# https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/

"""
Interface Segregation Principle (ISP)
"""

# The duck typing principle states that “if it walks like a duck and quacks like a duck, it must be a duck.” In other words, the methods of a class determine what its objects will be, not the type of the class.

# The interface segregation principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing. It doesn’t mean that the interface should have one method

# The interface segregation principle states that a client should not be forced to implement an interface that it doesn’t use. Instead of creating a large interface, you should create smaller interfaces that are specific to the client’s needs.

# The interface segregation principle is about breaking down large interfaces into smaller, more specific interfaces so that clients only need to know about the methods that are of interest to them.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Aircraft(Vehicle):
    def drive(self):
        print("Taking off")

    def fly(self):
        print("Flying")


class Car(Vehicle):
    def drive(self):
        print("Going")

    def fly(self):
        print("Can't fly")


"""
problem:- 
    This violates ISP as the Car class is forced to implement a method that it doesn't use.
"""
"""
solution:- 
    The solution is to break down the Vehicle interface into smaller, more specific interfaces.
    To fix the violation, we can create two separate interfaces: Drivable and Flyable.
    The Drivable interface has the drive() method, and the Flyable interface has the fly() method.
"""


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Vehicle):
    @abstractmethod
    def fly(self):
        pass


class Aircraft(Flyable):
    def fly(self):
        print("Flying")

    def go(self):
        print("Taking off")


class Car(Vehicle):
    def go(self):
        print("Going")
