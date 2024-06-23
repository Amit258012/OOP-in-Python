from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def call_target(self, name: str):
        pass


class Nokia(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        return "2% battery remaining"

    def call_target(self, name: str):
        return f"calling {name}...."
