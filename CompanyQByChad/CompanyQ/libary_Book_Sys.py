class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def __str__(self):
        return f"""Title : {self.title}\nAuthor : {self.author}\nIs Available : {'Yes' if self.available else 'No'}"""
    
    def borrow(self):
        if self.available:
            self.available = False
    
    def return_book(self):
        if not self.available:
            self.available = True
            
class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.borrow()
                print(f'You have borrowed "{title}".')
                return
        print(f'"{title}" is not available.')
        
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.return_book()
                print(f'You have returned "{title}".')
                return
        print(f'"{title}" was not borrowed or doesn’t exist.')
                
    
    def list_available_books(self):
        for book in self.books:
            if book.available:
                print(f' - {book.title} by {book.author}')
                
b1 = Book("The Hobbit", "J.R.R. Tolkien")
b2 = Book("1984", "George Orwell")
b3 = Book("Python 101", "John Doe")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.list_available_books()

lib.borrow_book("The Hobbit")
lib.list_available_books()

lib.return_book("The Hobbit")
lib.list_available_books()
