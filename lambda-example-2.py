'''
Author: Abhishek Balaji
Date of creation: 23-05-2025 / 11:49 AM

Problem 2: Maximum of Two Numbers
Statement:
Write a lambda function that returns the greater of two numbers.
'''

largest_number = lambda x,y: x if x > y else y # mention an expression not a statement
# Test cases
print(largest_number(10, 20))  # Output: 20
