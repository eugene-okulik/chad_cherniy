import os
from datetime import datetime, timedelta
from pathlib import Path

# Определение пути относительно текущего скрипта
file_path = (
    Path(__file__)
    .parent        # Переход в Homework_13
    .parent        # Переход в egor_fortius
    .parent        # Переход в homework
    / 'eugene_okulik'
    / 'hw_13'
    / 'data.txt'
)

with open(file_path, 'r', encoding='utf-8') as data_file:
    now = datetime.now()
    for line in data_file.readlines():
        date = line[3:29]
        dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        if '1. ' in line:
            # Действие для даты №1: прибавить 7 дней
            result = dt + timedelta(weeks=1)
            print(f"1. {dt} -> {result} (прибавили 1 неделю)")
        elif '2. ' in line:
            # Действие для даты №2: вывести день недели
            weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
            weekday = weekdays[dt.weekday()]
            print(f"2. {dt} -> {weekday} (день недели)")
        else:
            delta = now - dt
            print(
                f"3. {dt} -> {abs(delta.days)} дней назад"
                if delta.days > 0 else f"3. {dt} -> через {abs(delta.days)} дней")
