import sqlite3

""" This is an interface between our app and data storage mechanism """

books_file = "books.json"


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')  # we put "" around the values so we can put
    # the actual value not the table name
    # This is not the recommanded approach
    connection.commit()
    connection.close()


def get_all_books():

    with open(books_file, "r") as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, "w") as file:
        json.dump(books, file)


def read_book(name):
    books = get_all_books()

    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()

    books = [book for book in books if(book["name"] != name)]

    _save_all_books(books)





