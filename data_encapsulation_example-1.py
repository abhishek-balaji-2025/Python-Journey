# Author: Abhishek Balaji
# Date of creation: 11-05-2025 / 16:35

# Data abstraction is a concept that hides non-essential details and shows only essential features to the user.
# Data encapsulation is the concept of binding data and the methods that operate on it within a class, and
# restricting direct access from outside the class.

class Car:
    # Constructor called automatically when a new object is created
    def __init__(self, make, model, year):
        self.__make = make       # private attribute
        self.__model = model     # private attribute
        self.__year = year       # private attribute

    def get_car_info(self):
        print(
            f"The car is {self.__make}, model is {self.__model}, and year is {self.__year}")

    def update_model(self, new_model):
        # public method to update private model attribute
        self.__model = new_model

    def update_year(self, new_year):
        # public method to update private year attribute
        self.__year = new_year


# Create objects
car1 = Car("Ferrari", "F40", 2021)
car2 = Car("Porsche", "959", 1986)

# Use public methods
car1.get_car_info()
car1.update_model("F80")
car1.get_car_info()

car2.get_car_info()
car2.update_year(2023)
car2.update_model("Carrera GT")
car2.get_car_info()

# How to apply encapsulation in Python:
# Step 1: Mark sensitive data as private using double underscores (__)
# Step 2: Use public methods to read or update the private data
# Step 3: Access the object via public methods using the dot operator

# Note: In Python, private attributes/methods use double underscores like __method_name or __attribute
