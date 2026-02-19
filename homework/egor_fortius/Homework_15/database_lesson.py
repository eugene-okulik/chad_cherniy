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
result = cursor.fetchall()   # Возвращает то, что выполнил запрос, в формате списка
for student in result:
    print(student['second_name'])

"""Запрос 2"""
cursor.execute('SELECT * FROM students WHERE id=22284')
result2 = cursor.fetchone()    # Если мы знаем, что результат поиска - единственный
print(result2)

"""Запрос на sql-инъекцию"""


db.close()   # обязательно отключаться от БД
