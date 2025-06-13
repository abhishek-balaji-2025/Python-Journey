'''
Author: Abhishek Balaji
Date of creation: 13-05-2025 / 14:05 PM

📌 Problem Statement:
"Write a Python program that asks the user to enter their age and determines if they are eligible to vote. (Assume the voting age is 18 or above.)"

🎯 Objective:
This exercise helps you:

Practice if, else logic

Understand decision-making in code

Handle basic input/output operations
'''

# Allow the candidate to enter their age
candidate_input = int(input("Please enter your age: "))

def check_candidate_eligibility(add_age):
    if (add_age < 18 and add_age > 0):
        print("not eligible to vote, candidate needs to be 18 years old or above to vote")
    elif (add_age == 18):
        print("Candidate is eligible to vote, verification required")
    elif (add_age > 18):
        print("candidate is eligible")
    else:
        print("please enter a positive number")

# function call
check_candidate_eligibility(candidate_input)
