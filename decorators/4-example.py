#!/usr/bin/env python3


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Данные из декоратора:", args, kwargs )
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator
def my_function(x, y):
    return x + y

result = my_function(3, 5)