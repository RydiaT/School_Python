from random_upper import random_upper

print("Welcome! Your options are:")
print('''
\nMode 1: Sarcasm Generator
''')

user_input = ''

while True:
    user_input = input("Pick a mode, or say 'exit' to exit!")

    if user_input == 'exit' or user_input == 'Exit':
        print("Goodbye.")
        break

    if user_input == "Mode 1" or user_input == "mode 1" or user_input == "1":
        print(random_upper())
    else:
        print("That's not a mode.")