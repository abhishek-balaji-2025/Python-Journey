# Author: Abhishek Balaji
# Date of creation: 18-05-2025 / 17:20 PM

# Generators

''' Problem Statement:
Create a generator that yields even numbers from a given range
'''

# define the gernerator function
def generate_even_numbers(start, end):
        # check whether the start is even or odd
    if (start % 2 == 0):
        print("start is even")
    else:
        print("start is odd")
        start = start + 1 # if it is odd, make it even
    
    # for loop
    for items in range(start, end+1, 2): # range takes 3 parameters: start, stop, step
        yield items # return one value at a time


# create a generator function and store it in a variable
even_numbers = generate_even_numbers(1, 10)

# use next() function to get the next value from the generator
print(next(even_numbers))
print(next(even_numbers))
print(next(even_numbers))
print(next(even_numbers))


