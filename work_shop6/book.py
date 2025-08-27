# 1. Define a Book Class
# Attributes: title, author, isbn, price, stock
class Book:
    def __init__(self,title,author,isbn,price,stock):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = price
        self._stock = stock
    # Safely access without breaking encapsulation
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def isbn(self):
        return self._isbn
    @property
    def price(self):
        return self._price
    @property
    def stock(self):
        return self._stock
    # Methods:display_info()
    def display_info(self):
        print(f"Title:{self._title},Author:{self._author},ISBN:{self._isbn},Price:${self._price},Stock:{self._stock} copies")
    #  add_stock()
    def add_stock(self,quantity):
        if quantity > 0:
            self._stock =+ quantity
            print(f"Added: {quantity} copies. Updated stock: {self._stock}")
        else:
            print("Invalid input. Please enter a positive number.")
    #  sell_book()
    def sell_book(self,quantity):
        if quantity > 0:
            if quantity > self._stock:
                print(f"Not enough stock to sell. Only {self._stock} copies in stock.")
            else:
                self._stock -= quantity
                sell_price = self._price * quantity
                print(f"{quantity} copies sold. Total price is {sell_price}.")
        else:
            print("Invalid input.Please enter a positive number.")

# 2. Define a Specialized Book Class
# Create a subclass of Book called EBook with an additional attribute for file format (file_format).
class Ebook(Book):
    def __init__(self,title,author,isbn,price,stock,file_format):
        super().__init__(title,author,isbn,price,stock)
        self.file_format = file_format
    def display_info(self):
        super().display_info()
        print(f"File Format:{self.file_format}")


# 3. Create an Inventory Class
# Attributes: books (a list to store Book objects)
class Inventory:
    def __init__(self):
        self.books =[]
    # Methods: add_book()  
    def add_book(self,book):
        # do a isbn duplicate check
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print(f"The book with ISBN{book.isbn} is already in the inventory.")
                return
        self.books.append(book)
        print(f"Book: {book._title}  added to Inventory.")
    # remove_book()
    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book:{book.title} is removed from inventory.")
                return 
            else:
                print(f"Can not find the book.")
        return
    # find_book()
    def find_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
            else:
                print(f"Can not find the book.") 
        return
    # display_inventory()
    def display_inventory(self):
        for book in self.books:
            book.display_info()          

# 4. Main Program
# Create an instance of Inventory
inventory = Inventory()
# Add a few books to the inventory
book1 = Book("One piece. Vol. 73, Operation Dressrosa","Oda, Eiichirō","9781421576831",27.88,3)
book2 = Book("Hot Desk","Dickerman, Laura","9780241729656",19.99,1)
book3 = Ebook("A little book about fear"," Memory, Jelani","9780241743423",6.99,1,"PDF")
book4 = Ebook("Test"," Memory, Jelani","9780241743423",6.99,1,"PDF")
inventory.add_book(book1)
inventory.add_book(book2)
inventory.add_book(book3)
# testing for a isbn duplicate check
inventory.add_book(book4)
# Display the inventory
inventory.display_inventory()
# Simulate selling a book and updating the stock
selling_book = inventory.find_book("9781421576831")
if selling_book:
    selling_book.sell_book(2)
inventory.display_inventory()
