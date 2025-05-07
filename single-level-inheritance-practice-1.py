'''
Problem Statement:
Create a parent class called Animal that has a method make_sound() which prints a general sound ("Animal makes a sound"). Then, create a child class called Dog that inherits from Animal and overrides the make_sound() method to print "Bark". Create an object of the Dog class and call the make_sound() method.

'''

# Let me create a parent class named animal


class animal:

    # Include the constructor
    def __init__(self):
        pass

    def make_sound(self):
        print("animal makes a sound")

# create a child class named dog


class dog(animal):  # Single level inheritance

    def __init__(self):
        pass

    def make_sound(self):
        print("bark")
        super().make_sound()
        # super() is an inbuilt method that is used to link the child class to the parent class


# Create an object
dog1 = dog()

# use the dot operator to access the members in the class
dog1.make_sound()

''' 
class dog(animal) is used to inherit from parent class to child class
super().method(attribute) mentioned in the child class can access all methods and attributes from the parent class
'''
