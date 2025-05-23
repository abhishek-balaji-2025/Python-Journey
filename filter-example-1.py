'''
Author: Abhishek Balaji
Date of creation: 23-05-2025 / 13:02 PM

Problem: Filter Positive Numbers
📄 Statement:
Given a list of numbers (which can be positive, negative, or zero),
use a lambda function with filter() to create a new list containing only the positive numbers (greater than zero).
'''

list_of_numbers = [1, -55, 98, 101, 0, -87, -21]

positive_numbers_only = lambda v: v > 0

print(f" positive numbers from the given list are as follows: ", list(filter(positive_numbers_only, list_of_numbers)))

