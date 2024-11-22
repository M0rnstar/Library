from library import Library
from reader import Reader
from book import Book

library = Library()

print("-" * 25 + "Добро пожаловать в библиотеку!" + "-" * 25)
while True:
    print("Выберите действие:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Зарегистрировать читателя")
    print("4. Удалить читателя")
    print("5. Выдать книгу")
    print("6. Принять возврат книги")
    print("7. Поиск книги")
    print("8. Поиск читателя")
    print("9. Выйти")

    try:
        ans = int(input())
    except ValueError:
        print("Похоже, вы ввели не целочисленное число. Попробуйте ещё раз")
        continue 

    if ans == 1:
        title = input("Введите название книги: ")
        author = input("Введите имя автора: ")
        year = input("Введите год публикации книги: ")
        library.add_book(Book(title, author, year))
        print("Книга успешно добавлена")
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
        continue
    elif ans == 2:
        try:
            id = int(input("Введите уникальный номер книги: "))
        except ValueError:
            print("Похоже, вы ввели не целочисленное число. Возврат на главный экран")
            continue
        library.remove_book(id)
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
        continue
    elif ans == 3:
        name = input("Введите ФИО читателя: ")
        library.register_reader(Reader(name))
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 4:
        try:
            id = int(input("Введите уникальный номер читателя: "))
        except ValueError:
            print("Похоже, вы ввели не целочисленное число. Возврат на главный экран")
            continue
        library.remove_reader(id)
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 5:
        try:
            card_number = int(input("Введите уникальный номер читателя: "))
            isbn = int(input("Введите уникальный номер книги: "))
        except ValueError:
            print("Похоже, вы ввели не целочисленное число. Возврат на главный экран")
            continue
        library.issue_book(card_number, isbn)
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 6:
        card_number = int(input("Введите уникальный номер читателя: "))
        isbn = int(input("Введите уникальный номер книги: "))
        library.return_book(card_number, isbn)
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 7:
        find_book = input("Введите ключевое слово, либо оставьте поле пустым для получения списка всех книг: ")
        list_book = library.search_book(keyword=find_book)
        if not list_book:
            print("Данная книга не найдена")
        else: 
            for book in list_book:
                print(book.description())
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 8:
        find_reader = input("Введите ключевое слово, либо оставьте поле пустым для получения списка всех читателей: ")
        list_reader = library.search_reader(keyword=find_reader)
        if not list_reader:
            print("Данный читатель не найден")
        else:
            for reader in list_reader:
                print(reader.description())
        input("Нажмите на Enter, чтобы вернуться в меню выбора...")
    elif ans == 9:
        break
    else:
        input("Неккоректный ввод данных. Убедитесь в правильности ввода. Нажмите Enter, чтобы продолжить..")
