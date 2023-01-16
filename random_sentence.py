import random


def random_sentence():
    # Read file
    f = open("kind_sentences.txt")
    file_lines = f.readlines()

    # Find file length (number of lines/sentences)
    file_len = len(file_lines) - 1

    # Generate a random number in the range of 0 to (number of sentences)
    random_num = random.randint(0, file_len)

    # Choose a random sentence
    random_sentence = (file_lines[random_num])[0:-1] + ", NAME!"

    return random_sentence


