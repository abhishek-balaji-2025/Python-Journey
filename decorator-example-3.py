# Author: Abhishek Balaji
# Date of creation: 19-05-2025 / 12:58 PM

'''
Problem Statement:
Create a decorator named uppercase_decorator that modifies the output of any function returning a string by converting it to uppercase. Apply this decorator to a function called say_hello() which returns the string "hello world". When called, say_hello() should return the uppercase string "HELLO WORLD".
'''

initial_string = "hello world"

# define a decorator function
def uppercase_decorator(say_hello):
    def inner_function():
        print(f"original string: {say_hello()}")
        result_string = initial_string.upper()
        print("\n")
        print(f"uppercase string: {result_string}")
    return inner_function

# define a user-defined function
@uppercase_decorator
def say_hello():

    return initial_string

# call the function
say_hello()

