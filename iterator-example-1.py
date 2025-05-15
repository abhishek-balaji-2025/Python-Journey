# Author: Abhishek Balaji
# Date of creation: 15-05-2025 / 11:37 AM
# Description: This script demonstrates the use of iterators in Python.

# Iterators practice set

# 1. Create an iterator from a list and use the next() function to iterate through the elements.

# Existing sequence
mylist = [11, 22, 55, 63, 88, 99]

# creating an iterator object 
# using iter() function
# iter() function returns an iterator object
test_iterators =  iter(mylist)

# using next() function
print(next(test_iterators))  # output: 11
print(next(test_iterators))  # output: 22
print(next(test_iterators))  # output: 55
print(next(test_iterators))  # output: 63

# Summary: Iterators are used when one wants precise control over the iteration process.

# Keynote: Iterators are memory efficient cause they store only one value at a time making them suitable for large datasets.

# next() function is used to give the user the control over the iteration process.



