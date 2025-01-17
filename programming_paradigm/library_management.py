class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        """Returns whether the book is checked out."""
        return self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a new book to the library."""
        self.__books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out by its title."""
        for book in self.__books:
            if book.title == title and not book.is_checked_out():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"'{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Marks a book as returned by its title."""
        for book in self.__books:
            if book.title == title and book.is_checked_out():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self.__books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

