from random_upper import random_upper
from vowel_remover import remove_vowels

print("Welcome! Your options are:")
print('''
\nMode 1: Sarcasm Generator
\nMode 2: Vowel Remover
''')

user_input = ''

while True:
    user_input = input("Pick a mode, or say 'exit' to exit!")

    if user_input == 'exit' or user_input == 'Exit':
        print("Goodbye.")
        break

    if user_input == "Mode 1" or user_input == "mode 1" or user_input == "1":
        print(random_upper())
    elif user_input == "Mode 2" or user_input == "mode 2" or user_input == "2":
        print(remove_vowels())
    else:
        print("That's not a mode.")