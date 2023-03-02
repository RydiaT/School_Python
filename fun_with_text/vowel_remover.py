vowels = 'AEIOUYaeiouy'

def remove_vowels(user_input = ''):
    if user_input == '':
        sentence = input("What sentence do you want to remove vowels from? ")
    else:
        sentence = user_input
    result = ''

    # This used to be far more complicated, before I realized I was an idiot.

    for letter in sentence:
        if vowels.count(letter) == 0:
            result += letter    
    
    return result