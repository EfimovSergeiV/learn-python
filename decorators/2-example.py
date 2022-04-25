

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        print(args, '\n', kwargs)
        end = time.time()
        print("Время выполнения функции: {}".format(end - start))
        return return_value
    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.status_code


webpage = fetch_webpage('https://www.python.org/')
print(webpage)