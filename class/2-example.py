#!/usr/bin/env python3

import random
import asyncio

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
    
    def __call__(self, x):
        return self.value * x
    
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
    
    async def async_magic(self):
        await asyncio.sleep(1)
        return f"Async magic with {self.value}"

    async def async_counter(self, n):
        for i in range(n):
            await asyncio.sleep(0.5)
            print(f"Async count {i+1} for {self.value}")

@Exotic
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
    
    # Асинхронная магия
    async def run_async():
        print(await e.async_magic())
        await e.async_counter(3)
    
    asyncio.run(run_async())