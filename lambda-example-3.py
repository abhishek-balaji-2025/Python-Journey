'''
Problem 3: String Ends With Vowel
Statement:
Write a lambda function that returns True if a given string ends with a vowel (a, e, i, o, u, case-insensitive), otherwise returns False.
'''

user_input = input("enter any string: ")

result = lambda s: s[-1].lower() in 'aeiou'
print(result(user_input))

