# Author: Abhishek Balaji
# Date of creation: 18-05-2025 / 16:33 PM

# Create a sequence
# Create a tuple 
my_tuple = ("apple", "Banana", "kiwi", 0.15, 65, True)

# define the user-defined generator function
def generate_elements(add_sequence): # add_sequence is a parameter
    for items in add_sequence:
        yield items  # return one value at a time, only when called

# mention a user-defined generator function and store it in a variable
gen_elements = generate_elements(my_tuple)

# Use next() function to get the next value from the generator
print(next(gen_elements))
print(next(gen_elements))
print(next(gen_elements))
print(next(gen_elements))
print(next(gen_elements))
print(next(gen_elements))

print(type(my_tuple))


