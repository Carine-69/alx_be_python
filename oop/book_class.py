class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Creating an instance of the Book class
book1 = Book("1984", "George Orwell", 1949)

# Printing the string representation of the book
print(book1)  # Output: '1984' by George Orwell, published in 1949

# # Printing the official representation of the book
print(repr(book1))  # Output: Book('1984', 'George Orwell', 1949)
#
# # Deleting the instance
del book1
