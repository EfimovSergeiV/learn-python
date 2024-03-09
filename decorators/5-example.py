#!/usr/bin/env python3

def double_values(cls):
    def wrapper(*args, **kwargs):
        print("Данные из декоратора:", args, kwargs)
        new_args = [8 * i for i in args]
        result = cls(*new_args, **kwargs)
        return result
    return wrapper

@double_values
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def my_method(self):
        return self.x + self.y


print("Создаем экземпляр декорированного класса")
my_instance = MyClass(3, 5)

print("Вызываем метод экземпляра")
result = my_instance.my_method()
print("Результат: ", result)