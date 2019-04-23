from kebac import Kebac
with open("dict.txt") as infile, open("new.dict.txt", "w") as outfile:
    for line in infile:
        # word, phonemes = line.split("===")
        # phonemes = phonemes.replace("\n", "").split("_")
        # phonemes = [p if p != 'I' else 'K' for p in phonemes]
        # phonemes = '_'.join(phonemes)
        # outfile.write(word+"==="+phonemes+'\n')

        # line = line.replace("\"\'", "")
        # line = line.replace("\"", "")
        # line = line.replace("'", "")
        # line = line.replace("--", "")
        # line = line.replace("D:", "DJ")
        # line = line.replace("DD", "DJ")
        # line = line.replace("_\n", "\n")
        # line = line.replace("LAH", "L_AH")
        outfile.write(line)
