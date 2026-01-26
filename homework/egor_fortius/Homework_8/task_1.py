import random


def prog():

    salary = int(input('Введите сумму: '))
    bonus = random.choice([True, False])

    if bonus:
        total = salary + random.randint(1, 10000)
    else:
        total = salary

    return f'${total}'


print(prog())
