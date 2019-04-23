from kebac import Kebac
with open("dict.txt") as infile, open("new.dict.txt", "w") as outfile:
    for line in infile:
        line = line.replace("\"\'", "")
        line = line.replace("\"", "")
        line = line.replace(".", "")
        line = line.replace("_\n", "\n")
        outfile.write(line)
