""" Liskov Substitution Principle """

# The Liskov Substitution Principle states that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.
# Write super class code such that it can be easily overridded
# That requires the objects of your subclasses to behave in the same way as the objects of your superclass.
# The Liskov Substitution Principle is important because it ensures that the code is flexible and easy to maintain.
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
