"""
Problem Statement:
Create a class called `Person` with the following:

Attributes:
- `name` (string): The name of the person.
- `age` (integer): The age of the person.

Method:
- `introduce()`: This method should print:
  "Hi, my name is <name> and I am <age> years old."

After that:
- Create two objects of the `Person` class with different data.
- Call the `introduce()` method for both objects.
"""
# Let us create a class called person


class person:
    def __init__(self, name, age):
        # self.attribute = parameter
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")


# Let me create 2 objects
candidate1 = person("Jeevan Kumar", 26)
candidate2 = person("Jimmy James", 24)

# use the dot operator to access the members of the class
candidate1.introduce()
candidate2.introduce()
