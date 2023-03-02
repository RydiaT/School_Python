vowels = 'AEIOUaeiou'

def remove_vowels():
    sentence = input("What sentence do you want to remove vowels from? ")
    result = ''

    # This used to be far more complicated, before I realized I was an idiot.

    for letter in sentence:
        if vowels.count(letter) == 0:
            result += letter    
    
    return result