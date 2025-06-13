'''
Author: Abhishek Balaji
Date of creation: 13-05-2025 / 14:15 PM

Concept 4: Strings and String Manipulation
📌 Problem Statement:
"Write a Python program that takes a string from the user and checks whether it is a palindrome (reads the same forward and backward)."

🎯 Objective:
This exercise helps you:

Understand how to handle strings

Use string slicing techniques

Apply basic logic to compare characters
'''

# Receive string input from the user
user_string_input = input("Enter the string: ")

# create a user-defined function
def check_palindrome_eligiblility(add_string):
    # search from the opposite end
    reverse_order = add_string[::-1]
    
    if (add_string == reverse_order):
        print("yes, they match, it is a palindrome")
    else:
        print("no, they do not match, not a palindrome")
            
# function call
check_palindrome_eligiblility(user_string_input)
