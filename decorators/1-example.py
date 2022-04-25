def decorator_func(func):
    def wrapper():
        print("Функция обёртка")
        print("Оборачиваемая функция: {}".format(func))
        print("Выполняем обёрнутую функцию")
        func()
        print("Выходим из обёртки")
    return wrapper


@decorator_func
def hello_world():
    print("Hello world!")


hello_world()