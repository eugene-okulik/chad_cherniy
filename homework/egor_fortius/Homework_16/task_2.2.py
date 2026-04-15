import csv
import mysql.connector as mysql
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

csv_path = Path('/home/egor_f/Projects/chad_cherniy/homework/eugene_okulik/Lesson_16/hw_data/data.csv')

results = {
    'found': 0,
    'not_found': 0,
    'details': []
}

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        # Проверяем полную запись через JOIN
        query = '''
        SELECT
            s.name,
            s.second_name,
            g.title as group_title,
            b.title as book_title,
            sub.title as subject_title,
            l.title as lesson_title,
            m.value as mark_value
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.name = %s
        AND s.second_name = %s
        AND g.title = %s
        AND b.title = %s
        AND sub.title = %s
        AND l.title = %s
        '''

        # Преобразуем оценку
        mark_val = row['mark_value']
        if mark_val == 'OTL':
            mark_val = 5
        elif mark_val == 'ХОР':
            mark_val = 4
        elif mark_val == 'УД':
            mark_val = 3
        elif mark_val == 'НЕУД':
            mark_val = 2

        cursor.execute(query, (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title']
        ))

        db_record = cursor.fetchone()

        if db_record:
            results['found'] += 1
            status = "✅ НАЙДЕНА"
        else:
            results['not_found'] += 1
            status = "❌ НЕ НАЙДЕНА"

        results['details'].append({
            'student': f"{row['name']} {row['second_name']}",
            'status': status
        })

# Вывод результатов
print("=" * 80)
print("РЕЗУЛЬТАТЫ ПРОВЕРКИ ДАННЫХ ИЗ CSV В БАЗЕ ДАННЫХ")
print("=" * 80)

for detail in results['details']:
    print(f"{detail['status']} - {detail['student']}")

print("\n" + "=" * 80)
print(f"ВСЕГО ЗАПИСЕЙ: {results['found'] + results['not_found']}")
print(f"✅ НАЙДЕНО: {results['found']}")
print(f"❌ НЕ НАЙДЕНО: {results['not_found']}")
print("=" * 80)

db.close()
