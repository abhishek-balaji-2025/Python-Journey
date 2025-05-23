'''
Author: Abhishek Balaji
Date of creation: 23-05-2025 / 12:17 PM

Problem: Convert Celsius to Fahrenheit
📄 Statement:
You are given a list of temperatures in Celsius.
Use a lambda function with map() to convert each temperature to Fahrenheit.
Use the formula:
'''

# Fahrenheit = (Celsius * 9/5) + 32

# create a list of temperatures in celsius
temperatures_readings = [0, 20, 37, 100]

fahrenheit_readings = lambda celsius: (celsius * 1.8) + 32
print(f" fahrenheit readings are as follows: ", list(map(fahrenheit_readings, temperatures_readings)))


