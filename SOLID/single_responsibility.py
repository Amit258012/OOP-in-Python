"""Single responsibility principle"""

# A class should have only one reason to change, meaning that a class should have only one job or responsibility.

# If a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.

# This principle is important because it makes the code easier to implement and change. It also makes the code easier to read and understand.

# purposes :- avoid code duplication and make the code more readable and easier to maintain

# Example 1
"""
This Person class has two jobs:
   i)  Manage the person's details.
   ii) Store the person to the database.
"""


"""
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Person(name = {self.name})"

    @classmethod
    def save(cls, person):
        print(f"Saving {person} to the database")


if __name__ == "__main__":
    p = Person("Amit")
    Person.save(p)
"""

"""
Problem: 
    The Person class has two responsibilities. 
    If the database changes, the Person class needs to change. 
    If the Person class changes, the database needs to change.
    
    If we want to change the database, we need to change the Person class.
"""

"""
solution:- 
    We can separate the responsibilities into two classes. 
    One class will manage the person's properties, and the other class will store the person in the database.
"""

# refactored Correct code


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"


class PersonDB:
    def save(self, person):
        print(f"Saving the {person.name} to the database")


if __name__ == "__main__":
    p = Person("Amit")
    db = PersonDB()
    db.save(p)
