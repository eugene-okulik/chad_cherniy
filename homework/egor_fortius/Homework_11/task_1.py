class Book:
    material = "Бумага"
    have_text = True

    def __init__(self, title, author, count_pg, isbn, reserved=False):
        self.title = title
        self.author = author
        self.count_pg = count_pg
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        # Формируем базовую строку
        base = f"Название: {self.title}, Автор: {self.author}, страниц: {self.count_pg}, материал: {self.material}"
        # Добавляем статус резервации, если книга зарезервирована
        if self.reserved:
            return base + ", зарезервирована"
        return base


book1 = Book("Идиот", "Достоевский", 500, "978-5-17-074453-4")
book2 = Book("Мастер и Маргарита", "Булгаков", 480, "978-5-04-097832-1")
book3 = Book("Война и мир", "Толстой", 1225, "978-5-17-074453-6")
book4 = Book("Преступление и наказание", "Достоевский", 672, "978-5-17-074453-7")
book5 = Book("Анна Каренина", "Толстой", 864, "978-5-17-074453-8")

book3.reserved = True

# Выводим информацию о каждой книге
for book in (book1, book2, book3, book4, book5):
    print(book)
