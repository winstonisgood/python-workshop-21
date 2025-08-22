class Book():#a class of book with basic attributes and methods
    def __init__(self, title, author, isbn, price, stock):
        """attributes are all protected except stock is private for testing"""
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = price
        self.__stock = stock
    
    def get_stock(self):
        return self.__stock
    
    def add_stock(self, amount):
        if amount < 0:
            return
        self.__stock += amount
    
    def sell_book(self, amount):
        if amount < 0:
            return
        if amount <= self.__stock:#compare the amount with stock
            self.__stock -= amount
        else:#if amount is larger than stock, stock will be set to 0
            print(f"only {self.__stock} to sell")
            self.__stock = 0
            
    def display_info(self):#stock is private
        print(f"dispplay info: Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Price: {self._price}, Stock: {self.get_stock()}")

class EBook(Book):
    def __init__(self,title, author, isbn, price, stock,file_format):
        super().__init__(title, author, isbn, price, stock)
        self.file_format = file_format
    
    def set_format(self, file_format):
        self.file_format = file_format

    def display_info(self):#overwrite this method
        print(f"dispplay info: Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Price: {self._price}, Stock: {self.get_stock()}, Format: {self.file_format}")

# an inventory class to manage a list of books
# every element in the list is a Book object
class BookInventory():
    def __init__(self, books=[]):
        self.books = books
        
    def add_book(self, book):#to add a new book to the inventory list
        for book_element in self.books:#search if the book already exists in the inventory
            if book_element._isbn == book._isbn: #isbn is unique for each book
                print(f"This book isbn:{book.isbn} already exists in the inventory.")
                return
        self.books.append(book)#append the book as a element in the inventory list
    
    def remove_book(self, title):#remove this book permenently
        for book in self.books:
            if book._title == title:# use == to compare the title
                self.books.remove(book)
                print(f"Removed book: {title}")
                return
    
    def add_stock(self, isbn, amount):
        for book in self.books:
            if book._isbn == isbn:
                book.add_stock(amount)
    
    def sell_book(self, isbn, amount):
        for book in self.books:
            if book._isbn == isbn:
                book.sell_book(amount)
    
    def display_inventory(self):
        for book in self.books:
            print(f"Title: {book._title}, inventory: {book.get_stock()}")#stock is private so must be use its method
        
    def find_book(self,title):
        i = 0
        for book in self.books:
            if title in book._title.lower():
                i += 1                      #check value
                print(f"Found it: ")
                book.display_info()#automatically use the overwrited method if it has a more attribute of file_format
                # if isinstance(book, EBook) :#check if it is a ebook
                #     book.ebook_display_info()#print one more attribute:file_format
                # else:                        
                #     book.display_info()#only attributes from parrent class
        if i == 0:
            print("Not this book in the inventory")

#an instance of BookInventory
book_inventory = BookInventory()

#create an inventory class list and add some books, 
#every book is a Book object in the Inventory List
print("--------------create a book inventroy list-----------------")
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

#change stock in the inventory list by isbn
#add stock into the list by isbn
print("-----------------add stock by isbn------------------------")
book_inventory.add_stock("1111", 7)
print("add stock into 1111:")
book_inventory.display_inventory()
#sell book(minus stock from the list) by isbn
print("-----------------sell stock by isbn------------------------")
book_inventory.sell_book("1234", 15)
print("sell book 1234:")
book_inventory.display_inventory()

#to find a book by title with in title.lower()
print("---------find a book by title with in title.lower()-------")
book_inventory.find_book("sa")

#remove a book by title with ==
print("---------remove a book by title with == #------------")
book_inventory.remove_book("aaa")
book_inventory.display_inventory()

#set a Ebook and change its format attribute
print("------#set a Ebook and change its format attribute-----------")
ebook = EBook("harry 1", "au1", "888", 25.5, 30, "pdf")
ebook.display_info()
print("-------change file_format from pdf to bmp---------------")
ebook.set_format("bmp")#change format from pdf to bmp
ebook.display_info()
#append this Ebook into the inventory list
print("------------#append this Ebook into the inventory list--------")
book_inventory.add_book(ebook)#add ebook into the inventory list
book_inventory.display_inventory()
#change this ebook stock
print("------------change this ebook stock---------------------")
book_inventory.sell_book("888", 9)
book_inventory.display_inventory()
#search this Ebook from the list and display its Attribute
print("---------#search this Ebook from the list and display its Attribute------")
book_inventory.find_book("ha")#search if there is a ebook in the list

#git chekout -b Frank-workshop-6
#git branch --set-upstream-to=origin/Frank-workshop-6 Frank-workshop-6
#git pull
#git commit -m "dfdfdfd"
#git push
