# Classes and Objects – Basics

**Author:** Abhishek Balaji  
**Created on:** Wednesday, May 7, 2025 – 12:46 PM  
**Purpose:** This document summarizes my personal understanding of Python classes and objects, including key concepts like the constructor `__init__`, the `self` keyword, and usage of the dot operator. It serves as both a revision aid and a way for others to review my learning progress.

For example: 

class book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    # This class needs to contain get_book_info() method
    def get_book_info(self):
        # Print the info about the book
        print(
            f"Title: {self.title}, Author: {self.author}, Published Year: {self.year_published}")


# Object creation
book_1 = book("To Kill a Mockingbird", "Harper Lee", 1960)
book_2 = book("Brave New World", "Aldous Huxley", 1932)

# use dot operator to access the members in the class
book_1.get_book_info()
book_2.get_book_info()

Summary:

1. __init__() -> is a constructor that gets automatically initiated whenever an object is created
2. self       -> this keyword allows objects to remember their own values
3. In the code above, self.title is an attribute
4. dot operator . is used to allow the objects to access the members in the class


