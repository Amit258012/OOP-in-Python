"""
Implement / Realization:- Realization is a relationship where a class implements an interface.

A bird implements the flyable interface, providing concrete behavior for flying.

[Bird] - - - -|> [Flyable] // Bird can Fly
"""

from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Bird(Flyable):
    def fly(self):
        return "Flying high!"


bird = Bird()
print(bird.fly())  # Output: Flying high!
