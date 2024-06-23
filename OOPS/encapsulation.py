class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_employees += 1

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # use to create factory methods
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split("-")
        pay = int(pay)
        return cls(fname, lname, pay)

    # use for utility functions
    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)

    def __repr__(self):
        return f"Employee('{self.fname}', '{self.lname}', {self.pay})"

    def __str__(self):
        return f"{self.fullName} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay
