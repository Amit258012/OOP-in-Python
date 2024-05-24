# https://www.pythontutorial.net/python-oop/python-open-closed-principle/
# please refer for uml diagram

""" Open Close Principle """

# Class, methods, funtions should be open for extension but closed for modification
# This means that a class should be easily extendable without modifying the class itself.
# This principle is important because it allows us to add new features to an object without modifying the object.
# This principle is important because it makes the code easier to implement and change. It also makes the code easier to read and understand.


"""
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name = {self.name})"


class PersonStorage:
    def save_to_db(self, person):
        print(f"Saving {person} to the database")

    def save_to_json(self, person):
        print(f"Saving {person} to the json file")


if __name__ == "__main__":
    person = Person("Amit")
    storage = PersonStorage()
    storage.save_to_json(person)
    
"""

"""
Problem:- 
    PersonStorage class has two methods:

    The save_to_database() method saves a person to the database.
    The save_to_json() method saves a person to a JSON file.

    later, if you want save in XML, you have to modify the PersonStorage,
    => it is not open for extension it is open for modification.
"""

"""
solution:-

    Design a class so that if you want to save into different format, you can extend the class and add new method.

    Make PersonStorage class, save as abstract method, so if you want to save in different format, you can extend/inherit the class and implement new format method by overriding save method of PersonStorage. 
"""

from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name = {self.name})"


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f"Saving {person} to the database")


class PersonJson(PersonStorage):
    def save(self, person):
        print(f"save {person} to json file")


class PersonXML(PersonStorage):
    def save(self, person):
        print(f"save {person} to XML file")


if __name__ == "__main__":
    p = Person("Amit")
    storage1 = PersonDB()
    storage2 = PersonJson()
    storage3 = PersonXML()
    storage1.save(p)
    storage2.save(p)
    storage3.save(p)
