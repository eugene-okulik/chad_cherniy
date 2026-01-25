first = 'результат операции: 42'
second = 'результат операции: 514'
third = 'результат работы программы: 9'

print(int(first.split()[-1]) + 10)
print(int(second.split()[-1]) + 10)
print(int(third.split()[-1]) + 10)


# Обработка first
id_el = first.index(':')
num = int(first[id_el + 2:])
print(num + 10)

# Обработка second
id_el = second.index(':')
num = int(second[id_el + 2:])
print(num + 10)

# Обработка third
id_el = third.index(':')
num = int(third[id_el + 2:])
print(num + 10)
