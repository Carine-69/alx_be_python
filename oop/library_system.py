class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.books = []

class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.File_size = file_size

class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author) 
        self.page_count = page_count

    def add_book(self,book):
        self.book = book

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self,book):
        if isinstance(book,Book):
            self.books.append(book)
        else:
            print("Only instance of Book,EBook,printBook can be added")

    def list_books(self):
        if not self.books:
            print("The Library has no books")
        else:
            for book in self.books:
                print(book)