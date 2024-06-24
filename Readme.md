# Software Design Patterns and Principles

## Table of Contents

-   [Software Design Patterns and Principles](#software-design-patterns-and-principles)
    -   [Table of Contents](#table-of-contents)
    -   [OOP Basics](#oop-basics)
        -   [Abstraction](#abstraction)
        -   [Encapsulation](#encapsulation)
        -   [Polymorphism](#polymorphism)
        -   [Inheritance](#inheritance)
    -   [UML Diagram Relations](#uml-diagram-relations)
        -   [Association](#association)
        -   [Aggregation](#aggregation)
        -   [Composition](#composition)
        -   [Dependency](#dependency)
    -   [SOLID Principles](#solid-principles)
        -   [Single Responsibility Principle](#single-responsibility-principle)
        -   [Open/Closed Principle](#openclosed-principle)
        -   [Liskov Substitution Principle](#liskov-substitution-principle)
        -   [Interface Segregation Principle](#interface-segregation-principle)
        -   [Dependency Inversion Principle](#dependency-inversion-principle)

## OOP Basics

### Abstraction

-   **Definition**: Hiding complex implementation details and showing only essential features.
-   **Example**: A car's dashboard simplifies driving by providing controls without showing the engine's inner workings.
-   **Key Point**: Focuses on what an object does rather than how it does it.

### Encapsulation

-   **Definition**: Bundling data and methods that operate on the data within a single unit (class).
-   **Example**: A `BankAccount` class hides the balance variable and provides methods to deposit and withdraw money.
-   **Key Point**: Protects data integrity by restricting direct access to some of an object's components.

### Polymorphism

-   **Definition**: The ability of objects to take on many forms.
-   **Types**:
    -   Method Overloading: Same method name, different parameters.
    -   Method Overriding: Subclass method overrides superclass method.
-   **Example**: A `draw()` method can draw different shapes (circle, rectangle) based on the object calling it.
-   **Key Point**: Enables a single interface to represent different underlying forms (data types).

### Inheritance

-   **Definition**: Mechanism by which one class inherits properties and behaviors from another class.
-   **Types**:
    -   Single Inheritance: One class inherits from one superclass.
    -   Multiple Inheritance: One class inherits from multiple superclasses (not supported in Java).
    -   Multilevel Inheritance: A class inherits from a superclass, and another class inherits from that class.
    -   Hierarchical Inheritance: Multiple classes inherit from one superclass.
    -   Hybrid Inheritance: Combination of multiple inheritance types.
-   **Example**: A `Dog` class inherits from an `Animal` class and adds specific behaviors like `bark()`.
-   **Key Point**: Promotes code reusability and establishes a natural hierarchy.

## UML Diagram Relations

### Association

-   **Definition**: A relationship between two classes that are not dependent on each other.
-   **Example**: A `Teacher` can teach multiple `Students`, and students can be taught by multiple teachers.
-   **Key Point**: Represents a "has-a" relationship.

```plaintext
            teaches
[Teacher] <-----------> [Student]
           learns form
```

### Aggregation

-   **Definition**: A special form of association where a class can exist independently of its container.
-   **Example**: A `Library` contains `Books`, but books still exist if the library is destroyed.
-   **Key Point**: Represents a "whole-part" relationship with independent life cycles.

```plaintext
                 has
[Library] < >-----------> [Books]          //It is hallow diamond
```

### Composition

-   **Definition**: A stronger form of aggregation where the contained class cannot exist independently of its container.
-   **Example**: A `House` contains `Rooms`, and if the house is destroyed, the rooms are also destroyed.
-   **Key Point**: Represents a "whole-part" relationship with dependent life cycles.

```plaintext
           contains of
[House] <0>-----------> [Rooms]           //It is filled diamond
```

### Dependency

-   **Definition**: A "uses" relationship between two classes.
-   **Example**: A `Driver` class depends on a `Car` class to drive.
-   **Key Point**: Indicates that a class relies on another class to function.

```plaintext
         depends/uses
[Driver] - - - - - - -> [Car]
```

## SOLID Principles

### Single Responsibility Principle

-   **Definition**: A class should have only one reason to change, meaning it should have only one job or responsibility.
-   **Example**: A `User` class should not handle database operations; a separate `UserRepository` class should manage database interactions.
-   **Key Point**: Improves code maintainability and readability.
-   **Code**:

```Python
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
```

### Open/Closed Principle

-   **Definition**: Software entities should be open for extension but closed for modification.
-   **Example**: Adding new features through inheritance or interfaces without modifying existing code.
-   **Key Point**: Enhances code flexibility and prevents breaking existing functionality.
-   **Code**:

```Python
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
```

### Liskov Substitution Principle

-   **Definition**: Subtypes must be substitutable for their base types without altering the correctness of the program.
-   **Example**: A `Rectangle` class and a `Square` class should work correctly when used interchangeably as a `Shape`.
-   **Key Point**: Ensures that derived classes can replace their base classes without affecting the program.
-   **Code**:

```Python
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"send {message} to {email}")


class SMS(Notification):
    def notify(self, message, phone):
        print(f"send {message} to {phone}")


if __name__ == "__main__":
    notification = SMS()
    notification.notify("Congrats", "amit@gmail.com")

"""


"""
Problem:-
    The Notification class has a notify() method that takes a message and an email address.
    For SMS We require message and Phone number
    we cannot make notify method spicific, we havve to keep in general
"""

"""
Solution:-
    we can make sperate class for person contact
    the notify method only takes message in Notification class
    the subclass like Email and SMS will take care of the type of contact
    NotificationManager take care of sending message
"""
from abc import ABC, abstractmethod


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"send {message} to {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"send {message} to {self.phone}")


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == "__main__":
    contact = Contact("Amit", "amit@gmail.com", "99888766XX")
    email_notification = Email(contact.email)
    sms_notification = SMS(contact.phone)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Congrats")

    notification_manager = NotificationManager(email_notification)
    notification_manager.send("offer letter")
```

### Interface Segregation Principle

-   **Definition**: Clients should not be forced to depend on interfaces they do not use.
-   **Example**: An `IMultiFunctionPrinter` interface should be divided into smaller interfaces like `IPrinter` and `IScanner`.
-   **Key Point**: Promotes the use of fine-grained interfaces that are client-specific.
-   **Code**:

```Python
from abc import ABC, abstractmethod

"""
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
```

### Dependency Inversion Principle

-   **Definition**: High-level modules should not depend on low-level modules; both should depend on abstractions.
-   **Example**: A `Service` class should depend on an interface `ILogger` rather than a concrete `FileLogger` class.
-   **Key Point**: Reduces the coupling between high-level and low-level modules, making the code more modular and easier to maintain.
-   **Code**:

```Python

"""
class FXConverter:
    def convert(self, from_cur, to_cur, amount):
        print(f"{amount} {from_cur} = {amount * 1.3} {to_cur}")
        return amount * 1.3


class App:
    def start(self):
        converter = FXConverter()
        converter.convert("USD", "EUR", 100)


if __name__ == "__main__":
    app = App()
    app.start()
"""

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
```
