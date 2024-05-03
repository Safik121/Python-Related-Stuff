class Book:
    def __init__(self, name: str, author: str, isbn: int, price: str) -> None:
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library.")

    def find_book(self, query):
        found_books = []
        for book in self.books:
            if query == book.name or query == str(book.isbn):
                found_books.append(str(book))
        return found_books

    def find_authors_books(self, author):
        author_books = []
        for book in self.books:
            if author == book.author:
                author_books.append(str(book))
        return author_books

    def books_prices_under(self, price):
        affordable_books = []
        for book in self.books:
            if (book.price) < price:
                affordable_books.append(str(book))
        return affordable_books



library = Library()
book1 = Book("Book1", "Author1", 123456789, "20.00")
library.add_book(book1)

#print(library.books[0])
print(library.find_authors_books("Author1"))
