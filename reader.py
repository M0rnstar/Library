class Reader:
    # Счётчик id читателя
    _id_counter = 1

    def __init__(self, name: str):
        self.id = Reader._id_counter
        Reader._id_counter += 1
        self.name = name
        self.borrowed_books: list[int] = []

    def description(self):
        return f"Читатель: {self.name}, Номер карточки: {self.id}, Список уникальных номеров взятых книг: {self.borrowed_books}"

# Тестирование класса
if __name__ == "__main__":
    reader1 = Reader("Алиса")
    reader1.borrowed_books.append(101)
    reader1.borrowed_books.append(102)
    print(reader1.description())
