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
cursor = db.cursor()
cursor.execute('SELECT * FROM students')    # Выполняем простой запрос
result = cursor.fetchall()   # Возвращает то, что выполнил запрос, в формате списка
print(result)

db.close()   # обязательно отключаться от БД
