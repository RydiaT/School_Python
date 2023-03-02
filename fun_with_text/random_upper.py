from random import randint

def random_upper(user_input = ''):
    if user_input == '':
        sentence = input("Give me a sentence to make sarcastic: ")
    else:
        sentence = user_input
    result = ''

    sentence = sentence.lower()

    for letter in sentence:
        rand = randint(0,10)

        if rand >= 5:
            result += letter.upper()
        else:
            result += letter
        
    return result + "/s"