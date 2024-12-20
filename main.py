#Aggregation
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books ]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# We created a class for book and a library class as well
# we need to create some books and print them.
library = Library("NY Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkein")
book3 = Book("The Color Of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())

for book in library.books:
    print(f"Book's name : {book.title} , Book's Author : {book.author}")