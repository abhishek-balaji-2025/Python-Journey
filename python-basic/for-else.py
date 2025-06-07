'''
Author: Abhishek Balaji
Date of creation: 07-05-2025 / 18:51

Write a Python program that:

Takes a list of integers from the user (input as space-separated values).

Checks if the list contains any even number.

If an even number is found, print "Even number found: x" where x is the first even number found.

If no even numbers are found, print "No even numbers in the list".

Use a for-else loop to solve this.
'''

# get input from the user

user_input = input("enter the list of integers (space seperated): ")

# convert those strings into single integers
numbers = user_input.split()
print(f"the list of integers is: {numbers}")

# check if the list contains any even number
# I will be using a for loop to iterate through the list

for elements in numbers:
    elements = int(elements)
    if (elements % 2 == 0):
        print(f"Even number found: {elements}")
        break
else:
    print("No even numbers in the list")

