import mysql.connector as mysql

# подключение к БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Для БД создается переменная cursor, через которое происходит управление
cursor = db.cursor(dictionary=True)

"""Запрос 1 - Добавление студента"""
cursor.execute('INSERT INTO students (name, second_name) VALUES ("Egor3", "Fortius3")')
db.commit()
student_id = cursor.lastrowid   # Получаем ID
print(f'Создан студент с ID: {student_id}')

"""Запрос 2 - Добавление книг"""
cursor.execute('INSERT INTO books (title, taken_by_student_id) VALUES ("War and Peace", %s)', (student_id,))
cursor.execute('INSERT INTO books (title, taken_by_student_id) VALUES ("Шриланка про макс", %s)', (student_id,))
db.commit()

"""Запрос 3 - Добавление группы"""
cursor.execute('INSERT INTO `groups` (title, start_date, end_date) VALUES ("Fortius2 group", "Feb 2026", "Apr 2026")')
db.commit()
group_id = cursor.lastrowid   # Получаем ID новой группы
print(f'Создана группа с ID: {group_id}')

"""Запрос 4 - Обновление группы студента"""
cursor.execute('UPDATE students SET group_id = %s WHERE id = %s', (group_id, student_id))
db.commit()

"""Запрос 5 - Добавление предметов"""
cursor.execute('INSERT INTO `subjects` (title) VALUES ("Fortitutura"), ("Fortianiya")')
db.commit()
subject1_id = cursor.lastrowid   # Получаем ID первого предмета
subject2_id = subject1_id + 1    # Второй предмет будет следующим по ID

"""Запрос 6 - Добавление занятий"""
cursor.execute('INSERT INTO lessons (title, subject_id) VALUES ("Predmet1", %s), ("Predmet2", %s)', (subject1_id, subject1_id))
db.commit()
lesson1_id = cursor.lastrowid
lesson2_id = lesson1_id + 1

cursor.execute('INSERT INTO lessons (title, subject_id) VALUES ("Predmet3", %s), ("Predmet4", %s)', (subject2_id, subject2_id))
db.commit()
lesson3_id = cursor.lastrowid
lesson4_id = lesson3_id + 1

"""Запрос 7 - Добавление оценок"""
cursor.execute('''
    INSERT INTO marks (value, lesson_id, student_id) 
    VALUES (10, %s, %s), (10, %s, %s), (10, %s, %s), (10, %s, %s)
''', (lesson1_id, student_id, lesson2_id, student_id, lesson3_id, student_id, lesson4_id, student_id))
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

"""Запрос 10 - Полный отчёт по студенту"""
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
