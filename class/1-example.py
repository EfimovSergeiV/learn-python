#!/usr/bin/env python3

import random
from functools import wraps



class MetaWeird(type):
    def __new__(cls, name, bases, dct):
        dct["meta_magic"] = lambda self: f"Meta-magic of {self.__class__.__name__}!"
        return super().__new__(cls, name, bases, dct)


class BaseA:
    def feature_a(self):
        return "Feature A activated!"


class BaseB:
    def feature_b(self):
        return "Feature B engaged!"


class Exotic(BaseA, BaseB, metaclass=MetaWeird):
    def __init__(self, value):
        self.value = value
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Exotic decoration with {self.value}!")
            return func(*args, **kwargs)
        return wrapper

    def __getitem__(self, index):
        return f"Item {index}: {self.value}"
    
    def __setitem__(self, index, value):
        print(f"Setting item {index} to {value}")
    
    def __repr__(self):
        return f"Exotic<{self.value}>"
    
    @staticmethod
    def random_greet():
        return random.choice(["Hello!", "Bonjour!", "Hola!", "Ciao!"])
    
    @classmethod
    def from_double(cls, number):
        return cls(number / 2)


@Exotic(42)
def magic_function():
    return "This function is now exotic!"



if __name__ == "__main__":
    e = Exotic(42)
    print(e.feature_a())
    print(e.feature_b())
    print(e.meta_magic())
    print(e(3))  # Вызов экземпляра как функции
    print(e[5])  # Доступ по индексу
    e[5] = "Mystery"
    print(e)
    print(Exotic.random_greet())
    print(Exotic.from_double(84))
    print(magic_function())