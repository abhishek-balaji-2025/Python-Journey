# Author: Abhishek Balaji
# Date of creation: 18-05-2025 / 16:11 PM

# Generators are a special type of iterator in Python that allow you to create iterators in a more concise and readable way.

# define a sequence of elements
list_1 = [11, 22, 33, 55, 99]

# user-defined generator function
def generate_element(add_list): # add_list is a parameter
    for ele in add_list:
        yield ele  # return one element at a time, only when called

# create a generator
gen = generate_element(list_1)

# output each element using next()
print(next(gen))
print(next(gen))
print(next(gen))

# Generators and iterators are memory efficient because they store only one value at a time

# Step-1: Create a sequence of elements or add any existing sequence
# Step-2: define a user-defined generator function and store it in a variable
# Step-3: Create a generator using the user-defined generator function
# Step-4: Use the next() function to get the next value from the generator
# Step-5: Repeat step 4 to get the next value from the generator

