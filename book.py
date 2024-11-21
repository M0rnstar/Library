class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.check = True

    def description(self):
        return f"{self.title} by {self.author}, {self.year} year, {self.isbn}, {self.check}"


if __name__ == "__main__":
    list_books = [["Martin Iden", "Jack London", 1909, 1234], [" The Call of Cthulhu", "H. P. Lovecraft", 1928, 1235]]
    for info in list_books:
        book = Book(*info)
        print(book.description())
