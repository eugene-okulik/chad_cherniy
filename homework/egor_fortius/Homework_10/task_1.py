def finish_me(func):
    def text_fin(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result
    return text_fin


@finish_me
def example(text):
    print(text)


example('print me')
