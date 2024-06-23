from encapsulation import Employee


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return (
            f"Developer('{self.fname}', '{self.lname}', {self.pay}, '{self.prog_lang}')"
        )

    def __str__(self):
        return f"{self.fullName} - {self.email} ({self.prog_lang})"


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
