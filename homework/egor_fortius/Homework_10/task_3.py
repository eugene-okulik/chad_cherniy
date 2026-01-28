first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))


def decor(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
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


# Вызов функции
calc_result = calc(first, second)
print("Результат:", calc_result)
