'''
Problem 1: Cube Calculator
Statement:
Write a lambda function to calculate the cube of a number.
'''

# create a variable to store the lambda function
cube_result = lambda c: c ** 3

user_input = int(input("Enter a number to find the cube of: "))

# print the result of the lambda function
print(f"the cube of the number {user_input} is: ", cube_result(user_input))

