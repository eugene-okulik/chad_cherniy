import csv
import mysql.connector as mysql
import os
import dotenv
from pathlib import Path

# Загружаем переменные окружения
dotenv.load_dotenv()

# Подключаемся к БД
db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True, buffered=True)

# Путь к файлу CSV
csv_path = (
    Path(__file__)
    .parent        # Homework_16
    .parent        # egor_fortius
    .parent        # homework
    / 'eugene_okulik'
    / 'Lesson_16'
    / 'hw_data'
    / 'data.csv'
)

# Чтение CSV
with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_data = list(csv_reader)

print(f"📄 Записей в файле: {len(csv_data)}")
print("=" * 80)

# Проверка каждой записи из CSV
for i, row in enumerate(csv_data, 1):
    print(f"\nЗапись #{i} из CSV:")
    print(f"   Студент: {row['name']} {row['second_name']}")
    print(f"   Группа: {row['group_title']}")
    print(f"   Книга: {row['book_title']}")
    print(f"   Предмет: {row['subject_title']}")
    print(f"   Занятие: {row['lesson_title']}")
    print(f"   Оценка: {row['mark_value']}")

    # 1. Проверяем студента
    cursor.execute(
        'SELECT id, name, second_name FROM students WHERE name = %s AND second_name = %s',
        (row['name'], row['second_name'])
    )
    student = cursor.fetchone()

    # 2. Проверяем группу
    cursor.execute(
        'SELECT id FROM `groups` WHERE title = %s',
        (row['group_title'],)
    )
    group = cursor.fetchone()

    # 3. Проверяем книгу
    cursor.execute(
        'SELECT id FROM books WHERE title = %s',
        (row['book_title'],)
    )
    book = cursor.fetchone()

    # 4. Проверяем предмет
    cursor.execute(
        'SELECT id FROM subjects WHERE title = %s',
        (row['subject_title'],)
    )
    subject = cursor.fetchone()

    # 5. Проверяем занятие
    cursor.execute(
        '''
        SELECT l.id FROM lessons l
        JOIN subjects s ON l.subject_id = s.id
        WHERE l.title = %s AND s.title = %s
        ''',
        (row['lesson_title'], row['subject_title'])
    )
    lesson = cursor.fetchone()

    # 6. Оценка
    mark = None
    if student and lesson:
        mark_value = row['mark_value']

        cursor.execute(
            '''
            SELECT m.id, m.value
            FROM marks m
            WHERE m.student_id = %s AND m.lesson_id = %s AND m.value = %s
            ''',
            (student['id'], lesson['id'], mark_value)
        )
        mark = cursor.fetchone()
        print(mark)

    # Вывод результатов проверки
    print("\n   🔍 Результаты проверки:")
    print(f"   Студент: {'✅ найден' if student else '❌ не найден'}")
    print(f"   Группа: {'✅ найдена' if group else '❌ не найдена'}")
    print(f"   Книга: {'✅ найдена' if book else '❌ не найдена'}")
    print(f"   Предмет: {'✅ найден' if subject else '❌ не найден'}")
    print(f"   Занятие: {'✅ найдено' if lesson else '❌ не найдено'}")
    print(f"   Оценка: {'✅ найдена' if mark else '❌ не найдена'}")

    # Итог по записи
    all_found = all([student, group, book, subject, lesson, mark])
    if all_found:
        print(f"\n   🎉 Запись #{i} ПОЛНОСТЬЮ найдена в БД!")
    else:
        print(f"\n   ⚠️  Запись #{i} найдена НЕ ПОЛНОСТЬЮ или отсутствует")

    print("-" * 80)

# Общая статистика
print(f"\n📊 ВСЕГО ЗАПИСЕЙ: {len(csv_data)}")

db.close()
