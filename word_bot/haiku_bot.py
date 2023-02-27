from sentence_generator import generate_word

def get_syllables(word):
    #referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count

def generate_haiku():
    
    while True:

        word1 = generate_word()
        word2 = generate_word()
        word3 = generate_word()

        line1_syllabels = get_syllables(word1) + get_syllables(word2) + get_syllables(word3)

        if(line1_syllabels == 5):
            break

    line1 = f"{word1} {word2} {word3},\n"

    while True:

        word1 = generate_word()
        word2 = generate_word()
        word3 = generate_word()
        word4 = generate_word()
        word5 = generate_word()

        line2_syllabels = get_syllables(word1) + get_syllables(word2) + get_syllables(word3) + get_syllables(word4) + get_syllables(word5)

        if(line2_syllabels == 7):
            break

    line2 = f"{word1} {word2} {word3} {word4} {word5},\n"

    while True:

        word1 = generate_word()
        word2 = generate_word()
        word3 = generate_word()

        line3_syllabels = get_syllables(word1) + get_syllables(word2) + get_syllables(word3)

        if(line3_syllabels == 5):
            break

    line3 = f"{word1} {word2} {word3}"

    line1 = line1.capitalize()

    haiku = line1 + line2 + line3
    
    file = open("sentences.txt", "a")
    file.write("\n" + haiku)
    file.close()