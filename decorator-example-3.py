# Author: Abhishek Balaji
# Date of creation: 19-05-2025 / 12:58 PM

'''
Problem Statement:
Create a decorator named uppercase_decorator that modifies the output of any function returning a string by converting it to uppercase.
Apply this decorator to a function called say_hello() which returns the string "hello world". When called, say_hello() should return the uppercase string "HELLO WORLD".
'''

# define a decorator function
def uppercase_decorator(say_hello):
    def inner_function():
        initial_string = say_hello()
	print(f"original_string: {initial_string}")
        result_string = initial_string.upper()
        print(f"uppercase string: {result_string}")
	return result_string
    return inner_function

# define a user-defined function
@uppercase_decorator
def say_hello():
    return "hello world"

# call the function
say_hello()


