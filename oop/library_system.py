# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize common attributes for all types of books."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book instances."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size."""
        super().__init__(title, author)  # Initialize the base class attributes
        self.file_size = file_size  # Initialize EBook-specific attribute

    def __str__(self):
        """String representation for EBook instances."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Initialize the base class attributes
        self.page_count = page_count  # Initialize PrintBook-specific attribute

    def __str__(self):
        """String representation for PrintBook instances."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (either Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")

    def list_books(self):
        """Print details of all the books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)  # This calls the __str__ method of the book instances
