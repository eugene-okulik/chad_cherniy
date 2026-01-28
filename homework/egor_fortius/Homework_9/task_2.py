temperatures = [
    20, 15, 32, 34, 21, 19, 25,
    27, 30, 32, 34, 30, 29, 25,
    27, 22, 22, 23, 25, 29, 29,
    31, 33, 31, 30, 32, 30, 28, 24, 23
]


list_temp = list(filter(lambda t: t > 28, temperatures))
print(list_temp)

# 2 Находим нужные значения
max_temp = max(list_temp)
min_temp = min(list_temp)
avg_temp = sum(list_temp) / len(list_temp)

# 3 Выводим
print("Самая высокая температура:", max_temp)
print("Самая низкая температура среди жарких дней:", min_temp)
print("Средняя температура:", round(avg_temp, 2))
