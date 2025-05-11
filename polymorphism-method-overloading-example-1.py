# Author: Abhishek Balaji
# Date of creation: 11-05-2025 / 19:09 PM

# example for method overloading

class hello:

    def __init__(self):  # pass for now
        pass

    def greet(self, name=None):
        if name:
            print(f"Hello, {name} How are you doing today?")
        else:
            print("Hello there!")


# Object creation
person1 = hello()
person2 = hello()

person1.greet("Anil Kumar")
print("\n")
person2.greet()

# Explanation
# When name variable is an empty-string, the else block will be executed.
# If the name variable is filled by a string, the if block will be executed.
