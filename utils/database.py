import sqlite3

""" This is an interface between our app and data storage mechanism """


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))  # This is the right way to avoid
    # sql injection attack
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]  # we get a list of tuples
    # we could convert it as a list of dict like so
    connection.close()
    return books


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





