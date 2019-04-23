from kebac import Kebac
with open("dict.txt") as infile:
    for line in infile:
        word, phonemes = line.split("===")
        phonemes = phonemes.replace("\n", "").split("_")
        for p in phonemes:
            if p not in Kebac.PHONEMES:
                print(p)
                print(word)
                exit()

