'''
Author: Abhishek Balaji
Date of creation: 13-05-2025 / 14:15 PM

📌 Problem Statement:
"Write a Python program that takes 5 numbers from the user, stores them in a list, and then prints the maximum, minimum, and average of those numbers."

🎯 Objective:
This exercise helps you:

Work with Python lists

Accept multiple inputs

Use built-in list functions like max(), min(), sum()

Practice iteration (if done manually)
'''
# Receive user input
user_input = input("Enter any 5 random numbers with spaces in between: ")
list_generated = list(map(int, user_input.split()))

# Validate input length
if len(list_generated) != 5:
    print("Please enter exactly 5 numbers.")
else:
 # User-defined functions
    def check_min(add_list):
        return min(add_list)

    def check_max(add_list):
        return max(add_list)

    def check_sum(add_list):
        return sum(add_list)

    def check_avg(add_list):
        return sum(add_list) / len(add_list)

    # function call
    min_result = check_min(list_generated)
    max_result = check_max(list_generated)
    sum_result = check_sum(list_generated)
    avg_result = check_avg(list_generated)

    print(f"The maximum number from the list is: {max_result}")
    print(f"The minimum number from the list is: {min_result}")
    print(f"The sum of the entire list is: {sum_result}")
    print(f"The average of the entire list is: {avg_result}")
