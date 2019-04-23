import re

class Kebac:
    PHONEMES = {
        "AH": "a",     # se prononce comme le "A" du mot "Ami"
        "UH": "e",     # se prononce comme le "E" du mot "Neuf"
        "EU": "e",     # se prononce comme le "E" du mot "Deux"
        "E2": "e",     # se prononce comme le "E" du mot "Element"
        "OH": "o",     # se prononce comme le "O" du mot "Rock"
        "OW": "o",     # se prononce comme le "O" du mot "Rose"
        "U": "u",      # se prononce comme le "U" du mot "Elu"
        "Y": "i",      # se prononce comme le "Y" du mot "Yves"
        "AN": "an",    # se prononce comme le "An" du mot "Chant"
        "EH": "ai",    # se prononce comme le "Ai" du mot "Aime"
        "IN": "in",    # se prononce comme le "In" du mot "Sapin"
        "ON": "on",    # se prononce comme le "On" du mot "Bon"
        "OO": "ou",    # se prononce comme le "Ou" du mot "Amour"
        "L": "l",      # se prononce comme le "L" du mot "Langue"
        "M": "m",      # se prononce comme le "M" du mot "Mime"
        "N": "n",      # se prononce comme le "N" du mot "Nappe"
        "B": "b",      # se prononce comme le "B" du mot "Barbe"
        "D": "d",      # se prononce comme le "D" du mot "Dame"
        "DJ": "j",     # se prononce comme le "J" du mot "Jazz"
        "ZH": "j",     # se prononce comme le "J" du mot "Jour"
        "F": "f",      # se prononce comme le "F" du mot "France"
        "G": "g",      # se prononce comme le "G" du mot "Gant"
        "K": "k",      # se prononce comme le "K" du mot "Koala"
        "P": "p",      # se prononce comme le "P" du mot "Pape"
        "R": "r",      # se prononce comme le "R" du mot "Rouge"
        "S": "s",      # se prononce comme le "S" du mot "Soleil"
        "SH": "sh",    # se prononce comme le "SH" du mot "Shiva"
        "T": "t",      # se prononce comme le "T" du mot "Toute"
        "TCH": "tch",  # se prononce comme le "Tch" du mot "Match"
        "V": "v",      # se prononce comme le "V" du mot "Vacances"
        "W": "w",      # se prononce comme le "W" du mot "Western"
        "X": "x",      # se prononce comme le "X" du mot "Index"
        "Z": "z",      # se prononce comme le "Z" du mot "Zebre"
    }
    def __init__(self):
        """
        dictionary has the following format:
        [french_word]: [phoneme1, phoneme2, ...]
        """
        self.dictionary = self.load_dict("dict.txt")

    def load_dict(self, file):
        """
        Parse french-phonetic dictionary from text file
        """
        dictionary = {}
        with open(file) as dict_file:
            for line_number, line in enumerate(dict_file, 1):
                word, phoneme = line.split("===")
                phoneme = phoneme.replace("\n", "").split("_")
                # if word in dictionary:
                #     print("Error:", word, "already in dictionary. Line number: ", line_number)
                # else:
                dictionary[word] = phoneme
        return dictionary

    def phoneme_to_kebac(self, phonemes):
        """
        Takes a list of phonemes and converts it to a kebac word
        """
        return "".join([self.PHONEMES[phoneme] for phoneme in phonemes])

    def convert(self,french_words):
        """
        Converts a list of french words into a list of kebac words
        """
        kebac_words = []
        for word in french_words:
            if word in self.dictionary:
                phonemes = self.dictionary[word]
                kebac_word = self.phoneme_to_kebac(phonemes)
                kebac_words.append(kebac_word)
            else:
                kebac_words.append(word)
        return kebac_words

    def repl(self):
        """
        Read-eval-print loop for french-kebac conversion
        """
        while(True):
            input_str = input()
            words = input_str.split()
            kebac_words = self.convert(words)
            print(" ".join(kebac_words))


if __name__ == "__main__":
    k = Kebac()
    k.repl()

