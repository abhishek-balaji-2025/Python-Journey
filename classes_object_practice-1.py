''' 
Problem Statement:
Create a class named Book that has the following attributes:

title (string): The title of the book.

author (string): The author of the book.

year_published (integer): The year the book was published.

The class should also have the following methods:

get_book_info(): A method that returns a string with the following format:
"Title: <title>, Author: <author>, Published Year: <year_published>"

After that:

Create an object of the Book class, initializing it with appropriate values.

Use the get_book_info() method to print out the details of the book.

'''


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
