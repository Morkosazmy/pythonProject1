#Magic Methods
#add, less than, greater than, equals, string, contains, get item


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    #String
    def __str__(self):
        return f"'{self.title}' by {self.author} : {self.num_pages} pages."
    #<
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    #==
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    #>
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    #+
    def __add__(self, other):
        return self.num_pages + other.num_pages

    # in
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    #getter
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"'{key}' NOT FOUND!"



book1 = Book("Harry Potter and the philosopher's stone", "J.K Rowling", 213)
book2 = Book("Harry potter and the chamber of secrets","J.K Rowling", 320)
book3 = Book("The Hobbit", "J.R.R Tolkein", 280)
book4 = Book("Harry Potter and the philosopher's stone", "J.K Rowling", 213)

print(book1) #str
print(book2) #str
print(book3) #str
print(book4) #str

print(book1 == book4) #eq
print(book1 == book2) #eq
print(book1 < book3) #lt
print(book1 > book3) #gt
print(book1) #str
print("Harry" in book1) #contains
print(book2 + book3) #add
print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['hooligans'])