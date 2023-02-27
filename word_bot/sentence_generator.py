from nltk.corpus import brown
from random import choice as randidx
from random import randint
storage_txt = 'word_bot\sentences.txt'

word_list = brown.words()
punctuation = [".", "!", "?"]
banned_words = [",", ".", "!", "''", "``", "(", ")", "--", "?", ":", ":"]

def generate_word():
    word = randidx(word_list)

    while banned_words.__contains__(word):
        word = randidx(word_list)

    return word


def generate_sentences():
        
    num_words = randint(3, 20)

    sentence = ''

    i = 0

    while(i < num_words):

        word = generate_word()

        sentence += word

        if(i != num_words - 1):
            sentence += " "

        i += 1

    sentence += randidx(punctuation)
    result = sentence.capitalize()

    file = open(storage_txt, "a")
    file.write("\n" + result)
    file.close()