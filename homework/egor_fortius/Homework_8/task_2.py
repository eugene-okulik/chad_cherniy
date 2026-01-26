def fibonachi():
    num1 = 0
    num2 = 1

    while True:
        yield num1

        temp = num1 + num2
        num1 = num2
        num2 = temp


def print_numb(n):
    fib_gen = fibonachi()

    for i in range(n):
        val = next(fib_gen)
    return val


print(print_numb(5))
print(print_numb(200))
print(print_numb(1000))
print(print_numb(10000))
