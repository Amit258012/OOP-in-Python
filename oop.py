class Employee:
    num_of_employes = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_employes += 1

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

    @property
    def fullName(self):
        return f"{self.fname} {self.lname}"

    @fullName.setter
    def fullName(self, name):
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.fname = None
        self.lname = None

    def salary_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # you can use this as an alternative constructor
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative contructor
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split("-")
        pay = int(pay)
        return cls(fname, lname, pay)

    # Note:- static method does not take self or cls as an argument
    # it is just a utility function
    # it does not depend on the class or instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.fname}', '{self.lname}', {self.pay})"

    def __str__(self):
        return f"{self.fullName()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee("Amit", "Jahagirdar", 1000000)
emp2 = Employee("Vinit", "Jahagirdar", 5000000)

emp1.fullName = "Amruta Kulkarni"


# emp1.fname = "Shri" # it will fail to change email to shri
# without property decorator
# print(emp1.email())

# use property decorator to access the email as an attribute
# write like method and access like attribute
# print(emp1.email)
# print(emp1.fullName)
# del emp1.fullName


# Inheritance :- Developer class is inheriting Employee class
# we can override the class variable and methods in the child class using same keyword
# we can also add new methods and variables in the child class, to customize
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


dev1 = Developer("Amit", "Jahagirdar", 1000000, "Python")
dev2 = Developer("Vinit", "Jahagirdar", 5000000, "JavaScript")


class Manager(Employee):
    raise_amount = 1.09

    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print("-->", emp.fullName())


mgr_1 = Manager("Sue", "Smith", 90000, [dev1])
# print(mgr_1.raise_amount)
# mgr_1.add_employee(dev2)
# # mgr_1.print_employee()
# mgr_1.remove_employee(dev1)
# mgr_1.print_employee()
# print(isinstance(mgr_1, Manager))  # True
# print(issubclass(Developer, Employee))  # True
# print(issubclass(Manager, Employee))  # True
# print(issubclass(Manager, Developer))  # False

# Employee.set_raise_amount(1.05)

# emp_str1 = "Amit-Jahagirdar-1000000"
# emp_str2 = "Vinit-Jahagirdar-5000000"


# emp1 = Employee("Amit", "Jahagirdar", 1000000)
# emp2 = Employee("Vinit", "Jahagirdar", 5000000)
# emp1 = Employee.from_string(emp_str1)
# emp2 = Employee.from_string(emp_str2)


# print("num of employee: ", Employee.num_of_employes)
# print("Employee raise amount: ", Employee.raise_amount)
# print("before salary raise: ", dev2.pay)
# dev2.salary_raise()
# print("after salary raise: ", dev2.pay)

# import datetime

# my_date = datetime.date(2024, 1, 1)
# print(Employee.is_workday(my_date))

# print(dev1)

# used for debugging
# __repr__ is used to return a string containing a printable representation of an object
# print(repr(dev1))

# used to display properly
# __str__ is used to return a string containing a nicely printable(readable) representation of an object
# print(str(dev1))

# add employee salary
# print(emp1 + emp2)

# Abstract Class

from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    # abstract method:- blue print for what class can do
    # abstract method is an method without an implementation
    # An abstract class may or may not include abstract methods.
    # use abstractmethod decorator
    # it is mandatory to implement this method in the child class
    # abstract class is a class that cannot be instantiated

    @property
    @abstractmethod
    def power(self): ...

    @abstractmethod
    def call_target(self, name: str): ...


#  if you want to create instance of abstract class, you need to implement all the abstract methods
# phone = Phone("Nokia")


class Nokia(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        return "2% battery remaining"

    def call_target(self, name: str):
        return f"calling {name}...."


phone = Nokia("nokia 1100")
print(phone.power)
print(phone.call_target("Amit"))


# Multiple inhertence


# class ChildClass(parent1, parent2, parent3):
#     pass


class Car:
    def start(self):
        print("Car is starting")

    def go(self):
        print("Car is going")


class Flyable:
    def start(self):
        print("start the flying object")

    def fly(self):
        print("Flying")


class FlyingCar(Car, Flyable):
    def start(self):
        super().start()


if __name__ == "__main__":
    flying_car = FlyingCar()
    flying_car.start()
