# Author: Abhishek Balaji
# Date of creation: 18-05-2025 / 16:50 PM

# Generators 

# create a sequence
just_set = {11.5, 22.3, 98.5, 660, 45.23}

print(type(just_set))

# define the generator function
def generator_function(add_sequence): # add_sequence is a parameter
    for j in add_sequence:
        yield j # return one element at a time

# define a generator function and store it in a variable
next_element = generator_function(just_set)

# use the next() function to get the next element from the generator
print(next(next_element))
print(next(next_element))
print(next(next_element))
print(next(next_element))
print(next(next_element))
