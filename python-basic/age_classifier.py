'''
Author: Abhishek Balaji
Date_of_creation: 03-06-2025

Problem Statement 2: Age-Based Classification
Write a Python program that:

Asks the user to enter their age.

Based on their age, prints their category:

Below 13 → "You are a child."

13 to 19 (inclusive) → "You are a teenager."

20 to 64 (inclusive) → "You are an adult."

65 and above → "You are a senior citizen."
'''

# create a user-defined function to classify age

def classify_age(age):
    if (age < 13):
        return "you are a child"
    elif (age >= 13 and age <= 19):
        return "you are a teenager"
    elif (age >= 20 and age <= 64):
        return "you are an adult"
    else:
        return " you are a senior citizen"
    
# function call
user_age = int(input("Please enter your age: "))
print(classify_age(user_age))

