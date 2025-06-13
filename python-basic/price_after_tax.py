'''
Author: Abhishek Balaji
Date of creation: 13-05-2025 / 13:50 PM 

Problem Statement:
"You are given the price of a product before tax and the tax percentage. Write a Python program to calculate and print the final price after tax."

🎯 Objective:
This exercise will help you:

Practice variable declaration

Use basic arithmetic operations

Understand the real-world application of expressions
'''

# Receive inputs from the user 
before_tax = float(input("Please enter the price of the product before taxes: "))

# Enter the tax rate in percentage
tax_percentage = int(input("Please enter the tax percentage number: "))

# convert this into float values
float_percentage_rate = tax_percentage / 100.0

# User-defined function to make things simpler
def after_taxation (add_price, add_tax_rate):
   difference_amount = add_price * add_tax_rate
   post_taxation = add_price + difference_amount
   print(f"The post taxation price of the product is {post_taxation}/- only")

# function call

after_taxation(before_tax, float_percentage_rate)
