## You can find this conversation by searching 'OOP dodecahedron_practice_questions' in GPT-4

## Practice Problems on Python OOP
#-------------------------------------------------------------------------------------------

# OOP Exercise 1: Create a Book Class with Attributes and Methods
# Create a Book class with attributes title, author, and price. Add methods to:

# Display book information.
# Apply a discount to the book price.

# Expected output
# Title: Python Basics, Author: John Doe, Price: 19.99
# Discounted Price: 17.99


# My solution

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def discount(self, deduction):
        self.deduction = deduction
        return self.price - self.deduction

current_read = Book("The Thirty-Nine Steps", "John Buchanan", 11.95)
print("Title:", current_read.title, "Author:", current_read.author, "Price:", current_read.price)
print("Discounted Price", current_read.discount(2.00))

# GPT-4's solution

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def apply_discount(self, deduction):
        self.price -= deduction
        return self.price

current_read = Book("The Little Prince", "Pierre something", 10.99)
print("Title:", current_read.name, "Author:", current_read.author, "Price:", current_read.price)
print("Discounted Price:", current_read.apply_discount(4.00))

# I asked "How would this same class / method work with a percent discount?". This was GPT-4's response:

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def apply_deduction(self, deduction, is_percent=False):
        if is_percent:
            self.price *= 1 - (deduction / 100)
        else:
            self.price -= deduction
        return round(self.price, 2)

current_read = Book("The Old Man and the Sea", "Earnest Hemmingway", 16.14)
print("Title:", current_read.name, "Author:", current_read.author, "Price:", current_read.price)
print("Discounted Price:", current_read.apply_deduction(50, is_percent=True))


## OOP Exercise 2: Class without Attributes and Methods
# Task:
# Create a class called Placeholder that doesn't have any attributes or methods.

# Expected Output:
# <__main__.Placeholder object at 0x7f32f1e4a5b0>

class Placeholder:
    pass

place_holder = Placeholder()
print(place_holder)
print(Placeholder)


## OOP Exercise 3: Inheritance - Create a Magazine Class
# Task:
# Create a Magazine class that inherits from the Book class. Add an attribute for the issue_number.

# Expected Output:
# Title: Python Magazine, Author: Jane Doe, Issue Number: 42

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Magazine(Book):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author, None)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}")

# Create a magazine object
newest_issue = Magazine("Better Eyesight Magazine", "Dr. William Horatio Bates", "September 1925")
newest_issue.display_info()


## OOP Exercise 4: Method Overriding
# Task:
# In the Magazine class, override the method to display book information to also include the issue_number.

# Expected Output:
# Title: Python Magazine, Author: Jane Doe, Issue Number: 42

## (The main difference between Exercise 3 and Exercise 4 lies in method overriding. 
# while Exercise 3 focuses on inheriting attributes from a parent class (Book), 
# Exercise 4 asks you to override a method from the parent class in the child class (Magazine).
#Let's assume that the Book class has a method called display_info() that displays the book's title, author, and price.)

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def diplay_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

class Magazine(Book):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author, None)
        self.issue_number = issue_number

    # Override Book display_info method
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, issue_number: {self.issue_number} ")

newest_mag = Magazine("Better Eyesight Magazines", "Dr William H. Bates", "September 1919")
newest_mag.display_info()


## OOP Exercise 5: Class Attribute
# Task:
# Define a class attribute genre in the Book class with a default value of "Literature".

# Expected Output:
# Genre: Literature, Title: Python Basics, Author: John Doe

class Book:
    genre = "Literature"

    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display_info(self):
        print(f"Genere: {self.genre}, Title: {self.title}, Author: {self.author}")

genre_book = Book("The Great Gatsby", "F. Scott Fitzgeral")
genre_book.display_info()



## OOP Exercise 6: Calculating Costs
# Task:
# For the Book class, add a method that calculates the shipping cost of a book based on its price. 
# Assume the shipping cost is 5% of the book price.

# Expected Output:
# Shipping Cost: 1.0

class Book:
    def __init__(self, title, author, price, genre="Literature"):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre

    def shipping_cost(self):
        shipping = self.price * .05
        return round(shipping, 2)

    def display_info(self):
        print(f"Shipping Cost: {self.shipping_cost()}")

shipped_book = Book("The Ultimate Poe Collection", "Edgar Allen Poe", 40.99)
shipped_book.display_info()


# OOP Exercise 7: Check Object Type
# Task:
# Write a program to determine the class of a given object. For example, find out the class of a Magazine object.

# Expected Output:
# <class '__main__.Magazine'>

class Magazine:
    def __init__(self, title, author, issue):
        self.title = title
        self.author = author
        self.issue = issue
    
    def get_class(self):
        return type(self)

mag = Magazine("Vision Today", "Bill Quapcheck", 145)
print(mag.get_class())

###### Or more simply ###########

print(type(mag))


# OOP Exercise 8: Check Instance
# Determine if a Magazine object is also an instance of the Book class.

print(isinstance(mag, Book))

print(isinstance(shipped_book, Book))

# OOP Exercise 9: Encapsulation
# In the Book class, make the price attribute private and create getter and setter methods for it.

# What is Encapsulation?
# Encapsulation is the practice of restricting access to certain details of an object. Essentially, you're "encapsulating" the internal state of an object and only exposing what is necessary.

# In Python, encapsulation is often implemented using private variables and public methods (getters and setters).

# Private Variables
# In Python, you can indicate that a variable is intended to be private by prefixing it with an underscore _. This is a naming convention to indicate that the variable is for internal use within the class and should not be accessed directly outside of the class.

# Getter and Setter Methods
# Getter and setter methods allow you to control both the retrieval and modification of an attribute's value.

# Here's a simple example using a Book class:

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = round(float(price), 2) # Note the unerscore, making it 'private'
    
    # Getter method for price
    def get_price(self):
        return self._price
    
    # Setter meghod for price
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("must be a positive number")

# Create a book intance
my_book = Book("The Thirty-Nine Steps", "John Buchanan", 14.00)

# Access price via getter
print(f"The price of this book is: ${my_book.get_price():.2f}")

# Set to new price
my_book.set_price(12.00)
print(f"the new book price is: ${my_book.get_price():.2f}")

# Try to set price to negative
my_book.set_price(-3.44)


# OOP Exercise 10: Polymorphism
# Create a method in the Book class called get_type. This should return the string "Book". 
# Then, override this method in the Magazine class to return "Magazine".

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = price

    def get_type(self):
        return "Book"

class Magazine(Book):
    def __init__(self, title, author, issue):
        super().__init__(title, author, None)
        self.issue = issue
    
    def get_type(self):
        return "Magazine"

my_mag = Magazine("Discover", "John Jones Jr.", "May, 2023")

print(my_mag.get_type())