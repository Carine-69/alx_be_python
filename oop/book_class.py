class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author}, was published in {self.year}.'""

    def __del__(self):
        print(f'Deleting {self.author}.')

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


Book1 = Book("self improvement", "Max Milliano", 1998)

print(Book1)

