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
        base = (f"Название: {self.title}, Автор: {self.author}, страниц: {self.count_pg},"
                f" материал: {self.material}")
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


class SchoolBooks(Book):

    def __init__(self, title, author, count_pg, isbn, subject, klass, has_exercises, reserved=False):
        super().__init__(title, author, count_pg, isbn, reserved)
        self.subject = subject
        self.klass = klass
        self.has_exercises = has_exercises

    def __str__(self):
        school_base = (f"Название: {self.title}, Автор: {self.author}, страниц: {self.count_pg}"
                       f", предмет: {self.subject}, класс: {self.klass}")

        if self.reserved:
            return school_base + ", зарезервирована"
        return school_base


# Создаём несколько экземпляров учебников
school_book1 = SchoolBooks(
    title="Алгебра",
    author="Иванов",
    count_pg=200,
    isbn="978-5-12345-678-9",
    subject="Математика",
    klass=9,
    has_exercises=True
)

school_book2 = SchoolBooks(
    title="История",
    author="Смирнов",
    count_pg=180,
    isbn="978-5-12345-679-0",
    subject="История",
    klass=9,
    has_exercises=True
)

school_book3 = SchoolBooks(
    title="География",
    author="Петров",
    count_pg=150,
    isbn="978-5-12345-680-6",
    subject="География",
    klass=9,
    has_exercises=True
)

school_book4 = SchoolBooks(
    title="Физика",
    author="Сидоров",
    count_pg=220,
    isbn="978-5-12345-681-3",
    subject="Физика",
    klass=9,
    has_exercises=True
)

school_book5 = SchoolBooks(
    title="Биология",
    author="Козлов",
    count_pg=190,
    isbn="978-5-12345-682-0",
    subject="Биология",
    klass=9,
    has_exercises=False
)

school_book4.reserved = True

for school_book in (school_book1, school_book2, school_book3, school_book4, school_book5):
    print(school_book)
