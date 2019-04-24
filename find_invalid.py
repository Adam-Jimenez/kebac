from kebac import Kebac
with open("dict.txt") as infile:
    for ln, line in enumerate(infile, 1):
        word, phonemes = line.split("===")
        phonemes = phonemes.replace("\n", "").split("_")
        for p in phonemes:
            if p not in Kebac.PHONEMES:
                print(p, word, "line:",ln)

