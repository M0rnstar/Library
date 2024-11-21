class Reader:
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number
        self.borrowed_books = []

    def desc_reader(self):
        return f"{self.name} {self.card_number}"
