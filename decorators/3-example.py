def bechmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)

            print("Время выполнения функции: {}".format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@bechmark(10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.status_code


webpage = fetch_webpage('https://www.python.org/')
print(webpage)