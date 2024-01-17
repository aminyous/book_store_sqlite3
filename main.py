from utils import database

print("*** Welcome To The Book Store Console Application ***")

USER_CHOICE = """
ENTER:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()
    selection = input(USER_CHOICE).lower()
    while selection != 'q':
        if selection == 'a':

            prompt_add_book()

        elif selection == 'l':

            list_book()

        elif selection == 'r':

            prompt_read_book()

        elif selection == 'd':
            prompt_delete_book()

        else:
            print("Unknown command. please try again.")

        selection = input(USER_CHOICE).lower()


def prompt_add_book():
    name = input("Enter the book name: ")
    author = input("Enter the book author: ")
    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    if len(books) > 0:
        for index, book in enumerate(books):
            print(f"{index + 1} - Book name : {book['name']}, book author : {book['author']}, read : {book['read']}")
    else:
        print("Book list is empty")


def prompt_read_book():
    name = input("Enter the book name you just finished reading: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Enter the book name to delete: ")
    database.delete_book(name)


menu()
print("*** Good Bye ***")