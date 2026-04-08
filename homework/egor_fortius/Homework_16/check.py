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

cursor = db.cursor(dictionary=True, buffered=True)

csv_path = Path('/home/egor_f/Projects/chad_cherniy/homework/eugene_okulik/Lesson_16/hw_data/data.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    csv_data = list(reader)

for i, row in enumerate(csv_data, 1):
    print(f"\n{'='*80}")
    print(f"Запись #{i}: {row['name']} {row['second_name']}")
    print(f"{'='*80}")
    
    # 1. Студент
    cursor.execute(
        'SELECT id FROM students WHERE name = %s AND second_name = %s',
        (row['name'], row['second_name'])
    )
    student = cursor.fetchone()
    print(f"Студент: {'✅' if student else '❌'} {row['name']} {row['second_name']}")
    
    # 2. Группа
    cursor.execute(
        'SELECT id FROM `groups` WHERE title = %s',
        (row['group_title'],)
    )
    group = cursor.fetchone()
    print(f"Группа: {'✅' if group else '❌'} {row['group_title']}")
    
    # 3. Книга
    cursor.execute(
        'SELECT id FROM books WHERE title = %s',
        (row['book_title'],)
    )
    book = cursor.fetchone()
    print(f"Книга: {'✅' if book else '❌'} {row['book_title']}")
    
    # 4. Предмет
    cursor.execute(
        'SELECT id FROM subjects WHERE title = %s',
        (row['subject_title'],)
    )
    subject = cursor.fetchone()
    print(f"Предмет: {'✅' if subject else '❌'} {row['subject_title']}")
    
    # 5. Занятие
    cursor.execute(
        '''
        SELECT l.id FROM lessons l
        JOIN subjects s ON l.subject_id = s.id
        WHERE l.title = %s AND s.title = %s
        ''',
        (row['lesson_title'], row['subject_title'])
    )
    lesson = cursor.fetchone()
    print(f"Занятие: {'✅' if lesson else '❌'} {row['lesson_title']}")
    
    # 6. Оценка (с детальной проверкой)
    mark_found = False
    if student and lesson:
        # Конвертируем оценку
        mark_value = row['mark_value']
        mark_map = {'OTL': 5, 'ХОР': 4, 'УД': 3, 'НЕУД': 2}
        mark_int = mark_map.get(mark_value, mark_value)
        
        # Проверяем оценку в БД
        cursor.execute(
            '''
            SELECT id, value FROM marks 
            WHERE student_id = %s AND lesson_id = %s
            ''',
            (student['id'], lesson['id'])
        )
        marks = cursor.fetchall()
        
        if marks:
            print(f"  📊 Найдено оценок у студента на этом занятии: {len(marks)}")
            for m in marks:
                print(f"     - Оценка в БД: {m['value']} (тип: {type(m['value']).__name__})")
                # Сравниваем с приведением типов
                if str(m['value']) == str(mark_int):
                    mark_found = True
                    print(f"     ✅ Совпадение с оценкой из CSV: {mark_value}")
        else:
            print(f"  ⚠️  У студента нет оценок на этом занятии")
    
    print(f"\nОценка: {'✅' if mark_found else '❌'} {row['mark_value']}")
    
    # Итог
    all_found = all([student, group, book, subject, lesson, mark_found])
    print(f"\n{'🎉 ПОЛНОЕ СОВПАДЕНИЕ' if all_found else '⚠️  ЧАСТИЧНОЕ СОВПАДЕНИЕ'}")

db.close()
