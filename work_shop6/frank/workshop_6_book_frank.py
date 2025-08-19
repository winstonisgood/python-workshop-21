class Book():#a class of book with basic attributes and methods
    def __init__(self,title, author, isbn, price, stock):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock = stock
    
    def add_stock(self, amount):
        self.stock += amount
    
    def sell_book(self, amount):
        if amount <= self.stock:#compare the amount with stock
            self.stock -= amount
        else:#if amount is larger than stock, stock will be set to 0
            print(f"only {self.stock} to sell")
            self.stock = 0
            
    def display_info(self):
        print(f"dispplay info: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Stock: {self.stock}")

class EBook(Book):
    def __init__(self,title, author, isbn, price, stock,file_format):
        super().__init__(title, author, isbn, price, stock)
        self.file_format = file_format
    
    def set_format(self, file_format):
        self.file_format = file_format

    def display_info(self):
        print(f"dispplay info: Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Stock: {self.stock}, Format: {self.file_format}")

# an inventory class to manage a list of books
# every element in the list is a Book object
class BookInventory(Book):
    #books = []
    def __init__(self, books=[]):
        #super().__init__(self.title, self.author, self.isbn, self.price, self.stock)
        self.books = books
        
    def add_book(self, book):#to add a new book to the inventory list
        for book_element in self.books:#search if the book already exists in the inventory
            if book_element.isbn == book.isbn: #isbn is unique for each book
                print(f"This book isbn:{book.isbn} already exists in the inventory.")
                return
        self.books.append(book)#append the book as a element in the inventory list
    
    def remove_book(self, title):#remove this book permenently
        for book in self.books:
            if book.title == title:# use == to compare the title
                self.books.remove(book)
                print(f"Removed book: {title}")
                return
    
    def add_stock(self, isbn, amount):
        for book in self.books:
            if book.isbn == isbn:
                book.add_stock(amount)
    
    def sell_book(self, isbn, amount):
        for book in self.books:
            if book.isbn == isbn:
                book.sell_book(amount)
    
    def display_inventory(self):
        for book in self.books:
            print(f"Title: {book.title}, inventory: {book.stock}")
        
    def find_book(self,title):
        i = 0
        for book in self.books:
            if title in book.title.lower():
                i += 1
                print(f"Found it: ")
                book.display_info()
        if i == 0:
            print("Not this book in the inventory")

#an instance of BookInventory
book_inventory = BookInventory()

#create an inventory class list and add some books, 
#every book is a Book object in the Inventory List
book1 = Book("1984", "George Orwell", "1234567890", 15.99, 10)
book_inventory.add_book(book1)
book1 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 12.99, 5)
book_inventory.add_book(book1)
book1 = Book("San Guo Yanyi", "luo", "1234", 22, 8)
book_inventory.add_book(book1)
book1 = Book("San Guo Zhi", "cao", "1111", 111, 10)
book_inventory.add_book(book1)
book1 = Book("aaa", "bbb", "2222", 111, 10)
book_inventory.add_book(book1)
book_inventory.display_inventory()

#the latest book1 is "aaa"
#when change the stock in the book1 instance, inventory list is changed as well
book1.add_stock(3)
book1.display_info()
book_inventory.display_inventory()

#change stock in the inventory list by isbn
#add stock into the list by isbn
book_inventory.add_stock("1111", 7)
print("add stock into 1111:")
book_inventory.display_inventory()
#sell book(minus stock from the list) by isbn
book_inventory.sell_book("1234", 15)
print("sell book 1234:")
book_inventory.display_inventory()

#to find a book by title with in title.lower()
book_inventory.find_book("sa")

#remove a book by title with ==
book_inventory.remove_book("aaa")
book_inventory.display_inventory()

ebook = EBook("harry 1", "au1", "888", 25.5, 30, "pdf")
ebook.display_info()
ebook.set_format("bmp")#change format from pdf to bmp
ebook.display_info()

book_inventory.add_book(ebook)#add ebook into the inventory list
book_inventory.display_inventory()
