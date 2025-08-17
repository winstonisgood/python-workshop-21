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
        super().__init__(title, author, isbn, price, 0)
        #Set stock to unlimited for digital books
        self.stock = float('unlimited')
        self._file_format = file_format
        #Initialize a sold attribute to track the number of digital copies sold
        self._sold = 0
    
    #Override the display_info method to include file format
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, stock: unlimited (digital), File Format: {self._file_format}, sold: {self._sold}"
    
    #Override the sell_book method to handle digital sales
    def sell_book(self, quantity=0):
        if quantity > 0:
            self._sold += quantity
            return f"Sold {quantity} digital copy/copies of '{self._title}' (unlimited stock)."
    
    def add_stock(self, quantity):
        return f"EBook '{self._title}' is digital and does not require stock management."

#Create an Inventory Class


#Main Program


