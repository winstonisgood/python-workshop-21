# 1. Define a Book Class
# Attributes: title, author, isbn, price, stock
class Book:
    def __init__(self,title,author,isbn,price,stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock = stock
# Methods: display_info(), add_stock(), sell_book()
    def display_info(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"ISBN:{self.isbn}")
        # float-2 decimal places.Currency standard.
        print(f"Price:${self.price:.2f}")
        print(f"Stock:{self.stock} copies")

    def add_stock(self,quantity):
        if quantity > 0:
            self.stock =+ quantity
            print(f"Added: {quantity} copies. Updated stock: {self.stock}")
        else:
            print("Invalid input. Please enter a positive number.")

    def sell_book(self,quantity):
        if quantity > 0:
            if quantity > self.stock:
                print(f"Not enough stock to sell. Only {self.stock} copies in stock.")
            else:
                self.stock -= quantity
                sell_price = self.price * quantity
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
        self.book_lists =[]
# Methods: add_book(), remove_book(), find_book(), display_inventory()
    def add_book(self,book):
        self.book_lists.append(book)
        print(f"Book: {book.title}  added to Inventory.")
    def remove_book(self,isbn):
        for book in self.book_lists:
            if book.isbn == isbn:
                self.book_lists.remove(book)
                print(f"Book:{book.title} is removed from inventory.")
                return 
            else:
                print(f"Can not find the book.")
        return
    def find_book(self,isbn):
        for book in self.book_lists:
            if book.isbn == isbn:
                return book
            else:
                print(f"Can not find the book.") 
        return
    def display_inventory(self):
        for book in self.book_lists:
            book.display_info()          

# 4. Main Program
# Create an instance of Inventory
inventory = Inventory()
# Add a few books to the inventory
book1 = Book("One piece. Vol. 73, Operation Dressrosa","Oda, Eiichirō","9781421576831",27.88,3)
book2 = Book("Hot Desk","Dickerman, Laura","9780241729656",19.99,1)
book3 = Ebook("A little book about fear"," Memory, Jelani","9780241743423",6.99,1,"PDF")
inventory.add_book(book1)
inventory.add_book(book2)
inventory.add_book(book3)
# Display the inventory
inventory.display_inventory()
# Simulate selling a book and updating the stock
selling_book = inventory.find_book("9781421576831")
if selling_book:
    selling_book.sell_book(5)
inventory.display_inventory()

