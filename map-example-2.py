'''
Author: Abhishek Balaji
Date of creation: 23-05-2025 / 12:32 PM

Problem: Length of Words
📄 Statement:
You are given a list of words.
Use a lambda function with map() to compute the length of each word.
'''

list_of_words = ["apple", "airplane", "vaporizer", "grenade", "motorcycle", "computer"]

length_of_words = lambda word: len(word)

print("length of each word is as follows: ", list(map(length_of_words, list_of_words)))

