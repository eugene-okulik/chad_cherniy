import mysql.connector as mysql
import os
import dotenv


dotenv.load_dotenv() # Поиск файла dotenv и использует системные переменные

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

"""Запрос 1 - Добавление студента"""
cursor.execute(
    'INSERT INTO students (name, second_name) VALUES (%s, %s)',
    ('Egor', 'Fortius')
)
db.commit()
student_id = cursor.lastrowid
print(f'Создан студент с ID: {student_id}')

"""Запрос 2 - Добавление книг (executemany)"""
books_data = [
    ('War and Peace', student_id),
    ('Шриланка про макс', student_id)
]
cursor.executemany(
    'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
    books_data
)
db.commit()

"""Запрос 3 - Добавление группы"""
cursor.execute(
    'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)',
    ('Fortius_4 group', 'Feb 2026', 'Apr 2026')
)
db.commit()
group_id = cursor.lastrowid
print(f'Создана группа с ID: {group_id}')

"""Запрос 4 - Обновление группы студента"""
cursor.execute('UPDATE students SET group_id = %s WHERE id = %s', (group_id, student_id))
db.commit()

"""Запрос 5 - Добавление предметов"""
subjects_titles = ['Зельеварение', 'Антизельеварение']
subject_ids = []
for title in subjects_titles:
    cursor.execute('INSERT INTO `subjects` (title) VALUES (%s)', (title,))
    db.commit()
    subject_ids.append(cursor.lastrowid)
print(f'Созданы предметы с ID: {subject_ids}')

"""Запрос 6 - Добавление занятий"""
lessons_data = [
    ('Predmet11', subject_ids[0]),
    ('Predmet12', subject_ids[0]),
    ('Predmet13', subject_ids[1]),
    ('Predmet14', subject_ids[1])
]
lesson_ids = []
for title, subject_id in lessons_data:
    cursor.execute('INSERT INTO lessons (title, subject_id) VALUES (%s, %s)', (title, subject_id))
    db.commit()
    lesson_ids.append(cursor.lastrowid)
print(f'Созданы занятия с ID: {lesson_ids}')

"""Запрос 7 - Добавление оценок (executemany)"""
marks_data = [
    (10, lesson_ids[0], student_id),
    (10, lesson_ids[1], student_id),
    (10, lesson_ids[2], student_id),
    (10, lesson_ids[3], student_id)
]
cursor.executemany(
    'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
    marks_data
)
db.commit()

"""Запрос 8 - Выборка всех оценок студента"""
cursor.execute('SELECT * FROM marks WHERE student_id = %s', (student_id,))
result = cursor.fetchall()
print('\nОценки студента:')
for mark in result:
    print(mark)

"""Запрос 9 - Выборка всех книг студента"""
cursor.execute('SELECT * FROM books WHERE taken_by_student_id = %s', (student_id,))
result = cursor.fetchall()
print('\nКниги студента:')
for book in result:
    print(book['title'])

"""Запрос 10 - Полный отчёт по студенту (JOIN)"""
query = '''
SELECT
    s.name,
    s.second_name,
    g.title AS 'Группа',
    b.title AS 'Книга',
    m.value AS 'Оценка',
    l.title AS 'Занятие',
    sub.title AS 'Предмет'
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = %s
'''
cursor.execute(query, (student_id,))
result = cursor.fetchall()
print('\nПолный отчёт по студенту:')
for row in result:
    print(row)

db.close()
