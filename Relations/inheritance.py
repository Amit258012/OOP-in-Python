"""
Inheritance/ generalization:- Inheritance represents an "is-a" relationship where a subclass inherits from a superclass.

[Developer] ----|> [Employee] // Developer is an Employee
"""


class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} is working"


class Developer(Employee):
    def work(self):
        return f"{self.name} is coding"


developer = Developer("Amit")
print(developer.name)  # Output: Amit
print(developer.work())  # Output: Amit is coding
