#Define a Book Class
#Attributes: title, author, isbn, price, stock
#Methods: display_info(), add_stock(), sell_book()
class Book:
    def __init__(self, title, author, isbn, price, stock):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = price
        self._stock = stock
    
    #display_info method to return book details
    def display_info(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Price: ${self._price:.2f}, Stock: {self._stock}" #:.2f formats the price to two decimal places

    #add_stock method to increase stock
    def add_stock(self, quantity):
        if quantity > 0:
            self._stock += quantity
            return f"Added {quantity} copy/copies of '{self._title}'. New stock: {self._stock}."
        else:
            return "Invalid quantity to add."
    
    #sell_book method to decrease stock
    #Returns a message indicating the sale or lack of stock
    def sell_book(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
            return f"Sold {quantity} copy/copies of '{self._title}'. Remaining stock: {self._stock}."
        else:
            return f"Not enough stock to sell {quantity} copy/copies of '{self._title}'. Current stock: {self._stock}."
        
#Define a Specialized Book Class
#Create a subclass of Book called EBook with an additional attribute for file format (file_format).
class EBook(Book):
    def __init__(self, title, author, isbn, price, file_format):
        #stock initialized to 0 by default as EBooks are often digital and may not have physical stock.
        super().__init__(title, author, isbn, price, stock=float('inf'))  # Use float('inf') to represent unlimited stock
        #Set stock to unlimited for digital books
        self._stock = float('inf')
        self._file_format = file_format
        #Initialize sold attribute to track the number of digital copies sold
        self._sold = 0
    
    #Override the display_info method to include file format
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, unlimited (digital), File Format: {self._file_format}, sold: {self._sold}"
    
    #Override the sell_book method to handle digital sales
    def sell_book(self, quantity=0):
        if quantity > 0:
            self._sold += quantity
            return f"Sold {quantity} digital copy/copies of '{self._title}' (unlimited stock)."
    
    def add_stock(self, quantity):
        return f"EBook '{self._title}' is digital and does not require stock management."

#Create an Inventory Class
#Methods: add_book(), remove_book(), find_book(), display_inventory()
class Inventory:
    def __init__(self):
        #Attributes: books (a list to store Book objects)
        self._books = []
    
    #Method to add a book to the inventory
    def add_book(self, book):
        self._books.append(book)
        return f"Book '{book._title}' added to inventory."
    
    #Method to remove a book from the inventory by title
    def remove_book(self, title):
        for book in self._books:
            if book._title == title:
                self._books.remove(book)
                return f"Book '{book._title}' removed from inventory."
        return f"Book '{book._title}' not found in inventory."
    
    #Method to find a book by title
    def find_book(self, title):
        for book in self._books:
            if book._title == title:
                return book.display_info()
        return f"Book '{book._title}' not found in inventory."
    
    #Method to display all books in the inventory
    def display_inventory(self):
        if not self._books:
            return "Inventory is empty."
        return "\n".join(book.display_info() for book in self._books)

#Main Program
if __name__ == "__main__":
    #Create an instance of Inventory
    inventory = Inventory()
    
    #Add a few books to the inventory
    book1 = Book("The Lord of the Rings", "John Ronald Reuel Tolkien", "9780261103207", 58.09, 50)
    book2 = Book("Think and Grow Rich", "Napoleon Hill & Rosa Lee Beeland", "9781788441025", 20, 12)
    ebook1 = EBook("A Different Kind of Power", "Jacinda Ardern", "9781776951284", 20.99, "ePUB")
    
    print(inventory.add_book(book1))
    print(inventory.add_book(book2))
    print(inventory.add_book(ebook1))
    
    #Display the inventory
    print("\nCurrent Inventory:")
    print(inventory.display_inventory())
    
    #Simulate selling a book and updating the stock
    print("\nSelling a book:")
    print(book1.sell_book(2))  # Sell 2 copies of The Lord of the Rings
    print(inventory.display_inventory())
    
    print("\nSelling an EBook:")
    print(ebook1.sell_book(3))  # Sell 3 digital copies of A Different Kind of Power
    print(inventory.display_inventory())

