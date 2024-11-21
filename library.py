class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def register_reader(self, reader):
        self.readers.append(reader)

    def remove_reader(self, card_number):
        self.readers = [reader for reader in self.readers if reader.card_number != card_number]

    def issue_book(self, card_number, isbn):
        reader = next((r for r in self.readers if r.card_number == card_number), None)
        if not reader:
            print(f"No reader found with {card_number}")
            return

        book = next((b for b in self.books if b.isbn == isbn), None)
        if not book:
            print(f"No book found with {isbn}")
            return

        reader.borrowed_books.append(book)

        book.check = False

    def return_book(self, card_number, isbn):
        reader = next((r for r in self.readers if r.card_number == card_number), None)
        if not reader:
            print(f"No reader found with {card_number}")
            return None

        book = next((b for b in self.books if b.isbn == isbn), None)
        if not book:
            print(f"No books found with {isbn}")
            return None

        book.check = True

        reader.borrowed_books = [b for b in reader.borrowed_books if b.isbn != isbn]

    def search_book(self, keyword=None):
        if not keyword:
            return self.books

        keyword = keyword.lower()
        list_books = [
            b for b in self.books
            if keyword in b.title.lower() or
               keyword in b.author.lower() or
               keyword in str(b.year) or
               keyword in b.isbn
        ]
        return list_books

    def search_reader(self, keyword=None):
        if not keyword:
            return self.readers

        keyword = keyword.lower()
        list_readers = [
            r for r in self.books
            if keyword in r.name.lower() or
               keyword in str(r.card_number)
        ]
        return list_readers
