from book import Book
from reader import Reader


class Library:
    def __init__(self, filename1='books.txt', filename2='readers.txt'):
        self.filename1 = filename1
        self.filename2 = filename2
        self.books = self.load_books()
        self.readers = self.load_readers()

# Загрузка данных книг из текстового документа
    def load_books(self):
        books = []
        try:
            with open(self.filename1, 'r', encoding='utf-8') as f:
                for line in f:
                    title, author, year, book_id, status = line.strip().split(',')
                    books.append(Book(title, author, int(year), status))
        except FileNotFoundError:
            print(f"{self.filename1} не найдена. Создаю новый список книг")
        return books

# Сохранение данных книг в текстовый документ
    def save_books(self):
        with open(self.filename1, 'w', encoding='utf-8') as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.year},{book.id},{book.status}\n")

# Загрузка данных читателей из текстового документа
    def load_readers(self):
        readers = []
        try:
            with open(self.filename2, 'r', encoding='utf-8') as f:
                for line in f:
                    name, card_number = line.strip().split(',')
                    readers.append(Reader(name))
        except FileNotFoundError:
            print(f"{self.filename2} не найдена. Создаю новый список читателей")
        return readers

# Сохранение данных читателей в текстовый документ
    def save_readers(self):
        with open(self.filename2, 'w', encoding='utf-8') as f:
            for reader in self.readers:
                f.write(f"{reader.name},{reader.id}\n")

# Добавление кнгиги
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

# Удаление книги
    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()

# Регистрация читателя
    def register_reader(self, reader):
        self.readers.append(reader)
        self.save_readers()

# Удаление читателя по id
    def remove_reader(self, card_number):
        self.readers = [reader for reader in self.readers if reader.card_number != card_number]
        self.save_readers()

# Выдача книги по id читателя и книги
    def issue_book(self, card_number, book_id):
        reader = next((r for r in self.readers if r.id == card_number), None)
        if not reader:
            print(f"Не найден читатель с id: {card_number}")
            return

        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            print(f"Не найдена книга с id: {book_id}")
            return

        if book.status == "выдана":
            print("Данная книга уже выдана")
            return

        reader.borrowed_books.append(book)
        book.status = "выдана"

# Возврат книги по id пользователя и книги 
    def return_book(self, card_number, book_id):
        reader = next((r for r in self.readers if r.id == card_number), None)
        if not reader:
            print(f"Не найден читатель с id: {card_number}")
            return

        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            print(f"Не найдена книга с id: {book_id}")
            return

        if book == "в наличии":
            print("Данная книга уже возвращена")
            return

        if book.id not in reader.borrowed_books:
            print("Данной книги нет у читателя")
            return

        book.status = "в наличии"
        reader.borrowed_books = [b for b in reader.borrowed_books if b.id != book_id]

# Поиск книги по ключевому слову
    def search_book(self, keyword=None):
        if not keyword:
            return self.books

        keyword = keyword.lower()
        list_books = [
            b for b in self.books
            if keyword in b.title.lower() or
               keyword in b.author.lower() or
               keyword in str(b.year) or
               keyword in str(b.id)
        ]

        return list_books
    
# Поиск читателя по ключевому слову
    def search_reader(self, keyword=None):
        if not keyword:
            return self.readers

        keyword = keyword.lower()
        list_readers = [
            r for r in self.readers
            if keyword in r.name.lower() or
               keyword in str(r.id)
        ]
        return list_readers

