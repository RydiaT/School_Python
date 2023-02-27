from sentence_generator import generate_sentences
from haiku_bot import generate_haiku


print("Mode 1: 5 Random Sentences\nMode 2: 1 Random Haiku")
mode = input("Mode 1 or Mode 2?")

while not mode == "stop":
    if mode == 'Mode 1' or mode == '1':
        j = 0
        while(j < 5):
            generate_sentences()
            j += 1
        print("Check sentences.txt for your sentences!")
    elif mode == 'Mode 2' or mode == '2':
        generate_haiku()
        print("Check sentences.txt for your haiku!")
    else:
        print("Not a valid mode.")

    file = open("sentences.txt", "a")
    file.write("\n")
    file.close()

    print("Mode 1: 5 Random Sentences\nMode 2: 1 Random Haiku")
    mode = input("Mode 1 or Mode 2?")

print("Goodbye.")