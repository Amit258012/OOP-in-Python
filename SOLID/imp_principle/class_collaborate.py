"""
Program to an interface, not an implementation. Depend on abstractions, not on concrete classes.

When you want to make two classes collaborate, you can start by making one of them dependent on the other

Better way:-
- what method does it execute?
- make interface of these methods

Now obj 2 is depend on interface not on obj1 impementation, it more flexible 

ex:- creating software company, company is tightly coupled to classes of employees (designer, tester, developer)

=> create Employee <<interface>> (doWork) and implement designer, tester, developer 
"""

from abc import ABC, abstractmethod


# Base class for all employees
class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def work(self):
        pass


# Derived class for Designers
class Designer(Employee):
    def work(self):
        return f"Designer {self.name} is designing using {self.tool}."


# Derived class for Testers
class Tester(Employee):
    def work(self):
        return f"Tester {self.name} is testing using {self.testing_tool}."


# Derived class for Developers
class Developer(Employee):
    def work(self):
        return f"Developer {self.name} is developing software using {self.programming_language}."


# Company class that contains employees
class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(employee.work())


"""
Problem:-  The Company class remains coupled to the employee classes. This is bad because if we introduce new types of companies that work with other types of employees.
"""
# solution:- the sub class must return the employees what they need


# Base class for all employees
class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def work(self):
        pass


# Derived class for Designers
class Designer(Employee):
    def __init__(self, name, id, tool):
        super().__init__(name, id)
        self.tool = tool

    def work(self):
        return f"Designer {self.name} is designing using {self.tool}."


# Derived class for Testers
class Tester(Employee):
    def __init__(self, name, id, testing_tool):
        super().__init__(name, id)
        self.testing_tool = testing_tool

    def work(self):
        return f"Tester {self.name} is testing using {self.testing_tool}."


# Derived class for Developers
class Developer(Employee):
    def __init__(self, name, id, programming_language):
        super().__init__(name, id)
        self.programming_language = programming_language

    def work(self):
        return f"Developer {self.name} is developing software using {self.programming_language}."


# Abstract base class for Company
class Company(ABC):
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self):
        employee = self.create_employee()
        self.employees.append(employee)

    @abstractmethod
    def create_employee(self):
        pass

    def show_employees(self):
        for employee in self.employees:
            print(employee.work())


# Concrete company subclass that creates specific types of employees
class TechCompany(Company):
    def create_employee(self):
        return Developer("Charlie", 103, "Python")


class DesignCompany(Company):
    def create_employee(self):
        return Designer("Alice", 101, "Adobe XD")


class TestCompany(Company):
    def create_employee(self):
        return Tester("Bob", 102, "Selenium")


# Example usage
if __name__ == "__main__":
    tech_company = TechCompany("Tech Innovators Inc.")
    tech_company.add_employee()
    tech_company.show_employees()

    design_company = DesignCompany("Creative Minds Ltd.")
    design_company.add_employee()
    design_company.show_employees()

    test_company = TestCompany("Quality Assurance Co.")
    test_company.add_employee()
    test_company.show_employees()
