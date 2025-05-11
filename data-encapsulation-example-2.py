# Author: Abhishek Balaji
# Date of creation: 11-05-2025 / 17:09 PM

'''
Create a class Employee with the following:

Private Attributes:
__name (string) – The name of the employee

__salary (float) – The monthly salary of the employee

Public Methods:
get_employee_info() – Prints the employee's name and salary

update_salary(new_salary) – Updates the employee's salary

apply_bonus(percentage) – Increases salary by the given percentage
'''


class employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_employee_info(self):
        print(f"employee {self.__name}, and salary is {self.__salary}")

    def update_salary(self, new_salary):
        self.__salary = new_salary

    def apply_bonus(self, percentage):
        # Decimal conversion
        decimal_form = percentage / 100.0
        difference_amount = self.__salary * decimal_form
        self.__salary = self.__salary + difference_amount
        print(
            f"The salary hike is {decimal_form} and the end salary is {self.__salary}")


# Object creation
employee1 = employee("David Sang", 85000)
employee2 = employee("Milly Kumar", 75000)

# Use dot operator to access the public methods
employee1.get_employee_info()
employee1.update_salary(95000)
employee1.apply_bonus(7)

print("\n")

# Employee2
employee2.get_employee_info()
employee2.update_salary(100000)
employee2.apply_bonus(6)

print("\n")
