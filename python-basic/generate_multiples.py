'''
Author: Abhishek Balaji
Date of creation: 13-05-2025 / 14:15 PM

Problem Statement:
"Write a Python program that prints the multiplication table of a number entered by the user (from 1 to 10)."

🎯 Objective:
This exercise will help you:

Understand how to use for loops for repetition

Work with ranges and iteration

Practice formatting output cleanly
'''

# ask the user to enter a number
user_input = int(input("Enter any random number to generate a multiples table: "))

list_of_multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create a user_defined function for it
def generate_multiples(add_number):
    for ele in list_of_multiples:
        product = add_number * ele
        print(f"{add_number} x {ele} = {product}")

# function call
generate_multiples(user_input)

