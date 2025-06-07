'''
Author: Abhishek Balaji
Date of creation: 07-05-2025 / 19:11 PM

Write a Python program that:

Takes a list of words from the user (input as space-separated values).

Checks if any word in the list starts with a capital letter.

If such a word is found, print "Found capitalized word: <word>" where <word> is the first one found.

If no words start with a capital letter, print "No capitalized words found."

Use a for-else loop in your solution.
'''
# Takes a list of words from the user (input as space-separated values)
user_generated_words = input("Enter random words with spaces seperated: ").split()
print(user_generated_words)

# Checks if any word in the list starts with a capital letter.
def check_capital_letter(add_words):
    for words in user_generated_words:
        if words and words[0].isupper():
            print(f"Found capitalized word: {words}")
            break
    else:
        print("No capitalized words found.")
    
# function call
check_capital_letter(user_generated_words)
