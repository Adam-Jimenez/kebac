import string
from kebac import Kebac

def remove_punc(input_str):
    return input_str.translate(str.maketrans('', '', string.punctuation))

with open("phonetic_dict.txt") as infile, open("new.dict", "w") as outfile:
    for ln, line in enumerate(infile, 1):
        word, phonemes = line.split("===")
        stripped_word = remove_punc(word)
        if word != stripped_word:
            outfile.write("===".join([stripped_word, phonemes]))
        outfile.write("===".join([word, phonemes]))

