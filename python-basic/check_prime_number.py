'''
Author: Abhishek Balaji
Date of creation: 03-06-2025 / 11:33 AM

Problem Statement 4: Prime Number Checker
Write a Python program that:

Asks the user to enter a positive integer n.

Checks whether n is a prime number or not.

Prints "n is a prime number" if it is prime, or "n is not a prime number" if it is not.

'''

# create a user-defined function to check if a number is prime or not
def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:  # This else belongs to the for-loop, runs only if no break happens
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

# receive user input
num = int(input("enter the number: "))

# check if the number is negative
if num < 0:
    print("enter a positive number only: ")
else:
    check_prime(num)
