first = 'результат операции: 42'
second = 'результат операции: 514'
third = 'результат работы программы: 9'


def my_func(one_str):
    print(int(one_str.split()[-1]) + 10)


my_func(first)
my_func(second)
my_func(third)
