# Author: Abhishek Balaji
# Date of creation: 15-05-2025 / 14:33 PM

'''
Create a custom iterator class called EvenNumbers that generates the first N even numbers (starting from 0). Use this iterator in a loop to print the numbers.
'''

# create class even numbers
class evenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0 # current starting point

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.n > 0):
            even = self.current
            self.current = self.current + 2
            self.n = self.n - 1 # only n times backward
            return even
        else:
            raise StopIteration
            
        
# create an object
even_num = evenNumbers(10) # give me 10 even numbers

# Create a for loop to iterate the elements
for x in even_num:
    print("even numbers are: ", x)
    
# Try second case as well, provide a negative number as an argument
# For example: even_num = evenNumbers(-10)
# Output: Iteration is stopped


