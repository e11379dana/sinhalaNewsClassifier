import re

class removeUnnecessaryChars():
    def removeChars(self, title):
        cyril = re.compile(u'[\u0021-\u007F]', re.UNICODE)

        plaiText = cyril.sub('', title)

        return plaiText
