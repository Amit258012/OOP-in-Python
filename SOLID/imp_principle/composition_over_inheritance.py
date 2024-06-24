"""
Disadvantage of inheritance:
- We have to implement all abstract methods
- Overrideing new method must be compatible to base method
- It breaks encapsulation (by providing details to child class)
- sublass are tightly coupled to superclass (if we change base class the child class can break) 
- It can create parallel hierarchies
"""

from abc import ABC, abstractmethod

"""
class Transport:
    def __init__(self, name):
        self.name = name

    def deliver(self):
        print("delivering..")


class Truck(Transport):
    def deliver(self):
        print("Truck delivering..")


class Electric(Truck):
    def deliver(self):
        print("Electric Truck delivering..")


class Combustion(Truck):
    def deliver(self):
        print("Combustion Truck delivering..")


class Car(Transport):
    def deliver(self):
        print("Car delivering..")


class Electric(Car):
    def deliver(self):
        print("Electric Car delivering..")


class Combustion(Car):
    def deliver(self):
        print("Combustion Car delivering..")
"""


# similarly you need to create cass for auto poilet and manual

"""
solution:- favour Composition over inhertance
"""


# Engine interface with an abstract move method
class Engine(ABC):
    @abstractmethod
    def move(self):
        pass


# GasEngine class implementing the Engine interface
class GasEngine(Engine):
    def move(self):
        return "a gas engine"


# ElectricEngine class implementing the Engine interface
class ElectricEngine(Engine):
    def move(self):
        return "an electric engine"


class Driver(ABC):
    @abstractmethod
    def navigation(self):
        pass


class Autopiolot(Driver):
    def navigation(self):
        return "an autopilot"


class Manual(Driver):
    def navigation(self):
        return "a manual"


class Transport:
    def __init__(self, engine: Engine, driver: Driver):
        self.engine = engine
        self.driver = driver

    def deliverTo(self):
        engine_movement = self.engine.move()
        driver_navigation = self.driver.navigation()
        return f"The transport is moving with {engine_movement} in {driver_navigation} mode"


# Example usage
if __name__ == "__main__":
    gas_engine = GasEngine()
    electric_engine = ElectricEngine()

    autopilot_driver = Autopiolot()
    manual_driver = Manual()

    gas_transport_autopilot = Transport(gas_engine, autopilot_driver)
    electric_transport_manual = Transport(electric_engine, manual_driver)

    print(
        gas_transport_autopilot.deliverTo()
    )  # Output: The transport is moving with an gas engine in an autopilot mode
    print(
        electric_transport_manual.deliverTo()
    )  # Output: The transport is moving with an electric engine in a manual mode
