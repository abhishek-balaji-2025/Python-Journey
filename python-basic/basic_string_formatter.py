'''
Author: Abhishek Balaji
Date of creation: 03-03-2025 / 10:53 AM

Problem Statement 1:
Write a Python program that does the following:

Stores your name, age, height (in meters), and whether you're a student.

Prints a sentence using all these values in a formatted string.
'''
# Enter details
candidate_name = input("Enter your name: ")
candidate_age = int(input("Enter your age: "))
candidate_height = float(input("Enter your height in meters: "))
student_status = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# display formatted string
print(f"Hello, my name is {candidate_name}, I am {candidate_age} years old, my height is {candidate_height} meters tall, and {student_status}, I am a student.")

