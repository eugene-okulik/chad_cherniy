first = float(input('Введите 1-ое число: '))
second = float(input('Введите 2-ое число: '))


def decor(func):
    def wrapper(first, second):
        # если одно из чисел отрицательное - умножение
        if first < 0 or second < 0:
            operation = '*'
        # если числа равны, то функция calc вызывается с операцией сложения этих чисел
        elif first == second:
            operation = '+'
        # если первое больше второго, то происходит вычитание второго из певрого
        elif first > second:
            operation = '-'
        # если второе больше первого - деление первого на второе
        elif second > first:
            operation = '/'
        else:
            print('Ошибочка')

        result = func(first, second, operation)
        return result
    return wrapper


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return round(first / second, 2)
    else:
        raise ValueError("Неизвестная операция")


result_calc = calc(first, second)
print('Результат:', result_calc)
