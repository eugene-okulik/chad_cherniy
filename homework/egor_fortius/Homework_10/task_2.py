def repeat_me(func):
    def text_fin(*args, count, **kwargs):
        for i in range(count):
            func(*args, **kwargs)
    return text_fin


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
