'''
Author: Abhishek Balaji
Date of creation: 03-06-2025 / 11:18 AM

Problem Statement 3: Sum of Even Numbers
Write a Python program that:

Asks the user to enter a positive integer n.

Calculates the sum of all even numbers from 2 up to n (inclusive).

Prints the result.
'''

end_point = int(input("enter a positive end point number: "))

def sum_of_even_numbers(n):
    sum = 0
    for even in range(2, end_point + 1, 2):
        print (even)
        sum = sum + even
    return sum
    
# function call
print(f"The total sum of all even numbers is: ", sum_of_even_numbers(end_point))

