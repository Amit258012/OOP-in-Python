"""
Abstract Factory is a creational design pattern that allows you to create families of related objects without specifying their concrete classes. 

It acts as a factory of factories, grouping similar types of object creation.
"""

"""
Scenario:
Imagine we are creating a system that generates different types of shapes (Circle and rectangle) in different colors (Red and Green).
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


class Circle(Shape):
    def draw(self):
        return f"circle"


class Rectangle(Shape):
    def draw(self):
        return f"rectangle"


class Red(Color):
    def fill(self):
        return f"red"


class Green(Color):
    def fill(self):
        return f"green"


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass


class ColorFactory(ABC):
    @abstractmethod
    def fill_color(self):
        pass


class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()


class RectangleFactory(ShapeFactory):
    def create_shape(self):
        return Rectangle()


class RedFactory(ColorFactory):
    def fill_color(self):
        return Red()


class GreenFactory(ColorFactory):
    def fill_color(self):
        return Green()


# Client code
def create_shape_and_color(shape_factory: ShapeFactory, color_factory: ColorFactory):
    shape = shape_factory.create_shape()
    color = color_factory.fill_color()
    print(f"Drawing {color.fill()} {shape.draw()}")
    # print(shape.draw())
    # print(color.fill())


# Creating different combinations
circle_factory = CircleFactory()
rectangle_factory = RectangleFactory()
red_factory = RedFactory()
green_factory = GreenFactory()

# Red Circle
create_shape_and_color(circle_factory, red_factory)

# Green Circle
create_shape_and_color(circle_factory, green_factory)

# Red Rectangle
create_shape_and_color(rectangle_factory, red_factory)

# Green Rectangle
create_shape_and_color(rectangle_factory, green_factory)


"""
Real-world-example :-

1. GUI Toolkits:
Example: A graphical user interface (GUI) framework that supports multiple operating systems like Windows, macOS, and Linux.
Usage: An abstract factory can create GUI components (buttons, checkboxes, text fields) for different operating systems.

2. Database Connection:
Example: A system that needs to support multiple database management systems (DBMS) like MySQL, PostgreSQL, and SQLite.
Usage: An abstract factory can create database connections, queries, and transactions for different DBMS.

3. Cross-Platform Development:
Example: A mobile application that needs to run on both iOS and Android.
Usage: An abstract factory can create platform-specific components like UI elements and navigation logic.

4. Document Generation:
Example: A document processing system that supports various formats like PDF, DOCX, and HTML.
Usage: An abstract factory can create document parsers, renderers, and exporters for different formats.

5. Web Frameworks:
Example: A web framework that can be configured to use different templating engines like Jinja2, Mustache, and Handlebars.
Usage: An abstract factory can create components for different templating engines.

6. Themed Applications:
Example: An application that supports different themes like light mode and dark mode.
Usage: An abstract factory can create UI components styled according to the selected theme.

7. Multilingual Systems:
Example: A software application that needs to support multiple languages.
Usage: An abstract factory can create language-specific components like text labels, error messages, and date formats.

8. Vehicle Manufacturing:
Example: A car manufacturing system that produces different types of cars like SUVs, Sedans, and Trucks.
Usage: An abstract factory can create different components like engines, tires, and bodies for each type of vehicle.

9. Plugin Systems:
Example: A software application that supports plugins or extensions.
Usage: An abstract factory can create plugin-specific components, ensuring compatibility and extensibility.

10. Game Development:
Example: A game that supports different character types (warriors, mages, archers) with unique abilities.
Usage: An abstract factory can create character-specific components like weapons, armor, and skills.

11. Cloud Services:
Example: A cloud platform that integrates with various cloud service providers like AWS, Azure, and Google Cloud.
Usage: An abstract factory can create service-specific components like storage, computing, and networking resources.

12. Report Generation:
Example: A reporting system that generates reports in multiple formats like Excel, PDF, and CSV.
Usage: An abstract factory can create report generators, formatters, and exporters for different output formats.

13. Messaging Systems:
Example: A messaging application that supports different messaging protocols like SMS, Email, and Push Notifications.
Usage: An abstract factory can create message handlers, formatters, and senders for each protocol.

14. E-commerce Platforms:
Example: An e-commerce system that supports different payment gateways like PayPal, Stripe, and Square.
Usage: An abstract factory can create payment processors, validators, and receipt generators for each gateway.

15. AI/ML Model Management:
Example: A machine learning platform that supports different types of models like TensorFlow, PyTorch, and Scikit-learn.
Usage: An abstract factory can create model loaders, trainers, and evaluators for different frameworks.
"""
