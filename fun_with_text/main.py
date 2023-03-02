from random_upper import random_upper
from vowel_remover import remove_vowels
from sentence_shuffle import shuffle_sentence
from random import randint

print("Welcome! Your options are:")
print('''
\nMode 1: Sarcasm Generator
\nMode 2: Vowel Remover
\nMode 3: Shuffle Sentence
\nMode 4: Let us decide!
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
    elif user_input == "Mode 3" or user_input == "mode 3" or user_input == "3":
        print(shuffle_sentence())
    elif user_input == "Mode 4" or user_input == "mode 4" or user_input == "4":
        r = randint(0, 10)

        if r > 6:
            bungalo = random_upper()
            bungalo = remove_vowels(bungalo)
            bungalo = shuffle_sentence(bungalo)
            print(bungalo)
        elif r == 5:
            bungalo = remove_vowels()
            bungalo = shuffle_sentence(bungalo)
            bungalo = random_upper(bungalo)
            print(bungalo)
        elif r == 2:
            bungalo = shuffle_sentence()
            bungalo = shuffle_sentence(bungalo)
            bungalo = shuffle_sentence(bungalo)
            bungalo = remove_vowels(bungalo)
            bungalo = random_upper(bungalo)
            print(bungalo)
        else:
            bungalo = random_upper()
            bungalo = remove_vowels(bungalo)
            bungalo = shuffle_sentence(bungalo)
            print(bungalo)

    else:
        print("That's not a mode.")