from random import randint

def random_upper():
    sentence = input("Give me a sentence to make sarcastic: ")
    result = ''

    sentence = sentence.lower()

    for letter in sentence:
        rand = randint(0,10)

        if rand >= 5:
            result += letter.upper()
        else:
            result += letter
        
    return result + "/s"