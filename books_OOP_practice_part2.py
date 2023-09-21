# This is a continuation of practice with OOP from ./books_OOP_practice.py. Search GPT-4 for 'OOP dodecahedron_practice_questions'
# to find thread

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def list_books(self):
        for idx, book in enumerate(self.books, start=1):
             print(f"{idx}. {book.title} by {book.author}")


lib = Library()
book1 = Book("For Whom The Bell Tolls", "Ernest Hemmingway")
book2 = Book("The Cook Book", "M. Night Shayamalan")

lib.add_book(book1)
lib.add_book(book2)

print("Books in Library")
lib.list_books()

lib.remove_book(book1)

print("Books in library after removal")
lib.list_books()