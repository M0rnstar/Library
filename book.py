class Book:
    # Счётчик id книги
    _id_counter = 1

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def description(self):
        return f"ID: {self.id} | {self.title} от {self.author}, {self.year} год, Статус: {self.status}"


# Тестирование класса
if __name__ == "__main__":
    list_books = [["Martin Iden", "Jack London", 1909], ["The Call of Cthulhu", "H. P. Lovecraft", 1928]]
    for info in list_books:
        book = Book(*info)
        print(book.description())
