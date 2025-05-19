# Author: Abhishek Balaji
# Date of creation: 19-05-2025 / 11:50 AM
# Purpose: To demonstrate the use of decorators in Python

# Decorators are useful functions that dictate the behavior of another function.

'''
Step-1: Create a user-defined function
Step-2: Create a decorator function and pass the user-defined function as an argument
Step-3: Define an inner function inside the decorator function
Step-4: Call the user-defined function inside the inner function
Step-5: Return the inner function 
Step-6: Mention @decorator_function_name above the user-defined function
Step-7: Call the user-defined function
Step-8: The decorator function will be called and the inner function will be executed
'''

# create a decorator function
def decorator_display_name(display_name):
    def inner_function():
        print("Displaying the name of users: ")
        display_name()
        print("end of the list")
    return inner_function

# create a user-defined function
@decorator_display_name
def display_names():
    print("John")
    print("Lucas")
    print("Alex")

# function call
display_names()

'''
The reason why we use decorators is to add functionality to an existing function without modifying the existing logic of the function
Let's say you have been composing a critical function that is huge, it is painstaking to demolish everything and start from scratch. Instead, decorators can
be used to extend the functionality of the existing function.
'''
