from random import randint


def shuffle_sentence(user_input = ''):
    if user_input == '':
        original = input("What do you want to scramble? ")
    else:
        original = user_input
    originalArray = original.split(" ")
    shuffledArray = []
    result = ''

    for word in originalArray:
        shuffledArray.append("")

    for word in originalArray:
        index = randint(0, len(originalArray) - 1)

        while shuffledArray[index] != '':
            index = randint(0, len(originalArray) - 1)

        shuffledArray[index] = word

    for word in shuffledArray:
        result += word
        result += " "
    
    return result

    