import io

from removeUnnecessaryChars import removeUnnecessaryChars
from removeStopWords import removeStopwords
from sinhalaStemmer import stemmer

unnecessaryCharsObj = removeUnnecessaryChars()
stopWrdsObj = removeStopwords()
stemmObj = stemmer()


# plainText = unnecessaryCharsObj.removeChars(title)
# finalText = stopWrdsObj.removeStopwords(title)

inputFile = "text"
outputFile = "plainText.txt"

infile = io.open(inputFile, "r", encoding='utf-8').read()
outfile = io.open(outputFile, "w", encoding='utf-8')

text = unnecessaryCharsObj.removeChars(infile)
text = stopWrdsObj.removeStopwords(text)

text = text.lower()
plain = text.split()
stemmObj.stemminig(plain)

for x in plain:
    outfile.write(x)
    outfile.write(u'\u0020')
# plaintext = " ".join(str(x) for x in plain)

# outfile.write(plaintext)
outfile.close()
