import io

class removeStopwords:
    def removeStopwords(self, text):
        infile = "stopWordList.txt"
        fin = io.open(infile, "r", encoding='utf-8').read()

        # print fin
        text = text.lower()
        words = text.split()
        words.sort()


        for word in words:
            if word in fin:
                text = text.replace(word,"")
                # print text
        return text