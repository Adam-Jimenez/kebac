from unidecode import unidecode
import string

class Kebac:
    PHONEMES = {
        "AH": "a",     # se prononce comme le "A" du mot "Ami"
        "AN": "an",    # se prononce comme le "An" du mot "Chant"
        "B": "b",      # se prononce comme le "B" du mot "Barbe"
        "D": "d",      # se prononce comme le "D" du mot "Dame"
        "DJ": "j",     # se prononce comme le "J" du mot "Jazz"
        "E2": "é",     # se prononce comme le "É" du mot "Élément"
        "EH": "è",    # se prononce comme le "Ai" du mot "Aime"
        "EU": "eu",     # se prononce comme le "E" du mot "Deux"
        "F": "f",      # se prononce comme le "F" du mot "France"
        "G": "g",      # se prononce comme le "G" du mot "Gant"
        "IN": "in",    # se prononce comme le "In" du mot "Sapin"
        "K": "k",      # se prononce comme le "K" du mot "Koala"
        "L": "l",      # se prononce comme le "L" du mot "Langue"
        "M": "m",      # se prononce comme le "M" du mot "Mime"
        "N": "n",      # se prononce comme le "N" du mot "Nappe"
        "OH": "o",     # se prononce comme le "O" du mot "Rock"
        "ON": "on",    # se prononce comme le "On" du mot "Bon"
        "OO": "ou",    # se prononce comme le "Ou" du mot "Amour"
        "OW": "o",     # se prononce comme le "O" du mot "Rose"
        "P": "p",      # se prononce comme le "P" du mot "Pape"
        "R": "r",      # se prononce comme le "R" du mot "Rouge"
        "S": "s",      # se prononce comme le "S" du mot "Soleil"
        "SH": "sh",    # se prononce comme le "SH" du mot "Shiva"
        "T": "t",      # se prononce comme le "T" du mot "Toute"
        "TCH": "tch",  # se prononce comme le "Tch" du mot "Match"
        "U": "u",      # se prononce comme le "U" du mot "Elu"
        "UH": "eu",     # se prononce comme le "E" du mot "Neuf"
        "UN": "un",    # se prononce comme le "UN" du mot "Brun"
        "V": "v",      # se prononce comme le "V" du mot "Vacances"
        "W": "w",      # se prononce comme le "W" du mot "Western"
        "X": "x",      # se prononce comme le "X" du mot "Index"
        "Y": "i",      # se prononce comme le "Y" du mot "Yves"
        "Z": "z",      # se prononce comme le "Z" du mot "Zebre"
        "ZH": "j",     # se prononce comme le "J" du mot "Jour"
    }
    PHONETIC_DICT_PATH="phonetic_dict.txt"
    QC_DICT_PATH="french_qc_dict.txt"
    def __init__(self):
        """
        dictionary has the following format:
        [french_word]: [phoneme1, phoneme2, ...]
        """
        self.load_dict()

    def load_dict(self):
        """
        Parse french-phonetic and french-qc dictionary from text file
        """
        self.phonetic_dict = {}
        self.qc_dict = {}
        with open(self.PHONETIC_DICT_PATH) as phonetic_dict_file, open(self.QC_DICT_PATH) as qc_dict_file:
            for line_number, line in enumerate(phonetic_dict_file, 1):
                word, phoneme = line.split("===")
                phoneme = phoneme.replace("\n", "").split("_")
                self.phonetic_dict[word] = phoneme
            for line in qc_dict_file:
                fr_word, qc_word = line.split("===")
                qc_word = qc_word.replace("\n", "")
                self.qc_dict[fr_word] = qc_word

    def phoneme_to_kebac(self, phonemes):
        """
        Takes a list of phonemes and converts it to a kebac word
        """
        return "".join([self.PHONEMES[phoneme] for phoneme in phonemes])

    def convert_word(self, word):
        """
        Converts a french word into a kebac word
        Strategies applied for conversion:
        1. French-Qc dictionary lookup
        2. Phonetic reduction of the word
        """
        isupper = word.isupper()
        word = word.lower()
        kebac_word = word
        if word in self.qc_dict:
            kebac_word = self.qc_dict[word]
        elif word in self.phonetic_dict:
            phonemes = self.phonetic_dict[word]
            kebac_word = self.phoneme_to_kebac(phonemes)

        if isupper:
            kebac_word = word.upper()
        return kebac_word

    def convert(self,french_words):
        kebac_words = []
        for word in french_words:
            kebac_word = self.convert_word(word)
            no_punc_word = self.remove_punc(word)
            kebac_word2 = self.convert_word(no_punc_word)
            if len(kebac_word2) < len(kebac_word):
                kebac_word = kebac_word2
            punc_to_space_word = " ".join([self.convert_word(w) for w in self.punc_to_space(word).split(" ")])
            if len(punc_to_space_word) < len(kebac_word):
                kebac_word = punc_to_space_word
            kebac_words.append(kebac_word)
        return kebac_words

    def punc_to_space(self, input_str):
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        return input_str.translate(translator)

    def remove_punc(self, input_str):
        return input_str.translate(str.maketrans('', '', string.punctuation))

    def join_letters(self,word):
        new_word = ""
        cnt_since_last_space = 999
        for c in word:
            if c == ' ':
                if cnt_since_last_space > 2:
                    new_word += c
                cnt_since_last_space = 0
            else:
                new_word += c
            cnt_since_last_space += 1
        return new_word


    def convert_input(self, input_str):
        s = unidecode(input_str) # ler quebecois yutilise tu des accents?
        words = s.split()
        kebac_words = self.convert(words)
        kebac_str =  " ".join(kebac_words)
        joined_kebac_str = self.join_letters(kebac_str)
        return joined_kebac_str

    def repl(self):
        """
        Read-eval-print loop for french-kebac conversion
        """
        while(True):
            print(self.convert_input(input()))


if __name__ == "__main__":
    k = Kebac()
    k.repl()

