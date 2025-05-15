# Author: Abhishek Balaji
# Date of creation: 15-05-2025 / 12:36 PM

'''
Problem Statement 2: Even Numbers Iterator
Create a custom iterator class named EvenNumbers that takes two integers start and end and iterates over all the even numbers from start up to (and including) end.

If start is odd, start from the next even number.

Once the iterator exceeds end, it should raise a StopIteration.

Use this iterator in a for loop to print all the even numbers in the given range.
'''
class evennumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if self.start % 2 != 0: # If it is odd
            self.start = self.start + 1 # add 1 to it to make it even

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end:   # Once the iterator exceeds end, it should raise a StopIteration.
            raise StopIteration  
        
        result = self.start
        self.start = self.start + 2
        return result
            
        
# object creatiom
myobject = evennumber(1, 10)

# use for loop

for ele in myobject:
    print(ele)

