# Author: Abhishek Balaji
# Date of creation: 11-05-2025 / 17:56 PM

'''
Polymorphism is an important concept in Object-oriented-programming. The main logical principle is that multiple methods with the 
same name can house various commands allowing the objects to react a certain way

There can be multiple methods with the same name but what is present inside the methods determines how the objects will behave

There are 2 types of Polymorphism:
1. Method overriding
2. Method overloading

'''


class cow:

    def __init__(self):
        pass

    def speak(self):  # same method name
        print("Moo")  # actions can be different


class snake:

    def __init__(self):
        pass

    def speak(self):  # same method name
        print("Hiss")  # actions can be different


class tiger:

    def __init__(self):
        pass

    def speak(self):  # same method name
        print("roars")  # actions can be different


# create objects
cow1 = cow()
tiger1 = tiger()
snake1 = snake()

print("\n")

cow1.speak()
snake1.speak()
tiger1.speak()

print("\n")

# Keynote - This is a good example for method overriding
