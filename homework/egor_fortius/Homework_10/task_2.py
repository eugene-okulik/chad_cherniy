def repeat_me(func):
    def wrapper(*args, count=1, **kwargs):
        for x in range(count):
            func(*args, **kwargs)
    return wrapper


@repeat_me
def example(text):
    print(text)


# вывод
example('print me', count=2)
