# Author: Abhishek Balaji
# Date of creation: 15-05-2025 / 11:37 AM

'''
Problem Statement 1: countdown Iterator
Create a custom iterator class named Countdown that takes a positive integer n and iterates from n down to 1. Once the iterator reaches zero, it should raise a StopIteration exception to end the iteration. Use this iterator to print the countdown numbers in a for loop.
'''
# Custom iterator class Countdown
class countdown:
    def __init__(self, number): # When an object of this class is created, the __init__ method is called with the number parameter.
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 1:
            self.number = self.number - 1
            return self.number
        else:
            raise StopIteration
        
# use objects
countdown_obj = countdown(8)

for ele in countdown_obj:
        print(ele)
