import csv
import mysql.connector as mysql
import os
import dotenv
from pathlib import Path

# Загружаем переменные окружениия
dotenv.load_dotenv() 

# Подключаемся к БД
db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

# Путь к файлу
csv_path = (
    Path(__file__)
    .parent        # Переход в Homework_16
    .parent        # Переход в egor_fortius
    .parent        # Переход в homework
    / 'eugene_okulik'
    / 'Lesson_16'
    / 'hw_data'
    / 'data.csv'
)

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.DictReader(csv_file)
