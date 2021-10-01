from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def formula(self):
        pass

    def __add__(self, other):
        return self.formula + other.formula


class Coat(Wear):
    def __init__(self, size):
        self.size = size

    @property
    def formula(self):
        return float(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.formula:.2f} кв.м'


class Suit(Wear):
    def __init__(self, growth):
        self.growth = growth

    @property
    def formula(self):
        return float(2 * self.growth + 0.3) / 100

    def __str__(self):
        return f'Расход ткани на костюм: {self.formula:.2f} кв.м'


a = Coat(50)
print(a)
b = Suit(178)
print(b)
print(f'Общий расход ткани: {(a + b):.2f} кв.м')
