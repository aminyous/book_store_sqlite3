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
    try:
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
        connection.commit()
    except sqlite3.IntegrityError:
        print("You just entered a name that does exist, please try again.")
    finally:
        connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]  # we get a list of tuples
    # we could convert it as a list of dict like so
    connection.close()
    return books


def read_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE name=?", (name,))
    connection.commit()
    connection.close()





