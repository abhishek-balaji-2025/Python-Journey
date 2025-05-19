# Author: Abhishek Balaji
# Date of creation: 19-05-2025 / 12:35 PM
# Purpose: To create a decorator that calculates the execution time of a function

'''
Create a decorator named execution_time that calculates and displays the time taken by a user-defined function to execute. Apply this decorator to a function named greet()
'''
import time

# define a decorator function
def decorator_greet_people(greet_people):
    def inner_function():
        start = time.time()
        greet_people()
        end = time.time()
        execution_time = end - start
        print(f"Execution time: {execution_time} seconds, that was quick! huh?")
    return inner_function

# random names
name_1 = "Johnny Smith"
name_2 = "Mary Jane"
name_3 = "Peter Parker"
name_4 = "Bruce Wayne"

# Define a user-defined function
@decorator_greet_people
def greet_people():
    print(f"Hello, Mr. {name_1}. I hope you are doing well.")
    print("\n")
    print(f"Good Everning, Ms. {name_2}. How are you?")
    print("\n")
    print(f"Good Morning, Mr. {name_3}. Give me rent!")
    print("\n")
    print(f"Good morning master {name_4}. Is it going to be lamborghini or the batmobile?")
    print("\n")

# function call
greet_people()

'''
Note to remember:
Step-1: define a user-defined function
Step-2: define a decorator function and pass the user-defined function as an argument
Step-3: Create an inner function inside the decorator function
Step-4: call the user-defined function inside the inner function
Step-5: return the inner function
Step-6: Use the @decorator_function_name above the user-defined function
Step-7: Call the user-defined fucntion
'''


