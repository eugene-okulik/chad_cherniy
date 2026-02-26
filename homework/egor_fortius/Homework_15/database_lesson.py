import mysql.connector as mysql

# подключение к БД
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

"""Запрос 1"""
# Для БД создается переменная cursor, через которое происходит управление
cursor = db.cursor(dictionary=True)    # dictionary=True - получаем данные в виде словаря
cursor.execute('SELECT * FROM students ORDER BY id DESC LIMIT 10')   # Выполняем простой запрос
result = cursor.fetchall()   # Возвращает все результаты запроса, в формате СПИСКА
for student in result:
    print(student['second_name'])

"""Запрос 2"""
cursor.execute('SELECT * FROM students WHERE id=22284')
result2 = cursor.fetchone()    # Если мы знаем, что результат поиска - единственный
print(result2)

"""Запрос с переменными"""
# query = "SELECT * FROM students WHERE name = %s and second_name = %s"
# # Подстановка произойдет в места %s
# cursor.execute(query, (input('name'), input('second_name')))
# print(cursor.fetchall())

"""Запрос на изменение данных"""
# # Если нужно внести изменение данных или создать новый, то следует делать db.commit()
# # Добавляем нового студента
# cursor.execute("INSERT INTO students (name, second_name) VALUES ('Egor2', 'Fortius2')")
# # сохраняем изменения и подтверждаем
# db.commit()

"""Получаем id последнего созданного элемента"""
student_id = cursor.lastrowid
cursor.execute(f'SELECT * FROM students WHERE id={student_id}')
print(student_id)

db.close()   # обязательно отключаться от БД
